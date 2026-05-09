# 31 — CRUD com FastAPI: Interface HTTP para o Cadastro de Produtos

[<- Anterior: CRUD com SQLite](30-crud-sqlite.md) | [Glossário](00-glossário.md) | [Próximo: CRUD com Swagger ->](32-crud-swagger.md)

---

## Introdução

Nos módulos anteriores, você construiu um sistema CRUD que funciona pelo terminal: o usuario digita opcoes em um menu e ve os resultados na tela. Isso funciona bem para uso pessoal, mas e se você quiser que **outras pessoas** ou **outros programas** acessem o seu sistema de produtos? E se você quiser acessar de um celular, de um navegador ou de outro computador?

Para isso, precisamos transformar nosso programa em uma **API HTTP** — uma interface que permite que qualquer programa se comunique com o nosso sistema através da internet (ou rede local).

### O Que e uma API HTTP?

Imagine um **restaurante**. Você (o cliente) não vai ate a cozinha preparar sua comida. Em vez disso, você faz um **pedido** ao garcom, que leva o pedido ate a cozinha. A cozinha prepara o prato e o garcom traz de volta para você.

Uma API HTTP funciona da mesma forma:

- **Você (cliente):** Um navegador, aplicativo ou outro programa
- **O garcom (API):** Recebe pedidos e entrega respostas
- **A cozinha (servidor):** Processa os pedidos e prepara os dados

Os "pedidos" sao feitos usando **métodos HTTP**:

| Método HTTP | O Que Faz | Equivalente CRUD |
|-------------|-----------|-----------------|
| GET | Buscar/consultar dados | Read (Ler) |
| POST | Enviar/criar dados | Create (Criar) |
| PUT | Atualizar dados existentes | Update (Atualizar) |
| DELETE | Remover dados | Delete (Excluir) |

### O Que e FastAPI?

**FastAPI** e um framework Python para criar APIs HTTP de forma rapida e simples. Ele foi escolhido para este curso porque:

- E fácil de aprender e usar
- Gera documentação automática (Swagger — você vera no módulo 32)
- Válida os dados automaticamente
- E muito popular no mercado de trabalho

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Preparacao do Ambiente

Antes de começar, precisamos instalar o FastAPI e o Uvicorn (o servidor que roda a aplicação).

### Passo 1: Criar e Ativar o Ambiente Virtual

```bash
# Navegamos ate a pasta do projeto
# "cd" = change directory (mudar de diretorio)
cd ~/meus-projetos/crud-produtos

# Criamos o ambiente virtual (se ainda nao existir)
# "python3 -m venv venv" = criar ambiente virtual na pasta venv
python3 -m venv venv

# Ativamos o ambiente virtual
# "source" = executar script no terminal atual
# "activate" = ativar
source venv/bin/activate
```

> Apos ativar, você vera `(venv)` no inicio da linha do terminal. Isso confirma que o ambiente virtual esta ativo.

### Passo 2: Instalar FastAPI e Uvicorn

```bash
# Instalamos o FastAPI e o Uvicorn
# "pip3 install" = instalar pacote
# "fastapi" = framework para criar APIs
# "uvicorn" = servidor ASGI para rodar a aplicacao
pip3 install fastapi uvicorn
```

Saida esperada:
```
Successfully installed fastapi-0.110.0 uvicorn-0.27.0 ...
```

### Passo 3: Gerar o requirements.txt

```bash
# Geramos o arquivo de dependencias
# "freeze" = congelar (registrar estado atual)
pip3 freeze > requirements.txt
```

### Passo 4: Verificar a Instalacao

```bash
# Verificamos que o FastAPI foi instalado
pip3 show fastapi
```

Saida esperada:
```
Name: fastapi
Version: 0.110.0
...
```

---

## Conceitos Básicos de APIs HTTP

### Rotas (Endpoints)

Uma **rota** (route) ou **endpoint** e um endereco que o cliente acessa para realizar uma operação. No nosso caso:

| Rota | Método | O Que Faz |
|------|--------|-----------|
| `/products` | GET | Lista todos os produtos |
| `/products/{id}` | GET | Busca um produto pelo ID |
| `/products` | POST | Cadastra um novo produto |
| `/products/{id}` | PUT | Atualiza um produto |
| `/products/{id}` | DELETE | Exclui um produto |

### JSON

As APIs HTTP trocam dados no formato **JSON** (JavaScript Object Notation). Você ja aprendeu JSON no módulo 21. Um produto em JSON fica assim:

```json
{
    "id": 1,
    "name": "Arroz",
    "price": 8.99,
    "quantity": 50,
    "category": "Alimentos"
}
```

### Códigos de Status HTTP

Cada resposta da API vem com um **código de status** que indica se a operação deu certo:

| Código | Significado | Quando Usar |
|--------|-------------|-------------|
| 200 | OK | Operação bem-sucedida |
| 201 | Created | Registro criado com sucesso |
| 404 | Not Found | Registro não encontrado |
| 422 | Unprocessable Entity | Dados invalidos |

---

## Construindo a API Passo a Passo


### Passo 1: Modelo de Dados com Pydantic

O FastAPI usa **Pydantic** para definir e validar os dados. Pydantic e uma biblioteca que vem junto com o FastAPI.

Crie o arquivo `models.py`:

```python
# Arquivo: models.py
# Modelos de dados para a API de produtos
# "models" = modelos

# Importamos BaseModel do Pydantic para criar modelos de dados
# "BaseModel" = modelo base (classe que valida dados automaticamente)
from pydantic import BaseModel


# Modelo para criar um novo produto (sem ID — o banco gera)
# "Product" = produto, "Create" = criar
class ProductCreate(BaseModel):
    """Modelo de dados para criar um produto."""
    name: str           # Nome do produto (name = nome) — texto obrigatorio
    price: float        # Preco do produto (price = preco) — decimal obrigatorio
    quantity: int       # Quantidade em estoque (quantity = quantidade) — inteiro obrigatorio
    category: str       # Categoria do produto (category = categoria) — texto obrigatorio


# Modelo para a resposta (com ID — retornado pelo banco)
# "Product" = produto, "Response" = resposta
class ProductResponse(BaseModel):
    """Modelo de dados para a resposta com produto."""
    id: int             # Identificador unico (id = identificador)
    name: str           # Nome do produto
    price: float        # Preco do produto
    quantity: int       # Quantidade em estoque
    category: str       # Categoria do produto
```

**Por que dois modelos?**

- `ProductCreate`: Usado quando o cliente **envia** dados para criar um produto. Não tem `id` porque o banco gera automaticamente.
- `ProductResponse`: Usado quando a API **retorna** dados. Tem `id` porque o produto ja foi salvo no banco.

### Passo 2: Funções de Banco de Dados

Crie o arquivo `database.py`:

```python
# Arquivo: database.py
# Funcoes de acesso ao banco de dados SQLite
# "database" = banco de dados

# Importamos o modulo sqlite3
import sqlite3

# Nome do arquivo do banco de dados
# "DATABASE_FILE" = arquivo do banco de dados
DATABASE_FILE = "products.db"


def create_table():
    """Cria a tabela products se nao existir."""
    # Abrimos a conexao com gerenciador de contexto
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        # Criamos a tabela com os campos necessarios
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        """)


def insert_product(name, price, quantity, category):
    """Insere um produto e retorna o ID gerado."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
            (name, price, quantity, category)
        )
        # Retornamos o ID gerado pelo banco
        return cursor.lastrowid


def get_all_products():
    """Retorna todos os produtos como lista de dicionarios."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
    # Convertemos tuplas para dicionarios
    # "products" = produtos
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "quantity": row[3],
            "category": row[4]
        })
    return products


def get_product_by_id(product_id):
    """Busca um produto pelo ID. Retorna dicionario ou None."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
    if row is None:
        return None
    return {
        "id": row[0],
        "name": row[1],
        "price": row[2],
        "quantity": row[3],
        "category": row[4]
    }


def update_product(product_id, name, price, quantity, category):
    """Atualiza um produto. Retorna True se atualizou, False se nao encontrou."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE products SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?",
            (name, price, quantity, category, product_id)
        )
        return cursor.rowcount > 0


def delete_product(product_id):
    """Exclui um produto. Retorna True se excluiu, False se nao encontrou."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        return cursor.rowcount > 0
```

### Passo 3: Rotas da API

Crie o arquivo `main.py`:

```python
# Arquivo: main.py
# Aplicacao FastAPI — API HTTP para o CRUD de produtos
# "main" = principal

# Importamos o FastAPI para criar a aplicacao
# "FastAPI" = framework para criar APIs
from fastapi import FastAPI, HTTPException

# Importamos nossos modulos
# "database" = funcoes de banco de dados
# "models" = modelos de dados
import database
from models import ProductCreate, ProductResponse

# Criamos a aplicacao FastAPI
# "app" = aplicacao
app = FastAPI(title="CRUD de Produtos", description="API para cadastro de produtos")

# Criamos a tabela ao iniciar a aplicacao
# Isso garante que a tabela existe antes de qualquer operacao
database.create_table()


# --- Rota: Listar todos os produtos ---
# @app.get() define uma rota que responde ao metodo GET
# "/products" e o endereco da rota
@app.get("/products", response_model=list[ProductResponse])
def list_products():
    """Retorna todos os produtos cadastrados."""
    # Buscamos todos os produtos no banco
    # "products" = produtos
    products = database.get_all_products()
    # Retornamos a lista (FastAPI converte para JSON automaticamente)
    return products


# --- Rota: Buscar produto por ID ---
# {product_id} e um parametro de caminho (path parameter)
@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    """Retorna um produto pelo ID."""
    # Buscamos o produto no banco
    product = database.get_product_by_id(product_id)
    # Se nao encontrou, retornamos erro 404
    if product is None:
        # HTTPException gera uma resposta de erro
        # status_code=404 = Not Found (nao encontrado)
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    return product


# --- Rota: Cadastrar novo produto ---
# @app.post() define uma rota que responde ao metodo POST
# status_code=201 indica que um recurso foi criado
@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate):
    """Cadastra um novo produto."""
    # Inserimos no banco usando os dados do modelo Pydantic
    # product.name acessa o campo name do modelo
    product_id = database.insert_product(
        product.name,
        product.price,
        product.quantity,
        product.category
    )
    # Retornamos o produto criado com o ID gerado
    return {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }


# --- Rota: Atualizar produto ---
# @app.put() define uma rota que responde ao metodo PUT
@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductCreate):
    """Atualiza os dados de um produto."""
    # Tentamos atualizar no banco
    # "updated" = atualizado (True ou False)
    updated = database.update_product(
        product_id,
        product.name,
        product.price,
        product.quantity,
        product.category
    )
    # Se nao encontrou, retornamos erro 404
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


# --- Rota: Excluir produto ---
# @app.delete() define uma rota que responde ao metodo DELETE
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Exclui um produto pelo ID."""
    # Tentamos excluir do banco
    # "deleted" = excluido (True ou False)
    deleted = database.delete_product(product_id)
    # Se nao encontrou, retornamos erro 404
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto nao encontrado")
    # Retornamos mensagem de sucesso
    return {"message": f"Produto ID {product_id} excluido com sucesso"}
```

### Passo 4: Executar a Aplicação

Para rodar a API, use o Uvicorn no terminal:

```bash
# Certifique-se de que o ambiente virtual esta ativo
# Navegue ate a pasta do projeto
cd ~/meus-projetos/crud-produtos

# Execute a aplicacao com Uvicorn
# "uvicorn" = servidor ASGI
# "main:app" = arquivo main.py, variavel app
# "--reload" = reiniciar automaticamente quando o codigo mudar
uvicorn main:app --reload
```

Saida esperada:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

> A API esta rodando em `http://127.0.0.1:8000`. Mantenha o terminal aberto enquanto testa.

> Para parar o servidor, pressione `CTRL+C` no terminal.


### Passo 5: Testar a API

Você pode testar a API de várias formas. A mais simples e usar o **navegador** para rotas GET e o **curl** no terminal para todas as rotas.

#### Testar com o Navegador

Abra o navegador e acesse:

- `http://127.0.0.1:8000/products` — Lista todos os produtos (retorna JSON)
- `http://127.0.0.1:8000/products/1` — Busca o produto com ID 1

#### Testar com curl no Terminal

Abra **outro terminal** (mantenha o servidor rodando no primeiro) e execute:

```bash
# Listar todos os produtos (GET)
# "curl" = ferramenta para fazer requisicoes HTTP
# "-X GET" = metodo GET (buscar dados)
curl -X GET http://127.0.0.1:8000/products
```

Saida esperada:
```json
[]
```

> A lista esta vazia porque ainda não cadastramos nenhum produto pela API.

```bash
# Cadastrar um produto (POST)
# "-X POST" = metodo POST (criar dados)
# "-H" = header (cabecalho) — informamos que estamos enviando JSON
# "-d" = data (dados) — o corpo da requisicao em JSON
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"}'
```

