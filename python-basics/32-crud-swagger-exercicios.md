# 32 — Exercícios: CRUD com Swagger

[<- Voltar para o módulo](32-crud-swagger.md) | [Glossário](00-glossário.md)

---

> **Antes de começar:** Estes exercícios focam na personalizacao da documentação Swagger e no uso da interface interativa. Certifique-se de que o FastAPI esta instalado e que você sabe executar a aplicação com `uvicorn`. Tente resolver cada exercício sozinho antes de consultar a resposta.

> **Como testar:** Execute com `uvicorn nome_arquivo:app --reload` e acesse `http://127.0.0.1:8000/docs` no navegador.

---

### Exercício 1 — Acessar o Swagger UI

#### Enunciado

Crie uma aplicação FastAPI minima com uma rota GET em `/` que retorne `{"status": "online"}`. Execute a aplicação e acesse o Swagger UI no navegador. Identifique: o título da API, a rota listada e o botao "Try it out".

#### Dicas

- Crie o arquivo com `FastAPI()` e uma rota `@app.get("/")`
- Execute com `uvicorn nome:app --reload`
- Acesse `http://127.0.0.1:8000/docs` no navegador

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** A página do Swagger deve abrir mostrando a rota GET /
- **Caso de borda:** Acesse `http://127.0.0.1:8000/redoc` — deve mostrar a mesma documentação em formato diferente

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos o FastAPI
# "FastAPI" = framework para criar APIs
from fastapi import FastAPI

# Criamos a aplicacao
# "app" = aplicacao
app = FastAPI()


# Rota GET na raiz
# @app.get("/") = rota que responde a GET /
@app.get("/")
def root():
    """Verifica se a API esta funcionando."""
    # Retornamos o status da API
    # "status" = estado, "online" = funcionando
    return {"status": "online"}
```

Para executar:
```bash
uvicorn ex01_swagger:app --reload
```

Para testar:
```
1. Abra o navegador
2. Acesse http://127.0.0.1:8000/docs
3. Voce vera a rota GET / listada
4. Clique na rota, depois em "Try it out", depois em "Execute"
5. A resposta aparecera abaixo: {"status": "online"}
```

---

### Exercício 2 — Personalizar Título e Descricao

#### Enunciado

Crie uma aplicação FastAPI com título "Minha Primeira API", descricao "API de teste para aprender Swagger" e versão "0.1.0". Adicione uma rota GET `/hello` que retorne uma saudacao. Verifique no Swagger que o título e a descricao aparecem.

#### Dicas

- Use os parametros `title`, `description` e `version` do `FastAPI()`
- A docstring da função aparece como descricao da rota no Swagger

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** O Swagger deve mostrar "Minha Primeira API" como título e a descricao abaixo
- **Caso de borda:** Altere a versão para "0.2.0" e recarregue — a versão deve atualizar no Swagger

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI

# Criamos a aplicacao com informacoes personalizadas
# "title" = titulo, "description" = descricao, "version" = versao
app = FastAPI(
    title="Minha Primeira API",
    description="API de teste para aprender Swagger",
    version="0.1.0"
)


# Rota GET com docstring descritiva
@app.get("/hello")
def hello():
    """
    Retorna uma mensagem de saudacao.

    Esta rota e apenas para teste e aprendizado.
    """
    # "greeting" = saudacao
    return {"greeting": "Ola! Bem-vindo a minha primeira API!"}
```

Para testar:
```
1. Execute: uvicorn ex02_title:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Verifique o titulo "Minha Primeira API" no topo
4. Verifique a descricao abaixo do titulo
5. Clique na rota GET /hello — a docstring aparece como descricao
```

---

### Exercício 3 — Usar Tags para Organizar Rotas

#### Enunciado

Crie uma aplicação com 4 rotas: 2 rotas de "Produtos" (listar e buscar) e 2 rotas de "Sistema" (status e versão). Use tags para agrupar as rotas no Swagger.

