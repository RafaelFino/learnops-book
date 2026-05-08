# 13.4 — Documentação Técnica

[← Anterior: Desenvolvimento Incremental](cap13-mod03-desenvolvimento.md) · [Próximo: Apresentação e Defesa do Projeto →](cap13-mod05-apresentacao.md)

---

## Introdução

No módulo anterior, você aprendeu a desenvolver o TCC de forma incremental — etapa por etapa, testando e commitando a cada passo. Agora vamos falar de algo que muitos programadores negligenciam mas que faz toda a diferença: documentação.

Documentação técnica e o que permite que outras pessoas (e você mesmo no futuro) entendam o que o sistema faz, como funciona e como usar. Um projeto sem documentação e como um livro sem índice — pode ter conteúdo excelente, mas ninguém consegue encontrar o que precisa.

Na indústria, documentação e levada a serio. Empresas como Stripe, Twilio e FastAPI são conhecidas pela qualidade da sua documentação — e isso é um dos motivos do sucesso desses produtos. Desenvolvedores escolhem ferramentas com boa documentação porque economizam tempo e frustacao.

Para o seu TCC, a documentação tem dois propositos: mostrar que você sabe comunicar ideias técnicas com clareza, e permitir que qualquer pessoa consiga rodar e entender o seu projeto.

---

## Por que Documentar?

### O Problema do "Funciona na Minha Máquina"

Imagine que você terminou o TCC, está tudo funcionando no seu computador. Ai você precisa mostrar para alguém — um colega, um avaliador, um recrutador. A pessoa clona o repositório e... não consegue rodar. Falta uma dependência. O banco não é criado. Não sabe qual comando executar.

Isso acontece o tempo todo na indústria. E a documentação que resolve.

### Documentação como Portfolio

Para desenvolvedores juniores, o GitHub e o portfolio. Recrutadores olham seus repositórios para avaliar:

| O que olham | O que esperam ver |
|------------|------------------|
| README.md | Descrição clara do projeto, como instalar e rodar |
| Código | Organizado, comentado, com nomes claros |
| Commits | Mensagens descritivas, histórico lógico |
| Estrutura | Pastas organizadas, separacao de responsabilidades |

Um projeto com boa documentação se destaca imediatamente. Mostra maturidade profissional.

### Documentação para Você Mesmo

Você vai esquecer como o seu próprio código funciona. Isso não é fraqueza — e como o cerebro humano funciona. Daqui a 3 meses, você vai olhar para o código e pensar "por que eu fiz isso assim?". Se a resposta estiver documentada, você economiza horas.

---

## O README.md: O Documento Mais Importante

O README.md e a porta de entrada do seu projeto. E a primeira coisa que qualquer pessoa ve ao acessar o repositório. Um bom README responde todas as perguntas básicas sem que a pessoa precise ler o código.

### Estrutura Completa do README

Você já começou o README no módulo 12.1 (planejamento). Agora vai completa-lo com as seções técnicas:

````markdown
# [Nome do Projeto]

[Uma frase que descreve o que o projeto faz]

## Sobre

[1-2 paragrafos explicando o problema e a solucao]

## Funcionalidades

- [funcionalidade 1]
- [funcionalidade 2]
- ...

## Tecnologias

- Python 3.10+
- FastAPI
- SQLite
- Pydantic
- Uvicorn

## Como Executar

### Pre-requisitos

- Python 3.10 ou superior instalado
- pip (gerenciador de pacotes do Python)

### Instalacao

```bash
# Clonar o repositório
git clone https://github.com/seu-usuário/seu-projeto.git

# Entrar na pasta
cd seu-projeto

# Instalar dependências
pip3 install fastapi uvicorn
```

### Executando

```bash
# Iniciar o servidor
uvicorn main:app --reload

# O servidor estara disponível em http://localhost:8000
# Documentação interativa em http://localhost:8000/docs
```

## Endpoints da API

### Categorias

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| POST | /categories | Criar categoria |
| GET | /categories | Listar categorias |
| ...  | ...        | ...       |

### Transacoes

