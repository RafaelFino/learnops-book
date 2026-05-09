# Exercícios — Módulo 19: Estruturas de Dados

[<- Voltar ao Módulo 19](19-estruturas-dados.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-19/` e execute com `python3 nome_do_arquivo.py`.

---

## Exercício 1 — Criar e Exibir uma Lista — Nível: Básico
**Conceitos:** listas, criação, for

### Enunciado
Crie uma lista com 5 frutas e exiba cada fruta em uma linha separada, numerando-as de 1 a 5.

### Dicas
- Crie a lista com colchetes `[]`
- Use `for` com `enumerate()` ou um contador manual para numerar
- Lembre-se que `enumerate()` comeca em 0 por padrão, mas aceita `start=1`

### Proposta de Teste
- A saida deve exibir 5 linhas numeradas, por exemplo:
  `1 - maca`, `2 - banana`, `3 - laranja`, `4 - uva`, `5 - manga`
- Verifique que a numeracao comeca em 1 (não em 0)

### Resposta Comentada
```python
# Criamos uma lista com 5 frutas
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva", "manga"]

# Percorremos a lista com enumerate() para ter o indice
# enumerate() retorna pares (indice, valor)
# start=1 faz a contagem comecar em 1
for index, fruit in enumerate(fruits, start=1):
    # "index" = indice (posicao), "fruit" = fruta
    # Exibimos o numero e a fruta
    print(f"{index} - {fruit}")
```

---

## Exercício 2 — Soma dos Elementos — Nível: Básico
**Conceitos:** listas, for, acumulador

### Enunciado
Crie uma lista com 6 números inteiros e calcule a soma de todos os elementos sem usar a função `sum()`.

### Dicas
- Crie uma variável acumuladora iniciando em 0
- Percorra a lista com `for` e some cada item ao acumulador
- Exiba o resultado ao final

### Proposta de Teste
- Lista `[10, 20, 30, 40, 50, 60]` — Saida: `Soma: 210`
- Lista `[1, -1, 2, -2, 3, -3]` — Saida: `Soma: 0`

### Resposta Comentada
```python
# Criamos uma lista de numeros
# "numbers" = numeros
numbers = [10, 20, 30, 40, 50, 60]

# "total" = total — variavel acumuladora que comeca em 0
total = 0

# Percorremos cada numero da lista
for number in numbers:
    # "number" = numero (cada item da vez)
    # Somamos o numero ao total acumulado
    total = total + number

# Exibimos o resultado final
print(f"Soma: {total}")
```

---

## Exercício 3 — Adicionar e Remover da Lista — Nível: Básico
**Conceitos:** listas, append, remove, len

### Enunciado
Crie uma lista de compras vazia. Adicione 4 itens com `append()`. Exiba a lista. Remova 1 item com `remove()`. Exiba a lista novamente e quantos itens restaram.

### Dicas
- Comece com `shopping_list = []`
- Use `append()` para adicionar cada item
- Use `remove()` para remover pelo nome do item
- Use `len()` para contar os itens restantes

### Proposta de Teste
- Adicione "arroz", "feijao", "leite", "pao" — Lista: `['arroz', 'feijao', 'leite', 'pao']`
- Remova "leite" — Lista: `['arroz', 'feijao', 'pao']`, Quantidade: `3`

### Resposta Comentada
```python
# Criamos uma lista de compras vazia
# "shopping_list" = lista de compras
shopping_list = []

# Adicionamos 4 itens com append() (append = acrescentar)
shopping_list.append("arroz")
shopping_list.append("feijao")
shopping_list.append("leite")
shopping_list.append("pao")

# Exibimos a lista completa
print(f"Lista de compras: {shopping_list}")

# Removemos um item com remove() (remove = remover)
shopping_list.remove("leite")

# Exibimos a lista atualizada e a quantidade de itens
# len() = length = comprimento/tamanho
print(f"Apos remover leite: {shopping_list}")
print(f"Itens restantes: {len(shopping_list)}")
```

---

## Exercício 4 — Maior e Menor da Lista — Nível: Básico
**Conceitos:** listas, for, comparação

### Enunciado
Crie uma lista com 7 números. Encontre o maior e o menor valor sem usar as funções `max()` e `min()`.

### Dicas
- Comece assumindo que o primeiro item e o maior e o menor
- Percorra a lista comparando cada item com o maior e o menor atuais
- Atualize quando encontrar um valor maior ou menor

### Proposta de Teste
- Lista `[15, 3, 42, 8, 23, 1, 37]` — Saida: `Maior: 42` e `Menor: 1`
- Lista `[5, 5, 5, 5, 5, 5, 5]` — Saida: `Maior: 5` e `Menor: 5`

### Resposta Comentada
```python
# Criamos uma lista de numeros
# "numbers" = numeros
numbers = [15, 3, 42, 8, 23, 1, 37]

# Assumimos que o primeiro item e o maior e o menor
# "biggest" = maior, "smallest" = menor
biggest = numbers[0]
smallest = numbers[0]

# Percorremos a lista a partir do segundo item
for number in numbers:
    # "number" = numero (cada item da vez)
    # Se o numero atual for maior que o maior registrado, atualizamos
    if number > biggest:
        biggest = number
    # Se o numero atual for menor que o menor registrado, atualizamos
    if number < smallest:
        smallest = number

# Exibimos os resultados
print(f"Maior: {biggest}")
print(f"Menor: {smallest}")
```

---

## Exercício 5 — Fatiamento de Lista — Nível: Básico
**Conceitos:** listas, fatiamento (slicing)

### Enunciado
Crie uma lista com os números de 1 a 10. Usando fatiamento, exiba: os 3 primeiros, os 3 ultimos, os itens do índice 2 ao 6, e a lista invertida.

### Dicas
- Use `lista[:3]` para os primeiros, `lista[-3:]` para os ultimos
- Use `lista[2:7]` para um trecho do meio (lembre: o fim não e incluido)
- Use `lista[::-1]` para inverter

### Proposta de Teste
- Primeiros 3: `[1, 2, 3]`
- Ultimos 3: `[8, 9, 10]`
- Índice 2 ao 6: `[3, 4, 5, 6, 7]`
- Invertida: `[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]`

### Resposta Comentada
```python
# Criamos uma lista com numeros de 1 a 10
# "numbers" = numeros
# list(range(1, 11)) gera [1, 2, 3, ..., 10]
numbers = list(range(1, 11))

# Fatiamento (slicing = fatiar)
# [:3] pega do inicio ate o indice 3 (nao incluido)
print(f"Primeiros 3: {numbers[:3]}")

# [-3:] pega os 3 ultimos (indice negativo conta de tras)
print(f"Ultimos 3: {numbers[-3:]}")

# [2:7] pega do indice 2 ao 6 (o 7 nao e incluido)
print(f"Indice 2 ao 6: {numbers[2:7]}")

# [::-1] inverte a lista (passo -1 percorre de tras para frente)
print(f"Invertida: {numbers[::-1]}")
```

---

## Exercício 6 — Ordenar Lista de Nomes — Nível: Intermediario
**Conceitos:** listas, sort, input, while

### Enunciado
Peca ao usuario que digite nomes (um por vez) ate digitar "sair". Armazene os nomes em uma lista e exiba a lista em ordem alfabetica.

### Dicas
- Use um loop `while True` com `break` quando o usuario digitar "sair"
- Use `append()` para adicionar cada nome
- Use `sort()` para ordenar em ordem alfabetica

### Proposta de Teste
- Nomes: "Carlos", "Ana", "Bruno", "sair" — Saida: `['Ana', 'Bruno', 'Carlos']`
- Apenas "sair" — Saida: `Nenhum nome digitado.`

### Resposta Comentada
```python
# Criamos uma lista vazia para armazenar os nomes
# "names" = nomes
names = []

# Loop que pede nomes ate o usuario digitar "sair"
while True:
    # "name" = nome
    # strip() remove espacos extras no inicio e fim
    name = input("Digite um nome (ou 'sair' para encerrar): ").strip()

    # Se o usuario digitou "sair", saimos do loop
    if name.lower() == "sair":
        break

    # Se o nome nao estiver vazio, adicionamos a lista
    if name != "":
        names.append(name)

# Verificamos se algum nome foi digitado
if len(names) == 0:
    print("Nenhum nome digitado.")
else:
    # sort() ordena a lista em ordem alfabetica
    names.sort()
    # Exibimos a lista ordenada
    print(f"Nomes em ordem alfabetica: {names}")
```

---

## Exercício 7 — Tupla de Coordenadas — Nível: Básico
**Conceitos:** tuplas, criação, unpacking

### Enunciado
Crie uma tupla com as coordenadas de um ponto (x, y). Desempacote os valores em variáveis separadas e exiba cada coordenada. Depois, calcule a distancia do ponto ate a origem (0, 0) usando a formula: distancia = raiz quadrada de (x ao quadrado + y ao quadrado).

### Dicas
- Crie a tupla: `point = (3, 4)`
- Desempacote: `x, y = point`
- Para raiz quadrada, use `** 0.5` (elevar a 0.5 e o mesmo que raiz quadrada)

### Proposta de Teste
- Ponto `(3, 4)` — Distancia: `5.0`
- Ponto `(0, 0)` — Distancia: `0.0`

### Resposta Comentada
```python
# Criamos uma tupla com coordenadas
# "point" = ponto
point = (3, 4)

# Unpacking (desempacotar) — extraimos x e y da tupla
# "x" e "y" sao as coordenadas
x, y = point

# Exibimos cada coordenada
print(f"Coordenada x: {x}")
print(f"Coordenada y: {y}")

# Calculamos a distancia ate a origem (0, 0)
# "distance" = distancia
# ** 2 eleva ao quadrado, ** 0.5 calcula a raiz quadrada
distance = (x ** 2 + y ** 2) ** 0.5

# Exibimos a distancia
print(f"Distancia ate a origem: {distance}")
```

---

## Exercício 8 — Função com Retorno Multiplo — Nível: Intermediario
**Conceitos:** tuplas, funções, retorno multiplo

### Enunciado
Crie uma função `analyze_grades` que receba uma lista de notas e retorne uma tupla com: a menor nota, a maior nota e a media. Desempacote o retorno em variáveis separadas.

### Dicas
- Use `min()` e `max()` para menor e maior
- Para a media, some todos os valores e divida pela quantidade
- Retorne os tres valores separados por virgula (o Python empacota em tupla)

### Proposta de Teste
- Notas `[7, 8, 5, 9, 6]` — Menor: `5`, Maior: `9`, Media: `7.0`
- Notas `[10, 10, 10]` — Menor: `10`, Maior: `10`, Media: `10.0`

### Resposta Comentada
```python
# "analyze_grades" = analisar notas
# "grades" = notas (lista de numeros)
def analyze_grades(grades):
    # "lowest" = menor nota
    lowest = min(grades)
    # "highest" = maior nota
    highest = max(grades)
    # "average" = media — soma dividida pela quantidade
    average = sum(grades) / len(grades)
    # Retornamos tres valores — o Python empacota em uma tupla
    return lowest, highest, average

# Criamos uma lista de notas
# "grades" = notas
grades = [7, 8, 5, 9, 6]

# Desempacotamos o retorno da funcao em tres variaveis
# "lowest" = menor, "highest" = maior, "average" = media
lowest, highest, average = analyze_grades(grades)

# Exibimos os resultados
print(f"Menor nota: {lowest}")
print(f"Maior nota: {highest}")
print(f"Media: {average}")
```

---

## Exercício 9 — Cadastro com Dicionário — Nível: Básico
**Conceitos:** dicionários, criação, acesso por chave

### Enunciado
Crie um dicionário representando um produto com os campos: nome, preco, quantidade e categoria. Exiba cada campo formatado.

### Dicas
- Use chaves em ingles: "name", "price", "quantity", "category"
- Acesse cada valor com `dicionario["chave"]`
- Formate o preco com `R$`

### Proposta de Teste
- Produto: Arroz, R$ 5.99, 50 unidades, Alimentos — Exibir todos os campos
- Verifique que o tipo do dicionário e `<class 'dict'>`

### Resposta Comentada
```python
# Criamos um dicionario representando um produto
# "product" = produto
product = {
    "name": "Arroz",           # "name" = nome
    "price": 5.99,             # "price" = preco
    "quantity": 50,            # "quantity" = quantidade
    "category": "Alimentos"   # "category" = categoria
}

# Exibimos cada campo acessando pela chave
print(f"Produto: {product['name']}")
print(f"Preco: R$ {product['price']}")
print(f"Quantidade: {product['quantity']} unidades")
print(f"Categoria: {product['category']}")
```

---

## Exercício 10 — Agenda Telefonica — Nível: Intermediario
**Conceitos:** dicionários, adicionar, buscar, get

### Enunciado
Crie uma agenda telefonica usando dicionário. O programa deve ter um menu com opcoes: 1-Adicionar contato, 2-Buscar contato, 3-Listar todos, 0-Sair.

### Dicas
- Use o nome como chave e o telefone como valor
- Use `get()` para buscar sem gerar erro se o nome não existir
- Use um loop `while` para o menu

### Proposta de Teste
- Adicionar "Ana" com telefone "1234" e buscar "Ana" — Saida: `Telefone de Ana: 1234`
- Buscar "Carlos" (não cadastrado) — Saida: `Contato nao encontrado.`

### Resposta Comentada
```python
# "phone_book" = agenda telefonica (dicionario vazio)
phone_book = {}

# Loop do menu
while True:
    # Exibimos as opcoes
    print("\n=== Agenda Telefonica ===")
    print("1 - Adicionar contato")
    print("2 - Buscar contato")
    print("3 - Listar todos")
    print("0 - Sair")

    # "option" = opcao escolhida pelo usuario
    option = input("Opcao: ").strip()

    if option == "1":
        # Adicionar contato
        # "name" = nome, "phone" = telefone
        name = input("Nome: ").strip()
        phone = input("Telefone: ").strip()
        # Adicionamos ao dicionario (nome como chave, telefone como valor)
        phone_book[name] = phone
        print(f"Contato {name} adicionado!")

    elif option == "2":
        # Buscar contato
        name = input("Nome para buscar: ").strip()
        # get() retorna None se a chave nao existir
        phone = phone_book.get(name)
        if phone is not None:
            print(f"Telefone de {name}: {phone}")
        else:
            print("Contato nao encontrado.")

    elif option == "3":
        # Listar todos os contatos
        if len(phone_book) == 0:
            print("Agenda vazia.")
        else:
            # Percorremos os pares chave-valor
            for name, phone in phone_book.items():
                print(f"{name}: {phone}")

    elif option == "0":
        # Sair do programa
        print("Ate logo!")
        break
    else:
        # Opcao invalida
        print("Opcao invalida!")
```

---

## Exercício 11 — Contagem de Palavras — Nível: Intermediario
**Conceitos:** dicionários, strings, split, for

### Enunciado
Peca uma frase ao usuario e conte quantas vezes cada palavra aparece, armazenando o resultado em um dicionário.

### Dicas
- Use `split()` para separar a frase em palavras
- Use `lower()` para ignorar maiusculas/minusculas
- Para cada palavra, verifique se ja esta no dicionário e incremente o contador

### Proposta de Teste
- Frase: "o gato viu o rato e o gato correu" — Saida: `{'o': 3, 'gato': 2, 'viu': 1, 'rato': 1, 'e': 1, 'correu': 1}`
- Frase: "sim sim sim" — Saida: `{'sim': 3}`

### Resposta Comentada
```python
# Pedimos uma frase ao usuario
# "sentence" = frase
sentence = input("Digite uma frase: ")

# Convertemos para minusculas e separamos em palavras
# lower() = converter para minusculas
# split() = dividir em uma lista de palavras
# "words" = palavras
words = sentence.lower().split()

# Criamos um dicionario para contar as palavras
# "word_count" = contagem de palavras
word_count = {}

# Percorremos cada palavra
for word in words:
    # "word" = palavra (cada item da vez)
    # Se a palavra ja esta no dicionario, incrementamos
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        # Se nao esta, adicionamos com contagem 1
        word_count[word] = 1

# Exibimos o resultado
print(f"Contagem: {word_count}")
```

---

## Exercício 12 — Elementos Unicos com Conjunto — Nível: Básico
**Conceitos:** conjuntos, set, unicidade

### Enunciado
Crie uma lista com números repetidos. Use um conjunto para encontrar quais números sao unicos (aparecem na lista, sem repetição). Exiba quantos números unicos existem.

### Dicas
- Converta a lista para conjunto com `set()`
- O conjunto automaticamente remove duplicatas
- Use `len()` para contar

### Proposta de Teste
- Lista `[1, 2, 3, 2, 4, 1, 5, 3, 6, 2]` — Unicos: 6 números
- Lista `[7, 7, 7, 7]` — Unicos: 1 número

### Resposta Comentada
```python
# Criamos uma lista com numeros repetidos
# "numbers" = numeros
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 2]

