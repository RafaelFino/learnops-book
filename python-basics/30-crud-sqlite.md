# 30 — CRUD com SQLite: Persistência de Dados em Banco de Dados

[<- Anterior: CRUD em Memória](29-crud-memória.md) | [Glossário](00-glossário.md) | [Próximo: CRUD com FastAPI ->](31-crud-fastapi.md)

---

## Introdução

No módulo anterior, você construiu um sistema CRUD completo que armazena produtos em uma lista de dicionários na memória. O problema e que, quando o programa fecha, todos os dados sao perdidos. Imagine que você cadastrou 100 produtos e, ao fechar o terminal, tudo desaparece. Não e muito útil para uma loja real, certo?

Neste módulo, você vai resolver esse problema usando o **SQLite**, um banco de dados que salva os dados em um **arquivo no disco** do computador. Assim, mesmo que você feche o programa, desligue o computador e ligue novamente, os dados continuam la.

### O Que e SQLite?

Pense em um **caderno** onde você anota informações. Quando você fecha o caderno e guarda na gaveta, as anotacoes continuam la. Quando você abre o caderno novamente, pode ler e modificar as anotacoes. O SQLite funciona exatamente assim — e um "caderno digital" que guarda dados em um arquivo.

Caracteristicas do SQLite:

- **Sem servidor:** Não precisa instalar nenhum programa extra. O SQLite e um arquivo simples.
- **Ja vem com o Python:** O módulo `sqlite3` faz parte da biblioteca padrão. Não precisa instalar nada com pip.
- **Um arquivo:** Todo o banco de dados fica em um único arquivo (por exemplo, `products.db`).
- **Perfeito para aprender:** E o banco de dados mais simples que existe, ideal para iniciantes.

### O Que Você Vai Aprender

- Como conectar ao SQLite usando o módulo `sqlite3`
- Como criar tabelas para armazenar dados
- Como executar as 4 operações CRUD com SQL
- Como evoluir o programa do módulo 29 para usar banco de dados

> **Nota importante sobre SQL:** Este módulo foca na **integração Python-SQLite**, não no ensino de SQL. Os comandos SQL necessários serao fornecidos e explicados nos exemplos e exercícios. Você não precisa decorar SQL — o importante e entender como o Python se comunica com o banco de dados.

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Use a mesma pasta do projeto CRUD: `~/meus-projetos/crud-produtos/`
2. Copie o código e cole em um novo arquivo no VSCode
3. No terminal: `cd ~/meus-projetos/crud-produtos`
4. Execute: `python3 nome_do_arquivo.py`
5. O arquivo `products.db` sera criado automaticamente na mesma pasta

---

## Conceitos Básicos de Banco de Dados

Antes de começar a programar, vamos entender alguns conceitos básicos:

### Tabela

Uma **tabela** (table) e como uma planilha do Excel: tem **colunas** (campos) e **linhas** (registros). No nosso caso, a tabela se chama `products` e tem as colunas: id, name, price, quantity e category.

```
Tabela: products
+----+----------+-------+----------+-----------+
| id | name     | price | quantity | category  |
+----+----------+-------+----------+-----------+
| 1  | Arroz    | 8.99  | 50       | Alimentos |
| 2  | Sabao    | 4.50  | 80       | Limpeza   |
| 3  | Shampoo  | 12.75 | 25       | Higiene   |
+----+----------+-------+----------+-----------+
```

### SQL

**SQL** (Structured Query Language = Linguagem de Consulta Estruturada) e a linguagem usada para "conversar" com bancos de dados. Os comandos SQL que você vai usar neste módulo sao:


| Comando SQL | O Que Faz | Equivalente CRUD |
|-------------|-----------|-----------------|
| `CREATE TABLE` | Cria uma tabela | (estrutura) |
| `INSERT INTO` | Adiciona um registro | Create (Criar) |
| `SELECT` | Consulta registros | Read (Ler) |
| `UPDATE` | Modifica um registro | Update (Atualizar) |
| `DELETE` | Remove um registro | Delete (Excluir) |

