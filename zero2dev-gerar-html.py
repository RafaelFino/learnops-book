#!/usr/bin/env python3
"""Converte os módulos do curso 'De Zero a Dev' em HTML imprimível com capa, sumário e quebras de página.

Uso:
  python3 gerar-livro-html.py              # Gera o HTML (com validação prévia)
  python3 gerar-livro-html.py --validate   # Apenas valida (ortografia + code fences), sem gerar
  python3 gerar-livro-html.py --fix        # Corrige ortografia automaticamente e depois gera
  python3 gerar-livro-html.py --no-check   # Gera sem validação prévia
"""
import re, html as H, os, glob, sys

# Diretório base: onde este script está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Conteúdo do livro fica em Zero2Dev/ (relativo ao BASE_DIR)
CONTENT_DIR = os.path.join(BASE_DIR, 'Zero2Dev')

# ─── Definição da estrutura do livro ───────────────────────────────────────────

CAPITULOS = {
    1: {
        "titulo": "Fundamentos da Computação",
        "descricao": "Antes de programar, você precisa entender o que é um computador, como ele funciona e por que as coisas são como são.",
    },
    2: {
        "titulo": "Sistemas Operacionais e Linux",
        "descricao": "Linux é o sistema operacional que roda a maior parte da internet.",
    },
    3: {
        "titulo": "Terminal e Linha de Comando",
        "descricao": "O terminal é a ferramenta mais poderosa de um desenvolvedor.",
    },
    4: {
        "titulo": "Controle de Versão com Git",
        "descricao": "Git é como uma máquina do tempo para o seu código.",
    },
    5: {
        "titulo": "Lógica de Programação e Algoritmos com Python",
        "descricao": "Aqui começa a programação de verdade.",
    },
    6: {
        "titulo": "Virtualização, Containers e Docker",
        "descricao": "Empacotando e rodando código em ambientes isolados.",
    },
    7: {
        "titulo": "Estruturas de Dados com C",
        "descricao": "Entendendo como dados são organizados na memória.",
    },
    8: {
        "titulo": "Bancos de Dados e Projeto CRUD",
        "descricao": "Modelando, armazenando e consultando informações.",
    },
    9: {
        "titulo": "Programação Orientada a Objetos com .NET/C#",
        "descricao": "Organizando código em sistemas grandes.",
    },
    10: {
        "titulo": "Arquitetura de Software e Estrutura de Soluções",
        "descricao": "Estruturando aplicações de verdade.",
    },
    11: {
        "titulo": "Integração de Sistemas e APIs",
        "descricao": "Como serviços se comunicam entre si.",
    },
    12: {
        "titulo": "Boas Práticas e Carreira em Tecnologia",
        "descricao": "Conceitos, práticas e posturas que fazem a diferença.",
    },
    13: {
        "titulo": "Projeto Final: TCC",
        "descricao": "Consolidando tudo em um projeto completo.",
    },
}

PROJETOS = {
    5: "Zero2Dev/projects/projeto-cap05-programa-python.md",
    6: "Zero2Dev/projects/projeto-cap06-docker.md",
    7: "Zero2Dev/projects/projeto-cap07-estrutura-dados-c.md",
    8: "Zero2Dev/projects/projeto-crud.md",
    9: "Zero2Dev/projects/projeto-biblioteca.md",
    10: "Zero2Dev/projects/projeto-cap10-arquitetura.md",
    11: "Zero2Dev/projects/projeto-crud-fastapi.md",
    13: "Zero2Dev/projects/projeto-tcc.md",
}


# ─── Regex para remover emojis e ícones ───────────────────────────────────────

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"  # Misc Symbols, Emoticons, etc.
    "\U00002702-\U000027B0"  # Dingbats
    "\U0000FE00-\U0000FE0F"  # Variation Selectors
    "\U0000200D"             # Zero Width Joiner
    "\U000024C2-\U0001F251"  # Enclosed chars
    "\U0001FA00-\U0001FA6F"  # Chess symbols
    "\U0001FA70-\U0001FAFF"  # Symbols extended
    "\U00002600-\U000026FF"  # Misc symbols
    "\U00002300-\U000023FF"  # Misc technical
    "]+",
    flags=re.UNICODE
)

def strip_emojis(text):
    """Remove emojis e ícones Unicode do texto."""
    return EMOJI_RE.sub('', text)


# ─── Funções de conversão Markdown → HTML ─────────────────────────────────────

def ifmt(t):
    """Formata inline markdown: bold, italic, strikethrough, code, links, checkboxes."""
    # Inline code: escapar HTML DENTRO dos backticks
    def code_replace(m):
        inner = H.escape(m.group(1))
        return f'<code>{inner}</code>'
    t = re.sub(r'`([^`]+)`', code_replace, t)
    # Bold, italic, strikethrough
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'~~(.+?)~~', r'<del>\1</del>', t)
    # Links: externos mostram URL por extenso (livro impresso), internos viram texto puro
    def link_replace(m):
        text, url = m.group(1), m.group(2)
        # Links internos: âncoras, .md, relativos — viram texto puro (sem link)
        if url.startswith('#') or url.endswith('.md') or url.startswith('cap') or url.startswith('../'):
            return text
        # Link externo: mostrar URL por extenso
        if text == url:
            return f'<a href="{url}">{text}</a>'
        return f'<a href="{url}">{text}</a> <span class="url-print">({url})</span>'
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_replace, t)
    # Checkboxes
    t = t.replace('[x]', '<span class="check-done">[x]</span>')
    t = t.replace('[ ]', '<span class="check-todo">[ ]</span>')
    # Strip emojis
    t = strip_emojis(t)
    return t


def mkid(t):
    """Gera um ID HTML a partir de um título."""
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', t.lower())
    s = re.sub(r'\s+', '-', s.strip())
    return re.sub(r'-+', '-', s)


