# 28 — Exercícios: Modelagem de Dados

[<- Voltar para o módulo](28-modelagem-dados.md) | [Glossário](00-glossario.md)

---

> **Antes de começar:** Estes exercícios vao ajudar você a praticar a modelagem de dados e a validação de informações. Cada exercício constroi progressivamente o conhecimento que você vai usar no projeto CRUD (módulos 29 a 32). Tente resolver cada exercício sozinho antes de consultar a resposta.

---

### Exercício 1 — Identificando Campos de uma Entidade

#### Enunciado

Crie um dicionário Python que represente um **aluno** de uma escola. O aluno deve ter os seguintes campos: identificador (número inteiro), nome (texto), idade (número inteiro), nota final (número decimal) e aprovado (verdadeiro ou falso). Exiba todos os campos formatados.

#### Dicas

- Use um dicionário com chaves em ingles e comentários em portugues
- Escolha o tipo de dado adequado para cada campo
- Use f-string para formatar a saida

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com nome "Maria", idade 20, nota 8.5 e aprovado True, a saida deve mostrar todos os campos corretamente
- **Caso de borda:** Altere a nota para 4.0 e aprovado para False — verifique se os valores mudam corretamente na saida

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Criamos um dicionario representando um aluno
# "student" = aluno/estudante
student = {
    "id": 1,                # Identificador unico do aluno (id = identificador)
    "name": "Maria",        # Nome do aluno (name = nome)
    "age": 20,              # Idade do aluno (age = idade)
    "final_grade": 8.5,     # Nota final (final_grade = nota final)
    "approved": True         # Aprovado ou nao (approved = aprovado)
}

# Exibimos cada campo do aluno formatado
# print() mostra o texto no terminal
print(f"ID: {student['id']}")
# Exibimos o nome do aluno
print(f"Nome: {student['name']}")
# Exibimos a idade do aluno
print(f"Idade: {student['age']} anos")
# Exibimos a nota final com uma casa decimal
print(f"Nota Final: {student['final_grade']:.1f}")
# Exibimos se o aluno foi aprovado
print(f"Aprovado: {student['approved']}")
```

Saida esperada:
```
ID: 1
Nome: Maria
Idade: 20 anos
Nota Final: 8.5
Aprovado: True
```

---

### Exercício 2 — Escolhendo Tipos de Dados

#### Enunciado

Você recebeu a seguinte lista de campos para um cadastro de **livro**: título, autor, número de páginas, preco, disponível para emprestimo. Crie um dicionário com os tipos de dados adequados para cada campo e use `type()` para exibir o tipo de cada um.

#### Dicas

- Título e autor sao textos (str)
- Número de páginas e um número inteiro (int)
- Preco tem centavos, então e decimal (float)
- Disponível para emprestimo e sim ou não (bool)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** O tipo de "title" deve ser `<class 'str'>`, "pages" deve ser `<class 'int'>`, "price" deve ser `<class 'float'>`
- **Caso de borda:** Altere "available" para False — o tipo deve continuar sendo `<class 'bool'>`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Criamos um dicionario representando um livro
# "book" = livro
book = {
    "title": "O Pequeno Principe",   # Titulo do livro (title = titulo)
    "author": "Antoine de Saint",     # Autor do livro (author = autor)
    "pages": 96,                      # Numero de paginas (pages = paginas)
    "price": 29.90,                   # Preco do livro (price = preco)
    "available": True                  # Disponivel para emprestimo (available = disponivel)
}

# Exibimos o tipo de cada campo usando type()
# type() retorna o tipo de dado de um valor
print(f"title: {type(book['title'])}")
# Exibimos o tipo do autor
print(f"author: {type(book['author'])}")
# Exibimos o tipo do numero de paginas
print(f"pages: {type(book['pages'])}")
# Exibimos o tipo do preco
print(f"price: {type(book['price'])}")
# Exibimos o tipo da disponibilidade
print(f"available: {type(book['available'])}")
```

Saida esperada:
```
title: <class 'str'>
author: <class 'str'>
pages: <class 'int'>
price: <class 'float'>
available: <class 'bool'>
```

---

### Exercício 3 — Lista de Entidades

#### Enunciado