### Conexão, Cursor e Commit

Para usar o SQLite no Python, você precisa de tres conceitos:

1. **Conexão** (connection): Abre o "caderno" — conecta ao arquivo do banco de dados
2. **Cursor**: A "caneta" — executa os comandos SQL no banco
3. **Commit**: "Salvar" — confirma as alteracoes no banco de dados

```python
# Importamos o modulo sqlite3 (ja vem com o Python)
# "sqlite3" = modulo para trabalhar com banco de dados SQLite
import sqlite3

# Abrimos uma conexao com o banco de dados
# Se o arquivo nao existir, o SQLite cria automaticamente
# "connection" = conexao
connection = sqlite3.connect("products.db")

# Criamos um cursor para executar comandos SQL
# "cursor" = cursor (a "caneta" que escreve no banco)
cursor = connection.cursor()

# Aqui executamos comandos SQL com cursor.execute(...)

# Salvamos as alteracoes no banco
# "commit" = confirmar/salvar
connection.commit()

# Fechamos a conexao quando terminamos
# "close" = fechar
connection.close()
```

Saida esperada:
```
(nenhuma saida — o programa apenas cria o arquivo products.db)
```

> Apos executar, você vera o arquivo `products.db` na pasta do projeto. Esse e o banco de dados.

---

## Construindo o CRUD com SQLite Passo a Passo

### Passo 1: Criar a Tabela de Produtos

Antes de armazenar produtos, precisamos criar a tabela no banco de dados:

```python
# Importamos o modulo sqlite3
import sqlite3


# Funcao que cria a tabela de produtos no banco de dados
# "create" = criar, "table" = tabela
def create_table():
    """Cria a tabela products no banco de dados se nao existir."""
    # Abrimos a conexao com o banco
    # "connection" = conexao
    connection = sqlite3.connect("products.db")
    # Criamos o cursor
    cursor = connection.cursor()

    # Executamos o comando SQL para criar a tabela
    # CREATE TABLE IF NOT EXISTS = criar tabela se nao existir
    # INTEGER PRIMARY KEY AUTOINCREMENT = numero inteiro, chave primaria, incremento automatico
    # TEXT NOT NULL = texto que nao pode ser vazio
    # REAL NOT NULL = numero decimal que nao pode ser vazio
    # INTEGER NOT NULL = numero inteiro que nao pode ser vazio
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            category TEXT NOT NULL
        )
    """)

    # Salvamos as alteracoes
    connection.commit()
    # Fechamos a conexao
    connection.close()
    print("Tabela 'products' criada com sucesso!")


# Chamamos a funcao para criar a tabela
create_table()
```

Saida esperada:
```
Tabela 'products' criada com sucesso!
```

**Explicacao do SQL:**

- `CREATE TABLE IF NOT EXISTS products`: Cria a tabela `products` apenas se ela ainda não existir. Isso evita erros se você executar o programa mais de uma vez.
- `id INTEGER PRIMARY KEY AUTOINCREMENT`: O campo `id` e um número inteiro que serve como identificador único. O `AUTOINCREMENT` faz o SQLite gerar o próximo número automaticamente (1, 2, 3...).
- `TEXT NOT NULL`: Campo de texto que não pode ficar vazio.
- `REAL NOT NULL`: Campo de número decimal que não pode ficar vazio.

### Passo 2: Create — Inserir Produto no Banco