#### Dicas

- Use `tags=["Produtos"]` nas rotas de produtos
- Use `tags=["Sistema"]` nas rotas de sistema
- No Swagger, as rotas aparecerao agrupadas por tag

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** No Swagger, as rotas devem aparecer em 2 grupos: "Produtos" e "Sistema"
- **Caso de borda:** Clique no nome da tag para expandir/recolher o grupo

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI

app = FastAPI(title="API com Tags")

# Lista fixa de produtos para teste
products = [
    {"id": 1, "name": "Arroz", "price": 8.99},
    {"id": 2, "name": "Sabao", "price": 4.50}
]


# --- Rotas de Produtos (tag "Produtos") ---

# tags=["Produtos"] agrupa esta rota sob a tag "Produtos" no Swagger
@app.get("/products", tags=["Produtos"])
def list_products():
    """Lista todos os produtos cadastrados."""
    return products


@app.get("/products/{product_id}", tags=["Produtos"])
def get_product(product_id: int):
    """Busca um produto pelo ID."""
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Nao encontrado"}


# --- Rotas de Sistema (tag "Sistema") ---

# tags=["Sistema"] agrupa esta rota sob a tag "Sistema" no Swagger
@app.get("/status", tags=["Sistema"])
def get_status():
    """Retorna o status da API."""
    # "status" = estado, "online" = funcionando
    return {"status": "online", "products_count": len(products)}


@app.get("/version", tags=["Sistema"])
def get_version():
    """Retorna a versao da API."""
    # "version" = versao
    return {"version": "1.0.0", "api": "Cadastro de Produtos"}
```

Para testar:
```
1. Execute: uvicorn ex03_tags:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Verifique que as rotas estao agrupadas em "Produtos" e "Sistema"
```


---

### Exercício 4 — Modelo Pydantic com Field e Exemplos

#### Enunciado

Crie um modelo Pydantic `ProductCreate` usando `Field` para adicionar descricao, exemplo e validação (preco >= 0, quantidade >= 0) a cada campo. Crie uma rota POST que use esse modelo. Verifique no Swagger que as descricoes e exemplos aparecem.

#### Dicas

- Importe `Field` de `pydantic`
- Use `Field(description="...", example=..., ge=0)` para cada campo
- `ge=0` significa "greater than or equal to 0" (maior ou igual a zero)

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** No Swagger, clique em "Try it out" na rota POST — o exemplo deve aparecer preenchido
- **Caso de borda:** Envie preco negativo — deve retornar erro 422 com mensagem de validação

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
# Importamos Field para adicionar metadados aos campos
# "Field" = campo (com descricao, exemplo e validacao)
from pydantic import BaseModel, Field

app = FastAPI(title="API com Validacao")


# Modelo com Field para descricoes e validacoes
class ProductCreate(BaseModel):
    """Dados para criar um produto."""
    # Field() adiciona descricao, exemplo e validacao
    # "description" = descricao do campo
    # "example" = exemplo de valor
    # "ge" = greater than or equal (maior ou igual)
    name: str = Field(
        description="Nome do produto (nao pode ser vazio)",
        example="Arroz Integral"
    )
    price: float = Field(
        description="Preco em reais (deve ser >= 0)",
        example=12.50,
        ge=0
    )
    quantity: int = Field(
        description="Quantidade em estoque (deve ser >= 0)",
        example=30,
        ge=0
    )
    category: str = Field(
        description="Categoria do produto",
        example="Alimentos"
    )


# Rota POST que usa o modelo com validacao
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """Cadastra um novo produto com validacao automatica."""
    # Os dados ja foram validados pelo Pydantic
    return {
        "id": 1,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }
```

Para testar:
```
1. Execute: uvicorn ex04_field:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Clique em POST /products -> "Try it out"
4. O exemplo ja aparece preenchido
5. Altere o preco para -5 e clique "Execute" — erro 422
```

---

