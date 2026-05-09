# 19 — Estruturas de Dados: Listas, Tuplas, Dicionários e Conjuntos

[<- Anterior: Tratamento de Erros](18-tratamento-erros.md) | [Glossário](00-glossário.md) | [Próximo: Leitura e Escrita de Arquivos ->](20-leitura-escrita-arquivos.md)

---

## Introdução

Ate agora, você trabalhou com variáveis que guardam um único valor — um número, um texto, um verdadeiro ou falso. Mas e quando você precisa guardar **vários valores** ao mesmo tempo?

Imagine que você esta fazendo compras no mercado. Você não anota cada item em um papel separado — você faz uma **lista de compras** com todos os itens juntos. Em Python, temos estruturas que funcionam exatamente assim: elas guardam vários valores organizados em um único lugar.

Neste módulo, você vai aprender as quatro principais estruturas de dados do Python:

- **Listas** — como uma lista de compras: você pode adicionar, remover e reorganizar itens
- **Tuplas** — como uma data de nascimento: uma vez definida, não muda
- **Dicionários** — como uma agenda telefonica: cada nome (chave) tem um telefone (valor) associado
- **Conjuntos (sets)** — como um album de figurinhas sem repetidas: cada elemento aparece apenas uma vez

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-19/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-19`
4. Execute: `python3 nome_do_arquivo.py`

---

## Quando Usar Cada Estrutura

Antes de entrar nos detalhes, veja um resumo com analogias do dia a dia:

| Estrutura | Analogia | Quando usar |
|-----------|----------|-------------|
| Lista | Lista de compras | Coleção ordenada que pode mudar (adicionar, remover, reordenar) |
| Tupla | Data de nascimento | Dados que não devem mudar depois de criados |
| Dicionário | Agenda telefonica | Quando você precisa buscar um valor por uma chave (nome → telefone) |
| Conjunto | Album de figurinhas sem repetidas | Quando você precisa de elementos unicos, sem repetição |

---

## Listas

### O Que e Uma Lista

Uma lista e uma coleção **ordenada** e **mutavel** de elementos. "Ordenada" significa que os itens tem posição (primeiro, segundo, terceiro...). "Mutavel" significa que você pode adicionar, remover e alterar itens depois de criar a lista.

Pense em uma **lista de compras**: você escreve os itens em ordem, pode riscar um item, adicionar outro no final, ou trocar um item por outro.

### Criando Listas

```python
# Criando uma lista vazia
# "shopping_list" = lista de compras
shopping_list = []

# Criando uma lista com itens
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva", "manga"]

# Listas podem ter diferentes tipos de dados
# "mixed" = misturado
mixed = ["Ana", 25, 1.70, True]

# Verificando o tipo
print(type(fruits))
```

Saida esperada:
```
<class 'list'>
```

### Indexacao — Acessando Itens pela Posição

Cada item da lista tem uma posição chamada **índice** (index). O primeiro item tem índice **0** (zero), não 1. Isso e uma convencao da programação.

Pense em um predio: o terreo e o andar 0, o primeiro andar e o 1, e assim por diante.

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva", "manga"]

# Acessando pelo indice (index = posicao)
# Indice:   0        1         2        3       4
print(fruits[0])   # Primeiro item
print(fruits[1])   # Segundo item
print(fruits[4])   # Ultimo item
print(fruits[-1])  # Ultimo item (indice negativo conta de tras para frente)
print(fruits[-2])  # Penultimo item
```

Saida esperada:
```
maca
banana
manga
manga
uva
```

### Fatiamento (Slicing) — Pegando Pedacos da Lista

Fatiamento e como cortar um pedaco de um bolo: você escolhe onde começar e onde parar.

A sintaxe e `lista[inicio:fim]` — o inicio e incluido, mas o fim **não** e incluido.

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva", "manga"]

# Fatiamento (slicing = fatiar)
# Do indice 1 ate o 3 (o 3 nao entra)
print(fruits[1:3])

# Do inicio ate o indice 3 (o 3 nao entra)
print(fruits[:3])

# Do indice 2 ate o final
print(fruits[2:])

# Copia completa da lista
print(fruits[:])
```

Saida esperada:
```
['banana', 'laranja']
['maca', 'banana', 'laranja']
['laranja', 'uva', 'manga']
['maca', 'banana', 'laranja', 'uva', 'manga']
```

### Alterando Itens da Lista

Como listas sao mutaveis, você pode trocar qualquer item:

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja"]

# Trocando o item na posicao 1
# Antes: banana. Depois: abacaxi
fruits[1] = "abacaxi"

print(fruits)
```