# Convertemos para conjunto — remove duplicatas automaticamente
# "unique_numbers" = numeros unicos
unique_numbers = set(numbers)

# Exibimos os resultados
print(f"Lista original: {numbers}")
print(f"Numeros unicos: {unique_numbers}")
print(f"Quantidade de unicos: {len(unique_numbers)}")
```

---

## Exercício 13 — Alunos em Comum — Nível: Intermediario
**Conceitos:** conjuntos, intersecao, uniao, diferença

### Enunciado
Crie dois conjuntos representando alunos de duas turmas. Encontre: alunos em ambas as turmas (intersecao), todos os alunos (uniao) e alunos exclusivos de cada turma (diferença).

### Dicas
- Use `intersection()` para alunos em comum
- Use `union()` para todos os alunos
- Use `difference()` para alunos exclusivos

### Proposta de Teste
- Turma A: {"Ana", "Bruno", "Carlos", "Diana"}, Turma B: {"Bruno", "Diana", "Eva", "Felipe"}
  - Em comum: {"Bruno", "Diana"}
  - Todos: {"Ana", "Bruno", "Carlos", "Diana", "Eva", "Felipe"}
  - So turma A: {"Ana", "Carlos"}
- Turmas identicas: {"Ana", "Bruno"} e {"Ana", "Bruno"} — Em comum: {"Ana", "Bruno"}, Exclusivos: conjunto vazio

### Resposta Comentada
```python
# Criamos dois conjuntos de alunos
# "class_a" = turma A, "class_b" = turma B
class_a = {"Ana", "Bruno", "Carlos", "Diana"}
class_b = {"Bruno", "Diana", "Eva", "Felipe"}

