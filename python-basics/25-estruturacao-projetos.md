# 25 — Estruturação de Projetos: Organizando Arquivos e Pastas em Python

[<- Anterior: Módulos e Imports](24-módulos-imports.md) | [Glossário](00-glossário.md) | [Próximo: pip e Dependências ->](26-pip-dependências.md)

---

## Introdução

No módulo anterior, você aprendeu a criar e importar módulos — arquivos Python que podem ser reutilizados em outros programas. Agora vamos dar um passo adiante: como **organizar** esses arquivos em pastas de forma que o projeto seja fácil de entender, manter e expandir.

Imagine que você esta montando um escritorio em casa. No inicio, você coloca tudo em cima da mesa: canetas, papeis, livros, carregadores, documentos. Funciona por um tempo. Mas conforme o escritorio cresce, encontrar algo vira um pesadelo. A solução e organizar: gaveta para canetas, pasta para documentos, prateleira para livros. Cada coisa no seu lugar.

Em programação, a **estruturação de projetos** e exatamente isso: decidir onde cada arquivo vai ficar, como as pastas serao nomeadas e como as responsabilidades serao divididas. Um projeto bem organizado e mais fácil de entender, de corrigir erros e de expandir com novas funcionalidades.

Neste módulo, você vai aprender:

- Como nomear arquivos e pastas seguindo as convencoes do Python
- Como organizar projetos de diferentes tamanhos (pequeno, medio, grande)
- O papel dos arquivos especiais: `__init__.py`, `__main__.py` e `setup.py`
- Como separar responsabilidades: dados, lógica e interface
- Boas práticas que profissionais usam no dia a dia

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

Os exemplos deste módulo envolvem criar estruturas de pastas e arquivos. Para praticar:

1. Abra o terminal (no Linux, pressione `Ctrl + Alt + T`)
2. Crie uma pasta para os exercícios:
   ```bash
   mkdir ~/meus-projetos/python-curso/módulo-25
   ```
   > O comando `mkdir` significa "make directory" (criar diretório/pasta)
3. Navegue ate a pasta:
   ```bash
   cd ~/meus-projetos/python-curso/módulo-25
   ```
4. Crie os arquivos e pastas conforme os exemplos

---

## Convencoes de Nomenclatura

Antes de organizar os arquivos, precisamos saber como **nomear** cada um deles. O Python e a comunidade de desenvolvedores seguem convencoes claras para isso.

### Regras para Nomes de Arquivos e Pastas

**1. Use snake_case (palavras separadas por sublinhado)**

O snake_case e o padrão para arquivos e pastas em Python. O nome "snake_case" vem da analogia com uma cobra (snake) — as palavras ficam deitadas, separadas por sublinhados, como uma cobra rastejando.

```
# CORRETO — snake_case
meu_projeto/
    calcular_media.py
    validar_dados.py
    lista_produtos.py

# ERRADO — outros formatos
meu_projeto/
    CalcularMedia.py      # CamelCase — reservado para nomes de classes
    calcular-media.py     # kebab-case — nao funciona como modulo Python
    calcular media.py     # espaco — causa erros no terminal
```

**2. Sem acentos e sem caracteres especiais**

Mesmo que o Python 3 suporte Unicode, evite acentos em nomes de arquivos e pastas. Isso garante compatibilidade em diferentes sistemas operacionais e evita problemas ao compartilhar o projeto.

```
# CORRETO — sem acentos
calcular_media.py
validacao_dados.py
configuracao.py

# EVITAR — com acentos
calcular_média.py
validação_dados.py
configuração.py
```

**3. Sem espacos**

Espacos em nomes de arquivos causam problemas no terminal. Sempre use sublinhado no lugar de espaco.

```
# CORRETO
lista_de_compras.py
cadastro_usuario.py

# ERRADO
lista de compras.py
cadastro usuario.py
```

**4. Letras minusculas**

Por convencao, nomes de arquivos e pastas em Python usam apenas letras minusculas.

```
# CORRETO
utils.py
helpers.py
models.py

# EVITAR
Utils.py
Helpers.py
MODELS.py
```

**5. Nomes descritivos e em ingles**

Seguindo a Convencao de Idioma do curso, os nomes de arquivos e pastas devem ser em ingles e descritivos — o nome deve deixar claro o que o arquivo contem.

```
# CORRETO — descritivo e em ingles
database.py          # banco de dados
validators.py        # validadores
product_routes.py    # rotas de produto
user_models.py       # modelos de usuario

# EVITAR — nomes vagos
arquivo1.py
codigo.py
temp.py
```

### Resumo das Convencoes