def md2html(lines):
    """Converte linhas de markdown em HTML."""
    out = []
    i = 0
    n = len(lines)
    while i < n:
        L = lines[i]

        # Filtrar linhas de navegação entre módulos (não fazem sentido no livro)
        if re.match(r'^\s*\[?[←→]', L) or '← Voltar' in L or '← Anterior' in L or 'Próximo:' in L or 'Próximo →' in L:
            i += 1
            continue

        # Mermaid blocks: ```mermaid → <div class="mermaid">
        mf_mermaid = re.match(r'^(`{3,})mermaid\s*$', L)
        if mf_mermaid:
            fence_str = mf_mermaid.group(1)
            i += 1
            mermaid_lines = []
            while i < n:
                if lines[i].rstrip() == fence_str or lines[i].startswith(fence_str):
                    i += 1
                    break
                mermaid_lines.append(lines[i])
                i += 1
            mermaid_content = '\n'.join(mermaid_lines)
            out.append(f'<div class="mermaid">\n{mermaid_content}\n</div>')
            continue

        # Existing <div class="mermaid"> blocks
        if '<div class="mermaid">' in L:
            buf = []
            depth = 0
            while i < n:
                buf.append(lines[i])
                if '<div' in lines[i]:
                    depth += 1
                if '</div>' in lines[i]:
                    depth -= 1
                    if depth <= 0:
                        i += 1
                        break
                i += 1
            out.append('\n'.join(buf))
            continue

        # Script tags: skip
        if '<script' in L:
            i += 1
            continue

        # Code fence (non-mermaid)
        mf = re.match(r'^(`{3,})(\w*)', L)
        if mf:
            fence_str = mf.group(1)
            lang = mf.group(2)
            cls = f' class="language-{lang}"' if lang else ''
            i += 1
            code_lines = []
            while i < n:
                if lines[i].rstrip() == fence_str or lines[i].startswith(fence_str):
                    i += 1
                    break
                code_lines.append(H.escape(lines[i]))
                i += 1
            out.append(f'<pre><code{cls}>' + '\n'.join(code_lines) + '</code></pre>')
            continue

        # Header
        mh = re.match(r'^(#{1,6})\s+(.+)$', L)
        if mh:
            lv = len(mh.group(1))
            tx = strip_emojis(mh.group(2).strip())
            aid = mkid(tx)
            out.append(f'<h{lv} id="{aid}">{ifmt(tx)}</h{lv}>')
            i += 1
            continue

        # HR
        if re.match(r'^-{3,}\s*$', L):
            out.append('<hr/>')
            i += 1
            continue

        # Table
        if '|' in L and L.strip().startswith('|') and L.strip().endswith('|'):
            rows = []
            while i < n and '|' in lines[i] and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
                i += 1
            if len(rows) >= 2:
                t = '<table><thead><tr>'
                for c in rows[0]:
                    t += f'<th>{ifmt(c)}</th>'
                t += '</tr></thead><tbody>'
                for row in rows[2:]:
                    t += '<tr>'
                    for c in row:
                        t += f'<td>{ifmt(c)}</td>'
                    t += '</tr>'
                t += '</tbody></table>'
                out.append(t)
            continue

        # UL (com suporte a indentação)
        if re.match(r'^\s*[-*]\s', L):
            items = []
            while i < n and re.match(r'^\s*[-*]\s', lines[i]):
                indent = len(lines[i]) - len(lines[i].lstrip())
                c = re.sub(r'^\s*[-*]\s', '', lines[i])
                if indent >= 2:
                    items.append(f'<li class="nested">{ifmt(c)}</li>')
                else:
                    items.append(f'<li>{ifmt(c)}</li>')
                i += 1
            out.append('<ul>' + '\n'.join(items) + '</ul>')
            continue

        # OL
        if re.match(r'^\s*\d+\.\s', L):
            items = []
            while i < n and re.match(r'^\s*\d+\.\s', lines[i]):
                c = re.sub(r'^\s*\d+\.\s', '', lines[i])
                items.append(f'<li>{ifmt(c)}</li>')
                i += 1
            out.append('<ol>' + '\n'.join(items) + '</ol>')
            continue

        # Blockquote
        if L.startswith('>'):
            bq = []
            while i < n and lines[i].startswith('>'):
                bq.append(lines[i][1:].strip())
                i += 1
            out.append(f'<blockquote><p>{ifmt(" ".join(bq))}</p></blockquote>')
            continue

        # Empty
        if L.strip() == '':
            i += 1
            continue

        # Paragraph
        out.append(f'<p>{ifmt(L)}</p>')
        i += 1

    return '\n'.join(out)


# ─── CSS do livro ─────────────────────────────────────────────────────────────