Crie uma lista contendo tres dicionários, cada um representando um **produto** com os campos: id, name, price, quantity e category. Depois, percorra a lista com um loop `for` e exiba cada produto em uma linha formatada.

#### Dicas

- Cada produto e um dicionário dentro de uma lista
- Use um loop `for` para percorrer a lista
- Use f-string com `:.2f` para formatar o preco com duas casas decimais

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve mostrar tres linhas, uma para cada produto, com id, nome, preco e quantidade
- **Caso de borda:** Adicione um quarto produto a lista e verifique se a saida agora mostra quatro linhas

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Criamos uma lista de produtos
# "products" = produtos (lista de dicionarios)
products = [
    {
        "id": 1,                        # Identificador do primeiro produto
        "name": "Arroz",                # Nome do produto (name = nome)
        "price": 8.99,                  # Preco do produto (price = preco)
        "quantity": 50,                 # Quantidade em estoque (quantity = quantidade)
        "category": "Alimentos"         # Categoria do produto (category = categoria)
    },
    {
        "id": 2,                        # Identificador do segundo produto
        "name": "Sabao",                # Nome do produto (name = nome)
        "price": 4.50,                  # Preco do produto (price = preco)
        "quantity": 80,                 # Quantidade em estoque (quantity = quantidade)
        "category": "Limpeza"           # Categoria do produto (category = categoria)
    },
    {
        "id": 3,                        # Identificador do terceiro produto
        "name": "Pasta de Dente",       # Nome do produto (name = nome)
        "price": 6.75,                  # Preco do produto (price = preco)
        "quantity": 35,                 # Quantidade em estoque (quantity = quantidade)
        "category": "Higiene"           # Categoria do produto (category = categoria)
    }
]

# Percorremos a lista e exibimos cada produto
# "product" = produto (cada item da lista)
for product in products:
    # Exibimos os dados formatados com f-string
    # :.2f formata o numero com duas casas decimais
    print(f"[{product['id']}] {product['name']} - R$ {product['price']:.2f} - {product['quantity']} un. - {product['category']}")
```

Saida esperada:
```
[1] Arroz - R$ 8.99 - 50 un. - Alimentos
[2] Sabao - R$ 4.50 - 80 un. - Limpeza
[3] Pasta de Dente - R$ 6.75 - 35 un. - Higiene
```

---

### Exercício 4 — Função para Criar Entidade

#### Enunciado

Crie uma função chamada `create_product` que receba nome, preco, quantidade e categoria como parametros e retorne um dicionário representando o produto. Use um contador global para gerar o id automaticamente. Crie dois produtos e exiba-os.

#### Dicas

- Use uma variável global para o contador de ids
- A função deve montar e retornar o dicionário
- Lembre-se de usar `global` para modificar a variável do contador dentro da função

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** O primeiro produto deve ter id 1 e o segundo deve ter id 2
- **Caso de borda:** Crie um terceiro produto e verifique se o id e 3

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Contador global para gerar identificadores unicos
# "next" = proximo, "id" = identificador
next_id = 1


# Funcao que cria um dicionario de produto com id automatico
# "create" = criar, "product" = produto
def create_product(name, price, quantity, category):
    """Cria e retorna um dicionario representando um produto."""
    # Acessamos a variavel global next_id
    global next_id
    # Montamos o dicionario do produto
    # "product" = produto
    product = {
        "id": next_id,              # Usamos o contador como identificador
        "name": name,               # Nome do produto (name = nome)
        "price": price,             # Preco do produto (price = preco)
        "quantity": quantity,       # Quantidade (quantity = quantidade)
        "category": category         # Categoria (category = categoria)
    }
    # Incrementamos o contador para o proximo produto
    next_id = next_id + 1
    # Retornamos o dicionario pronto
    return product


# Criamos dois produtos usando a funcao
# "product" = produto
product_1 = create_product("Cafe", 15.90, 30, "Alimentos")
product_2 = create_product("Amaciante", 9.50, 45, "Limpeza")

# Exibimos os produtos criados
# print() mostra o texto no terminal
print(f"Produto 1: {product_1}")
print(f"Produto 2: {product_2}")
```

