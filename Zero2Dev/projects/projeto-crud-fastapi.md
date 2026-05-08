# Projeto do Capítulo 11 — CRUD Completo com FastAPI e SQLite

## Visao Geral

Neste projeto, você vai construir uma API REST completa de gerenciamento de produtos usando Python, FastAPI e SQLite. A API permite criar, listar, buscar, atualizar e remover produtos organizados por categorias, com persistência em banco de dados, validação automática e documentação interativa.

Este projeto consolida tudo que você aprendeu nos capítulos 5 (Python), 8 (bancos de dados), 10 (arquitetura) e 11 (APIs e integracoes).

---

## Requisitos

- Python 3.10 ou superior
- FastAPI e Uvicorn instalados (`pip3 install fastapi uvicorn`)
- Terminal para executar comandos
- Editor de código (VSCode recomendado)

---

## Fase 1: Banco de Dados e Modelos

### 1.1 — Configuração do Banco

Crie o arquivo `database.py` que inicializa o SQLite:

```python
# database.py
# Configuracao e inicializacao do banco de dados SQLite
import sqlite3  # "sqlite3" = modulo Python para SQLite (ja vem instalado)

# Nome do arquivo do banco de dados
# "DATABASE" = caminho do banco
DATABASE = "products.db"

def get_connection():
    """Cria e retorna uma conexao com o banco de dados"""
    # "connect" = conectar ao banco
    conn = sqlite3.connect(DATABASE)
    # "row_factory" = como os resultados sao retornados
    # "sqlite3.Row" = retorna como dicionario (acesso por nome da coluna)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Cria as tabelas se nao existirem"""
    conn = get_connection()
    cursor = conn.cursor()  # "cursor" = objeto para executar SQL

    # Tabela de categorias
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """)

    # Tabela de produtos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            price REAL NOT NULL CHECK(price > 0),
            stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0),
            category_id INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)

    conn.commit()  # "commit" = salvar as alteracoes
    conn.close()   # "close" = fechar a conexao
    print("Banco de dados inicializado com sucesso!")
```

### 1.2 — Modelos Pydantic

Crie a pasta `models/` com os modelos de dados:

```python
# models/__init__.py
# Arquivo vazio — marca a pasta como pacote Python
```

```python
# models/category.py
# Modelos Pydantic para categorias
from pydantic import BaseModel, Field

class CategoryCreate(BaseModel):
    """Dados para criar uma categoria"""
    name: str = Field(min_length=2, max_length=100)
    description: str = None

class CategoryResponse(BaseModel):
    """Dados retornados pela API"""
    id: int
    name: str
    description: str = None
```

```python
# models/product.py
# Modelos Pydantic para produtos
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    """Dados para criar um produto"""
    name: str = Field(min_length=2, max_length=200)
    description: str = None
    price: float = Field(gt=0)          # "gt" = greater than = maior que 0
    stock: int = Field(ge=0, default=0)  # "ge" = greater or equal = maior ou igual a 0
    category_id: int

class ProductUpdate(BaseModel):
    """Dados para atualizar um produto (todos opcionais)"""
    name: str = None
    description: str = None
    price: float = None
    stock: int = None
    category_id: int = None

class ProductResponse(BaseModel):
    """Dados retornados pela API"""
    id: int
    name: str
    description: str = None
    price: float
    stock: int
    category_id: int
    category_name: str = None  # Preenchido pelo service
    created_at: str = None
```

---

## Fase 2: Repositórios e CRUD Básico

### 2.1 — Repositório de Categorias

```python
# repositories/__init__.py
```

