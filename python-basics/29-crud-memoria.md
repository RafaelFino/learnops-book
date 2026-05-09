# 29 — CRUD em Memória: Cadastro de Produtos com Listas e Dicionários

[<- Anterior: Modelagem de Dados](28-modelagem-dados.md) | [Glossário](00-glossario.md) | [Próximo: CRUD com SQLite ->](30-crud-sqlite.md)

---

## Introdução

Parabéns por ter chegado ate aqui! Você ja aprendeu variáveis, condicionais, loops, funções, estruturas de dados, classes, módulos, boas práticas e modelagem de dados. Agora e hora de juntar tudo isso em um **projeto real**: um sistema de cadastro de produtos.

Imagine que você trabalha em uma loja pequena e precisa de um programa para controlar os produtos. Você precisa poder **cadastrar** novos produtos, **ver** a lista de produtos, **alterar** informações de um produto e **remover** produtos que não sao mais vendidos. Essas quatro operações formam o que chamamos de **CRUD**:

- **C** — Create (Criar): cadastrar um novo produto
- **R** — Read (Ler): consultar produtos existentes
- **U** — Update (Atualizar): alterar dados de um produto
- **D** — Delete (Excluir): remover um produto

O CRUD e um dos padrões mais importantes da programação. Praticamente todo sistema que você usa no dia a dia — redes sociais, lojas online, aplicativos de banco — usa operações CRUD por tras.

Neste módulo, você vai construir a **primeira versão** do CRUD, armazenando os dados em **listas e dicionários na memória** do programa. Isso significa que, quando o programa fechar, os dados serao perdidos. No próximo módulo (30), você vai aprender a salvar os dados em um banco de dados para que eles persistam.