Saida esperada:
```
['maca', 'abacaxi', 'laranja']
```

### Métodos de Lista

Métodos sao funções que "pertencem" a lista. Você chama um método usando o ponto: `lista.metodo()`.

#### append() — Adicionar no Final

```python
# "shopping_list" = lista de compras
shopping_list = ["arroz", "feijao"]

# append() = acrescentar/adicionar ao final
shopping_list.append("macarrao")
shopping_list.append("leite")

print(shopping_list)
```

Saida esperada:
```
['arroz', 'feijao', 'macarrao', 'leite']
```

#### insert() — Adicionar em Posição Específica

```python
# "fruits" = frutas
fruits = ["maca", "laranja", "uva"]

# insert(posicao, item) = inserir na posicao especificada
# Inserindo "banana" na posicao 1
fruits.insert(1, "banana")

print(fruits)
```

Saida esperada:
```
['maca', 'banana', 'laranja', 'uva']
```

#### extend() — Juntar Duas Listas

```python
# "fruits" = frutas, "more_fruits" = mais frutas
fruits = ["maca", "banana"]
more_fruits = ["uva", "manga"]

# extend() = estender/juntar outra lista ao final
fruits.extend(more_fruits)

print(fruits)
```

Saida esperada:
```
['maca', 'banana', 'uva', 'manga']
```

#### remove() — Remover pelo Valor

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "banana"]

# remove() = remover a PRIMEIRA ocorrencia do valor
fruits.remove("banana")

print(fruits)
```

Saida esperada:
```
['maca', 'laranja', 'banana']
```

> **Nota:** O remove() so remove a **primeira** ocorrência. A segunda "banana" permaneceu.

#### pop() — Remover pela Posição

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva"]

# pop() sem argumento remove o ULTIMO item e retorna ele
# "last" = ultimo
last = fruits.pop()
print(f"Removido: {last}")
print(f"Lista: {fruits}")

# pop(indice) remove o item na posicao especificada
# "first" = primeiro
first = fruits.pop(0)
print(f"Removido: {first}")
print(f"Lista: {fruits}")
```

Saida esperada:
```
Removido: uva
Lista: ['maca', 'banana', 'laranja']
Removido: maca
Lista: ['banana', 'laranja']
```

#### sort() — Ordenar a Lista

```python
# "numbers" = numeros
numbers = [5, 2, 8, 1, 9, 3]

# sort() = ordenar em ordem crescente (modifica a lista original)
numbers.sort()
print(f"Crescente: {numbers}")

# sort(reverse=True) = ordenar em ordem decrescente
# "reverse" = reverso/inverso
numbers.sort(reverse=True)
print(f"Decrescente: {numbers}")
```

Saida esperada:
```
Crescente: [1, 2, 3, 5, 8, 9]
Decrescente: [9, 8, 5, 3, 2, 1]
```

#### reverse() — Inverter a Ordem

```python
# "letters" = letras
letters = ["a", "b", "c", "d"]

# reverse() = inverter a ordem dos itens
letters.reverse()

print(letters)
```

Saida esperada:
```
['d', 'c', 'b', 'a']
```

#### index() — Encontrar a Posição de um Item

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva"]

# index() = encontrar o indice (posicao) de um item
# "position" = posicao
position = fruits.index("laranja")
print(f"Laranja esta na posicao: {position}")
```

Saida esperada:
```
Laranja esta na posicao: 2
```

#### count() — Contar Ocorrências

```python
# "grades" = notas
grades = [7, 8, 7, 9, 7, 10, 8]

# count() = contar quantas vezes um valor aparece
# "count_seven" = contagem de setes
count_seven = grades.count(7)
print(f"A nota 7 aparece {count_seven} vezes")
```

Saida esperada:
```
A nota 7 aparece 3 vezes
```

#### len() — Tamanho da Lista

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva", "manga"]

# len() = length = comprimento/tamanho
# Retorna quantos itens a lista tem
# "size" = tamanho
size = len(fruits)
print(f"A lista tem {size} frutas")
```

Saida esperada:
```
A lista tem 5 frutas
```

> **Nota:** `len()` não e um método da lista — e uma função do Python que funciona com várias estruturas de dados.

### Percorrendo Listas com for

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja"]