### Exercício 5 — Modelo com json_schema_extra

#### Enunciado

Adicione `model_config` com `json_schema_extra` ao modelo `ProductCreate` para definir um exemplo completo que apareca no Swagger. Crie uma rota POST e verifique que o exemplo aparece ao clicar "Try it out".

#### Dicas

- Adicione `model_config` como atributo da classe
- Use `json_schema_extra` com uma lista de `examples`
- Cada exemplo e um dicionário com todos os campos

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** No Swagger, o exemplo deve aparecer preenchido ao clicar "Try it out"
- **Caso de borda:** Altere o exemplo e recarregue — o novo exemplo deve aparecer

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API com Exemplos")


# Modelo com exemplo completo via model_config
class ProductCreate(BaseModel):
    """Dados para criar um produto."""
    name: str       # Nome do produto (name = nome)
    price: float    # Preco do produto (price = preco)
    quantity: int   # Quantidade (quantity = quantidade)
    category: str   # Categoria (category = categoria)

    # model_config define configuracoes do modelo
    # json_schema_extra adiciona exemplos ao schema JSON
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Cafe Premium",
                    "price": 25.90,
                    "quantity": 15,
                    "category": "Bebidas"
                }
            ]
        }
    }


@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """Cadastra produto com exemplo no Swagger."""
    return {"id": 1, **product.model_dump()}
```

Para testar:
```
1. Execute: uvicorn ex05_examples:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Clique em POST /products -> "Try it out"
4. O exemplo "Cafe Premium" deve aparecer preenchido
```

---

### Exercício 6 — Rota com Summary e Descricao Detalhada

#### Enunciado

Crie 3 rotas (GET, POST, DELETE) com `summary` (título curto) e docstrings detalhadas (descricao longa). Use formatacao Markdown nas docstrings. Verifique no Swagger que o summary aparece como título e a docstring como descricao expandida.

#### Dicas

- Use `summary="Titulo curto"` no decorador da rota
- A docstring da função aparece como descricao detalhada
- Você pode usar Markdown na docstring (negrito, listas, etc.)

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** No Swagger, cada rota deve mostrar o summary como título
- **Caso de borda:** Clique na rota para expandir — a docstring detalhada deve aparecer

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API com Descricoes")

# Lista simples para teste
products = [{"id": 1, "name": "Arroz", "price": 8.99}]


class ProductCreate(BaseModel):
    name: str
    price: float


# Rota GET com summary e docstring detalhada
# "summary" = resumo (titulo curto no Swagger)
@app.get("/products", summary="Listar todos os produtos")
def list_products():
    """
    Retorna a lista completa de produtos cadastrados.

    **Formato da resposta:** Lista de objetos JSON.

    **Campos retornados:**
    - `id`: Identificador unico do produto
    - `name`: Nome do produto
    - `price`: Preco em reais

    Se nao houver produtos, retorna uma lista vazia `[]`.
    """
    return products


# Rota POST com summary e docstring
@app.post("/products", status_code=201, summary="Cadastrar novo produto")
def create_product(product: ProductCreate):
    """
    Cadastra um novo produto no sistema.

    **Campos obrigatorios:**
    - `name`: Nome do produto (texto)
    - `price`: Preco em reais (numero decimal)

    O ID e gerado automaticamente.
    """
    new_product = {"id": len(products) + 1, "name": product.name, "price": product.price}
    products.append(new_product)
    return new_product


# Rota DELETE com summary e docstring
@app.delete("/products/{product_id}", summary="Excluir produto")
def delete_product(product_id: int):
    """
    Exclui um produto pelo seu identificador.

    **Parametro:**
    - `product_id`: ID do produto a excluir (inteiro)

    **Erros possiveis:**
    - `404`: Produto nao encontrado

    **Atencao:** A exclusao e permanente.
    """
    for i, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(i)
            return {"message": f"Produto {product_id} excluido"}
    raise HTTPException(status_code=404, detail="Nao encontrado")
```