```python
# repositories/category_repository.py
# Acesso a dados de categorias
from database import get_connection

class CategoryRepository:
    """Repositorio para operacoes de banco de dados de categorias"""

    def create(self, name: str, description: str = None) -> dict:
        """Insere uma nova categoria no banco"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO categories (name, description) VALUES (?, ?)",
            (name, description)
        )
        conn.commit()
        category_id = cursor.lastrowid  # "lastrowid" = ID do ultimo registro inserido
        conn.close()
        return self.find_by_id(category_id)

    def find_all(self) -> list:
        """Retorna todas as categorias"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories ORDER BY name")
        rows = cursor.fetchall()  # "fetchall" = buscar todos os resultados
        conn.close()
        return [dict(row) for row in rows]

    def find_by_id(self, category_id: int) -> dict:
        """Busca categoria por ID"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories WHERE id = ?", (category_id,))
        row = cursor.fetchone()  # "fetchone" = buscar um resultado
        conn.close()
        return dict(row) if row else None

    def find_by_name(self, name: str) -> dict:
        """Busca categoria por nome"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories WHERE LOWER(name) = LOWER(?)", (name,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def delete(self, category_id: int) -> bool:
        """Remove uma categoria"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categories WHERE id = ?", (category_id,))
        conn.commit()
        affected = cursor.rowcount  # "rowcount" = linhas afetadas
        conn.close()
        return affected > 0

    def has_products(self, category_id: int) -> bool:
        """Verifica se a categoria tem produtos associados"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM products WHERE category_id = ?", (category_id,))
        row = cursor.fetchone()
        conn.close()
        return row["count"] > 0
```

### 2.2 — Repositório de Produtos

```python
# repositories/product_repository.py
# Acesso a dados de produtos
from database import get_connection

class ProductRepository:
    """Repositorio para operacoes de banco de dados de produtos"""

    def create(self, name: str, description: str, price: float,
               stock: int, category_id: int) -> dict:
        """Insere um novo produto no banco"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO products (name, description, price, stock, category_id)
               VALUES (?, ?, ?, ?, ?)""",
            (name, description, price, stock, category_id)
        )
        conn.commit()
        product_id = cursor.lastrowid
        conn.close()
        return self.find_by_id(product_id)

    def find_all(self, skip: int = 0, limit: int = 20,
                 category_id: int = None, min_price: float = None,
                 max_price: float = None, in_stock: bool = None,
                 search: str = None) -> list:
        """Retorna produtos com filtros e paginacao"""
        conn = get_connection()
        cursor = conn.cursor()

        # Monta a query dinamicamente com filtros
        query = """
            SELECT p.*, c.name as category_name
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE 1=1
        """
        params = []  # "params" = parametros da query

        if category_id is not None:
            query += " AND p.category_id = ?"
            params.append(category_id)

        if min_price is not None:
            query += " AND p.price >= ?"
            params.append(min_price)

        if max_price is not None:
            query += " AND p.price <= ?"
            params.append(max_price)

        if in_stock is True:
            query += " AND p.stock > 0"
        elif in_stock is False:
            query += " AND p.stock = 0"

        if search:
            query += " AND LOWER(p.name) LIKE LOWER(?)"
            params.append(f"%{search}%")  # "%" = qualquer texto antes/depois

        query += " ORDER BY p.name LIMIT ? OFFSET ?"
        params.extend([limit, skip])

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def find_by_id(self, product_id: int) -> dict:
        """Busca produto por ID com nome da categoria"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT p.*, c.name as category_name
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.id
            WHERE p.id = ?
        """, (product_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def find_by_name(self, name: str) -> dict:
        """Busca produto por nome (case-insensitive)"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE LOWER(name) = LOWER(?)", (name,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    def update(self, product_id: int, **fields) -> dict:
        """Atualiza campos de um produto"""
        # Filtra campos nao-nulos
        updates = {k: v for k, v in fields.items() if v is not None}
        if not updates:
            return self.find_by_id(product_id)

        # Monta SET dinamicamente
        set_clause = ", ".join(f"{k} = ?" for k in updates.keys())
        values = list(updates.values()) + [product_id]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"UPDATE products SET {set_clause} WHERE id = ?", values)
        conn.commit()
        conn.close()
        return self.find_by_id(product_id)

    def delete(self, product_id: int) -> bool:
        """Remove um produto"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        conn.commit()
        affected = cursor.rowcount
        conn.close()
        return affected > 0

    def get_stats(self) -> dict:
        """Retorna estatisticas dos produtos"""
        conn = get_connection()
        cursor = conn.cursor()

        # Total de produtos
        cursor.execute("SELECT COUNT(*) as total FROM products")
        total = cursor.fetchone()["total"]

        # Valor medio
        cursor.execute("SELECT AVG(price) as avg_price FROM products")
        avg_price = cursor.fetchone()["avg_price"] or 0

        # Por categoria
        cursor.execute("""
            SELECT c.name, COUNT(p.id) as count, AVG(p.price) as avg_price
            FROM categories c
            LEFT JOIN products p ON c.id = p.category_id
            GROUP BY c.id, c.name
            ORDER BY count DESC
        """)
        by_category = [dict(row) for row in cursor.fetchall()]

        # Em estoque vs sem estoque
        cursor.execute("SELECT COUNT(*) as count FROM products WHERE stock > 0")
        in_stock = cursor.fetchone()["count"]

        conn.close()
        return {
            "total_products": total,
            "average_price": round(avg_price, 2),
            "in_stock": in_stock,
            "out_of_stock": total - in_stock,
            "by_category": by_category
        }
```

