#!/usr/bin/env python3
"""Converte os módulos do curso 'Python Basics' em HTML imprimível com capa, sumário e quebras de página.

Uso:
  python3 gerar-python-basics-html.py              # Gera o HTML (com validação prévia)
  python3 gerar-python-basics-html.py --validate   # Apenas valida (ortografia + code fences), sem gerar
  python3 gerar-python-basics-html.py --fix        # Corrige ortografia automaticamente e depois gera
  python3 gerar-python-basics-html.py --no-check   # Gera sem validação prévia
"""
import re, html as H, os, glob, sys

# Diretório base: onde este script está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Conteúdo do livro fica em python-basics/ (relativo ao BASE_DIR)
CONTENT_DIR = os.path.join(BASE_DIR, 'python-basics')

# ─── Definição da estrutura do livro ───────────────────────────────────────────

CAPITULOS = {
    1: {
        "titulo": "Fundamentos Teóricos",
        "descricao": "O que é programação, como os programas funcionam e como preparar seu ambiente de desenvolvimento.",
        "modulos": [
            "01-introducao-programacao.md",
            "02-scripts-compilados-vm.md",
            "03-preparacao-ambiente.md",
            "04-execucao-permissoes-pastas.md",
            "05-historia-python.md",
        ],
    },
    2: {
        "titulo": "Fundamentos da Linguagem",
        "descricao": "Os blocos básicos do Python: entrada e saída, variáveis, tipos, strings e operadores.",
        "modulos": [
            "06-entrada-saida.md",
            "06-entrada-saida-exercicios.md",
            "07-variaveis-tipos.md",
            "07-variaveis-tipos-exercicios.md",
            "08-conversao-tipos.md",
            "08-conversao-tipos-exercicios.md",
            "09-manipulacao-strings.md",
            "09-manipulacao-strings-exercicios.md",
            "10-indentacao-escopo.md",
            "10-indentacao-escopo-exercicios.md",
            "11-operadores.md",
            "11-operadores-exercicios.md",
        ],
    },
    3: {
        "titulo": "Controle de Fluxo",
        "descricao": "Tomando decisões e repetindo ações: condicionais, seletores e loops.",
        "modulos": [
            "12-condicionais.md",
            "12-condicionais-exercicios.md",
            "13-seletores-match-case.md",
            "13-seletores-match-case-exercicios.md",
            "14-controles-repeticao.md",
            "14-controles-repeticao-exercicios.md",
            "15-funcoes.md",
            "15-funcoes-exercicios.md",
            "16-exercicios-logica.md",
            "16-exercicios-logica-parte1.md",
            "16-exercicios-logica-parte2.md",
            "16-exercicios-logica-parte3.md",
            "16-exercicios-logica-parte4.md",
            "16-exercicios-logica-parte5.md",
        ],
    },
    4: {
        "titulo": "Tópicos Intermediários",
        "descricao": "Debugging, tratamento de erros, estruturas de dados, arquivos e JSON.",
        "modulos": [
            "17-debugging.md",
            "17-debugging-exercicios.md",
            "18-tratamento-erros.md",
            "18-tratamento-erros-exercicios.md",
            "19-estruturas-dados.md",
            "19-estruturas-dados-exercicios.md",
            "20-leitura-escrita-arquivos.md",
            "20-leitura-escrita-arquivos-exercicios.md",
            "21-manipulacao-json.md",
            "21-manipulacao-json-exercicios.md",
            "22-classes-objetos.md",
            "22-classes-objetos-exercicios.md",
            "23-exercicios-integradores.md",
        ],
    },
    5: {
        "titulo": "Organização e Boas Práticas",
        "descricao": "Módulos, imports, estruturação de projetos, pip e código limpo.",
        "modulos": [
            "24-modulos-imports.md",
            "24-modulos-imports-exercicios.md",
            "25-estruturacao-projetos.md",
            "25-estruturacao-projetos-exercicios.md",
            "26-pip-dependencias.md",
            "26-pip-dependencias-exercicios.md",
            "27-boas-praticas.md",
            "27-boas-praticas-exercicios.md",
            "28-modelagem-dados.md",
            "28-modelagem-dados-exercicios.md",
        ],
    },
    6: {
        "titulo": "Projeto CRUD — Do Zero à API",
        "descricao": "Construindo um sistema completo de cadastro de produtos em 4 fases progressivas.",
        "modulos": [
            "29-crud-memoria.md",
            "29-crud-memoria-exercicios.md",
            "30-crud-sqlite.md",
            "30-crud-sqlite-exercicios.md",
            "31-crud-fastapi.md",
            "31-crud-fastapi-exercicios.md",
            "32-crud-swagger.md",
            "32-crud-swagger-exercicios.md",
        ],
    },
    7: {
        "titulo": "Glossário",
        "descricao": "Referência completa de termos, conceitos e comandos utilizados ao longo do curso.",
        "modulos": [
            "00-glossario.md",
            "00-glossario-a-d.md",
            "00-glossario-e-i.md",
            "00-glossario-j-p.md",
            "00-glossario-q-z.md",
            "00-glossario-comandos.md",
        ],
    },
}


# ─── Regex para remover emojis e ícones ───────────────────────────────────────

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U00002702-\U000027B0"
    "\U0000FE00-\U0000FE0F"
    "\U0000200D"
    "\U000024C2-\U0001F251"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\U00002600-\U000026FF"
    "\U00002300-\U000023FF"
    "]+",
    flags=re.UNICODE
)

def strip_emojis(text):
    return EMOJI_RE.sub('', text)


# ─── Funções de conversão Markdown → HTML ─────────────────────────────────────

def ifmt(t):
    def code_replace(m):
        inner = H.escape(m.group(1))
        return f'<code>{inner}</code>'
    t = re.sub(r'`([^`]+)`', code_replace, t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'~~(.+?)~~', r'<del>\1</del>', t)
    def link_replace(m):
        text, url = m.group(1), m.group(2)
        if url.startswith('#') or url.endswith('.md') or url.startswith('cap') or url.startswith('../'):
            return text
        if text == url:
            return f'<a href="{url}">{text}</a>'
        return f'<a href="{url}">{text}</a> <span class="url-print">({url})</span>'
    t = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', link_replace, t)
    t = t.replace('[x]', '<span class="check-done">[x]</span>')
    t = t.replace('[ ]', '<span class="check-todo">[ ]</span>')
    t = strip_emojis(t)
    return t


def mkid(t):
    s = re.sub(r'[^a-zA-Z0-9\s-]', '', t.lower())
    s = re.sub(r'\s+', '-', s.strip())
    return re.sub(r'-+', '-', s)