# Intersecao — alunos que estao em AMBAS as turmas
# "common" = em comum
common = class_a.intersection(class_b)
print(f"Em ambas as turmas: {common}")

# Uniao — TODOS os alunos (sem repetir)
# "all_students" = todos os alunos
all_students = class_a.union(class_b)
print(f"Todos os alunos: {all_students}")

# Diferenca — alunos EXCLUSIVOS de cada turma
# "only_a" = somente na turma A
only_a = class_a.difference(class_b)
print(f"So na turma A: {only_a}")

# "only_b" = somente na turma B
only_b = class_b.difference(class_a)
print(f"So na turma B: {only_b}")
```

---

## Exercício 14 — Lista de Dicionários — Nível: Intermediario
**Conceitos:** listas, dicionários, for, funções

### Enunciado
Crie uma lista de 3 produtos (cada produto e um dicionário com nome, preco e quantidade). Crie uma função que receba a lista e retorne o valor total do estoque (preco vezes quantidade de cada produto, somados).

### Dicas
- Cada produto e um dicionário: `{"name": "Arroz", "price": 5.99, "quantity": 10}`
- Percorra a lista e para cada produto multiplique preco por quantidade
- Acumule o total

### Proposta de Teste
- Produtos: Arroz (5.99, 10), Feijao (7.49, 8), Macarrao (3.29, 15)
  - Total: 5.99*10 + 7.49*8 + 3.29*15 = 59.90 + 59.92 + 49.35 = `169.17`
- Lista vazia `[]` — Total: `0`

### Resposta Comentada
```python
# "calculate_stock_value" = calcular valor do estoque
# "products" = produtos (lista de dicionarios)
def calculate_stock_value(products):
    # "total" = total acumulado
    total = 0
    # Percorremos cada produto da lista
    for product in products:
        # "product" = produto (cada dicionario da vez)
        # Multiplicamos preco (price) pela quantidade (quantity)
        # "item_value" = valor do item
        item_value = product["price"] * product["quantity"]
        # Somamos ao total
        total = total + item_value
    # Retornamos o valor total do estoque
    return total