| Convencao | Correto | Evitar |
|-----------|---------|--------|
| Formato | `meu_arquivo.py` | `MeuArquivo.py`, `meu-arquivo.py` |
| Acentos | `validacao.py` | `validação.py` |
| Espacos | `lista_compras.py` | `lista compras.py` |
| Maiusculas | `helpers.py` | `Helpers.py`, `HELPERS.py` |
| Clareza | `product_validator.py` | `pv.py`, `arquivo1.py` |


---

## Estruturas de Projeto por Tamanho

Não existe uma única forma "certa" de organizar um projeto. A estrutura ideal depende do **tamanho** e da **complexidade** do projeto. Vamos ver tres exemplos: projeto pequeno, medio e grande.

### Projeto Pequeno (1 a 3 arquivos)

Quando você esta aprendendo ou criando algo simples, um projeto pequeno e suficiente. Todos os arquivos ficam na mesma pasta, sem subpastas.

**Analogia:** Pense em uma mesa de estudos com poucos itens — um caderno, uma caneta e uma borracha. Não precisa de gavetas nem organizadores. Tudo cabe na mesa.

```
calculadora/
    main.py
    calculator.py
    README.md
```

Vamos ver o que cada arquivo faz:

```python
# Arquivo: calculator.py
# Modulo com funcoes de calculo
# "calculator" = calculadora

# Funcao que soma dois numeros
# "add" = somar
def add(a, b):
    # Retorna a soma de a e b
    return a + b

# Funcao que subtrai dois numeros
# "subtract" = subtrair
def subtract(a, b):
    # Retorna a subtracao de a por b
    return a - b
```

```python
# Arquivo: main.py
# Arquivo principal que usa o modulo calculator
# "main" = principal

# Importamos as funcoes do nosso modulo calculator
from calculator import add, subtract

# Pedimos dois numeros ao usuario
# "first_number" = primeiro numero
first_number = float(input("Digite o primeiro numero: "))
# "second_number" = segundo numero
second_number = float(input("Digite o segundo numero: "))

# Calculamos e exibimos os resultados
# "sum_result" = resultado da soma
sum_result = add(first_number, second_number)
print(f"Soma: {sum_result}")

# "sub_result" = resultado da subtracao
sub_result = subtract(first_number, second_number)
print(f"Subtracao: {sub_result}")
```

Saida esperada:
```
Digite o primeiro numero: 10
Digite o segundo numero: 3
Soma: 13.0
Subtracao: 7.0
```

**Quando usar:** Exercícios do curso, scripts simples, automacoes rapidas.

### Projeto Medio (4 a 10 arquivos)

Conforme o projeto cresce, faz sentido separar os arquivos em pastas por **responsabilidade**. Cada pasta agrupa arquivos que fazem coisas parecidas.

**Analogia:** Agora sua mesa de estudos tem muitos itens. Você compra um organizador com divisorias: uma para canetas, outra para papeis, outra para livros. Cada divisoria tem um proposito claro.

```
cadastro_produtos/
    main.py
    README.md
    models/
        __init__.py
        product.py
    utils/
        __init__.py
        validators.py
        formatters.py
    data/
        products.json
```

Vamos entender cada pasta:

| Pasta/Arquivo | Função |
|---------------|--------|
| `main.py` | Ponto de entrada do programa — onde tudo comeca |
| `README.md` | Documentação do projeto — explica o que ele faz |
| `models/` | Modelos de dados — define a estrutura dos dados (produto) |
| `utils/` | Utilitarios — funções auxiliares (validação, formatacao) |
| `data/` | Dados — arquivos de dados do projeto (JSON, CSV) |
| `__init__.py` | Transforma a pasta em um pacote Python (veja módulo 24) |

Exemplo do arquivo `models/product.py`:

```python
# Arquivo: models/product.py
# Define a estrutura de um produto
# "product" = produto

# Funcao que cria um novo produto
# "create_product" = criar produto
# "name" = nome, "price" = preco, "quantity" = quantidade
def create_product(name, price, quantity):
    # Criamos um dicionario representando o produto
    # "product" = produto
    product = {
        "name": name,           # nome do produto
        "price": price,         # preco do produto
        "quantity": quantity     # quantidade em estoque
    }
    # Retornamos o dicionario do produto
    return product
```

Exemplo do arquivo `utils/validators.py`:

```python
# Arquivo: utils/validators.py
# Funcoes de validacao de dados
# "validators" = validadores

# Funcao que verifica se o nome e valido
# "is_valid_name" = e um nome valido
def is_valid_name(name):
    # O nome nao pode ser vazio apos remover espacos
    # strip() remove espacos do inicio e fim
    return name.strip() != ""

# Funcao que verifica se o preco e valido
# "is_valid_price" = e um preco valido
def is_valid_price(price):
    # O preco deve ser maior que zero
    return price > 0
```