```python
import sqlite3


def create_product(name, price, quantity, category):
    """Insere um novo produto no banco de dados."""
    # Abrimos a conexao
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # Executamos o comando SQL para inserir
    # INSERT INTO products (campos) VALUES (valores)
    # Os "?" sao placeholders — o sqlite3 substitui pelos valores da tupla
    # Isso protege contra SQL Injection (um tipo de ataque)
    cursor.execute(
        "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
        (name, price, quantity, category)
    )

    # Salvamos as alteracoes
    connection.commit()

    # Obtemos o ID gerado automaticamente pelo banco
    # lastrowid retorna o ID do ultimo registro inserido
    # "product_id" = identificador do produto
    product_id = cursor.lastrowid

    # Fechamos a conexao
    connection.close()

    print(f"Produto '{name}' cadastrado com sucesso! ID: {product_id}")
    return product_id


# Testamos a funcao (a tabela ja deve existir)
create_product("Arroz", 8.99, 50, "Alimentos")
create_product("Sabao", 4.50, 80, "Limpeza")
create_product("Shampoo", 12.75, 25, "Higiene")
```

Saida esperada:
```
Produto 'Arroz' cadastrado com sucesso! ID: 1
Produto 'Sabao' cadastrado com sucesso! ID: 2
Produto 'Shampoo' cadastrado com sucesso! ID: 3
```

**Sobre os placeholders `?`:** Em vez de colocar os valores diretamente no SQL (como `VALUES ('Arroz', 8.99, 50, 'Alimentos')`), usamos `?` e passamos os valores em uma tupla separada. Isso e uma **boa prática de segurança** que protege contra ataques de SQL Injection.

### Passo 3: Read — Consultar Produtos

```python
import sqlite3


def list_all_products():
    """Lista todos os produtos do banco de dados."""
    # Abrimos a conexao
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # Executamos o comando SQL para buscar todos os registros
    # SELECT * FROM products = selecionar tudo da tabela products
    cursor.execute("SELECT * FROM products")

    # fetchall() retorna todos os resultados como lista de tuplas
    # "rows" = linhas (registros do banco)
    rows = cursor.fetchall()

    # Fechamos a conexao
    connection.close()

    # Verificamos se ha resultados
    if len(rows) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Exibimos os resultados em formato de tabela
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)

    # Cada row e uma tupla: (id, name, price, quantity, category)
    for row in rows:
        # Desempacotamos a tupla
        product_id, name, price, quantity, category = row
        print(f"{product_id:<5} {name:<20} {price:>10.2f} {quantity:>5} {category:<15}")

    print(f"\nTotal: {len(rows)} produto(s)")


def find_product_by_id(product_id):
    """Busca um produto pelo ID no banco de dados."""
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # SELECT * FROM products WHERE id = ? — busca pelo ID
    # WHERE = onde (condicao de filtro)
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))

    # fetchone() retorna apenas um resultado (ou None se nao encontrar)
    # "row" = linha (registro)
    row = cursor.fetchone()

    connection.close()

    # Se nao encontrou, retornamos None
    if row is None:
        return None

    # Convertemos a tupla para dicionario para facilitar o uso
    # "product" = produto
    product = {
        "id": row[0],
        "name": row[1],
        "price": row[2],
        "quantity": row[3],
        "category": row[4]
    }
    return product


# Testamos as funcoes
list_all_products()

print("\nBusca por ID 2:")
product = find_product_by_id(2)
if product is not None:
    print(f"  {product['name']} - R$ {product['price']:.2f}")
else:
    print("  Nao encontrado")
```

Saida esperada:
```
ID    Nome                     Preco   Qtd Categoria
------------------------------------------------------------
1     Arroz                     8.99    50 Alimentos
2     Sabao                     4.50    80 Limpeza
3     Shampoo                  12.75    25 Higiene

Total: 3 produto(s)

Busca por ID 2:
  Sabao - R$ 4.50
```

**Diferença importante:** No módulo 29, `find_product_by_id` percorria uma lista com um loop `for`. Agora, o banco de dados faz a busca por nos com `WHERE id = ?`. Isso e muito mais eficiente, especialmente com muitos registros.


### Passo 4: Update — Atualizar Produto no Banco