CSS = r"""
@page { size: A4; margin: 2.5cm 2cm 2.5cm 2.5cm; @bottom-center { content: counter(page); font-family: 'JetBrains Mono',monospace; font-size: 9pt; color: #888; } }
@page :first { @bottom-center { content: none; } }
*{box-sizing:border-box}
body{font-family:'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif;font-size:11pt;line-height:1.7;color:#1a1a1a;margin:0;padding:0;background:#fff}

/* Capa */
.cover{page-break-after:always;display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:92vh;text-align:center;padding:4cm 2cm;background:linear-gradient(135deg,#111 0%,#1a1a1a 50%,#111 100%);color:#fff}
.cover h1{font-size:36pt;color:#fbbf24;margin-bottom:.2em;border:none;letter-spacing:2px;font-family:'JetBrains Mono','Fira Code',monospace;font-weight:700}
.cover .subtitle{font-size:14pt;color:#a3a3a3;font-style:italic;margin-bottom:2em;max-width:80%;line-height:1.8;font-family:'Inter',sans-serif}
.cover .author{font-size:13pt;color:#e5e5e5;margin-bottom:.5em}
.cover .version{font-size:10pt;color:#737373;margin-top:2em}
.cover .line{width:40%;height:2px;background:linear-gradient(90deg,transparent,#fbbf24,transparent);margin:1.5em auto}

/* Prefácio e Introdução */
.preface{page-break-after:always;padding:2em 0}
.preface h2{font-size:20pt;color:#1a1a1a;border-bottom:2px solid #fbbf24;padding-bottom:.3em;margin-bottom:1em}
.preface p{text-align:justify;margin:.8em 0;line-height:1.8}

/* Sumário */
.toc{page-break-after:always;padding-top:2em}
.toc h2{font-size:20pt;text-align:center;margin-bottom:1.5em;border:none;color:#1a1a1a}
.toc .toc-chapter{font-size:11pt;font-weight:bold;color:#1a1a1a;margin-top:1.2em;margin-bottom:.3em;padding-bottom:.2em;border-bottom:1px solid #fbbf24;font-family:'JetBrains Mono',monospace}
.toc .toc-entry{display:flex;justify-content:space-between;align-items:baseline;padding:.12em 0 .12em 1.2em;font-size:9.5pt}
.toc .toc-entry a{color:#1a1a1a;text-decoration:none}
.toc .toc-entry a:hover{color:#b45309}
.toc .toc-dots{flex:1;border-bottom:1px dotted #d4d4d4;margin:0 .5em;min-width:2em}
.toc .toc-project{font-style:italic;color:#737373}

/* Quebras de página */
.page-break{page-break-before:always}

/* Cabeçalhos de capítulo */
h1.chapter-header{font-size:24pt;color:#1a1a1a;border-bottom:3px solid #fbbf24;padding-bottom:.3em;margin-top:0;margin-bottom:.5em;font-family:'JetBrains Mono','Fira Code',monospace;font-weight:700}
h1.chapter-header .chapter-desc{display:block;font-size:11pt;font-weight:normal;color:#737373;font-style:italic;margin-top:.3em}

/* Cabeçalhos de módulo */
h1.module-header{font-size:20pt;color:#1a1a1a;border-bottom:2px solid #fbbf24;padding-bottom:.2em;margin-top:0;margin-bottom:.8em}

/* Cabeçalhos gerais */
h1{font-size:20pt;color:#1a1a1a;border-bottom:2px solid #fbbf24;padding-bottom:.2em;margin-top:1.5em;font-family:'JetBrains Mono','Fira Code',monospace;font-weight:700}
h2{font-size:15pt;color:#292929;border-bottom:1px solid #e5e5e5;padding-bottom:.2em;margin-top:1.5em;font-family:'Inter',sans-serif;font-weight:600}
h3{font-size:13pt;color:#1a1a1a;margin-top:1.2em;font-family:'Inter',sans-serif;font-weight:600}
h4{font-size:11pt;color:#404040;margin-top:1em;font-weight:600;font-family:'Inter',sans-serif}
h5{font-size:10pt;color:#525252;margin-top:.8em}
h6{font-size:9.5pt;color:#737373;margin-top:.6em}

/* Texto */
p{margin:.6em 0;text-align:justify;orphans:3;widows:3}
a{color:#b45309;text-decoration:none}
a:hover{text-decoration:underline;color:#92400e}
code{font-family:'JetBrains Mono','Fira Code','Courier New',monospace;font-size:9pt;background:#fefce8;padding:.15em .4em;border-radius:3px;color:#92400e;border:1px solid #fde68a}
pre{background:#1a1a1a;border:1px solid #404040;border-radius:6px;padding:1em 1.2em;overflow-x:auto;font-size:9pt;line-height:1.5;page-break-inside:avoid;margin:.8em 0;position:relative}
pre code{background:none;padding:0;color:#e5e5e5;font-size:9pt;border:none}

/* Tabelas */
table{width:100%;border-collapse:collapse;margin:.8em 0;font-size:10pt;page-break-inside:avoid;border-radius:6px;overflow:hidden}
th,td{border:1px solid #d4d4d4;padding:.5em .7em;text-align:left;vertical-align:top}
th{background:#1a1a1a;color:#fbbf24;font-weight:600;font-size:9.5pt}
tr:nth-child(even){background:#fafafa}
tr:hover{background:#fefce8}

/* Blockquote */
blockquote{border-left:4px solid #fbbf24;margin:.8em 0;padding:.6em 1.2em;color:#525252;background:#fefce8;border-radius:0 6px 6px 0;font-style:italic}

/* Listas */
ul,ol{margin:.5em 0;padding-left:1.5em}
li{margin:.3em 0}
li.nested{margin-left:1.5em}

/* Checkboxes */
.check-done{color:#16a34a;font-weight:bold}
.check-todo{color:#a3a3a3}

hr{border:none;border-top:1px solid #e5e5e5;margin:1.5em 0}

/* Mermaid */
.mermaid{text-align:center;margin:1.2em 0;padding:1em;background:#fafafa;border:1px solid #e5e5e5;border-radius:6px;page-break-inside:avoid}

strong{font-weight:bold}
em{font-style:italic}

/* Separador de módulo */
.module-separator{border:none;border-top:2px dashed #e5e5e5;margin:2.5em 0}

/* Projeto */
.project-header{background:linear-gradient(135deg,#fefce8,#fef9c3);border:1px solid #fde68a;border-radius:8px;padding:.8em 1.2em;margin:1.5em 0 1em 0}
.project-header h2{border:none;margin:0;color:#92400e;font-size:14pt;font-family:'JetBrains Mono',monospace;font-weight:700}

/* Seções especiais com cores */
.section-faq h2,.section-faq h3{color:#525252}
.section-culture h2,.section-culture h3{color:#92400e}
.section-ai h2,.section-ai h3{color:#525252}

/* URLs por extenso para impressão */
.url-print{font-size:8pt;color:#737373;word-break:break-all}

/* Print */
@media print{
    body{font-size:10.5pt}
    .cover{background:#1a1a1a !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
    .page-break{page-break-before:always}
    h1,h2,h3,h4{page-break-after:avoid}
    table,pre,.mermaid,blockquote{page-break-inside:avoid}
    pre{background:#f5f5f5 !important;border:1px solid #d4d4d4}
    pre code{color:#1a1a1a !important}
    th{background:#e5e5e5 !important;color:#1a1a1a !important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
    a{color:#1a1a1a;text-decoration:underline}
    a[href^="#"]::after{content:none}
}

/* Screen */
@media screen{
    body{max-width:210mm;margin:0 auto;padding:2cm;box-shadow:0 0 30px rgba(0,0,0,.1)}
    .page-break{border-top:3px dashed #e5e5e5;margin:3em 0;padding-top:2em}
}
"""


# ─── Capa ─────────────────────────────────────────────────────────────────────

COVER = """<div class="cover">
<h1>De Zero a Dev</h1>
<div class="line"></div>
<div class="subtitle">Curso Completo de Tecnologia<br/>
Do zero absoluto ao desenvolvedor j&uacute;nior &mdash; um guia completo para quem quer entrar no mundo da tecnologia.</div>
<div class="line"></div>
<div class="author">Rafael Gottardi (Fino)</div>
<div class="version">Vers&atilde;o 1.0 &mdash; 2026</div>
</div>"""

# ─── Prefácio ─────────────────────────────────────────────────────────────────

PREFACIO = """<div class="preface page-break">
<h2>Pref&aacute;cio</h2>

<p>Este livro nasceu de uma convic&ccedil;&atilde;o simples: qualquer pessoa pode aprender a programar. N&atilde;o importa sua idade, sua forma&ccedil;&atilde;o anterior ou se voc&ecirc; nunca tocou em uma linha de c&oacute;digo. O que importa &eacute; curiosidade e persist&ecirc;ncia.</p>

<p>Durante anos ensinando tecnologia, percebi que o maior obst&aacute;culo para iniciantes n&atilde;o &eacute; a complexidade dos conceitos &mdash; &eacute; a forma como eles s&atilde;o apresentados. Materiais que assumem conhecimento pr&eacute;vio, que pulam etapas, que usam jarg&atilde;o sem explicar. Este livro foi escrito para resolver exatamente esse problema.</p>

<p>Cada conceito &eacute; constru&iacute;do sobre o anterior. Cada termo t&eacute;cnico &eacute; explicado na primeira vez que aparece. Cada exemplo pode ser copiado e executado. N&atilde;o h&aacute; saltos, n&atilde;o h&aacute; atalhos, n&atilde;o h&aacute; &ldquo;&eacute; &oacute;bvio que&rdquo;.</p>

<p>O material cobre desde o que &eacute; um computador at&eacute; a constru&ccedil;&atilde;o de APIs profissionais, passando por tr&ecirc;s linguagens de programa&ccedil;&atilde;o (Python, C e C#), bancos de dados, Docker, arquitetura de software e boas pr&aacute;ticas de carreira. Ao final, voc&ecirc; ter&aacute; as bases para trabalhar como desenvolvedor j&uacute;nior.</p>

<p>Dois princ&iacute;pios guiam todo o conte&uacute;do:</p>

<p><strong>&ldquo;Qual problema voc&ecirc; quer resolver?&rdquo;</strong> &mdash; Antes de apresentar qualquer ferramenta ou tecnologia, explicamos qual problema ela resolve. Ningu&eacute;m criou Linux &ldquo;porque sim&rdquo;. Ningu&eacute;m inventou bancos de dados &ldquo;porque sim&rdquo;. Tudo existe para resolver um problema real.</p>

<p><strong>&ldquo;Conceitos s&atilde;o para sempre, ferramentas apenas os implementam&rdquo;</strong> &mdash; Python pode ser substitu&iacute;do. Docker pode ser substitu&iacute;do. Mas l&oacute;gica de programa&ccedil;&atilde;o, estruturas de dados, modelagem e arquitetura s&atilde;o permanentes. Este livro prioriza o conceito sobre a ferramenta.</p>

<p>Use IA como parceira de aprendizado &mdash; ao longo do livro, mostramos como. Mas n&atilde;o pule etapas. Leia, pratique, erre, corrija. &Eacute; assim que se aprende.</p>

<p style="text-align:right;margin-top:2em;color:#737373;font-style:italic">&mdash; Fino, 2026</p>
</div>"""