Exemplo do arquivo `main.py` usando os módulos:

```python
# Arquivo: main.py
# Programa principal do cadastro de produtos
# "main" = principal

# Importamos funcoes dos nossos modulos usando importacao absoluta
# "models" = modelos, "product" = produto
from models.product import create_product
# "utils" = utilitarios, "validators" = validadores
from utils.validators import is_valid_name, is_valid_price

# Pedimos os dados do produto ao usuario
# "name" = nome
name = input("Nome do produto: ")

# Validamos o nome
if not is_valid_name(name):
    # Exibimos mensagem de erro se o nome for invalido
    print("Erro: nome nao pode ser vazio")
else:
    # Pedimos o preco e convertemos para float
    # "price" = preco
    price = float(input("Preco: "))

    # Validamos o preco
    if not is_valid_price(price):
        # Exibimos mensagem de erro se o preco for invalido
        print("Erro: preco deve ser maior que zero")
    else:
        # Pedimos a quantidade e convertemos para int
        # "quantity" = quantidade
        quantity = int(input("Quantidade: "))

        # Criamos o produto usando a funcao do modulo models
        # "product" = produto
        product = create_product(name, price, quantity)

        # Exibimos o produto cadastrado
        print(f"Produto cadastrado: {product}")
```

Saida esperada:
```
Nome do produto: Arroz
Preco: 5.99
Quantidade: 100
Produto cadastrado: {'name': 'Arroz', 'price': 5.99, 'quantity': 100}
```

**Quando usar:** Projetos do curso (como o CRUD), ferramentas com várias funcionalidades, programas com mais de 3 arquivos.

### Projeto Grande (10+ arquivos)

Projetos maiores precisam de uma organização mais rigorosa. A estrutura segue padrões usados pela comunidade Python profissional.

**Analogia:** Agora você não tem apenas uma mesa — tem um escritorio inteiro. Cada comodo tem uma função: sala de reunioes, arquivo morto, sala de trabalho, recepcao. Cada comodo e claramente identificado e tem um proposito específico.

```
meu_sistema/
    README.md
    requirements.txt
    setup.py
    main.py
    src/
        __init__.py
        models/
            __init__.py
            product.py
            user.py
        services/
            __init__.py
            product_service.py
            user_service.py
        utils/
            __init__.py
            validators.py
            formatters.py
            helpers.py
        routes/
            __init__.py
            product_routes.py
            user_routes.py
    data/
        products.json
        users.json
    tests/
        __init__.py
        test_product.py
        test_user.py
    docs/
        guia_usuario.md
        arquitetura.md
```

Vamos entender cada pasta:

| Pasta | Função | Analogia |
|-------|--------|----------|
| `src/` | Código-fonte principal | Sala de trabalho — onde o trabalho acontece |
| `src/models/` | Modelos de dados | Formularios — definem a estrutura dos dados |
| `src/services/` | Lógica de negocio | Funcionarios — fazem o trabalho real |
| `src/utils/` | Funções auxiliares | Ferramentas — ajudam nas tarefas |
| `src/routes/` | Rotas da API (se houver) | Recepcao — recebe e direciona pedidos |
| `data/` | Arquivos de dados | Arquivo morto — armazena informações |
| `tests/` | Testes automatizados | Controle de qualidade — verifica se tudo funciona |
| `docs/` | Documentação | Manual de instruções — explica como tudo funciona |

**Quando usar:** Projetos profissionais, sistemas com multiplas funcionalidades, projetos colaborativos com mais de uma pessoa.

> **Nota para iniciantes:** Você não precisa usar essa estrutura agora. Comece com projetos pequenos e va crescendo conforme a necessidade. O importante e entender que essa organização existe e por que ela e útil.

---

## Arquivos Especiais do Python

O Python tem alguns arquivos com nomes especiais que desempenham papeis importantes na organização de projetos. Vamos conhecer os tres principais.

### O Arquivo __init__.py

Você ja conheceu o `__init__.py` no módulo anterior (módulo 24). Vamos relembrar e aprofundar.

O `__init__.py` (pronuncia-se "dunder init" — "dunder" vem de "double underscore", que significa "duplo sublinhado") e o arquivo que transforma uma pasta comum em um **pacote Python**. Sem ele, o Python não reconhece a pasta como um pacote e você não consegue importar módulos dela.

**Analogia:** O `__init__.py` e como a placa na porta de uma sala em um predio comercial. Sem a placa, ninguem sabe o que tem la dentro. Com a placa, todos sabem que aquela sala contem algo útil.

