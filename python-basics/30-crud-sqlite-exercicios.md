# 30 — Exercícios: CRUD com SQLite

[<- Voltar para o módulo](30-crud-sqlite.md) | [Glossário](00-glossario.md)

---

> **Antes de começar:** Estes exercícios constroem progressivamente um sistema CRUD com banco de dados SQLite. Cada exercício fornece os comandos SQL necessários — o foco e na integração Python-SQLite. Tente resolver cada exercício sozinho antes de consultar a resposta.

> **Importante:** Antes de executar os exercícios, certifique-se de que a tabela `products` foi criada executando o programa do módulo principal. Se quiser começar do zero, apague o arquivo `products.db` da pasta.

---

### Exercício 1 — Criar a Tabela de Produtos

#### Enunciado

Crie um programa que conecte ao banco de dados `products.db` e crie a tabela `products` com os campos: id (inteiro, chave primaria, autoincremento), name (texto, não nulo), price (decimal, não nulo), quantity (inteiro, não nulo) e category (texto, não nulo). Use `CREATE TABLE IF NOT EXISTS` para evitar erros em execucoes repetidas.

#### Dicas

- Use `sqlite3.connect("products.db")` para conectar
- Use `cursor.execute()` para executar o SQL
- Use `connection.commit()` para salvar
- Use `connection.close()` para fechar

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** O programa deve criar o arquivo `products.db` na pasta e exibir "Tabela criada com sucesso"
- **Caso de borda:** Execute o programa duas vezes — na segunda vez, não deve dar erro (gracas ao `IF NOT EXISTS`)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos o modulo sqlite3 para trabalhar com banco de dados
# "sqlite3" = modulo para banco de dados SQLite
import sqlite3

# Abrimos a conexao com o banco de dados
# Se o arquivo nao existir, sera criado automaticamente
# "connection" = conexao
connection = sqlite3.connect("products.db")

# Criamos um cursor para executar comandos SQL
# "cursor" = cursor (executa comandos no banco)
cursor = connection.cursor()

# Executamos o comando SQL para criar a tabela
# CREATE TABLE IF NOT EXISTS = criar tabela se nao existir
# INTEGER PRIMARY KEY AUTOINCREMENT = inteiro, chave primaria, autoincremento
# TEXT NOT NULL = texto que nao pode ser vazio
# REAL NOT NULL = decimal que nao pode ser vazio
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL,
        category TEXT NOT NULL
    )
