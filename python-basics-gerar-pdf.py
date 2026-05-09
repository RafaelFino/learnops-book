#!/usr/bin/env python3
"""
Gera PDF do livro 'Python Basics' a partir do HTML gerado.

Requisitos:
    - Google Chrome instalado (para PDF via headless)
    - pypdf + reportlab instalados: pip3 install pypdf reportlab

Uso:
    python3 gerar-python-basics-pdf.py

Tamanho de página: 17cm x 24cm (formato livro técnico brasileiro)
"""

import argparse
import os
import re
import subprocess
import sys
import shutil

# Diretório base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_INPUT = os.path.join(BASE_DIR, "python-basics.html")
PDF_OUTPUT = os.path.join(BASE_DIR, "python-basics.pdf")

# Chrome paths
CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
    shutil.which("google-chrome-stable") or "",
]

# CSS override para formato livro 17x24cm
CSS_OVERRIDE = """
@page {
    size: 17cm 24cm;
    margin: 2cm 1.8cm 2.5cm 2.2cm;
}
@page :first {
    margin: 0;
}
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
.preface, .toc {
    page-break-after: always !important;
    break-after: page !important;
}
.page-break {
    page-break-before: always !important;
    break-before: page !important;
}
h1.chapter-header {
    margin-top: 0 !important;
    padding-top: 0.5em !important;
}
.mermaid {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    max-width: 100% !important;
    max-height: 18cm !important;
    overflow: hidden !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
}
.mermaid svg {
    max-width: 100% !important;
    max-height: 17cm !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
}
table {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
th {
    background: #1a1a1a !important;
    color: #3b82f6 !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
tr:nth-child(even) {
    background: #fafafa !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
pre {
    page-break-inside: auto;
    break-inside: auto;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
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
code {
    background: #eff6ff !important;
    color: #1d4ed8 !important;
    border: 1px solid #bfdbfe !important;
    border-radius: 3px !important;
    padding: 0.1em 0.3em !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
pre code {
    border: none !important;
    padding: 0 !important;
    color: #d4d4d4 !important;
    background: transparent !important;
}
blockquote {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
.exercise-header {
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
}
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
.toc .toc-entry { font-size: 8.5pt !important; }
.toc .toc-chapter { font-size: 10pt !important; }
p { orphans: 3 !important; widows: 3 !important; }
h1, h2, h3, h4 { page-break-after: avoid !important; break-after: avoid !important; }
* { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
"""

MERMAID_SYNC_SCRIPT = """
<script>
mermaid.initialize({startOnLoad:false, theme:'neutral', securityLevel:'loose',
    flowchart: { useMaxWidth: true, htmlLabels: true, padding: 10 },
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
                    var svg = el.querySelector('svg');
                    if (svg) { svg.style.maxWidth = '100%'; svg.style.height = 'auto'; }
                    done++;
                }).catch(function() {
                    el.innerHTML = '<pre style="color:#999;font-size:9pt">[Diagrama nao renderizado]</pre>';
                    done++;
                });
            } catch(e) {
                el.innerHTML = '<pre style="color:#999;font-size:9pt">[Diagrama nao renderizado]</pre>';
                done++;
            }
        });
    }
    renderAll();
    var checkInterval = setInterval(function() {
        if (done >= total) {
            clearInterval(checkInterval);
            document.body.setAttribute('data-mermaid-ready', 'true');
        }
    }, 100);
})();
</script>
"""


def find_chrome():
    for path in CHROME_PATHS:
        if path and os.path.exists(path):
            return path
    return None


def prepare_html_for_print(html_content):
    html_content = re.sub(r'@page\s*\{[^}]+\}', '/* @page original removido */', html_content, count=1)
    html_content = re.sub(r'@page\s*:first\s*\{[^}]+\}', '/* @page :first original removido */', html_content, count=1)
    html_content = re.sub(
        r'@media\s+print\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}',
        '/* @media print original removido */',
        html_content, count=1
    )
    html_content = html_content.replace('</style>', CSS_OVERRIDE + '\n</style>', 1)
    html_content = re.sub(
        r'<script>\s*// Mermaid: lazy render.*?</script>',
        MERMAID_SYNC_SCRIPT,
        html_content,
        flags=re.DOTALL
    )
    return html_content


def generate_pdf(html_content):
    chrome = find_chrome()
    if not chrome:
        print("❌ Google Chrome não encontrado.")
        sys.exit(1)

    print(f"📄 Gerando PDF (17cm x 24cm) com Chrome headless...")
    print(f"   Chrome: {chrome}")

    prepared_html = prepare_html_for_print(html_content)

    tmp_html = os.path.join(BASE_DIR, "_tmp_python_basics_print.html")
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

        print("   Aguardando renderização (pode demorar alguns minutos)...")
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)

        if result.returncode != 0 and not os.path.exists(PDF_OUTPUT):
            print(f"❌ Chrome falhou: {result.stderr[:500]}")
            sys.exit(1)

        if os.path.exists(PDF_OUTPUT):
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
    try:
        from pypdf import PdfReader, PdfWriter
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        import io
    except ImportError:
        print("   pypdf/reportlab não instalados. Numeração de páginas não adicionada.")
        print("      Instale com: pip3 install pypdf reportlab")
        return

    print("   Adicionando numeração de páginas...")

    reader = PdfReader(PDF_OUTPUT)
    writer = PdfWriter()

    total_pages = len(reader.pages)
    start_numbering = 4  # Pular capa, prefácio, introdução e sumário

    page_width = 17 * cm
    page_height = 24 * cm

    for i, page in enumerate(reader.pages):
        if i >= start_numbering:
            packet = io.BytesIO()
            c = canvas.Canvas(packet, pagesize=(page_width, page_height))
            c.setFont("Helvetica", 9)
            c.setFillColorRGB(0.4, 0.4, 0.4)
            page_num = i - start_numbering + 1
            c.drawCentredString(page_width / 2, 1.0 * cm, str(page_num))
            c.save()
            packet.seek(0)
            overlay_reader = PdfReader(packet)
            page.merge_page(overlay_reader.pages[0])
        writer.add_page(page)

    with open(PDF_OUTPUT, 'wb') as f:
        writer.write(f)

    print(f"   Numeração adicionada: páginas {start_numbering + 1} a {total_pages}")


def main():
    parser = argparse.ArgumentParser(description="Gera PDF do livro 'Python Basics' (17x24cm)")
    parser.parse_args()

    if not os.path.exists(HTML_INPUT):
        print(f"Erro: HTML não encontrado: {HTML_INPUT}")
        print("   Execute primeiro: python3 gerar-python-basics-html.py")
        sys.exit(1)

    print(f"Lendo HTML: {HTML_INPUT}")
    with open(HTML_INPUT, 'r', encoding='utf-8') as f:
        html_content = f.read()
    print(f"   {len(html_content):,} caracteres lidos")

    generate_pdf(html_content)

    print("\nGeração concluída!")


if __name__ == '__main__':
    main()