Para testar:
```
1. Execute: uvicorn ex06_summary:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Cada rota mostra o summary como titulo
4. Clique para expandir — a docstring formatada aparece
```

---

### Exercício 7 — Response Model para Documentar Respostas

#### Enunciado

Crie modelos Pydantic separados para requisicao (`ProductCreate`) e resposta (`ProductResponse`). Use `response_model` nas rotas para documentar o formato exato da resposta no Swagger.

#### Dicas

- `ProductCreate` não tem `id` (o banco gera)
- `ProductResponse` tem `id` (retornado pelo banco)
- Use `response_model=ProductResponse` no decorador da rota

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** No Swagger, a secao "Responses" de cada rota deve mostrar o formato da resposta
- **Caso de borda:** O modelo de resposta deve incluir o campo `id` que não existe no modelo de requisicao

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="API com Response Model")


# Modelo para requisicao (sem ID)
class ProductCreate(BaseModel):
    """Dados para criar produto (enviados pelo cliente)."""
    name: str = Field(example="Arroz")
    price: float = Field(example=8.99, ge=0)


# Modelo para resposta (com ID)
class ProductResponse(BaseModel):
    """Dados do produto retornado pela API (com ID)."""
    id: int = Field(description="ID gerado pelo banco")
    name: str = Field(description="Nome do produto")
    price: float = Field(description="Preco em reais")


# Contador simples para IDs
next_id = 1


# Rota POST com response_model
# response_model=ProductResponse documenta o formato da resposta
@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    """Cadastra produto e retorna com ID."""
    global next_id
    # Montamos a resposta com o ID gerado
    response = {
        "id": next_id,
        "name": product.name,
        "price": product.price
    }
    next_id = next_id + 1
    return response


# Rota GET com response_model de lista
# response_model=list[ProductResponse] = lista de produtos
@app.get("/products", response_model=list[ProductResponse])
def list_products():
    """Lista todos os produtos."""
    return [
        {"id": 1, "name": "Arroz", "price": 8.99},
        {"id": 2, "name": "Sabao", "price": 4.50}
    ]
```

Para testar:
```
1. Execute: uvicorn ex07_response:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Clique em POST /products — veja "Responses" com o formato ProductResponse
4. Clique em GET /products — veja que retorna lista de ProductResponse
```

---

### Exercício 8 — Testar Todas as Operações pelo Swagger

#### Enunciado

Usando a API completa do módulo principal (`main.py` com `database.py` e `models.py`), execute a seguinte sequência de testes pelo Swagger UI: (1) cadastre 3 produtos, (2) liste todos, (3) busque o produto 2, (4) atualize o produto 1, (5) exclua o produto 3, (6) liste novamente para confirmar.

#### Dicas

- Execute `uvicorn main:app --reload` na pasta do projeto
- Acesse `http://127.0.0.1:8000/docs`
- Use "Try it out" em cada rota na sequência indicada
- Anote os IDs retornados para usar nas operações seguintes

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Apos a sequência completa, a lista final deve ter 2 produtos (o 3 foi excluido)
- **Caso de borda:** Tente buscar o produto 3 apos excluir — deve retornar 404

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```
Sequencia de testes no Swagger UI:

1. POST /products — Cadastrar produto 1:
   Body: {"name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"}
   Resposta esperada: {"id": 1, "name": "Arroz", ...}

2. POST /products — Cadastrar produto 2:
   Body: {"name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"}
   Resposta esperada: {"id": 2, "name": "Sabao", ...}

3. POST /products — Cadastrar produto 3:
   Body: {"name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
   Resposta esperada: {"id": 3, "name": "Shampoo", ...}

4. GET /products — Listar todos:
   Resposta esperada: lista com 3 produtos

5. GET /products/2 — Buscar produto 2:
   Resposta esperada: {"id": 2, "name": "Sabao", ...}

6. PUT /products/1 — Atualizar produto 1:
   Body: {"name": "Arroz Integral", "price": 12.50, "quantity": 30, "category": "Alimentos"}
   Resposta esperada: {"id": 1, "name": "Arroz Integral", ...}

7. DELETE /products/3 — Excluir produto 3:
   Resposta esperada: {"message": "Produto ID 3 excluido com sucesso"}

8. GET /products — Listar novamente:
   Resposta esperada: lista com 2 produtos (Arroz Integral e Sabao)

9. GET /products/3 — Buscar produto excluido:
   Resposta esperada: {"detail": "Produto nao encontrado"} (status 404)
```