```python
import sqlite3


def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto no banco de dados."""
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # UPDATE products SET campo = valor WHERE id = ?
    # SET = definir (novos valores)
    # WHERE = onde (qual registro atualizar)
    cursor.execute(
        "UPDATE products SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?",
        (name, price, quantity, category, product_id)
    )

    # Salvamos as alteracoes
    connection.commit()

    # rowcount indica quantas linhas foram afetadas
    # Se for 0, o produto nao foi encontrado
    # "rows_affected" = linhas afetadas
    rows_affected = cursor.rowcount

    connection.close()

    if rows_affected == 0:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False

    print(f"Produto ID {product_id} atualizado com sucesso!")
    return True


# Testamos a funcao
update_product(1, "Arroz Integral", 12.50, 30, "Alimentos")
update_product(99, "Teste", 1.0, 1, "Teste")  # ID inexistente
```

Saida esperada:
```
Produto ID 1 atualizado com sucesso!
Produto com ID 99 nao encontrado.
```

**Sobre `rowcount`:** Apos executar um `UPDATE` ou `DELETE`, o atributo `cursor.rowcount` indica quantas linhas foram afetadas. Se for 0, significa que nenhum registro correspondia a condição `WHERE`, ou seja, o produto não existe.

### Passo 5: Delete — Excluir Produto do Banco

```python
import sqlite3


def delete_product(product_id):
    """Remove um produto do banco de dados."""
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # DELETE FROM products WHERE id = ?
    # DELETE FROM = excluir de
    # WHERE = onde (qual registro excluir)
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

    # Salvamos as alteracoes
    connection.commit()

    # Verificamos se algum registro foi excluido
    rows_affected = cursor.rowcount

    connection.close()

    if rows_affected == 0:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False

    print(f"Produto ID {product_id} excluido com sucesso!")
    return True


# Testamos a funcao
delete_product(2)   # Exclui o Sabao
delete_product(99)  # ID inexistente
```

Saida esperada:
```
Produto ID 2 excluido com sucesso!
Produto com ID 99 nao encontrado.
```

---

## Comparação: Memória vs SQLite

Vamos comparar as duas versoes para entender as diferencas:

| Aspecto | v1 (Memória) | v2 (SQLite) |
|---------|-------------|-------------|
| Armazenamento | Lista de dicionários | Arquivo .db |
| Persistência | Dados perdidos ao fechar | Dados salvos no disco |
| ID | Contador manual (`next_id`) | Gerado automaticamente (`AUTOINCREMENT`) |
| Busca | Loop `for` na lista | `SELECT ... WHERE` (otimizado) |
| Validação | Função Python | Função Python + restrições SQL (`NOT NULL`) |
| Dependências | Nenhuma | Módulo `sqlite3` (ja vem com Python) |

### O Que Mudou no Código

1. **Sem lista global:** Não precisamos mais da variável `products = []`. Os dados ficam no banco.
2. **Sem contador global:** O `AUTOINCREMENT` do SQLite gera os IDs automaticamente.
3. **Conexão a cada operação:** Abrimos e fechamos a conexão em cada função. Isso e simples e seguro.
4. **Tuplas em vez de dicionários:** O SQLite retorna os dados como tuplas. Convertemos para dicionários quando necessário.

---

## Usando `with` para Gerenciar Conexões

Assim como usamos `with open(...)` para arquivos, podemos usar `with` para conexões SQLite. Isso garante que as alteracoes sejam salvas (commit) automaticamente:

```python
import sqlite3


# Funcao que lista produtos usando gerenciador de contexto
def list_products_with_context():
    """Lista produtos usando 'with' para gerenciar a conexao."""
    # "with" garante que o commit e feito automaticamente
    # Se ocorrer um erro, as alteracoes sao revertidas (rollback)
    with sqlite3.connect("products.db") as connection:
        # Criamos o cursor
        cursor = connection.cursor()
        # Executamos a consulta
        cursor.execute("SELECT * FROM products")
        # Obtemos os resultados
        rows = cursor.fetchall()

    # A conexao ja foi fechada automaticamente pelo "with"
    # Exibimos os resultados
    for row in rows:
        product_id, name, price, quantity, category = row
        print(f"[{product_id}] {name} - R$ {price:.2f}")


# Testamos
list_products_with_context()
```