def md2html(lines):
    out = []
    i = 0
    n = len(lines)
    while i < n:
        L = lines[i]

        # Filtrar linhas de navegação entre módulos (não fazem sentido no livro impresso)
        # Detecta no markdown cru, antes de qualquer processamento de links
        _L = L.strip()
        _is_nav = (
            # Setas Unicode: [← ...] ou linha começando com ←/→
            re.match(r'^\[?[←→]', _L)
            # ASCII: [<- ...] ou [... ->]
            or re.match(r'^\[<-\s', _L)
            or re.match(r'^<-\s', _L)
            # Padrões de texto de navegação comuns
            or 'Voltar ao Modulo' in _L
            or 'Voltar ao README' in _L
            or '← Voltar' in _L
            or '← Anterior' in _L
            or '<- Anterior' in _L
            or '<- Voltar' in _L
            or 'Próximo →' in _L
            or 'Próximo:' in _L
            or 'Proximo ->' in _L
            or 'Proximo:' in _L
            # Linhas de navegação entre partes (ex: [<- Parte 1] | [Voltar ao Modulo 16] | [Parte 3 ->])
            or (re.match(r'^\[<- Parte', _L))
            # "Ir para os Exercícios do Módulo X ->"
            or re.match(r'^Ir para os Exerc', _L)
            or re.match(r'^\[Ir para os Exerc', _L)
        )
        if _is_nav:
            i += 1
            continue

        # Mermaid blocks
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

        # UL
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


# ─── CSS do livro (mesmo padrão do Zero2Dev) ──────────────────────────────────

CSS = r"""
@page { size: A4; margin: 2.5cm 2cm 2.5cm 2.5cm; @bottom-center { content: counter(page); font-family: 'JetBrains Mono',monospace; font-size: 9pt; color: #888; } }
@page :first { @bottom-center { content: none; } }
*{box-sizing:border-box}
body{font-family:'Inter','Segoe UI','Helvetica Neue',Arial,sans-serif;font-size:11pt;line-height:1.7;color:#1a1a1a;margin:0;padding:0;background:#fff}

/* Capa */
.cover{page-break-after:always;display:flex;flex-direction:column;justify-content:center;align-items:center;min-height:92vh;text-align:center;padding:4cm 2cm;background:linear-gradient(135deg,#111 0%,#1a1a1a 50%,#111 100%);color:#fff}
.cover h1{font-size:36pt;color:#3b82f6;margin-bottom:.2em;border:none;letter-spacing:2px;font-family:'JetBrains Mono','Fira Code',monospace;font-weight:700}
.cover .subtitle{font-size:14pt;color:#a3a3a3;font-style:italic;margin-bottom:2em;max-width:80%;line-height:1.8;font-family:'Inter',sans-serif}
.cover .author{font-size:13pt;color:#e5e5e5;margin-bottom:.5em}
.cover .version{font-size:10pt;color:#737373;margin-top:2em}
.cover .line{width:40%;height:2px;background:linear-gradient(90deg,transparent,#3b82f6,transparent);margin:1.5em auto}

/* Prefácio e Introdução */
.preface{page-break-after:always;padding:2em 0}
.preface h2{font-size:20pt;color:#1a1a1a;border-bottom:2px solid #3b82f6;padding-bottom:.3em;margin-bottom:1em}
.preface p{text-align:justify;margin:.8em 0;line-height:1.8}

/* Sumário */
.toc{page-break-after:always;padding-top:2em}
.toc h2{font-size:20pt;text-align:center;margin-bottom:1.5em;border:none;color:#1a1a1a}
.toc .toc-chapter{font-size:11pt;font-weight:bold;color:#1a1a1a;margin-top:1.2em;margin-bottom:.3em;padding-bottom:.2em;border-bottom:1px solid #3b82f6;font-family:'JetBrains Mono',monospace}
.toc .toc-entry{display:flex;justify-content:space-between;align-items:baseline;padding:.12em 0 .12em 1.2em;font-size:9.5pt}
.toc .toc-entry a{color:#1a1a1a;text-decoration:none}
.toc .toc-entry a:hover{color:#1d4ed8}
.toc .toc-dots{flex:1;border-bottom:1px dotted #d4d4d4;margin:0 .5em;min-width:2em}
.toc .toc-exercise{font-style:italic;color:#737373}

/* Quebras de página */
.page-break{page-break-before:always}

/* Cabeçalhos de capítulo */
h1.chapter-header{font-size:24pt;color:#1a1a1a;border-bottom:3px solid #3b82f6;padding-bottom:.3em;margin-top:0;margin-bottom:.5em;font-family:'JetBrains Mono','Fira Code',monospace;font-weight:700}
h1.chapter-header .chapter-desc{display:block;font-size:11pt;font-weight:normal;color:#737373;font-style:italic;margin-top:.3em}

/* Cabeçalhos de módulo */
h1.module-header{font-size:20pt;color:#1a1a1a;border-bottom:2px solid #3b82f6;padding-bottom:.2em;margin-top:0;margin-bottom:.8em}

/* Cabeçalhos gerais */
h1{font-size:20pt;color:#1a1a1a;border-bottom:2px solid #3b82f6;padding-bottom:.2em;margin-top:1.5em;font-family:'JetBrains Mono','Fira Code',monospace;font-weight:700}
h2{font-size:15pt;color:#292929;border-bottom:1px solid #e5e5e5;padding-bottom:.2em;margin-top:1.5em;font-family:'Inter',sans-serif;font-weight:600}
h3{font-size:13pt;color:#1a1a1a;margin-top:1.2em;font-family:'Inter',sans-serif;font-weight:600}
h4{font-size:11pt;color:#404040;margin-top:1em;font-weight:600;font-family:'Inter',sans-serif}
h5{font-size:10pt;color:#525252;margin-top:.8em}
h6{font-size:9.5pt;color:#737373;margin-top:.6em}

/* Texto */
p{margin:.6em 0;text-align:justify;orphans:3;widows:3}
a{color:#1d4ed8;text-decoration:none}
a:hover{text-decoration:underline;color:#1e40af}
code{font-family:'JetBrains Mono','Fira Code','Courier New',monospace;font-size:9pt;background:#eff6ff;padding:.15em .4em;border-radius:3px;color:#1d4ed8;border:1px solid #bfdbfe}
pre{background:#1a1a1a;border:1px solid #404040;border-radius:6px;padding:1em 1.2em;overflow-x:auto;font-size:9pt;line-height:1.5;page-break-inside:avoid;margin:.8em 0;position:relative}
pre code{background:none;padding:0;color:#e5e5e5;font-size:9pt;border:none}

/* Tabelas */
table{width:100%;border-collapse:collapse;margin:.8em 0;font-size:10pt;page-break-inside:avoid;border-radius:6px;overflow:hidden}
th,td{border:1px solid #d4d4d4;padding:.5em .7em;text-align:left;vertical-align:top}
th{background:#1a1a1a;color:#3b82f6;font-weight:600;font-size:9.5pt}
tr:nth-child(even){background:#fafafa}
tr:hover{background:#eff6ff}

/* Blockquote */
blockquote{border-left:4px solid #3b82f6;margin:.8em 0;padding:.6em 1.2em;color:#525252;background:#eff6ff;border-radius:0 6px 6px 0;font-style:italic}

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

/* Exercícios */
.exercise-header{background:linear-gradient(135deg,#eff6ff,#dbeafe);border:1px solid #bfdbfe;border-radius:8px;padding:.8em 1.2em;margin:1.5em 0 1em 0}
.exercise-header h2{border:none;margin:0;color:#1d4ed8;font-size:14pt;font-family:'JetBrains Mono',monospace;font-weight:700}

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
<h1>Python Basics</h1>
<div class="line"></div>
<div class="subtitle">Curso Completo de Programa&ccedil;&atilde;o com Python<br/>
Do zero absoluto &agrave; constru&ccedil;&atilde;o de uma API real &mdash; um guia completo para quem quer aprender a programar.</div>
<div class="line"></div>
<div class="author">Rafael Gottardi (Fino)</div>
<div class="version">Vers&atilde;o 1.0 &mdash; 2026</div>
</div>"""