| Metodo | Endpoint | Descricao |
|--------|----------|-----------|
| POST | /transactions | Criar transacao |
| GET | /transactions | Listar transacoes |
| ...  | ...           | ...       |

## Exemplos de Uso

```bash
# Criar uma categoria
curl -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Alimentacao"}'

# Criar uma transação
curl -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{"description": "Almoço", "amount": 25.50, ...}'
```

## Modelo de Dados

[Diagrama ER em Mermaid]

## Arquitetura

[Diagrama de arquitetura em Mermaid]

## Decisoes Tecnicas

[Lista de decisoes com justificativas]

## Autor

[Seu nome] — [seu GitHub]
````

### Erros Comuns no README

| Erro | Problema | Solução |
|------|---------|---------|
| Sem instruções de instalação | Ninguém consegue rodar | Listar todos os passos, do clone ao run |
| Assumir dependências | "Funciona na minha máquina" | Listar todas as dependências e versões |
| Sem exemplos de uso | Ninguém sabe como testar | Incluir comandos curl ou instruções de uso |
| Texto demais, estrutura de menos | Difícil de encontrar informação | Usar seções claras, tabelas e listas |
| Desatualizado | Documentação não reflete o código | Atualizar README a cada mudança significativa |

---

## Comentários no Código

### Quando Comentar

Comentários no código explicam o "por que", não o "o que". O código já diz o que faz — o comentário explica por que faz daquela forma.

**Comentário ruim (explica o óbvio):**
```python
# Incrementa o contador
counter = counter + 1  # "counter" = contador
```

**Comentário bom (explica o por que):**
```python
# Incrementa o contador de tentativas. Apos 3 tentativas,
# o sistema para de tentar e retorna erro ao usuario.
retry_count = retry_count + 1  # "retry_count" = contador de tentativas
```

### O que Comentar no TCC

Para o TCC, comente:

1. **Cabecalho de cada arquivo**: o que o arquivo faz e qual camada pertence
2. **Funções complexas**: o que a função faz, parâmetros e retorno
3. **Regras de negócio**: por que a validação existe
4. **Queries SQL complexas**: o que a query busca
5. **Decisões não obvias**: por que você fez de um jeito e não de outro

**Exemplo de arquivo bem comentado:**

```python
"""
transaction_service.py — Servico de transacoes

Camada de servico que implementa as regras de negocio
para transacoes financeiras. Recebe dados validados do
router e usa o repositorio para persistir no banco.

Regras implementadas:
- Categoria deve existir ao criar transacao
- Valor deve ser positivo
- Tipo deve ser "income" ou "expense"
- Nao permite remover categoria com transacoes
"""

from models.transaction import TransactionCreate, TransactionResponse
from repositories.transaction_repository import TransactionRepository
from repositories.category_repository import CategoryRepository


class TransactionService:
    """Servico responsavel pela logica de negocio de transacoes"""

    def __init__(self, db_path: str = "fincontrol.db"):
        self.transaction_repo = TransactionRepository(db_path)
        self.category_repo = CategoryRepository(db_path)

    def create(self, data: TransactionCreate) -> TransactionResponse:
        """
        Cria uma nova transacao.

        Verifica se a categoria existe antes de inserir.
        Retorna a transacao criada com ID gerado.

        Raises:
            ValueError: se a categoria nao existir
        """
        # Verificar se a categoria existe antes de criar a transacao
        # Isso evita dados orfaos no banco (transacao sem categoria valida)
        category = self.category_repo.get_by_id(data.category_id)
        if not category:
            raise ValueError(f"Category {data.category_id} not found")

        return self.transaction_repo.create(data)
```

Saída esperada:
```
(nenhuma saida — e definicao de classe, nao executavel sozinha)
```

### Convenção de Comentários

| Tipo | Formato | Quando usar |
|------|---------|------------|
| Docstring de módulo | `"""texto"""` no topo do arquivo | Todo arquivo .py |
| Docstring de classe | `"""texto"""` abaixo do class | Toda classe |
| Docstring de função | `"""texto"""` abaixo do def | Funções publicas |
| Comentário inline | `# texto` | Explicar decisões não obvias |
| Traducao de variável | `# "name" = nome` | Variáveis em ingles |