""")

# Salvamos as alteracoes no banco
# commit() confirma as alteracoes
connection.commit()

# Fechamos a conexao
# close() libera os recursos
connection.close()

# Informamos o sucesso
print("Tabela 'products' criada com sucesso!")
```

Saida esperada:
```
Tabela 'products' criada com sucesso!
```

---

### Exercício 2 — Inserir Produtos no Banco

#### Enunciado

Crie uma função `insert_product` que receba nome, preco, quantidade e categoria, e insira o produto no banco de dados. Use placeholders `?` para os valores. Insira 3 produtos e exiba o ID gerado para cada um.

#### Dicas

- Use `INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)`
- Passe os valores como tupla no segundo argumento de `execute()`
- Use `cursor.lastrowid` para obter o ID gerado

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Os 3 produtos devem receber IDs sequenciais (1, 2, 3 se o banco estiver vazio)
- **Caso de borda:** Execute novamente — os novos IDs devem continuar a sequência (4, 5, 6)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos o modulo sqlite3
import sqlite3


# Funcao que insere um produto no banco de dados
# "insert" = inserir, "product" = produto
def insert_product(name, price, quantity, category):
    """Insere um produto no banco e retorna o ID gerado."""
    # Abrimos a conexao com o banco
    connection = sqlite3.connect("products.db")
    # Criamos o cursor
    cursor = connection.cursor()

    # Executamos o comando SQL de insercao
    # INSERT INTO = inserir em
    # VALUES (?, ?, ?, ?) = valores (placeholders para seguranca)
    cursor.execute(
        "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
        (name, price, quantity, category)
    )

    # Salvamos as alteracoes
    connection.commit()

    # Obtemos o ID gerado automaticamente
    # lastrowid = ID da ultima linha inserida
    product_id = cursor.lastrowid

    # Fechamos a conexao
    connection.close()

    # Exibimos o resultado
    print(f"Produto '{name}' inserido com ID: {product_id}")
    # Retornamos o ID
    return product_id


# Inserimos 3 produtos
insert_product("Arroz", 8.99, 50, "Alimentos")
insert_product("Sabao", 4.50, 80, "Limpeza")
insert_product("Shampoo", 12.75, 25, "Higiene")
```

Saida esperada:
```
Produto 'Arroz' inserido com ID: 1
Produto 'Sabao' inserido com ID: 2
Produto 'Shampoo' inserido com ID: 3
```


---

### Exercício 3 — Listar Todos os Produtos do Banco

#### Enunciado

Crie uma função `list_all` que consulte todos os produtos do banco e exiba em formato de tabela. Use `SELECT * FROM products` e `fetchall()`.

#### Dicas

- Use `cursor.execute("SELECT * FROM products")` para consultar
- Use `cursor.fetchall()` para obter todos os resultados
- Cada resultado e uma tupla: (id, name, price, quantity, category)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Deve exibir todos os produtos cadastrados em formato de tabela
- **Caso de borda:** Se o banco estiver vazio, deve exibir "Nenhum produto cadastrado"

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que lista todos os produtos do banco
# "list" = listar, "all" = todos
def list_all():
    """Lista todos os produtos do banco de dados."""
    # Abrimos a conexao
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # Executamos a consulta SQL
    # SELECT * FROM products = selecionar tudo da tabela products
    cursor.execute("SELECT * FROM products")

    # Obtemos todos os resultados
    # fetchall() retorna uma lista de tuplas
    # "rows" = linhas (registros)
    rows = cursor.fetchall()

    # Fechamos a conexao
    connection.close()

    # Verificamos se ha resultados
    if len(rows) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Exibimos o cabecalho da tabela
    print(f"{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)

    # Percorremos cada registro
    for row in rows:
        # Desempacotamos a tupla
        # Cada tupla tem: (id, name, price, quantity, category)
        pid, name, price, quantity, category = row
        # Exibimos formatado
        print(f"{pid:<5} {name:<20} {price:>10.2f} {quantity:>5} {category:<15}")

    # Exibimos o total
    print(f"\nTotal: {len(rows)} produto(s)")


# Testamos a funcao
list_all()
```

Saida esperada:
```
ID    Nome                     Preco   Qtd Categoria
------------------------------------------------------------
1     Arroz                     8.99    50 Alimentos
2     Sabao                     4.50    80 Limpeza
3     Shampoo                  12.75    25 Higiene

Total: 3 produto(s)
```

---

### Exercício 4 — Buscar Produto por ID

#### Enunciado

Crie uma função `find_by_id` que receba um ID e retorne o produto como dicionário, ou `None` se não encontrar. Use `SELECT * FROM products WHERE id = ?` e `fetchone()`.

#### Dicas

- Use `WHERE id = ?` com placeholder para filtrar pelo ID
- Use `fetchone()` para obter um único resultado
- Converta a tupla para dicionário antes de retornar

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar ID 1 deve retornar o produto "Arroz"
- **Caso de borda:** Buscar ID 99 deve retornar None

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que busca um produto pelo ID no banco
# "find" = encontrar, "by" = por, "id" = identificador
def find_by_id(product_id):
    """Busca um produto pelo ID e retorna dicionario ou None."""
    # Abrimos a conexao
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # Executamos a consulta com filtro por ID
    # WHERE id = ? filtra pelo identificador
    # O segundo argumento e uma tupla com o valor do placeholder
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))

    # Obtemos um unico resultado
    # fetchone() retorna uma tupla ou None
    row = cursor.fetchone()

    # Fechamos a conexao
    connection.close()

    # Se nao encontrou, retornamos None
    if row is None:
        return None

    # Convertemos a tupla para dicionario
    # "product" = produto
    product = {
        "id": row[0],          # Primeiro elemento = id
        "name": row[1],        # Segundo elemento = name
        "price": row[2],       # Terceiro elemento = price
        "quantity": row[3],    # Quarto elemento = quantity
        "category": row[4]     # Quinto elemento = category
    }
    return product


# Teste 1: buscar ID existente
product = find_by_id(1)
if product is not None:
    print(f"Encontrado: {product['name']} - R$ {product['price']:.2f}")
else:
    print("Nao encontrado")

# Teste 2: buscar ID inexistente
product = find_by_id(99)
if product is not None:
    print(f"Encontrado: {product['name']}")
else:
    print("Nao encontrado")
```

Saida esperada:
```
Encontrado: Arroz - R$ 8.99
Nao encontrado
```

---

### Exercício 5 — Atualizar Produto no Banco

#### Enunciado

Crie uma função `update_product` que receba o ID e os novos dados, e atualize o registro no banco. Use `UPDATE products SET ... WHERE id = ?`. Verifique se o produto foi encontrado usando `cursor.rowcount`.

#### Dicas

- Use `UPDATE products SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?`
- Apos o execute, verifique `cursor.rowcount` — se for 0, o produto não existe
- Não esqueca do `commit()` para salvar as alteracoes

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Atualizar o produto ID 1 deve funcionar e exibir mensagem de sucesso
- **Caso de borda:** Atualizar ID 99 deve informar que o produto não foi encontrado

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que atualiza um produto no banco
# "update" = atualizar, "product" = produto
def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto no banco."""
    # Abrimos a conexao
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # Executamos o comando de atualizacao
    # UPDATE products SET campo = valor WHERE id = ?
    # SET = definir novos valores
    # WHERE = condicao (qual registro atualizar)
    cursor.execute(
        "UPDATE products SET name = ?, price = ?, quantity = ?, category = ? WHERE id = ?",
        (name, price, quantity, category, product_id)
    )

    # Salvamos as alteracoes
    connection.commit()

    # Verificamos se algum registro foi atualizado
    # rowcount = quantidade de linhas afetadas
    rows_affected = cursor.rowcount

    # Fechamos a conexao
    connection.close()

    # Se nenhuma linha foi afetada, o produto nao existe
    if rows_affected == 0:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False

    print(f"Produto ID {product_id} atualizado com sucesso!")
    return True