# ─── Prefácio ─────────────────────────────────────────────────────────────────

PREFACIO = """<div class="preface page-break">
<h2>Pref&aacute;cio</h2>

<p>Este livro nasceu de uma pergunta simples: por que aprender a programar ainda parece t&atilde;o dif&iacute;cil para quem come&ccedil;a do zero?</p>

<p>N&atilde;o &eacute; por falta de material. Existe conte&uacute;do de sobra na internet. O problema &eacute; que a maioria desse material foi escrito por programadores para programadores &mdash; assumindo conhecimento pr&eacute;vio, pulando etapas, usando jarg&atilde;o sem explicar. Quem est&aacute; come&ccedil;ando fica perdido logo nas primeiras p&aacute;ginas.</p>

<p>Este livro foi escrito de forma diferente. Cada conceito &eacute; apresentado como se o leitor nunca tivesse visto uma linha de c&oacute;digo. Cada termo t&eacute;cnico &eacute; explicado na primeira vez que aparece. Cada exemplo pode ser copiado e executado imediatamente. N&atilde;o h&aacute; saltos, n&atilde;o h&aacute; &ldquo;&eacute; &oacute;bvio que&rdquo;, n&atilde;o h&aacute; &ldquo;como voc&ecirc; j&aacute; sabe&rdquo;.</p>

<p>Python foi escolhido como linguagem por tr&ecirc;s raz&otilde;es: &eacute; simples de ler, &eacute; amplamente usado no mercado e &eacute; vers&aacute;til o suficiente para ir do primeiro &ldquo;Ol&aacute;, mundo!&rdquo; at&eacute; uma API profissional com documenta&ccedil;&atilde;o autom&aacute;tica.</p>

<p>O material cobre 32 m&oacute;dulos organizados em ordem progressiva, do mais simples ao mais complexo. Come&ccedil;a com o que &eacute; um programa de computador e termina com um sistema completo de cadastro de produtos com banco de dados, interface web e documenta&ccedil;&atilde;o de API. Cada m&oacute;dulo tem teoria, exemplos pr&aacute;ticos e exerc&iacute;cios com respostas comentadas.</p>

<p>Dois princ&iacute;pios guiam todo o conte&uacute;do:</p>

<p><strong>&ldquo;Voc&ecirc; aprende programando, n&atilde;o lendo sobre programar&rdquo;</strong> &mdash; Por isso cada m&oacute;dulo tem exerc&iacute;cios pr&aacute;ticos. Leia a teoria, execute os exemplos, resolva os exerc&iacute;cios. N&atilde;o pule essa etapa.</p>

<p><strong>&ldquo;Conceitos s&atilde;o para sempre, sintaxe voc&ecirc; consulta&rdquo;</strong> &mdash; N&atilde;o tente memorizar comandos. Entenda o que cada conceito faz e por qu&ecirc;. A sintaxe voc&ecirc; encontra no gloss&aacute;rio ou na documenta&ccedil;&atilde;o. O racioc&iacute;nio l&oacute;gico &eacute; o que fica.</p>

<p>Se algo parecer dif&iacute;cil, releia, pratique e pe&ccedil;a ajuda. Todo programador j&aacute; esteve onde voc&ecirc; est&aacute; agora. A &uacute;nica diferen&ccedil;a entre um iniciante e um profissional &eacute; o tempo de pr&aacute;tica.</p>

<p style="text-align:right;margin-top:2em;color:#737373;font-style:italic">&mdash; Fino, 2026</p>
</div>"""

# ─── Introdução ───────────────────────────────────────────────────────────────

INTRODUCAO = """<div class="preface page-break">
<h2>Introdu&ccedil;&atilde;o</h2>

<h3>Para quem &eacute; este livro</h3>

<p>Este livro foi escrito para quem nunca programou. Se voc&ecirc; nunca abriu um terminal, nunca escreveu uma linha de c&oacute;digo, nunca ouviu falar de vari&aacute;veis ou fun&ccedil;&otilde;es &mdash; este livro &eacute; para voc&ecirc;. N&atilde;o assumimos nenhum conhecimento pr&eacute;vio al&eacute;m de saber usar um computador para tarefas b&aacute;sicas.</p>

<p>Tamb&eacute;m &eacute; &uacute;til para quem j&aacute; tentou aprender a programar antes e desistiu por achar dif&iacute;cil demais. A abordagem aqui &eacute; diferente: passo a passo, sem pular etapas, com exemplos do dia a dia.</p>

<h3>Como este livro est&aacute; organizado</h3>

<p>O conte&uacute;do est&aacute; dividido em 7 cap&iacute;tulos, cada um com m&uacute;ltiplos m&oacute;dulos. Os cap&iacute;tulos s&atilde;o sequenciais &mdash; cada um depende dos anteriores. Siga na ordem.</p>

<table>
<thead><tr><th>Cap&iacute;tulo</th><th>Conte&uacute;do</th><th>M&oacute;dulos</th></tr></thead>
<tbody>
<tr><td>1</td><td>Fundamentos Te&oacute;ricos</td><td>01 a 05</td></tr>
<tr><td>2</td><td>Fundamentos da Linguagem</td><td>06 a 11</td></tr>
<tr><td>3</td><td>Controle de Fluxo</td><td>12 a 16</td></tr>
<tr><td>4</td><td>T&oacute;picos Intermedi&aacute;rios</td><td>17 a 23</td></tr>
<tr><td>5</td><td>Organiza&ccedil;&atilde;o e Boas Pr&aacute;ticas</td><td>24 a 28</td></tr>
<tr><td>6</td><td>Projeto CRUD &mdash; Do Zero &agrave; API</td><td>29 a 32</td></tr>
<tr><td>7</td><td>Gloss&aacute;rio</td><td>Refer&ecirc;ncia</td></tr>
</tbody>
</table>

<h3>Estrutura de cada m&oacute;dulo</h3>

<p>Cada m&oacute;dulo de conte&uacute;do &eacute; acompanhado de um m&oacute;dulo de exerc&iacute;cios. Os exerc&iacute;cios t&ecirc;m enunciado, dicas, proposta de teste e resposta comentada. Tente resolver sozinho antes de consultar a resposta.</p>

<h3>O projeto final</h3>

<p>O cap&iacute;tulo 6 constr&oacute;i um sistema completo de cadastro de produtos em 4 fases progressivas:</p>

<ol>
<li><strong>CRUD em mem&oacute;ria</strong> &mdash; usando listas e dicion&aacute;rios</li>
<li><strong>CRUD com SQLite</strong> &mdash; persistindo dados em banco de dados</li>
<li><strong>CRUD com FastAPI</strong> &mdash; expondo o sistema como uma API web</li>
<li><strong>CRUD com Swagger</strong> &mdash; documentando a API automaticamente</li>
</ol>

<h3>Conven&ccedil;&otilde;es do livro</h3>

<p>C&oacute;digo Python aparece em blocos com destaque de sintaxe. Todos os exemplos podem ser copiados e executados diretamente. Coment&aacute;rios no c&oacute;digo est&atilde;o sempre em portugu&ecirc;s.</p>

<p>Termos t&eacute;cnicos em ingl&ecirc;s s&atilde;o traduzidos e explicados na primeira ocorr&ecirc;ncia. O gloss&aacute;rio no cap&iacute;tulo 7 cont&eacute;m todos os termos com explica&ccedil;&otilde;es detalhadas.</p>

<p>Blocos de exerc&iacute;cios s&atilde;o identificados visualmente com fundo azul claro.</p>

<h3>Requisitos</h3>

<p>Para acompanhar este livro voc&ecirc; precisa de um computador com Linux, Python 3 instalado e um editor de c&oacute;digo (recomendamos o VSCode). O m&oacute;dulo 03 explica como instalar tudo do zero.</p>
</div>"""