# ─── Introdução ───────────────────────────────────────────────────────────────

INTRODUCAO = """<div class="preface page-break">
<h2>Introdu&ccedil;&atilde;o</h2>

<h3>Para quem &eacute; este livro</h3>

<p>Este livro foi escrito para quem n&atilde;o sabe nada de tecnologia. Zero. Se voc&ecirc; nunca programou, nunca usou um terminal, nunca ouviu falar de Linux &mdash; este livro &eacute; para voc&ecirc;. N&atilde;o assumimos nenhum conhecimento pr&eacute;vio al&eacute;m de saber usar um computador para tarefas b&aacute;sicas.</p>

<h3>Como este livro est&aacute; organizado</h3>

<p>O conte&uacute;do est&aacute; dividido em 13 cap&iacute;tulos, cada um com m&uacute;ltiplos m&oacute;dulos. Os cap&iacute;tulos s&atilde;o sequenciais &mdash; cada um depende dos anteriores. Siga na ordem.</p>

<p>Os primeiros quatro cap&iacute;tulos s&atilde;o te&oacute;ricos: fundamentos da computa&ccedil;&atilde;o, Linux, terminal e Git. A partir do cap&iacute;tulo 5, voc&ecirc; come&ccedil;a a programar de verdade com Python. Depois passa por Docker, estruturas de dados com C, bancos de dados, orienta&ccedil;&atilde;o a objetos com C#, arquitetura de software e APIs.</p>

<p>Cada cap&iacute;tulo termina com um projeto pr&aacute;tico que consolida tudo que foi ensinado. Os projetos s&atilde;o progressivos e se conectam entre si.</p>

<h3>Como usar este livro</h3>

<ol>
<li>Leia cada m&oacute;dulo na ordem apresentada</li>
<li>Execute todos os exemplos de c&oacute;digo no seu computador</li>
<li>Fa&ccedil;a todos os exerc&iacute;cios antes de avan&ccedil;ar</li>
<li>Consulte o gloss&aacute;rio sempre que encontrar um termo desconhecido</li>
<li>Use IA como ferramenta de apoio &mdash; vamos ensinar como ao longo do livro</li>
</ol>

<h3>Linguagens utilizadas</h3>

<table>
<thead><tr><th>Linguagem</th><th>Cap&iacute;tulos</th><th>Prop&oacute;sito</th></tr></thead>
<tbody>
<tr><td>Python</td><td>5, 8, 11</td><td>L&oacute;gica de programa&ccedil;&atilde;o, CRUD, APIs</td></tr>
<tr><td>C</td><td>7</td><td>Aloca&ccedil;&atilde;o de mem&oacute;ria e estruturas de dados</td></tr>
<tr><td>C# (.NET)</td><td>9</td><td>Orienta&ccedil;&atilde;o a objetos e estrutura&ccedil;&atilde;o de solu&ccedil;&otilde;es</td></tr>
</tbody>
</table>

<h3>Conven&ccedil;&otilde;es do livro</h3>

<p>Termos t&eacute;cnicos em ingl&ecirc;s aparecem em negrito na primeira ocorr&ecirc;ncia, com tradu&ccedil;&atilde;o em portugu&ecirc;s. Nas ocorr&ecirc;ncias seguintes, usamos apenas o termo.</p>

<p>Blocos de c&oacute;digo sempre t&ecirc;m coment&aacute;rios explicativos em portugu&ecirc;s e podem ser copiados e executados diretamente.</p>

<p>Se algo parecer dif&iacute;cil, releia, pratique e pe&ccedil;a ajuda. Todo programador j&aacute; esteve onde voc&ecirc; est&aacute; agora.</p>
</div>"""


# ─── Funções auxiliares ───────────────────────────────────────────────────────

def find_modules(cap_num):
    """Encontra todos os arquivos de módulo de um capítulo, na ordem correta."""
    pattern = os.path.join(CONTENT_DIR, f'capitulos/cap{cap_num:02d}-mod*.md')
    files = sorted(glob.glob(pattern))
    return files


def read_file(path):
    """Lê um arquivo markdown e retorna seu conteúdo."""
    # Suporta paths absolutos e relativos ao BASE_DIR
    if not os.path.isabs(path):
        path = os.path.join(BASE_DIR, path)
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def get_first_h1(md_content):
    """Extrai o título do primeiro H1 do markdown."""
    m = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    return m.group(1).strip() if m else None