# Teste 1: atualizar produto existente
update_product(1, "Arroz Integral", 12.50, 30, "Alimentos")

# Teste 2: atualizar produto inexistente
update_product(99, "Teste", 1.0, 1, "Teste")
```

Saida esperada:
```
Produto ID 1 atualizado com sucesso!
Produto com ID 99 nao encontrado.
```

---

### Exercício 6 — Excluir Produto do Banco

#### Enunciado

Crie uma função `delete_product` que receba o ID e remova o registro do banco. Use `DELETE FROM products WHERE id = ?`. Verifique se o produto foi encontrado usando `cursor.rowcount`.

#### Dicas

- Use `DELETE FROM products WHERE id = ?` com placeholder
- Verifique `cursor.rowcount` apos o execute
- Não esqueca do `commit()`

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Excluir o produto ID 2 deve funcionar e exibir mensagem de sucesso
- **Caso de borda:** Excluir ID 99 deve informar que o produto não foi encontrado

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que exclui um produto do banco
# "delete" = excluir, "product" = produto
def delete_product(product_id):
    """Remove um produto do banco de dados."""
    # Abrimos a conexao
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    # Executamos o comando de exclusao
    # DELETE FROM products WHERE id = ?
    # DELETE FROM = excluir de
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

    # Salvamos as alteracoes
    connection.commit()

    # Verificamos se algum registro foi excluido
    rows_affected = cursor.rowcount

    # Fechamos a conexao
    connection.close()

    # Se nenhuma linha foi afetada, o produto nao existe
    if rows_affected == 0:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False

    print(f"Produto ID {product_id} excluido com sucesso!")
    return True


# Teste 1: excluir produto existente
delete_product(2)

# Teste 2: excluir produto inexistente
delete_product(99)
```

Saida esperada:
```
Produto ID 2 excluido com sucesso!
Produto com ID 99 nao encontrado.
```


---

### Exercício 7 — Usar Gerenciador de Contexto (with)

#### Enunciado

Reescreva a função `insert_product` do exercício 2 usando `with sqlite3.connect(...)` em vez de abrir e fechar a conexão manualmente. Compare as duas versoes.

#### Dicas