# ─── Funções auxiliares ───────────────────────────────────────────────────────

def find_modules(cap_num):
    """Retorna os arquivos de módulo de um capítulo na ordem definida."""
    cap_info = CAPITULOS[cap_num]
    files = []
    for fname in cap_info["modulos"]:
        path = os.path.join(CONTENT_DIR, fname)
        if os.path.exists(path):
            files.append(path)
    return files


def read_file(path):
    if not os.path.isabs(path):
        path = os.path.join(BASE_DIR, path)
    if not os.path.exists(path):
        return ""
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def get_first_h1(md_content):
    m = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
    return m.group(1).strip() if m else None


def build_book():
    all_modules = []
    body_parts = []

    for cap_num in sorted(CAPITULOS.keys()):
        cap_info = CAPITULOS[cap_num]
        cap_title = f"Capítulo {cap_num} — {cap_info['titulo']}"
        cap_id = mkid(cap_title)

        body_parts.append(f'<div class="page-break"></div>')
        body_parts.append(
            f'<h1 class="chapter-header" id="{cap_id}">{H.escape(cap_title)}'
            f'<span class="chapter-desc">{H.escape(cap_info["descricao"])}</span></h1>'
        )

        modules = find_modules(cap_num)
        for mod_path in modules:
            md_content = read_file(mod_path)
            if not md_content.strip():
                continue

            mod_title = get_first_h1(md_content) or os.path.basename(mod_path)
            mod_title = strip_emojis(mod_title)
            mod_id = mkid(mod_title)

            is_exercise = '-exercicios' in mod_path or 'exercicios-logica-parte' in mod_path

            all_modules.append({
                'cap': cap_num,
                'title': mod_title,
                'id': mod_id,
                'is_exercise': is_exercise,
            })

            body_parts.append(f'<div class="page-break"></div>')

            if is_exercise:
                body_parts.append(f'<div class="exercise-header"><h2>Exerc&iacute;cios</h2></div>')

            html_content = md2html(md_content.split('\n'))
            body_parts.append(html_content)

    body_html = '\n'.join(body_parts)

    # Remover as duas primeiras quebras de página (capítulo 1 + primeiro módulo)
    body_html = body_html.replace('<div class="page-break"></div>', '', 1)
    body_html = body_html.replace('<div class="page-break"></div>', '', 1)

    return body_html, all_modules


def build_toc(all_modules):
    h = '<div class="toc"><h2>Sum&aacute;rio</h2>\n'

    current_cap = None
    for mod in all_modules:
        if mod['cap'] != current_cap:
            current_cap = mod['cap']
            cap_info = CAPITULOS[current_cap]
            cap_label = f"Capítulo {current_cap} — {cap_info['titulo']}"
            h += f'<div class="toc-chapter">{H.escape(cap_label)}</div>\n'

        title = mod['title']
        aid = mod['id']
        css_class = ' toc-exercise' if mod['is_exercise'] else ''

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


# ─── Validação: Ortografia via aspell ────────────────────────────────────────
#
# Usa `aspell --lang=pt_BR` para detectar erros reais.
# Palavras técnicas, inglês e nomes de arquivo são ignorados via lista de
# exceções (ASPELL_IGNORAR). O arquivo .aspell-python-basics.pws persiste
# novas exceções adicionadas pelo usuário entre execuções.
#
# Instalar dicionário (uma vez):
#   sudo apt install aspell aspell-pt-br
#
# Fluxo:
#   --validate  → lista erros por arquivo, não gera HTML
#   --fix       → abre aspell interativo em cada arquivo com erros, depois gera
#   (padrão)    → lista erros como aviso, gera HTML mesmo assim
#   --no-check  → pula validação completamente

import subprocess
import shutil

# Arquivo de palavras pessoais (persiste entre execuções)
ASPELL_PWS = os.path.join(BASE_DIR, '.aspell-python-basics.pws')

# Termos técnicos, inglês e padrões que o aspell pt_BR não conhece mas são válidos
# Adicione aqui palavras que aparecem como falso positivo e não devem ser corrigidas
ASPELL_IGNORAR = {
    # Linguagens e tecnologias
    "python", "Python", "fastapi", "FastAPI", "sqlite", "SQLite", "swagger", "Swagger",
    "pydantic", "Pydantic", "uvicorn", "pip", "venv", "virtualenv", "pyenv",
    "linux", "Linux", "windows", "Windows", "macos", "MacOS", "ubuntu", "Ubuntu",
    "vscode", "VSCode", "git", "Git", "github", "GitHub", "docker", "Docker",
    "html", "HTML", "css", "CSS", "json", "JSON", "yaml", "YAML", "xml", "XML",
    "http", "HTTP", "https", "HTTPS", "api", "API", "rest", "REST", "crud", "CRUD",
    "sql", "SQL", "nosql", "NoSQL", "orm", "ORM",
    # Palavras-chave Python
    "def", "class", "return", "import", "from", "if", "else", "elif", "for",
    "while", "try", "except", "finally", "with", "as", "pass", "break",
    "continue", "lambda", "yield", "async", "await", "True", "False", "None",
    "and", "or", "not", "in", "is", "global", "nonlocal", "del", "raise",
    # Tipos e builtins Python
    "int", "str", "float", "bool", "list", "dict", "tuple", "set", "type",
    "print", "input", "len", "range", "open", "read", "write", "append",
    "format", "split", "strip", "join", "replace", "lower", "upper",
    "isinstance", "hasattr", "getattr", "setattr", "super", "self",
    "enumerate", "zip", "map", "filter", "sorted", "reversed",
    # Termos técnicos gerais
    "backend", "frontend", "endpoint", "middleware", "framework", "runtime",
    "deploy", "debug", "debugger", "breakpoint", "stack", "heap", "cache",
    "token", "hash", "encode", "decode", "parse", "serialize", "deserialize",
    "callback", "handler", "wrapper", "decorator", "iterator", "generator",
    "boolean", "booleano", "booleanos", "Booleano", "Booleanos",
    "string", "strings", "integer", "float", "array", "object", "null",
    "loop", "loops", "script", "scripts", "log", "logs", "output", "input",
    "status", "request", "response", "header", "body", "payload",
    "router", "route", "schema", "model", "query", "index",
    # Inglês técnico comum
    "case", "match", "default", "switch", "override", "abstract", "interface",
    "getter", "setter", "method", "attribute", "instance", "constructor",
    "namespace", "module", "package", "library", "dependency", "version",
    "commit", "branch", "merge", "pull", "push", "clone", "fork",
    "container", "image", "volume", "network", "port", "host",
    # Abreviações e siglas
    "PEP", "OOP", "DRY", "SOLID", "MVC", "MVP", "CLI", "GUI", "IDE",
    "URL", "URI", "UUID", "JWT", "SSH", "SSL", "TLS", "TCP", "UDP",
    "RAM", "CPU", "GPU", "SSD", "HDD", "OS", "VM",
    # Nomes de arquivos e extensões (aparecem em exemplos)
    "py", "txt", "csv", "md", "env", "cfg", "ini", "toml", "req",
    "requirements", "setup", "config", "settings", "main", "app",
    # Termos do curso que o aspell não conhece mas estão corretos
    "booleano", "booleana", "booleanos", "booleanas",
    "indentacao", "Indentacao",  # título de módulo — será corrigido pelo fix
    # Inglês técnico que aparece em títulos de links e referências nos glossários
    "Introduction", "Getting", "Started", "Application", "Programming",
    "What", "Functions", "imports", "Imports", "Requests", "Exception",
    "Operators", "Formatting", "Asked", "Frequently", "Questions", "APIs",
    "bytecode", "CamelCase", "Variables", "Notation", "JavaScript",
    "Methods", "Dictionary", "change", "directory", "working", "home",
    "command", "found", "such", "Permission", "denied", "Debugging",
    "Debugging", "debugging",
}