> Este exercício não tem código Python — e um exercício prático de uso da interface Swagger.

---

### Exercício 9 — Acessar a Especificacao OpenAPI

#### Enunciado

Com a API rodando, acesse a especificacao OpenAPI em `http://127.0.0.1:8000/openapi.json`. Identifique no JSON: o título da API, a versão, a lista de rotas (paths) e os modelos de dados (schemas).

#### Dicas

- Acesse a URL no navegador ou com curl
- O JSON e grande — use um formatador de JSON online para facilitar a leitura
- Procure as chaves: "info", "paths", "components"

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** O JSON deve conter "info" com título e versão, "paths" com as rotas
- **Caso de borda:** Adicione uma nova rota e recarregue — a especificacao deve atualizar automaticamente

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Acessamos a especificacao OpenAPI com curl
# O resultado e um JSON grande com toda a estrutura da API
curl http://127.0.0.1:8000/openapi.json
```

```
Estrutura do JSON retornado:

{
    "openapi": "3.1.0",           <- Versao do padrao OpenAPI
    "info": {
        "title": "API de Cadastro de Produtos",  <- Titulo da API
        "description": "Sistema CRUD...",          <- Descricao
        "version": "1.0.0"                        <- Versao da API
    },
    "paths": {
        "/products": {             <- Rota /products
            "get": { ... },        <- Metodo GET (listar)
            "post": { ... }        <- Metodo POST (criar)
        },
        "/products/{product_id}": {  <- Rota com parametro
            "get": { ... },          <- Metodo GET (buscar)
            "put": { ... },          <- Metodo PUT (atualizar)
            "delete": { ... }        <- Metodo DELETE (excluir)
        }
    },
    "components": {
        "schemas": {               <- Modelos de dados
            "ProductCreate": { ... },   <- Modelo de criacao
            "ProductResponse": { ... }  <- Modelo de resposta
        }
    }
}
```

> A especificacao OpenAPI e gerada automaticamente pelo FastAPI. Qualquer alteração no código reflete imediatamente na especificacao.

---

### Exercício 10 — Desativar e Reativar o Swagger

#### Enunciado

Crie uma aplicação onde o Swagger UI esta desativado (`docs_url=None`). Verifique que `/docs` retorna 404. Depois, reative mudando para `docs_url="/documentacao"` e acesse pelo novo endereco.

#### Dicas

- Use `docs_url=None` para desativar o Swagger
- Use `docs_url="/documentacao"` para mudar o endereco
- Use `redoc_url=None` para desativar o ReDoc também

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Com `docs_url=None`, acessar `/docs` deve retornar 404
- **Caso de borda:** Com `docs_url="/documentacao"`, acessar `/documentacao` deve abrir o Swagger

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI

# Versao 1: Swagger desativado
# docs_url=None desativa o Swagger UI
# redoc_url=None desativa o ReDoc
# app = FastAPI(docs_url=None, redoc_url=None)

# Versao 2: Swagger em endereco customizado
# docs_url="/documentacao" muda o endereco do Swagger
app = FastAPI(
    title="API com Swagger Customizado",
    docs_url="/documentacao",
    redoc_url="/leitura"
)


@app.get("/")
def root():
    """Rota principal."""
    return {"message": "API funcionando"}


@app.get("/products")
def list_products():
    """Lista produtos."""
    return [{"id": 1, "name": "Arroz"}]
```