# Percorrendo cada item da lista
for fruit in fruits:
    # "fruit" = fruta (cada item da vez)
    print(f"Eu gosto de {fruit}")
```

Saida esperada:
```
Eu gosto de maca
Eu gosto de banana
Eu gosto de laranja
```

### Verificando se um Item Existe na Lista

```python
# "fruits" = frutas
fruits = ["maca", "banana", "laranja"]

# "in" verifica se o item esta na lista
if "banana" in fruits:
    print("Banana esta na lista!")

if "abacaxi" not in fruits:
    print("Abacaxi NAO esta na lista!")
```

Saida esperada:
```
Banana esta na lista!
Abacaxi NAO esta na lista!
```

---

## Tuplas

### O Que e Uma Tupla

Uma tupla e uma coleção **ordenada** e **imutavel** de elementos. "Imutavel" significa que, depois de criada, você **não pode** adicionar, remover ou alterar itens.

Pense em uma **data de nascimento**: uma vez que você nasceu em 15/03/1990, essa data nunca vai mudar. Ela tem tres partes (dia, mes, ano) em uma ordem fixa. Isso e uma tupla.

### Criando Tuplas

```python
# Criando uma tupla com parenteses
# "birth_date" = data de nascimento
# (dia, mes, ano)
birth_date = (15, 3, 1990)

# Tupla com um unico item — precisa da virgula!
# "single" = unico
single = (42,)

# Sem a virgula, Python entende como um numero entre parenteses, nao como tupla
not_a_tuple = (42)

print(type(birth_date))
print(type(single))
print(type(not_a_tuple))
```

Saida esperada:
```
<class 'tuple'>
<class 'tuple'>
<class 'int'>
```

> **Atenção:** Para criar uma tupla com um único item, você **precisa** colocar uma virgula depois do item: `(42,)`. Sem a virgula, o Python entende como um número comum entre parenteses.

### Acessando Itens da Tupla

O acesso funciona igual ao de listas — por índice:

```python
# "birth_date" = data de nascimento
birth_date = (15, 3, 1990)

# Acessando pelo indice
# "day" = dia, "month" = mes, "year" = ano
day = birth_date[0]
month = birth_date[1]
year = birth_date[2]

print(f"Nascimento: {day}/{month}/{year}")
```

Saida esperada:
```
Nascimento: 15/3/1990
```

### Imutabilidade — Não Pode Alterar

```python
# "colors" = cores
colors = ("vermelho", "verde", "azul")

# Tentar alterar gera um erro!
# colors[0] = "amarelo"  # TypeError: 'tuple' object does not support item assignment

# Voce pode ler, mas nao pode modificar
print(colors[0])
```

Saida esperada:
```
vermelho
```

> **Por que usar tuplas se não posso alterar?** Justamente por isso! Quando você quer garantir que os dados não sejam modificados acidentalmente, use uma tupla. Além disso, tuplas sao mais rapidas que listas e podem ser usadas como chaves de dicionário (listas não podem).

### Packing e Unpacking — Empacotar e Desempacotar

**Packing** (empacotar) e quando você coloca vários valores em uma tupla. **Unpacking** (desempacotar) e quando você extrai os valores da tupla para variáveis separadas.

```python
# Packing (empacotar) — varios valores viram uma tupla
# "coordinates" = coordenadas
coordinates = (10, 20)

# Unpacking (desempacotar) — a tupla vira variaveis separadas
# "x" e "y" recebem os valores da tupla
x, y = coordinates

print(f"x = {x}")
print(f"y = {y}")
```

Saida esperada:
```
x = 10
y = 20
```

```python
# Unpacking com mais valores
# "person" = pessoa
person = ("Ana", 25, "Sao Paulo")

# "name" = nome, "age" = idade, "city" = cidade
name, age, city = person

print(f"{name} tem {age} anos e mora em {city}")
```

Saida esperada:
```
Ana tem 25 anos e mora em Sao Paulo
```

> **Importante:** O número de variáveis no unpacking deve ser igual ao número de itens na tupla. Se forem diferentes, o Python gera um erro.

### Tuplas como Retorno Multiplo de Funções

Funções podem retornar vários valores de uma vez usando tuplas:

```python
# "calculate_rectangle" = calcular retangulo
# "width" = largura, "height" = altura
def calculate_rectangle(width, height):
    # "area" = area, "perimeter" = perimetro
    area = width * height
    perimeter = 2 * (width + height)
    # Retornamos dois valores — o Python empacota em uma tupla
    return area, perimeter