def _aspell_disponivel():
    """Verifica se aspell com dicionário pt_BR está instalado."""
    if not shutil.which("aspell"):
        return False, "aspell não encontrado. Instale com: sudo apt install aspell aspell-pt-br"
    result = subprocess.run(
        ["aspell", "dump", "dicts"],
        capture_output=True, text=True
    )
    if "pt_BR" not in result.stdout:
        return False, "Dicionário pt_BR não encontrado. Instale com: sudo apt install aspell-pt-br"
    return True, ""


def _extrair_texto_md(content):
    """Extrai linhas de texto fora de code fences e inline code."""
    lines = content.split('\n')
    resultado = []
    in_code = False
    fence = None
    for i, L in enumerate(lines):
        # Detectar abertura/fechamento de code fence
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
        # Pular linhas que são só URLs, imagens ou links de navegação
        stripped = L.strip()
        if stripped.startswith('http') or stripped.startswith('!['):
            continue
        # Remover inline code antes de passar pro aspell
        L_sem_code = re.sub(r'`[^`]+`', ' ', L)
        # Remover links markdown — manter só o texto
        L_sem_code = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', L_sem_code)
        resultado.append((i + 1, L_sem_code))
    return resultado


def _carregar_pws():
    """Carrega palavras do arquivo .pws pessoal."""
    palavras = set()
    if os.path.exists(ASPELL_PWS):
        with open(ASPELL_PWS, 'r', encoding='utf-8') as f:
            for linha in f:
                w = linha.strip()
                if w and not w.startswith('personal_ws'):
                    palavras.add(w)
    return palavras


def _salvar_pws(palavras):
    """Salva palavras no arquivo .pws pessoal."""
    with open(ASPELL_PWS, 'w', encoding='utf-8') as f:
        f.write(f"personal_ws-1.1 pt_BR {len(palavras)}\n")
        for w in sorted(palavras):
            f.write(w + '\n')


def _verificar_com_aspell(texto):
    """Passa texto pelo aspell e retorna set de palavras sinalizadas."""
    cmd = ["aspell", "--lang=pt_BR", "--encoding=utf-8", "list"]
    if os.path.exists(ASPELL_PWS):
        cmd += [f"--personal={ASPELL_PWS}"]
    result = subprocess.run(cmd, input=texto, capture_output=True, text=True, encoding='utf-8')
    return set(w.strip() for w in result.stdout.splitlines() if w.strip())


def _e_palavra_ignorada(palavra, ignorar_extra=None):
    """Retorna True se a palavra deve ser ignorada na validação."""
    ignorar = ASPELL_IGNORAR | (ignorar_extra or set())
    # Ignorar a palavra exata, versão lower e versão capitalizada
    if palavra in ignorar or palavra.lower() in ignorar or palavra.capitalize() in ignorar:
        return True
    # Ignorar palavras que parecem nomes de arquivo (contêm - ou _)
    if '-' in palavra or '_' in palavra:
        return True
    # Ignorar siglas (tudo maiúsculo com 2+ letras)
    if palavra.isupper() and len(palavra) >= 2:
        return True
    # Ignorar números e palavras com dígitos
    if re.search(r'\d', palavra):
        return True
    # Ignorar palavras muito curtas (2 letras ou menos)
    if len(palavra) <= 2:
        return True
    return False


def validar_ortografia(arquivos):
    """Valida ortografia usando aspell pt_BR. Retorna total de problemas."""
    ok, msg = _aspell_disponivel()
    if not ok:
        print(f"  AVISO: {msg}")
        print("  Validação de ortografia ignorada.")
        return 0

    pws_extra = _carregar_pws()
    total = 0

    for arq in arquivos:
        with open(arq, 'r', encoding='utf-8') as f:
            content = f.read()

        linhas = _extrair_texto_md(content)
        # Montar texto com marcadores de linha para rastrear posição
        texto_para_checar = '\n'.join(L for _, L in linhas)

        sinalizadas = _verificar_com_aspell(texto_para_checar)

        # Filtrar falsos positivos
        erros_reais = {
            w for w in sinalizadas
            if not _e_palavra_ignorada(w, pws_extra)
        }

        if not erros_reais:
            continue

        # Encontrar número de linha de cada erro
        problemas = []
        for line_num, linha in linhas:
            for palavra in erros_reais:
                if re.search(r'\b' + re.escape(palavra) + r'\b', linha):
                    problemas.append((line_num, palavra))

        # Deduplicar e ordenar
        vistos = set()
        problemas_unicos = []
        for ln, p in sorted(problemas):
            if p not in vistos:
                vistos.add(p)
                problemas_unicos.append((ln, p))

        if problemas_unicos:
            total += len(problemas_unicos)
            nome = os.path.relpath(arq, BASE_DIR)
            print(f"  {nome}: {len(problemas_unicos)} palavra(s) suspeita(s)")
            for ln, palavra in problemas_unicos[:8]:
                print(f"    L{ln}: {palavra}")
            if len(problemas_unicos) > 8:
                print(f"    ... e mais {len(problemas_unicos) - 8}")

    return total


def corrigir_ortografia_interativo(arquivos):
    """Abre aspell interativo para cada arquivo com erros."""
    ok, msg = _aspell_disponivel()
    if not ok:
        print(f"  AVISO: {msg}")
        return 0, 0

    modificados = 0
    total_arquivos = 0

    for arq in arquivos:
        # Verificar se tem erros antes de abrir interativo
        with open(arq, 'r', encoding='utf-8') as f:
            content = f.read()
        linhas = _extrair_texto_md(content)
        texto = '\n'.join(L for _, L in linhas)
        sinalizadas = _verificar_com_aspell(texto)
        pws_extra = _carregar_pws()
        erros = {w for w in sinalizadas if not _e_palavra_ignorada(w, pws_extra)}

        if not erros:
            continue

        total_arquivos += 1
        nome = os.path.relpath(arq, BASE_DIR)
        print(f"\n  Abrindo aspell em: {nome} ({len(erros)} suspeita(s))")

        mtime_antes = os.path.getmtime(arq)
        cmd = ["aspell", "--lang=pt_BR", "--encoding=utf-8", "check"]
        if os.path.exists(ASPELL_PWS):
            cmd += [f"--personal={ASPELL_PWS}"]
        cmd.append(arq)

        subprocess.run(cmd)

        if os.path.getmtime(arq) != mtime_antes:
            modificados += 1
            print(f"    Arquivo modificado.")

    return total_arquivos, modificados


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
                bt = sum(1 for c in stripped if c == '`') if all(c == '`' for c in stripped[:3]) else 3
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
    return sorted(glob.glob(os.path.join(CONTENT_DIR, '*.md')))