Para testar:
```bash
# Execute a aplicacao
uvicorn ex10_custom:app --reload

# Swagger no endereco customizado
# Acesse: http://127.0.0.1:8000/documentacao

# ReDoc no endereco customizado
# Acesse: http://127.0.0.1:8000/leitura

# O endereco padrao /docs retorna 404
# Acesse: http://127.0.0.1:8000/docs -> Not Found
```


---

### Exercício 11 — Adicionar Rota de Saude (Health Check)

#### Enunciado

Crie uma rota GET em `/health` com tag "Sistema" que retorne o status da API e a contagem de produtos no banco. Use `database.py` para contar os produtos. Verifique no Swagger que a rota aparece na tag "Sistema".

#### Dicas

- Use `tags=["Sistema"]` para separar das rotas de produtos
- Conte os produtos com `len(database.get_all_products())`
- Retorne um dicionário com status e contagem

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** A rota deve retornar `{"status": "healthy", "products_count": N}`
- **Caso de borda:** Com banco vazio, `products_count` deve ser 0

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
import database

app = FastAPI(title="API com Health Check")
database.create_table()


# Rota de saude (health check) com tag "Sistema"
# "health" = saude, "check" = verificacao
# tags=["Sistema"] agrupa sob a tag "Sistema" no Swagger
@app.get("/health", tags=["Sistema"], summary="Verificar saude da API")
def health_check():
    """
    Verifica se a API esta funcionando corretamente.

    Retorna o status da API e a quantidade de produtos cadastrados.
    """
    # Contamos os produtos no banco
    products = database.get_all_products()
    # "healthy" = saudavel (funcionando)
    return {
        "status": "healthy",
        "products_count": len(products)
    }


# Rota de produtos com tag "Produtos"
@app.get("/products", tags=["Produtos"], summary="Listar produtos")
def list_products():
    """Lista todos os produtos."""
    return database.get_all_products()
```

Para testar:
```bash
curl http://127.0.0.1:8000/health
```

Saida esperada:
```json
{"status":"healthy","products_count":3}
```

---

### Exercício 12 — Documentar Códigos de Resposta

#### Enunciado

Crie uma rota GET `/products/{product_id}` que documente explicitamente os códigos de resposta possiveis: 200 (sucesso) e 404 (não encontrado). Use o parametro `responses` no decorador da rota.

#### Dicas

- Use `responses={404: {"description": "Produto nao encontrado"}}` no decorador
- O código 200 e documentado automaticamente pelo `response_model`
- No Swagger, os códigos aparecem na secao "Responses"

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** No Swagger, a secao "Responses" deve mostrar 200 e 404
- **Caso de borda:** Teste com ID inexistente — a resposta 404 deve corresponder a documentação

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API com Codigos de Resposta")

products = [
    {"id": 1, "name": "Arroz", "price": 8.99},
    {"id": 2, "name": "Sabao", "price": 4.50}
]


class ProductResponse(BaseModel):
    """Produto retornado pela API."""
    id: int
    name: str
    price: float


# Rota com documentacao explicita de codigos de resposta
# "responses" = respostas possiveis documentadas no Swagger
@app.get(
    "/products/{product_id}",
    response_model=ProductResponse,
    responses={
        200: {"description": "Produto encontrado com sucesso"},
        404: {"description": "Produto nao encontrado no banco de dados"}
    },
    summary="Buscar produto por ID"
)
def get_product(product_id: int):
    """
    Busca um produto pelo seu identificador unico.

    **Codigos de resposta:**
    - **200**: Produto encontrado e retornado
    - **404**: Nenhum produto com o ID informado
    """
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Produto nao encontrado")
```

Para testar:
```
1. Execute: uvicorn ex12_responses:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Clique em GET /products/{product_id}
4. Na secao "Responses", veja os codigos 200 e 404 documentados
```

---

### Exercício 13 — API Completa com Swagger Personalizado