### O que Não Comentar

Comentários desnecessários poluem o código e dificultam a leitura. Evite:

```python
# RUIM: comentario que repete o codigo
x = x + 1  # soma 1 a x

# RUIM: comentario obvio
def get_all():  # funcao que retorna todos
    return self.repo.get_all()  # retorna todos do repositorio

# RUIM: comentario desatualizado (pior que nenhum comentario)
# Retorna lista de categorias ordenada por nome
def get_all():
    return self.repo.get_all()  # na verdade retorna sem ordenacao
```

A regra e: se o código e claro o suficiente sozinho, não precisa de comentário. Comentários existem para explicar o "por que", não o "o que".

### Nomes Claros Reduzem a Necessidade de Comentários

O melhor comentário é um nome de variável ou função que se explica sozinho:

```python
# RUIM: nome generico que precisa de comentario
d = 30  # dias ate o vencimento

# BOM: nome descritivo que nao precisa de comentario
days_until_due = 30  # "days_until_due" = dias ate o vencimento

# RUIM: funcao com nome vago
def process(data):
    pass

# BOM: funcao com nome descritivo
def validate_and_create_transaction(data):
    pass
```

---

## Tipos de Documentação

Existem diferentes tipos de documentação, cada um com um proposito:

### Documentação para Usuários

Explica como usar o sistema. No caso de uma API, e o Swagger e os exemplos de curl no README.

**Perguntas que responde:**
- Como instalo e rodo o sistema?
- Quais endpoints existem?
- Que dados preciso enviar?
- Que respostas vou receber?
- Que erros podem acontecer?

### Documentação para Desenvolvedores

Explica como o sistema funciona internamente. São os comentários no código, docstrings e diagramas de arquitetura.

**Perguntas que responde:**
- Como o código esta organizado?
- Qual a responsabilidade de cada camada?
- Quais decisões técnicas foram tomadas e por que?
- Como adicionar uma nova funcionalidade?

### Documentação para Operação

Explica como manter o sistema rodando. Para o TCC, e simples (SQLite não precisa de manutenção), mas em sistemas reais inclui: como fazer backup, como monitorar, como escalar.

**Perguntas que responde:**
- Como faco backup do banco?
- Como vejo logs de erro?
- Como reinicio o servidor?

Para o TCC, foque na documentação para usuários (README + Swagger) e para desenvolvedores (comentários + diagramas). A documentação de operação é um diferencial.

---

## Versionamento da Documentação

A documentação deve evoluir junto com o código. Quando você adiciona uma funcionalidade, atualize o README. Quando muda uma regra de negócio, atualize os comentários.

### Quando Atualizar a Documentação

| Evento | O que atualizar |
|--------|----------------|
| Novo endpoint | Tabela de endpoints no README, Swagger |
| Nova regra de negócio | Comentários no serviço, README |
| Mudança no modelo | Diagrama ER, dicionário de dados, SQL |
| Nova dependência | Seção de instalação no README |
| Bug corrigido | Nada (a menos que mude comportamento documentado) |

### Documentação Desatualizada e Pior que Nenhuma

Se o README diz "execute `python main.py`" mas o comando correto e `uvicorn main:app`, o usuário vai perder tempo tentando algo que não funciona. Documentação errada gera mais frustacao do que nenhuma documentação.

**Regra:** a cada commit que muda comportamento, verifique se a documentação precisa ser atualizada.

---

## Licença do Projeto

Todo projeto open source deve ter uma licença. A licença define o que outras pessoas podem fazer com o seu código.

### Licenças Comuns

| Licença | Permite | Exige | Ideal para |
|---------|---------|-------|-----------|
| MIT | Quase tudo | Manter aviso de copyright | Projetos simples, portfolio |
| Apache 2.0 | Quase tudo | Manter aviso + listar mudanças | Projetos maiores |
| GPL v3 | Quase tudo | Código derivado também deve ser GPL | Projetos que querem garantir abertura |

Para o TCC, a licença MIT e a mais simples e adequada. Crie um arquivo `LICENSE` na raiz do projeto:

```
MIT License

Copyright (c) 2026 [Seu Nome]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Documentação como Processo, Não como Tarefa Final

Um erro comum e tratar documentação como algo que se faz "no final". O problema e que no final você esta cansado, com pressa e já esqueceu detalhes importantes.

A abordagem correta e documentar durante o desenvolvimento:

| Quando | O que documentar |
|--------|-----------------|
| Ao criar o projeto | README com descrição e escopo |
| Ao modelar o banco | Diagrama ER e dicionário de dados |
| Ao definir a arquitetura | Diagrama de arquitetura e decisões técnicas |
| Ao implementar cada função | Docstring da função |
| Ao implementar cada endpoint | Descrição no Swagger |
| Ao encontrar um bug interessante | Comentário explicando a correção |
| Ao finalizar | Revisao geral e instruções de instalação |

Essa abordagem tem duas vantagens:

1. A documentação é mais precisa (você escreve enquanto o contexto esta fresco)
2. O trabalho e distribuido (não acumula tudo no final)

### O README Evolui com o Projeto

O README não é escrito uma vez e esquecido. Ele evolui:

```
Commit 1: docs: initial project planning (problema, escopo, entidades)
Commit 5: docs: add data model and ER diagram
Commit 10: docs: add architecture diagram and tech decisions
Commit 20: docs: add API endpoints table
Commit 30: docs: add installation and usage instructions
Commit 35: docs: add examples with curl commands
Commit 40: docs: final review and cleanup
```

Cada commit adiciona uma peça ao README. No final, você tem um documento completo sem ter precisado escrever tudo de uma vez.

---

## O Arquivo .gitignore

O `.gitignore` define quais arquivos o Git deve ignorar. Isso evita que arquivos desnecessários (cache, banco de dados local, configurações de IDE) sejam commitados.

### .gitignore para Projetos Python

```
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
dist/
build/
.env

# Banco de dados local (recriado automaticamente)
*.db

# IDE e editores
.vscode/
.idea/
*.swp
*.swo
*~

# Sistema operacional
.DS_Store
Thumbs.db

# Ambientes virtuais
venv/
.venv/
env/
```

### Por que Ignorar o Banco de Dados?

O arquivo `.db` do SQLite e recriado automaticamente pelo código. Commitar o banco de dados causa problemas:

- O arquivo muda a cada operação (commits desnecessários)
- Conflitos de merge são impossíveis de resolver
- Dados de teste ficam no repositório (pode conter dados sensiveis)

Em vez disso, o código cria o banco automaticamente se ele não existir. Isso é mais limpo e seguro.

---

## Documentação da API (Swagger)

Se você está usando FastAPI, a documentação da API e gerada automaticamente. Mas você pode (e deve) melhorar essa documentação.

### Adicionando Descricoes aos Endpoints

```python
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]  # Agrupa no Swagger
)

@router.post(
    "/",
    response_model=TransactionResponse,
    status_code=201,
    summary="Criar transacao",
    description="Cria uma nova transacao financeira. "
                "A categoria informada deve existir no sistema."
)
async def create_transaction(data: TransactionCreate):
    """
    Cria uma nova transacao com os seguintes dados:

    - **description**: descricao da transacao (obrigatorio)
    - **amount**: valor da transacao, deve ser positivo (obrigatorio)
    - **type**: "income" para receita ou "expense" para despesa (obrigatorio)
    - **category_id**: ID da categoria (deve existir)
    - **date**: data da transacao no formato YYYY-MM-DD (obrigatorio)
    """
    # ... implementacao
```

### Adicionando Descricoes aos Modelos

```python
from pydantic import BaseModel, Field

class TransactionCreate(BaseModel):
    """Dados necessarios para criar uma transacao"""

    description: str = Field(
        min_length=1,
        max_length=200,
        description="Descricao da transacao",
        examples=["Almoco no restaurante"]
    )
    amount: float = Field(
        gt=0,
        description="Valor da transacao (deve ser positivo)",
        examples=[25.50]
    )
    type: str = Field(
        pattern="^(income|expense)$",
        description="Tipo: 'income' para receita, 'expense' para despesa",
        examples=["expense"]
    )
    category_id: int = Field(
        description="ID da categoria (deve existir no sistema)",
        examples=[1]
    )
    date: str = Field(
        description="Data da transacao no formato YYYY-MM-DD",
        examples=["2026-04-28"]
    )