def build_book():
    """Monta o conteúdo completo do livro em HTML."""
    all_modules = []  # Lista de dicts para o sumário

    body_parts = []

    for cap_num in sorted(CAPITULOS.keys()):
        cap_info = CAPITULOS[cap_num]
        cap_title = f"Capítulo {cap_num} -- {cap_info['titulo']}"
        cap_id = mkid(cap_title)

        # Quebra de página + header do capítulo
        body_parts.append(f'<div class="page-break"></div>')
        body_parts.append(
            f'<h1 class="chapter-header" id="{cap_id}">{H.escape(cap_title)}'
            f'<span class="chapter-desc">{H.escape(cap_info["descricao"])}</span></h1>'
        )

        # Módulos do capítulo
        modules = find_modules(cap_num)
        for mod_path in modules:
            md_content = read_file(mod_path)
            if not md_content.strip():
                continue

            # Extrair título do módulo
            mod_title = get_first_h1(md_content) or os.path.basename(mod_path)
            mod_title = strip_emojis(mod_title)
            mod_id = mkid(mod_title)

            is_exercise = '-exercicios' in mod_path

            all_modules.append({
                'cap': cap_num,
                'title': mod_title,
                'id': mod_id,
                'is_project': False,
                'is_exercise': is_exercise,
            })

            # Quebra de página antes de cada módulo
            body_parts.append(f'<div class="page-break"></div>')

            # Converter markdown para HTML
            html_content = md2html(md_content.split('\n'))
            body_parts.append(html_content)

        # Projeto do capítulo (se existir)
        if cap_num in PROJETOS:
            proj_path = PROJETOS[cap_num]
            proj_content = read_file(proj_path)
            if proj_content.strip():
                proj_title = get_first_h1(proj_content) or f"Projeto do Capítulo {cap_num}"
                proj_title = strip_emojis(proj_title)
                proj_id = mkid(proj_title)

                all_modules.append({
                    'cap': cap_num,
                    'title': proj_title,
                    'id': proj_id,
                    'is_project': True,
                    'is_exercise': False,
                })

                body_parts.append(f'<div class="page-break"></div>')
                body_parts.append(f'<div class="project-header"><h2>Projeto Pratico</h2></div>')
                html_content = md2html(proj_content.split('\n'))
                body_parts.append(html_content)

    body_html = '\n'.join(body_parts)

    # Remover as duas primeiras quebras de página (capítulo 1 header + primeiro módulo)
    # para que o título do capítulo 1 e seu primeiro módulo fiquem na mesma página
    body_html = body_html.replace('<div class="page-break"></div>', '', 1)
    body_html = body_html.replace('<div class="page-break"></div>', '', 1)

    return body_html, all_modules


def build_toc(all_modules):
    """Constrói o sumário a partir da lista de módulos."""
    h = '<div class="toc"><h2>Sum&aacute;rio</h2>\n'

    current_cap = None
    for mod in all_modules:
        if mod['cap'] != current_cap:
            current_cap = mod['cap']
            cap_info = CAPITULOS[current_cap]
            cap_label = f"Capítulo {current_cap} -- {cap_info['titulo']}"
            h += f'<div class="toc-chapter">{H.escape(cap_label)}</div>\n'

        title = mod['title']
        aid = mod['id']
        css_class = ' toc-project' if mod['is_project'] else ''

        if len(title) > 80:
            title = title[:77] + '...'

        h += (
            f'<div class="toc-entry{css_class}">'
            f'<a href="#{aid}">{H.escape(title)}</a>'
            f'<span class="toc-dots"></span>'
            f'</div>\n'
        )

    h += '</div>\n'
    return h


# ─── Validação: Ortografia ────────────────────────────────────────────────────