- Use `with sqlite3.connect("products.db") as connection:` para gerenciar a conexão
- O `with` faz o commit automaticamente ao sair do bloco
- Não precisa chamar `connection.close()` — o `with` cuida disso

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** O produto deve ser inserido normalmente, com o mesmo resultado do exercício 2
- **Caso de borda:** Se ocorrer um erro dentro do `with`, as alteracoes sao revertidas automaticamente

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que insere produto usando gerenciador de contexto
# "insert" = inserir, "product" = produto
def insert_product(name, price, quantity, category):
    """Insere um produto usando 'with' para gerenciar a conexao."""
    # "with" abre a conexao e garante commit automatico
    # Se ocorrer erro, as alteracoes sao revertidas (rollback)
    with sqlite3.connect("products.db") as connection:
        # Criamos o cursor dentro do bloco with
        cursor = connection.cursor()
        # Executamos a insercao
        cursor.execute(
            "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
            (name, price, quantity, category)
        )
        # Obtemos o ID gerado
        product_id = cursor.lastrowid
    # Ao sair do bloco with, o commit e feito automaticamente
    # A conexao tambem e fechada automaticamente
    print(f"Produto '{name}' inserido com ID: {product_id}")
    return product_id


# Testamos a funcao
insert_product("Cafe", 15.90, 20, "Alimentos")
insert_product("Detergente", 3.50, 60, "Limpeza")
```

Saida esperada:
```
Produto 'Cafe' inserido com ID: 4
Produto 'Detergente' inserido com ID: 5
```

---

### Exercício 8 — Buscar Produtos por Categoria

#### Enunciado

Crie uma função `find_by_category` que receba uma categoria e retorne uma lista de dicionários com os produtos daquela categoria. Use `SELECT * FROM products WHERE category = ?`.

#### Dicas

- Use `WHERE category = ?` com placeholder
- Use `fetchall()` para obter todos os resultados
- Converta cada tupla para dicionário

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar "Alimentos" deve retornar os produtos dessa categoria
- **Caso de borda:** Buscar "Eletronicos" deve retornar lista vazia

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que busca produtos por categoria
# "find" = encontrar, "by" = por, "category" = categoria
def find_by_category(category):
    """Busca produtos por categoria e retorna lista de dicionarios."""
    # Abrimos a conexao com gerenciador de contexto
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # Consultamos produtos da categoria informada
        # WHERE category = ? filtra pela categoria
        cursor.execute("SELECT * FROM products WHERE category = ?", (category,))
        # Obtemos todos os resultados
        rows = cursor.fetchall()

    # Convertemos as tuplas para dicionarios
    # "products" = produtos (lista de dicionarios)
    products = []
    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "quantity": row[3],
            "category": row[4]
        }
        products.append(product)

    return products


# Teste 1: categoria existente
results = find_by_category("Alimentos")
print(f"Alimentos: {len(results)} produto(s)")
for p in results:
    print(f"  [{p['id']}] {p['name']} - R$ {p['price']:.2f}")

# Teste 2: categoria inexistente
results = find_by_category("Eletronicos")
print(f"\nEletronicos: {len(results)} produto(s)")
```

Saida esperada:
```
Alimentos: 2 produto(s)
  [1] Arroz Integral - R$ 12.50
  [4] Cafe - R$ 15.90

Eletronicos: 0 produto(s)
```

---

### Exercício 9 — Contar Produtos por Categoria

#### Enunciado

Crie uma função `count_by_category` que use o SQL `SELECT category, COUNT(*) FROM products GROUP BY category` para contar quantos produtos existem em cada categoria. Exiba o resultado formatado.

#### Dicas

- `COUNT(*)` conta o número de registros
- `GROUP BY category` agrupa os resultados por categoria
- O resultado sera uma lista de tuplas: (categoria, contagem)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Deve exibir cada categoria com a quantidade de produtos
- **Caso de borda:** Se o banco estiver vazio, não deve exibir nenhuma categoria

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que conta produtos por categoria
# "count" = contar, "by" = por, "category" = categoria
def count_by_category():
    """Conta e exibe a quantidade de produtos por categoria."""
    # Abrimos a conexao
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # Executamos a consulta com agrupamento
        # SELECT category, COUNT(*) = selecionar categoria e contagem
        # GROUP BY category = agrupar por categoria
        cursor.execute("SELECT category, COUNT(*) FROM products GROUP BY category")
        # Obtemos os resultados
        rows = cursor.fetchall()

    # Verificamos se ha resultados
    if len(rows) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Exibimos o resultado formatado
    print("\n--- Produtos por Categoria ---")
    print(f"{'Categoria':<20} {'Quantidade':>10}")
    print("-" * 32)

    # Cada row e uma tupla: (categoria, contagem)
    for row in rows:
        # Desempacotamos a tupla
        category, count = row
        print(f"{category:<20} {count:>10}")

    print("-" * 32)