```

Com essas descricoes, o Swagger em `/docs` fica muito mais informativo e profissional.

### Customizando o Swagger

```python
from fastapi import FastAPI

app = FastAPI(
    title="FinControl API",
    description="API REST para controle financeiro pessoal. "
                "Permite registrar receitas e despesas, "
                "categorizar transacoes e consultar resumos.",
    version="1.0.0",
    contact={
        "name": "Seu Nome",
        "url": "https://github.com/seu-usuario"
    }
)
```

---

## Documentação do Banco de Dados

Além do diagrama ER no README, documente o banco de dados com:

### Dicionário de Dados

Para cada tabela, crie uma seção no README ou em um arquivo separado (`docs/database.md`):

```markdown
## Dicionario de Dados

### Tabela: categories

| Campo | Tipo | Restricoes | Descricao |
|-------|------|-----------|-----------|
| id | INTEGER | PK, AUTOINCREMENT | Identificador unico |
| name | TEXT | NOT NULL, UNIQUE | Nome da categoria |
| description | TEXT | — | Descricao opcional |
| created_at | TEXT | NOT NULL, DEFAULT now | Data de criacao |

### Tabela: transactions

| Campo | Tipo | Restricoes | Descricao |
|-------|------|-----------|-----------|
| id | INTEGER | PK, AUTOINCREMENT | Identificador unico |
| description | TEXT | NOT NULL | Descricao da transacao |
| amount | REAL | NOT NULL, CHECK > 0 | Valor (sempre positivo) |
| type | TEXT | NOT NULL, CHECK IN | "income" ou "expense" |
| category_id | INTEGER | NOT NULL, FK | Referencia categories.id |
| date | TEXT | NOT NULL | Data no formato ISO 8601 |
| created_at | TEXT | NOT NULL, DEFAULT now | Data de criacao |
| updated_at | TEXT | — | Data da ultima atualizacao |

### Indices