#### Enunciado

Crie a versão final da API com todas as personalizacoes: título, descricao, versão, tags, summaries, response_models, Field com descricoes e exemplos, e códigos de resposta documentados. Use `database.py` para persistência.

#### Dicas

- Combine todas as técnicas dos exercícios anteriores
- Use tags para separar "Produtos" e "Sistema"
- Adicione `summary` em todas as rotas
- Use `Field` com descricoes e exemplos no modelo

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** O Swagger deve estar completo com todas as personalizacoes visiveis
- **Caso de borda:** Teste todas as operações CRUD pelo Swagger — todas devem funcionar

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import database

# Aplicacao com documentacao completa
app = FastAPI(
    title="API de Cadastro de Produtos",
    description=(
        "Sistema CRUD completo para gerenciamento de produtos. "
        "Armazenamento em SQLite com documentacao Swagger interativa."
    ),
    version="1.0.0"
)

# Inicializamos o banco
database.create_table()


# --- Modelos ---

class ProductCreate(BaseModel):
    """Dados para criar ou atualizar um produto."""
    name: str = Field(description="Nome do produto", example="Arroz Integral")
    price: float = Field(description="Preco em reais", example=12.50, ge=0)
    quantity: int = Field(description="Quantidade em estoque", example=30, ge=0)
    category: str = Field(description="Categoria", example="Alimentos")

    model_config = {
        "json_schema_extra": {
            "examples": [{"name": "Arroz Integral", "price": 12.50, "quantity": 30, "category": "Alimentos"}]
        }
    }


class ProductResponse(BaseModel):
    """Produto retornado pela API."""
    id: int = Field(description="ID unico")
    name: str = Field(description="Nome")
    price: float = Field(description="Preco")
    quantity: int = Field(description="Quantidade")
    category: str = Field(description="Categoria")


class MessageResponse(BaseModel):
    """Mensagem de confirmacao."""
    message: str = Field(description="Mensagem")


# --- Rotas de Produtos ---

@app.get("/products", response_model=list[ProductResponse], tags=["Produtos"],
         summary="Listar todos os produtos")
def list_products():
    """Retorna a lista completa de produtos cadastrados."""
    return database.get_all_products()


@app.get("/products/{product_id}", response_model=ProductResponse, tags=["Produtos"],
         summary="Buscar produto por ID",
         responses={404: {"description": "Produto nao encontrado"}})
def get_product(product_id: int):
    """Busca um produto pelo identificador unico."""
    product = database.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return product


@app.post("/products", response_model=ProductResponse, status_code=201,
          tags=["Produtos"], summary="Cadastrar novo produto")
def create_product(product: ProductCreate):
    """Cadastra um novo produto no sistema."""
    pid = database.insert_product(product.name, product.price, product.quantity, product.category)
    return {"id": pid, "name": product.name, "price": product.price,
            "quantity": product.quantity, "category": product.category}


@app.put("/products/{product_id}", response_model=ProductResponse, tags=["Produtos"],
         summary="Atualizar produto",
         responses={404: {"description": "Produto nao encontrado"}})
def update_product(product_id: int, product: ProductCreate):
    """Atualiza os dados de um produto existente."""
    updated = database.update_product(product_id, product.name, product.price, product.quantity, product.category)
    if not updated:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {"id": product_id, "name": product.name, "price": product.price,
            "quantity": product.quantity, "category": product.category}


@app.delete("/products/{product_id}", response_model=MessageResponse, tags=["Produtos"],
            summary="Excluir produto",
            responses={404: {"description": "Produto nao encontrado"}})
def delete_product(product_id: int):
    """Exclui um produto permanentemente."""
    deleted = database.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return {"message": f"Produto ID {product_id} excluido com sucesso"}


# --- Rotas de Sistema ---

@app.get("/health", tags=["Sistema"], summary="Verificar saude da API")
def health_check():
    """Retorna status da API e contagem de produtos."""
    products = database.get_all_products()
    return {"status": "healthy", "products_count": len(products)}