Saida esperada:
```
Produto 1: {'id': 1, 'name': 'Cafe', 'price': 15.9, 'quantity': 30, 'category': 'Alimentos'}
Produto 2: {'id': 2, 'name': 'Amaciante', 'price': 9.5, 'quantity': 45, 'category': 'Limpeza'}
```

---

### Exercício 5 — Validação de Nome Não Vazio

#### Enunciado

Crie uma função chamada `validate_name` que receba um nome (texto) e retorne `True` se o nome for válido (não vazio e não apenas espacos em branco) ou `False` caso contrario. Teste a função com diferentes entradas.

#### Dicas

- Use o método `strip()` para remover espacos em branco das pontas
- Uma string vazia `""` e uma string so com espacos `"   "` devem ser consideradas invalidas
- A função deve retornar um valor booleano (True ou False)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** `validate_name("Arroz")` deve retornar `True` e exibir "Válido"
- **Caso de borda:** `validate_name("   ")` deve retornar `False` e exibir "Inválido"

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que valida se um nome nao esta vazio
# "validate" = validar, "name" = nome
def validate_name(name):
    """Retorna True se o nome for valido, False caso contrario."""
    # Verificamos se o nome e uma string nao vazia
    # strip() remove espacos em branco das pontas do texto
    if name and name.strip() != "":
        # Nome valido — retornamos True (verdadeiro)
        return True
    else:
        # Nome vazio ou so com espacos — retornamos False (falso)
        return False


# Testamos com diferentes entradas
# "test" = teste, "names" = nomes
test_names = ["Arroz", "", "   ", "Feijao", None]

# Percorremos cada nome de teste
# "name" = nome
for name in test_names:
    # Chamamos a funcao de validacao
    # "result" = resultado
    result = validate_name(name)
    # Exibimos o resultado
    # repr() mostra o valor com aspas, util para ver strings vazias
    print(f"validate_name({repr(name)}) = {result}")
```

Saida esperada:
```
validate_name('Arroz') = True
validate_name('') = False
validate_name('   ') = False
validate_name('Feijao') = True
validate_name(None) = False
```

---

### Exercício 6 — Validação de Preco

#### Enunciado

Crie uma função chamada `validate_price` que receba um valor e retorne `True` se for um número (int ou float) maior ou igual a zero, ou `False` caso contrario. Teste com valores validos e invalidos.

#### Dicas

- Use `isinstance()` para verificar se o valor e int ou float
- O preco deve ser maior ou igual a zero (zero e válido — produto gratuito)
- Valores negativos e textos devem ser rejeitados

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** `validate_price(8.99)` deve retornar `True`
- **Caso de borda:** `validate_price(0)` deve retornar `True` (produto gratuito e válido), `validate_price(-5.0)` deve retornar `False`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que valida se um preco e valido
# "validate" = validar, "price" = preco
def validate_price(price):
    """Retorna True se o preco for um numero >= 0, False caso contrario."""
    # Verificamos se o valor e um numero (int ou float)
    # isinstance() verifica se o valor e do tipo esperado
    if not isinstance(price, (int, float)):
        # Nao e um numero — invalido
        return False
    # Verificamos se o preco nao e negativo
    if price < 0:
        # Preco negativo — invalido
        return False
    # Passou em todas as verificacoes — valido
    return True


# Testamos com diferentes valores
# "test" = teste, "prices" = precos
test_prices = [8.99, 0, 15, -5.0, "abc", None, 0.01]

# Percorremos cada preco de teste
# "price" = preco
for price in test_prices:
    # Chamamos a funcao de validacao
    # "result" = resultado
    result = validate_price(price)
    # Exibimos o resultado
    print(f"validate_price({repr(price)}) = {result}")
```

Saida esperada:
```
validate_price(8.99) = True
validate_price(0) = True
validate_price(15) = True
validate_price(-5.0) = False
validate_price('abc') = False
validate_price(None) = False
validate_price(0.01) = True
```

---

### Exercício 7 — Validação Completa de Produto

#### Enunciado

Crie uma função chamada `validate_product` que receba nome, preco, quantidade e categoria, e retorne uma lista de mensagens de erro. Se a lista estiver vazia, significa que todos os dados sao validos. Teste com dados validos e com dados que tenham multiplos erros.

#### Dicas