| Nome | Tabela | Campos | Proposito |
|------|--------|--------|-----------|
| idx_transactions_category | transactions | category_id | Acelerar filtro por categoria |
| idx_transactions_date | transactions | date | Acelerar filtro por data |
| idx_transactions_type | transactions | type | Acelerar filtro por tipo |
```

---

## Checklist de Documentação

Antes de considerar o projeto pronto, verifique:

- [ ] README.md completo com todas as seções
- [ ] Instruções de instalação testadas (clonar, instalar, rodar)
- [ ] Exemplos de uso com curl ou instruções de CLI
- [ ] Diagrama ER no README
- [ ] Diagrama de arquitetura no README
- [ ] Decisões técnicas documentadas
- [ ] Comentários nos arquivos de código (cabecalho + funções)
- [ ] Swagger customizado (se usando FastAPI)
- [ ] Dicionário de dados
- [ ] Histórico de commits limpo e descritivo
- [ ] Commit: `docs: complete project documentation`

---

## Como a IA pode te ajudar aqui

**Prompt 1 — Criar com ajuda da IA:**
> "Gere um README.md completo para meu projeto com base nesta descrição: [descrição]. Inclua seções de instalação, uso, endpoints e modelo de dados."

**Prompt 2 — Praticar com projetos:**
> "Revise este README e me diga se esta faltando alguma seção importante para um projeto de portfolio no GitHub."

**Prompt 3 — Explorar o conceito:**
> "Adicione docstrings a estas funções Python seguindo o padrão do projeto: [código]."

---

## Casos de Uso no Mundo Real

### Caso 1: Documentação da Stripe

A Stripe (empresa de pagamentos) e considerada referência em documentação de API. Cada endpoint tem descrição clara, exemplos em múltiplas linguagens, códigos de erro documentados é um playground interativo. Desenvolvedores escolhem a Stripe em vez de concorrentes em parte por causa da documentação. O Swagger que você esta gerando no TCC segue o mesmo princípio — documentação interativa que facilita o uso.

### Caso 2: READMEs no GitHub

Projetos open source de sucesso no GitHub tem READMEs excelentes. O framework FastAPI, por exemplo, tem um README que explica o que é, mostra exemplos de código, lista funcionalidades e tem badges de status. Quando recrutadores avaliam candidatos juniores, um dos primeiros lugares que olham e o README dos projetos no GitHub.

### Caso 3: Onboarding em Empresas

Quando um novo desenvolvedor entra em uma empresa, a primeira coisa que ele faz e ler a documentação do projeto. Se a documentação e boa, ele consegue rodar o projeto e entender a arquitetura em horas. Se e ruim, leva dias ou semanas. Empresas como Shopify e GitLab investem pesado em documentação interna exatamente por isso.

---

## Resumo do Módulo

| Conceito | Definição |
|----------|-----------|
| README.md | Documento principal que descreve o projeto |
| Docstring | Comentário estruturado em Python que documenta módulos, classes e funções |
| Swagger | Documentação interativa de API gerada automaticamente |
| Dicionário de dados | Documento que descreve todas as tabelas e campos do banco |
| Comentário inline | Comentário no código que explica o "por que" de uma decisão |
| Portfolio | Conjunto de projetos que demonstra suas habilidades |

---

## Glossário do Módulo

| Termo | Definição |
|-------|-----------|
| Badge | Imagem pequena no README que mostra status (build, versão, licença) |
| Dicionário de dados | Documento que descreve tabelas, campos, tipos e restrições |
| Docstring | String de documentação em Python, delimitada por aspas triplas |
| Endpoint | URL específica que aceita requisições em uma API |
| Markdown | Linguagem de marcacao usada em READMEs e documentação |
| Onboarding | Processo de integração de novo membro em uma equipe |
| Open source | Software com código-fonte aberto e acessível |
| Portfolio | Coleção de projetos que demonstra competências técnicas |
| README | Arquivo principal de documentação de um projeto |
| Swagger | Ferramenta de documentação interativa para APIs REST |
| Tag | Marcacao de versão no Git |

---

## Na Cultura Popular

- **Apollo 13** (filme, 1995) — quando o módulo lunar teve problemas, os engenheiros da NASA conseguiram resolver porque tinham documentação detalhada de cada componente. Sem essa documentação, seria impossível improvisar soluções a distancia. Documentação salva projetos — e as vezes, vidas.

- **The Martian** (filme, 2015) — Mark Watney sobrevive em Marte em parte porque documenta tudo que faz. Cada experimento, cada decisão, cada resultado. Quando a NASA precisa ajuda-lo, a documentação permite que engenheiros na Terra entendam a situação e proponham soluções.

---

## Para Saber Mais

- [How to Write a Good README](https://www.makeareadme.com/) — *Guia prático e visual para escrever READMEs profissionais*
- [FastAPI Documentation — Metadata and Docs URLs](https://fastapi.tiangolo.com/tutorial/metadata/) — *Como customizar o Swagger gerado pelo FastAPI*
- [Choose a License](https://choosealicense.com/) — *Guia para escolher a licença certa para seu projeto open source*
- [GitHub Student Developer Pack](https://education.github.com/pack) — *Ferramentas gratuitas para estudantes, incluindo GitHub Pro*

---

## Perguntas Frequentes (FAQ)

**P: Preciso documentar tudo?**
R: Não tudo, mas o suficiente para que alguém consiga rodar e entender o projeto sem perguntar para você. README completo, comentários nas partes não obvias e Swagger customizado são o mínimo.

**P: Posso escrever a documentação em portugues?**
R: O README pode ser em portugues (e o idioma do curso). Comentários no código podem ser em portugues. Nomes de variáveis e funções devem ser em ingles (convenção técnica). O Swagger pode ser em ingles ou portugues.

**P: Quando devo escrever a documentação?**
R: Idealmente, durante o desenvolvimento — não no final. Atualize o README a cada etapa. Adicione comentários enquanto escreve o código. Documentação escrita "depois" tende a ser incompleta.

**P: A documentação conta na avaliação do TCC?**
R: Sim, é muito. Um projeto funcional com boa documentação e avaliado melhor que um projeto com mais funcionalidades mas sem documentação. Documentação mostra maturidade profissional.

**P: Como documento regras de negócio?**
R: No código, use comentários no serviço explicando cada regra. No README, liste as regras na seção de funcionalidades. Exemplo: "Não é possível remover uma categoria que possui transações associadas (retorna erro 409)."

**P: Preciso de um changelog?**
R: Para o TCC, o histórico de commits do Git funciona como changelog. Se quiser ir além, crie um arquivo CHANGELOG.md listando as mudanças por versão. Mas não é obrigatório.

**P: Como documento erros da API?**
R: No Swagger, use `responses` para documentar cada código de erro possível. No README, inclua uma tabela com os códigos de erro e quando ocorrem. Exemplo: "409 Conflict — ao tentar remover categoria com transações associadas."

**P: Devo documentar o processo de desenvolvimento?**
R: O histórico de commits já documenta o processo. Se quiser ir além, adicione uma seção "Desenvolvimento" no README descrevendo as fases e o que foi feito em cada uma. Mas não é obrigatório para o TCC.

**P: Como faco para o README ficar bonito no GitHub?**
R: Use Markdown corretamente: títulos com `#`, tabelas com `|`, blocos de código com crases triplas, listas com `-`. O GitHub renderiza Markdown automaticamente. Diagramas Mermaid também são renderizados no GitHub. Adicione uma descrição curta no campo "About" do repositório e topics relevantes.