```

Para testar:
```
1. Execute: uvicorn ex13_complete:app --reload
2. Acesse: http://127.0.0.1:8000/docs
3. Verifique: titulo, descricao, tags, summaries, exemplos
4. Teste todas as operacoes CRUD pelo Swagger
```

---

### Exercício 14 — Comparar Swagger UI e ReDoc

#### Enunciado

Com a API completa rodando, acesse tanto o Swagger UI (`/docs`) quanto o ReDoc (`/redoc`). Compare as duas interfaces e liste 3 diferencas que você observou.

#### Dicas

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`
- Observe: interatividade, layout, organização, detalhes dos modelos

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Ambas as páginas devem abrir e mostrar a documentação da API
- **Caso de borda:** Tente usar "Try it out" no ReDoc — não existe (ReDoc e apenas leitura)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```
Comparacao entre Swagger UI e ReDoc:

1. INTERATIVIDADE:
   - Swagger UI: Tem botao "Try it out" para testar rotas diretamente
   - ReDoc: Apenas leitura — nao permite testar rotas

2. LAYOUT:
   - Swagger UI: Lista de rotas expandiveis, uma abaixo da outra
   - ReDoc: Menu lateral com navegacao, conteudo a direita

3. DETALHES DOS MODELOS:
   - Swagger UI: Mostra os modelos (schemas) no final da pagina
   - ReDoc: Mostra os modelos inline, junto com cada rota

4. USO RECOMENDADO:
   - Swagger UI: Para desenvolvimento e testes (interativo)
   - ReDoc: Para documentacao publica (mais bonito e legivel)
```

> Este exercício não tem código Python — e um exercício de observacao e comparação.

---

### Exercício 15 — Projeto Final: API Documentada Completa

#### Enunciado

Revise todo o projeto CRUD (arquivos `main.py`, `models.py`, `database.py`) e garanta que: (1) todas as rotas tem summary e docstring, (2) todos os modelos tem Field com descricao e exemplo, (3) as tags estão organizadas, (4) os códigos de resposta estão documentados. Execute a API e faca um teste completo pelo Swagger.

#### Dicas

- Revise cada arquivo verificando as personalizacoes
- Teste cada rota pelo Swagger na sequência: criar, listar, buscar, atualizar, excluir
- Verifique que os exemplos aparecem preenchidos ao clicar "Try it out"

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Todas as rotas devem ter documentação completa no Swagger
- **Caso de borda:** Feche o servidor, apague o `products.db`, reinicie e teste — o banco deve ser recriado automaticamente

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```
Checklist de revisao do projeto:

1. main.py:
   [x] FastAPI com title, description e version
   [x] Todas as rotas com tags
   [x] Todas as rotas com summary
   [x] Todas as rotas com docstring detalhada
   [x] Todas as rotas com response_model
   [x] Rotas de erro com responses={404: ...}
   [x] Rota de health check com tag "Sistema"

2. models.py:
   [x] ProductCreate com Field (description, example, ge=0)
   [x] ProductCreate com model_config e json_schema_extra
   [x] ProductResponse com Field (description)
   [x] MessageResponse para respostas de exclusao

3. database.py:
   [x] create_table() com CREATE TABLE IF NOT EXISTS
   [x] Todas as funcoes CRUD implementadas
   [x] Uso de placeholders (?) para seguranca
   [x] Uso de gerenciador de contexto (with)

4. Teste pelo Swagger:
   [x] POST /products — cadastrar com exemplo preenchido
   [x] GET /products — listar todos
   [x] GET /products/{id} — buscar existente e inexistente
   [x] PUT /products/{id} — atualizar existente
   [x] DELETE /products/{id} — excluir existente
   [x] GET /health — verificar status
```

> Este exercício e uma revisao prática do projeto completo. Use o checklist acima para verificar cada item.