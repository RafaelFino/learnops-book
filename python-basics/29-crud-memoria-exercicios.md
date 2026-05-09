# 29 — Exercícios: CRUD em Memória

[<- Voltar para o módulo](29-crud-memória.md) | [Glossário](00-glossário.md)

---

> **Antes de começar:** Estes exercícios constroem progressivamente um sistema CRUD completo. Os primeiros exercícios focam em funções individuais, e os ultimos combinam tudo em programas completos. Tente resolver cada exercício sozinho antes de consultar a resposta.

---

### Exercício 1 — Criar um Produto Simples

#### Enunciado

Crie uma função chamada `create_product` que receba nome, preco, quantidade e categoria, e retorne um dicionário representando o produto. Use um contador global para gerar o ID automaticamente. Crie 3 produtos e exiba cada um.

#### Dicas

- Use uma variável global `next_id` iniciando em 1
- A função deve montar o dicionário e incrementar o contador
- Use `global next_id` dentro da função para modificar a variável externa

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** O primeiro produto deve ter id 1, o segundo id 2 e o terceiro id 3
- **Caso de borda:** Crie um quarto produto e verifique se o id e 4

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Contador global para gerar identificadores unicos
# "next_id" = proximo identificador
next_id = 1


# Funcao que cria um dicionario de produto com id automatico
# "create" = criar, "product" = produto
def create_product(name, price, quantity, category):
    """Cria e retorna um dicionario representando um produto."""
    # Acessamos a variavel global para modificar o contador
    global next_id
    # Montamos o dicionario do produto
    # "product" = produto
    product = {
        "id": next_id,              # Identificador unico (id = identificador)
        "name": name,               # Nome do produto (name = nome)
        "price": price,             # Preco do produto (price = preco)
        "quantity": quantity,       # Quantidade em estoque (quantity = quantidade)
        "category": category        # Categoria do produto (category = categoria)
    }
    # Incrementamos o contador para o proximo produto
    next_id = next_id + 1
    # Retornamos o dicionario pronto
    return product


# Criamos 3 produtos usando a funcao
# "product" = produto
product_1 = create_product("Arroz", 8.99, 50, "Alimentos")
product_2 = create_product("Sabao", 4.50, 80, "Limpeza")
product_3 = create_product("Shampoo", 12.75, 25, "Higiene")

# Exibimos cada produto
# print() mostra o texto no terminal
print(f"Produto 1: {product_1}")
print(f"Produto 2: {product_2}")
print(f"Produto 3: {product_3}")
```

Saida esperada:
```
Produto 1: {'id': 1, 'name': 'Arroz', 'price': 8.99, 'quantity': 50, 'category': 'Alimentos'}
Produto 2: {'id': 2, 'name': 'Sabao', 'price': 4.5, 'quantity': 80, 'category': 'Limpeza'}
Produto 3: {'id': 3, 'name': 'Shampoo', 'price': 12.75, 'quantity': 25, 'category': 'Higiene'}
```

---

### Exercício 2 — Validação de Dados do Produto

#### Enunciado

Crie uma função `validate_product_data` que receba nome, preco, quantidade e categoria, e retorne uma lista de mensagens de erro. Se a lista estiver vazia, os dados sao validos. Teste com dados validos e com dados que tenham multiplos erros.

#### Dicas

- Crie uma lista vazia para armazenar os erros
- Verifique: nome não vazio, preco numerico e >= 0, quantidade inteira e >= 0, categoria não vazia
- Use `isinstance()` para verificar tipos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com dados validos ("Arroz", 8.99, 50, "Alimentos"), a lista de erros deve estar vazia
- **Caso de borda:** Com dados invalidos ("", -1, -5, ""), a lista deve conter 4 mensagens de erro

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que valida os dados de um produto
# "validate" = validar, "product" = produto, "data" = dados
def validate_product_data(name, price, quantity, category):
    """Valida os dados de um produto e retorna lista de erros."""
    # Lista para armazenar mensagens de erro
    # "errors" = erros
    errors = []

    # Validacao do nome: nao pode ser vazio nem so espacos
    # strip() remove espacos em branco das pontas
    if not name or name.strip() == "":
        errors.append("Nome nao pode ser vazio")

    # Validacao do preco: deve ser numero e nao negativo
    # isinstance() verifica se o valor e do tipo esperado
    if not isinstance(price, (int, float)):
        errors.append("Preco deve ser um numero")
    elif price < 0:
        errors.append("Preco nao pode ser negativo")

    # Validacao da quantidade: deve ser inteiro e nao negativo
    if not isinstance(quantity, int):
        errors.append("Quantidade deve ser um numero inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")

    # Validacao da categoria: nao pode ser vazia
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")

    # Retornamos a lista de erros (vazia = tudo valido)
    return errors


# Teste 1: dados validos
# "errors" = erros
errors = validate_product_data("Arroz", 8.99, 50, "Alimentos")
# Exibimos o resultado
print(f"Teste valido: {len(errors)} erros -> {errors}")

# Teste 2: todos os dados invalidos
errors = validate_product_data("", -1, -5, "")
# Exibimos o resultado e cada erro
print(f"Teste invalido: {len(errors)} erros")
# Percorremos cada mensagem de erro
for error in errors:
    print(f"  - {error}")
```

Saida esperada:
```
Teste valido: 0 erros -> []
Teste invalido: 4 erros
  - Nome nao pode ser vazio
  - Preco nao pode ser negativo
  - Quantidade nao pode ser negativa
  - Categoria nao pode ser vazia
```


---

### Exercício 3 — Cadastrar com Validação

#### Enunciado

Combine as funções dos exercícios 1 e 2: crie uma função `add_product` que valide os dados antes de cadastrar. Se os dados forem invalidos, exiba os erros e retorne `None`. Se forem validos, adicione o produto a uma lista global e retorne o produto. Tente cadastrar 3 produtos validos e 1 inválido.

#### Dicas

- Use uma lista global `products` para armazenar os produtos
- Chame `validate_product_data` antes de criar o produto
- Se houver erros, exiba-os e retorne None sem adicionar a lista

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Apos cadastrar 3 validos e 1 inválido, a lista deve conter exatamente 3 produtos
- **Caso de borda:** O produto inválido não deve aparecer na lista, e os IDs devem ser 1, 2 e 3

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista global que armazena todos os produtos
# "products" = produtos
products = []
# Contador global para gerar ids unicos
# "next_id" = proximo identificador
next_id = 1