> **Dica:** Consulte o [Glossário](00-glossario.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Crie uma pasta para o projeto: `mkdir -p ~/meus-projetos/crud-produtos`
2. Copie o código e cole em um novo arquivo no VSCode
3. Salve na pasta `~/meus-projetos/crud-produtos/`
4. No terminal: `cd ~/meus-projetos/crud-produtos`
5. Execute: `python3 nome_do_arquivo.py`

---

## O Que e CRUD

CRUD e uma sigla em ingles que representa as quatro operações básicas que podemos fazer com dados:

| Operação | Ingles | Portugues | O Que Faz |
|----------|--------|-----------|-----------|
| C | Create | Criar | Adiciona um novo registro |
| R | Read | Ler | Consulta registros existentes |
| U | Update | Atualizar | Modifica um registro existente |
| D | Delete | Excluir | Remove um registro |

### Analogia: Caderno de Enderecos

Pense em um **caderno de enderecos** fisico:

- **Criar:** Você escreve o nome e telefone de um novo contato em uma página em branco
- **Ler:** Você folheia o caderno para encontrar o telefone de alguem
- **Atualizar:** Alguem mudou de número — você apaga o antigo e escreve o novo
- **Excluir:** Você perdeu contato com alguem — risca o nome do caderno

O nosso programa vai fazer exatamente isso, mas com **produtos** em vez de contatos.

---

## Estrutura do Projeto

Nosso projeto CRUD vai evoluir ao longo de 4 módulos. Nesta primeira versão, a estrutura e simples:


```
crud-produtos/
    crud_memory.py         # Programa principal (CRUD em memoria)
```

Nos proximos módulos, essa estrutura vai crescer:

```
crud-produtos/
    crud_memory.py         # Modulo 29 — CRUD em memoria
    crud_sqlite.py         # Modulo 30 — CRUD com SQLite
    database.py            # Modulo 30 — Conexao com banco de dados
    main.py                # Modulo 31 — Aplicacao FastAPI
    models.py              # Modulo 31 — Modelos de dados
    routes.py              # Modulo 31 — Rotas da API
    requirements.txt       # Modulo 31 — Dependencias
    products.db            # Modulo 30 — Banco de dados (gerado)
```

> Não se preocupe com os arquivos dos proximos módulos agora. Vamos focar apenas no `crud_memory.py`.

---

## O Modelo de Dados: Produto

Antes de começar a programar, precisamos definir **o que e um produto** no nosso sistema. Isso e a modelagem de dados que você aprendeu no módulo 28.

Cada produto sera um **dicionário** com os seguintes campos:

```python
# Modelo de dados de um produto
# "product" = produto
product = {
    "id": 1,                 # Identificador unico (id = identificador)
    "name": "Arroz",         # Nome do produto (name = nome)
    "price": 5.99,           # Preco do produto (price = preco)
    "quantity": 10,          # Quantidade em estoque (quantity = quantidade)
    "category": "Alimentos"  # Categoria do produto (category = categoria)
}
```

| Campo | Tipo | Descricao | Regra de Validação |
|-------|------|-----------|-------------------|
| id | int | Identificador único, gerado automaticamente | Sempre positivo, nunca repetido |
| name | str | Nome do produto | Não pode ser vazio |
| price | float | Preco em reais | Deve ser >= 0 (zero = gratuito) |
| quantity | int | Quantidade em estoque | Deve ser >= 0 |
| category | str | Categoria do produto | Não pode ser vazia |

---

## Construindo o CRUD Passo a Passo

Vamos construir o programa de forma **progressiva**, adicionando uma funcionalidade de cada vez.

### Passo 1: A Lista de Produtos e o Contador de IDs

Primeiro, precisamos de um lugar para armazenar os produtos e um contador para gerar IDs unicos:

```python
# Lista que armazena todos os produtos cadastrados
# "products" = produtos (lista de dicionarios)
products = []

# Contador para gerar identificadores unicos
# "next_id" = proximo identificador
next_id = 1
```

A lista `products` comeca vazia. Cada produto cadastrado sera adicionado a essa lista como um dicionário. O `next_id` comeca em 1 e sera incrementado a cada novo produto.

> **Importante:** Como os dados ficam na memória (na variável `products`), eles serao perdidos quando o programa fechar. No módulo 30, você aprendera a resolver isso com SQLite.

### Passo 2: Função de Validação

Antes de cadastrar um produto, precisamos verificar se os dados sao validos:

```python
# Funcao que valida os dados de um produto antes de cadastrar
# "validate" = validar, "product" = produto, "data" = dados
def validate_product_data(name, price, quantity, category):
    """Valida os dados de um produto e retorna lista de erros."""
    # Lista para armazenar mensagens de erro encontradas
    # "errors" = erros
    errors = []

    # Validacao do nome: nao pode ser vazio nem so espacos
    # strip() remove espacos em branco das pontas
    if not name or name.strip() == "":
        # Adicionamos a mensagem de erro a lista
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
```

Saida esperada (exemplo de uso):
```python
errors = validate_product_data("", -5, -1, "")
print(errors)
```
```
['Nome nao pode ser vazio', 'Preco nao pode ser negativo', 'Quantidade nao pode ser negativa', 'Categoria nao pode ser vazia']
```


### Passo 3: Create — Cadastrar Produto

A função de criação valida os dados, monta o dicionário do produto e adiciona a lista:

```python
# Funcao que cadastra um novo produto na lista
# "create" = criar, "product" = produto
def create_product(name, price, quantity, category):
    """Cadastra um novo produto apos validar os dados."""
    # Acessamos o contador global de IDs
    global next_id

    # Validamos os dados antes de cadastrar
    # "errors" = erros
    errors = validate_product_data(name, price, quantity, category)

    # Se houver erros, exibimos e retornamos None (nenhum produto criado)
    if len(errors) > 0:
        print(f"Erro ao cadastrar produto:")
        # Exibimos cada mensagem de erro
        for error in errors:
            print(f"  - {error}")
        return None

    # Montamos o dicionario do produto com os dados validados
    # "product" = produto
    product = {
        "id": next_id,          # Usamos o contador como identificador
        "name": name,           # Nome do produto (name = nome)
        "price": price,         # Preco do produto (price = preco)
        "quantity": quantity,   # Quantidade (quantity = quantidade)
        "category": category    # Categoria (category = categoria)
    }

    # Adicionamos o produto a lista global
    # append() adiciona um item ao final da lista
    products.append(product)

    # Incrementamos o contador para o proximo produto
    next_id = next_id + 1

    # Informamos o sucesso ao usuario
    print(f"Produto '{name}' cadastrado com sucesso! ID: {product['id']}")

    # Retornamos o produto criado
    return product
```

Saida esperada:
```
Produto 'Arroz' cadastrado com sucesso! ID: 1
```

### Passo 4: Read — Listar e Buscar Produtos

Precisamos de funções para listar todos os produtos e buscar um produto específico:

```python
# Funcao que lista todos os produtos cadastrados
# "list" = listar, "all" = todos, "products" = produtos
def list_all_products():
    """Exibe todos os produtos cadastrados."""
    # Verificamos se a lista esta vazia
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Exibimos o cabecalho da tabela
    print("\n--- Lista de Produtos ---")
    print(f"{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)

    # Percorremos cada produto na lista
    # "product" = produto
    for product in products:
        # Exibimos os dados formatados em colunas
        # :<5 alinha a esquerda com 5 caracteres
        # :>10 alinha a direita com 10 caracteres
        # :.2f formata com 2 casas decimais
        print(f"{product['id']:<5} {product['name']:<20} {product['price']:>10.2f} {product['quantity']:>5} {product['category']:<15}")

    # Exibimos o total de produtos
    print(f"\nTotal: {len(products)} produto(s)")


# Funcao que busca um produto pelo identificador
# "find" = encontrar, "product" = produto, "by" = por, "id" = identificador
def find_product_by_id(product_id):
    """Busca um produto pelo ID e retorna o dicionario ou None."""
    # Percorremos cada produto na lista
    for product in products:
        # Comparamos o ID do produto com o ID buscado
        if product["id"] == product_id:
            # Encontramos — retornamos o produto
            return product
    # Se o loop terminou sem encontrar, retornamos None
    return None
```

Saida esperada (list_all_products com 2 produtos):
```
--- Lista de Produtos ---
ID    Nome                     Preco   Qtd Categoria
------------------------------------------------------------
1     Arroz                     8.99    50 Alimentos
2     Sabao                     4.50    80 Limpeza

Total: 2 produto(s)
```

### Passo 5: Update — Atualizar Produto

A função de atualização busca o produto pelo ID e permite alterar seus dados:

```python
# Funcao que atualiza os dados de um produto existente
# "update" = atualizar, "product" = produto
def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto existente."""
    # Buscamos o produto pelo ID
    # "product" = produto
    product = find_product_by_id(product_id)

    # Verificamos se o produto foi encontrado
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False

    # Validamos os novos dados
    # "errors" = erros
    errors = validate_product_data(name, price, quantity, category)

    # Se houver erros, exibimos e nao atualizamos
    if len(errors) > 0:
        print(f"Erro ao atualizar produto:")
        for error in errors:
            print(f"  - {error}")
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
```

Saida esperada:
```
Produto ID 1 atualizado com sucesso!
```

### Passo 6: Delete — Excluir Produto

A função de exclusao busca o produto pelo ID e remove da lista:

```python
# Funcao que exclui um produto da lista
# "delete" = excluir, "product" = produto
def delete_product(product_id):
    """Remove um produto da lista pelo ID."""
    # Buscamos o produto pelo ID
    # "product" = produto
    product = find_product_by_id(product_id)

    # Verificamos se o produto foi encontrado
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False

    # Guardamos o nome antes de remover (para a mensagem)
    # "product_name" = nome do produto
    product_name = product["name"]

    # Removemos o produto da lista
    # remove() encontra e remove o item da lista
    products.remove(product)

    # Informamos o sucesso
    print(f"Produto '{product_name}' (ID {product_id}) excluido com sucesso!")
    return True
```

Saida esperada:
```
Produto 'Arroz' (ID 1) excluido com sucesso!
```


### Passo 7: Menu Interativo

Agora vamos criar o menu que permite ao usuario interagir com o sistema:

```python
# Funcao que exibe o menu de opcoes
# "show" = mostrar, "menu" = menu de opcoes
def show_menu():
    """Exibe o menu principal do sistema."""
    print("\n========================================")
    print("   SISTEMA DE CADASTRO DE PRODUTOS")
    print("========================================")
    print("1. Cadastrar produto")
    print("2. Listar todos os produtos")
    print("3. Buscar produto por ID")
    print("4. Atualizar produto")
    print("5. Excluir produto")
    print("0. Sair")
    print("========================================")
```

### Passo 8: Funções de Interação com o Usuario

Precisamos de funções que leiam os dados do usuario pelo terminal:

```python
# Funcao que le os dados de um produto do usuario
# "read" = ler, "product" = produto, "input" = entrada
def read_product_input():
    """Le os dados de um produto a partir do teclado."""
    # Pedimos cada campo ao usuario
    # input() sempre retorna uma string
    # "name" = nome
    name = input("Nome do produto: ")

    # Pedimos o preco e convertemos para float
    # "price" = preco
    try:
        price = float(input("Preco (ex: 9.99): "))
    except ValueError:
        print("Preco invalido. Use apenas numeros.")
        return None

    # Pedimos a quantidade e convertemos para int
    # "quantity" = quantidade
    try:
        quantity = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Quantidade invalida. Use apenas numeros inteiros.")
        return None

    # Pedimos a categoria
    # "category" = categoria
    category = input("Categoria: ")

    # Retornamos os dados como uma tupla
    return name, price, quantity, category


# Funcao que executa a opcao de cadastrar produto
# "handle" = tratar/executar, "create" = criar
def handle_create():
    """Executa o fluxo de cadastro de produto."""
    print("\n--- Cadastrar Novo Produto ---")
    # Lemos os dados do usuario
    # "data" = dados
    data = read_product_input()
    # Se a leitura falhou, retornamos
    if data is None:
        return
    # Desempacotamos os dados da tupla
    name, price, quantity, category = data
    # Chamamos a funcao de criacao
    create_product(name, price, quantity, category)


# Funcao que executa a opcao de buscar produto
# "handle" = tratar/executar, "search" = buscar
def handle_search():
    """Executa o fluxo de busca por ID."""
    print("\n--- Buscar Produto por ID ---")
    try:
        # Pedimos o ID ao usuario
        # "product_id" = identificador do produto
        product_id = int(input("Digite o ID do produto: "))
    except ValueError:
        print("ID invalido. Use apenas numeros inteiros.")
        return

    # Buscamos o produto
    # "product" = produto
    product = find_product_by_id(product_id)

    # Verificamos se encontrou
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
    else:
        # Exibimos os dados do produto encontrado
        print(f"\nProduto encontrado:")
        print(f"  ID:         {product['id']}")
        print(f"  Nome:       {product['name']}")
        print(f"  Preco:      R$ {product['price']:.2f}")
        print(f"  Quantidade: {product['quantity']}")
        print(f"  Categoria:  {product['category']}")


# Funcao que executa a opcao de atualizar produto
# "handle" = tratar/executar, "update" = atualizar
def handle_update():
    """Executa o fluxo de atualizacao de produto."""
    print("\n--- Atualizar Produto ---")
    try:
        # Pedimos o ID do produto a ser atualizado
        product_id = int(input("Digite o ID do produto a atualizar: "))
    except ValueError:
        print("ID invalido. Use apenas numeros inteiros.")
        return

    # Verificamos se o produto existe antes de pedir os novos dados
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return

    # Mostramos os dados atuais
    print(f"Dados atuais: {product['name']} - R$ {product['price']:.2f} - {product['quantity']} un. - {product['category']}")
    print("Digite os novos dados:")

    # Lemos os novos dados
    data = read_product_input()
    if data is None:
        return
    name, price, quantity, category = data

    # Chamamos a funcao de atualizacao
    update_product(product_id, name, price, quantity, category)


# Funcao que executa a opcao de excluir produto
# "handle" = tratar/executar, "delete" = excluir
def handle_delete():
    """Executa o fluxo de exclusao de produto."""
    print("\n--- Excluir Produto ---")
    try:
        # Pedimos o ID do produto a ser excluido
        product_id = int(input("Digite o ID do produto a excluir: "))
    except ValueError:
        print("ID invalido. Use apenas numeros inteiros.")
        return

    # Verificamos se o produto existe
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return

    # Pedimos confirmacao antes de excluir
    print(f"Tem certeza que deseja excluir '{product['name']}'?")
    # "confirmation" = confirmacao
    confirmation = input("Digite 's' para confirmar: ")

    if confirmation.lower() == "s":
        delete_product(product_id)
    else:
        print("Exclusao cancelada.")
```


### Passo 9: Loop Principal

Finalmente, o loop principal que mantem o programa rodando ate o usuario escolher sair:

```python
# Funcao principal que executa o loop do programa
# "main" = principal
def main():
    """Funcao principal que executa o loop do menu."""
    print("Bem-vindo ao Sistema de Cadastro de Produtos!")
    print("(Os dados ficam na memoria e serao perdidos ao fechar o programa)")

    # Loop infinito que mantem o programa rodando
    # O loop so para quando o usuario escolher "0" (sair)
    while True:
        # Exibimos o menu de opcoes
        show_menu()

        # Lemos a opcao escolhida pelo usuario
        # "choice" = escolha
        choice = input("Escolha uma opcao: ")

        # Verificamos qual opcao foi escolhida
        if choice == "1":
            handle_create()
        elif choice == "2":
            list_all_products()
        elif choice == "3":
            handle_search()
        elif choice == "4":
            handle_update()
        elif choice == "5":
            handle_delete()
        elif choice == "0":
            print("\nObrigado por usar o sistema! Ate a proxima.")
            # break interrompe o loop while
            break
        else:
            print("Opcao invalida. Tente novamente.")


# Executamos a funcao principal
# Esta linha so executa se o arquivo for rodado diretamente
# (nao quando importado como modulo)
if __name__ == "__main__":
    main()
```

### Programa Completo

Aqui esta o programa completo reunindo todos os passos. Salve como `crud_memory.py`:

```python
# ============================================================
# CRUD de Produtos em Memoria — Versao 1
# Armazenamento: lista de dicionarios (dados temporarios)
# ============================================================
# "crud" = Create, Read, Update, Delete (Criar, Ler, Atualizar, Excluir)
# "memory" = memoria (os dados ficam na memoria do programa)

# Lista global que armazena todos os produtos cadastrados
# "products" = produtos
products = []

# Contador global para gerar identificadores unicos
# "next_id" = proximo identificador
next_id = 1


# --- Funcoes de Validacao ---

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
        errors.append("Quantidade deve ser um numero inteiro")
    elif quantity < 0:
        errors.append("Quantidade nao pode ser negativa")
    # Categoria nao pode ser vazia
    if not category or category.strip() == "":
        errors.append("Categoria nao pode ser vazia")
    return errors


# --- Funcoes CRUD ---

def create_product(name, price, quantity, category):
    """Cadastra um novo produto apos validar os dados."""
    global next_id
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao cadastrar produto:")
        for error in errors:
            print(f"  - {error}")
        return None
    product = {
        "id": next_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "category": category
    }
    products.append(product)
    next_id = next_id + 1
    print(f"Produto '{name}' cadastrado com sucesso! ID: {product['id']}")
    return product


def list_all_products():
    """Exibe todos os produtos cadastrados."""
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return
    print(f"\n{'ID':<5} {'Nome':<20} {'Preco':>10} {'Qtd':>5} {'Categoria':<15}")
    print("-" * 60)
    for product in products:
        print(f"{product['id']:<5} {product['name']:<20} {product['price']:>10.2f} {product['quantity']:>5} {product['category']:<15}")
    print(f"\nTotal: {len(products)} produto(s)")


def find_product_by_id(product_id):
    """Busca um produto pelo ID e retorna o dicionario ou None."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def update_product(product_id, name, price, quantity, category):
    """Atualiza os dados de um produto existente."""
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    errors = validate_product_data(name, price, quantity, category)
    if len(errors) > 0:
        print("Erro ao atualizar produto:")
        for error in errors:
            print(f"  - {error}")
        return False
    product["name"] = name
    product["price"] = price
    product["quantity"] = quantity
    product["category"] = category
    print(f"Produto ID {product_id} atualizado com sucesso!")
    return True


def delete_product(product_id):
    """Remove um produto da lista pelo ID."""
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return False
    product_name = product["name"]
    products.remove(product)
    print(f"Produto '{product_name}' (ID {product_id}) excluido com sucesso!")
    return True


# --- Funcoes de Interface ---

def show_menu():
    """Exibe o menu principal do sistema."""
    print("\n========================================")
    print("   SISTEMA DE CADASTRO DE PRODUTOS")
    print("========================================")
    print("1. Cadastrar produto")
    print("2. Listar todos os produtos")
    print("3. Buscar produto por ID")
    print("4. Atualizar produto")
    print("5. Excluir produto")
    print("0. Sair")
    print("========================================")


def read_product_input():
    """Le os dados de um produto a partir do teclado."""
    name = input("Nome do produto: ")
    try:
        price = float(input("Preco (ex: 9.99): "))
    except ValueError:
        print("Preco invalido. Use apenas numeros.")
        return None
    try:
        quantity = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Quantidade invalida. Use apenas numeros inteiros.")
        return None
    category = input("Categoria: ")
    return name, price, quantity, category


def handle_create():
    """Executa o fluxo de cadastro de produto."""
    print("\n--- Cadastrar Novo Produto ---")
    data = read_product_input()
    if data is None:
        return
    name, price, quantity, category = data
    create_product(name, price, quantity, category)


def handle_search():
    """Executa o fluxo de busca por ID."""
    print("\n--- Buscar Produto por ID ---")
    try:
        product_id = int(input("Digite o ID do produto: "))
    except ValueError:
        print("ID invalido. Use apenas numeros inteiros.")
        return
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
    else:
        print(f"\nProduto encontrado:")
        print(f"  ID:         {product['id']}")
        print(f"  Nome:       {product['name']}")
        print(f"  Preco:      R$ {product['price']:.2f}")
        print(f"  Quantidade: {product['quantity']}")
        print(f"  Categoria:  {product['category']}")


def handle_update():
    """Executa o fluxo de atualizacao de produto."""
    print("\n--- Atualizar Produto ---")
    try:
        product_id = int(input("Digite o ID do produto a atualizar: "))
    except ValueError:
        print("ID invalido. Use apenas numeros inteiros.")
        return
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return
    print(f"Dados atuais: {product['name']} - R$ {product['price']:.2f}")
    print("Digite os novos dados:")
    data = read_product_input()
    if data is None:
        return
    name, price, quantity, category = data
    update_product(product_id, name, price, quantity, category)


def handle_delete():
    """Executa o fluxo de exclusao de produto."""
    print("\n--- Excluir Produto ---")
    try:
        product_id = int(input("Digite o ID do produto a excluir: "))
    except ValueError:
        print("ID invalido. Use apenas numeros inteiros.")
        return
    product = find_product_by_id(product_id)
    if product is None:
        print(f"Produto com ID {product_id} nao encontrado.")
        return
    print(f"Tem certeza que deseja excluir '{product['name']}'?")
    confirmation = input("Digite 's' para confirmar: ")
    if confirmation.lower() == "s":
        delete_product(product_id)
    else:
        print("Exclusao cancelada.")


def main():
    """Funcao principal que executa o loop do menu."""
    print("Bem-vindo ao Sistema de Cadastro de Produtos!")
    print("(Os dados ficam na memoria e serao perdidos ao fechar)")
    while True:
        show_menu()
        choice = input("Escolha uma opcao: ")
        if choice == "1":
            handle_create()
        elif choice == "2":
            list_all_products()
        elif choice == "3":
            handle_search()
        elif choice == "4":
            handle_update()
        elif choice == "5":
            handle_delete()
        elif choice == "0":
            print("\nObrigado por usar o sistema! Ate a proxima.")
            break
        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
```

Para executar:

```bash
# Navegamos ate a pasta do projeto
cd ~/meus-projetos/crud-produtos

# Executamos o programa
python3 crud_memory.py
```

> O programa exibe o menu e aguarda sua escolha. Teste cadastrando alguns produtos, listando, buscando, atualizando e excluindo.


---

## Entendendo Cada Operação em Detalhe

### Create — Por Que Validar Antes de Cadastrar?

Imagine que você esta preenchendo um formulário de cadastro em um site. Se você deixar o campo "nome" vazio e clicar em "enviar", o site mostra uma mensagem de erro pedindo para preencher o campo. Isso e **validação**.

No nosso programa, a função `validate_product_data` faz esse papel. Ela verifica cada campo antes de permitir o cadastro. Isso evita que dados incorretos entrem no sistema.

### Read — Duas Formas de Consultar

Nosso sistema oferece duas formas de consultar produtos:

1. **Listar todos** (`list_all_products`): mostra uma tabela com todos os produtos. Útil para ter uma visao geral do estoque.
2. **Buscar por ID** (`find_product_by_id`): encontra um produto específico. Útil quando você sabe qual produto quer ver.

### Update — Por Que Buscar Antes de Atualizar?

Antes de atualizar um produto, precisamos verificar se ele existe. Não faz sentido tentar alterar algo que não esta no sistema. Por isso, a função `update_product` primeiro busca o produto pelo ID e so depois aplica as alteracoes.

### Delete — Por Que Pedir Confirmacao?

Excluir um produto e uma ação que não pode ser desfeita (nesta versão). Por isso, o programa pede confirmacao antes de excluir. Isso e uma boa prática de usabilidade — protege o usuario de exclusoes acidentais.

### O Papel do `if __name__ == "__main__"`

No final do programa, você viu esta linha:

```python
# Esta linha verifica se o arquivo esta sendo executado diretamente
# Se sim, chama a funcao main()
# Se o arquivo for importado como modulo, esta linha nao executa
if __name__ == "__main__":
    main()
```

Quando você executa `python3 crud_memory.py`, o Python define `__name__` como `"__main__"`. Isso significa que o arquivo esta sendo executado diretamente, e a função `main()` sera chamada.

Se outro arquivo importar `crud_memory.py` como módulo (por exemplo, `import crud_memory`), o `__name__` sera `"crud_memory"` em vez de `"__main__"`, e a função `main()` **não** sera chamada automaticamente. Isso permite reutilizar as funções sem executar o menu.

---

## Limitacoes da Versão em Memória

Esta primeira versão tem uma limitacao importante: **os dados sao temporarios**. Quando você fecha o programa, todos os produtos cadastrados sao perdidos.

Isso acontece porque os dados ficam armazenados na variável `products`, que existe apenas na **memória RAM** do computador enquanto o programa esta rodando. Quando o programa termina, a memória e liberada e os dados desaparecem.

No próximo módulo (30 — CRUD com SQLite), você vai aprender a resolver esse problema salvando os dados em um **banco de dados**, que e um arquivo no disco do computador. Assim, os dados persistem mesmo depois de fechar o programa.

---

## Para Saber Mais

- [W3Schools — Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
  _Referencia completa sobre dicionários em Python, a estrutura que usamos para representar produtos_
- [W3Schools — Python Lists](https://www.w3schools.com/python/python_lists.asp)
  _Referencia sobre listas, que usamos para armazenar a coleção de produtos_
- [W3Schools — Python Functions](https://www.w3schools.com/python/python_functions.asp)
  _Revisao sobre funções, que sao a base da organização do nosso CRUD_
- [W3Schools — Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
  _Referencia sobre o loop while, usado no menu principal do programa_
- [Documentação Oficial Python — Estruturas de Dados](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
  _Tutorial oficial sobre listas, dicionários e outras estruturas de dados_
- [Documentação Oficial Python — Funções](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions)
  _Tutorial oficial sobre definição e uso de funcoes_

---

## Perguntas Frequentes (FAQ)

**P: O que significa CRUD?**
R: CRUD e uma sigla em ingles para Create (Criar), Read (Ler), Update (Atualizar) e Delete (Excluir). Sao as quatro operações básicas que podemos fazer com dados em qualquer sistema. Praticamente todo aplicativo que você usa — redes sociais, lojas online, aplicativos de banco — usa CRUD por tras.

**P: Por que os dados somem quando fecho o programa?**
R: Porque os dados estão armazenados na memória RAM do computador, dentro da variável `products`. A memória RAM e temporária — quando o programa termina, ela e liberada. No módulo 30, você vai aprender a salvar os dados em um banco de dados SQLite, que e um arquivo no disco e persiste mesmo apos fechar o programa.

**P: O que e uma lista de dicionários?**
R: E uma lista onde cada item e um dicionário. No nosso caso, `products` e uma lista onde cada item e um dicionário representando um produto (com id, name, price, quantity e category). Pense em uma pasta de fichas: a pasta e a lista e cada ficha e um dicionário.

**P: Por que usar um contador global para o ID?**
R: O contador `next_id` garante que cada produto receba um identificador único. Mesmo que você exclua um produto, o ID dele não sera reutilizado. Isso evita confusao — se o produto 3 foi excluido, o próximo produto sera 4, nunca 3 novamente.

**P: Posso usar o ID do produto como índice da lista?**
R: Não e recomendado. O ID e um identificador logico do produto, e o índice da lista e a posição fisica. Quando você exclui um produto, os indices mudam, mas os IDs devem permanecer fixos. Por isso usamos `find_product_by_id` para buscar pelo ID em vez de acessar por índice.

**P: O que e `global` e por que preciso usar?**
R: A palavra `global` permite que uma função modifique uma variável definida fora dela. Sem `global`, a função criaria uma variável local com o mesmo nome, sem alterar a original. Usamos `global next_id` na função `create_product` porque precisamos incrementar o contador que esta fora da função.

**P: O que acontece se eu digitar letras quando o programa pede um número?**
R: O programa captura esse erro com `try/except`. Quando você digita "abc" e o programa tenta converter com `int()` ou `float()`, ocorre um `ValueError`. O bloco `except` captura esse erro e exibe uma mensagem amigavel em vez de travar o programa.

**P: Por que a função `validate_product_data` retorna uma lista de erros?**
R: Porque um produto pode ter vários problemas ao mesmo tempo (nome vazio E preco negativo E quantidade negativa). Retornando uma lista, podemos mostrar todos os erros de uma vez, em vez de mostrar um por um e obrigar o usuario a corrigir e tentar novamente várias vezes.

**P: O que significa `if __name__ == "__main__"`?**
R: Essa linha verifica se o arquivo esta sendo executado diretamente (com `python3 arquivo.py`) ou sendo importado como módulo. Se executado diretamente, `__name__` vale `"__main__"` e a função `main()` e chamada. Se importado, `__name__` vale o nome do arquivo e `main()` não e chamada automaticamente.

**P: Posso ter dois produtos com o mesmo nome?**
R: Sim, no nosso sistema isso e permitido. Cada produto tem um ID único que o identifica, então dois produtos podem ter o mesmo nome mas terao IDs diferentes. Em sistemas mais avancados, você poderia adicionar uma validação para impedir nomes duplicados.

**P: Por que usar `products.remove(product)` e não `del products[indice]`?**
R: Usamos `remove()` porque ja temos o dicionário do produto (encontrado por `find_product_by_id`). O `remove()` encontra e remove exatamente aquele dicionário da lista. Usar `del` com índice exigiria encontrar o índice primeiro, o que seria um passo extra.

**P: O que e `None` e por que as funções retornam `None`?**
R: `None` e um valor especial do Python que significa "nada" ou "nenhum valor". Quando `find_product_by_id` não encontra o produto, retorna `None` para indicar que a busca falhou. Quando `create_product` falha na validação, retorna `None` para indicar que nenhum produto foi criado.

**P: Posso adicionar mais campos ao produto?**
R: Sim. Como o produto e um dicionário, você pode adicionar quantos campos quiser: marca, fornecedor, data de validade, código de barras, etc. Basta adicionar a chave no dicionário e atualizar as funções de validação, criação e exibicao.

**P: O que e `f-string` e por que usamos tanto?**
R: F-string (formatted string literal) e uma forma de inserir valores de variáveis dentro de textos. Você coloca `f` antes das aspas e usa `{variavel}` para inserir valores. Por exemplo, `f"Preco: R$ {price:.2f}"` insere o valor de `price` formatado com 2 casas decimais.

**P: Por que separar o programa em tantas funções?**
R: Separar em funções torna o código mais organizado, fácil de entender e fácil de manter. Cada função tem uma única responsabilidade. Se você precisar corrigir a validação, sabe exatamente onde ir (`validate_product_data`). Se precisar mudar o menu, vai em `show_menu`. Isso e o principio da responsabilidade única.

**P: Esse programa funciona no Windows também?**
R: Sim. O programa usa apenas Python puro, sem dependências do sistema operacional. Funciona em Linux, Windows e macOS. A única diferença e o comando para executar: no Windows pode ser `python crud_memory.py` (sem o `3`).

**P: O que acontece se a lista de produtos ficar muito grande?**
R: Na versão em memória, a lista e limitada pela quantidade de RAM disponível. Para uso normal (centenas ou milhares de produtos), não ha problema. Para milhoes de registros, você precisaria de um banco de dados (como o SQLite do módulo 30), que e otimizado para grandes volumes de dados.

**P: Posso usar classes em vez de dicionários para os produtos?**
R: Sim, e seria uma otima prática. Você poderia criar uma classe `Product` com atributos e métodos. No módulo 31 (FastAPI), você vera algo parecido com os modelos Pydantic. Nesta versão, usamos dicionários para manter a simplicidade e reforcar o que você aprendeu nos módulos anteriores.

**P: Como faco para testar o programa sem digitar tudo manualmente?**
R: Você pode criar dados de teste no inicio do programa, antes do loop do menu. Por exemplo, adicione chamadas a `create_product("Arroz", 8.99, 50, "Alimentos")` logo apos definir as funções. Assim, o programa ja comeca com produtos cadastrados para você testar as outras operações.

**P: O que e o `:<5` e `:>10` na formatacao da tabela?**
R: Sao especificadores de alinhamento em f-strings. `:<5` alinha o texto a esquerda com largura de 5 caracteres. `:>10` alinha a direita com largura de 10. `:.2f` formata um número com 2 casas decimais. Isso cria colunas alinhadas na tabela de produtos.

---

## Exercícios

Os exercícios deste módulo estão em um arquivo separado para facilitar a navegação:

[Ir para os Exercícios do Módulo 29 ->](29-crud-memoria-exercicios.md)