# Testamos a funcao
count_by_category()
```

Saida esperada:
```
--- Produtos por Categoria ---
Categoria              Quantidade
--------------------------------
Alimentos                       2
Higiene                         1
Limpeza                         1
--------------------------------
```

---

### Exercício 10 — Calcular Valor Total do Estoque com SQL

#### Enunciado

Crie uma função `total_stock_value` que use o SQL `SELECT SUM(price * quantity) FROM products` para calcular o valor total do estoque diretamente no banco de dados, sem precisar de loop Python.

#### Dicas

- `SUM(price * quantity)` calcula a soma de preco vezes quantidade para todos os produtos
- Use `fetchone()` para obter o resultado único
- O resultado pode ser `None` se o banco estiver vazio

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** O valor total deve ser a soma de (preco x quantidade) de todos os produtos
- **Caso de borda:** Com banco vazio, o valor deve ser R$ 0.00

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que calcula o valor total do estoque usando SQL
# "total" = total, "stock" = estoque, "value" = valor
def total_stock_value():
    """Calcula o valor total do estoque usando SQL."""
    # Abrimos a conexao
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # Executamos a consulta com SUM
        # SUM(price * quantity) = soma de (preco vezes quantidade)
        cursor.execute("SELECT SUM(price * quantity) FROM products")
        # Obtemos o resultado unico
        # fetchone() retorna uma tupla com um elemento
        row = cursor.fetchone()

    # O resultado e uma tupla: (valor_total,)
    # Se o banco estiver vazio, o valor sera None
    # "total" = total
    total = row[0]

    # Se for None (banco vazio), usamos 0
    if total is None:
        total = 0.0

    # Exibimos o resultado formatado
    print(f"Valor total do estoque: R$ {total:.2f}")
    return total


# Testamos a funcao
total_stock_value()
```

Saida esperada:
```
Valor total do estoque: R$ 1221.75
```

---

### Exercício 11 — Buscar Produtos com Preco em Faixa

#### Enunciado

Crie uma função `find_by_price_range` que receba um preco mínimo e um preco máximo, e retorne os produtos cujo preco esteja dentro dessa faixa. Use `SELECT * FROM products WHERE price BETWEEN ? AND ?`.

#### Dicas

- `BETWEEN ? AND ?` filtra valores dentro de uma faixa (inclusive)
- Passe os dois valores como tupla no execute
- Retorne uma lista de dicionários

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar entre R$ 5.00 e R$ 15.00 deve retornar os produtos nessa faixa
- **Caso de borda:** Buscar entre R$ 100.00 e R$ 200.00 deve retornar lista vazia

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que busca produtos por faixa de preco
# "find" = encontrar, "by" = por, "price" = preco, "range" = faixa
def find_by_price_range(min_price, max_price):
    """Busca produtos com preco entre min e max."""
    # Abrimos a conexao
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # Consultamos produtos na faixa de preco
        # BETWEEN ? AND ? = entre valor1 e valor2 (inclusive)
        cursor.execute(
            "SELECT * FROM products WHERE price BETWEEN ? AND ?",
            (min_price, max_price)
        )
        rows = cursor.fetchall()

    # Convertemos para lista de dicionarios
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


# Teste 1: faixa com resultados
results = find_by_price_range(5.00, 15.00)
print(f"Produtos entre R$ 5.00 e R$ 15.00: {len(results)}")
for p in results:
    print(f"  [{p['id']}] {p['name']} - R$ {p['price']:.2f}")

# Teste 2: faixa sem resultados
results = find_by_price_range(100.00, 200.00)
print(f"\nProdutos entre R$ 100.00 e R$ 200.00: {len(results)}")
```

Saida esperada:
```
Produtos entre R$ 5.00 e R$ 15.00: 3
  [1] Arroz Integral - R$ 12.50
  [3] Shampoo - R$ 12.75
  [4] Cafe - R$ 15.90

