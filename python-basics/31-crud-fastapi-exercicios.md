# 31 — Exercícios: CRUD com FastAPI

[<- Voltar para o módulo](31-crud-fastapi.md) | [Glossário](00-glossário.md)

---

> **Antes de começar:** Estes exercícios constroem progressivamente uma API HTTP com FastAPI. Certifique-se de que o FastAPI e o Uvicorn estão instalados no ambiente virtual. Para testar as rotas, use curl em outro terminal ou o navegador. Tente resolver cada exercício sozinho antes de consultar a resposta.

> **Como testar:** Apos criar cada arquivo, execute com `uvicorn nome_arquivo:app --reload` e teste com curl ou navegador em outro terminal.

---

### Exercício 1 — Primeira Rota GET

#### Enunciado

Crie um arquivo `ex01_hello.py` com uma aplicação FastAPI que tenha uma única rota GET em `/` que retorne a mensagem `{"message": "Bem-vindo a API de Produtos"}`.

#### Dicas

- Importe `FastAPI` de `fastapi`
- Crie a aplicação com `app = FastAPI()`
- Use `@app.get("/")` para definir a rota
- Execute com `uvicorn ex01_hello:app --reload`

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Acesse `http://127.0.0.1:8000/` no navegador — deve exibir o JSON com a mensagem
- **Caso de borda:** Acesse `http://127.0.0.1:8000/inexistente` — deve retornar erro 404

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos o FastAPI para criar a aplicacao
# "FastAPI" = framework para criar APIs HTTP
from fastapi import FastAPI

# Criamos a aplicacao FastAPI
# "app" = aplicacao
app = FastAPI()


# Definimos uma rota GET na raiz "/"
# @app.get("/") = quando alguem acessar GET /, execute esta funcao
# "root" = raiz (pagina inicial)
@app.get("/")
def root():
    """Retorna mensagem de boas-vindas."""
    # Retornamos um dicionario — o FastAPI converte para JSON
    # "message" = mensagem
    return {"message": "Bem-vindo a API de Produtos"}
```

Para executar:
```bash
uvicorn ex01_hello:app --reload
```

Para testar:
```bash
curl http://127.0.0.1:8000/
```

Saida esperada:
```json
{"message":"Bem-vindo a API de Produtos"}
```

---

### Exercício 2 — Rota GET com Lista Fixa

#### Enunciado

Crie um arquivo `ex02_list.py` com uma rota GET em `/products` que retorne uma lista fixa de 3 produtos em formato JSON. Cada produto deve ter id, name, price, quantity e category.

#### Dicas

- Crie uma lista de dicionários com os produtos
- A rota deve retornar essa lista
- O FastAPI converte automaticamente para JSON

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Acesse `/products` — deve retornar um array JSON com 3 produtos
- **Caso de borda:** Verifique que os campos estão corretos (id, name, price, quantity, category)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos o FastAPI
from fastapi import FastAPI

# Criamos a aplicacao
app = FastAPI()

# Lista fixa de produtos para teste
# "sample_products" = produtos de exemplo
sample_products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Rota GET para listar produtos
# @app.get("/products") = rota GET no endereco /products
@app.get("/products")
def list_products():
    """Retorna a lista de produtos."""
    # Retornamos a lista — o FastAPI converte para JSON
    return sample_products
```

Para testar:
```bash
curl http://127.0.0.1:8000/products
```

Saida esperada:
```json
[{"id":1,"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"},{"id":2,"name":"Sabao","price":4.5,"quantity":80,"category":"Limpeza"},{"id":3,"name":"Shampoo","price":12.75,"quantity":25,"category":"Higiene"}]
```


---

### Exercício 3 — Rota GET com Parametro de Caminho

#### Enunciado

Crie uma rota GET em `/products/{product_id}` que receba o ID como parametro e retorne o produto correspondente da lista fixa. Se o ID não existir, retorne erro 404.

#### Dicas