- Crie uma lista vazia para armazenar os erros
- Verifique cada campo e adicione uma mensagem de erro se for inválido
- Retorne a lista de erros no final (vazia = tudo válido)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com dados validos ("Arroz", 8.99, 50, "Alimentos"), a lista de erros deve estar vazia
- **Caso de borda:** Com dados invalidos ("", -1, -5, ""), a lista deve conter 4 mensagens de erro

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que valida todos os campos de um produto
# "validate" = validar, "product" = produto
def validate_product(name, price, quantity, category):
    """Valida os dados de um produto e retorna lista de erros."""
    # Criamos uma lista vazia para armazenar os erros
    # "errors" = erros
    errors = []

    # Validacao do nome: nao pode ser vazio
    if not name or name.strip() == "":
        # Adicionamos a mensagem de erro a lista
        errors.append("Nome nao pode ser vazio")

    # Validacao do preco: deve ser numero >= 0
    if not isinstance(price, (int, float)):
        errors.append("Preco deve ser um numero")
    elif price < 0:
        errors.append("Preco nao pode ser negativo")

    # Validacao da quantidade: deve ser inteiro >= 0
    if not isinstance(quantity, int):
        errors.append("Quantidade deve ser um numero inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")

    # Validacao da categoria: nao pode ser vazia
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")

    # Retornamos a lista de erros
    return errors


# Teste 1: dados validos
# "errors" = erros
errors = validate_product("Arroz", 8.99, 50, "Alimentos")
# Exibimos o resultado
print(f"Teste 1 (valido): {len(errors)} erros")

# Teste 2: todos os dados invalidos
errors = validate_product("", -1, -5, "")
# Exibimos o resultado e cada erro
print(f"Teste 2 (invalido): {len(errors)} erros")
# "error" = erro
for error in errors:
    # Exibimos cada mensagem de erro
    print(f"  - {error}")
```

Saida esperada:
```
Teste 1 (valido): 0 erros
Teste 2 (invalido): 4 erros
  - Nome nao pode ser vazio
  - Preco nao pode ser negativo
  - Quantidade nao pode ser negativa
  - Categoria nao pode ser vazia