---

## Fase 3: Servicos e Regras de Negocio

### 3.1 — Servico de Categorias

```python
# services/__init__.py
```

```python
# services/category_service.py
# Logica de negocio de categorias
from repositories.category_repository import CategoryRepository

class CategoryService:
    """Servico com regras de negocio para categorias"""

    def __init__(self):
        self.repo = CategoryRepository()

    def create(self, name: str, description: str = None) -> dict:
        """Cria categoria com validacao de nome unico"""
        # Verifica se ja existe
        existing = self.repo.find_by_name(name)
        if existing:
            raise ValueError(f"Categoria '{name}' ja existe")
        return self.repo.create(name, description)

    def list_all(self) -> list:
        """Lista todas as categorias"""
        return self.repo.find_all()

    def get_by_id(self, category_id: int) -> dict:
        """Busca categoria por ID"""
        category = self.repo.find_by_id(category_id)
        if not category:
            raise LookupError(f"Categoria {category_id} nao encontrada")
        return category

    def delete(self, category_id: int) -> None:
        """Remove categoria (so se nao tiver produtos)"""
        category = self.repo.find_by_id(category_id)
        if not category:
            raise LookupError(f"Categoria {category_id} nao encontrada")

        if self.repo.has_products(category_id):
            raise ValueError(f"Categoria '{category['name']}' tem produtos associados")

        self.repo.delete(category_id)
```

### 3.2 — Servico de Produtos

```python
# services/product_service.py
# Logica de negocio de produtos
from repositories.product_repository import ProductRepository
from repositories.category_repository import CategoryRepository

class ProductService:
    """Servico com regras de negocio para produtos"""

    def __init__(self):
        self.repo = ProductRepository()
        self.category_repo = CategoryRepository()

    def create(self, name: str, description: str, price: float,
               stock: int, category_id: int) -> dict:
        """Cria produto com validacoes de negocio"""
        # Verifica se categoria existe
        category = self.category_repo.find_by_id(category_id)
        if not category:
            raise LookupError(f"Categoria {category_id} nao encontrada")

        # Verifica nome unico
        existing = self.repo.find_by_name(name)
        if existing:
            raise ValueError(f"Produto '{name}' ja existe")

        return self.repo.create(name, description, price, stock, category_id)

    def list_all(self, skip: int = 0, limit: int = 20,
                 category_id: int = None, min_price: float = None,
                 max_price: float = None, in_stock: bool = None,
                 search: str = None) -> list:
        """Lista produtos com filtros e paginacao"""
        return self.repo.find_all(
            skip=skip, limit=limit, category_id=category_id,
            min_price=min_price, max_price=max_price,
            in_stock=in_stock, search=search
        )

    def get_by_id(self, product_id: int) -> dict:
        """Busca produto por ID"""
        product = self.repo.find_by_id(product_id)
        if not product:
            raise LookupError(f"Produto {product_id} nao encontrado")
        return product

    def update(self, product_id: int, **fields) -> dict:
        """Atualiza produto com validacoes"""
        # Verifica se produto existe
        product = self.repo.find_by_id(product_id)
        if not product:
            raise LookupError(f"Produto {product_id} nao encontrado")

        # Se mudou categoria, verifica se a nova existe
        if fields.get("category_id"):
            category = self.category_repo.find_by_id(fields["category_id"])
            if not category:
                raise LookupError(f"Categoria {fields['category_id']} nao encontrada")

        # Se mudou nome, verifica unicidade
        if fields.get("name"):
            existing = self.repo.find_by_name(fields["name"])
            if existing and existing["id"] != product_id:
                raise ValueError(f"Produto '{fields['name']}' ja existe")

        # Valida preco e estoque
        if fields.get("price") is not None and fields["price"] <= 0:
            raise ValueError("Preco deve ser maior que zero")
        if fields.get("stock") is not None and fields["stock"] < 0:
            raise ValueError("Estoque nao pode ser negativo")

        return self.repo.update(product_id, **fields)

    def delete(self, product_id: int) -> None:
        """Remove produto"""
        product = self.repo.find_by_id(product_id)
        if not product:
            raise LookupError(f"Produto {product_id} nao encontrado")
        self.repo.delete(product_id)

    def get_stats(self) -> dict:
        """Retorna estatisticas"""
        return self.repo.get_stats()
```

