#!/usr/bin/env python3
"""
Gera PDF do livro 'De Zero a Dev' a partir do HTML gerado.

Requisitos:
    - Google Chrome instalado (para PDF via headless)
    - pypdf + reportlab instalados (para numeração de páginas): pip3 install pypdf reportlab

Uso:
    python3 curso/gerar-livro-pdf.py

Tamanho de página: 17cm x 24cm (formato livro técnico brasileiro)
Margens: 2.2cm interna (encadernação), 1.8cm externa, 2cm topo/2.5cm base
"""

import argparse
import os
import re
import subprocess
import sys
import shutil
import json
import time

# Diretório base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_INPUT = os.path.join(BASE_DIR, "de-zero-a-dev.html")
PDF_OUTPUT = os.path.join(BASE_DIR, "de-zero-a-dev.pdf")

# Margens em cm
MARGIN_TOP = 2.0
MARGIN_BOTTOM = 2.5
MARGIN_LEFT = 2.2    # Margem interna (encadernação) - maior
MARGIN_RIGHT = 1.8   # Margem externa - menor

# Tamanho da página em polegadas (17cm x 24cm)
PAGE_WIDTH_IN = 17 / 2.54   # 6.693 in
PAGE_HEIGHT_IN = 24 / 2.54  # 9.449 in

# Chrome paths no macOS
CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
]