```

---

### Exercício 8 — Cadastro com Validação e Lista

#### Enunciado

Crie um programa que mantenha uma lista de produtos. Crie uma função `add_product` que valide os dados antes de adicionar o produto a lista. Use um contador global para gerar ids automaticamente. Tente cadastrar 4 produtos (3 validos e 1 inválido) e exiba a lista final.

#### Dicas

- Combine a função de validação do exercício anterior com a criação do produto
- Use `global` para acessar o contador de ids e a lista de produtos
- A função deve retornar o produto criado ou None se os dados forem invalidos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Apos cadastrar 3 produtos validos e 1 inválido, a lista deve conter exatamente 3 produtos
- **Caso de borda:** O produto inválido não deve aparecer na lista, e os ids devem ser 1, 2 e 3

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista global que armazena todos os produtos
# "products" = produtos
products = []
# Contador global para gerar ids unicos
# "next" = proximo, "id" = identificador
next_id = 1


# Funcao que valida os dados de um produto
# "validate" = validar, "product" = produto, "data" = dados
def validate_product_data(name, price, quantity, category):
    """Valida os dados e retorna lista de erros."""
    # "errors" = erros
    errors = []
    # Validacao do nome
    if not name or name.strip() == "":
        errors.append("Nome nao pode ser vazio")
    # Validacao do preco
    if not isinstance(price, (int, float)):
        errors.append("Preco deve ser um numero")
    elif price < 0:
        errors.append("Preco nao pode ser negativo")
    # Validacao da quantidade
    if not isinstance(quantity, int):
        errors.append("Quantidade deve ser inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")
    # Validacao da categoria
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    return errors


# Funcao que adiciona um produto validado a lista
# "add" = adicionar, "product" = produto
def add_product(name, price, quantity, category):
    """Adiciona um produto a lista se os dados forem validos."""
    # Acessamos as variaveis globais
    global next_id
    # Validamos os dados
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
    return product


# Cadastramos 3 produtos validos e 1 invalido
add_product("Arroz", 8.99, 50, "Alimentos")
add_product("Sabao", 4.50, 80, "Limpeza")
add_product("", -3.00, -1, "")  # Invalido — sera rejeitado
add_product("Shampoo", 12.75, 25, "Higiene")

# Exibimos a lista final
print(f"\nTotal de produtos: {len(products)}")
# "product" = produto
for product in products:
    # Exibimos cada produto formatado
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

### Exercício 9 — Buscar Produto por ID

#### Enunciado

Usando a lista de produtos do exercício anterior como base, crie uma função chamada `find_product_by_id` que receba um id e retorne o dicionário do produto correspondente, ou `None` se o produto não for encontrado. Teste buscando um id existente e um id inexistente.

#### Dicas

- Percorra a lista de produtos com um loop `for`
- Compare o id de cada produto com o id buscado
- Se encontrar, retorne o produto imediatamente
- Se o loop terminar sem encontrar, retorne None

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar id 2 deve retornar o produto "Sabao" com preco 4.50
- **Caso de borda:** Buscar id 99 deve retornar None e exibir "Produto não encontrado"

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


# Funcao que busca um produto pelo identificador
# "find" = encontrar, "product" = produto, "by" = por, "id" = identificador
def find_product_by_id(product_id):
    """Busca um produto pelo id e retorna o dicionario ou None."""
    # Percorremos cada produto na lista
    # "product" = produto
    for product in products:
        # Comparamos o id do produto com o id buscado
        if product["id"] == product_id:
            # Encontramos — retornamos o produto
            return product
    # Se o loop terminou sem encontrar, retornamos None
    return None


# Teste 1: buscar id existente
# "found" = encontrado, "product" = produto
found_product = find_product_by_id(2)
# Verificamos se o produto foi encontrado
if found_product is not None:
    # Exibimos os dados do produto encontrado
    print(f"Encontrado: {found_product['name']} - R$ {found_product['price']:.2f}")
else:
    print("Produto nao encontrado")

# Teste 2: buscar id inexistente
found_product = find_product_by_id(99)
# Verificamos se o produto foi encontrado
if found_product is not None:
    print(f"Encontrado: {found_product['name']}")
else:
    # Produto nao existe na lista
    print("Produto nao encontrado")
```

Saida esperada:
```
Encontrado: Sabao - R$ 4.50
Produto nao encontrado
```

---

### Exercício 10 — Filtrar Produtos por Categoria

#### Enunciado

Crie uma função chamada `filter_by_category` que receba uma categoria (texto) e retorne uma nova lista contendo apenas os produtos daquela categoria. Teste filtrando por uma categoria existente e uma inexistente.

#### Dicas

- Crie uma lista vazia para armazenar os produtos filtrados
- Percorra a lista de produtos e adicione os que correspondem a categoria
- Compare as categorias ignorando maiusculas/minusculas usando `lower()`

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Filtrar por "Alimentos" deve retornar uma lista com os produtos dessa categoria
- **Caso de borda:** Filtrar por "Eletronicos" (categoria inexistente) deve retornar uma lista vazia

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Lista de produtos cadastrados
# "products" = produtos
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
    # Lista vazia para armazenar os produtos filtrados
    # "filtered" = filtrados
    filtered = []
    # Percorremos cada produto na lista
    # "product" = produto
    for product in products:
        # Comparamos as categorias ignorando maiusculas/minusculas
        # lower() converte o texto para minusculas
        if product["category"].lower() == category.lower():
            # O produto pertence a categoria — adicionamos a lista filtrada
            filtered.append(product)
    # Retornamos a lista de produtos filtrados
    return filtered


# Teste 1: filtrar por categoria existente
# "result" = resultado
result = filter_by_category("Alimentos")
# Exibimos a quantidade de produtos encontrados
print(f"Alimentos: {len(result)} produto(s)")
# Exibimos cada produto encontrado
# "product" = produto
for product in result:
    print(f"  - {product['name']}")

# Teste 2: filtrar por categoria inexistente
result = filter_by_category("Eletronicos")
# Exibimos a quantidade (deve ser zero)
print(f"Eletronicos: {len(result)} produto(s)")
```

Saida esperada:
```
Alimentos: 2 produto(s)
  - Arroz
  - Feijao