# Funcao de validacao (mesma do exercicio 2)
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
        errors.append("Quantidade deve ser um numero inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    return errors


# Funcao que adiciona um produto validado a lista
# "add" = adicionar, "product" = produto
def add_product(name, price, quantity, category):
    """Adiciona um produto a lista se os dados forem validos."""
    # Acessamos a variavel global
    global next_id
    # Validamos os dados
    # "errors" = erros
    errors = validate_product_data(name, price, quantity, category)
    # Se houver erros, exibimos e retornamos None
    if len(errors) > 0:
        print(f"Erro ao cadastrar '{name}': {errors}")
        return None
    # Criamos o dicionario do produto
    # "product" = produto
    product = {
        "id": next_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    # Adicionamos a lista global
    products.append(product)
    # Incrementamos o contador
    next_id = next_id + 1
    # Informamos o sucesso
    print(f"Produto '{name}' cadastrado com ID {product['id']}")
    # Retornamos o produto criado
    return product


# Cadastramos 3 produtos validos e 1 invalido
add_product("Arroz", 8.99, 50, "Alimentos")
add_product("Sabao", 4.50, 80, "Limpeza")
add_product("", -3.00, -1, "")  # Invalido — sera rejeitado
add_product("Shampoo", 12.75, 25, "Higiene")

# Exibimos a lista final
print(f"\nTotal de produtos: {len(products)}")
# Percorremos cada produto para exibir
for product in products:
    print(f"  [{product['id']}] {product['name']} - R$ {product['price']:.2f}")
```

Saida esperada:
```
Produto 'Arroz' cadastrado com ID 1
Produto 'Sabao' cadastrado com ID 2
Erro ao cadastrar '': ['Nome nao pode ser vazio', 'Preco nao pode ser negativo', 'Quantidade nao pode ser negativa', 'Categoria nao pode ser vazia']
Produto 'Shampoo' cadastrado com ID 3

Total de produtos: 3
  [1] Arroz - R$ 8.99
  [2] Sabao - R$ 4.50
  [3] Shampoo - R$ 12.75
```

---

### Exercício 4 — Listar Produtos em Formato de Tabela

#### Enunciado

Crie uma função `list_products` que exiba todos os produtos em formato de tabela com colunas alinhadas. A função deve mostrar uma mensagem se a lista estiver vazia. Use os especificadores de formatacao `:<`, `:>` e `:.2f` para alinhar as colunas.

#### Dicas

- Use `:<20` para alinhar texto a esquerda com 20 caracteres
- Use `:>10` para alinhar números a direita com 10 caracteres
- Use `:.2f` para formatar precos com 2 casas decimais
- Verifique se a lista esta vazia antes de exibir a tabela

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com 3 produtos cadastrados, a tabela deve mostrar 3 linhas de dados com colunas alinhadas
- **Caso de borda:** Com a lista vazia, deve exibir "Nenhum produto cadastrado."

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos ja cadastrados (simulando dados existentes)
# "products" = produtos
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que lista todos os produtos em formato de tabela
# "list" = listar, "products" = produtos
def list_products(product_list):
    """Exibe todos os produtos em formato de tabela."""
    # Verificamos se a lista esta vazia
    if len(product_list) == 0:
        print("Nenhum produto cadastrado.")
        return
    # Exibimos o cabecalho da tabela
    # :<5 alinha a esquerda com 5 caracteres de largura
    # :<20 alinha a esquerda com 20 caracteres
    # :>10 alinha a direita com 10 caracteres
    print(f"{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    # Exibimos uma linha separadora
    print("-" * 60)
    # Percorremos cada produto na lista
    # "product" = produto
    for product in product_list:
        # Exibimos os dados formatados em colunas
        # :.2f formata o numero com 2 casas decimais
        print(f"{product['id']:<5} {product['name']:<20} {product['price']:>10.2f} {product['quantity']:>5} {product['category']:<15}")
    # Exibimos o total de produtos
    print(f"\nTotal: {len(product_list)} produto(s)")


# Teste 1: lista com produtos
print("--- Lista com produtos ---")
list_products(products)

# Teste 2: lista vazia
print("\n--- Lista vazia ---")
list_products([])
```

Saida esperada:
```
--- Lista com produtos ---
ID    Nome                     Preco   Qtd Categoria
------------------------------------------------------------
1     Arroz                     8.99    50 Alimentos
2     Sabao                     4.50    80 Limpeza
3     Shampoo                  12.75    25 Higiene

Total: 3 produto(s)

--- Lista vazia ---
Nenhum produto cadastrado.
```

---

### Exercício 5 — Buscar Produto por ID

#### Enunciado

Crie uma função `find_by_id` que receba um ID e retorne o dicionário do produto correspondente, ou `None` se não encontrar. Teste buscando um ID existente e um inexistente.

#### Dicas

- Percorra a lista com um loop `for`
- Compare o id de cada produto com o id buscado
- Se encontrar, retorne imediatamente com `return`
- Se o loop terminar sem encontrar, retorne `None`

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar id 2 deve retornar o produto "Sabao"
- **Caso de borda:** Buscar id 99 deve retornar None

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
# "products" = produtos
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que busca um produto pelo identificador
# "find" = encontrar, "by" = por, "id" = identificador
def find_by_id(product_id):
    """Busca um produto pelo ID e retorna o dicionario ou None."""
    # Percorremos cada produto na lista
    # "product" = produto
    for product in products:
        # Comparamos o id do produto com o id buscado
        if product["id"] == product_id:
            # Encontramos — retornamos o produto imediatamente
            return product
    # Se o loop terminou sem encontrar, retornamos None
    return None


# Teste 1: buscar id existente
# "found" = encontrado
found = find_by_id(2)
# Verificamos se encontrou
if found is not None:
    print(f"Encontrado: {found['name']} - R$ {found['price']:.2f}")
else:
    print("Produto nao encontrado")

# Teste 2: buscar id inexistente
found = find_by_id(99)
# Verificamos se encontrou
if found is not None:
    print(f"Encontrado: {found['name']}")
else:
    print("Produto nao encontrado")
```

Saida esperada:
```
Encontrado: Sabao - R$ 4.50
Produto nao encontrado
```


---

### Exercício 6 — Atualizar Produto

#### Enunciado

Crie uma função `update_product` que receba o ID do produto e os novos dados (nome, preco, quantidade, categoria). A função deve buscar o produto, validar os novos dados e atualizar os campos. Retorne `True` se atualizou com sucesso ou `False` se falhou.

#### Dicas

- Use `find_by_id` para buscar o produto
- Use `validate_product_data` para validar os novos dados
- Como dicionários sao mutaveis, alterar o dicionário encontrado altera o item na lista

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Atualizar o produto com ID 1 para novos dados deve funcionar e exibir os dados atualizados
- **Caso de borda:** Tentar atualizar um ID inexistente (99) deve retornar False

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"}
]


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
        errors.append("Quantidade deve ser um numero inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    return errors


def find_by_id(product_id):
    """Busca um produto pelo ID."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Funcao que atualiza os dados de um produto existente
# "update" = atualizar, "product" = produto
def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto existente."""
    # Buscamos o produto pelo ID
    # "product" = produto
    product = find_by_id(product_id)
    # Verificamos se o produto foi encontrado
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    # Validamos os novos dados
    # "errors" = erros
    errors = validate_product_data(name, price, quantity, category)
    # Se houver erros, exibimos e nao atualizamos
    if len(errors) > 0:
        print(f"Erro ao atualizar: {errors}")
        return False
    # Atualizamos os campos do produto
    # Como o dicionario e mutavel, as alteracoes refletem na lista
    product["name"] = name
    product["price"] = price
    product["quantity"] = quantity
    product["category"] = category
    # Informamos o sucesso
    print(f"Produto ID {product_id} atualizado com sucesso!")
    return True


# Teste 1: atualizar produto existente
print("Antes:", products[0])
# Atualizamos o Arroz para Arroz Integral com novo preco
result = update_product(1, "Arroz Integral", 12.50, 30, "Alimentos")
print(f"Resultado: {result}")
print("Depois:", products[0])

# Teste 2: atualizar produto inexistente
print()
result = update_product(99, "Teste", 1.0, 1, "Teste")
print(f"Resultado: {result}")
```

Saida esperada:
```
Antes: {'id': 1, 'name': 'Arroz', 'price': 8.99, 'quantity': 50, 'category': 'Alimentos'}
Produto ID 1 atualizado com sucesso!
Resultado: True
Depois: {'id': 1, 'name': 'Arroz Integral', 'price': 12.5, 'quantity': 30, 'category': 'Alimentos'}

Produto com ID 99 nao encontrado.
Resultado: False
```

---

### Exercício 7 — Excluir Produto

#### Enunciado

Crie uma função `delete_product` que receba o ID do produto, busque na lista e remova. Retorne `True` se excluiu com sucesso ou `False` se o produto não foi encontrado. Exiba a lista antes e depois da exclusao.

#### Dicas

- Use `find_by_id` para buscar o produto
- Use `products.remove(product)` para remover o dicionário da lista
- Guarde o nome do produto antes de remover para exibir na mensagem

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Excluir o produto com ID 2 deve remover "Sabao" da lista
- **Caso de borda:** Tentar excluir ID 99 deve retornar False e a lista deve permanecer inalterada

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


def find_by_id(product_id):
    """Busca um produto pelo ID."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Funcao que exclui um produto da lista
# "delete" = excluir, "product" = produto
def delete_product(product_id):
    """Remove um produto da lista pelo ID."""
    # Buscamos o produto pelo ID
    product = find_by_id(product_id)
    # Verificamos se o produto foi encontrado
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    # Guardamos o nome antes de remover
    # "product_name" = nome do produto
    product_name = product["name"]
    # Removemos o produto da lista
    # remove() encontra e remove o item da lista
    products.remove(product)
    # Informamos o sucesso
    print(f"Produto '{product_name}' (ID {product_id}) excluido!")
    return True


# Exibimos a lista antes da exclusao
print(f"Antes: {len(products)} produtos")
for p in products:
    print(f"  [{p['id']}] {p['name']}")

# Teste 1: excluir produto existente
print()
result = delete_product(2)
print(f"Resultado: {result}")

# Exibimos a lista apos a exclusao
print(f"\nDepois: {len(products)} produtos")
for p in products:
    print(f"  [{p['id']}] {p['name']}")

# Teste 2: excluir produto inexistente
print()
result = delete_product(99)
print(f"Resultado: {result}")
```

Saida esperada:
```
Antes: 3 produtos
  [1] Arroz
  [2] Sabao
  [3] Shampoo

Produto 'Sabao' (ID 2) excluido!
Resultado: True

Depois: 2 produtos
  [1] Arroz
  [3] Shampoo

Produto com ID 99 nao encontrado.
Resultado: False
```

---

### Exercício 8 — Filtrar Produtos por Categoria

#### Enunciado

Crie uma função `filter_by_category` que receba uma categoria e retorne uma nova lista contendo apenas os produtos daquela categoria. A comparação deve ignorar maiusculas e minusculas.

#### Dicas

- Crie uma lista vazia para armazenar os produtos filtrados
- Use `lower()` para comparar categorias sem diferenciar maiusculas/minusculas
- Retorne a lista filtrada (pode estar vazia se nenhum produto corresponder)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Filtrar por "Alimentos" deve retornar os produtos dessa categoria
- **Caso de borda:** Filtrar por "Eletronicos" (inexistente) deve retornar lista vazia

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Feijao", "price": 7.50, "quantity": 40, "category": "Alimentos"},
    {"id": 3, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 4, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que filtra produtos por categoria
# "filter" = filtrar, "by" = por, "category" = categoria
def filter_by_category(category):
    """Retorna uma lista de produtos da categoria informada."""
    # Lista para armazenar os produtos filtrados
    # "filtered" = filtrados
    filtered = []
    # Percorremos cada produto na lista
    for product in products:
        # Comparamos as categorias ignorando maiusculas/minusculas
        # lower() converte o texto para minusculas
        if product["category"].lower() == category.lower():
            # O produto pertence a categoria — adicionamos
            filtered.append(product)
    # Retornamos a lista filtrada
    return filtered


# Teste 1: categoria existente
# "result" = resultado
result = filter_by_category("Alimentos")
print(f"Alimentos: {len(result)} produto(s)")
# Exibimos cada produto encontrado
for product in result:
    print(f"  - {product['name']}")

# Teste 2: categoria inexistente
result = filter_by_category("Eletronicos")
print(f"Eletronicos: {len(result)} produto(s)")

# Teste 3: categoria com maiusculas diferentes
result = filter_by_category("alimentos")
print(f"alimentos (minusculo): {len(result)} produto(s)")
```

Saida esperada:
```
Alimentos: 2 produto(s)
  - Arroz
  - Feijao
Eletronicos: 0 produto(s)
alimentos (minusculo): 2 produto(s)
```


---

### Exercício 9 — Calcular Valor Total do Estoque

#### Enunciado

Crie uma função `calculate_stock_value` que percorra a lista de produtos e calcule o valor total do estoque (preco multiplicado pela quantidade de cada produto). Exiba o valor de cada produto e o total geral.

#### Dicas

- O valor de estoque de um produto e: preco vezes quantidade
- Use um acumulador para somar os valores
- Formate os valores com `:.2f` para 2 casas decimais

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com Arroz (8.99 x 50 = 449.50), Sabao (4.50 x 80 = 360.00) e Shampoo (12.75 x 25 = 318.75), o total deve ser R$ 1128.25
- **Caso de borda:** Com lista vazia, o total deve ser R$ 0.00

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que calcula o valor total do estoque
# "calculate" = calcular, "stock" = estoque, "value" = valor
def calculate_stock_value(product_list):
    """Calcula e retorna o valor total do estoque."""
    # Acumulador para somar o valor total
    # "total" = total
    total = 0
    # Percorremos cada produto na lista
    for product in product_list:
        # Calculamos o valor de estoque deste produto
        # Valor = preco (price) multiplicado pela quantidade (quantity)
        # "item_value" = valor do item
        item_value = product["price"] * product["quantity"]
        # Exibimos o valor deste produto
        print(f"  {product['name']}: R$ {product['price']:.2f} x {product['quantity']} = R$ {item_value:.2f}")
        # Somamos ao total
        total = total + item_value
    # Retornamos o valor total
    return total


# Teste 1: lista com produtos
print("Valor do estoque:")
# "total" = total
total = calculate_stock_value(products)
print(f"  TOTAL: R$ {total:.2f}")

# Teste 2: lista vazia
print("\nEstoque vazio:")
total = calculate_stock_value([])
print(f"  TOTAL: R$ {total:.2f}")
```

Saida esperada:
```
Valor do estoque:
  Arroz: R$ 8.99 x 50 = R$ 449.50
  Sabao: R$ 4.50 x 80 = R$ 360.00
  Shampoo: R$ 12.75 x 25 = R$ 318.75
  TOTAL: R$ 1128.25

Estoque vazio:
  TOTAL: R$ 0.00
```

---

### Exercício 10 — Menu Interativo Simples

#### Enunciado

Crie um menu interativo com as opcoes: 1-Cadastrar, 2-Listar, 0-Sair. Use um loop `while True` que so para quando o usuario digitar "0". Implemente apenas as opcoes de cadastrar e listar (as outras serao adicionadas nos proximos exercícios).

#### Dicas

- Use `while True` para manter o programa rodando
- Use `input()` para ler a opcao do usuario
- Use `if/elif/else` para executar a opcao escolhida
- Use `break` para sair do loop quando o usuario digitar "0"

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Cadastre 2 produtos (opcao 1), liste (opcao 2) e saia (opcao 0)
- **Caso de borda:** Digite uma opcao inválida (como "9") — o programa deve informar que a opcao e inválida e mostrar o menu novamente

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista global de produtos e contador de IDs
products = []
next_id = 1


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


def create_product(name, price, quantity, category):
    """Cadastra um novo produto apos validar os dados."""
    global next_id
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao cadastrar:")
        for error in errors:
            print(f"  - {error}")
        return None
    product = {"id": next_id, "name": name, "price": price, "quantity": quantity, "category": category}
    products.append(product)
    next_id = next_id + 1
    print(f"Produto '{name}' cadastrado! ID: {product['id']}")
    return product


def list_products():
    """Exibe todos os produtos cadastrados."""
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)
    for product in products:
        print(f"{product['id']:<5} {product['name']:<20} {product['price']:>10.2f} {product['quantity']:>5} {product['category']:<15}")
    print(f"\nTotal: {len(products)} produto(s)")


# Funcao que exibe o menu de opcoes
# "show" = mostrar, "menu" = menu
def show_menu():
    """Exibe o menu principal."""
    print("\n=== CADASTRO DE PRODUTOS ===")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("0. Sair")
    print("============================")


# Funcao principal com o loop do menu
# "main" = principal
def main():
    """Funcao principal que executa o loop do menu."""
    print("Bem-vindo ao Cadastro de Produtos!")
    # Loop infinito — so para com break
    while True:
        # Exibimos o menu
        show_menu()
        # Lemos a opcao do usuario
        # "choice" = escolha
        choice = input("Escolha uma opcao: ")
        # Executamos a opcao escolhida
        if choice == "1":
            # Opcao cadastrar
            print("\n--- Cadastrar Produto ---")
            # Lemos os dados do usuario
            name = input("Nome: ")
            try:
                price = float(input("Preco: "))
            except ValueError:
                print("Preco invalido.")
                continue
            try:
                quantity = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade invalida.")
                continue
            category = input("Categoria: ")
            # Chamamos a funcao de criacao
            create_product(name, price, quantity, category)
        elif choice == "2":
            # Opcao listar
            list_products()
        elif choice == "0":
            # Opcao sair
            print("Ate a proxima!")
            break
        else:
            # Opcao invalida
            print("Opcao invalida. Tente novamente.")


# Executamos a funcao principal
if __name__ == "__main__":
    main()
```

Saida esperada (exemplo de interação):
```
Bem-vindo ao Cadastro de Produtos!

=== CADASTRO DE PRODUTOS ===
1. Cadastrar produto
2. Listar produtos
0. Sair
============================
Escolha uma opcao: 1

--- Cadastrar Produto ---
Nome: Arroz
Preco: 8.99
Quantidade: 50
Categoria: Alimentos
Produto 'Arroz' cadastrado! ID: 1

=== CADASTRO DE PRODUTOS ===
1. Cadastrar produto
2. Listar produtos
0. Sair
============================
Escolha uma opcao: 2

ID    Nome                     Preco   Qtd Categoria
------------------------------------------------------------
1     Arroz                     8.99    50 Alimentos

Total: 1 produto(s)

=== CADASTRO DE PRODUTOS ===
1. Cadastrar produto
2. Listar produtos
0. Sair
============================
Escolha uma opcao: 0
Ate a proxima!
```


---

### Exercício 11 — Menu Completo com Todas as Operações CRUD

#### Enunciado

Expanda o menu do exercício anterior para incluir todas as operações: 1-Cadastrar, 2-Listar, 3-Buscar por ID, 4-Atualizar, 5-Excluir, 0-Sair. Implemente cada opcao com tratamento de erros para entradas invalidas.

#### Dicas

- Reutilize as funções dos exercícios anteriores
- Para buscar, atualizar e excluir, peca o ID ao usuario com `int(input(...))`
- Use `try/except ValueError` para tratar IDs não numericos
- Na exclusao, peca confirmacao antes de remover

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Cadastre 2 produtos, liste, busque por ID 1, atualize o ID 1, liste novamente, exclua o ID 2, liste para confirmar
- **Caso de borda:** Tente buscar ID 99 (não encontrado), tente atualizar com preco negativo (erro de validação), digite "abc" quando pedir ID (erro de conversão)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista global de produtos e contador de IDs
products = []
next_id = 1


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


def create_product(name, price, quantity, category):
    """Cadastra um novo produto."""
    global next_id
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao cadastrar:")
        for error in errors:
            print(f"  - {error}")
        return None
    product = {"id": next_id, "name": name, "price": price, "quantity": quantity, "category": category}
    products.append(product)
    next_id = next_id + 1
    print(f"Produto '{name}' cadastrado! ID: {product['id']}")
    return product


def list_products():
    """Exibe todos os produtos."""
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)
    for product in products:
        print(f"{product['id']:<5} {product['name']:<20} {product['price']:>10.2f} {product['quantity']:>5} {product['category']:<15}")
    print(f"\nTotal: {len(products)} produto(s)")


def find_by_id(product_id):
    """Busca um produto pelo ID."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto."""
    product = find_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao atualizar:")
        for error in errors:
            print(f"  - {error}")
        return False
    product["name"] = name
    product["price"] = price
    product["quantity"] = quantity
    product["category"] = category
    print(f"Produto ID {product_id} atualizado!")
    return True


def delete_product(product_id):
    """Remove um produto da lista."""
    product = find_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    product_name = product["name"]
    products.remove(product)
    print(f"Produto '{product_name}' (ID {product_id}) excluido!")
    return True


# Funcao que le os dados de um produto do teclado
# "read" = ler, "input" = entrada
def read_product_input():
    """Le os dados de um produto do usuario."""
    # Pedimos cada campo
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
    # Retornamos como tupla
    return name, price, quantity, category


# Funcao principal com menu completo
def main():
    """Funcao principal com loop do menu."""
    print("=== Sistema de Cadastro de Produtos ===")
    # Loop principal
    while True:
        # Menu de opcoes
        print("\n1-Cadastrar  2-Listar  3-Buscar  4-Atualizar  5-Excluir  0-Sair")
        choice = input("Opcao: ")

        if choice == "1":
            # Cadastrar produto
            print("\n--- Cadastrar ---")
            data = read_product_input()
            if data is not None:
                name, price, quantity, category = data
                create_product(name, price, quantity, category)

        elif choice == "2":
            # Listar produtos
            list_products()

        elif choice == "3":
            # Buscar por ID
            print("\n--- Buscar ---")
            try:
                product_id = int(input("ID: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_by_id(product_id)
            if product is None:
                print("Produto nao encontrado.")
            else:
                print(f"  ID: {product['id']}")
                print(f"  Nome: {product['name']}")
                print(f"  Preco: R$ {product['price']:.2f}")
                print(f"  Quantidade: {product['quantity']}")
                print(f"  Categoria: {product['category']}")

        elif choice == "4":
            # Atualizar produto
            print("\n--- Atualizar ---")
            try:
                product_id = int(input("ID do produto: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_by_id(product_id)
            if product is None:
                print("Produto nao encontrado.")
                continue
            print(f"Dados atuais: {product['name']} - R$ {product['price']:.2f}")
            print("Novos dados:")
            data = read_product_input()
            if data is not None:
                name, price, quantity, category = data
                update_product(product_id, name, price, quantity, category)

        elif choice == "5":
            # Excluir produto
            print("\n--- Excluir ---")
            try:
                product_id = int(input("ID do produto: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_by_id(product_id)
            if product is None:
                print("Produto nao encontrado.")
                continue
            # Pedimos confirmacao
            confirm = input(f"Excluir '{product['name']}'? (s/n): ")
            if confirm.lower() == "s":
                delete_product(product_id)
            else:
                print("Exclusao cancelada.")

        elif choice == "0":
            # Sair
            print("Ate a proxima!")
            break

        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
```

Saida esperada (exemplo resumido de interação):
```
=== Sistema de Cadastro de Produtos ===

1-Cadastrar  2-Listar  3-Buscar  4-Atualizar  5-Excluir  0-Sair
Opcao: 1

--- Cadastrar ---
Nome: Arroz
Preco: 8.99
Quantidade: 50
Categoria: Alimentos
Produto 'Arroz' cadastrado! ID: 1

1-Cadastrar  2-Listar  3-Buscar  4-Atualizar  5-Excluir  0-Sair
Opcao: 0
Ate a proxima!
```


---

### Exercício 12 — Buscar Produto por Nome

#### Enunciado

Crie uma função `search_by_name` que receba um texto de busca e retorne uma lista de produtos cujo nome contenha esse texto (busca parcial). A busca deve ignorar maiusculas e minusculas.

#### Dicas

- Use `in` para verificar se o texto de busca esta contido no nome do produto
- Use `lower()` em ambos os textos para ignorar maiusculas/minusculas
- Retorne uma lista com todos os produtos que correspondem

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar "arr" deve encontrar "Arroz"
- **Caso de borda:** Buscar "xyz" deve retornar lista vazia

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz Branco", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Arroz Integral", "price": 12.50, "quantity": 30, "category": "Alimentos"},
    {"id": 3, "name": "Sabao em Po", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 4, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que busca produtos pelo nome (busca parcial)
# "search" = buscar, "by" = por, "name" = nome
def search_by_name(search_text):
    """Busca produtos cujo nome contenha o texto informado."""
    # Lista para armazenar os resultados
    # "results" = resultados
    results = []
    # Percorremos cada produto na lista
    for product in products:
        # Verificamos se o texto de busca esta contido no nome
        # lower() converte para minusculas para ignorar maiusculas
        # "in" verifica se um texto esta dentro de outro
        if search_text.lower() in product["name"].lower():
            # O produto corresponde — adicionamos aos resultados
            results.append(product)
    # Retornamos a lista de resultados
    return results


# Teste 1: busca parcial que encontra resultados
# "results" = resultados
results = search_by_name("arroz")
print(f"Busca 'arroz': {len(results)} resultado(s)")
for product in results:
    print(f"  [{product['id']}] {product['name']}")

# Teste 2: busca que nao encontra nada
results = search_by_name("xyz")
print(f"\nBusca 'xyz': {len(results)} resultado(s)")

# Teste 3: busca com uma letra
results = search_by_name("s")
print(f"\nBusca 's': {len(results)} resultado(s)")
for product in results:
    print(f"  [{product['id']}] {product['name']}")
```

Saida esperada:
```
Busca 'arroz': 2 resultado(s)
  [1] Arroz Branco
  [2] Arroz Integral

Busca 'xyz': 0 resultado(s)

Busca 's': 2 resultado(s)
  [3] Sabao em Po
  [4] Shampoo
```

---

### Exercício 13 — Ordenar Produtos por Preco

#### Enunciado

Crie uma função `sort_by_price` que receba a lista de produtos e um parametro `ascending` (booleano). Se `ascending` for `True`, ordene do menor para o maior preco. Se for `False`, ordene do maior para o menor. Retorne uma nova lista ordenada sem modificar a original.

#### Dicas

- Use a função `sorted()` que retorna uma nova lista ordenada
- Use o parametro `key` para indicar qual campo usar na ordenação
- Use o parametro `reverse` para inverter a ordem
- Não modifique a lista original

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Ordenar crescente deve mostrar o produto mais barato primeiro
- **Caso de borda:** Ordenar decrescente deve mostrar o produto mais caro primeiro

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"},
    {"id": 4, "name": "Feijao", "price": 7.50, "quantity": 40, "category": "Alimentos"}
]


# Funcao que ordena produtos por preco
# "sort" = ordenar, "by" = por, "price" = preco
def sort_by_price(product_list, ascending=True):
    """Retorna uma nova lista de produtos ordenada por preco."""
    # sorted() retorna uma nova lista ordenada
    # key= indica qual valor usar para ordenar
    # lambda e uma funcao anonima que extrai o preco de cada produto
    # reverse=True inverte a ordem (maior para menor)
    # "sorted_list" = lista ordenada
    sorted_list = sorted(
        product_list,
        key=lambda product: product["price"],
        reverse=not ascending
    )
    # Retornamos a nova lista ordenada
    return sorted_list


# Teste 1: ordem crescente (mais barato primeiro)
print("--- Preco crescente ---")
# "sorted_products" = produtos ordenados
sorted_products = sort_by_price(products, ascending=True)
for product in sorted_products:
    print(f"  R$ {product['price']:>6.2f} - {product['name']}")

# Teste 2: ordem decrescente (mais caro primeiro)
print("\n--- Preco decrescente ---")
sorted_products = sort_by_price(products, ascending=False)
for product in sorted_products:
    print(f"  R$ {product['price']:>6.2f} - {product['name']}")

# Verificamos que a lista original nao foi modificada
print(f"\nLista original (primeiro item): {products[0]['name']}")
```

Saida esperada:
```
--- Preco crescente ---
  R$   4.50 - Sabao
  R$   7.50 - Feijao
  R$   8.99 - Arroz
  R$  12.75 - Shampoo

--- Preco decrescente ---
  R$  12.75 - Shampoo
  R$   8.99 - Arroz
  R$   7.50 - Feijao
  R$   4.50 - Sabao

Lista original (primeiro item): Arroz
```

---

### Exercício 14 — Relatório de Estoque por Categoria

#### Enunciado

Crie uma função `stock_report_by_category` que agrupe os produtos por categoria e exiba um relatório com: quantidade de produtos, quantidade total em estoque e valor total por categoria.

#### Dicas

- Use um dicionário para agrupar os dados por categoria
- Para cada categoria, acumule: contagem de produtos, soma de quantidades e soma de valores
- Percorra o dicionário para exibir o relatório

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com 2 produtos em "Alimentos" e 1 em "Limpeza", o relatório deve mostrar os totais corretos para cada categoria
- **Caso de borda:** Com lista vazia, deve exibir "Nenhum produto para gerar relatório"

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Feijao", "price": 7.50, "quantity": 40, "category": "Alimentos"},
    {"id": 3, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 4, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que gera relatorio de estoque por categoria
# "stock" = estoque, "report" = relatorio, "by" = por, "category" = categoria
def stock_report_by_category(product_list):
    """Gera relatorio de estoque agrupado por categoria."""
    # Verificamos se a lista esta vazia
    if len(product_list) == 0:
        print("Nenhum produto para gerar relatorio.")
        return
    # Dicionario para agrupar dados por categoria
    # "categories" = categorias
    categories = {}
    # Percorremos cada produto
    for product in product_list:
        # Obtemos a categoria do produto
        # "cat" = categoria (abreviacao)
        cat = product["category"]
        # Se a categoria ainda nao existe no dicionario, criamos
        if cat not in categories:
            # Inicializamos com contadores zerados
            categories[cat] = {
                "count": 0,           # Quantidade de produtos (count = contagem)
                "total_quantity": 0,  # Quantidade total em estoque
                "total_value": 0.0    # Valor total do estoque
            }
        # Incrementamos os contadores
        categories[cat]["count"] = categories[cat]["count"] + 1
        categories[cat]["total_quantity"] = categories[cat]["total_quantity"] + product["quantity"]
        categories[cat]["total_value"] = categories[cat]["total_value"] + (product["price"] * product["quantity"])
    # Exibimos o relatorio
    print("\n--- Relatorio de Estoque por Categoria ---")
    print(f"{'Categoria':<15} {'Produtos':>10} {'Qtd Estoque':>12} {'Valor Total':>12}")
    print("-" * 52)
    # Percorremos cada categoria no dicionario
    for cat, data in categories.items():
        print(f"{cat:<15} {data['count']:>10} {data['total_quantity']:>12} {data['total_value']:>12.2f}")
    print("-" * 52)


# Teste: relatorio com produtos
stock_report_by_category(products)

# Teste: relatorio com lista vazia
print()
stock_report_by_category([])
```

Saida esperada:
```
--- Relatorio de Estoque por Categoria ---
Categoria         Produtos  Qtd Estoque  Valor Total
----------------------------------------------------
Alimentos                2           90       749.50
Limpeza                  1           80       360.00
Higiene                  1           25       318.75
----------------------------------------------------

Nenhum produto para gerar relatorio.
```


---

### Exercício 15 — Exportar Produtos para Texto Formatado

#### Enunciado

Crie uma função `export_to_text` que receba a lista de produtos e retorne uma string formatada com todos os produtos, um por linha, no formato: `ID | Nome | R$ Preco | Qtd unidades | Categoria`. Exiba a string gerada.

#### Dicas

- Use uma lista para acumular as linhas de texto
- Use f-string para formatar cada linha
- Use `"\n".join(lista)` para juntar todas as linhas com quebra de linha

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com 3 produtos, a string deve conter 3 linhas formatadas
- **Caso de borda:** Com lista vazia, deve retornar "Nenhum produto cadastrado."

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 80, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"}
]


# Funcao que exporta produtos para texto formatado
# "export" = exportar, "to" = para, "text" = texto
def export_to_text(product_list):
    """Retorna uma string formatada com todos os produtos."""
    # Verificamos se a lista esta vazia
    if len(product_list) == 0:
        return "Nenhum produto cadastrado."
    # Lista para acumular as linhas de texto
    # "lines" = linhas
    lines = []
    # Adicionamos o cabecalho
    lines.append("=== Lista de Produtos ===")
    # Percorremos cada produto
    for product in product_list:
        # Formatamos a linha do produto
        # "line" = linha
        line = f"{product['id']} | {product['name']} | R$ {product['price']:.2f} | {product['quantity']} unidades | {product['category']}"
        # Adicionamos a linha a lista
        lines.append(line)
    # Adicionamos o total
    lines.append(f"=== Total: {len(product_list)} produto(s) ===")
    # Juntamos todas as linhas com quebra de linha
    # "\n".join() une os itens da lista com "\n" entre eles
    # "result" = resultado
    result = "\n".join(lines)
    return result


# Teste 1: lista com produtos
# "text" = texto
text = export_to_text(products)
print(text)

# Teste 2: lista vazia
print()
text = export_to_text([])
print(text)
```

Saida esperada:
```
=== Lista de Produtos ===
1 | Arroz | R$ 8.99 | 50 unidades | Alimentos
2 | Sabao | R$ 4.50 | 80 unidades | Limpeza
3 | Shampoo | R$ 12.75 | 25 unidades | Higiene
=== Total: 3 produto(s) ===

Nenhum produto cadastrado.
```

---

### Exercício 16 — Atualizar Quantidade (Entrada e Saida de Estoque)

#### Enunciado

Crie duas funções: `add_stock` (adicionar ao estoque) e `remove_stock` (retirar do estoque). Ambas recebem o ID do produto e a quantidade. A função `remove_stock` deve verificar se ha estoque suficiente antes de retirar.

#### Dicas

- Use `find_by_id` para buscar o produto
- Na adicao, some a quantidade ao estoque atual
- Na remoção, verifique se a quantidade em estoque e suficiente antes de subtrair
- Retorne True se a operação foi bem-sucedida, False caso contrario

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Adicionar 20 unidades ao produto com 50 deve resultar em 70
- **Caso de borda:** Tentar remover 100 unidades de um produto com 50 deve falhar

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 10, "category": "Limpeza"}
]


def find_by_id(product_id):
    """Busca um produto pelo ID."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


# Funcao que adiciona unidades ao estoque
# "add" = adicionar, "stock" = estoque
def add_stock(product_id, quantity):
    """Adiciona unidades ao estoque de um produto."""
    # Buscamos o produto
    product = find_by_id(product_id)
    # Verificamos se o produto existe
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    # Verificamos se a quantidade e valida
    if not isinstance(quantity, int) or quantity <= 0:
        print("Quantidade deve ser um numero inteiro positivo.")
        return False
    # Adicionamos ao estoque
    product["quantity"] = product["quantity"] + quantity
    print(f"Adicionadas {quantity} unidades de '{product['name']}'. Estoque: {product['quantity']}")
    return True


# Funcao que remove unidades do estoque
# "remove" = remover, "stock" = estoque
def remove_stock(product_id, quantity):
    """Remove unidades do estoque de um produto."""
    # Buscamos o produto
    product = find_by_id(product_id)
    # Verificamos se o produto existe
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    # Verificamos se a quantidade e valida
    if not isinstance(quantity, int) or quantity <= 0:
        print("Quantidade deve ser um numero inteiro positivo.")
        return False
    # Verificamos se ha estoque suficiente
    if product["quantity"] < quantity:
        print(f"Estoque insuficiente. Disponivel: {product['quantity']}, solicitado: {quantity}")
        return False
    # Removemos do estoque
    product["quantity"] = product["quantity"] - quantity
    print(f"Removidas {quantity} unidades de '{product['name']}'. Estoque: {product['quantity']}")
    return True


# Teste 1: adicionar estoque
print("--- Adicionar estoque ---")
add_stock(1, 20)

# Teste 2: remover estoque (sucesso)
print("\n--- Remover estoque (sucesso) ---")
remove_stock(1, 30)

# Teste 3: remover estoque (insuficiente)
print("\n--- Remover estoque (insuficiente) ---")
remove_stock(2, 100)

# Teste 4: produto inexistente
print("\n--- Produto inexistente ---")
add_stock(99, 10)
```

Saida esperada:
```
--- Adicionar estoque ---
Adicionadas 20 unidades de 'Arroz'. Estoque: 70

--- Remover estoque (sucesso) ---
Removidas 30 unidades de 'Arroz'. Estoque: 40

--- Remover estoque (insuficiente) ---
Estoque insuficiente. Disponivel: 10, solicitado: 100

--- Produto inexistente ---
Produto com ID 99 nao encontrado.
```

---

### Exercício 17 — Produtos com Estoque Baixo

#### Enunciado

Crie uma função `low_stock_alert` que receba um limite mínimo e retorne uma lista de produtos cuja quantidade em estoque esteja abaixo desse limite. Exiba um alerta para cada produto encontrado.

#### Dicas

- Percorra a lista e compare a quantidade de cada produto com o limite
- Adicione a uma lista os produtos com estoque abaixo do limite
- Exiba um alerta formatado para cada produto

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com limite 30, produtos com quantidade menor que 30 devem aparecer no alerta
- **Caso de borda:** Com limite 0, nenhum produto deve aparecer (todos tem estoque >= 0)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
products = [
    {"id": 1, "name": "Arroz", "price": 8.99, "quantity": 50, "category": "Alimentos"},
    {"id": 2, "name": "Sabao", "price": 4.50, "quantity": 5, "category": "Limpeza"},
    {"id": 3, "name": "Shampoo", "price": 12.75, "quantity": 25, "category": "Higiene"},
    {"id": 4, "name": "Pasta de Dente", "price": 6.00, "quantity": 3, "category": "Higiene"}
]


# Funcao que identifica produtos com estoque baixo
# "low" = baixo, "stock" = estoque, "alert" = alerta
def low_stock_alert(minimum):
    """Retorna produtos com estoque abaixo do limite minimo."""
    # Lista para armazenar produtos com estoque baixo
    # "low_stock" = estoque baixo
    low_stock = []
    # Percorremos cada produto
    for product in products:
        # Verificamos se a quantidade esta abaixo do limite
        # "minimum" = minimo
        if product["quantity"] < minimum:
            # Adicionamos a lista de alertas
            low_stock.append(product)
    # Exibimos o resultado
    if len(low_stock) == 0:
        print(f"Nenhum produto com estoque abaixo de {minimum}.")
    else:
        print(f"\n*** ALERTA: {len(low_stock)} produto(s) com estoque baixo (< {minimum}) ***")
        for product in low_stock:
            print(f"  [{product['id']}] {product['name']} - apenas {product['quantity']} unidade(s)")
    # Retornamos a lista
    return low_stock


# Teste 1: limite 30
low_stock_alert(30)

# Teste 2: limite 10
print()
low_stock_alert(10)

# Teste 3: limite 0 (nenhum produto)
print()
low_stock_alert(0)
```

Saida esperada:
```
*** ALERTA: 3 produto(s) com estoque baixo (< 30) ***
  [2] Sabao - apenas 5 unidade(s)
  [3] Shampoo - apenas 25 unidade(s)
  [4] Pasta de Dente - apenas 3 unidade(s)

*** ALERTA: 2 produto(s) com estoque baixo (< 10) ***
  [2] Sabao - apenas 5 unidade(s)
  [4] Pasta de Dente - apenas 3 unidade(s)

Nenhum produto com estoque abaixo de 0.
```

---

### Exercício 18 — CRUD Completo com Dados de Teste

#### Enunciado

Crie o programa CRUD completo (todas as funções) e adicione uma função `load_sample_data` que pre-carrega 5 produtos de teste. O programa deve iniciar com os dados de teste ja carregados, facilitando os testes das operações. Inclua todas as 5 operações no menu.

#### Dicas

- Crie a função `load_sample_data` que chama `create_product` 5 vezes com dados diferentes
- Chame `load_sample_data` no inicio da função `main`, antes do loop do menu
- Inclua produtos de pelo menos 3 categorias diferentes

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Ao iniciar, a opcao "Listar" deve mostrar 5 produtos pre-cadastrados
- **Caso de borda:** Cadastre um 6o produto — ele deve receber ID 6 (os IDs 1-5 ja foram usados)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista global de produtos e contador de IDs
products = []
next_id = 1


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


def create_product(name, price, quantity, category):
    """Cadastra um novo produto."""
    global next_id
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        for error in errors:
            print(f"  Erro: {error}")
        return None
    product = {"id": next_id, "name": name, "price": price, "quantity": quantity, "category": category}
    products.append(product)
    next_id = next_id + 1
    return product


def list_products():
    """Exibe todos os produtos."""
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)
    for p in products:
        print(f"{p['id']:<5} {p['name']:<20} {p['price']:>10.2f} {p['quantity']:>5} {p['category']:<15}")
    print(f"\nTotal: {len(products)} produto(s)")


def find_by_id(product_id):
    """Busca um produto pelo ID."""
    for p in products:
        if p["id"] == product_id:
            return p
    return None


def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto."""
    product = find_by_id(product_id)
    if product is None:
        print(f"Produto ID {product_id} nao encontrado.")
        return False
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        for error in errors:
            print(f"  Erro: {error}")
        return False
    product["name"] = name
    product["price"] = price
    product["quantity"] = quantity
    product["category"] = category
    return True


def delete_product(product_id):
    """Remove um produto da lista."""
    product = find_by_id(product_id)
    if product is None:
        print(f"Produto ID {product_id} nao encontrado.")
        return False
    products.remove(product)
    return True


# Funcao que carrega dados de teste
# "load" = carregar, "sample" = amostra, "data" = dados
def load_sample_data():
    """Carrega 5 produtos de teste no sistema."""
    # Cadastramos 5 produtos de diferentes categorias
    create_product("Arroz", 8.99, 50, "Alimentos")
    create_product("Feijao", 7.50, 40, "Alimentos")
    create_product("Sabao em Po", 12.90, 30, "Limpeza")
    create_product("Shampoo", 15.00, 20, "Higiene")
    create_product("Pasta de Dente", 6.50, 45, "Higiene")
    # Informamos que os dados foram carregados
    print(f"Dados de teste carregados: {len(products)} produtos")


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


# Funcao principal
def main():
    """Funcao principal com menu completo e dados de teste."""
    # Carregamos os dados de teste
    load_sample_data()

    # Loop principal do menu
    while True:
        print("\n1-Cadastrar 2-Listar 3-Buscar 4-Atualizar 5-Excluir 0-Sair")
        choice = input("Opcao: ")

        if choice == "1":
            print("\n--- Cadastrar ---")
            data = read_product_input()
            if data is not None:
                n, p, q, c = data
                result = create_product(n, p, q, c)
                if result is not None:
                    print(f"Cadastrado: {result['name']} (ID {result['id']})")

        elif choice == "2":
            list_products()

        elif choice == "3":
            try:
                pid = int(input("ID: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_by_id(pid)
            if product is None:
                print("Nao encontrado.")
            else:
                print(f"  {product['name']} - R$ {product['price']:.2f} - {product['quantity']} un.")

        elif choice == "4":
            try:
                pid = int(input("ID para atualizar: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_by_id(pid)
            if product is None:
                print("Nao encontrado.")
                continue
            print(f"Atual: {product['name']} - R$ {product['price']:.2f}")
            data = read_product_input()
            if data is not None:
                n, p, q, c = data
                if update_product(pid, n, p, q, c):
                    print("Atualizado com sucesso!")

        elif choice == "5":
            try:
                pid = int(input("ID para excluir: "))
            except ValueError:
                print("ID invalido.")
                continue
            product = find_by_id(pid)
            if product is None:
                print("Nao encontrado.")
                continue
            confirm = input(f"Excluir '{product['name']}'? (s/n): ")
            if confirm.lower() == "s":
                if delete_product(pid):
                    print("Excluido com sucesso!")
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

Saida esperada (inicio do programa):
```
Dados de teste carregados: 5 produtos

1-Cadastrar 2-Listar 3-Buscar 4-Atualizar 5-Excluir 0-Sair
Opcao: 2

ID    Nome                     Preco   Qtd Categoria
------------------------------------------------------------
1     Arroz                     8.99    50 Alimentos
2     Feijao                    7.50    40 Alimentos
3     Sabao em Po              12.90    30 Limpeza
4     Shampoo                  15.00    20 Higiene
5     Pasta de Dente            6.50    45 Higiene

Total: 5 produto(s)
```