# CSS override para formato livro 17x24cm
CSS_OVERRIDE = """
/* Override: formato livro 17cm x 24cm para impressão */
@page {
    size: 17cm 24cm;
    margin: 2cm 1.8cm 2.5cm 2.2cm;
}

/* Capa: sem margem */
@page :first {
    margin: 0;
}

/* Numeração de páginas via CSS counter - rodapé fixo */
body {
    counter-reset: page-number;
}
.page-break {
    counter-increment: page-number;
}

/* Capa: ocupar página inteira sem overflow */
.cover {
    min-height: 100vh !important;
    height: 100vh !important;
    max-height: 100vh !important;
    padding: 3cm 1.5cm !important;
    box-sizing: border-box !important;
    overflow: hidden !important;
    page-break-after: always !important;
    break-after: page !important;
}
.cover h1 {
    font-size: 28pt !important;
}
.cover .subtitle {
    font-size: 11pt !important;
}

/* Prefácio e sumário: sem numeração de página */
.preface, .toc {
    page-break-after: always !important;
    break-after: page !important;
}

/* Capítulos sempre em página nova - SEM duplicar quebra */
.page-break {
    page-break-before: always !important;
    break-before: page !important;
}
h1.chapter-header {
    margin-top: 0 !important;
    padding-top: 0.5em !important;
}

/* Diagramas Mermaid: nunca quebrar entre páginas, máximo 1 página */
.mermaid {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    max-width: 100% !important;
    max-height: 18cm !important;  /* Altura útil da página (24 - 2 - 2 - 2 de margem extra) */
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.mermaid svg {
    max-width: 100% !important;
    max-height: 17cm !important;  /* Garantir que SVG cabe na área útil */
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
}
/* Garantir que labels mermaid não sejam cortados */
.mermaid .nodeLabel,
.mermaid .edgeLabel,
.mermaid .label,
.mermaid text {
    overflow: visible !important;
    white-space: normal !important;
    text-overflow: clip !important;
    font-size: 11px !important;
}
.mermaid .node rect,
.mermaid .node circle,
.mermaid .node polygon {
    overflow: visible !important;
}

/* Tabelas: evitar quebra e MANTER cores */
table {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
}
th {
    background: #1a1a1a !important;
    color: #fbbf24 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
}
tr:nth-child(even) {
    background: #fafafa !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
}

/* Blocos de código: podem quebrar (conforme requisito), tema escuro legível */
pre {
    page-break-inside: auto;
    break-inside: auto;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
    background: #1e1e1e !important;
    border: 1px solid #333 !important;
    border-radius: 6px !important;
    padding: 1em 1.2em !important;
}
pre code {
    color: #d4d4d4 !important;
    background: transparent !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
/* Inline code: fundo suave, texto escuro legível */
code {
    background: #f0f0f0 !important;
    color: #c7254e !important;
    border: 1px solid #ddd !important;
    border-radius: 3px !important;
    padding: 0.1em 0.3em !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
/* Código dentro de pre NÃO herda estilo inline */
pre code {
    border: none !important;
    padding: 0 !important;
    color: #d4d4d4 !important;
    background: transparent !important;
}

/* Highlight.js - tema escuro para impressão (VS Code Dark+) */
.hljs { background: #1e1e1e !important; color: #d4d4d4 !important; }
.hljs-keyword { color: #569cd6 !important; }
.hljs-string { color: #ce9178 !important; }
.hljs-number { color: #b5cea8 !important; }
.hljs-comment { color: #6a9955 !important; font-style: italic !important; }
.hljs-function { color: #dcdcaa !important; }
.hljs-title { color: #dcdcaa !important; }
.hljs-params { color: #9cdcfe !important; }
.hljs-built_in { color: #4ec9b0 !important; }
.hljs-type { color: #4ec9b0 !important; }
.hljs-attr { color: #9cdcfe !important; }
.hljs-variable { color: #9cdcfe !important; }
.hljs-literal { color: #569cd6 !important; }
.hljs-operator { color: #d4d4d4 !important; }
.hljs-punctuation { color: #d4d4d4 !important; }
.hljs-meta { color: #569cd6 !important; }
.hljs-selector-tag { color: #d7ba7d !important; }
.hljs-selector-class { color: #d7ba7d !important; }
.hljs-selector-id { color: #d7ba7d !important; }
.hljs-name { color: #569cd6 !important; }
.hljs-tag { color: #569cd6 !important; }
.hljs-attribute { color: #9cdcfe !important; }
.hljs-symbol { color: #b5cea8 !important; }
.hljs-class { color: #4ec9b0 !important; }
.hljs-subst { color: #d4d4d4 !important; }

/* Blockquotes: evitar quebra, manter cores */
blockquote {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
}

/* Ajuste de fontes para formato menor (17x24 vs A4) */
body {
    font-size: 10pt !important;
    line-height: 1.6 !important;
}
h1 { font-size: 18pt !important; }
h1.chapter-header { font-size: 22pt !important; }
h1.module-header { font-size: 17pt !important; }
h2 { font-size: 13pt !important; }
h3 { font-size: 11pt !important; }
h4 { font-size: 10pt !important; }
pre { font-size: 8pt !important; line-height: 1.4 !important; }
pre code { font-size: 8pt !important; }
code { font-size: 8pt !important; }
table { font-size: 9pt !important; }
th, td { padding: 0.3em 0.5em !important; }

/* Sumário: ajustar */
.toc .toc-entry {
    font-size: 8.5pt !important;
}
.toc .toc-chapter {
    font-size: 10pt !important;
}

/* Evitar órfãos e viúvas */
p {
    orphans: 3 !important;
    widows: 3 !important;
}

/* Seções: evitar quebra logo após título */
h1, h2, h3, h4 {
    page-break-after: avoid !important;
    break-after: avoid !important;
}

/* Forçar cores em modo print */
* {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
    color-adjust: exact !important;
}
"""



def find_chrome():
    """Encontra o executável do Chrome no sistema."""
    for path in CHROME_PATHS:
        if path and os.path.exists(path):
            return path
    return None