Eletronicos: 0 produto(s)
```

---

### Exercício 11 — Calcular Valor Total do Estoque

#### Enunciado

Crie uma função chamada `calculate_stock_value` que percorra a lista de produtos e calcule o valor total do estoque (preco multiplicado pela quantidade de cada produto). Exiba o valor total formatado em reais.

#### Dicas

- O valor de estoque de um produto e: preco vezes quantidade
- Use um acumulador para somar o valor de todos os produtos
- Formate o resultado com duas casas decimais usando `:.2f`

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com os produtos Arroz (8.99 x 50 = 449.50), Sabao (4.50 x 80 = 360.00) e Shampoo (12.75 x 25 = 318.75), o total deve ser R$ 1128.25
- **Caso de borda:** Com uma lista vazia, o valor total deve ser R$ 0.00

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


# Funcao que calcula o valor total do estoque
# "calculate" = calcular, "stock" = estoque, "value" = valor
def calculate_stock_value(product_list):
    """Calcula e retorna o valor total do estoque."""
    # Acumulador para somar o valor total
    # "total" = total, "value" = valor
    total_value = 0
    # Percorremos cada produto na lista
    # "product" = produto
    for product in product_list:
        # Calculamos o valor de estoque deste produto
        # Valor = preco (price) multiplicado pela quantidade (quantity)
        # "item" = item, "value" = valor
        item_value = product["price"] * product["quantity"]
        # Somamos ao total
        total_value = total_value + item_value
    # Retornamos o valor total
    return total_value


# Teste 1: lista com produtos
# "total" = total
total = calculate_stock_value(products)
# Exibimos o valor total formatado
# :.2f formata com duas casas decimais
print(f"Valor total do estoque: R$ {total:.2f}")

# Teste 2: lista vazia
# "empty" = vazio, "list" = lista
empty_list = []
total = calculate_stock_value(empty_list)
# Exibimos o valor total (deve ser zero)
print(f"Valor do estoque vazio: R$ {total:.2f}")
```

Saida esperada:
```
Valor total do estoque: R$ 1128.25
Valor do estoque vazio: R$ 0.00
```

---

### Exercício 12 — Modelo Completo com Todas as Operações

#### Enunciado

Crie um programa completo que simule um mini-cadastro de produtos. O programa deve ter funções para: (1) validar dados, (2) adicionar produto, (3) listar todos os produtos, (4) buscar por id e (5) calcular o valor total do estoque. Cadastre pelo menos 3 produtos e demonstre todas as funções.

Este exercício e uma preparacao direta para o projeto CRUD do módulo 29.

#### Dicas

- Reutilize as funções dos exercícios anteriores
- Organize o código com funções separadas para cada operação
- Use uma lista global para armazenar os produtos e um contador global para os ids
- Ao final, demonstre cada função com exemplos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Cadastrar 3 produtos validos, listar todos (deve mostrar 3), buscar por id 2 (deve encontrar), calcular valor total do estoque
- **Caso de borda:** Tentar cadastrar um produto inválido (deve ser rejeitado), buscar por id 99 (deve mostrar "não encontrado")

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# ============================================================
# Mini-cadastro de produtos — preparacao para o CRUD
# ============================================================

# Lista global que armazena todos os produtos
# "products" = produtos
products = []
# Contador global para gerar ids unicos
# "next" = proximo, "id" = identificador
next_id = 1


# --- Funcao 1: Validacao ---
# "validate" = validar, "product" = produto, "data" = dados
def validate_product_data(name, price, quantity, category):
    """Valida os dados de um produto e retorna lista de erros."""
    # "errors" = erros
    errors = []
    # Nome nao pode ser vazio
    if not name or name.strip() == "":
        errors.append("Nome nao pode ser vazio")
    # Preco deve ser numero >= 0
    if not isinstance(price, (int, float)):
        errors.append("Preco deve ser um numero")
    elif price < 0:
        errors.append("Preco nao pode ser negativo")
    # Quantidade deve ser inteiro >= 0
    if not isinstance(quantity, int):
        errors.append("Quantidade deve ser inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")
    # Categoria nao pode ser vazia
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    # Retornamos a lista de erros
    return errors