Saida esperada:
```json
{"id":1,"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}
```

```bash
# Buscar produto por ID (GET)
curl -X GET http://127.0.0.1:8000/products/1
```

Saida esperada:
```json
{"id":1,"name":"Arroz","price":8.99,"quantity":50,"category":"Alimentos"}
```

```bash
# Atualizar produto (PUT)
# "-X PUT" = metodo PUT (atualizar dados)
curl -X PUT http://127.0.0.1:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"name": "Arroz Integral", "price": 12.50, "quantity": 30, "category": "Alimentos"}'
```

Saida esperada:
```json
{"id":1,"name":"Arroz Integral","price":12.5,"quantity":30,"category":"Alimentos"}
```

```bash
# Excluir produto (DELETE)
# "-X DELETE" = metodo DELETE (excluir dados)
curl -X DELETE http://127.0.0.1:8000/products/1
```

Saida esperada:
```json
{"message":"Produto ID 1 excluido com sucesso"}
```

---

## Comparação: Terminal vs API HTTP

| Aspecto | v2 (Terminal + SQLite) | v3 (FastAPI + SQLite) |
|---------|----------------------|----------------------|
| Interface | Menu no terminal | Rotas HTTP |
| Acesso | Apenas no computador local | Qualquer dispositivo na rede |
| Formato de dados | Texto no terminal | JSON |
| Validação | Função Python manual | Pydantic (automática) |
| Documentação | Nenhuma | Swagger (automática) |
| Multiplos clientes | Não | Sim |

---

## Estrutura Final do Projeto

```
crud-produtos/
    main.py                # Aplicacao FastAPI (rotas da API)
    models.py              # Modelos de dados Pydantic
    database.py            # Funcoes de acesso ao SQLite
    crud_memory.py         # Modulo 29 — versao em memoria
    crud_sqlite.py         # Modulo 30 — versao terminal + SQLite
    products.db            # Banco de dados SQLite (gerado)
    requirements.txt       # Dependencias (fastapi, uvicorn)
    venv/                  # Ambiente virtual
```

---

## Para Saber Mais