# Criamos a lista de produtos
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99, "quantity": 10},
    {"name": "Feijao", "price": 7.49, "quantity": 8},
    {"name": "Macarrao", "price": 3.29, "quantity": 15}
]

# Calculamos e exibimos o valor total
# "stock_value" = valor do estoque
stock_value = calculate_stock_value(products)
print(f"Valor total do estoque: R$ {stock_value:.2f}")
```

---

## Exercício 15 — Dicionário Aninhado de Alunos — Nível: Avancado
**Conceitos:** dicionários aninhados, for, funções

### Enunciado
Crie um dicionário onde cada chave e o nome de um aluno e o valor e outro dicionário com as notas de 3 materias. Crie uma função que calcule a media de cada aluno e exiba quem foi aprovado (media >= 7).

### Dicas
- Estrutura: `{"Ana": {"math": 8, "portuguese": 7, "science": 9}}`
- Percorra com `.items()` para ter nome e notas
- Calcule a media somando as notas e dividindo por 3

### Proposta de Teste
- Ana (8, 7, 9) media 8.0 — Aprovada
- Bruno (5, 6, 4) media 5.0 — Reprovado
- Carlos (7, 7, 7) media 7.0 — Aprovado

### Resposta Comentada
```python
# "show_results" = exibir resultados
# "students" = alunos (dicionario aninhado)
def show_results(students):
    # Percorremos cada aluno e suas notas
    for name, grades in students.items():
        # "name" = nome, "grades" = notas (dicionario interno)
        # Calculamos a media somando os valores das notas
        # values() retorna os valores do dicionario de notas
        # "average" = media
        average = sum(grades.values()) / len(grades)
        # Verificamos se foi aprovado (media >= 7)
        # "status" = situacao
        if average >= 7:
            status = "Aprovado(a)"
        else:
            status = "Reprovado(a)"
        # Exibimos o resultado
        print(f"{name}: media {average:.1f} - {status}")