O `__init__.py` pode estar **vazio** — sua simples existência ja e suficiente:

```python
# Arquivo: utils/__init__.py
# Este arquivo transforma a pasta "utils" em um pacote Python
# Pode estar vazio — sua existencia ja e suficiente
```

Ou pode conter **imports de conveniencia** para facilitar o uso do pacote:

```python
# Arquivo: utils/__init__.py
# Importamos as funcoes mais usadas para facilitar o acesso
# Assim, quem importar o pacote utils pode acessar diretamente

# "validators" = validadores
from utils.validators import is_valid_name, is_valid_price
# "formatters" = formatadores
from utils.formatters import format_price, format_name
```

Com esse `__init__.py`, em vez de escrever:

```python
# Sem __init__.py configurado — caminho completo
from utils.validators import is_valid_name
```

Você pode escrever:

```python
# Com __init__.py configurado — mais curto
from utils import is_valid_name
```

**Regra prática:** Para projetos simples, crie o `__init__.py` vazio. Para projetos maiores, use-o para exportar as funções mais importantes do pacote.

### O Arquivo __main__.py

O `__main__.py` (pronuncia-se "dunder main") e um arquivo especial que permite **executar um pacote inteiro** como se fosse um programa. Quando você executa `python3 -m nome_do_pacote`, o Python procura e executa o `__main__.py` dentro desse pacote.

**Analogia:** Pense em um restaurante. Ele tem cozinha, salao, estoque — várias partes. Mas quando um cliente chega, ele entra pela **porta principal**. O `__main__.py` e a porta principal do seu pacote — o ponto de entrada.

Vamos ver um exemplo. Considere a seguinte estrutura:

```
calculadora/
    __init__.py
    __main__.py
    operations.py
```

**Arquivo `calculadora/operations.py`** (operações):

```python
# Arquivo: calculadora/operations.py
# Modulo com operacoes matematicas
# "operations" = operacoes

# Funcao que soma dois numeros
# "add" = somar
def add(a, b):
    # Retorna a soma
    return a + b

# Funcao que multiplica dois numeros
# "multiply" = multiplicar
def multiply(a, b):
    # Retorna a multiplicacao
    return a * b
```

**Arquivo `calculadora/__init__.py`** (vazio):

```python
# Arquivo: calculadora/__init__.py
# Transforma a pasta em um pacote Python
```

**Arquivo `calculadora/__main__.py`** (ponto de entrada):

```python
# Arquivo: calculadora/__main__.py
# Ponto de entrada quando o pacote e executado com python3 -m
# "main" = principal

# Importamos as funcoes do modulo operations
# "operations" = operacoes
from calculadora.operations import add, multiply

# Exibimos uma mensagem de boas-vindas
print("=== Calculadora Simples ===")

# Pedimos dois numeros ao usuario
# "first" = primeiro, "second" = segundo
first = float(input("Primeiro numero: "))
second = float(input("Segundo numero: "))

# Calculamos e exibimos os resultados
# "sum_result" = resultado da soma
sum_result = add(first, second)
print(f"Soma: {sum_result}")

# "product_result" = resultado da multiplicacao
product_result = multiply(first, second)
print(f"Multiplicacao: {product_result}")
```

**Como executar:**

Para executar o pacote, use o terminal na pasta **acima** da pasta `calculadora`:

```bash
python3 -m calculadora
```

> O `-m` significa "module" (módulo). Esse comando diz ao Python: "execute o pacote `calculadora` como um programa".

Saida esperada:
```
=== Calculadora Simples ===
Primeiro numero: 8
Segundo numero: 5
Soma: 13.0
Multiplicacao: 40.0
```

**Quando usar o __main__.py:**
- Quando você quer que um pacote inteiro possa ser executado como programa
- Quando você quer um ponto de entrada claro para o seu projeto
- Quando você distribui seu código como pacote e quer que outros possam executa-lo facilmente

### O Arquivo setup.py

O `setup.py` e um arquivo de configuração usado para **distribuir** seu projeto Python como um pacote instalavel. Ele contem informações sobre o projeto: nome, versão, autor, dependências e outros metadados.

**Analogia:** Pense no `setup.py` como a **etiqueta de um produto** no supermercado. A etiqueta contem o nome do produto, o fabricante, os ingredientes e o preco. Sem a etiqueta, ninguem sabe o que e o produto. O `setup.py` e a etiqueta do seu projeto Python.

Vamos ver um exemplo simples:

```python
# Arquivo: setup.py
# Configuracao para distribuir o projeto como pacote
# "setup" = configuracao/instalacao

# Importamos a funcao setup do modulo setuptools
# "setuptools" = ferramentas de configuracao
from setuptools import setup, find_packages

# Chamamos a funcao setup com as informacoes do projeto
setup(
    # "name" = nome do pacote
    name="calculadora",
    # "version" = versao do pacote
    version="1.0.0",
    # "description" = descricao do pacote
    description="Uma calculadora simples em Python",
    # "author" = autor do pacote
    author="Seu Nome",
    # "packages" = pacotes incluidos
    # find_packages() encontra automaticamente todos os pacotes
    packages=find_packages(),
    # "python_requires" = versao minima do Python necessaria
    python_requires=">=3.8",
)
```

> **Nota para iniciantes:** Você não precisa criar um `setup.py` agora. Esse arquivo e mais usado quando você quer compartilhar seu projeto com outras pessoas ou pública-lo na internet. Nos módulos seguintes (módulo 26 — pip e Dependências), você aprendera mais sobre instalacao de pacotes.

**Quando usar o setup.py:**
- Quando você quer instalar seu projeto com `pip install .`
- Quando você quer compartilhar seu projeto com outras pessoas
- Quando você quer publicar seu pacote no PyPI (repositório público de pacotes Python)

---

## Separacao de Responsabilidades

Um dos principios mais importantes da organização de projetos e a **separacao de responsabilidades**. Isso significa que cada arquivo e cada pasta devem ter uma **única função clara**.

**Analogia:** Em uma cozinha bem organizada, cada utensilio tem seu lugar e sua função. A faca corta, a panela cozinha, o prato serve. Você não usa a faca para servir nem o prato para cortar. Cada um faz o que sabe fazer melhor.

Em programação, dividimos o código em tres grandes areas:

### 1. Dados (Models)

Os arquivos de **dados** (models = modelos) definem a **estrutura** das informações que o programa manipula. Eles respondem a pergunta: "como sao os dados?"

```python
# Arquivo: models/product.py
# Define a estrutura de dados de um produto
# "product" = produto

# Funcao que cria um novo produto com todos os campos necessarios
# "create_product" = criar produto
def create_product(product_id, name, price, quantity, category):
    # Criamos um dicionario com os dados do produto
    # "product" = produto
    product = {
        "id": product_id,           # identificador unico
        "name": name,               # nome do produto
        "price": price,             # preco do produto
        "quantity": quantity,        # quantidade em estoque
        "category": category         # categoria do produto
    }
    # Retornamos o dicionario do produto
    return product

# Funcao que exibe os dados de um produto formatados
# "display_product" = exibir produto
def display_product(product):
    # Exibimos cada campo do produto
    print(f"ID: {product['id']}")
    print(f"Nome: {product['name']}")
    print(f"Preco: R$ {product['price']:.2f}")
    print(f"Quantidade: {product['quantity']}")
    print(f"Categoria: {product['category']}")
```

### 2. Lógica (Services)

Os arquivos de **lógica** (services = servicos) contem as **regras de negocio** — o que o programa faz com os dados. Eles respondem a pergunta: "o que fazer com os dados?"

```python
# Arquivo: services/product_service.py
# Logica de negocio para gerenciar produtos
# "product_service" = servico de produto

# Importamos a funcao de criacao de produto
from models.product import create_product

# Lista que armazena todos os produtos cadastrados
# "product_list" = lista de produtos
product_list = []

# Variavel que controla o proximo ID disponivel
# "next_id" = proximo identificador
next_id = 1

# Funcao que adiciona um novo produto a lista
# "add_product" = adicionar produto
def add_product(name, price, quantity, category):
    # Usamos global para acessar as variaveis definidas fora da funcao
    global next_id
    # Criamos o produto usando a funcao do modulo models
    # "product" = produto
    product = create_product(next_id, name, price, quantity, category)
    # Adicionamos o produto a lista
    product_list.append(product)
    # Incrementamos o ID para o proximo produto
    next_id = next_id + 1
    # Retornamos o produto criado
    return product

# Funcao que retorna todos os produtos cadastrados
# "get_all_products" = obter todos os produtos
def get_all_products():
    # Retornamos a lista completa de produtos
    return product_list
```

### 3. Interface (Views / Routes)

Os arquivos de **interface** contem o código que **interage com o usuario** — seja pelo terminal, por uma página web ou por uma API. Eles respondem a pergunta: "como o usuario interage com o programa?"