CORRECOES = {
    "Logica": "Lógica", "logica": "lógica",
    "Codigo": "Código", "codigo": "código",
    "Numero": "Número", "numero": "número",
    "Numeros": "Números", "numeros": "números",
    "Memoria": "Memória", "memoria": "memória",
    "Historico": "Histórico", "historico": "histórico",
    "Historia": "História", "historia": "história",
    "Basico": "Básico", "basico": "básico",
    "Basica": "Básica", "basica": "básica",
    "Basicos": "Básicos", "basicos": "básicos",
    "Basicas": "Básicas", "basicas": "básicas",
    "Unico": "Único", "unico": "único",
    "Unica": "Única", "unica": "única",
    "Publico": "Público", "publico": "público",
    "Publica": "Pública", "publica": "pública",
    "Tecnico": "Técnico", "tecnico": "técnico",
    "Tecnica": "Técnica", "tecnica": "técnica",
    "Tecnicas": "Técnicas", "tecnicas": "técnicas",
    "Tecnicos": "Técnicos", "tecnicos": "técnicos",
    "Topico": "Tópico", "topico": "tópico",
    "Topicos": "Tópicos", "topicos": "tópicos",
    "Grafico": "Gráfico", "grafico": "gráfico",
    "Graficos": "Gráficos", "graficos": "gráficos",
    "Automatico": "Automático", "automatico": "automático",
    "Automatica": "Automática", "automatica": "automática",
    "Especifico": "Específico", "especifico": "específico",
    "Especifica": "Específica", "especifica": "específica",
    "Especificos": "Específicos", "especificos": "específicos",
    "Generico": "Genérico", "generico": "genérico",
    "Generica": "Genérica", "generica": "genérica",
    "Dinamico": "Dinâmico", "dinamico": "dinâmico",
    "Dinamica": "Dinâmica", "dinamica": "dinâmica",
    "Estatico": "Estático", "estatico": "estático",
    "Estatica": "Estática", "estatica": "estática",
    "Sintatico": "Sintático", "sintatico": "sintático",
    "Semantico": "Semântico", "semantico": "semântico",
    "Aritmetico": "Aritmético", "aritmetico": "aritmético",
    "Matematico": "Matemático", "matematico": "matemático",
    "Matematica": "Matemática", "matematica": "matemática",
    "Binario": "Binário", "binario": "binário",
    "Primario": "Primário", "primario": "primário",
    "Secundario": "Secundário", "secundario": "secundário",
    "Terciario": "Terciário", "terciario": "terciário",
    "Exercicio": "Exercício", "exercicio": "exercício",
    "Exercicios": "Exercícios", "exercicios": "exercícios",
    "Capitulo": "Capítulo", "capitulo": "capítulo",
    "Capitulos": "Capítulos", "capitulos": "capítulos",
    "Modulo": "Módulo", "modulo": "módulo",
    "Modulos": "Módulos", "modulos": "módulos",
    "Indice": "Índice", "indice": "índice",
    "Glossario": "Glossário", "glossario": "glossário",
    "Pratico": "Prático", "pratico": "prático",
    "Pratica": "Prática", "pratica": "prática",
    "Praticos": "Práticos", "praticos": "práticos",
    "Praticas": "Práticas", "praticas": "práticas",
    "Introducao": "Introdução", "introducao": "introdução",
    "Conclusao": "Conclusão", "conclusao": "conclusão",
    "Secao": "Seção", "secao": "seção",
    "Secoes": "Seções", "secoes": "seções",
    "Funcao": "Função", "funcao": "função",
    "Funcoes": "Funções", "funcoes": "funções",
    "Condicao": "Condição", "condicao": "condição",
    "Condicoes": "Condições", "condicoes": "condições",
    "Excecao": "Exceção", "excecao": "exceção",
    "Excecoes": "Exceções", "excecoes": "exceções",
    "Operacao": "Operação", "operacao": "operação",
    "Operacoes": "Operações", "operacoes": "operações",
    "Aplicacao": "Aplicação", "aplicacao": "aplicação",
    "Aplicacoes": "Aplicações", "aplicacoes": "aplicações",
    "Informacao": "Informação", "informacao": "informação",
    "Informacoes": "Informações", "informacoes": "informações",
    "Configuracao": "Configuração", "configuracao": "configuração",
    "Configuracoes": "Configurações", "configuracoes": "configurações",
    "Comunicacao": "Comunicação", "comunicacao": "comunicação",
    "Documentacao": "Documentação", "documentacao": "documentação",
    "Implementacao": "Implementação", "implementacao": "implementação",
    "Programacao": "Programação", "programacao": "programação",
    "Compilacao": "Compilação", "compilacao": "compilação",
    "Execucao": "Execução", "execucao": "execução",
    "Instrucao": "Instrução", "instrucao": "instrução",
    "Instrucoes": "Instruções", "instrucoes": "instruções",
    "Conexao": "Conexão", "conexao": "conexão",
    "Conexoes": "Conexões", "conexoes": "conexões",
    "Versao": "Versão", "versao": "versão",
    "Versoes": "Versões", "versoes": "versões",
    "Permissao": "Permissão", "permissao": "permissão",
    "Permissoes": "Permissões", "permissoes": "permissões",
    "Extensao": "Extensão", "extensao": "extensão",
    "Extensoes": "Extensões", "extensoes": "extensões",
    "Resolucao": "Resolução", "resolucao": "resolução",
    "Evolucao": "Evolução", "evolucao": "evolução",
    "Solucao": "Solução", "solucao": "solução",
    "Solucoes": "Soluções", "solucoes": "soluções",
    "Protecao": "Proteção", "protecao": "proteção",
    "Validacao": "Validação", "validacao": "validação",
    "Criacao": "Criação", "criacao": "criação",
    "Alteracao": "Alteração", "alteracao": "alteração",
    "Interacao": "Interação", "interacao": "interação",
    "Integracao": "Integração", "integracao": "integração",
    "Migracao": "Migração", "migracao": "migração",
    "Navegacao": "Navegação", "navegacao": "navegação",
    "Organizacao": "Organização", "organizacao": "organização",
    "Autenticacao": "Autenticação", "autenticacao": "autenticação",
    "Autorizacao": "Autorização", "autorizacao": "autorização",
    "Virtualizacao": "Virtualização", "virtualizacao": "virtualização",
    "Manipulacao": "Manipulação", "manipulacao": "manipulação",
    "Comparacao": "Comparação", "comparacao": "comparação",
    "Classificacao": "Classificação", "classificacao": "classificação",
    "Ordenacao": "Ordenação", "ordenacao": "ordenação",
    "Repeticao": "Repetição", "repeticao": "repetição",
    "Iteracao": "Iteração", "iteracao": "iteração",
    "Atribuicao": "Atribuição", "atribuicao": "atribuição",
    "Definicao": "Definição", "definicao": "definição",
    "Definicoes": "Definições", "definicoes": "definições",
    "Descricao": "Descrição", "descricao": "descrição",
    "Abstracoes": "Abstrações", "abstracoes": "abstrações",
    "Abstracao": "Abstração", "abstracao": "abstração",
    "Colecao": "Coleção", "colecao": "coleção",
    "Colecoes": "Coleções", "colecoes": "coleções",
    "Posicao": "Posição", "posicao": "posição",
    "Posicoes": "Posições", "posicoes": "posições",
    "Situacao": "Situação", "situacao": "situação",
    "Transacao": "Transação", "transacao": "transação",
    "Transacoes": "Transações", "transacoes": "transações",
    "Alocacao": "Alocação", "alocacao": "alocação",
    "Notacao": "Notação", "notacao": "notação",
    "Relacao": "Relação", "relacao": "relação",
    "Relacoes": "Relações", "relacoes": "relações",
    "Padrao": "Padrão", "padrao": "padrão",
    "Padroes": "Padrões", "padroes": "padrões",
    "Nao": "Não",
    "Entao": "Então", "entao": "então",
    "Tambem": "Também", "tambem": "também",
    "Voce": "Você", "voce": "você",
    "Alem": "Além", "alem": "além",
    "Porem": "Porém", "porem": "porém",
    "Atraves": "Através", "atraves": "através",
    "Facil": "Fácil", "facil": "fácil",
    "Dificil": "Difícil", "dificil": "difícil",
    "Possivel": "Possível", "possivel": "possível",
    "Impossivel": "Impossível", "impossivel": "impossível",
    "Disponivel": "Disponível", "disponivel": "disponível",
    "Variavel": "Variável", "variavel": "variável",
    "Variaveis": "Variáveis", "variaveis": "variáveis",
    "Responsavel": "Responsável", "responsavel": "responsável",
    "Compativel": "Compatível", "compativel": "compatível",
    "Util": "Útil", "util": "útil",
    "Uteis": "Úteis", "uteis": "úteis",
    "Nivel": "Nível", "nivel": "nível",
    "Niveis": "Níveis", "niveis": "níveis",
    "Visivel": "Visível", "visivel": "visível",
    "Acessivel": "Acessível", "acessivel": "acessível",
    "Flexivel": "Flexível", "flexivel": "flexível",
    "Movel": "Móvel", "movel": "móvel",
    "Portatil": "Portátil", "portatil": "portátil",
    "Volatil": "Volátil", "volatil": "volátil",
    "Analise": "Análise", "analise": "análise",
    "Metodo": "Método", "metodo": "método",
    "Metodos": "Métodos", "metodos": "métodos",
    "Periodo": "Período", "periodo": "período",
    "Conteudo": "Conteúdo", "conteudo": "conteúdo",
    "Conteudos": "Conteúdos", "conteudos": "conteúdos",
    "Titulo": "Título", "titulo": "título",
    "Titulos": "Títulos", "titulos": "títulos",
    "Valido": "Válido", "valido": "válido",
    "Valida": "Válida", "valida": "válida",
    "Invalido": "Inválido", "invalido": "inválido",
    "Invalida": "Inválida", "invalida": "inválida",
    "Rapido": "Rápido", "rapido": "rápido",
    "Rapida": "Rápida", "rapida": "rápida",
    "Proximo": "Próximo", "proximo": "próximo",
    "Proxima": "Próxima", "proxima": "próxima",
    "Ultimo": "Último", "ultimo": "último",
    "Ultima": "Última", "ultima": "última",
    "Minimo": "Mínimo", "minimo": "mínimo",
    "Minima": "Mínima", "minima": "mínima",
    "Maximo": "Máximo", "maximo": "máximo",
    "Maxima": "Máxima", "maxima": "máxima",
    "Otimo": "Ótimo", "otimo": "ótimo",
    "Otima": "Ótima", "otima": "ótima",
    "Obrigatorio": "Obrigatório", "obrigatorio": "obrigatório",
    "Obrigatoria": "Obrigatória", "obrigatoria": "obrigatória",
    "Necessario": "Necessário", "necessario": "necessário",
    "Necessaria": "Necessária", "necessaria": "necessária",
    "Temporario": "Temporário", "temporario": "temporário",
    "Temporaria": "Temporária", "temporaria": "temporária",
    "Diretorio": "Diretório", "diretorio": "diretório",
    "Diretorios": "Diretórios", "diretorios": "diretórios",
    "Repositorio": "Repositório", "repositorio": "repositório",
    "Repositorios": "Repositórios", "repositorios": "repositórios",
    "Formulario": "Formulário", "formulario": "formulário",
    "Comentario": "Comentário", "comentario": "comentário",
    "Comentarios": "Comentários", "comentarios": "comentários",
    "Cenario": "Cenário", "cenario": "cenário",
    "Cenarios": "Cenários", "cenarios": "cenários",
    "Criterio": "Critério", "criterio": "critério",
    "Criterios": "Critérios", "criterios": "critérios",
    "Relatorio": "Relatório", "relatorio": "relatório",
    "Dicionario": "Dicionário", "dicionario": "dicionário",
    "Dicionarios": "Dicionários", "dicionarios": "dicionários",
    "Simbolo": "Símbolo", "simbolo": "símbolo",
    "Simbolos": "Símbolos", "simbolos": "símbolos",
    "Sequencia": "Sequência", "sequencia": "sequência",
    "Sequencias": "Sequências", "sequencias": "sequências",
    "Frequencia": "Frequência", "frequencia": "frequência",
    "Referencia": "Referência", "referencia": "referência",
    "Referencias": "Referências", "referencias": "referências",
    "Experiencia": "Experiência", "experiencia": "experiência",
    "Diferenca": "Diferença", "diferenca": "diferença",
    "Diferencas": "Diferenças", "diferencas": "diferenças",
    "Seguranca": "Segurança", "seguranca": "segurança",
    "Heranca": "Herança", "heranca": "herança",
    "Instancia": "Instância", "instancia": "instância",
    "Instancias": "Instâncias", "instancias": "instâncias",
    "Importancia": "Importância", "importancia": "importância",
    "Dependencia": "Dependência", "dependencia": "dependência",
    "Dependencias": "Dependências", "dependencias": "dependências",
    "Eficiencia": "Eficiência", "eficiencia": "eficiência",
    "Potencia": "Potência", "potencia": "potência",
    "Essencia": "Essência", "essencia": "essência",
    "Presenca": "Presença", "presenca": "presença",
    "Ausencia": "Ausência", "ausencia": "ausência",
    "Licenca": "Licença", "licenca": "licença",
    "Licencas": "Licenças", "licencas": "licenças",
    "Gerencia": "Gerência", "gerencia": "gerência",
    "Ciencia": "Ciência", "ciencia": "ciência",
    "Existencia": "Existência", "existencia": "existência",
    "Persistencia": "Persistência", "persistencia": "persistência",
    "Consistencia": "Consistência", "consistencia": "consistência",
    "Concorrencia": "Concorrência", "concorrencia": "concorrência",
    "Preferencia": "Preferência", "preferencia": "preferência",
    "Ocorrencia": "Ocorrência", "ocorrencia": "ocorrência",
    "Ocorrencias": "Ocorrências", "ocorrencias": "ocorrências",
    "Inteligencia": "Inteligência", "inteligencia": "inteligência",
    "Consequencia": "Consequência", "consequencia": "consequência",
    "Consequencias": "Consequências", "consequencias": "consequências",
    "Acao": "Ação", "acao": "ação",
    "Acoes": "Ações", "acoes": "ações",
    "Manutencao": "Manutenção", "manutencao": "manutenção",
    "Producao": "Produção", "producao": "produção",
    "Reducao": "Redução", "reducao": "redução",
    "Construcao": "Construção", "construcao": "construção",
    "Substituicao": "Substituição", "substituicao": "substituição",
    "Distribuicao": "Distribuição", "distribuicao": "distribuição",
    "Restricao": "Restrição", "restricao": "restrição",
    "Restricoes": "Restrições", "restricoes": "restrições",
    "Insercao": "Inserção", "insercao": "inserção",
    "Remocao": "Remoção", "remocao": "remoção",
    "Selecao": "Seleção", "selecao": "seleção",
    "Educacao": "Educação", "educacao": "educação",
    "Geracao": "Geração", "geracao": "geração",
    "Geracoes": "Gerações", "geracoes": "gerações",
    "Utilizacao": "Utilização", "utilizacao": "utilização",
    "Otimizacao": "Otimização", "otimizacao": "otimização",
    "Inicializacao": "Inicialização", "inicializacao": "inicialização",
    "Serializacao": "Serialização", "serializacao": "serialização",
    "Normalizacao": "Normalização", "normalizacao": "normalização",
    "Visualizacao": "Visualização", "visualizacao": "visualização",
    "Atualizacao": "Atualização", "atualizacao": "atualização",
    "Localizacao": "Localização", "localizacao": "localização",
    "Reutilizacao": "Reutilização", "reutilizacao": "reutilização",
    "Arvore": "Árvore", "arvore": "árvore",
    "Arvores": "Árvores", "arvores": "árvores",
    "Pagina": "Página", "pagina": "página",
    "Paginas": "Páginas", "paginas": "páginas",
    "Maquina": "Máquina", "maquina": "máquina",
    "Maquinas": "Máquinas", "maquinas": "máquinas",
    "Fabrica": "Fábrica", "fabrica": "fábrica",
    "Calculo": "Cálculo", "calculo": "cálculo",
    "Calculos": "Cálculos", "calculos": "cálculos",
    "Varias": "Várias", "varias": "várias",
    "Varios": "Vários", "varios": "vários",
    "Necessarias": "Necessárias", "necessarias": "necessárias",
    "Necessarios": "Necessários", "necessarios": "necessários",
    "Obrigatorias": "Obrigatórias", "obrigatorias": "obrigatórias",
    "Obrigatorios": "Obrigatórios", "obrigatorios": "obrigatórios",
}