Produtos entre R$ 100.00 e R$ 200.00: 0
```


---

### Exercício 12 — Ordenar Produtos com SQL

#### Enunciado

Crie uma função `list_sorted` que receba o nome do campo para ordenar ("name", "price" ou "quantity") e a direcao ("ASC" para crescente, "DESC" para decrescente). Use `SELECT * FROM products ORDER BY campo direcao`.

#### Dicas

- `ORDER BY name ASC` ordena por nome em ordem crescente
- `ORDER BY price DESC` ordena por preco em ordem decrescente
- Valide o campo e a direcao antes de usar no SQL (não use placeholders para nomes de colunas)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Ordenar por preco crescente deve mostrar o mais barato primeiro
- **Caso de borda:** Ordenar por um campo inválido deve exibir mensagem de erro

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que lista produtos ordenados
# "list" = listar, "sorted" = ordenado
def list_sorted(sort_field="name", sort_direction="ASC"):
    """Lista produtos ordenados pelo campo e direcao informados."""
    # Validamos o campo de ordenacao
    # Campos permitidos para evitar SQL Injection
    # "allowed_fields" = campos permitidos
    allowed_fields = ["name", "price", "quantity", "category"]
    if sort_field not in allowed_fields:
        print(f"Campo invalido: {sort_field}. Use: {allowed_fields}")
        return

    # Validamos a direcao
    # "allowed_directions" = direcoes permitidas
    allowed_directions = ["ASC", "DESC"]
    if sort_direction.upper() not in allowed_directions:
        print(f"Direcao invalida: {sort_direction}. Use: ASC ou DESC")
        return

    # Abrimos a conexao
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # Montamos o SQL com o campo e direcao validados
        # ORDER BY = ordenar por
        # ASC = ascending (crescente), DESC = descending (decrescente)
        sql = f"SELECT * FROM products ORDER BY {sort_field} {sort_direction.upper()}"
        cursor.execute(sql)
        rows = cursor.fetchall()

    # Exibimos os resultados
    if len(rows) == 0:
        print("Nenhum produto cadastrado.")
        return

    print(f"\n--- Ordenado por {sort_field} ({sort_direction.upper()}) ---")
    for row in rows:
        pid, name, price, quantity, category = row
        print(f"  [{pid}] {name} - R$ {price:.2f} - {quantity} un.")


# Teste 1: ordenar por preco crescente
list_sorted("price", "ASC")

# Teste 2: ordenar por nome decrescente
list_sorted("name", "DESC")

# Teste 3: campo invalido
list_sorted("invalido", "ASC")
```

Saida esperada:
```
--- Ordenado por price (ASC) ---
  [5] Detergente - R$ 3.50 - 60 un.
  [1] Arroz Integral - R$ 12.50 - 30 un.
  [3] Shampoo - R$ 12.75 - 25 un.
  [4] Cafe - R$ 15.90 - 20 un.

--- Ordenado por name (DESC) ---
  [3] Shampoo - R$ 12.75 - 25 un.
  [5] Detergente - R$ 3.50 - 60 un.
  [4] Cafe - R$ 15.90 - 20 un.
  [1] Arroz Integral - R$ 12.50 - 30 un.

Campo invalido: invalido. Use: ['name', 'price', 'quantity', 'category']
```

---

### Exercício 13 — Inserir Multiplos Produtos de Uma Vez

#### Enunciado

Crie uma função `insert_many` que receba uma lista de tuplas (nome, preco, quantidade, categoria) e insira todos os produtos de uma vez usando `cursor.executemany()`. Exiba quantos produtos foram inseridos.

#### Dicas

- `executemany()` executa o mesmo SQL para cada tupla da lista
- E mais eficiente que chamar `execute()` em um loop
- Não esqueca do `commit()`

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Inserir 3 produtos de uma vez deve funcionar e exibir "3 produtos inseridos"
- **Caso de borda:** Inserir uma lista vazia deve exibir "0 produtos inseridos"

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que insere multiplos produtos de uma vez
# "insert" = inserir, "many" = muitos
def insert_many(product_list):
    """Insere multiplos produtos usando executemany."""
    # Verificamos se a lista esta vazia
    if len(product_list) == 0:
        print("0 produtos inseridos.")
        return

    # Abrimos a conexao
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # executemany() executa o SQL para cada tupla da lista
        # Cada tupla deve ter: (name, price, quantity, category)
        cursor.executemany(
            "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
            product_list
        )

    # Exibimos quantos produtos foram inseridos
    print(f"{len(product_list)} produto(s) inserido(s)!")


# Teste 1: inserir 3 produtos
# "new_products" = novos produtos
new_products = [
    ("Leite", 5.99, 100, "Alimentos"),
    ("Esponja", 2.50, 200, "Limpeza"),
    ("Condicionador", 18.90, 15, "Higiene")
]
insert_many(new_products)