# Manter compatibilidade: corrigir_ortografia chama o modo interativo
def corrigir_ortografia(arquivos):
    total_arqs, modificados = corrigir_ortografia_interativo(arquivos)
    return modificados, total_arqs


# ─── Correção automática (--fix-auto) ────────────────────────────────────────
# Tabela de substituições seguras: palavra sem acento → com acento.
# Só inclui casos onde a forma sem acento NUNCA é válida em português.
# Aplicada apenas fora de code fences e inline code.

CORRECOES_AUTO = {
    # Palavras de alta frequência nos arquivos (top erros do --validate)
    "Glossario": "Glossário", "glossario": "glossário",
    "Exercicios": "Exercícios", "exercicios": "exercícios",
    "Exercicio": "Exercício", "exercicio": "exercício",
    "Introducao": "Introdução", "introducao": "introdução",
    "Proximo": "Próximo", "proximo": "próximo",
    "comecar": "começar", "Comecar": "Começar",
    "atencao": "atenção", "Atencao": "Atenção",
    "solucao": "solução", "Solucao": "Solução",
    "solucoes": "soluções", "Solucoes": "Soluções",
    "codigo": "código", "Codigo": "Código",
    "codigos": "códigos", "Codigos": "Códigos",
    "Basico": "Básico", "basico": "básico",
    "Basica": "Básica", "basica": "básica",
    "Basicos": "Básicos", "basicos": "básicos",
    "Basicas": "Básicas", "basicas": "básicas",
    "Nivel": "Nível", "nivel": "nível",
    "Niveis": "Níveis", "niveis": "níveis",
    "Manipulacao": "Manipulação", "manipulacao": "manipulação",
    "Repeticao": "Repetição", "repeticao": "repetição",
    "Funcoes": "Funções", "funcoes": "funções",
    "Funcao": "Função", "funcao": "função",
    "Dependencias": "Dependências", "dependencias": "dependências",
    "Dependencia": "Dependência", "dependencia": "dependência",
    "Conversao": "Conversão", "conversao": "conversão",
    "Programacao": "Programação", "programacao": "programação",
    "Estruturacao": "Estruturação", "estruturacao": "estruturação",
    "Variaveis": "Variáveis", "variaveis": "variáveis",
    "Variavel": "Variável", "variavel": "variável",
    "Modulos": "Módulos", "modulos": "módulos",
    "Modulo": "Módulo", "modulo": "módulo",
    "Nao": "Não", "nao": "não",
    "Voce": "Você", "voce": "você",
    "informacoes": "informações", "Informacoes": "Informações",
    "informacao": "informação", "Informacao": "Informação",
    "Parabens": "Parabéns", "parabens": "parabéns",
    "numeros": "números", "Numeros": "Números",
    "numero": "número", "Numero": "Número",
    "estao": "estão", "Estao": "Estão",
    "sao": "são",
    "Imports": "Imports",  # já correto, manter
    "Documentacao": "Documentação", "documentacao": "documentação",
    "Configuracao": "Configuração", "configuracao": "configuração",
    "Atualizacao": "Atualização", "atualizacao": "atualização",
    "Operacao": "Operação", "operacao": "operação",
    "Operacoes": "Operações", "operacoes": "operações",
    "Aplicacao": "Aplicação", "aplicacao": "aplicação",
    "Aplicacoes": "Aplicações", "aplicacoes": "aplicações",
    "Execucao": "Execução", "execucao": "execução",
    "Instrucao": "Instrução", "instrucao": "instrução",
    "Instrucoes": "Instruções", "instrucoes": "instruções",
    "Versao": "Versão", "versao": "versão",
    "Permissao": "Permissão", "permissao": "permissão",
    "Permissoes": "Permissões", "permissoes": "permissões",
    "Validacao": "Validação", "validacao": "validação",
    "Criacao": "Criação", "criacao": "criação",
    "Iteracao": "Iteração", "iteracao": "iteração",
    "Atribuicao": "Atribuição", "atribuicao": "atribuição",
    "Definicao": "Definição", "definicao": "definição",
    "Definicoes": "Definições", "definicoes": "definições",
    "Colecao": "Coleção", "colecao": "coleção",
    "Colecoes": "Coleções", "colecoes": "coleções",
    "Posicao": "Posição", "posicao": "posição",
    "Transacao": "Transação", "transacao": "transação",
    "Transacoes": "Transações", "transacoes": "transações",
    "Notacao": "Notação", "notacao": "notação",
    "Relacao": "Relação", "relacao": "relação",
    "Relacoes": "Relações", "relacoes": "relações",
    "Padrao": "Padrão", "padrao": "padrão",
    "Padroes": "Padrões", "padroes": "padrões",
    "Entao": "Então", "entao": "então",
    "Tambem": "Também", "tambem": "também",
    "Alem": "Além", "alem": "além",
    "Porem": "Porém", "porem": "porém",
    "Atraves": "Através", "atraves": "através",
    "Facil": "Fácil", "facil": "fácil",
    "Dificil": "Difícil", "dificil": "difícil",
    "Possivel": "Possível", "possivel": "possível",
    "Disponivel": "Disponível", "disponivel": "disponível",
    "Analise": "Análise", "analise": "análise",
    "Metodo": "Método", "metodo": "método",
    "Metodos": "Métodos", "metodos": "métodos",
    "Conteudo": "Conteúdo", "conteudo": "conteúdo",
    "Titulo": "Título", "titulo": "título",
    "Titulos": "Títulos", "titulos": "títulos",
    "Rapido": "Rápido", "rapido": "rápido",
    "Ultimo": "Último", "ultimo": "último",
    "Minimo": "Mínimo", "minimo": "mínimo",
    "Maximo": "Máximo", "maximo": "máximo",
    "Necessario": "Necessário", "necessario": "necessário",
    "Necessaria": "Necessária", "necessaria": "necessária",
    "Necessarios": "Necessários", "necessarios": "necessários",
    "Diretorio": "Diretório", "diretorio": "diretório",
    "Diretorios": "Diretórios", "diretorios": "diretórios",
    "Repositorio": "Repositório", "repositorio": "repositório",
    "Comentario": "Comentário", "comentario": "comentário",
    "Comentarios": "Comentários", "comentarios": "comentários",
    "Dicionario": "Dicionário", "dicionario": "dicionário",
    "Dicionarios": "Dicionários", "dicionarios": "dicionários",
    "Sequencia": "Sequência", "sequencia": "sequência",
    "Referencia": "Referência", "referencia": "referência",
    "Referencias": "Referências", "referencias": "referências",
    "Experiencia": "Experiência", "experiencia": "experiência",
    "Diferenca": "Diferença", "diferenca": "diferença",
    "Seguranca": "Segurança", "seguranca": "segurança",
    "Instancia": "Instância", "instancia": "instância",
    "Instancias": "Instâncias", "instancias": "instâncias",
    "Eficiencia": "Eficiência", "eficiencia": "eficiência",
    "Persistencia": "Persistência", "persistencia": "persistência",
    "Consistencia": "Consistência", "consistencia": "consistência",
    "Inteligencia": "Inteligência", "inteligencia": "inteligência",
    "Acao": "Ação", "acao": "ação",
    "Acoes": "Ações", "acoes": "ações",
    "Manutencao": "Manutenção", "manutencao": "manutenção",
    "Producao": "Produção", "producao": "produção",
    "Insercao": "Inserção", "insercao": "inserção",
    "Remocao": "Remoção", "remocao": "remoção",
    "Selecao": "Seleção", "selecao": "seleção",
    "Geracao": "Geração", "geracao": "geração",
    "Utilizacao": "Utilização", "utilizacao": "utilização",
    "Otimizacao": "Otimização", "otimizacao": "otimização",
    "Inicializacao": "Inicialização", "inicializacao": "inicialização",
    "Serializacao": "Serialização", "serializacao": "serialização",
    "Normalizacao": "Normalização", "normalizacao": "normalização",
    "Pagina": "Página", "pagina": "página",
    "Paginas": "Páginas", "paginas": "páginas",
    "Maquina": "Máquina", "maquina": "máquina",
    "Calculo": "Cálculo", "calculo": "cálculo",
    "Calculos": "Cálculos", "calculos": "cálculos",
    "Varias": "Várias", "varias": "várias",
    "Varios": "Vários", "varios": "vários",
    "Arvore": "Árvore", "arvore": "árvore",
    "Arvores": "Árvores", "arvores": "árvores",
    "Simbolo": "Símbolo", "simbolo": "símbolo",
    "Simbolos": "Símbolos", "simbolos": "símbolos",
    "Matematico": "Matemático", "matematico": "matemático",
    "Matematica": "Matemática", "matematica": "matemática",
    "Binario": "Binário", "binario": "binário",
    "Aritmetico": "Aritmético", "aritmetico": "aritmético",
    "Semantico": "Semântico", "semantico": "semântico",
    "Sintatico": "Sintático", "sintatico": "sintático",
    "Dinamico": "Dinâmico", "dinamico": "dinâmico",
    "Dinamica": "Dinâmica", "dinamica": "dinâmica",
    "Estatico": "Estático", "estatico": "estático",
    "Estatica": "Estática", "estatica": "estática",
    "Automatico": "Automático", "automatico": "automático",
    "Automatica": "Automática", "automatica": "automática",
    "Especifico": "Específico", "especifico": "específico",
    "Especifica": "Específica", "especifica": "específica",
    "Especificos": "Específicos", "especificos": "específicos",
    "Generico": "Genérico", "generico": "genérico",
    "Generica": "Genérica", "generica": "genérica",
    "Grafico": "Gráfico", "grafico": "gráfico",
    "Graficos": "Gráficos", "graficos": "gráficos",
    "Tecnico": "Técnico", "tecnico": "técnico",
    "Tecnica": "Técnica", "tecnica": "técnica",
    "Tecnicas": "Técnicas", "tecnicas": "técnicas",
    "Tecnicos": "Técnicos", "tecnicos": "técnicos",
    "Topico": "Tópico", "topico": "tópico",
    "Topicos": "Tópicos", "topicos": "tópicos",
    "Capitulo": "Capítulo", "capitulo": "capítulo",
    "Capitulos": "Capítulos", "capitulos": "capítulos",
    "Indice": "Índice", "indice": "índice",
    "Pratico": "Prático", "pratico": "prático",
    "Pratica": "Prática", "pratica": "prática",
    "Praticos": "Práticos", "praticos": "práticos",
    "Praticas": "Práticas", "praticas": "práticas",
    "Conclusao": "Conclusão", "conclusao": "conclusão",
    "Condicao": "Condição", "condicao": "condição",
    "Condicoes": "Condições", "condicoes": "condições",
    "Excecao": "Exceção", "excecao": "exceção",
    "Excecoes": "Exceções", "excecoes": "exceções",
    "Unico": "Único", "unico": "único",
    "Unica": "Única", "unica": "única",
    "Publico": "Público", "publico": "público",
    "Publica": "Pública", "publica": "pública",
    "Historico": "Histórico", "historico": "histórico",
    "Historia": "História", "historia": "história",
    "Memoria": "Memória", "memoria": "memória",
    "Logica": "Lógica", "logica": "lógica",
    "Conexao": "Conexão", "conexao": "conexão",
    "Conexoes": "Conexões", "conexoes": "conexões",
    "Extensao": "Extensão", "extensao": "extensão",
    "Extensoes": "Extensões", "extensoes": "extensões",
    "Restricao": "Restrição", "restricao": "restrição",
    "Restricoes": "Restrições", "restricoes": "restrições",
    "Distribuicao": "Distribuição", "distribuicao": "distribuição",
    "Substituicao": "Substituição", "substituicao": "substituição",
    "Construcao": "Construção", "construcao": "construção",
    "Reducao": "Redução", "reducao": "redução",
    "Educacao": "Educação", "educacao": "educação",
    "Autenticacao": "Autenticação", "autenticacao": "autenticação",
    "Autorizacao": "Autorização", "autorizacao": "autorização",
    "Virtualizacao": "Virtualização", "virtualizacao": "virtualização",
    "Comparacao": "Comparação", "comparacao": "comparação",
    "Classificacao": "Classificação", "classificacao": "classificação",
    "Ordenacao": "Ordenação", "ordenacao": "ordenação",
    "Alocacao": "Alocação", "alocacao": "alocação",
    "Migracao": "Migração", "migracao": "migração",
    "Navegacao": "Navegação", "navegacao": "navegação",
    "Organizacao": "Organização", "organizacao": "organização",
    "Integracao": "Integração", "integracao": "integração",
    "Interacao": "Interação", "interacao": "interação",
    "Alteracao": "Alteração", "alteracao": "alteração",
    "Protecao": "Proteção", "protecao": "proteção",
    "Comunicacao": "Comunicação", "comunicacao": "comunicação",
    "Implementacao": "Implementação", "implementacao": "implementação",
    "Compilacao": "Compilação", "compilacao": "compilação",
    "Gerencia": "Gerência", "gerencia": "gerência",
    "Ciencia": "Ciência", "ciencia": "ciência",
    "Frequencia": "Frequência", "frequencia": "frequência",
    "Importancia": "Importância", "importancia": "importância",
    "Ocorrencia": "Ocorrência", "ocorrencia": "ocorrência",
    "Ocorrencias": "Ocorrências", "ocorrencias": "ocorrências",
    "Consequencia": "Consequência", "consequencia": "consequência",
    "Consequencias": "Consequências", "consequencias": "consequências",
    "Presenca": "Presença", "presenca": "presença",
    "Ausencia": "Ausência", "ausencia": "ausência",
    "Licenca": "Licença", "licenca": "licença",
    "Concorrencia": "Concorrência", "concorrencia": "concorrência",
    "Preferencia": "Preferência", "preferencia": "preferência",
    "Existencia": "Existência", "existencia": "existência",
    "Heranca": "Herança", "heranca": "herança",
    "Potencia": "Potência", "potencia": "potência",
    "Essencia": "Essência", "essencia": "essência",
    "Cenario": "Cenário", "cenario": "cenário",
    "Cenarios": "Cenários", "cenarios": "cenários",
    "Criterio": "Critério", "criterio": "critério",
    "Criterios": "Critérios", "criterios": "critérios",
    "Relatorio": "Relatório", "relatorio": "relatório",
    "Formulario": "Formulário", "formulario": "formulário",
    "Responsavel": "Responsável", "responsavel": "responsável",
    "Compativel": "Compatível", "compativel": "compatível",
    "Util": "Útil", "util": "útil",
    "Uteis": "Úteis", "uteis": "úteis",
    "Visivel": "Visível", "visivel": "visível",
    "Acessivel": "Acessível", "acessivel": "acessível",
    "Flexivel": "Flexível", "flexivel": "flexível",
    "Volatil": "Volátil", "volatil": "volátil",
    "Portatil": "Portátil", "portatil": "portátil",
    "Periodo": "Período", "periodo": "período",
    "Valido": "Válido", "valido": "válido",
    "Valida": "Válida",  # cuidado: "valida" pode ser verbo — só corrigir maiúsculo
    "Invalido": "Inválido", "invalido": "inválido",
    "Invalida": "Inválida", "invalida": "inválida",
    "Obrigatorio": "Obrigatório", "obrigatorio": "obrigatório",
    "Obrigatoria": "Obrigatória", "obrigatoria": "obrigatória",
    "Obrigatorios": "Obrigatórios", "obrigatorios": "obrigatórios",
    "Temporario": "Temporário", "temporario": "temporário",
    "Temporaria": "Temporária", "temporaria": "temporária",
    "Primario": "Primário", "primario": "primário",
    "Secundario": "Secundário", "secundario": "secundário",
    "Fabrica": "Fábrica", "fabrica": "fábrica",
    "Cracha": "Crachá", "cracha": "crachá",
    "acucar": "açúcar", "Acucar": "Açúcar",
    "Pagina": "Página", "pagina": "página",
}