# Criamos o dicionario de alunos com notas
# "students" = alunos
# "math" = matematica, "portuguese" = portugues, "science" = ciencias
students = {
    "Ana": {"math": 8, "portuguese": 7, "science": 9},
    "Bruno": {"math": 5, "portuguese": 6, "science": 4},
    "Carlos": {"math": 7, "portuguese": 7, "science": 7}
}

# Chamamos a funcao para exibir os resultados
show_results(students)
```

---

## Exercício 16 — Carrinho de Compras Completo — Nível: Avancado
**Conceitos:** listas, dicionários, funções, while, menu

### Enunciado
Crie um programa de carrinho de compras com menu: 1-Adicionar produto (nome e preco), 2-Remover produto (pelo nome), 3-Exibir carrinho com total, 0-Sair. Cada produto e um dicionário na lista.

### Dicas
- O carrinho e uma lista de dicionários: `[{"name": "Arroz", "price": 5.99}]`
- Para remover, percorra a lista e encontre o produto pelo nome
- Para o total, some todos os precos

### Proposta de Teste
- Adicionar "Arroz" (5.99) e "Feijao" (7.49) — Total: `R$ 13.48`
- Remover "Arroz" — Total: `R$ 7.49`
- Carrinho vazio — Saida: `Carrinho vazio.`

### Resposta Comentada
```python
# "cart" = carrinho (lista de dicionarios)
cart = []