---

## Fase 4: Routers e Aplicação Principal

### 4.1 — Router de Categorias

```python
# routers/__init__.py
```

```python
# routers/categories.py
# Endpoints de categorias
from fastapi import APIRouter, HTTPException
from models.category import CategoryCreate, CategoryResponse
from services.category_service import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])
service = CategoryService()

@router.post("/", response_model=CategoryResponse, status_code=201)
def create_category(data: CategoryCreate):
    """Cria uma nova categoria"""
    try:
        return service.create(data.name, data.description)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/", response_model=list[CategoryResponse])
def list_categories():
    """Lista todas as categorias"""
    return service.list_all()

@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int):
    """Busca categoria por ID"""
    try:
        return service.get_by_id(category_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int):
    """Remove uma categoria (so se nao tiver produtos)"""
    try:
        service.delete(category_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
```

### 4.2 — Router de Produtos

```python
# routers/products.py
# Endpoints de produtos
from fastapi import APIRouter, HTTPException, Query
from models.product import ProductCreate, ProductUpdate, ProductResponse
from services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])
service = ProductService()

@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(data: ProductCreate):
    """Cria um novo produto"""
    try:
        return service.create(
            name=data.name, description=data.description,
            price=data.price, stock=data.stock,
            category_id=data.category_id
        )
    except LookupError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/stats")
def get_stats():
    """Retorna estatisticas dos produtos"""
    return service.get_stats()

@router.get("/", response_model=list[ProductResponse])
def list_products(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    category_id: int = None,
    min_price: float = None,
    max_price: float = None,
    in_stock: bool = None,
    search: str = None
):
    """Lista produtos com filtros e paginacao"""
    return service.list_all(
        skip=skip, limit=limit, category_id=category_id,
        min_price=min_price, max_price=max_price,
        in_stock=in_stock, search=search
    )

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):
    """Busca produto por ID"""
    try:
        return service.get_by_id(product_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductUpdate):
    """Atualiza um produto"""
    try:
        return service.update(
            product_id,
            name=data.name, description=data.description,
            price=data.price, stock=data.stock,
            category_id=data.category_id
        )
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int):
    """Remove um produto"""
    try:
        service.delete(product_id)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))
```

### 4.3 — Aplicação Principal

```python
# main.py
# Ponto de entrada da aplicacao
import time
from fastapi import FastAPI, Request
from database import init_db
from routers import categories, products

# Cria a aplicacao
app = FastAPI(
    title="API de Produtos",
    description="CRUD completo de produtos com categorias, filtros e paginacao",
    version="1.0.0"
)

# Middleware de logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url.path} - {response.status_code} - {duration:.3f}s")
    return response

# Registra routers
app.include_router(categories.router)
app.include_router(products.router)

# Endpoint raiz
@app.get("/", tags=["Root"])
def root():
    return {
        "name": "API de Produtos",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "categories": "/categories",
            "products": "/products",
            "stats": "/products/stats"
        }
    }

# Inicializa o banco ao iniciar
@app.on_event("startup")
def startup():
    init_db()
```

---

## Testando o Projeto Completo

### Iniciando o Servidor

```bash
uvicorn main:app --reload
```

### Script de Teste Completo

Execute estes comandos em sequência para testar todas as funcionalidades:

```bash
# === CATEGORIAS ===

# Criar categorias
echo "--- Criando categorias ---"
curl -s -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Eletronicos", "description": "Produtos eletronicos e informatica"}'

curl -s -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Moveis", "description": "Moveis para casa e escritorio"}'

curl -s -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Roupas", "description": "Vestuario em geral"}'

# Listar categorias
echo "\n--- Listando categorias ---"
curl -s http://localhost:8000/categories

# Tentar criar categoria duplicada (deve dar 409)
echo "\n--- Categoria duplicada ---"
curl -s -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Eletronicos"}'

# === PRODUTOS ===

# Criar produtos
echo "\n--- Criando produtos ---"
curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Notebook Dell", "price": 3500.0, "stock": 10, "category_id": 1}'

curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Mouse Logitech", "price": 89.90, "stock": 50, "category_id": 1}'

curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Cadeira Gamer", "price": 1200.0, "stock": 5, "category_id": 2}'

curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Mesa de Escritorio", "price": 750.0, "stock": 0, "category_id": 2}'

curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Camiseta Preta", "price": 49.90, "stock": 100, "category_id": 3}'

# Listar todos os produtos
echo "\n--- Todos os produtos ---"
curl -s http://localhost:8000/products

# Filtrar por categoria
echo "\n--- Eletronicos ---"
curl -s "http://localhost:8000/products?category_id=1"

# Filtrar por preco
echo "\n--- Preco entre 100 e 2000 ---"
curl -s "http://localhost:8000/products?min_price=100&max_price=2000"

# Filtrar em estoque
echo "\n--- Em estoque ---"
curl -s "http://localhost:8000/products?in_stock=true"

# Buscar por nome
echo "\n--- Busca: 'note' ---"
curl -s "http://localhost:8000/products?search=note"

# Paginacao
echo "\n--- Pagina 1 (2 itens) ---"
curl -s "http://localhost:8000/products?skip=0&limit=2"

echo "\n--- Pagina 2 (2 itens) ---"
curl -s "http://localhost:8000/products?skip=2&limit=2"

# Buscar por ID
echo "\n--- Produto ID 1 ---"
curl -s http://localhost:8000/products/1

# Atualizar produto
echo "\n--- Atualizando preco ---"
curl -s -X PUT http://localhost:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{"price": 3200.0}'

# Estatisticas
echo "\n--- Estatisticas ---"
curl -s http://localhost:8000/products/stats

# === VALIDACOES ===

# Produto com categoria inexistente (deve dar 400)
echo "\n--- Categoria inexistente ---"
curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Teste", "price": 10.0, "stock": 1, "category_id": 999}'

# Produto com nome duplicado (deve dar 409)
echo "\n--- Nome duplicado ---"
curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Notebook Dell", "price": 4000.0, "stock": 5, "category_id": 1}'

# Preco negativo (deve dar 422)
echo "\n--- Preco negativo ---"
curl -s -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Invalido", "price": -10, "stock": 1, "category_id": 1}'

# Deletar categoria com produtos (deve dar 409)
echo "\n--- Deletar categoria com produtos ---"
curl -s -X DELETE http://localhost:8000/categories/1

# Deletar produto
echo "\n--- Deletando produto 5 ---"
curl -s -X DELETE http://localhost:8000/products/5

# Produto nao encontrado (deve dar 404)
echo "\n--- Produto inexistente ---"
curl -s http://localhost:8000/products/999
```

---

## Seu Projeto Esta Pronto Quando

- [ ] O servidor inicia sem erros com `uvicorn main:app --reload`
- [ ] Acessar `http://localhost:8000/docs` mostra a documentação interativa
- [ ] Categorias podem ser criadas, listadas e removidas
- [ ] Produtos podem ser criados, listados, atualizados e removidos
- [ ] Reiniciar o servidor não perde os dados (persistência SQLite)
- [ ] Validação rejeita dados invalidos (preco negativo, nome vazio)
- [ ] Produto com categoria inexistente retorna erro 400
- [ ] Produto com nome duplicado retorna erro 409
- [ ] Categoria com produtos não pode ser removida (erro 409)
- [ ] Paginacao funciona (skip/limit)
- [ ] Filtros funcionam (categoria, preco, estoque)
- [ ] Busca por nome funciona (parcial, case-insensitive)
- [ ] Estatisticas retornam dados corretos
- [ ] Código organizado em camadas (routers, services, repositories, models)
- [ ] Middleware de logging registra todas as requisicoes

---

## Extensões Sugeridas

Apos completar o projeto base, tente adicionar:

1. **Autenticação**: proteger endpoints de criação/delecao com API key
2. **Histórico de precos**: registrar toda alteração de preco em tabela separada
3. **Importacao em lote**: endpoint que recebe lista de produtos e cria todos
4. **Exportacao CSV**: endpoint que retorna todos os produtos em formato CSV
5. **Testes automatizados**: usar pytest com TestClient do FastAPI
6. **Docker**: containerizar a aplicação com Dockerfile e docker-compose

Cada extensão e uma oportunidade de praticar conceitos que você aprendeu ao longo do curso.