- [W3Schools — Python Machine Learning](https://www.w3schools.com/python/python_ml_getting_started.asp)
  _Introducao a conceitos de programação com Python (W3Schools)_
- [W3Schools — HTTP Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
  _Referencia sobre os métodos HTTP (GET, POST, PUT, DELETE)_
- [W3Schools — HTTP Status Codes](https://www.w3schools.com/tags/ref_httpmessages.asp)
  _Lista completa de códigos de status HTTP_
- [W3Schools — JSON](https://www.w3schools.com/js/js_json_intro.asp)
  _Introducao ao formato JSON_
- [Documentação Oficial FastAPI](https://fastapi.tiangolo.com/)
  _Documentacao completa do FastAPI em ingles_
- [Documentação Oficial Python — sqlite3](https://docs.python.org/pt-br/3/library/sqlite3.html)
  _Referencia do módulo sqlite3 em portugues_

---

## Perguntas Frequentes (FAQ)

**P: O que e uma API?**
R: API (Application Programming Interface) e uma interface que permite que programas se comuniquem entre si. No nosso caso, a API permite que navegadores, aplicativos e outros programas acessem o sistema de produtos através de requisicoes HTTP.

**P: O que e FastAPI?**
R: FastAPI e um framework Python para criar APIs HTTP. Ele e rápido, fácil de usar e gera documentação automática. Foi criado por Sebastian Ramirez e e um dos frameworks mais populares do Python.

**P: O que e Uvicorn?**
R: Uvicorn e o servidor que roda a aplicação FastAPI. Ele recebe as requisicoes HTTP e as encaminha para o FastAPI processar. Pense nele como o "garcom" que recebe os pedidos dos clientes.

**P: O que e HTTP?**
R: HTTP (HyperText Transfer Protocol) e o protocolo usado para comunicação na internet. Quando você acessa um site no navegador, esta usando HTTP. Nossa API usa HTTP para receber pedidos e enviar respostas.

**P: O que sao GET, POST, PUT e DELETE?**
R: Sao os métodos HTTP que indicam o tipo de operação. GET busca dados, POST cria dados, PUT atualiza dados e DELETE remove dados. Cada rota da API responde a um método específico.

**P: O que e JSON?**
R: JSON (JavaScript Object Notation) e um formato de texto para representar dados estruturados. E o formato padrão para troca de dados entre APIs. Você ja aprendeu JSON no módulo 21.

**P: O que e Pydantic?**
R: Pydantic e uma biblioteca Python para validação de dados. O FastAPI usa Pydantic para verificar automaticamente se os dados enviados pelo cliente estão no formato correto. Se o cliente enviar um preco como texto em vez de número, o Pydantic rejeita automaticamente.

**P: O que e `@app.get()` e `@app.post()`?**
R: Sao decoradores que associam uma função Python a uma rota HTTP. `@app.get("/products")` significa: "quando alguem fizer uma requisicao GET para /products, execute esta função". O decorador e a linha que comeca com `@` acima da função.

**P: O que e HTTPException?**
R: E uma classe do FastAPI que permite retornar erros HTTP. Quando usamos `raise HTTPException(status_code=404, detail="Nao encontrado")`, a API retorna uma resposta com código 404 e a mensagem de erro em JSON.

**P: O que e `response_model`?**
R: E um parametro do decorador de rota que define o formato da resposta. O FastAPI usa o modelo Pydantic para validar e formatar a resposta automaticamente, garantindo que os dados retornados estejam no formato correto.

**P: Por que separar em 3 arquivos (main, models, database)?**
R: Separar em arquivos organiza o código por responsabilidade. `models.py` define os formatos de dados, `database.py` cuida do banco de dados e `main.py` define as rotas da API. Isso facilita a manutenção — se precisar mudar o banco, so altera `database.py`.

**P: O que e `127.0.0.1:8000`?**
R: `127.0.0.1` e o endereco do seu proprio computador (localhost). `8000` e a porta onde o servidor esta escutando. Juntos, formam o endereco completo da API. Você acessa no navegador ou com curl.

**P: Posso acessar a API de outro computador?**
R: Por padrão, a API so aceita conexões do proprio computador (127.0.0.1). Para aceitar conexões de outros computadores na rede, execute com `uvicorn main:app --host 0.0.0.0 --reload`. Mas cuidado — isso expoe a API na rede.

**P: O que e `--reload` no comando uvicorn?**
R: O `--reload` faz o servidor reiniciar automaticamente quando você salva alteracoes no código. Isso e muito útil durante o desenvolvimento. Em produção, não use `--reload`.

**P: O que e curl?**
R: curl e uma ferramenta de linha de comando para fazer requisicoes HTTP. E como um "navegador no terminal". Você pode enviar requisicoes GET, POST, PUT e DELETE com curl. Ja vem instalado na maioria dos sistemas Linux e macOS.

**P: O que acontece se eu enviar dados invalidos?**
R: O Pydantic valida os dados automaticamente. Se você enviar um preco como texto ("abc" em vez de 8.99), a API retorna erro 422 (Unprocessable Entity) com uma mensagem explicando qual campo esta inválido.

**P: Posso usar o banco de dados do módulo 30?**
R: Sim. Como ambos usam o mesmo arquivo `products.db` e a mesma estrutura de tabela, os dados cadastrados pelo programa do módulo 30 estarao disponiveis na API do módulo 31, e vice-versa.

**P: O que e ASGI?**
R: ASGI (Asynchronous Server Gateway Interface) e o padrão que o Uvicorn usa para se comunicar com o FastAPI. E a evolucao do WSGI, suportando operações assincronas. Você não precisa se preocupar com os detalhes — basta saber que o Uvicorn e o servidor e o FastAPI e a aplicação.

**P: Preciso saber JavaScript para usar APIs?**
R: Não. APIs sao independentes de linguagem. Você pode acessar uma API de qualquer linguagem ou ferramenta que suporte HTTP: Python, JavaScript, curl, navegador, Postman, etc. Neste módulo, usamos curl e o navegador.

**P: O que e um endpoint?**
R: Endpoint e o endereco específico de uma operação na API. Por exemplo, `/products` e o endpoint para listar produtos, e `/products/1` e o endpoint para buscar o produto com ID 1. Cada endpoint responde a um ou mais métodos HTTP.

**P: O FastAPI e gratuito?**
R: Sim. O FastAPI e um projeto open source (código aberto) e totalmente gratuito. Você pode usar em projetos pessoais e comerciais sem custo.

---

## Exercícios

Os exercícios deste módulo estão em um arquivo separado para facilitar a navegação:

[Ir para os Exercícios do Módulo 31 ->](31-crud-fastapi-exercícios.md)