# Desempacotamos os dois valores retornados
# "area" = area, "perimeter" = perimetro
area, perimeter = calculate_rectangle(5, 3)

print(f"Area: {area}")
print(f"Perimetro: {perimeter}")
```

Saida esperada:
```
Area: 15
Perimetro: 16
```

### Tuplas como Chaves de Dicionário

Listas não podem ser chaves de dicionário porque sao mutaveis. Tuplas podem, porque sao imutaveis:

```python
# Usando tuplas como chaves de dicionario
# Cada chave e uma coordenada (linha, coluna)
# "board" = tabuleiro
board = {}
board[(0, 0)] = "X"
board[(0, 1)] = "O"
board[(1, 1)] = "X"

print(board)
print(f"Posicao (0, 0): {board[(0, 0)]}")
```

Saida esperada:
```
{(0, 0): 'X', (0, 1): 'O', (1, 1): 'X'}
Posicao (0, 0): X
```

---

## Dicionários

### O Que e Um Dicionário

Um dicionário e uma coleção de pares **chave: valor**. Cada chave e única e aponta para um valor. E como uma **agenda telefonica**: você procura pelo nome (chave) e encontra o telefone (valor).

Dicionários sao **mutaveis** (você pode adicionar, remover e alterar itens) e, a partir do Python 3.7, mantem a **ordem de inserção**.

### Criando Dicionários

```python
# Criando um dicionario vazio
# "contacts" = contatos
contacts = {}

# Criando um dicionario com dados
# "student" = estudante
# "name" = nome, "age" = idade, "city" = cidade
student = {
    "name": "Carlos",
    "age": 20,
    "city": "Belo Horizonte"
}

print(student)
print(type(student))
```

Saida esperada:
```
{'name': 'Carlos', 'age': 20, 'city': 'Belo Horizonte'}
<class 'dict'>
```

### Acessando Valores por Chave

```python
# "student" = estudante
student = {
    "name": "Carlos",
    "age": 20,
    "city": "Belo Horizonte"
}

# Acessando pelo nome da chave (key = chave)
print(student["name"])
print(student["age"])
```

Saida esperada:
```
Carlos
20
```

> **Cuidado:** Se você tentar acessar uma chave que não existe com `[]`, o Python gera um erro `KeyError`. Para evitar isso, use o método `get()`.

### O Método get() — Acesso Seguro

```python
# "student" = estudante
student = {
    "name": "Carlos",
    "age": 20
}

# get() retorna o valor se a chave existir
print(student.get("name"))

# Se a chave nao existir, retorna None (nenhum valor)
print(student.get("phone"))

# Voce pode definir um valor padrao para quando a chave nao existir
# "default" = padrao
print(student.get("phone", "Nao informado"))
```

Saida esperada:
```
Carlos
None
Nao informado
```

### Adicionando e Alterando Itens

```python
# "student" = estudante
student = {
    "name": "Carlos",
    "age": 20
}

# Adicionando uma nova chave
# "email" = email
student["email"] = "carlos@email.com"

# Alterando um valor existente
student["age"] = 21

print(student)
```

Saida esperada:
```
{'name': 'Carlos', 'age': 21, 'email': 'carlos@email.com'}
```

### Métodos de Dicionário

#### keys() — Todas as Chaves

```python
# "product" = produto
product = {"name": "Arroz", "price": 5.99, "quantity": 10}

# keys() = chaves — retorna todas as chaves do dicionario
# "all_keys" = todas as chaves
all_keys = product.keys()
print(all_keys)
```

Saida esperada:
```
dict_keys(['name', 'price', 'quantity'])
```

#### values() — Todos os Valores

```python
# "product" = produto
product = {"name": "Arroz", "price": 5.99, "quantity": 10}

# values() = valores — retorna todos os valores do dicionario
# "all_values" = todos os valores
all_values = product.values()
print(all_values)
```

Saida esperada:
```
dict_values(['Arroz', 5.99, 10])
```

#### items() — Pares Chave-Valor

```python
# "product" = produto
product = {"name": "Arroz", "price": 5.99, "quantity": 10}

# items() = itens — retorna pares (chave, valor) como tuplas
# "all_items" = todos os itens
all_items = product.items()
print(all_items)
```

Saida esperada:
```
dict_items([('name', 'Arroz'), ('price', 5.99), ('quantity', 10)])
```

#### update() — Atualizar com Outro Dicionário

```python
# "product" = produto
product = {"name": "Arroz", "price": 5.99}