# Loop do menu
while True:
    print("\n=== Carrinho de Compras ===")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Exibir carrinho")
    print("0 - Sair")

    # "option" = opcao
    option = input("Opcao: ").strip()

    if option == "1":
        # Adicionar produto
        # "name" = nome do produto
        name = input("Nome do produto: ").strip()
        try:
            # "price" = preco do produto
            price = float(input("Preco: R$ "))
            # Criamos o dicionario do produto e adicionamos ao carrinho
            cart.append({"name": name, "price": price})
            print(f"{name} adicionado ao carrinho!")
        except ValueError:
            print("Preco invalido!")

    elif option == "2":
        # Remover produto pelo nome
        name = input("Nome do produto para remover: ").strip()
        # "found" = encontrado (controle para saber se achamos o produto)
        found = False
        for product in cart:
            if product["name"].lower() == name.lower():
                cart.remove(product)
                print(f"{name} removido do carrinho!")
                found = True
                break
        if not found:
            print("Produto nao encontrado.")

    elif option == "3":
        # Exibir carrinho
        if len(cart) == 0:
            print("Carrinho vazio.")
        else:
            # "total" = total acumulado
            total = 0
            print("\n--- Seu Carrinho ---")
            for product in cart:
                print(f"  {product['name']}: R$ {product['price']:.2f}")
                total = total + product["price"]
            print(f"  Total: R$ {total:.2f}")

    elif option == "0":
        print("Ate logo!")
        break
    else:
        print("Opcao invalida!")