```python
# Arquivo: views/menu.py
# Interface de terminal para o cadastro de produtos
# "menu" = menu (interface do usuario)

# Importamos as funcoes de servico
from services.product_service import add_product, get_all_products
# Importamos a funcao de exibicao
from models.product import display_product

# Funcao que exibe o menu principal
# "show_menu" = mostrar menu
def show_menu():
    # Exibimos as opcoes disponiveis
    print("\n=== Cadastro de Produtos ===")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Sair")

# Funcao principal que executa o programa
# "run" = executar
def run():
    # Loop principal — repete ate o usuario escolher sair
    while True:
        # Mostramos o menu
        show_menu()
        # Pedimos a opcao do usuario
        # "option" = opcao
        option = input("Escolha uma opcao: ")

        # Verificamos qual opcao foi escolhida
        if option == "1":
            # Cadastrar produto
            # "name" = nome
            name = input("Nome: ")
            # "price" = preco
            price = float(input("Preco: "))
            # "quantity" = quantidade
            quantity = int(input("Quantidade: "))
            # "category" = categoria
            category = input("Categoria: ")
            # Adicionamos o produto usando o servico
            # "product" = produto
            product = add_product(name, price, quantity, category)
            print("Produto cadastrado com sucesso!")
        elif option == "2":
            # Listar produtos
            # "products" = produtos
            products = get_all_products()
            # Verificamos se ha produtos cadastrados
            if len(products) == 0:
                print("Nenhum produto cadastrado.")
            else:
                # Exibimos cada produto
                for product in products:
                    print("---")
                    display_product(product)
        elif option == "3":
            # Sair do programa
            print("Ate logo!")
            # break encerra o loop while
            break
        else:
            # Opcao invalida
            print("Opcao invalida. Tente novamente.")
```

### Por Que Separar?

A separacao de responsabilidades traz vários beneficios:

| Beneficio | Explicacao |
|-----------|-----------|
| Facilidade de leitura | Cada arquivo tem um proposito claro — você sabe onde procurar |
| Facilidade de manutenção | Para corrigir um erro na validação, você vai direto ao arquivo de validação |
| Reutilizacao | As funções de validação podem ser usadas em outros projetos |
| Trabalho em equipe | Cada pessoa pode trabalhar em uma parte sem conflitos |
| Testabilidade | E mais fácil testar funções isoladas do que um programa inteiro |

---

## Exemplo Completo: Estrutura de um Projeto CRUD

Vamos ver como ficaria a estrutura do projeto CRUD de cadastro de produtos que você construira nos proximos módulos (módulos 29 a 32):

```
crud_produtos/
    main.py
    README.md
    requirements.txt
    models/
        __init__.py
        product.py
    services/
        __init__.py
        product_service.py
    views/
        __init__.py
        menu.py
    utils/
        __init__.py
        validators.py
    data/
        products.json
```

Cada pasta tem uma responsabilidade clara:

| Pasta | Responsabilidade | Exemplo de Conteúdo |
|-------|-----------------|---------------------|
| `models/` | Estrutura dos dados | Função `create_product()` |
| `services/` | Lógica de negocio | Funções `add_product()`, `get_all_products()` |
| `views/` | Interface com o usuario | Menu do terminal, entrada de dados |
| `utils/` | Funções auxiliares | Validação de nome, preco, quantidade |
| `data/` | Armazenamento de dados | Arquivo JSON com os produtos |

> **Nota:** Nos módulos 29 a 32, você construira esse projeto passo a passo. Por enquanto, o importante e entender a **lógica** por tras da organização.

---

## Boas Práticas de Estruturação

Aqui estão as práticas mais importantes que profissionais seguem ao organizar projetos Python:

**1. Comece simples e cresca conforme necessário**

Não crie uma estrutura complexa para um projeto simples. Comece com poucos arquivos e adicione pastas quando sentir que o projeto esta ficando confuso.

**2. Um arquivo, uma responsabilidade**

Cada arquivo deve fazer uma coisa bem feita. Se um arquivo esta ficando muito grande (mais de 200-300 linhas), considere dividi-lo em arquivos menores.

**3. Nomes descritivos**

O nome do arquivo deve deixar claro o que ele contem. `product_validator.py` e muito melhor que `pv.py` ou `arquivo2.py`.

**4. Mantenha o main.py limpo**

O arquivo principal (`main.py`) deve ser curto e simples — ele apenas importa e chama as funções dos outros módulos. A lógica real fica nos módulos.

```python
# Arquivo: main.py
# Arquivo principal — apenas importa e executa
# "main" = principal

# Importamos a funcao de execucao da interface
from views.menu import run

# Executamos o programa
# Esta e a unica linha de logica no main.py
run()
```

**5. Sempre crie um README.md**

Todo projeto deve ter um arquivo `README.md` que explique: o que o projeto faz, como instalar, como executar e como contribuir.

**6. Use __init__.py em todas as pastas de pacotes**