# Teste 2: lista vazia
insert_many([])
```

Saida esperada:
```
3 produto(s) inserido(s)!
0 produtos inseridos.
```

---

### Exercício 14 — Tratamento de Erros com try/except

#### Enunciado

Crie uma função `safe_insert` que insira um produto no banco com tratamento completo de erros. Capture `sqlite3.IntegrityError` (violacao de restrição), `sqlite3.OperationalError` (erro operacional) e `sqlite3.Error` (qualquer erro genérico).

#### Dicas

- Use `try/except` com tipos específicos de erro do sqlite3
- `IntegrityError` ocorre quando uma restrição e violada (ex: NOT NULL)
- `OperationalError` ocorre quando ha problema com o banco (ex: tabela não existe)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Inserir dados validos deve funcionar normalmente
- **Caso de borda:** Inserir None como nome deve gerar IntegrityError (violacao de NOT NULL)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que insere produto com tratamento de erros
# "safe" = seguro, "insert" = inserir
def safe_insert(name, price, quantity, category):
    """Insere um produto com tratamento completo de erros."""
    try:
        # Tentamos executar a insercao
        with sqlite3.connect("products.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)",
                (name, price, quantity, category)
            )
            product_id = cursor.lastrowid
        # Se chegou aqui, deu certo
        print(f"Produto '{name}' inserido com ID: {product_id}")
        return product_id

    except sqlite3.IntegrityError as error:
        # Erro de integridade (ex: campo NOT NULL com valor None)
        # "integrity" = integridade
        print(f"Erro de integridade: {error}")
        return None

    except sqlite3.OperationalError as error:
        # Erro operacional (ex: tabela nao existe)
        # "operational" = operacional
        print(f"Erro operacional: {error}")
        return None

    except sqlite3.Error as error:
        # Qualquer outro erro do SQLite
        print(f"Erro no banco: {error}")
        return None


# Teste 1: dados validos
safe_insert("Manteiga", 8.50, 30, "Alimentos")

# Teste 2: nome None (viola NOT NULL)
safe_insert(None, 5.0, 10, "Teste")
```

Saida esperada:
```
Produto 'Manteiga' inserido com ID: 9
Erro de integridade: NOT NULL constraint failed: products.name
```

---

### Exercício 15 — Apagar Todos os Produtos

#### Enunciado

Crie uma função `delete_all` que apague todos os registros da tabela `products`. A função deve pedir confirmacao antes de executar e exibir quantos registros foram removidos. Use `DELETE FROM products` (sem WHERE).

#### Dicas

- `DELETE FROM products` sem WHERE apaga todos os registros
- Use `cursor.rowcount` para saber quantos foram apagados
- Peca confirmacao ao usuario antes de executar

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Confirmar a exclusao deve apagar todos os registros e exibir a contagem
- **Caso de borda:** Cancelar a exclusao deve manter os registros intactos

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3


# Funcao que apaga todos os produtos do banco
# "delete" = excluir, "all" = todos
def delete_all():
    """Apaga todos os registros da tabela products."""
    # Pedimos confirmacao ao usuario
    # "confirm" = confirmacao
    confirm = input("ATENCAO: Isso vai apagar TODOS os produtos. Confirma? (s/n): ")

    # Verificamos a confirmacao
    if confirm.lower() != "s":
        print("Operacao cancelada.")
        return 0

    # Executamos a exclusao
    with sqlite3.connect("products.db") as connection:
        cursor = connection.cursor()
        # DELETE FROM products (sem WHERE) apaga tudo
        cursor.execute("DELETE FROM products")
        # Obtemos a quantidade de registros apagados
        # "deleted_count" = quantidade excluida
        deleted_count = cursor.rowcount

    # Exibimos o resultado
    print(f"{deleted_count} produto(s) excluido(s).")
    return deleted_count


