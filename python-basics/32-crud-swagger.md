# 32 — CRUD com Swagger: Documentação Interativa da API

[<- Anterior: CRUD com FastAPI](31-crud-fastapi.md) | [Glossário](00-glossario.md)

---

## Introdução

No módulo anterior, você construiu uma API HTTP com FastAPI que permite cadastrar, listar, buscar, atualizar e excluir produtos. Para testar, você usou o curl no terminal — digitando comandos longos com headers e JSON. Funciona, mas não e a forma mais prática.

Neste módulo, você vai descobrir que o FastAPI ja vem com uma ferramenta incrivel embutida: o **Swagger UI**. E uma interface grafica no navegador que permite testar todas as rotas da API sem digitar nenhum comando curl. Além disso, o Swagger serve como **documentação viva** da sua API — qualquer pessoa que acessar consegue entender o que a API faz e como usa-la.

### O Que e Swagger?

Imagine que você comprou um eletrodomestico novo. Junto com ele vem um **manual de instruções** que explica: quais botoes existem, o que cada botao faz, e como usar cada função. O Swagger e o "manual de instruções" da sua API.

Mais especificamente:

- **Swagger UI:** Uma página web interativa que lista todas as rotas da API, mostra os parametros esperados e permite testar cada rota diretamente no navegador
- **OpenAPI:** O padrão (especificacao) que descreve a estrutura da API em formato JSON. O Swagger UI le essa especificacao e gera a interface grafica

O melhor de tudo: **o FastAPI gera o Swagger automaticamente**. Você não precisa escrever nenhuma documentação extra — o FastAPI cria tudo a partir do seu código Python.

### O Que Você Vai Aprender

- Como acessar o Swagger UI gerado pelo FastAPI
- Como testar todas as operações CRUD pelo navegador
- Como personalizar a documentação com títulos, descricoes e exemplos
- Como usar tags para organizar as rotas
- Como adicionar exemplos de requisicao e resposta