```

---

## Exercício 17 — Frequência de Letras com Dicionário e Conjunto — Nível: Avancado
**Conceitos:** dicionários, conjuntos, strings, for

### Enunciado
Peca uma frase ao usuario. Conte a frequência de cada letra (ignorando espacos e maiusculas). Depois, use um conjunto para exibir quais letras distintas aparecem na frase.

### Dicas
- Converta para minusculas com `lower()`
- Ignore espacos verificando `if char != " "`
- Use um dicionário para contar e `set()` ou as chaves do dicionário para letras unicas

### Proposta de Teste
- Frase: "Ana ama" — Frequência: `{'a': 4, 'n': 1, 'm': 1}`, Letras unicas: `{'a', 'n', 'm'}`
- Frase: "aaa" — Frequência: `{'a': 3}`, Letras unicas: `{'a'}`

### Resposta Comentada
```python
# Pedimos uma frase ao usuario
# "sentence" = frase
sentence = input("Digite uma frase: ")

# Criamos um dicionario para contar a frequencia de cada letra
# "letter_count" = contagem de letras
letter_count = {}

# Percorremos cada caractere da frase
for char in sentence.lower():
    # "char" = caractere (cada letra da vez)
    # Ignoramos espacos
    if char != " ":
        # Se a letra ja esta no dicionario, incrementamos
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            # Se nao esta, adicionamos com contagem 1
            letter_count[char] = 1

# Exibimos a frequencia de cada letra
print(f"Frequencia: {letter_count}")

