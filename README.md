# learnops-book

Repositório oficial: [github.com/RafaelFino/learnops-book](https://github.com/RafaelFino/learnops-book)

Material didático completo e gratuito para quem quer entrar no mundo da tecnologia. Dois livros independentes, cada um com scripts para gerar HTML e PDF prontos para impressão.

**Este material é gratuito.** Pode ser usado, estudado, compartilhado e adaptado livremente por qualquer pessoa.

---

## Livros

### De Zero a Dev

Curso completo de tecnologia — do zero absoluto ao desenvolvedor júnior. Cobre desde o que é um computador até a construção de APIs profissionais, passando por Linux, terminal, Git, Python, Docker, estruturas de dados com C, bancos de dados, orientação a objetos com C# e arquitetura de software.

- Conteúdo: `Zero2Dev/capitulos/` — 180 módulos em Markdown
- Projetos práticos: `Zero2Dev/projects/`
- HTML gerado: `de-zero-a-dev.html`
- PDF gerado: `de-zero-a-dev.pdf`

| Capítulo | Tema |
|---|---|
| 1 | Fundamentos da Computação |
| 2 | Sistemas Operacionais e Linux |
| 3 | Terminal e Linha de Comando |
| 4 | Controle de Versão com Git |
| 5 | Lógica de Programação e Algoritmos com Python |
| 6 | Virtualização, Containers e Docker |
| 7 | Estruturas de Dados com C |
| 8 | Bancos de Dados e Projeto CRUD |
| 9 | Programação Orientada a Objetos com .NET/C# |
| 10 | Arquitetura de Software e Estrutura de Soluções |
| 11 | Integração de Sistemas e APIs |
| 12 | Boas Práticas e Carreira em Tecnologia |
| 13 | Projeto Final: TCC |

---

### Python Basics

Curso completo de programação com Python — do zero absoluto à construção de uma API real. Cobre lógica de programação, estruturas de dados, orientação a objetos, boas práticas e um projeto CRUD progressivo em 4 fases (memória → SQLite → FastAPI → Swagger).

- Conteúdo: `python-basics/` — 69 módulos em Markdown
- HTML gerado: `python-basics.html`
- PDF gerado: `python-basics.pdf`

| Capítulo | Tema | Módulos |
|---|---|---|
| 1 | Fundamentos Teóricos | 01–05 |
| 2 | Fundamentos da Linguagem | 06–11 |
| 3 | Controle de Fluxo | 12–16 |
| 4 | Tópicos Intermediários | 17–23 |
| 5 | Organização e Boas Práticas | 24–28 |
| 6 | Projeto CRUD — Do Zero à API | 29–32 |
| 7 | Glossário | referência |

---

## Estrutura do repositório

```
.
├── Zero2Dev/
│   ├── capitulos/                  # 180 módulos em Markdown
│   └── projects/                   # Projetos práticos por capítulo
├── python-basics/                  # 69 módulos em Markdown
├── zero2dev-gerar-html.py          # Gera de-zero-a-dev.html
├── zero2dev-gerar-pdf.py           # Gera de-zero-a-dev.pdf
├── python-basics-gerar-html.py     # Gera python-basics.html
├── python-basics-gerar-pdf.py      # Gera python-basics.pdf
└── requirements.txt                # Dependências Python (pypdf, reportlab)
```

---

## Como gerar os livros

### Pré-requisitos

```bash
pip install -r requirements.txt
```

Para gerar os PDFs é necessário ter o **Google Chrome** instalado.
Para validação de ortografia é necessário o **aspell** com dicionário pt_BR:

```bash
sudo apt install aspell aspell-pt-br
```

---

### De Zero a Dev

```bash
# Gerar HTML
python3 zero2dev-gerar-html.py

# Gerar PDF (requer o HTML gerado acima)
python3 zero2dev-gerar-pdf.py
```

Arquivo de saída: `de-zero-a-dev.html` e `de-zero-a-dev.pdf`

---

### Python Basics

```bash
# Gerar HTML
python3 python-basics-gerar-html.py

# Gerar PDF (requer o HTML gerado acima)
python3 python-basics-gerar-pdf.py
```

Arquivo de saída: `python-basics.html` e `python-basics.pdf`

---

### Opções dos scripts HTML

Ambos os scripts `*-gerar-html.py` aceitam as mesmas opções:

| Opção | Descrição |
|---|---|
| *(sem opção)* | Valida os markdowns e gera o HTML |
| `--no-check` | Gera sem validação prévia |
| `--validate` | Apenas valida (ortografia + code fences), sem gerar |
| `--fix-auto` | Corrige acentuação automaticamente e gera |
| `--fix` | Abre aspell interativo para correção manual e gera |

> O `--fix-auto` aplica um dicionário de ~200 substituições seguras de acentuação (palavras sem acento → com acento) fora de blocos de código. O `--fix` abre o aspell interativo arquivo por arquivo para revisão manual.

---

## Autor

Rafael Gottardi (Fino) — 2026