# Palavras válidas sem acento (falsos positivos)
IGNORAR_ORTOGRAFIA = {"ate", "nos", "so", "ja", "Nos", "valida"}

# Regex compilada para correção rápida
_palavras_erradas = {k: v for k, v in CORRECOES.items() if k != v and k not in IGNORAR_ORTOGRAFIA}
_sorted_keys = sorted(_palavras_erradas.keys(), key=len, reverse=True)
_SPELL_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(k) for k in _sorted_keys) + r')\b')


def _extrair_texto_md(content):
    """Extrai linhas de texto fora de code fences."""
    lines = content.split('\n')
    resultado = []
    in_code = False
    fence = None
    for i, L in enumerate(lines):
        mf = re.match(r'^(`{3,})', L)
        if mf:
            if not in_code:
                in_code = True
                fence = mf.group(1)
            elif L.strip().startswith(fence):
                in_code = False
                fence = None
            continue
        if in_code:
            continue
        if L.strip().startswith('http') or L.strip().startswith('!['):
            continue
        resultado.append((i + 1, L))
    return resultado


def validar_ortografia(arquivos):
    """Valida ortografia fora de code blocks. Retorna total de problemas."""
    total = 0
    for arq in arquivos:
        with open(arq, 'r', encoding='utf-8') as f:
            content = f.read()
        linhas = _extrair_texto_md(content)
        problemas = []
        for line_num, line in linhas:
            for m in re.finditer(r'\b([A-Za-zÀ-ÿ]+)\b', line):
                palavra = m.group(1)
                if palavra in IGNORAR_ORTOGRAFIA:
                    continue
                if palavra in CORRECOES and CORRECOES[palavra] != palavra:
                    problemas.append((line_num, palavra, CORRECOES[palavra]))
        if problemas:
            total += len(problemas)
            print(f"  {arq}: {len(problemas)} problemas de ortografia")
            for ln, errado, correto in problemas[:5]:
                print(f"    L{ln}: {errado} → {correto}")
            if len(problemas) > 5:
                print(f"    ... e mais {len(problemas) - 5}")
    return total