# Usamos as chaves do dicionario como conjunto de letras unicas
# set() converte as chaves em um conjunto
# "unique_letters" = letras unicas
unique_letters = set(letter_count.keys())
print(f"Letras unicas: {unique_letters}")
```

---

## Exercício 18 — Sistema de Cadastro Completo — Nível: Avancado
**Conceitos:** listas, dicionários, tuplas, conjuntos, funções, menu

### Enunciado
Crie um sistema de cadastro de alunos com menu: 1-Cadastrar aluno (nome, idade, cidade), 2-Listar alunos, 3-Buscar por nome, 4-Cidades unicas (usar conjunto), 5-Estatisticas (usar tupla para retorno), 0-Sair. Cada aluno e um dicionário em uma lista.

### Dicas
- Aluno: `{"name": "Ana", "age": 20, "city": "Recife"}`
- Para cidades unicas, extraia as cidades em um conjunto
- Para estatisticas, crie uma função que retorne uma tupla (total, media de idade, cidade mais frequente)

### Proposta de Teste
- Cadastrar Ana (20, Recife), Bruno (25, Recife), Carlos (22, Salvador)
  - Cidades unicas: {"Recife", "Salvador"}
  - Estatisticas: total 3, media 22.33, cidade mais frequente: Recife
- Nenhum aluno cadastrado — Estatisticas: mensagem de lista vazia

### Resposta Comentada
```python
# "calculate_stats" = calcular estatisticas
# "students" = alunos (lista de dicionarios)
def calculate_stats(students):
    # Se a lista estiver vazia, retornamos None
    if len(students) == 0:
        return None
    # "total" = total de alunos
    total = len(students)
    # Calculamos a media de idade
    # "age_sum" = soma das idades
    age_sum = 0
    # "city_count" = contagem de cidades (dicionario)
    city_count = {}
    for student in students:
        age_sum = age_sum + student["age"]
        # Contamos a frequencia de cada cidade
        city = student["city"]
        if city in city_count:
            city_count[city] = city_count[city] + 1
        else:
            city_count[city] = 1
    # "average_age" = media de idade
    average_age = age_sum / total
    # Encontramos a cidade mais frequente
    # "most_common_city" = cidade mais comum
    most_common_city = ""
    # "max_count" = contagem maxima
    max_count = 0
    for city, count in city_count.items():
        if count > max_count:
            max_count = count
            most_common_city = city
    # Retornamos uma tupla com as estatisticas
    return total, average_age, most_common_city

# "students" = alunos (lista de dicionarios)
students = []

# Loop do menu principal
while True:
    print("\n=== Cadastro de Alunos ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Buscar por nome")
    print("4 - Cidades unicas")
    print("5 - Estatisticas")
    print("0 - Sair")

    # "option" = opcao
    option = input("Opcao: ").strip()

    if option == "1":
        # Cadastrar aluno
        # "name" = nome, "city" = cidade
        name = input("Nome: ").strip()
        try:
            # "age" = idade
            age = int(input("Idade: "))
        except ValueError:
            print("Idade invalida!")
            continue
        city = input("Cidade: ").strip()
        # Criamos o dicionario do aluno e adicionamos a lista
        students.append({"name": name, "age": age, "city": city})
        print(f"Aluno {name} cadastrado!")

    elif option == "2":
        # Listar todos os alunos
        if len(students) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for student in students:
                print(f"  {student['name']}, {student['age']} anos, {student['city']}")

    elif option == "3":
        # Buscar por nome
        # "search_name" = nome para buscar
        search_name = input("Nome para buscar: ").strip()
        # "found" = encontrado
        found = False
        for student in students:
            if student["name"].lower() == search_name.lower():
                print(f"  {student['name']}, {student['age']} anos, {student['city']}")
                found = True
        if not found:
            print("Aluno nao encontrado.")

    elif option == "4":
        # Cidades unicas usando conjunto
        if len(students) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            # Extraimos as cidades em um conjunto (remove duplicatas)
            # "unique_cities" = cidades unicas
            unique_cities = set()
            for student in students:
                unique_cities.add(student["city"])
            print(f"Cidades: {unique_cities}")

    elif option == "5":
        # Estatisticas usando tupla de retorno
        # "result" = resultado da funcao
        result = calculate_stats(students)
        if result is None:
            print("Nenhum aluno cadastrado.")
        else:
            # Desempacotamos a tupla retornada
            total, average_age, most_common_city = result
            print(f"Total de alunos: {total}")
            print(f"Media de idade: {average_age:.2f}")
            print(f"Cidade mais frequente: {most_common_city}")

    elif option == "0":
        print("Ate logo!")
        break
    else:
        print("Opcao invalida!")
```

---

[<- Voltar ao Módulo 19](19-estruturas-dados.md) | [Glossário](00-glossario.md)