Mesmo que o arquivo esteja vazio, crie o `__init__.py` em cada pasta que contenha módulos Python. Isso deixa claro que a pasta e um pacote.

**7. Separe dados do código**

Arquivos de dados (JSON, CSV, banco de dados) devem ficar em uma pasta separada (`data/`), não misturados com o código-fonte.

---

## Resumo

Neste módulo, você aprendeu como organizar arquivos e pastas em projetos Python:

| Conceito | O Que E | Exemplo |
|----------|---------|---------|
| snake_case | Padrão de nomenclatura com sublinhados | `meu_arquivo.py` |
| Projeto pequeno | 1-3 arquivos na mesma pasta | `main.py`, `calculator.py` |
| Projeto medio | Pastas por responsabilidade | `models/`, `utils/`, `data/` |
| Projeto grande | Estrutura completa com testes e docs | `src/`, `tests/`, `docs/` |
| `__init__.py` | Transforma pasta em pacote Python | `utils/__init__.py` |
| `__main__.py` | Ponto de entrada para executar pacote | `python3 -m pacote` |
| `setup.py` | Configuração para distribuir o pacote | `pip install .` |
| Separacao de responsabilidades | Cada arquivo com uma função clara | models, services, views |

Pontos importantes para lembrar:

- Use **snake_case** para nomes de arquivos e pastas
- **Sem acentos**, sem espacos, letras minusculas
- Comece **simples** e cresca conforme necessário
- Separe **dados**, **lógica** e **interface** em pastas diferentes
- Sempre crie `__init__.py` em pastas de pacotes
- Mantenha o `main.py` limpo e curto
- Todo projeto deve ter um `README.md`

---

## Para Saber Mais