# "new_data" = novos dados
new_data = {"price": 6.49, "category": "Alimentos"}

# update() = atualizar — adiciona/atualiza com os dados do outro dicionario
product.update(new_data)

print(product)
```

Saida esperada:
```
{'name': 'Arroz', 'price': 6.49, 'category': 'Alimentos'}
```

> **Nota:** O preco (price) foi atualizado de 5.99 para 6.49, e a categoria (category) foi adicionada.

#### pop() — Remover por Chave

```python
# "product" = produto
product = {"name": "Arroz", "price": 5.99, "quantity": 10}

# pop(chave) = remover o item com a chave especificada e retornar o valor
# "removed_price" = preco removido
removed_price = product.pop("price")

print(f"Preco removido: {removed_price}")
print(f"Dicionario: {product}")
```

Saida esperada:
```
Preco removido: 5.99
Dicionario: {'name': 'Arroz', 'quantity': 10}
```

### Percorrendo Dicionários com for

```python
# "student" = estudante
student = {"name": "Ana", "age": 22, "city": "Recife"}

# Percorrendo as chaves
print("--- Chaves ---")
for key in student:
    # "key" = chave
    print(key)

# Percorrendo os valores
print("--- Valores ---")
for value in student.values():
    # "value" = valor
    print(value)

# Percorrendo chaves E valores juntos
print("--- Chaves e Valores ---")
for key, value in student.items():
    print(f"{key}: {value}")
```

Saida esperada:
```
--- Chaves ---
name
age
city
--- Valores ---
Ana
22
Recife
--- Chaves e Valores ---
name: Ana
age: 22
city: Recife
```

### Verificando se uma Chave Existe

```python
# "student" = estudante
student = {"name": "Ana", "age": 22}

# "in" verifica se a CHAVE existe no dicionario
if "name" in student:
    print("A chave 'name' existe!")

if "phone" not in student:
    print("A chave 'phone' NAO existe!")
```

Saida esperada:
```
A chave 'name' existe!
A chave 'phone' NAO existe!
```

### Dicionários Aninhados

Dicionários podem conter outros dicionários como valores. Isso e útil para representar dados mais complexos.

Pense em uma **ficha de cadastro** que tem uma secao de endereco dentro dela:

```python
# "student" = estudante
# "address" = endereco, "street" = rua, "number" = numero
student = {
    "name": "Maria",
    "age": 19,
    "address": {
        "street": "Rua das Flores",
        "number": 123,
        "city": "Curitiba"
    }
}

# Acessando dados do dicionario interno
print(student["name"])
print(student["address"]["street"])
print(student["address"]["city"])
```

Saida esperada:
```
Maria
Rua das Flores
Curitiba
```

```python
# Lista de dicionarios — muito comum em programas reais
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99},
    {"name": "Feijao", "price": 7.49},
    {"name": "Macarrao", "price": 3.29}
]

# Percorrendo a lista de dicionarios
for product in products:
    # "product" = produto (cada dicionario da vez)
    print(f"{product['name']}: R$ {product['price']}")
```

Saida esperada:
```
Arroz: R$ 5.99
Feijao: R$ 7.49
Macarrao: R$ 3.29
```

---

## Conjuntos (Sets)

### O Que e Um Conjunto

Um conjunto (set) e uma coleção **não ordenada** de elementos **unicos**. "Não ordenada" significa que os itens não tem posição fixa. "Unicos" significa que não pode haver itens repetidos.

Pense em um **album de figurinhas sem repetidas**: se você ja tem a figurinha número 5, não adianta tentar colocar outra número 5 — o album so aceita uma de cada.

### Criando Conjuntos

```python
# Criando um conjunto com chaves {}
# "fruits" = frutas
fruits = {"maca", "banana", "laranja"}

# Criando um conjunto a partir de uma lista (remove duplicatas!)
# "numbers" = numeros
numbers = {1, 2, 3, 2, 1, 4, 3, 5}

print(fruits)
print(numbers)
print(type(fruits))
```

Saida esperada:
```
{'maca', 'banana', 'laranja'}
{1, 2, 3, 4, 5}
<class 'set'>
```

> **Nota:** Os números repetidos foram removidos automaticamente! O conjunto so mantem uma copia de cada valor.

> **Atenção:** Para criar um conjunto **vazio**, use `set()`, não `{}`. As chaves vazias `{}` criam um dicionário vazio, não um conjunto.

```python
# Conjunto vazio — use set(), nao {}
# "empty_set" = conjunto vazio
empty_set = set()