def prepare_html_for_print(html_content):
    """Prepara o HTML para geração de PDF no formato livro."""
    
    # Remover o @page original e @page :first
    html_content = re.sub(
        r'@page\s*\{[^}]+\}',
        '/* @page original removido */',
        html_content,
        count=1
    )
    html_content = re.sub(
        r'@page\s*:first\s*\{[^}]+\}',
        '/* @page :first original removido */',
        html_content,
        count=1
    )
    
    # Remover o bloco @media print que sobrescreve cores
    html_content = re.sub(
        r'@media\s+print\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}',
        '/* @media print original removido */',
        html_content,
        count=1
    )
    
    # Inserir CSS override antes do </style>
    html_content = html_content.replace(
        '</style>',
        CSS_OVERRIDE + '\n</style>',
        1
    )
    
    # Garantir que o Mermaid renderize ANTES do print:
    # Substituir o lazy-loading IntersectionObserver por renderização imediata
    # e adicionar um delay antes de imprimir
    mermaid_sync_script = """
<script>
// Override: renderizar TODOS os diagramas mermaid imediatamente (sem lazy load)
mermaid.initialize({startOnLoad:false, theme:'neutral', securityLevel:'loose',
    flowchart: { useMaxWidth: true, htmlLabels: true, padding: 10, nodeSpacing: 30, rankSpacing: 30 },
    sequence: { useMaxWidth: true, height: 30, boxMargin: 5 },
    classDiagram: { useMaxWidth: true },
    stateDiagram: { useMaxWidth: true },
    themeVariables: { fontSize: '11px' }
});
(function(){
    var pending = document.querySelectorAll('.mermaid');
    var total = pending.length;
    var done = 0;
    var id = 0;
    
    function renderAll() {
        pending.forEach(function(el) {
            if(el.dataset.rendered) return;
            el.dataset.rendered = '1';
            var code = el.textContent.trim();
            var eid = 'mermaid-sync-' + id++;
            try {
                mermaid.render(eid, code).then(function(r) {
                    el.innerHTML = r.svg;
                    // Garantir que SVG não corte labels
                    var svg = el.querySelector('svg');
                    if (svg) {
                        svg.style.maxWidth = '100%';
                        svg.style.height = 'auto';
                        svg.style.overflow = 'visible';
                        svg.setAttribute('width', '100%');
                    }
                    done++;
                }).catch(function(err) {
                    el.innerHTML = '<pre style="color:#999;font-size:9pt">[Diagrama: ' + code.split('\\n')[0] + ']</pre>';
                    done++;
                });
            } catch(e) {
                el.innerHTML = '<pre style="color:#999;font-size:9pt">[Diagrama nao renderizado]</pre>';
                done++;
            }
        });
    }
    
    renderAll();
    
    // Sinalizar quando todos os diagramas estiverem prontos
    var checkInterval = setInterval(function() {
        if (done >= total) {
            clearInterval(checkInterval);
            // Ajustar SVGs que excedem a altura da página (17cm úteis)
            var maxH = 640; // ~17cm em px (96dpi)
            document.querySelectorAll('.mermaid svg').forEach(function(svg) {
                var bbox = svg.getBoundingClientRect();
                if (bbox.height > maxH) {
                    var scale = maxH / bbox.height;
                    svg.style.maxHeight = maxH + 'px';
                    svg.style.width = 'auto';
                    svg.style.height = maxH + 'px';
                }
                svg.style.maxWidth = '100%';
                svg.removeAttribute('height');
                svg.setAttribute('preserveAspectRatio', 'xMidYMid meet');
            });
            document.body.setAttribute('data-mermaid-ready', 'true');
        }
    }, 100);
})();
</script>
"""
    
    # Remover o script mermaid original (lazy load) e substituir pelo síncrono
    html_content = re.sub(
        r'<script>\s*// Mermaid: lazy render.*?</script>',
        mermaid_sync_script,
        html_content,
        flags=re.DOTALL
    )
    
    return html_content