Saida esperada:
```
[1] Arroz Integral - R$ 12.50
[3] Shampoo - R$ 12.75
```

> O produto 2 (Sabao) não aparece porque foi excluido no passo anterior.

---

## Programa Completo: CRUD com SQLite

Aqui esta o programa completo reunindo todas as funções. Salve como `crud_sqlite.py`:

```python
# ============================================================
# CRUD de Produtos com SQLite — Versao 2
# Armazenamento: banco de dados SQLite (dados persistentes)
# ============================================================
# "crud" = Create, Read, Update, Delete
# "sqlite" = banco de dados leve em arquivo

# Importamos o modulo sqlite3 (ja vem com o Python)
import sqlite3

# Nome do arquivo do banco de dados
# "DATABASE_FILE" = arquivo do banco de dados
DATABASE_FILE = "products.db"


# --- Funcao de Inicializacao ---

def create_table():
    """Cria a tabela products se nao existir."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        """)


# --- Funcoes de Validacao ---

def validate_product_data(name, price, quantity, category):
    """Valida os dados de um produto e retorna lista de erros."""
    errors = []
    if not name or name.strip() == "":
        errors.append("Nome nao pode ser vazio")
    if not isinstance(price, (int, float)):
        errors.append("Preco deve ser um numero")
    elif price < 0:
        errors.append("Preco nao pode ser negativo")
    if not isinstance(quantity, int):
        errors.append("Quantidade deve ser inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    return errors


# --- Funcoes CRUD ---

def create_product(name, price, quantity, category):
    """Insere um novo produto no banco de dados."""
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao cadastrar:")
        for error in errors:
            print(f"  - {error}")
        return None
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
            (name, price, quantity, category)
        )
        product_id = cursor.lastrowid
    print(f"Produto '{name}' cadastrado! ID: {product_id}")
    return product_id


def list_all_products():
    """Lista todos os produtos do banco."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
    if len(rows) == 0:
        print("Nenhum produto cadastrado.")
        return
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)
    for row in rows:
        pid, name, price, qty, cat = row
        print(f"{pid:<5} {name:<20} {price:>10.2f} {qty:>5} {cat:<15}")
    print(f"\nTotal: {len(rows)} produto(s)")


def find_product_by_id(product_id):
    """Busca um produto pelo ID."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "price": row[2], "quantity": row[3], "category": row[4]}


def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto."""
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao atualizar:")
        for error in errors:
            print(f"  - {error}")
        return False
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE products SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?",
            (name, price, quantity, category, product_id)
        )
        if cursor.rowcount == 0:
            print(f"Produto ID {product_id} nao encontrado.")
            return False
    print(f"Produto ID {product_id} atualizado!")
    return True


def delete_product(product_id):
    """Remove um produto do banco."""
    with sqlite3.connect(DATABASE_FILE) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        if cursor.rowcount == 0:
            print(f"Produto ID {product_id} nao encontrado.")
            return False
    print(f"Produto ID {product_id} excluido!")
    return True


# --- Funcoes de Interface ---

def read_product_input():
    """Le os dados de um produto do usuario."""
    name = input("Nome: ")
    try:
        price = float(input("Preco: "))
    except ValueError:
        print("Preco invalido.")
        return None
    try:
        quantity = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade invalida.")
        return None
    category = input("Categoria: ")
    return name, price, quantity, category


def main():
    """Funcao principal com menu interativo."""
    create_table()
    print("=== CRUD de Produtos com SQLite ===")
    print("(Os dados sao salvos no arquivo products.db)")

    while True:
        print("\n1-Cadastrar 2-Listar 3-Buscar 4-Atualizar 5-Excluir 0-Sair")
        choice = input("Opcao: ")

        if choice == "1":
            print("\n--- Cadastrar ---")
            data = read_product_input()
            if data is not None:
                name, price, quantity, category = data
                create_product(name, price, quantity, category)

        elif choice == "2":
            list_all_products()

        elif choice == "3":
            try:
                pid = int(input("ID: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_product_by_id(pid)
            if product is None:
                print("Nao encontrado.")
            else:
                print(f"  ID: {product['id']}")
                print(f"  Nome: {product['name']}")
                print(f"  Preco: R$ {product['price']:.2f}")
                print(f"  Quantidade: {product['quantity']}")
                print(f"  Categoria: {product['category']}")

        elif choice == "4":
            try:
                pid = int(input("ID para atualizar: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_product_by_id(pid)
            if product is None:
                print("Nao encontrado.")
                continue
            print(f"Atual: {product['name']} - R$ {product['price']:.2f}")
            data = read_product_input()
            if data is not None:
                name, price, quantity, category = data
                update_product(pid, name, price, quantity, category)

        elif choice == "5":
            try:
                pid = int(input("ID para excluir: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_product_by_id(pid)
            if product is None:
                print("Nao encontrado.")
                continue
            confirm = input(f"Excluir '{product['name']}'? (s/n): ")
            if confirm.lower() == "s":
                delete_product(pid)
            else:
                print("Cancelado.")

        elif choice == "0":
            print("Ate a proxima!")
            break

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
```