**P: Devo incluir screenshots no README?**
R: Para o TCC, screenshots do Swagger e de respostas da API são um diferencial. Crie uma pasta `docs/images/` e referencie no README com `![descrição](docs/images/screenshot.png)`. Mas não é obrigatório — os diagramas Mermaid e exemplos curl já são suficientes.

**P: Posso ter documentação em ingles?**
R: O README pode ser em portugues (idioma do curso). Se você quiser ter uma versão em ingles também (README.en.md), é um diferencial para portfolio internacional. Mas não é obrigatório.

**P: Preciso de um arquivo requirements.txt?**
R: Sim. Crie um arquivo `requirements.txt` listando as dependências do projeto com versões: `fastapi>=0.100.0`, `uvicorn>=0.20.0`. Isso permite que qualquer pessoa instale as dependências com `pip install -r requirements.txt`. É uma prática padrão em projetos Python.

**P: Preciso de documentação além do README?**
R: Para o TCC, o README completo e suficiente. Se quiser ir além, um arquivo `docs/database.md` com o dicionário de dados é um diferencial.

**P: Como sei se minha documentação esta boa?**
R: Peça para alguém que não conhece o projeto tentar roda-lo usando apenas o README. Se conseguir sem perguntar nada, a documentação esta boa.

**P: Posso usar a IA para gerar a documentação?**
R: Sim, mas revise tudo. A IA pode gerar um rascunho excelente, mas você precisa garantir que está correto e completo. Documentação errada é pior que nenhuma documentação.


---

## Exercícios Práticos

### Exercício 1: Complete o README

Atualize o README.md do seu projeto com todas as seções listadas neste módulo:
- Descrição, funcionalidades, tecnologias
- Instruções de instalação e execução
- Tabela de endpoints (se API)
- Exemplos de uso com curl
- Diagramas ER e de arquitetura
- Decisões técnicas

### Exercício 2: Adicione Comentários ao Código

Revise todos os arquivos do projeto e adicione:
- Docstring no topo de cada arquivo
- Docstring em cada classe
- Docstring em cada função pública
- Comentários inline nas decisões não obvias
- Traducao de variáveis em ingles

### Exercício 3: Teste a Documentação

Peça para um colega (ou simule você mesmo em uma pasta nova):
1. Clone o repositório
2. Siga apenas as instruções do README
3. Tente rodar o projeto e testar os endpoints
4. Anote tudo que não ficou claro ou que faltou
5. Ajuste a documentação com base no feedback

---

[← Anterior: Desenvolvimento Incremental](cap13-mod03-desenvolvimento.md) · [Próximo: Apresentação e Defesa do Projeto →](cap13-mod05-apresentacao.md)