def generate_pdf(html_content):
    """Gera o PDF usando Chrome headless.
    
    Usa --print-to-pdf com displayHeaderFooter para numeração de páginas.
    """
    chrome = find_chrome()
    if not chrome:
        print("❌ Google Chrome não encontrado.")
        sys.exit(1)
    
    print(f"📄 Gerando PDF (17cm x 24cm) com Chrome headless...")
    print(f"   Chrome: {chrome}")
    
    prepared_html = prepare_html_for_print(html_content)
    
    # Salvar HTML temporário
    tmp_html = os.path.join(BASE_DIR, "_tmp_livro_print.html")
    with open(tmp_html, 'w', encoding='utf-8') as f:
        f.write(prepared_html)
    
    try:
        cmd = [
            chrome,
            '--headless=new',
            '--disable-gpu',
            '--no-sandbox',
            '--disable-extensions',
            '--disable-software-rasterizer',
            '--run-all-compositor-stages-before-draw',
            '--virtual-time-budget=60000',
            f'--print-to-pdf={PDF_OUTPUT}',
            '--no-pdf-header-footer',
            f'file://{tmp_html}',
        ]
        
        print("   Aguardando renderização dos diagramas Mermaid (processo demorado — pode levar muitos minutos, pois o arquivo é grande e possui centenas de diagramas para renderizar)...")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600
        )
        
        if result.returncode != 0 and not os.path.exists(PDF_OUTPUT):
            print(f"❌ Chrome falhou: {result.stderr[:500]}")
            sys.exit(1)
        
        if os.path.exists(PDF_OUTPUT):
            # Adicionar numeração de páginas ao PDF gerado
            add_page_numbers_to_pdf()
            size_mb = os.path.getsize(PDF_OUTPUT) / (1024 * 1024)
            print(f"✅ PDF gerado: {PDF_OUTPUT} ({size_mb:.1f} MB)")
        else:
            print("❌ PDF não foi gerado")
            sys.exit(1)
            
    except subprocess.TimeoutExpired:
        print("❌ Timeout ao gerar PDF (>10 min)")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        sys.exit(1)
    finally:
        if os.path.exists(tmp_html):
            os.remove(tmp_html)


def add_page_numbers_to_pdf():
    """Adiciona numeracao de paginas ao PDF usando pypdf + reportlab.

    Footer: apenas o numero da pagina centralizado na parte inferior.
    """
    try:
        from pypdf import PdfReader, PdfWriter
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        import io
    except ImportError:
        print("   pypdf/reportlab nao instalados. Numeracao de paginas nao adicionada.")
        print("      Instale com: pip3 install pypdf reportlab")
        return

    print("   Adicionando numeracao de paginas...")

    reader = PdfReader(PDF_OUTPUT)
    writer = PdfWriter()

    total_pages = len(reader.pages)
    # Pular capa, prefacio, introducao e sumario (primeiras ~4 paginas)
    start_numbering = 4

    page_width = 17 * cm
    page_height = 24 * cm

    for i, page in enumerate(reader.pages):
        if i >= start_numbering:
            # Criar overlay com apenas o numero de pagina
            packet = io.BytesIO()
            c = canvas.Canvas(packet, pagesize=(page_width, page_height))
            c.setFont("Helvetica", 9)
            c.setFillColorRGB(0.4, 0.4, 0.4)
            page_num = i - start_numbering + 1
            # Numero centralizado no footer
            c.drawCentredString(page_width / 2, 1.0 * cm, str(page_num))
            c.save()
            packet.seek(0)

            # Merge overlay com a pagina
            overlay_reader = PdfReader(packet)
            page.merge_page(overlay_reader.pages[0])

        writer.add_page(page)

    # Salvar
    with open(PDF_OUTPUT, 'wb') as f:
        writer.write(f)

    print(f"   Numeracao adicionada: paginas {start_numbering + 1} a {total_pages}")






def main():
    parser = argparse.ArgumentParser(
        description="Gera PDF do livro 'De Zero a Dev' (17x24cm)"
    )
    parser.parse_args()

    if not os.path.exists(HTML_INPUT):
        print(f"Erro: HTML nao encontrado: {HTML_INPUT}")
        print("   Execute primeiro: python3 curso/gerar-livro-html.py")
        sys.exit(1)

    print(f"Lendo HTML: {HTML_INPUT}")
    with open(HTML_INPUT, 'r', encoding='utf-8') as f:
        html_content = f.read()
    print(f"   {len(html_content):,} caracteres lidos")

    generate_pdf(html_content)

    print("\nGeracao concluida!")


if __name__ == '__main__':
    main()