# Palavras que são válidas sem acento em alguns contextos — não corrigir automaticamente
_CORRECOES_SKIP = {"sao", "valida", "ate", "nos", "so", "ja"}

_AUTO_KEYS = sorted(
    (k for k in CORRECOES_AUTO if k not in _CORRECOES_SKIP and CORRECOES_AUTO[k] != k),
    key=len, reverse=True
)
_AUTO_PATTERN = re.compile(r'\b(' + '|'.join(re.escape(k) for k in _AUTO_KEYS) + r')\b')


def corrigir_ortografia_auto(arquivos):
    """Aplica correções automáticas de acentuação fora de code fences."""
    total_correcoes = 0
    total_arquivos = 0

    for arq in arquivos:
        with open(arq, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = content.split('\n')
        resultado = []
        in_code = False
        fence = None
        count = 0

        for L in lines:
            # Controle de code fence
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

            # Preservar inline code: substituir temporariamente
            placeholders = {}
            ph_idx = [0]

            def salvar_inline(m):
                key = f'\x00INLINE{ph_idx[0]}\x00'
                placeholders[key] = m.group(0)
                ph_idx[0] += 1
                return key

            L_proc = re.sub(r'`[^`]+`', salvar_inline, L)

            # Aplicar correções
            def replacer(m):
                nonlocal count
                word = m.group(0)
                if word in CORRECOES_AUTO and word not in _CORRECOES_SKIP:
                    count += 1
                    return CORRECOES_AUTO[word]
                return word

            L_proc = _AUTO_PATTERN.sub(replacer, L_proc)

            # Restaurar inline code
            for key, val in placeholders.items():
                L_proc = L_proc.replace(key, val)

            resultado.append(L_proc)

        novo = '\n'.join(resultado)
        if novo != content:
            with open(arq, 'w', encoding='utf-8') as f:
                f.write(novo)
            total_arquivos += 1
            total_correcoes += count
            print(f"  {os.path.relpath(arq, BASE_DIR)}: {count} correção(ões)")

    return total_correcoes, total_arquivos


# CORRECOES mantido vazio — aspell substitui o dicionário manual
CORRECOES = {}



# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    args = set(sys.argv[1:])
    validate_only = '--validate' in args
    fix_spelling = '--fix' in args
    fix_auto = '--fix-auto' in args
    no_check = '--no-check' in args

    arquivos = listar_markdowns()

    # --fix-auto: aplica correções de acentuação automaticamente (sem interação)
    if fix_auto:
        print("Corrigindo ortografia automaticamente...")
        total_c, total_f = corrigir_ortografia_auto(arquivos)
        print(f"  {total_c} correção(ões) em {total_f} arquivo(s)")
        print()

    # --fix: abre aspell interativo em cada arquivo com erros restantes
    if fix_spelling:
        print("Corrigindo ortografia (aspell interativo)...")
        total_arqs, modificados = corrigir_ortografia_interativo(arquivos)
        if modificados:
            print(f"  {modificados} arquivo(s) modificado(s) de {total_arqs} com erros")
        elif total_arqs:
            print(f"  {total_arqs} arquivo(s) com suspeitas, nenhum modificado")
        else:
            print("  Nenhum erro encontrado")
        print()

    if not no_check:
        print("Validando markdowns...")
        erros_fence = validar_code_fences(arquivos)
        erros_ortografia = validar_ortografia(arquivos)

        if erros_fence:
            print(f"\nERRO: {len(erros_fence)} arquivo(s) com code fences desbalanceados.")
            print("Corrija antes de gerar o HTML.")
            sys.exit(1)

        if erros_ortografia and not fix_spelling and not fix_auto:
            print(f"\nAVISO: {erros_ortografia} palavra(s) suspeita(s) encontrada(s).")
            print("  Use --fix-auto para corrigir acentuação automaticamente.")
            print("  Use --fix para corrigir interativamente com aspell.")
            print("  Use --no-check para ignorar e gerar mesmo assim.")

        if not erros_fence and not erros_ortografia:
            print("  Tudo OK")
        print()

    if validate_only:
        return

    print("Gerando livro HTML do curso 'Python Basics'...")

    body_html, all_modules = build_book()
    toc_html = build_toc(all_modules)

    full = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Python Basics -- Curso Completo de Programação com Python</title>
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
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/bash.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/sql.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/json.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/yaml.min.js"></script>
<script>hljs.highlightAll();</script>
</body>
</html>"""

    output_path = os.path.join(BASE_DIR, 'python-basics.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full)

    sz = os.path.getsize(output_path)
    total_all = len(all_modules)
    total_content = len([m for m in all_modules if not m['is_exercise']])
    total_exercises = len([m for m in all_modules if m['is_exercise']])
    total_chapters = len(CAPITULOS)
    mermaid_count = body_html.count('class="mermaid"')

    print(f"\nLivro HTML gerado: {output_path} ({sz/1024:.0f} KB)")
    print(f"Capitulos: {total_chapters}")
    print(f"Modulos de conteudo: {total_content}")
    print(f"Modulos de exercicios: {total_exercises}")
    print(f"Total de secoes: {total_all}")
    print(f"Diagramas Mermaid: {mermaid_count}")


if __name__ == '__main__':
    main()