Para executar:

```bash
cd ~/meus-projetos/crud-produtos
python3 crud_sqlite.py
```

> Na primeira execução, o arquivo `products.db` sera criado. Nas execucoes seguintes, os dados cadastrados anteriormente estarao disponiveis.


---

## Verificando o Banco de Dados

Você pode verificar o conteúdo do banco de dados de duas formas:

### Pelo Python

```python
import sqlite3

# Abrimos o banco e listamos todos os registros
with sqlite3.connect("products.db") as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

# Exibimos cada registro
for row in rows:
    print(row)
```

Saida esperada:
```
(1, 'Arroz', 8.99, 50, 'Alimentos')
(2, 'Sabao', 4.50, 80, 'Limpeza')
(3, 'Shampoo', 12.75, 25, 'Higiene')
```

### Pelo Terminal (sqlite3 CLI)

Se você tiver o comando `sqlite3` instalado no terminal:

```bash
# Abrimos o banco de dados no terminal
sqlite3 products.db

# Dentro do sqlite3, listamos os registros
SELECT * FROM products;

# Para sair do sqlite3
.quit
```

> O comando `sqlite3` pode não estar instalado por padrão. No Ubuntu/Debian, instale com: `sudo apt install sqlite3`

---

## Tratamento de Erros com Banco de Dados

Ao trabalhar com banco de dados, podem ocorrer erros. E importante trata-los:

```python
import sqlite3


# Funcao que demonstra tratamento de erros com SQLite
def safe_create_product(name, price, quantity, category):
    """Cadastra um produto com tratamento de erros."""
    try:
        # Tentamos executar a operacao no banco
        with sqlite3.connect("products.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
                (name, price, quantity, category)
            )
            product_id = cursor.lastrowid
        print(f"Produto '{name}' cadastrado! ID: {product_id}")
        return product_id
    except sqlite3.IntegrityError as error:
        # Erro de integridade (ex: campo NOT NULL com valor None)
        # "integrity" = integridade
        print(f"Erro de integridade: {error}")
        return None
    except sqlite3.OperationalError as error:
        # Erro operacional (ex: tabela nao existe, banco corrompido)
        # "operational" = operacional
        print(f"Erro operacional: {error}")
        return None
    except sqlite3.Error as error:
        # Qualquer outro erro do SQLite
        print(f"Erro no banco de dados: {error}")
        return None


# Testamos com dados validos
safe_create_product("Cafe", 15.90, 20, "Alimentos")

# Testamos com dados que violam NOT NULL
safe_create_product(None, 5.0, 10, "Teste")
```