- [W3Schools — Módulos em Python](https://www.w3schools.com/python/python_modules.asp)
  _Aqui você encontra mais exemplos de como organizar módulos e pacotes em Python_
- [W3Schools — pip e Pacotes](https://www.w3schools.com/python/python_pip.asp)
  _Introducao ao gerenciador de pacotes pip, que você aprendera no próximo modulo_
- [Documentação Oficial Python — Módulos e Pacotes](https://docs.python.org/pt-br/3/tutorial/modules.html)
  _Referencia completa sobre módulos, pacotes e o sistema de imports do Python, em portugues_
- [Documentação Oficial Python — Distribuindo Pacotes](https://docs.python.org/pt-br/3/distributing/index.html)
  _Como distribuir seus projetos Python como pacotes instalaveis_
- [PEP 8 — Guia de Estilo](https://peps.python.org/pep-0008/)
  _O guia oficial de estilo do Python, incluindo convencoes de nomenclatura (em ingles)_

---

## Perguntas Frequentes (FAQ)

**P: Preciso criar toda essa estrutura de pastas para projetos simples?**
R: Não. Para projetos pequenos (1 a 3 arquivos), basta colocar tudo na mesma pasta. A estrutura com subpastas so e necessária quando o projeto cresce e fica difícil encontrar as coisas. Comece simples e organize conforme a necessidade.

**P: O que acontece se eu não criar o __init__.py?**
R: No Python 3.3+, o Python reconhece pastas como "namespace packages" mesmo sem o `__init__.py`. Porém, e uma boa prática sempre cria-lo para deixar claro que a pasta e um pacote. Em versoes mais antigas do Python, sem o `__init__.py` os imports não funcionam.

**P: Posso usar nomes de pastas em portugues?**
R: Tecnicamente sim, mas a convencao profissional e usar nomes em ingles. Isso facilita a colaboracao com desenvolvedores de outros paises e segue o padrão da comunidade Python. Use nomes como `models`, `utils`, `services` em vez de `modelos`, `utilitarios`, `servicos`.

**P: Qual a diferença entre __init__.py e __main__.py?**
R: O `__init__.py` transforma uma pasta em um pacote Python (permite importar módulos dela). O `__main__.py` define o ponto de entrada quando você executa o pacote como programa com `python3 -m nome_do_pacote`. Sao arquivos com propositos completamente diferentes.

**P: Preciso usar setup.py em todos os projetos?**
R: Não. O `setup.py` so e necessário quando você quer distribuir seu projeto como um pacote instalavel (por exemplo, publicar no PyPI). Para projetos pessoais e exercícios do curso, você não precisa dele.

**P: E normal ficar confuso com tantas pastas?**
R: Sim, completamente normal. A organização de projetos e algo que se aprende com a prática. No inicio, pode parecer excessivo criar tantas pastas para pouco código. Com o tempo, você vai perceber que essa organização economiza muito tempo quando o projeto cresce.

**P: O que e o diretório src/?**
R: O `src/` (source = fonte/código-fonte) e uma pasta que agrupa todo o código-fonte do projeto. Nem todos os projetos usam essa pasta — e mais comum em projetos grandes. Para projetos pequenos e medios, você pode colocar as pastas `models/`, `utils/` e `services/` diretamente na raiz.

**P: Posso ter pastas dentro de pastas?**
R: Sim. Você pode ter pacotes dentro de pacotes (pacotes aninhados). Por exemplo: `src/models/product.py`. Cada pasta que contenha módulos Python deve ter seu proprio `__init__.py`.

**P: O que e o arquivo requirements.txt?**
R: O `requirements.txt` e um arquivo que lista todas as bibliotecas externas que seu projeto precisa. Você aprendera sobre ele em detalhes no próximo módulo (módulo 26 — pip e Dependências).

**P: Posso usar acentos em nomes de arquivos?**
R: Embora o Python 3 suporte Unicode, evite acentos em nomes de arquivos e pastas. Acentos podem causar problemas em diferentes sistemas operacionais (Windows, Mac, Linux) e ao compartilhar o projeto com outras pessoas.

**P: Como sei quando meu projeto precisa de mais organização?**
R: Alguns sinais de que e hora de reorganizar: você tem dificuldade para encontrar um arquivo, um arquivo tem mais de 200-300 linhas, você esta copiando e colando código entre arquivos, ou você precisa explicar para alguem onde cada coisa esta. Quando sentir qualquer um desses sinais, e hora de criar pastas e separar responsabilidades.

**P: O que significa "separacao de responsabilidades"?**
R: Significa que cada arquivo e cada pasta devem ter uma única função clara. O arquivo de validação so valida dados. O arquivo de modelos so define a estrutura dos dados. O arquivo de interface so interage com o usuario. Ninguem faz o trabalho do outro.

**P: Posso colocar tudo em um único arquivo grande?**
R: Tecnicamente sim, mas não e recomendado. Um arquivo com centenas de linhas e difícil de ler, de manter e de encontrar erros. Dividir em arquivos menores com responsabilidades claras facilita muito o trabalho.

**P: O que e um "pacote" em Python?**
R: Um pacote (package) e uma pasta que contem módulos Python (arquivos `.py`) e um arquivo `__init__.py`. Pacotes permitem organizar módulos relacionados em uma hierarquia de pastas. Por exemplo, a pasta `utils/` com `__init__.py`, `validators.py` e `formatters.py` e um pacote.

**P: Preciso decorar todas essas convencoes?**
R: Não. Com a prática, essas convencoes se tornam naturais. No inicio, consulte este módulo sempre que precisar. O mais importante e entender o **por que** de cada convencao — isso ajuda a lembrar.

**P: O que e o diretório tests/?**
R: O `tests/` e uma pasta que contem os testes automatizados do projeto — programas que verificam se o código funciona corretamente. Testes automatizados sao um tópico avancado que você aprendera mais adiante na sua jornada como desenvolvedor.

**P: Posso usar espacos em nomes de pastas?**
R: Evite ao máximo. Espacos em nomes de pastas causam problemas no terminal e em muitas ferramentas de desenvolvimento. Use sublinhado (`_`) no lugar de espaco: `meu_projeto` em vez de `meu projeto`.

**P: O que e o diretório docs/?**
R: O `docs/` (documents = documentos) e uma pasta para guardar a documentação do projeto: guias de uso, explicacoes de arquitetura, manuais e outros textos que ajudam a entender o projeto.

**P: E obrigatório ter um README.md?**
R: Não e obrigatório tecnicamente, mas e uma prática tao importante que e considerada essencial. O `README.md` e a primeira coisa que alguem ve ao abrir seu projeto. Ele explica o que o projeto faz, como instalar e como usar. Sempre crie um.

**P: Posso mudar a estrutura do projeto depois?**
R: Sim. A estrutura de um projeto pode e deve evoluir conforme o projeto cresce. Comece simples e reorganize quando necessário. O importante e que a estrutura faca sentido para quem trabalha no projeto.

**P: O que e o arquivo main.py?**
R: O `main.py` (main = principal) e o arquivo que serve como ponto de entrada do programa — e o arquivo que você executa com `python3 main.py`. Ele deve ser curto e simples, apenas importando e chamando funções dos outros módulos.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a navegação.

[Ir para os Exercícios do Módulo 25](25-estruturação-projetos-exercícios.md)

---

[<- Anterior: Módulos e Imports](24-módulos-imports.md) | [Glossário](00-glossário.md) | [Próximo: pip e Dependências ->](26-pip-dependências.md)