# Testamos a funcao
# (o usuario precisara digitar 's' ou 'n')
delete_all()
```

Saida esperada (se confirmar):
```
ATENCAO: Isso vai apagar TODOS os produtos. Confirma? (s/n): s
8 produto(s) excluido(s).
```

---

### Exercício 16 — CRUD Completo com SQLite e Menu

#### Enunciado

Crie o programa CRUD completo com SQLite e menu interativo. O programa deve: criar a tabela ao iniciar, oferecer todas as 5 operações CRUD no menu, usar validação Python antes de cada operação, e tratar erros de entrada do usuario.

#### Dicas

- Chame `create_table()` no inicio da função `main()`
- Reutilize as funções dos exercícios anteriores
- Use `try/except ValueError` para tratar entradas não numericas
- Use `with` para gerenciar conexões

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Cadastre 2 produtos, liste, busque por ID, atualize, exclua e liste novamente
- **Caso de borda:** Feche o programa, abra novamente e liste — os dados devem estar la (persistência)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
import sqlite3

# Nome do arquivo do banco de dados
DATABASE_FILE = "products.db"


def create_table():
    """Cria a tabela products se nao existir."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                category TEXT NOT NULL
            )
        """)


def validate_data(name, price, quantity, category):
    """Valida os dados e retorna lista de erros."""
    errors = []
    if not name or name.strip() == "":
        errors.append("Nome nao pode ser vazio")
    if not isinstance(price, (int, float)) or price < 0:
        errors.append("Preco invalido")
    if not isinstance(quantity, int) or quantity < 0:
        errors.append("Quantidade invalida")
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    return errors


def create_product(name, price, quantity, category):
    """Insere um produto no banco."""
    errors = validate_data(name, price, quantity, category)
    if errors:
        for e in errors:
            print(f"  Erro: {e}")
        return None
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)", (name, price, quantity, category))
        pid = cursor.lastrowid
    print(f"Cadastrado: {name} (ID {pid})")
    return pid


def list_products():
    """Lista todos os produtos."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
    if not rows:
        print("Nenhum produto.")
        return
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)
    for r in rows:
        print(f"{r[0]:<5} {r[1]:<20} {r[2]:>10.2f} {r[3]:>5} {r[4]:<15}")
    print(f"\nTotal: {len(rows)}")


def find_by_id(product_id):
    """Busca produto por ID."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "price": row[2], "quantity": row[3], "category": row[4]}


def update_product(pid, name, price, quantity, category):
    """Atualiza produto no banco."""
    errors = validate_data(name, price, quantity, category)
    if errors:
        for e in errors:
            print(f"  Erro: {e}")
        return False
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET name=?, price=?, quantity=?, category=? WHERE id=?", (name, price, quantity, category, pid))
        if cursor.rowcount == 0:
            print("Nao encontrado.")
            return False
    print(f"Atualizado ID {pid}!")
    return True


def delete_product(pid):
    """Exclui produto do banco."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (pid,))
        if cursor.rowcount == 0:
            print("Nao encontrado.")
            return False
    print(f"Excluido ID {pid}!")
    return True


def read_input():
    """Le dados do usuario."""
    name = input("Nome: ")
    try:
        price = float(input("Preco: "))
    except ValueError:
        print("Preco invalido.")
        return None
    try:
        qty = int(input("Quantidade: "))
    except ValueError:
        print("Quantidade invalida.")
        return None
    cat = input("Categoria: ")
    return name, price, qty, cat


def main():
    """Funcao principal."""
    create_table()
    print("=== CRUD SQLite ===")
    while True:
        print("\n1-Cadastrar 2-Listar 3-Buscar 4-Atualizar 5-Excluir 0-Sair")
        choice = input("Opcao: ")
        if choice == "1":
            data = read_input()
            if data:
                create_product(*data)
        elif choice == "2":
            list_products()
        elif choice == "3":
            try:
                pid = int(input("ID: "))
            except ValueError:
                print("ID invalido.")
                continue
            p = find_by_id(pid)
            if p:
                print(f"  {p['name']} - R$ {p['price']:.2f} - {p['quantity']} un. - {p['category']}")
            else:
                print("Nao encontrado.")
        elif choice == "4":
            try:
                pid = int(input("ID: "))
            except ValueError:
                print("ID invalido.")
                continue
            p = find_by_id(pid)
            if not p:
                print("Nao encontrado.")
                continue
            print(f"Atual: {p['name']} - R$ {p['price']:.2f}")
            data = read_input()
            if data:
                update_product(pid, *data)
        elif choice == "5":
            try:
                pid = int(input("ID: "))
            except ValueError:
                print("ID invalido.")
                continue
            p = find_by_id(pid)
            if not p:
                print("Nao encontrado.")
                continue
            if input(f"Excluir '{p['name']}'? (s/n): ").lower() == "s":
                delete_product(pid)
        elif choice == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
```

Saida esperada (inicio):
```
=== CRUD SQLite ===

1-Cadastrar 2-Listar 3-Buscar 4-Atualizar 5-Excluir 0-Sair
Opcao: 
```