Saida esperada:
```
Produto 'Cafe' cadastrado! ID: 4
Erro de integridade: NOT NULL constraint failed: products.name
```

---

## Para Saber Mais

- [W3Schools — Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)
  _Introducao a bancos de dados com Python (conceitos similares ao SQLite)_
- [W3Schools — SQL Tutorial](https://www.w3schools.com/sql/)
  _Tutorial completo de SQL para quem quiser aprofundar os comandos_
- [W3Schools — SQL INSERT INTO](https://www.w3schools.com/sql/sql_insert.asp)
  _Referencia sobre o comando INSERT para adicionar registros_
- [W3Schools — SQL SELECT](https://www.w3schools.com/sql/sql_select.asp)
  _Referencia sobre o comando SELECT para consultar registros_
- [Documentação Oficial Python — sqlite3](https://docs.python.org/pt-br/3/library/sqlite3.html)
  _Referencia completa do módulo sqlite3 em portugues_
- [Documentação Oficial Python — DB-API 2.0](https://docs.python.org/pt-br/3/library/sqlite3.html#sqlite3-tutorial)
  _Tutorial oficial sobre como usar o sqlite3 no Python_

---

## Perguntas Frequentes (FAQ)

**P: O que e SQLite?**
R: SQLite e um banco de dados leve que armazena todos os dados em um único arquivo. Não precisa de servidor, não precisa de instalacao extra e ja vem incluido no Python. E perfeito para aplicações pequenas, prototipos e aprendizado.

**P: Preciso instalar algo para usar o SQLite no Python?**
R: Não. O módulo `sqlite3` ja faz parte da biblioteca padrão do Python. Basta escrever `import sqlite3` e começar a usar. Não precisa de pip install.

**P: O que e o arquivo .db que aparece na pasta?**
R: E o arquivo do banco de dados. Todo o conteúdo das tabelas (produtos, no nosso caso) fica armazenado nesse arquivo. Você pode copiar esse arquivo para outro computador e os dados estarao la.

**P: O que acontece se eu apagar o arquivo .db?**
R: Todos os dados serao perdidos. O arquivo .db e o banco de dados. Se você apagar, e como apagar o caderno de anotacoes. Na proxima execução do programa, um novo arquivo vazio sera criado.

**P: O que e SQL?**
R: SQL (Structured Query Language) e a linguagem usada para "conversar" com bancos de dados. Com SQL, você pode criar tabelas, inserir dados, consultar, atualizar e excluir registros. Neste módulo, os comandos SQL sao fornecidos — você não precisa decorar.

**P: O que sao os `?` nos comandos SQL?**
R: Sao placeholders (marcadores de posição). Em vez de colocar os valores diretamente no SQL, usamos `?` e passamos os valores em uma tupla separada. Isso protege contra SQL Injection, um tipo de ataque onde alguem tenta inserir comandos maliciosos no banco.

**P: O que e SQL Injection?**
R: E um ataque onde alguem insere comandos SQL maliciosos através de campos de entrada. Por exemplo, se você colocar o nome do produto diretamente no SQL sem usar placeholders, alguem poderia digitar um nome que contenha comandos SQL para apagar dados. Os placeholders `?` evitam isso.

**P: O que e `cursor`?**
R: O cursor e um objeto que permite executar comandos SQL no banco de dados. Pense nele como uma "caneta" que escreve e le no banco. Você cria um cursor a partir da conexão e usa `cursor.execute()` para executar comandos.

**P: O que e `commit`?**
R: Commit e o ato de confirmar e salvar as alteracoes no banco de dados. Quando você insere, atualiza ou exclui dados, as alteracoes ficam "pendentes" ate você chamar `connection.commit()`. Usando `with`, o commit e feito automaticamente.

**P: O que e `fetchall` e `fetchone`?**
R: Sao métodos para obter os resultados de uma consulta SELECT. `fetchall()` retorna todos os resultados como uma lista de tuplas. `fetchone()` retorna apenas o primeiro resultado (ou None se não houver). Use `fetchone` quando espera um único resultado (busca por ID) e `fetchall` quando espera vários.

**P: Por que abrir e fechar a conexão em cada função?**
R: E a abordagem mais simples e segura para iniciantes. Cada função abre sua propria conexão, executa a operação e fecha. Isso evita problemas com conexões abertas por muito tempo. Em aplicações mais avancadas, você pode usar um pool de conexões.

**P: Posso usar o SQLite para aplicações grandes?**
R: O SQLite funciona bem para aplicações com ate milhoes de registros e poucos usuarios simultaneos. Para aplicações com muitos usuarios acessando ao mesmo tempo, bancos como PostgreSQL ou MySQL sao mais adequados. Para aprendizado e projetos pessoais, o SQLite e mais que suficiente.

**P: O que e `AUTOINCREMENT`?**
R: E uma instrução que diz ao SQLite para gerar o próximo número automaticamente para o campo ID. O primeiro produto recebe ID 1, o segundo ID 2, e assim por diante. Você não precisa controlar o contador manualmente como fazia na versão em memória.

**P: O que e `PRIMARY KEY`?**
R: Primary Key (chave primaria) e o campo que identifica cada registro de forma única. No nosso caso, o campo `id` e a chave primaria. Isso significa que não podem existir dois produtos com o mesmo ID.

**P: O que e `NOT NULL`?**
R: E uma restrição que impede que o campo fique vazio. Se você tentar inserir um produto sem nome (None), o SQLite vai gerar um erro. Isso e uma camada extra de proteção além da validação Python.

**P: Qual a diferença entre `TEXT`, `REAL` e `INTEGER` no SQL?**
R: Sao os tipos de dados do SQLite. `TEXT` armazena texto (equivalente a str no Python). `REAL` armazena números decimais (equivalente a float). `INTEGER` armazena números inteiros (equivalente a int). Escolha o tipo adequado para cada campo.

**P: O que e `rowcount`?**
R: E um atributo do cursor que indica quantas linhas foram afetadas pelo último comando UPDATE ou DELETE. Se `rowcount` for 0 apos um UPDATE, significa que nenhum registro foi encontrado com aquele ID. Usamos isso para verificar se a operação teve efeito.

**P: Posso ter mais de uma tabela no mesmo banco?**
R: Sim. Um banco SQLite pode ter quantas tabelas você quiser. Por exemplo, você poderia ter uma tabela `products` para produtos e uma tabela `categories` para categorias. Neste módulo, usamos apenas uma tabela para manter a simplicidade.

**P: Como faco backup do banco de dados?**
R: Basta copiar o arquivo `.db`. Como todo o banco esta em um único arquivo, copiar esse arquivo e fazer um backup completo. Você pode usar `cp products.db products_backup.db` no terminal.

**P: O que acontece se dois programas acessarem o mesmo banco ao mesmo tempo?**
R: O SQLite tem um sistema de bloqueio que permite apenas uma escrita por vez. Para leituras simultaneas, funciona bem. Para muitas escritas simultaneas, pode haver lentidao. Para nosso caso de uso (um programa de cada vez), não ha problema.

**P: Posso ver o conteúdo do banco sem o Python?**
R: Sim. Você pode usar o comando `sqlite3` no terminal (se estiver instalado) ou ferramentas graficas como DB Browser for SQLite. Também existem extensões do VSCode para visualizar bancos SQLite.

---

## Exercícios

Os exercícios deste módulo estão em um arquivo separado para facilitar a navegação:

[Ir para os Exercícios do Módulo 30 ->](30-crud-sqlite-exercícios.md)