# Isso cria um DICIONARIO vazio, nao um conjunto!
# "empty_dict" = dicionario vazio
empty_dict = {}

print(type(empty_set))
print(type(empty_dict))
```

Saida esperada:
```
<class 'set'>
<class 'dict'>
```

### Adicionando e Removendo Elementos

```python
# "fruits" = frutas
fruits = {"maca", "banana"}

# add() = adicionar um elemento ao conjunto
fruits.add("laranja")
fruits.add("uva")
print(f"Apos adicionar: {fruits}")

# Adicionar um item que ja existe nao faz nada (sem erro)
fruits.add("maca")
print(f"Apos adicionar 'maca' de novo: {fruits}")

# discard() = descartar/remover um elemento (sem erro se nao existir)
fruits.discard("banana")
print(f"Apos remover 'banana': {fruits}")

# discard() de item que nao existe — nao gera erro
fruits.discard("abacaxi")

# remove() = remover um elemento (gera erro se nao existir!)
# fruits.remove("abacaxi")  # KeyError!
```

Saida esperada:
```
Apos adicionar: {'maca', 'banana', 'laranja', 'uva'}
Apos adicionar 'maca' de novo: {'maca', 'banana', 'laranja', 'uva'}
Apos remover 'banana': {'maca', 'laranja', 'uva'}
```

> **Dica:** Prefira `discard()` em vez de `remove()` quando não tiver certeza se o item existe. O `discard()` não gera erro se o item não for encontrado.

> **Nota:** A ordem dos itens exibidos pode variar porque conjuntos não tem ordem fixa.

### Verificando Pertencimento

```python
# "fruits" = frutas
fruits = {"maca", "banana", "laranja"}

# "in" verifica se o item pertence ao conjunto
if "banana" in fruits:
    print("Banana esta no conjunto!")

if "abacaxi" not in fruits:
    print("Abacaxi NAO esta no conjunto!")
```

Saida esperada:
```
Banana esta no conjunto!
Abacaxi NAO esta no conjunto!
```

### Operações de Conjuntos

Conjuntos suportam operações matematicas que sao muito úteis. Pense em dois grupos de amigos e as operações que você pode fazer com eles:

#### Uniao — Todos os Elementos de Ambos

```python
# "group_a" = grupo A, "group_b" = grupo B
group_a = {"Ana", "Bruno", "Carlos"}
group_b = {"Bruno", "Diana", "Carlos", "Eva"}

# union() = uniao — todos os elementos de ambos (sem repetir)
# "all_people" = todas as pessoas
all_people = group_a.union(group_b)
print(f"Uniao: {all_people}")
```

Saida esperada:
```
Uniao: {'Ana', 'Bruno', 'Carlos', 'Diana', 'Eva'}
```

#### Intersecao — Elementos em Comum

```python
# "group_a" = grupo A, "group_b" = grupo B
group_a = {"Ana", "Bruno", "Carlos"}
group_b = {"Bruno", "Diana", "Carlos", "Eva"}

# intersection() = intersecao — elementos que estao em AMBOS
# "common" = em comum
common = group_a.intersection(group_b)
print(f"Em comum: {common}")
```

Saida esperada:
```
Em comum: {'Bruno', 'Carlos'}
```

#### Diferença — Elementos Exclusivos

```python
# "group_a" = grupo A, "group_b" = grupo B
group_a = {"Ana", "Bruno", "Carlos"}
group_b = {"Bruno", "Diana", "Carlos", "Eva"}

# difference() = diferenca — elementos que estao em A mas NAO em B
# "only_a" = somente no grupo A
only_a = group_a.difference(group_b)
print(f"So no grupo A: {only_a}")

# Diferenca no sentido contrario
# "only_b" = somente no grupo B
only_b = group_b.difference(group_a)
print(f"So no grupo B: {only_b}")
```

Saida esperada:
```
So no grupo A: {'Ana'}
So no grupo B: {'Diana', 'Eva'}
```

### Removendo Duplicatas de uma Lista com set()

Um uso muito prático de conjuntos e remover itens duplicados de uma lista:

```python
# Lista com itens repetidos
# "names_with_duplicates" = nomes com duplicatas
names_with_duplicates = ["Ana", "Bruno", "Ana", "Carlos", "Bruno", "Ana"]