> **Dica:** Consulte o [Glossário](00-glossario.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Use a mesma pasta do projeto CRUD: `~/meus-projetos/crud-produtos/`
2. Certifique-se de que o ambiente virtual esta ativo: `source venv/bin/activate`
3. Certifique-se de que FastAPI e Uvicorn estão instalados
4. Execute a aplicação: `uvicorn main:app --reload`
5. Acesse o Swagger no navegador: `http://127.0.0.1:8000/docs`

---

## Acessando o Swagger UI

Quando você executa a aplicação FastAPI com `uvicorn main:app --reload`, o FastAPI automaticamente gera duas páginas de documentação:

| Endereco | O Que E |
|----------|---------|
| `http://127.0.0.1:8000/docs` | Swagger UI — interface interativa |
| `http://127.0.0.1:8000/redoc` | ReDoc — documentação em formato de leitura |

### Passo a Passo: Acessar o Swagger

1. Abra o terminal e execute a aplicação:

```bash
cd ~/meus-projetos/crud-produtos
source venv/bin/activate
uvicorn main:app --reload
```

2. Abra o navegador e acesse: `http://127.0.0.1:8000/docs`

3. Você vera uma página com todas as rotas da API listadas, organizadas por método HTTP (GET, POST, PUT, DELETE)

### O Que Você Ve no Swagger UI

A página do Swagger mostra:

- **Título da API** e descricao (configurados no FastAPI)
- **Lista de rotas** agrupadas por tags
- **Cada rota** mostra: método HTTP, endereco, descricao, parametros e formato da resposta
- **Botao "Try it out"** em cada rota para testar diretamente

---

## Testando o CRUD pelo Swagger

### Testar POST (Cadastrar Produto)

1. No Swagger UI, clique na rota **POST /products**
2. Clique no botao **"Try it out"**
3. No campo "Request body", edite o JSON:

```json
{
    "name": "Arroz",
    "price": 8.99,
    "quantity": 50,
    "category": "Alimentos"
}
```

4. Clique em **"Execute"**
5. Veja a resposta abaixo com o produto criado e o ID gerado

### Testar GET (Listar Produtos)

1. Clique na rota **GET /products**
2. Clique em **"Try it out"**
3. Clique em **"Execute"**
4. Veja a lista de produtos em formato JSON

### Testar GET por ID (Buscar Produto)

1. Clique na rota **GET /products/{product_id}**
2. Clique em **"Try it out"**
3. Digite o ID no campo (por exemplo, `1`)
4. Clique em **"Execute"**
5. Veja os dados do produto ou erro 404 se não existir

### Testar PUT (Atualizar Produto)

1. Clique na rota **PUT /products/{product_id}**
2. Clique em **"Try it out"**
3. Digite o ID e edite o JSON com os novos dados
4. Clique em **"Execute"**

### Testar DELETE (Excluir Produto)

1. Clique na rota **DELETE /products/{product_id}**
2. Clique em **"Try it out"**
3. Digite o ID do produto a excluir
4. Clique em **"Execute"**

> Todas as operações que você fazia com curl agora podem ser feitas pelo navegador, de forma visual e interativa.

---

## Personalizando a Documentação

### Título e Descricao da API

Você pode personalizar o título, descricao e versão da API ao criar a aplicação FastAPI:


```python
# Importamos o FastAPI
from fastapi import FastAPI

# Criamos a aplicacao com informacoes personalizadas
# "title" = titulo da API
# "description" = descricao da API
# "version" = versao da API
app = FastAPI(
    title="API de Cadastro de Produtos",
    description="Sistema CRUD para gerenciamento de produtos com SQLite. "
                "Permite cadastrar, listar, buscar, atualizar e excluir produtos.",
    version="1.0.0"
)
```

Essas informações aparecem no topo da página do Swagger UI.

### Descricoes nas Rotas

As docstrings das funções aparecem como descricao de cada rota no Swagger:

```python
# A docstring da funcao aparece no Swagger como descricao da rota
@app.get("/products")
def list_products():
    """
    Lista todos os produtos cadastrados no sistema.

    Retorna uma lista de produtos em formato JSON.
    Se nao houver produtos, retorna uma lista vazia.
    """
    return database.get_all_products()
```

### Tags para Organizar Rotas

Você pode usar **tags** para agrupar rotas relacionadas no Swagger:

```python
# Importamos FastAPI e HTTPException
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

app = FastAPI(
    title="API de Cadastro de Produtos",
    description="Sistema CRUD completo com SQLite",
    version="1.0.0"
)

database.create_table()


class ProductCreate(BaseModel):
    """Modelo para criar/atualizar produto."""
    name: str
    price: float
    quantity: int
    category: str


# Tag "Produtos" agrupa todas as rotas de produtos
# "tags" = etiquetas (agrupamento no Swagger)
@app.get("/products", tags=["Produtos"])
def list_products():
    """Lista todos os produtos cadastrados."""
    return database.get_all_products()


@app.get("/products/{product_id}", tags=["Produtos"])
def get_product(product_id: int):
    """Busca um produto pelo ID."""
    product = database.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return product


@app.post("/products", tags=["Produtos"], status_code=201)
def create_product(product: ProductCreate):
    """Cadastra um novo produto no sistema."""
    pid = database.insert_product(
        product.name, product.price, product.quantity, product.category
    )
    return {
        "id": pid, "name": product.name, "price": product.price,
        "quantity": product.quantity, "category": product.category
    }


@app.put("/products/{product_id}", tags=["Produtos"])
def update_product(product_id: int, product: ProductCreate):
    """Atualiza os dados de um produto existente."""
    updated = database.update_product(
        product_id, product.name, product.price, product.quantity, product.category
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {
        "id": product_id, "name": product.name, "price": product.price,
        "quantity": product.quantity, "category": product.category
    }


@app.delete("/products/{product_id}", tags=["Produtos"])
def delete_product(product_id: int):
    """Exclui um produto pelo ID."""
    deleted = database.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {"message": f"Produto ID {product_id} excluido com sucesso"}
```

No Swagger UI, todas as rotas aparecerao agrupadas sob a tag "Produtos".

### Exemplos de Requisicao com `model_config`

Você pode adicionar exemplos ao modelo Pydantic para que aparecam no Swagger:

```python
from pydantic import BaseModel


# Modelo com exemplo para o Swagger
class ProductCreate(BaseModel):
    """Modelo para criar um produto."""
    name: str
    price: float
    quantity: int
    category: str

    # model_config define configuracoes do modelo
    # json_schema_extra adiciona exemplos ao Swagger
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Arroz Integral",
                    "price": 12.50,
                    "quantity": 30,
                    "category": "Alimentos"
                }
            ]
        }
    }
```

Quando você clicar em "Try it out" no Swagger, o exemplo ja aparecera preenchido no campo de requisicao.

### Descricoes nos Campos do Modelo

Você pode adicionar descricoes a cada campo usando `Field`:

```python
from pydantic import BaseModel, Field


# Modelo com descricoes nos campos
class ProductCreate(BaseModel):
    """Modelo para criar um produto."""
    # Field() permite adicionar descricao, exemplo e validacao
    # "description" = descricao do campo
    # "example" = exemplo de valor
    name: str = Field(description="Nome do produto", example="Arroz")
    price: float = Field(description="Preco em reais (>= 0)", example=8.99, ge=0)
    quantity: int = Field(description="Quantidade em estoque (>= 0)", example=50, ge=0)
    category: str = Field(description="Categoria do produto", example="Alimentos")
```

No Swagger, cada campo mostrara sua descricao e exemplo. O `ge=0` (greater than or equal = maior ou igual) adiciona validação automática.

---

## Programa Completo: API com Swagger Personalizado

Aqui esta a versão final do `main.py` com todas as personalizacoes:

```python
# ============================================================
# CRUD de Produtos — Versao 4 (Final)
# API HTTP com FastAPI + SQLite + Swagger personalizado
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import database

# Criamos a aplicacao com documentacao personalizada
app = FastAPI(
    title="API de Cadastro de Produtos",
    description=(
        "Sistema CRUD completo para gerenciamento de produtos. "
        "Armazenamento em banco de dados SQLite com documentacao Swagger interativa. "
        "Desenvolvido como projeto final do curso de Python para iniciantes."
    ),
    version="1.0.0"
)

# Criamos a tabela ao iniciar
database.create_table()


# --- Modelos ---

class ProductCreate(BaseModel):
    """Dados para criar ou atualizar um produto."""
    name: str = Field(description="Nome do produto", example="Arroz Integral")
    price: float = Field(description="Preco em reais", example=12.50, ge=0)
    quantity: int = Field(description="Quantidade em estoque", example=30, ge=0)
    category: str = Field(description="Categoria do produto", example="Alimentos")

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Arroz Integral",
                    "price": 12.50,
                    "quantity": 30,
                    "category": "Alimentos"
                }
            ]
        }
    }


class ProductResponse(BaseModel):
    """Dados de um produto retornado pela API."""
    id: int = Field(description="Identificador unico do produto")
    name: str = Field(description="Nome do produto")
    price: float = Field(description="Preco em reais")
    quantity: int = Field(description="Quantidade em estoque")
    category: str = Field(description="Categoria do produto")


class MessageResponse(BaseModel):
    """Mensagem de resposta para operacoes de exclusao."""
    message: str = Field(description="Mensagem de confirmacao")


# --- Rotas ---

@app.get("/products", response_model=list[ProductResponse], tags=["Produtos"],
         summary="Listar todos os produtos")
def list_products():
    """
    Retorna a lista completa de produtos cadastrados.

    Se nao houver produtos, retorna uma lista vazia `[]`.
    """
    return database.get_all_products()


@app.get("/products/{product_id}", response_model=ProductResponse, tags=["Produtos"],
         summary="Buscar produto por ID")
def get_product(product_id: int):
    """
    Busca um produto pelo seu identificador unico.

    - **product_id**: ID do produto (numero inteiro)

    Retorna erro 404 se o produto nao for encontrado.
    """
    product = database.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return product


@app.post("/products", response_model=ProductResponse, status_code=201,
          tags=["Produtos"], summary="Cadastrar novo produto")
def create_product(product: ProductCreate):
    """
    Cadastra um novo produto no sistema.

    O ID e gerado automaticamente pelo banco de dados.
    Todos os campos sao obrigatorios.
    """
    pid = database.insert_product(
        product.name, product.price, product.quantity, product.category
    )
    return {
        "id": pid, "name": product.name, "price": product.price,
        "quantity": product.quantity, "category": product.category
    }


@app.put("/products/{product_id}", response_model=ProductResponse,
         tags=["Produtos"], summary="Atualizar produto")
def update_product(product_id: int, product: ProductCreate):
    """
    Atualiza os dados de um produto existente.

    - **product_id**: ID do produto a atualizar

    Retorna erro 404 se o produto nao for encontrado.
    """
    updated = database.update_product(
        product_id, product.name, product.price, product.quantity, product.category
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {
        "id": product_id, "name": product.name, "price": product.price,
        "quantity": product.quantity, "category": product.category
    }


@app.delete("/products/{product_id}", response_model=MessageResponse,
            tags=["Produtos"], summary="Excluir produto")
def delete_product(product_id: int):
    """
    Exclui um produto pelo seu identificador.

    - **product_id**: ID do produto a excluir

    Retorna erro 404 se o produto nao for encontrado.
    A exclusao e permanente e nao pode ser desfeita.
    """
    deleted = database.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {"message": f"Produto ID {product_id} excluido com sucesso"}
```

Para executar:

```bash
cd ~/meus-projetos/crud-produtos
source venv/bin/activate
uvicorn main:app --reload
```

Acesse `http://127.0.0.1:8000/docs` no navegador para ver o Swagger completo.

---

## A Especificacao OpenAPI

O FastAPI gera automaticamente a especificacao OpenAPI da sua API. Você pode acessar em:

- `http://127.0.0.1:8000/openapi.json` — Especificacao completa em JSON

Essa especificacao e um documento JSON que descreve toda a estrutura da API: rotas, parametros, modelos de dados, códigos de resposta, etc. O Swagger UI le esse documento e gera a interface grafica.

Você pode usar essa especificacao para:

- Gerar clientes automaticos em outras linguagens
- Importar no Postman para testes
- Compartilhar com outros desenvolvedores

---

## Evolucao Completa do Projeto CRUD

Parabéns! Você completou as 4 versoes do projeto CRUD:

```
Modulo 29: CRUD em Memoria
    Lista de dicionarios → dados temporarios → menu no terminal
         |
         v
Modulo 30: CRUD com SQLite
    Banco de dados em arquivo → dados persistentes → menu no terminal
         |
         v
Modulo 31: CRUD com FastAPI
    SQLite + API HTTP → acesso por qualquer cliente → curl/navegador
         |
         v
Modulo 32: CRUD com Swagger
    FastAPI + documentacao automatica → interface interativa → Swagger UI
```

| Versão | Armazenamento | Interface | Documentação |
|--------|---------------|-----------|-------------|
| v1 (Mod 29) | Memória (lista) | Terminal (menu) | Nenhuma |
| v2 (Mod 30) | SQLite (arquivo) | Terminal (menu) | Nenhuma |
| v3 (Mod 31) | SQLite | HTTP (curl) | Nenhuma |
| v4 (Mod 32) | SQLite | HTTP (Swagger UI) | Automática |

Cada versão adicionou uma camada ao projeto, sem descartar o que ja existia. Essa e a forma como projetos reais evoluem — de forma incremental.

---

## Para Saber Mais

- [W3Schools — What is an API](https://www.w3schools.com/whatis/whatis_api.asp)
  _Explicacao simples sobre o que e uma API_
- [W3Schools — HTTP Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
  _Referencia sobre os métodos HTTP usados nas APIs_
- [W3Schools — JSON](https://www.w3schools.com/js/js_json_intro.asp)
  _Introducao ao formato JSON usado nas APIs_
- [Documentação Oficial FastAPI](https://fastapi.tiangolo.com/)
  _Documentacao completa do FastAPI_
- [Documentação Oficial FastAPI — Swagger UI](https://fastapi.tiangolo.com/tutorial/metadata/)
  _Como personalizar a documentação Swagger no FastAPI_
- [Documentação Oficial Python — sqlite3](https://docs.python.org/pt-br/3/library/sqlite3.html)
  _Referencia do módulo sqlite3 em portugues_

---

## Perguntas Frequentes (FAQ)

**P: O que e Swagger?**
R: Swagger e uma ferramenta que gera documentação interativa para APIs. No FastAPI, o Swagger UI e gerado automaticamente a partir do seu código Python. Você acessa pelo navegador e pode testar todas as rotas da API sem usar curl.

**P: Preciso instalar o Swagger separadamente?**
R: Não. O FastAPI ja inclui o Swagger UI automaticamente. Basta acessar `/docs` no navegador quando a aplicação estiver rodando. Não precisa instalar nada extra.

**P: O que e OpenAPI?**
R: OpenAPI e uma especificacao (padrão) que descreve a estrutura de uma API em formato JSON. O Swagger UI le essa especificacao e gera a interface grafica. O FastAPI gera a especificacao OpenAPI automaticamente a partir do seu código.

**P: Qual a diferença entre `/docs` e `/redoc`?**
R: Ambos mostram a documentação da API, mas com interfaces diferentes. `/docs` usa o Swagger UI (interativo, permite testar rotas). `/redoc` usa o ReDoc (formato de leitura, mais bonito para documentação). Ambos sao gerados automaticamente pelo FastAPI.

**P: O que e `response_model`?**
R: E um parametro do decorador de rota que define o formato da resposta. O FastAPI usa o modelo Pydantic para validar a resposta e mostrar o formato esperado no Swagger. Isso ajuda quem esta lendo a documentação a entender o que a rota retorna.

**P: O que sao tags?**
R: Tags sao etiquetas que agrupam rotas relacionadas no Swagger UI. Por exemplo, todas as rotas de produtos ficam sob a tag "Produtos". Isso organiza a documentação quando a API tem muitas rotas.

**P: O que e `summary`?**
R: E um texto curto que aparece ao lado do método HTTP no Swagger. Por exemplo, `summary="Listar todos os produtos"` aparece como título da rota. A docstring da função aparece como descricao detalhada.

**P: O que e `Field` do Pydantic?**
R: `Field` permite adicionar metadados aos campos do modelo: descricao, exemplo, validação (mínimo, máximo). Essas informações aparecem no Swagger, ajudando quem usa a API a entender cada campo.

**P: O que e `ge=0` no Field?**
R: `ge` significa "greater than or equal" (maior ou igual). `ge=0` valida que o valor deve ser maior ou igual a zero. Se alguem enviar um preco negativo, o Pydantic rejeita automaticamente com erro 422.

**P: O que e `model_config` com `json_schema_extra`?**
R: E uma forma de adicionar exemplos ao modelo Pydantic. Os exemplos aparecem no Swagger UI quando você clica em "Try it out", facilitando os testes. O campo ja vem preenchido com o exemplo.

**P: Posso desativar o Swagger?**
R: Sim. Basta passar `docs_url=None` ao criar a aplicação: `app = FastAPI(docs_url=None)`. Isso desativa o Swagger UI. Você pode querer fazer isso em produção por segurança.

**P: O Swagger funciona com qualquer API?**
R: O Swagger UI funciona com qualquer API que tenha uma especificacao OpenAPI. O FastAPI gera essa especificacao automaticamente. Outros frameworks (Flask, Django) precisam de bibliotecas extras para gerar a especificacao.

**P: Posso compartilhar a documentação Swagger com outras pessoas?**
R: Sim. Qualquer pessoa que acessar o endereco da API com `/docs` vera a documentação. Se a API estiver acessível na rede (usando `--host 0.0.0.0`), outros computadores podem acessar.

**P: O que e Postman?**
R: Postman e uma ferramenta popular para testar APIs. Você pode importar a especificacao OpenAPI (`/openapi.json`) no Postman e ele cria automaticamente todas as requisicoes para testar. E uma alternativa ao Swagger UI e ao curl.

**P: O que e CORS?**
R: CORS (Cross-Origin Resource Sharing) e uma politica de segurança dos navegadores. Se você tentar acessar a API de um site em outro dominio, o navegador pode bloquear. O FastAPI tem um middleware para configurar CORS, mas isso esta fora do escopo deste curso.

**P: Posso adicionar autenticação a API?**
R: Sim. O FastAPI suporta vários tipos de autenticação: API Key, OAuth2, JWT, etc. O Swagger UI também suporta autenticação — você pode configurar um botao "Authorize" na página. Isso esta fora do escopo deste curso, mas e um próximo passo natural.

**P: O que e um middleware?**
R: Middleware e um código que executa antes ou depois de cada requisicao. Por exemplo, um middleware de log registra todas as requisicoes, e um middleware de CORS adiciona headers de segurança. O FastAPI suporta middlewares, mas isso esta fora do escopo deste curso.

**P: O FastAPI e usado em empresas reais?**
R: Sim. O FastAPI e usado por empresas como Microsoft, Netflix, Uber e muitas outras. E um dos frameworks Python mais populares para APIs, junto com Django REST Framework e Flask.

**P: Qual o próximo passo depois deste curso?**
R: Você pode aprofundar em vários caminhos: aprender mais sobre bancos de dados (PostgreSQL), autenticação (JWT), deploy em nuvem (Heroku, Railway), frontend (HTML/CSS/JavaScript), ou frameworks web completos (Django). O importante e que você ja tem uma base solida.

**P: Posso usar o Swagger para gerar código automaticamente?**
R: Sim. A especificacao OpenAPI pode ser usada para gerar clientes em várias linguagens (JavaScript, Java, Go, etc.) usando ferramentas como o OpenAPI Generator. Isso e muito útil em equipes onde o frontend e o backend sao desenvolvidos separadamente.

**P: O que e REST?**
R: REST (Representational State Transfer) e um estilo de arquitetura para APIs. Uma API RESTful usa métodos HTTP (GET, POST, PUT, DELETE) para operar sobre recursos (como produtos). Nossa API segue os principios REST, embora não tenhamos usado esse termo explicitamente.

---

## Exercícios

Os exercícios deste módulo estão em um arquivo separado para facilitar a navegação:

[Ir para os Exercícios do Módulo 32 ->](32-crud-swagger-exercicios.md)