def corrigir_ortografia(arquivos):
    """Corrige ortografia fora de code blocks. Retorna total de correções."""
    total = 0
    modificados = 0
    for arq in arquivos:
        with open(arq, 'r', encoding='utf-8') as f:
            content = f.read()
        lines = content.split('\n')
        resultado = []
        in_code = False
        fence = None
        count = 0
        for L in lines:
            mf = re.match(r'^(`{3,})', L)
            if mf:
                if not in_code:
                    in_code = True
                    fence = mf.group(1)
                elif L.strip().startswith(fence):
                    in_code = False
                    fence = None
                resultado.append(L)
                continue
            if in_code:
                resultado.append(L)
                continue
            def replacer(m):
                nonlocal count
                word = m.group(0)
                if word in _palavras_erradas:
                    count += 1
                    return _palavras_erradas[word]
                return word
            resultado.append(_SPELL_PATTERN.sub(replacer, L))
        novo = '\n'.join(resultado)
        if novo != content:
            with open(arq, 'w', encoding='utf-8') as f:
                f.write(novo)
            modificados += 1
            total += count
            print(f"  {arq}: {count} correções")
    return total, modificados


def validar_code_fences(arquivos):
    """Verifica code fences balanceados. Retorna lista de arquivos com problema."""
    problemas = []
    for arq in arquivos:
        with open(arq, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        in_fence = False
        fence_bt = 0
        fence_line = 0
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith('```'):
                bt = 0
                for c in stripped:
                    if c == '`':
                        bt += 1
                    else:
                        break
                if not in_fence:
                    in_fence = True
                    fence_bt = bt
                    fence_line = i
                elif bt >= fence_bt:
                    in_fence = False
                    fence_bt = 0
        if in_fence:
            problemas.append((arq, fence_line))
            print(f"  ERRO: {arq} — code fence aberto na linha {fence_line} sem fechar")
    return problemas


def listar_markdowns():
    """Lista todos os markdowns do curso (capítulos + projetos)."""
    caps = glob.glob(os.path.join(CONTENT_DIR, 'capitulos/*.md'))
    projs = glob.glob(os.path.join(CONTENT_DIR, 'projects/*.md'))
    return sorted(caps + projs)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = set(sys.argv[1:])
    validate_only = '--validate' in args
    fix_spelling = '--fix' in args
    no_check = '--no-check' in args

    arquivos = listar_markdowns()

    # Modo --fix: corrigir ortografia e sair ou continuar para gerar
    if fix_spelling:
        print("Corrigindo ortografia...")
        total, modificados = corrigir_ortografia(arquivos)
        if total:
            print(f"  {total} correções em {modificados} arquivos")
        else:
            print("  Nenhuma correção necessária")
        print()

    # Validação prévia (a menos que --no-check)
    if not no_check:
        print("Validando markdowns...")
        erros_fence = validar_code_fences(arquivos)
        erros_ortografia = validar_ortografia(arquivos)

        if erros_fence:
            print(f"\nERRO: {len(erros_fence)} arquivo(s) com code fences desbalanceados.")
            print("Corrija antes de gerar o HTML.")
            sys.exit(1)

        if erros_ortografia and not fix_spelling:
            print(f"\nAVISO: {erros_ortografia} problemas de ortografia encontrados.")
            print("Use --fix para corrigir automaticamente, ou --no-check para ignorar.")

        if not erros_fence and not erros_ortografia:
            print("  Tudo OK")
        print()

    if validate_only:
        return

    print("Gerando livro HTML do curso 'De Zero a Dev'...")

    body_html, all_modules = build_book()
    toc_html = build_toc(all_modules)

    full = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>De Zero a Dev -- Curso Completo de Tecnologia</title>
<style>{CSS}</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
</head>
<body>
{COVER}
{PREFACIO}
{INTRODUCAO}
{toc_html}
{body_html}
<script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
<script>
// Mermaid: lazy render via IntersectionObserver para não travar o navegador
mermaid.initialize({{startOnLoad:false,theme:'neutral',securityLevel:'loose'}});
(function(){{
  var pending=document.querySelectorAll('.mermaid');
  var id=0;
  function render(el){{
    if(el.dataset.rendered) return;
    el.dataset.rendered='1';
    var code=el.textContent;
    var eid='mermaid-'+id++;
    try{{
      mermaid.render(eid,code).then(function(r){{el.innerHTML=r.svg;}}).catch(function(){{
        el.innerHTML='<pre style="color:#999;font-size:9pt">[Diagrama nao renderizado]</pre>';
      }});
    }}catch(e){{
      el.innerHTML='<pre style="color:#999;font-size:9pt">[Diagrama nao renderizado]</pre>';
    }}
  }}
  if('IntersectionObserver' in window){{
    var obs=new IntersectionObserver(function(entries){{
      entries.forEach(function(e){{if(e.isIntersecting){{render(e.target);obs.unobserve(e.target);}}}});
    }},{{rootMargin:'200px'}});
    pending.forEach(function(el){{obs.observe(el);}});
  }}else{{
    pending.forEach(render);
  }}
}})();
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/c.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/csharp.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/bash.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/sql.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/json.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/yaml.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/xml.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/dockerfile.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/ini.min.js"></script>
<script>hljs.highlightAll();</script>
</body>
</html>"""

    output_path = os.path.join(BASE_DIR, 'de-zero-a-dev.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full)

    # Estatísticas
    sz = os.path.getsize(output_path)
    total_all = len(all_modules)
    total_content = len([m for m in all_modules if not m['is_exercise'] and not m['is_project']])
    total_exercises = len([m for m in all_modules if m['is_exercise']])
    total_projects = len([m for m in all_modules if m['is_project']])
    total_chapters = len(CAPITULOS)
    mermaid_count = body_html.count('class="mermaid"')

    print(f"\nLivro HTML gerado: {output_path} ({sz/1024:.0f} KB)")
    print(f"Capitulos: {total_chapters}")
    print(f"Modulos de conteudo: {total_content}")
    print(f"Modulos de exercicios: {total_exercises}")
    print(f"Projetos praticos: {total_projects}")
    print(f"Total de secoes: {total_all}")
    print(f"Diagramas Mermaid: {mermaid_count}")


if __name__ == '__main__':
    main()