# Convertemos para conjunto (remove duplicatas) e depois de volta para lista
# "unique_names" = nomes unicos
unique_names = list(set(names_with_duplicates))

print(f"Com duplicatas: {names_with_duplicates}")
print(f"Sem duplicatas: {unique_names}")
```

Saida esperada:
```
Com duplicatas: ['Ana', 'Bruno', 'Ana', 'Carlos', 'Bruno', 'Ana']
Sem duplicatas: ['Ana', 'Bruno', 'Carlos']
```

> **Nota:** A ordem pode mudar ao converter para conjunto e de volta para lista, porque conjuntos não mantem ordem.

---

## Comparação entre as Estruturas

| Caracteristica | Lista | Tupla | Dicionário | Conjunto |
|----------------|-------|-------|------------|----------|
| Sintaxe | `[1, 2, 3]` | `(1, 2, 3)` | `{"a": 1}` | `{1, 2, 3}` |
| Ordenada | Sim | Sim | Sim (3.7+) | Não |
| Mutavel | Sim | Não | Sim | Sim |
| Permite duplicatas | Sim | Sim | Chaves unicas | Não |
| Acesso por índice | Sim | Sim | Por chave | Não |
| Analogia | Lista de compras | Data de nascimento | Agenda telefonica | Figurinhas sem repetidas |

### Quando Usar Cada Uma

- **Lista**: quando você precisa de uma coleção ordenada que pode mudar. Exemplo: lista de tarefas, notas de alunos.
- **Tupla**: quando os dados não devem mudar. Exemplo: coordenadas (x, y), retorno de funções com multiplos valores.
- **Dicionário**: quando você precisa associar chaves a valores. Exemplo: cadastro de produtos, dados de um usuario.
- **Conjunto**: quando você precisa de elementos unicos ou fazer operações de conjuntos. Exemplo: verificar quais alunos estão em duas turmas.

---

## Para Saber Mais

- [W3Schools — Python Lists](https://www.w3schools.com/python/python_lists.asp) — _Listas em Python com exemplos interativos_
- [W3Schools — Python Tuples](https://www.w3schools.com/python/python_tuples.asp) — _Tuplas em Python_
- [W3Schools — Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) — _Dicionarios em Python_
- [W3Schools — Python Sets](https://www.w3schools.com/python/python_sets.asp) — _Conjuntos em Python_
- [Documentação Python — Estruturas de Dados](https://docs.python.org/pt-br/3/tutorial/datastructures.html) — _Referencia oficial em portugues_

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre lista e tupla?**
R: A principal diferença e que listas sao mutaveis (você pode alterar, adicionar e remover itens) e tuplas sao imutaveis (uma vez criadas, não podem ser modificadas). Use listas quando os dados podem mudar e tuplas quando os dados devem permanecer fixos.

**P: Quando devo usar um dicionário em vez de uma lista?**
R: Use um dicionário quando você precisa buscar valores por um nome (chave), como buscar o telefone de alguem pelo nome. Use uma lista quando a ordem dos itens importa e você acessa por posição (índice).

**P: O que acontece se eu tentar acessar um índice que não existe na lista?**
R: O Python gera um erro `IndexError`. Por exemplo, se a lista tem 3 itens (indices 0, 1, 2) e você tentar acessar o índice 5, vai dar erro. Sempre verifique o tamanho da lista com `len()` antes de acessar.

**P: Posso misturar tipos diferentes em uma lista?**
R: Sim! Uma lista pode conter inteiros, strings, floats, booleanos e ate outras listas ou dicionários. Exemplo: `["Ana", 25, True, 1.70]`. Porém, na prática, e mais comum ter listas com itens do mesmo tipo.

**P: O que e "mutavel" e "imutavel"?**
R: Mutavel significa que pode ser alterado depois de criado — você pode adicionar, remover ou trocar itens. Imutavel significa que não pode ser alterado — uma vez criado, permanece igual. Listas e dicionários sao mutaveis. Tuplas e strings sao imutaveis.

**P: Por que o índice comeca em 0 e não em 1?**
R: E uma convencao da programação que vem da forma como o computador organiza a memória. O índice 0 significa "zero posicoes de distancia do inicio". Com o tempo, você se acostuma e isso se torna natural.

**P: Posso ter uma lista dentro de outra lista?**
R: Sim! Isso se chama lista aninhada. Exemplo: `matrix = [[1, 2, 3], [4, 5, 6]]`. Para acessar um item, use dois indices: `matrix[0][1]` retorna `2` (primeira lista, segundo item).

**P: Qual a diferença entre remove() e pop() em listas?**
R: `remove()` busca pelo **valor** e remove a primeira ocorrência. `pop()` remove pelo **índice** (posição) e retorna o item removido. Se você sabe o valor, use `remove()`. Se sabe a posição, use `pop()`.

**P: O que acontece se eu usar append() com uma lista como argumento?**
R: O `append()` adiciona o item como um único elemento. Se você fizer `lista.append([4, 5])`, a lista interna sera adicionada como um único item. Para juntar duas listas, use `extend()`.

**P: Posso ordenar uma lista de strings?**
R: Sim! O `sort()` ordena strings em ordem alfabetica. Exemplo: `["banana", "abacaxi", "uva"].sort()` resulta em `["abacaxi", "banana", "uva"]`. Letras maiusculas vem antes de minusculas na ordenação padrão.

**P: O que e um dicionário aninhado?**
R: E um dicionário que contem outro dicionário como valor. Exemplo: um cadastro de aluno com endereco, onde o endereco e outro dicionário com rua, número e cidade. Você acessa com chaves encadeadas: `aluno["address"]["city"]`.

**P: Posso usar números como chaves de dicionário?**
R: Sim! Chaves podem ser qualquer tipo imutavel: strings, números inteiros, floats ou tuplas. Não podem ser listas ou outros dicionários (porque sao mutaveis).

**P: O que acontece se eu adicionar um item repetido a um conjunto?**
R: Nada! O conjunto simplesmente ignora o item duplicado, sem gerar erro. Essa e justamente a utilidade dos conjuntos — garantir que cada elemento apareca apenas uma vez.

**P: Posso acessar itens de um conjunto pelo índice?**
R: Não! Conjuntos não tem ordem fixa, então não suportam acesso por índice. Se você precisa de acesso por posição, use uma lista. Conjuntos sao úteis para verificar pertencimento (`in`) e operações de conjuntos (uniao, intersecao).

**P: Qual a diferença entre discard() e remove() em conjuntos?**
R: Ambos removem um elemento, mas `remove()` gera erro `KeyError` se o item não existir, enquanto `discard()` não gera erro. Prefira `discard()` quando não tiver certeza se o item esta no conjunto.

**P: Posso converter entre as estruturas?**
R: Sim! Use `list()`, `tuple()`, `set()` e `dict()` para converter. Exemplo: `list({1, 2, 3})` converte um conjunto em lista. Para dicionários, a conversão e mais específica — você precisa de pares chave-valor.

**P: O que e "fatiamento" (slicing)?**
R: E uma forma de pegar um pedaco de uma lista ou tupla usando a sintaxe `[inicio:fim]`. O inicio e incluido e o fim não. Exemplo: `[1, 2, 3, 4, 5][1:3]` retorna `[2, 3]`.

**P: Posso usar for para percorrer qualquer estrutura de dados?**
R: Sim! O `for` funciona com listas, tuplas, dicionários, conjuntos e strings. Em dicionários, o `for` percorre as chaves por padrão. Use `.values()` para percorrer valores e `.items()` para percorrer pares chave-valor.

**P: O que e "unpacking" de tupla?**
R: E extrair os valores de uma tupla para variáveis separadas. Exemplo: `x, y = (10, 20)` coloca 10 em `x` e 20 em `y`. O número de variáveis deve ser igual ao número de itens na tupla.

**P: E normal achar estruturas de dados confusas no inicio?**
R: Completamente normal! Estruturas de dados sao um dos tópicos mais importantes da programação e levam tempo para dominar. A dica e praticar bastante com os exercícios e voltar a este módulo sempre que precisar. Com o tempo, você vai saber instintivamente qual estrutura usar em cada situacao.

**P: Preciso decorar todos os métodos de lista e dicionário?**
R: Não! Programadores profissionais consultam a documentação o tempo todo. O importante e saber que os métodos existem e onde encontra-los. Com a prática, os mais usados (como `append`, `get`, `keys`) ficam naturais.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado:

**[Acessar Exercícios do Módulo 19](19-estruturas-dados-exercícios.md)**

---

[<- Anterior: Tratamento de Erros](18-tratamento-erros.md) | [Glossário](00-glossário.md) | [Próximo: Leitura e Escrita de Arquivos ->](20-leitura-escrita-arquivos.md)