- Use `{product_id}` na rota e `product_id: int` no parametro da função
- Percorra a lista para encontrar o produto com o ID informado
- Use `HTTPException(status_code=404)` para retornar erro

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Acesse `/products/1` — deve retornar o produto com ID 1
- **Caso de borda:** Acesse `/products/99` — deve retornar erro 404

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos FastAPI e HTTPException
# "HTTPException" = excecao HTTP (para retornar erros)
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Lista fixa de produtos
sample_products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Rota GET com parametro de caminho
# {product_id} na rota = parametro extraido da URL
# product_id: int = o FastAPI converte automaticamente para inteiro
@app.get("/products/{product_id}")
def get_product(product_id: int):
    """Retorna um produto pelo ID."""
    # Percorremos a lista para encontrar o produto
    for product in sample_products:
        if product["id"] == product_id:
            # Encontramos — retornamos o produto
            return product
    # Se nao encontrou, retornamos erro 404
    # "raise" = levantar/lancar (uma excecao)
    # status_code=404 = Not Found (nao encontrado)
    # "detail" = detalhe (mensagem de erro)
    raise HTTPException(status_code=404, detail="Produto nao encontrado")
```

Para testar:
```bash
curl http://127.0.0.1:8000/products/1
curl http://127.0.0.1:8000/products/99
```

Saida esperada (ID 1):
```json
{"id":1,"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}
```

Saida esperada (ID 99):
```json
{"detail":"Produto nao encontrado"}
```

---

### Exercício 4 — Modelo Pydantic para Produto

#### Enunciado

Crie um modelo Pydantic `ProductCreate` com os campos name (str), price (float), quantity (int) e category (str). Crie uma rota POST em `/products` que receba dados no formato do modelo e retorne os dados recebidos com um ID fixo (1).

#### Dicas

- Importe `BaseModel` de `pydantic`
- Defina a classe com os campos e tipos
- Na rota POST, use `product: ProductCreate` como parametro

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Envie um POST com dados validos — deve retornar os dados com ID 1
- **Caso de borda:** Envie um POST com preco como texto — deve retornar erro 422

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
# Importamos BaseModel do Pydantic para criar modelos
# "BaseModel" = modelo base para validacao de dados
from pydantic import BaseModel

app = FastAPI()


# Modelo Pydantic para criar produto
# "Product" = produto, "Create" = criar
class ProductCreate(BaseModel):
    """Modelo de dados para criar um produto."""
    name: str           # Nome — texto obrigatorio (name = nome)
    price: float        # Preco — decimal obrigatorio (price = preco)
    quantity: int       # Quantidade — inteiro obrigatorio (quantity = quantidade)
    category: str       # Categoria — texto obrigatorio (category = categoria)


# Rota POST para criar produto
# @app.post("/products") = rota POST no endereco /products
# status_code=201 = Created (recurso criado)
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """Recebe dados de um produto e retorna com ID fixo."""
    # product.name, product.price, etc. acessam os campos validados
    # Retornamos os dados com um ID fixo para teste
    return {
        "id": 1,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }
```

Para testar:
```bash
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Cafe", "price": 15.90, "quantity": 20, "category": "Alimentos"}'
```

Saida esperada:
```json
{"id":1,"name":"Cafe","price":15.9,"quantity":20,"category":"Alimentos"}
```

---

### Exercício 5 — Rota POST com Banco de Dados

#### Enunciado

Crie uma rota POST em `/products` que insira o produto no banco de dados SQLite e retorne o produto com o ID gerado. Use o módulo `database.py` do módulo principal.

#### Dicas

- Importe as funções de `database.py`
- Chame `database.create_table()` ao iniciar
- Use `database.insert_product()` na rota POST
- Retorne o produto com o ID gerado por `lastrowid`

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Envie um POST — o produto deve ser inserido e retornado com ID gerado
- **Caso de borda:** Envie dois POSTs — os IDs devem ser sequenciais

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
from pydantic import BaseModel
# Importamos nosso modulo de banco de dados
import database

app = FastAPI()

# Criamos a tabela ao iniciar
database.create_table()


class ProductCreate(BaseModel):
    """Modelo para criar produto."""
    name: str
    price: float
    quantity: int
    category: str


# Rota POST que insere no banco de dados
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """Cadastra um produto no banco e retorna com ID."""
    # Inserimos no banco usando as funcoes do database.py
    # insert_product retorna o ID gerado
    product_id = database.insert_product(
        product.name,
        product.price,
        product.quantity,
        product.category
    )
    # Retornamos o produto com o ID gerado
    return {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }
```

Para testar:
```bash
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Leite", "price": 5.99, "quantity": 100, "category": "Alimentos"}'
```

Saida esperada:
```json
{"id":1,"name":"Leite","price":5.99,"quantity":100,"category":"Alimentos"}
```

---

### Exercício 6 — Rota GET Listando do Banco

#### Enunciado

Crie uma rota GET em `/products` que liste todos os produtos do banco de dados SQLite. Use `database.get_all_products()`.

#### Dicas

- A função `get_all_products()` retorna uma lista de dicionários
- O FastAPI converte automaticamente para JSON
- Se a lista estiver vazia, retorne uma lista vazia `[]`

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Apos cadastrar produtos, a rota deve retornar a lista completa
- **Caso de borda:** Com banco vazio, deve retornar `[]`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
import database

app = FastAPI()
database.create_table()


# Rota GET para listar todos os produtos do banco
@app.get("/products")
def list_products():
    """Retorna todos os produtos do banco de dados."""
    # Buscamos todos os produtos
    # get_all_products() retorna lista de dicionarios
    products = database.get_all_products()
    # Retornamos a lista (pode estar vazia)
    return products
```

Para testar:
```bash
curl http://127.0.0.1:8000/products
```

Saida esperada (com produtos cadastrados):
```json
[{"id":1,"name":"Leite","price":5.99,"quantity":100,"category":"Alimentos"}]
```

---

### Exercício 7 — Rota GET por ID com Banco

#### Enunciado

Crie uma rota GET em `/products/{product_id}` que busque o produto no banco de dados. Se não encontrar, retorne erro 404.

#### Dicas

- Use `database.get_product_by_id(product_id)` para buscar
- Se retornar None, lance HTTPException com status 404
- O parametro `product_id: int` e convertido automaticamente

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Buscar um ID existente deve retornar o produto
- **Caso de borda:** Buscar ID 999 deve retornar erro 404

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
import database

app = FastAPI()
database.create_table()


# Rota GET com parametro de caminho para buscar por ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    """Busca um produto pelo ID no banco."""
    # Buscamos no banco
    product = database.get_product_by_id(product_id)
    # Se nao encontrou, retornamos 404
    if product is None:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    # Retornamos o produto encontrado
    return product
```

Para testar:
```bash
curl http://127.0.0.1:8000/products/1
curl http://127.0.0.1:8000/products/999
```

Saida esperada (ID existente):
```json
{"id":1,"name":"Leite","price":5.99,"quantity":100,"category":"Alimentos"}
```

Saida esperada (ID inexistente):
```json
{"detail":"Produto nao encontrado"}
```

---

### Exercício 8 — Rota PUT para Atualizar

#### Enunciado

Crie uma rota PUT em `/products/{product_id}` que atualize os dados de um produto no banco. Se o produto não existir, retorne erro 404.

#### Dicas

- Use `database.update_product()` que retorna True/False
- Se retornar False, o produto não foi encontrado
- Retorne o produto atualizado com o ID

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Atualizar um produto existente deve retornar os novos dados
- **Caso de borda:** Atualizar ID inexistente deve retornar 404

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

app = FastAPI()
database.create_table()


class ProductCreate(BaseModel):
    """Modelo para dados do produto."""
    name: str
    price: float
    quantity: int
    category: str


# Rota PUT para atualizar produto
# @app.put() = rota que responde ao metodo PUT (atualizar)
@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate):
    """Atualiza os dados de um produto."""
    # Tentamos atualizar no banco
    # update_product retorna True se atualizou, False se nao encontrou
    updated = database.update_product(
        product_id,
        product.name,
        product.price,
        product.quantity,
        product.category
    )
    # Se nao encontrou, retornamos 404
    if not updated:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    # Retornamos o produto atualizado
    return {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }
```

Para testar:
```bash
curl -X PUT http://127.0.0.1:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Leite Integral", "price": 6.99, "quantity": 80, "category": "Alimentos"}'
```

Saida esperada:
```json
{"id":1,"name":"Leite Integral","price":6.99,"quantity":80,"category":"Alimentos"}
```

---

### Exercício 9 — Rota DELETE para Excluir

#### Enunciado

Crie uma rota DELETE em `/products/{product_id}` que exclua um produto do banco. Se o produto não existir, retorne erro 404. Retorne uma mensagem de sucesso.

#### Dicas

- Use `database.delete_product()` que retorna True/False
- Se retornar False, o produto não foi encontrado
- Retorne um dicionário com a mensagem de sucesso

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Excluir um produto existente deve retornar mensagem de sucesso
- **Caso de borda:** Excluir ID inexistente deve retornar 404

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
import database

app = FastAPI()
database.create_table()


# Rota DELETE para excluir produto
# @app.delete() = rota que responde ao metodo DELETE (excluir)
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Exclui um produto pelo ID."""
    # Tentamos excluir do banco
    # delete_product retorna True se excluiu, False se nao encontrou
    deleted = database.delete_product(product_id)
    # Se nao encontrou, retornamos 404
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    # Retornamos mensagem de sucesso
    return {"message": f"Produto ID {product_id} excluido com sucesso"}
```

Para testar:
```bash
curl -X DELETE http://127.0.0.1:8000/products/1
```

Saida esperada:
```json
{"message":"Produto ID 1 excluido com sucesso"}
```


---

### Exercício 10 — API Completa com Todas as Rotas

#### Enunciado

Crie uma API completa com todas as 5 rotas CRUD (listar, buscar, criar, atualizar, excluir) em um único arquivo. Use os modelos Pydantic e o módulo database.py. Teste todas as operações com curl.

#### Dicas

- Combine as rotas dos exercícios 5 a 9 em um único arquivo
- Chame `database.create_table()` ao iniciar
- Use `response_model` para definir o formato das respostas

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Cadastre 2 produtos (POST), liste (GET), busque por ID (GET), atualize (PUT), exclua (DELETE), liste novamente
- **Caso de borda:** Feche o servidor, reinicie e liste — os dados devem persistir

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import database

# Criamos a aplicacao
app = FastAPI(title="CRUD Produtos")

# Criamos a tabela ao iniciar
database.create_table()


# Modelo Pydantic
class ProductCreate(BaseModel):
    """Modelo para criar/atualizar produto."""
    name: str       # Nome (name = nome)
    price: float    # Preco (price = preco)
    quantity: int   # Quantidade (quantity = quantidade)
    category: str   # Categoria (category = categoria)


# Rota: listar todos
@app.get("/products")
def list_products():
    """Lista todos os produtos."""
    return database.get_all_products()


# Rota: buscar por ID
@app.get("/products/{product_id}")
def get_product(product_id: int):
    """Busca produto por ID."""
    product = database.get_product_by_id(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Nao encontrado")
    return product


# Rota: criar produto
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """Cadastra novo produto."""
    pid = database.insert_product(product.name, product.price, product.quantity, product.category)
    return {"id": pid, "name": product.name, "price": product.price, "quantity": product.quantity, "category": product.category}


# Rota: atualizar produto
@app.put("/products/{product_id}")
def update_product(product_id: int, product: ProductCreate):
    """Atualiza produto existente."""
    updated = database.update_product(product_id, product.name, product.price, product.quantity, product.category)
    if not updated:
        raise HTTPException(status_code=404, detail="Nao encontrado")
    return {"id": product_id, "name": product.name, "price": product.price, "quantity": product.quantity, "category": product.category}


# Rota: excluir produto
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Exclui produto."""
    deleted = database.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Nao encontrado")
    return {"message": f"Produto ID {product_id} excluido"}
```

Para testar todas as operações:
```bash
# Cadastrar
curl -X POST http://127.0.0.1:8000/products -H "Content-Type: application/json" -d '{"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}'

# Listar
curl http://127.0.0.1:8000/products

# Buscar
curl http://127.0.0.1:8000/products/1

# Atualizar
curl -X PUT http://127.0.0.1:8000/products/1 -H "Content-Type: application/json" -d '{"name":"Arroz Integral","price":12.50,"quantity":30,"category":"Alimentos"}'

# Excluir
curl -X DELETE http://127.0.0.1:8000/products/1
```

---

### Exercício 11 — Rota GET com Filtro por Categoria

#### Enunciado

Adicione um parametro de consulta (query parameter) opcional `category` a rota GET `/products`. Se informado, retorne apenas os produtos daquela categoria. Se não informado, retorne todos.

#### Dicas

- Use `category: str = None` como parametro da função (valor padrão None)
- Se `category` for None, retorne todos os produtos
- Se `category` tiver valor, filtre os resultados

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** `/products?category=Alimentos` deve retornar apenas produtos de Alimentos
- **Caso de borda:** `/products` sem parametro deve retornar todos os produtos

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
import database

app = FastAPI()
database.create_table()


# Rota GET com parametro de consulta opcional
# category: str = None — parametro opcional (query parameter)
# Se o cliente acessar /products?category=Alimentos, category = "Alimentos"
# Se acessar /products sem parametro, category = None
@app.get("/products")
def list_products(category: str = None):
    """Lista produtos, opcionalmente filtrados por categoria."""
    # Buscamos todos os produtos
    products = database.get_all_products()
    # Se a categoria foi informada, filtramos
    if category is not None:
        # Filtramos os produtos pela categoria
        # "filtered" = filtrados
        filtered = []
        for product in products:
            # Comparamos ignorando maiusculas/minusculas
            if product["category"].lower() == category.lower():
                filtered.append(product)
        return filtered
    # Se nao foi informada, retornamos todos
    return products
```

Para testar:
```bash
# Todos os produtos
curl http://127.0.0.1:8000/products

# Filtrar por categoria
curl "http://127.0.0.1:8000/products?category=Alimentos"
```

Saida esperada (filtrado):
```json
[{"id":1,"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}]
```

---

### Exercício 12 — Validação Customizada com Pydantic

#### Enunciado

Melhore o modelo `ProductCreate` adicionando validacoes: preco deve ser >= 0, quantidade deve ser >= 0, nome não pode ser vazio. Use `field_validator` do Pydantic.

#### Dicas

- Importe `field_validator` de `pydantic`
- Crie métodos com `@field_validator("campo")` dentro da classe
- Lance `ValueError` se a validação falhar

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Enviar dados validos deve funcionar normalmente
- **Caso de borda:** Enviar preco negativo deve retornar erro 422 com mensagem explicativa

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI
# Importamos field_validator para validacoes customizadas
from pydantic import BaseModel, field_validator

app = FastAPI()


# Modelo com validacoes customizadas
class ProductCreate(BaseModel):
    """Modelo com validacao de dados."""
    name: str
    price: float
    quantity: int
    category: str

    # Validacao do nome: nao pode ser vazio
    # @field_validator("name") = validar o campo "name"
    @field_validator("name")
    @classmethod
    def name_not_empty(cls, value):
        """Valida que o nome nao esta vazio."""
        # strip() remove espacos em branco
        if not value or value.strip() == "":
            # ValueError = erro de valor (dado invalido)
            raise ValueError("Nome nao pode ser vazio")
        return value.strip()

    # Validacao do preco: deve ser >= 0
    @field_validator("price")
    @classmethod
    def price_not_negative(cls, value):
        """Valida que o preco nao e negativo."""
        if value < 0:
            raise ValueError("Preco nao pode ser negativo")
        return value

    # Validacao da quantidade: deve ser >= 0
    @field_validator("quantity")
    @classmethod
    def quantity_not_negative(cls, value):
        """Valida que a quantidade nao e negativa."""
        if value < 0:
            raise ValueError("Quantidade nao pode ser negativa")
        return value

    # Validacao da categoria: nao pode ser vazia
    @field_validator("category")
    @classmethod
    def category_not_empty(cls, value):
        """Valida que a categoria nao esta vazia."""
        if not value or value.strip() == "":
            raise ValueError("Categoria nao pode ser vazia")
        return value.strip()


# Rota POST para testar a validacao
@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    """Cadastra produto com validacao."""
    return {"message": "Produto valido", "name": product.name, "price": product.price}
```

Para testar:
```bash
# Dados validos
curl -X POST http://127.0.0.1:8000/products -H "Content-Type: application/json" -d '{"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}'

# Preco negativo (deve dar erro)
curl -X POST http://127.0.0.1:8000/products -H "Content-Type: application/json" -d '{"name":"Teste","price":-5,"quantity":10,"category":"Teste"}'
```

Saida esperada (preco negativo):
```json
{"detail":[{"type":"value_error","loc":["body","price"],"msg":"Value error, Preco nao pode ser negativo"}]}
```

---

### Exercício 13 — Rota de Contagem de Produtos

#### Enunciado

Crie uma rota GET em `/products/count` que retorne a quantidade total de produtos cadastrados e a quantidade por categoria. Use SQL com `COUNT(*)` e `GROUP BY`.

#### Dicas

- Crie uma função no `database.py` que execute o SQL de contagem
- A rota deve retornar um dicionário com total e contagem por categoria
- Cuidado com a ordem das rotas: `/products/count` deve vir antes de `/products/{product_id}`

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Com 3 produtos em 2 categorias, deve mostrar total 3 e a contagem por categoria
- **Caso de borda:** Com banco vazio, total deve ser 0

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3
from fastapi import FastAPI

app = FastAPI()

DATABASE_FILE = "products.db"


# Funcao que conta produtos por categoria
def count_products():
    """Retorna total e contagem por categoria."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        # Total geral
        cursor.execute("SELECT COUNT(*) FROM products")
        total = cursor.fetchone()[0]
        # Contagem por categoria
        cursor.execute("SELECT category, COUNT(*) FROM products GROUP BY category")
        categories = cursor.fetchall()
    # Montamos o resultado
    # "by_category" = por categoria
    by_category = {}
    for cat, count in categories:
        by_category[cat] = count
    return {"total": total, "by_category": by_category}


# IMPORTANTE: esta rota deve vir ANTES de /products/{product_id}
# Senao o FastAPI interpreta "count" como um product_id
@app.get("/products/count")
def get_count():
    """Retorna contagem de produtos."""
    return count_products()
```

Para testar:
```bash
curl http://127.0.0.1:8000/products/count
```

Saida esperada:
```json
{"total":3,"by_category":{"Alimentos":2,"Limpeza":1}}
```

---

### Exercício 14 — Rota de Busca por Nome

#### Enunciado

Crie uma rota GET em `/products/search` que receba um parametro de consulta `q` (texto de busca) e retorne os produtos cujo nome contenha esse texto. Use `SELECT * FROM products WHERE name LIKE ?`.

#### Dicas

- Use `LIKE '%texto%'` para busca parcial no SQL
- O `%` e um coringa que significa "qualquer coisa"
- Passe o valor como `f"%{q}%"` no placeholder

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** `/products/search?q=arroz` deve encontrar produtos com "arroz" no nome
- **Caso de borda:** `/products/search?q=xyz` deve retornar lista vazia

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3
from fastapi import FastAPI

app = FastAPI()

DATABASE_FILE = "products.db"


# Funcao que busca produtos por nome
def search_products(search_text):
    """Busca produtos cujo nome contenha o texto."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        # LIKE '%texto%' busca o texto em qualquer posicao do nome
        # % = coringa (qualquer coisa antes e depois)
        cursor.execute(
            "SELECT * FROM products WHERE name LIKE ?",
            (f"%{search_text}%",)
        )
        rows = cursor.fetchall()
    # Convertemos para lista de dicionarios
    products = []
    for row in rows:
        products.append({
            "id": row[0], "name": row[1], "price": row[2],
            "quantity": row[3], "category": row[4]
        })
    return products


# Rota de busca por nome
# q: str = parametro de consulta obrigatorio
@app.get("/products/search")
def search(q: str):
    """Busca produtos pelo nome."""
    # Chamamos a funcao de busca
    results = search_products(q)
    return results
```

Para testar:
```bash
curl "http://127.0.0.1:8000/products/search?q=arroz"
```

Saida esperada:
```json
[{"id":1,"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}]
```

---

### Exercício 15 — Tratamento de Erros Global

#### Enunciado

Adicione tratamento de erros global a API usando `@app.exception_handler`. Capture erros genericos e retorne uma resposta JSON padronizada com código 500 e mensagem amigavel.

#### Dicas

- Use `@app.exception_handler(Exception)` para capturar erros genericos
- Retorne um `JSONResponse` com status 500
- Importe `JSONResponse` de `fastapi.responses`

#### Proposta de Teste

Execute e verifique:
- **Caso básico:** Operações normais devem funcionar sem alteração
- **Caso de borda:** Se ocorrer um erro interno, a API deve retornar JSON com mensagem amigavel em vez de travar

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
from fastapi import FastAPI, Request
# Importamos JSONResponse para respostas customizadas
# "JSONResponse" = resposta em formato JSON
from fastapi.responses import JSONResponse

app = FastAPI()


# Tratamento de erros global
# @app.exception_handler(Exception) = capturar qualquer excecao
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, error: Exception):
    """Captura erros nao tratados e retorna resposta padronizada."""
    # Retornamos uma resposta JSON com codigo 500
    # status_code=500 = Internal Server Error (erro interno do servidor)
    return JSONResponse(
        status_code=500,
        content={
            "error": "Erro interno do servidor",
            "detail": str(error)
        }
    )


# Rota normal
@app.get("/")
def root():
    """Rota de teste."""
    return {"message": "API funcionando"}


# Rota que simula um erro
@app.get("/error")
def simulate_error():
    """Simula um erro para testar o tratamento global."""
    # Forcamos um erro dividindo por zero
    result = 1 / 0
    return {"result": result}
```

Para testar:
```bash
# Rota normal
curl http://127.0.0.1:8000/

# Rota com erro
curl http://127.0.0.1:8000/error
```

Saida esperada (rota com erro):
```json
{"error":"Erro interno do servidor","detail":"division by zero"}
```