# --- Funcao 2: Adicionar produto ---
# "add" = adicionar, "product" = produto
def add_product(name, price, quantity, category):
    """Adiciona um produto validado a lista."""
    # Acessamos a variavel global
    global next_id
    # Validamos os dados
    errors = validate_product_data(name, price, quantity, category)
    # Se houver erros, exibimos e retornamos None
    if len(errors) > 0:
        print(f"Erro ao cadastrar: {errors}")
        return None
    # Criamos o dicionario do produto
    product = {
        "id": next_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    # Adicionamos a lista e incrementamos o contador
    products.append(product)
    next_id = next_id + 1
    print(f"Produto '{name}' cadastrado com ID {product['id']}")
    return product


# --- Funcao 3: Listar todos ---
# "list" = listar, "all" = todos, "products" = produtos
def list_all_products():
    """Exibe todos os produtos cadastrados."""
    # Verificamos se a lista esta vazia
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return
    # Exibimos o cabecalho
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    # Exibimos uma linha separadora
    print("-" * 60)
    # Percorremos cada produto
    for product in products:
        # Exibimos os dados formatados em colunas
        print(f"{product['id']:<5} {product['name']:<20} {product['price']:>10.2f} {product['quantity']:>5} {product['category']:<15}")


# --- Funcao 4: Buscar por id ---
# "find" = encontrar, "product" = produto, "by" = por
def find_product_by_id(product_id):
    """Busca um produto pelo id e retorna o dicionario ou None."""
    # Percorremos cada produto
    for product in products:
        # Comparamos o id
        if product["id"] == product_id:
            return product
    # Nao encontrado
    return None


# --- Funcao 5: Calcular valor do estoque ---
# "calculate" = calcular, "stock" = estoque, "value" = valor
def calculate_stock_value():
    """Calcula o valor total do estoque."""
    # Acumulador para o valor total
    total = 0
    # Percorremos cada produto
    for product in products:
        # Somamos preco vezes quantidade
        total = total + (product["price"] * product["quantity"])
    return total


# ============================================================
# Demonstracao de todas as funcoes
# ============================================================

print("=== CADASTRO DE PRODUTOS ===\n")

# Cadastramos 3 produtos validos
add_product("Arroz Integral", 8.99, 50, "Alimentos")
add_product("Detergente", 3.50, 100, "Limpeza")
add_product("Shampoo", 12.75, 25, "Higiene")

# Tentamos cadastrar um produto invalido
add_product("", -5.00, -10, "")

# Listamos todos os produtos
print("\n=== LISTA DE PRODUTOS ===")
list_all_products()

# Buscamos por id existente
print("\n=== BUSCA POR ID ===")
found = find_product_by_id(2)
if found is not None:
    print(f"ID 2 encontrado: {found['name']} - R$ {found['price']:.2f}")
else:
    print("ID 2 nao encontrado")

# Buscamos por id inexistente
found = find_product_by_id(99)
if found is not None:
    print(f"ID 99 encontrado: {found['name']}")
else:
    print("ID 99 nao encontrado")

# Calculamos o valor total do estoque
print("\n=== VALOR DO ESTOQUE ===")
total = calculate_stock_value()
print(f"Valor total: R$ {total:.2f}")
```

Saida esperada:
```
=== CADASTRO DE PRODUTOS ===

Produto 'Arroz Integral' cadastrado com ID 1
Produto 'Detergente' cadastrado com ID 2
Produto 'Shampoo' cadastrado com ID 3
Erro ao cadastrar: ['Nome nao pode ser vazio', 'Preco nao pode ser negativo', 'Quantidade nao pode ser negativa', 'Categoria nao pode ser vazia']

=== LISTA DE PRODUTOS ===

ID    Nome                      Preco   Qtd Categoria      
------------------------------------------------------------
1     Arroz Integral              8.99    50 Alimentos      
2     Detergente                  3.50   100 Limpeza        
3     Shampoo                    12.75    25 Higiene        

=== BUSCA POR ID ===
ID 2 encontrado: Detergente - R$ 3.50
ID 99 nao encontrado

=== VALOR DO ESTOQUE ===
Valor total: R$ 1118.25
```

---

[<- Voltar para o módulo](28-modelagem-dados.md) | [Glossário](00-glossario.md)
