# De Zero a Dev

Material didático completo para quem quer entrar no mundo da tecnologia partindo do zero absoluto.

O conteúdo cobre desde o que é um computador até a construção de APIs profissionais, passando por Linux, terminal, Git, Python, Docker, estruturas de dados com C, bancos de dados, orientação a objetos com C#, arquitetura de software e boas práticas de carreira. Ao final, o leitor tem as bases para trabalhar como desenvolvedor júnior.

**Este material é gratuito.** Pode ser usado, estudado, compartilhado e adaptado livremente por qualquer pessoa.

---

## Estrutura do repositório

```
.
├── Zero2Dev/
│   ├── capitulos/       # Módulos de conteúdo em Markdown (180 arquivos)
│   └── projects/        # Projetos práticos por capítulo
├── gerar-livro-html.py  # Gera o livro em HTML
├── gerar-livro-pdf.py   # Gera o livro em PDF (requer Google Chrome)
└── requirements.txt     # Dependências Python para o script PDF
```

---

## Como gerar o livro

### Pré-requisitos

```bash
pip install -r requirements.txt
```

Para gerar o PDF, é necessário ter o **Google Chrome** instalado.

---

### 1. Gerar o HTML

```bash
python3 gerar-livro-html.py
```

Isso gera o arquivo `de-zero-a-dev.html` na raiz do repositório. O HTML é autocontido e pode ser aberto em qualquer navegador para leitura ou impressão.

**Opções disponíveis:**

| Opção | Descrição |
|---|---|
| *(sem opção)* | Valida os markdowns e gera o HTML |
| `--no-check` | Gera sem validação prévia |
| `--validate` | Apenas valida (ortografia + code fences), sem gerar |
| `--fix` | Corrige ortografia automaticamente e depois gera |

---

### 2. Gerar o PDF

Primeiro gere o HTML (passo acima), depois:

```bash
python3 gerar-livro-pdf.py
```

Isso gera o arquivo `de-zero-a-dev.pdf` na raiz do repositório, no formato livro técnico (17cm × 24cm).

> O processo pode ser demorado — pode levar muitos minutos, pois o arquivo é grande e possui centenas de diagramas que precisam ser renderizados.

---

## Conteúdo do livro

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

## Autor

Rafael Gottardi (Fino) — 2026
