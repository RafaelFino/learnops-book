# 23 — Exercícios Integradores

[<- Anterior: Classes e Objetos](22-classes-objetos.md) | [Glossário](00-glossário.md) | [Próximo: Módulos e Imports ->](24-módulos-imports.md)

---

## Introdução

Parabéns! Você chegou a um marco muito importante na sua jornada de aprendizado. Ate aqui, você aprendeu variáveis, tipos, condicionais, loops, funções, estruturas de dados (listas, tuplas, dicionários, conjuntos), classes, arquivos, JSON e tratamento de erros. Cada um desses conceitos e como um ingrediente de cozinha — sozinho ja e útil, mas quando combinados, criam pratos completos e deliciosos.

Este módulo e dedicado exclusivamente a prática. Não ha teoria nova aqui. O objetivo e integrar todos os conceitos que você aprendeu em exercícios que simulam situacoes reais de programação. Pense neste módulo como uma prova de fogo amigavel: você vai combinar tudo o que sabe para resolver problemas cada vez mais complexos.

Os exercícios estão organizados em tres níveis de dificuldade:

| Nível | Descricao | Exercícios |
|-------|-----------|------------|
| Básico | Variáveis, condicionais, loops e funções simples | 1-6 |
| Intermediario | Funções, listas, dicionários, tuplas, conjuntos e tratamento de erros | 7-18 |
| Avancado | Classes, arquivos, JSON e combinacao de multiplos conceitos | 19-28 |

Não se preocupe se não conseguir resolver todos de primeira. Volte aos módulos anteriores, releia as explicacoes, e tente novamente. A prática constante e o caminho mais seguro para se tornar um bom programador.

> **Dica:** Consulte o [Glossário](00-glossário.md) e os módulos anteriores sempre que precisar relembrar um conceito.

---

## Como Executar os Exemplos

1. Abra o terminal (no Linux, pressione `Ctrl + Alt + T`)
2. Navegue ate a pasta do módulo:
   ```bash
   cd ~/meus-projetos/python-curso/módulo-23/
   ```
3. Salve cada exercício em um arquivo separado (por exemplo, `exercicio01.py`)
4. Execute com:
   ```bash
   python3 exercicio01.py
   ```

---

## Exercício 1 — Calculadora de Desconto — Nível: Básico

**Conceitos:** variáveis, input, condicionais, funções, operadores matematicos

### Enunciado

Crie um programa que pergunte o preco original de um produto e a porcentagem de desconto. O programa deve calcular e exibir o valor do desconto e o preco final. Se o desconto for maior que 50%, exiba um aviso de "Super Promocao!".

### Dicas

- Use `input()` para receber os valores e converta para `float()`
- Calcule o desconto: `preco * porcentagem / 100`
- Calcule o preco final: `preco - desconto`
- Use `if` para verificar se a porcentagem e maior que 50

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Preco `200.0`, desconto `10` → saida: `Desconto: R$ 20.00` e `Preco final: R$ 180.00`
- **Caso de borda:** Preco `100.0`, desconto `60` → saida deve incluir `Super Promocao!`, `Desconto: R$ 60.00` e `Preco final: R$ 40.00`

### Resposta Comentada

```python
# Pedimos o preco original ao usuario
# "original_price" = preco original
# input() retorna string, float() converte para numero decimal
original_price = float(input("Digite o preco original do produto: "))

# Pedimos a porcentagem de desconto
# "discount_percent" = porcentagem de desconto
discount_percent = float(input("Digite a porcentagem de desconto: "))

# Calculamos o valor do desconto
# "discount_value" = valor do desconto
# Multiplicamos o preco pela porcentagem e dividimos por 100
discount_value = original_price * discount_percent / 100

# Calculamos o preco final subtraindo o desconto do preco original
# "final_price" = preco final
final_price = original_price - discount_value

# Verificamos se o desconto e maior que 50%
if discount_percent > 50:
    # Exibimos aviso de super promocao
    print("Super Promocao!")

# Exibimos o valor do desconto formatado com 2 casas decimais
# :.2f formata o numero com 2 casas decimais
print(f"Desconto: R$ {discount_value:.2f}")

# Exibimos o preco final formatado com 2 casas decimais
print(f"Preco final: R$ {final_price:.2f}")
```

---

## Exercício 2 — Classificador de Triangulos — Nível: Básico

**Conceitos:** variáveis, input, condicionais, funções, comparação

### Enunciado

Crie um programa que receba os tres lados de um triangulo e classifique-o como: equilatero (3 lados iguais), isosceles (2 lados iguais) ou escaleno (3 lados diferentes). Antes de classificar, verifique se os valores formam um triangulo válido (a soma de dois lados deve ser maior que o terceiro).

### Dicas

- Receba os tres lados com `input()` e converta para `float()`
- Para verificar se e triangulo válido: `a + b > c` e `a + c > b` e `b + c > a`
- Equilatero: `a == b == c`
- Isosceles: dois lados iguais (use `or` para verificar as combinacoes)
- Escaleno: nenhum lado igual

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Lados `5`, `5`, `5` → saida: `Triangulo equilatero`
- **Caso de borda:** Lados `1`, `2`, `3` → saida: `Nao forma um triangulo valido` (pois 1 + 2 não e maior que 3)

### Resposta Comentada

```python
# Pedimos os tres lados do triangulo ao usuario
# "side_a", "side_b", "side_c" = lado a, lado b, lado c
side_a = float(input("Digite o primeiro lado: "))
side_b = float(input("Digite o segundo lado: "))
side_c = float(input("Digite o terceiro lado: "))

# Verificamos se os lados formam um triangulo valido
# A soma de dois lados deve ser maior que o terceiro lado
# "is_valid" = e valido
is_valid = side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a

# Se nao for valido, informamos e encerramos
if not is_valid:
    # Exibimos mensagem de triangulo invalido
    print("Nao forma um triangulo valido")
else:
    # Verificamos se e equilatero (3 lados iguais)
    if side_a == side_b == side_c:
        # Todos os lados sao iguais
        print("Triangulo equilatero")
    # Verificamos se e isosceles (2 lados iguais)
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        # Dois lados sao iguais
        print("Triangulo isosceles")
    else:
        # Nenhum lado e igual — escaleno
        print("Triangulo escaleno")
```

---

## Exercício 3 — Tabuada Personalizada — Nível: Básico

**Conceitos:** variáveis, input, loops (for), range, funções

### Enunciado

Crie uma função chamada `show_multiplication_table` (mostrar tabuada) que receba um número e um limite. A função deve exibir a tabuada desse número de 1 ate o limite informado. O programa deve pedir o número e o limite ao usuario.

### Dicas

- Use `def` para criar a função com dois parametros
- Use `for` com `range(1, limite + 1)` para percorrer os multiplicadores
- Dentro do loop, calcule e exiba cada linha da tabuada
- Lembre-se: `range(1, 4)` gera 1, 2, 3 (o limite não e incluido)

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Número `3`, limite `5` → saida:
  ```
  3 x 1 = 3
  3 x 2 = 6
  3 x 3 = 9
  3 x 4 = 12
  3 x 5 = 15
  ```
- **Caso de borda:** Número `7`, limite `1` → saida: `7 x 1 = 7` (apenas uma linha)

### Resposta Comentada

```python
# Funcao que exibe a tabuada de um numero ate um limite
# "show_multiplication_table" = mostrar tabuada
# "number" = numero, "limit" = limite
def show_multiplication_table(number, limit):
    # Percorremos de 1 ate o limite (incluindo o limite)
    # "multiplier" = multiplicador
    for multiplier in range(1, limit + 1):
        # Calculamos o resultado da multiplicacao
        # "result" = resultado
        result = number * multiplier
        # Exibimos a linha da tabuada formatada
        print(f"{number} x {multiplier} = {result}")

# Pedimos o numero ao usuario
# "number" = numero
number = int(input("Digite o numero para a tabuada: "))

# Pedimos o limite ao usuario
# "limit" = limite
limit = int(input("Digite ate qual numero multiplicar: "))

# Chamamos a funcao passando o numero e o limite
show_multiplication_table(number, limit)
```

---

## Exercício 4 — Verificador de Palindromo — Nível: Básico

**Conceitos:** variáveis, strings, fatiamento, funções, condicionais

### Enunciado

Crie uma função chamada `is_palindrome` (e palindromo) que receba uma palavra e retorne `True` se ela for um palindromo (lida igual de tras para frente) ou `False` caso contrario. O programa deve ignorar maiusculas e minusculas. Peca uma palavra ao usuario e informe se e palindromo.

### Dicas

- Use `.lower()` para converter a palavra para minusculas
- Use fatiamento `[::-1]` para inverter a string
- Compare a palavra original (em minusculas) com a invertida
- Retorne `True` ou `False`

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Palavra `"arara"` → saida: `arara e um palindromo!`
- **Caso de borda:** Palavra `"Ana"` → saida: `Ana e um palindromo!` (deve ignorar maiusculas)

### Resposta Comentada

```python
# Funcao que verifica se uma palavra e palindromo
# "is_palindrome" = e palindromo
# "word" = palavra
def is_palindrome(word):
    # Convertemos para minusculas para ignorar maiusculas/minusculas
    # "cleaned" = limpa (palavra tratada)
    cleaned = word.lower()
    # Invertemos a palavra usando fatiamento [::-1]
    # "reversed_word" = palavra invertida
    reversed_word = cleaned[::-1]
    # Comparamos a palavra original com a invertida
    # Se forem iguais, e palindromo
    return cleaned == reversed_word

# Pedimos uma palavra ao usuario
# "user_word" = palavra do usuario
user_word = input("Digite uma palavra: ")

# Verificamos se e palindromo usando a funcao
if is_palindrome(user_word):
    # A palavra e palindromo
    print(f"{user_word} e um palindromo!")
else:
    # A palavra nao e palindromo
    print(f"{user_word} nao e um palindromo.")
```

---

## Exercício 5 — Gerador de Senha Simples — Nível: Básico

**Conceitos:** variáveis, strings, loops, funções, condicionais

### Enunciado

Crie uma função chamada `generate_password` (gerar senha) que receba o nome do usuario e o ano de nascimento. A função deve gerar uma senha combinando: as 3 primeiras letras do nome (em maiusculas) + o ano invertido + o tamanho do nome. Exiba a senha gerada.

### Dicas

- Use fatiamento `[:3]` para pegar as 3 primeiras letras
- Use `.upper()` para converter para maiusculas
- Converta o ano para string e use `[::-1]` para inverter
- Use `len()` para obter o tamanho do nome
- Concatene tudo com `+` ou use f-string

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Nome `"Carlos"`, ano `1990` → saida: `Sua senha: CAR09916`
- **Caso de borda:** Nome `"Lu"`, ano `2005` → saida: `Sua senha: LU50022` (nome com menos de 3 letras usa o que tem)

### Resposta Comentada

```python
# Funcao que gera uma senha simples a partir do nome e ano de nascimento
# "generate_password" = gerar senha
# "name" = nome, "birth_year" = ano de nascimento
def generate_password(name, birth_year):
    # Pegamos as 3 primeiras letras do nome e convertemos para maiusculas
    # "prefix" = prefixo (inicio da senha)
    prefix = name[:3].upper()
    # Convertemos o ano para string e invertemos
    # "reversed_year" = ano invertido
    reversed_year = str(birth_year)[::-1]
    # Calculamos o tamanho do nome
    # "name_length" = tamanho do nome
    name_length = len(name)
    # Montamos a senha concatenando as partes
    # "password" = senha
    password = f"{prefix}{reversed_year}{name_length}"
    # Retornamos a senha gerada
    return password

# Pedimos o nome ao usuario
# "user_name" = nome do usuario
user_name = input("Digite seu nome: ")

# Pedimos o ano de nascimento
# "year" = ano
year = int(input("Digite seu ano de nascimento: "))

# Geramos a senha usando a funcao
# "result" = resultado
result = generate_password(user_name, year)

# Exibimos a senha gerada
print(f"Sua senha: {result}")
```

---

## Exercício 6 — Jogo de Adivinhacao — Nível: Básico

**Conceitos:** variáveis, loops (while), condicionais, input, contadores

### Enunciado

Crie um programa que defina um número secreto (fixo no código, por exemplo 42). O usuario tem ate 5 tentativas para adivinhar. A cada tentativa, o programa deve informar se o palpite e "muito alto" ou "muito baixo". Se acertar, exiba quantas tentativas foram necessarias. Se esgotar as tentativas, revele o número.

### Dicas

- Use uma variável para o número secreto e outra para contar tentativas
- Use `while` com duas condições: tentativas restantes e não acertou
- Compare o palpite com o número secreto usando `if/elif/else`
- Incremente o contador a cada tentativa

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Número secreto `42`, palpites `20`, `50`, `42` → saida: `Parabens! Voce acertou em 3 tentativas!`
- **Caso de borda:** Número secreto `42`, palpites `1`, `2`, `3`, `4`, `5` → saida: `Suas tentativas acabaram! O numero era 42`

### Resposta Comentada

```python
# Definimos o numero secreto
# "secret_number" = numero secreto
secret_number = 42

# Definimos o maximo de tentativas
# "max_attempts" = maximo de tentativas
max_attempts = 5

# Contador de tentativas realizadas
# "attempts" = tentativas
attempts = 0

# Variavel que indica se o usuario acertou
# "guessed" = adivinhou
guessed = False

# Informamos as regras ao usuario
print(f"Adivinhe o numero entre 1 e 100. Voce tem {max_attempts} tentativas.")

# Loop que continua enquanto houver tentativas e nao tiver acertado
while attempts < max_attempts and not guessed:
    # Pedimos um palpite ao usuario
    # "guess" = palpite
    guess = int(input("Seu palpite: "))
    # Incrementamos o contador de tentativas
    attempts = attempts + 1

    # Verificamos se acertou
    if guess == secret_number:
        # O usuario acertou
        guessed = True
        # Exibimos parabens com o numero de tentativas
        print(f"Parabens! Voce acertou em {attempts} tentativas!")
    elif guess < secret_number:
        # O palpite e menor que o numero secreto
        print("Muito baixo! Tente um numero maior.")
    else:
        # O palpite e maior que o numero secreto
        print("Muito alto! Tente um numero menor.")

# Se nao acertou apos todas as tentativas
if not guessed:
    # Revelamos o numero secreto
    print(f"Suas tentativas acabaram! O numero era {secret_number}")
```

---

## Exercício 7 — Agenda de Contatos — Nível: Intermediario

**Conceitos:** dicionários, listas, funções, loops, condicionais

### Enunciado

Crie um programa com uma lista de dicionários representando contatos (nome, telefone, email). Implemente uma função `find_contact` (encontrar contato) que receba a lista e um nome, e retorne o dicionário do contato encontrado ou `None` se não existir. Implemente também uma função `list_contacts` (listar contatos) que exiba todos os contatos formatados.

### Dicas

- Crie a lista de contatos com pelo menos 3 dicionários
- Na função de busca, use `for` para percorrer a lista
- Compare o nome buscado com o nome do contato (use `.lower()` para ignorar maiusculas)
- Na função de listagem, use `for` e `enumerate()` para numerar

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Buscar `"Ana"` em uma lista que contem Ana → saida: `Nome: Ana | Telefone: 1234-5678 | Email: ana@email.com`
- **Caso de borda:** Buscar `"Zeca"` em uma lista que não contem Zeca → saida: `Contato nao encontrado`

### Resposta Comentada

```python
# Funcao que busca um contato pelo nome na lista
# "find_contact" = encontrar contato
# "contacts" = contatos, "search_name" = nome buscado
def find_contact(contacts, search_name):
    # Percorremos cada contato na lista
    # "contact" = contato
    for contact in contacts:
        # Comparamos o nome do contato com o nome buscado (ignorando maiusculas)
        if contact["name"].lower() == search_name.lower():
            # Encontramos o contato, retornamos o dicionario
            return contact
    # Se percorreu toda a lista sem encontrar, retorna None (nenhum)
    return None

# Funcao que lista todos os contatos formatados
# "list_contacts" = listar contatos
# "contacts" = contatos
def list_contacts(contacts):
    # Verificamos se a lista esta vazia
    if len(contacts) == 0:
        # Lista vazia, informamos ao usuario
        print("Nenhum contato cadastrado.")
        # Saimos da funcao
        return
    # Percorremos cada contato com indice numerado
    # "index" = indice, "contact" = contato
    for index, contact in enumerate(contacts, 1):
        # Exibimos o contato formatado com numero, nome, telefone e email
        print(f"{index}. Nome: {contact['name']} | Telefone: {contact['phone']} | Email: {contact['email']}")

# Criamos a lista de contatos com 3 dicionarios
# "contacts_list" = lista de contatos
contacts_list = [
    {"name": "Ana", "phone": "1234-5678", "email": "ana@email.com"},
    {"name": "Bruno", "phone": "9876-5432", "email": "bruno@email.com"},
    {"name": "Carla", "phone": "5555-1234", "email": "carla@email.com"}
]

# Listamos todos os contatos
print("=== Lista de Contatos ===")
list_contacts(contacts_list)

# Buscamos um contato pelo nome
# "search" = busca
print("\n=== Busca de Contato ===")
search = input("Digite o nome para buscar: ")

# Usamos a funcao de busca
# "found" = encontrado
found = find_contact(contacts_list, search)

# Verificamos se encontrou
if found is not None:
    # Exibimos os dados do contato encontrado
    print(f"Nome: {found['name']} | Telefone: {found['phone']} | Email: {found['email']}")
else:
    # Contato nao encontrado
    print("Contato nao encontrado")
```

---

## Exercício 8 — Contador de Palavras — Nível: Intermediario

**Conceitos:** funções, strings, métodos de string, dicionários, loops

### Enunciado

Crie uma função chamada `count_words` (contar palavras) que receba um texto e retorne um dicionário onde cada chave e uma palavra (em minusculas) e o valor e a quantidade de vezes que ela aparece no texto. Exiba as palavras e suas contagens.

### Dicas

- Use `.lower()` para converter o texto para minusculas
- Use `.split()` para separar o texto em uma lista de palavras
- Percorra a lista com `for` e use um dicionário para contar
- Para cada palavra, verifique se ja existe no dicionário com `in`

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Texto `"o gato viu o rato e o gato correu"` → saida deve incluir `o: 3`, `gato: 2`, `viu: 1`, `rato: 1`
- **Caso de borda:** Texto `"Python"` → saida: `python: 1` (apenas uma palavra)

### Resposta Comentada

```python
# Funcao que conta quantas vezes cada palavra aparece no texto
# "count_words" = contar palavras
# "text" = texto
def count_words(text):
    # Convertemos o texto para minusculas para tratar "O" e "o" como iguais
    # "lower_text" = texto em minusculas
    lower_text = text.lower()
    # Separamos o texto em uma lista de palavras usando split()
    # "words" = palavras
    words = lower_text.split()
    # Criamos um dicionario vazio para armazenar as contagens
    # "word_count" = contagem de palavras
    word_count = {}
    # Percorremos cada palavra da lista
    # "word" = palavra
    for word in words:
        # Verificamos se a palavra ja esta no dicionario
        if word in word_count:
            # Se ja existe, incrementamos a contagem em 1
            word_count[word] = word_count[word] + 1
        else:
            # Se nao existe, adicionamos com contagem 1
            word_count[word] = 1
    # Retornamos o dicionario com as contagens
    return word_count

# Pedimos um texto ao usuario
# "user_text" = texto do usuario
user_text = input("Digite um texto: ")

# Chamamos a funcao e guardamos o resultado
# "result" = resultado
result = count_words(user_text)

# Exibimos cada palavra e sua contagem
# "word" = palavra, "count" = contagem
for word, count in result.items():
    # Exibimos no formato "palavra: contagem"
    print(f"{word}: {count}")
```

---

## Exercício 9 — Filtro de Números Pares e Impares — Nível: Intermediario

**Conceitos:** funções, listas, loops, condicionais, operador módulo

### Enunciado

Crie uma função chamada `separate_numbers` (separar números) que receba uma lista de números inteiros e retorne duas listas: uma com os números pares e outra com os impares. O programa deve pedir números ao usuario ate que ele digite 0 para parar.

### Dicas

- Use um loop `while` para receber números ate o usuario digitar 0
- Dentro da função, use `for` para percorrer a lista
- Use o operador módulo `%` para verificar se e par: `numero % 2 == 0`
- Retorne as duas listas usando `return pares, impares`

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Números `3, 8, 5, 12, 7, 0` → saida: `Pares: [8, 12]` e `Impares: [3, 5, 7]`
- **Caso de borda:** Números `0` (apenas zero) → saida: `Pares: []` e `Impares: []` (listas vazias)

### Resposta Comentada

```python
# Funcao que separa numeros em pares e impares
# "separate_numbers" = separar numeros
# "numbers" = numeros
def separate_numbers(numbers):
    # Criamos uma lista vazia para os numeros pares
    # "even" = par
    even = []
    # Criamos uma lista vazia para os numeros impares
    # "odd" = impar
    odd = []
    # Percorremos cada numero da lista recebida
    # "number" = numero
    for number in numbers:
        # Verificamos se o numero e par usando o operador modulo
        # Se o resto da divisao por 2 for zero, e par
        if number % 2 == 0:
            # Adicionamos o numero a lista de pares
            even.append(number)
        else:
            # Caso contrario, adicionamos a lista de impares
            odd.append(number)
    # Retornamos as duas listas (pares e impares)
    return even, odd

# Criamos uma lista vazia para armazenar os numeros digitados
# "user_numbers" = numeros do usuario
user_numbers = []

# Informamos as instrucoes ao usuario
print("Digite numeros inteiros (0 para parar):")

# Loop que continua ate o usuario digitar 0
while True:
    # Pedimos um numero ao usuario
    # "value" = valor
    value = int(input("Numero: "))
    # Verificamos se o usuario quer parar
    if value == 0:
        # Saimos do loop com break
        break
    # Adicionamos o numero a lista
    user_numbers.append(value)

# Chamamos a funcao e recebemos as duas listas
# "even_list" = lista de pares, "odd_list" = lista de impares
even_list, odd_list = separate_numbers(user_numbers)

# Exibimos os resultados
print(f"Pares: {even_list}")
print(f"Impares: {odd_list}")
```

---

## Exercício 10 — Calculadora de Media com Conceito — Nível: Intermediario

**Conceitos:** funções, listas, loops, condicionais, operadores matematicos, tuplas

### Enunciado

Crie uma função chamada `calculate_average` (calcular media) que receba uma lista de notas e retorne uma tupla com a media e o conceito. Os conceitos sao: A (media >= 9), B (media >= 7), C (media >= 5), D (media < 5). O programa deve pedir as notas ao usuario.

### Dicas

- Use `sum()` para somar todos os elementos da lista
- Use `len()` para contar quantos elementos tem na lista
- Media = soma / quantidade
- Use `if/elif/else` para determinar o conceito
- Retorne uma tupla: `return media, conceito`

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Notas `8.0, 7.5, 9.0` → saida: `Media: 8.17` e `Conceito: B`
- **Caso de borda:** Notas `10.0` → saida: `Media: 10.00` e `Conceito: A` (apenas uma nota)

### Resposta Comentada

```python
# Funcao que calcula a media e retorna o conceito
# "calculate_average" = calcular media
# "grades" = notas
def calculate_average(grades):
    # Verificamos se a lista de notas esta vazia
    if len(grades) == 0:
        # Se estiver vazia, retornamos zero e conceito D
        return 0.0, "D"
    # Calculamos a soma de todas as notas
    # "total" = total (soma)
    total = sum(grades)
    # Calculamos a media dividindo a soma pela quantidade de notas
    # "average" = media
    average = total / len(grades)
    # Determinamos o conceito com base na media
    # "grade_letter" = letra do conceito
    if average >= 9:
        # Media 9 ou mais: conceito A
        grade_letter = "A"
    elif average >= 7:
        # Media 7 ou mais: conceito B
        grade_letter = "B"
    elif average >= 5:
        # Media 5 ou mais: conceito C
        grade_letter = "C"
    else:
        # Media abaixo de 5: conceito D
        grade_letter = "D"
    # Retornamos a media e o conceito como tupla
    return average, grade_letter

# Criamos uma lista vazia para armazenar as notas
# "grades_list" = lista de notas
grades_list = []

# Pedimos quantas notas o usuario quer digitar
# "num_grades" = numero de notas
num_grades = int(input("Quantas notas voce quer digitar? "))

# Loop para receber cada nota
# "i" = indice (contador)
for i in range(num_grades):
    # Pedimos cada nota ao usuario
    # "grade" = nota
    grade = float(input(f"Digite a nota {i + 1}: "))
    # Adicionamos a nota a lista
    grades_list.append(grade)

# Chamamos a funcao e recebemos a media e o conceito
# "avg" = media (abreviacao de average), "concept" = conceito
avg, concept = calculate_average(grades_list)

# Exibimos a media formatada com 2 casas decimais
print(f"Media: {avg:.2f}")
# Exibimos o conceito
print(f"Conceito: {concept}")
```

---

## Exercício 11 — Removedor de Duplicatas — Nível: Intermediario

**Conceitos:** funções, listas, conjuntos, loops, condicionais

### Enunciado

Crie uma função chamada `remove_duplicates` (remover duplicatas) que receba uma lista e retorne uma nova lista sem elementos repetidos, mantendo a ordem original de aparicao. Não use a conversão direta para `set()` — implemente a lógica manualmente.

### Dicas

- Crie uma lista vazia para o resultado e um conjunto vazio para controle
- Percorra a lista original com `for`
- Para cada elemento, verifique se ja esta no conjunto de controle
- Se não estiver, adicione ao resultado e ao conjunto de controle

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Lista `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]` → saida: `[3, 1, 4, 5, 9, 2, 6]`
- **Caso de borda:** Lista `[7, 7, 7, 7]` → saida: `[7]` (todos iguais)

### Resposta Comentada

```python
# Funcao que remove elementos duplicados mantendo a ordem original
# "remove_duplicates" = remover duplicatas
# "original_list" = lista original
def remove_duplicates(original_list):
    # Criamos uma lista vazia para armazenar os elementos unicos
    # "unique_list" = lista de unicos
    unique_list = []
    # Criamos um conjunto vazio para controlar quais elementos ja vimos
    # "seen" = vistos (elementos ja encontrados)
    seen = set()
    # Percorremos cada elemento da lista original
    # "element" = elemento
    for element in original_list:
        # Verificamos se o elemento ainda nao foi visto
        if element not in seen:
            # Adicionamos o elemento a lista de unicos
            unique_list.append(element)
            # Marcamos o elemento como visto no conjunto
            seen.add(element)
    # Retornamos a lista sem duplicatas
    return unique_list

# Criamos uma lista de exemplo com elementos repetidos
# "numbers" = numeros
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Exibimos a lista original
print(f"Lista original: {numbers}")

# Chamamos a funcao e guardamos o resultado
# "clean_list" = lista limpa (sem duplicatas)
clean_list = remove_duplicates(numbers)

# Exibimos a lista sem duplicatas
print(f"Sem duplicatas: {clean_list}")
```

---

## Exercício 12 — Validador de CPF Simplificado — Nível: Intermediario

**Conceitos:** funções, strings, loops, condicionais, tratamento de erros

### Enunciado

Crie uma função chamada `validate_cpf_format` (validar formato de CPF) que receba uma string e verifique se ela tem o formato básico de um CPF: exatamente 11 digitos numericos (sem pontos ou tracos). A função deve retornar `True` se o formato for válido ou `False` caso contrario. Também verifique se todos os digitos não sao iguais (como "11111111111").

### Dicas

- Use `len()` para verificar se tem 11 caracteres
- Use `.isdigit()` para verificar se todos os caracteres sao números
- Para verificar se todos os digitos sao iguais, compare com `cpf[0] * 11`
- Retorne `True` apenas se passar em todas as verificacoes

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** CPF `"12345678901"` → saida: `Formato valido`
- **Caso de borda:** CPF `"11111111111"` → saida: `Formato invalido` (todos os digitos iguais)
- **Caso de borda:** CPF `"123.456.789-01"` → saida: `Formato invalido` (contem pontos e tracos)

### Resposta Comentada

```python
# Funcao que valida o formato basico de um CPF
# "validate_cpf_format" = validar formato de CPF
# "cpf" = CPF (Cadastro de Pessoa Fisica)
def validate_cpf_format(cpf):
    # Verificamos se o CPF tem exatamente 11 caracteres
    if len(cpf) != 11:
        # Se nao tem 11 caracteres, o formato e invalido
        return False
    # Verificamos se todos os caracteres sao digitos numericos
    # isdigit() retorna True se todos os caracteres forem numeros
    if not cpf.isdigit():
        # Se contem letras, pontos ou tracos, e invalido
        return False
    # Verificamos se todos os digitos sao iguais
    # Multiplicamos o primeiro digito por 11 e comparamos com o CPF inteiro
    if cpf == cpf[0] * 11:
        # Se todos os digitos forem iguais, e invalido
        return False
    # Se passou em todas as verificacoes, o formato e valido
    return True

# Pedimos o CPF ao usuario
# "user_cpf" = CPF do usuario
user_cpf = input("Digite um CPF (apenas numeros): ")

# Verificamos o formato usando a funcao
if validate_cpf_format(user_cpf):
    # O formato e valido
    print("Formato valido")
else:
    # O formato e invalido
    print("Formato invalido")
```

---

## Exercício 13 — Conversor de Temperaturas — Nível: Intermediario

**Conceitos:** funções, dicionários, condicionais, tratamento de erros, loops

### Enunciado

Crie um programa com tres funções de conversão: `celsius_to_fahrenheit` (Celsius para Fahrenheit), `fahrenheit_to_celsius` (Fahrenheit para Celsius) e `celsius_to_kelvin` (Celsius para Kelvin). O programa deve exibir um menu para o usuario escolher a conversão desejada e repetir ate que ele escolha sair.

### Dicas

- Formulas: F = C * 9/5 + 32, C = (F - 32) * 5/9, K = C + 273.15
- Use `while True` para repetir o menu
- Use `if/elif/else` para tratar a opcao escolhida
- Use `try/except` para tratar entradas invalidas

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Celsius `100` para Fahrenheit → saida: `212.00 F`
- **Caso de borda:** Celsius `0` para Kelvin → saida: `273.15 K` (zero absoluto em Celsius)

### Resposta Comentada

```python
# Funcao que converte Celsius para Fahrenheit
# "celsius_to_fahrenheit" = celsius para fahrenheit
# "celsius" = temperatura em Celsius
def celsius_to_fahrenheit(celsius):
    # Aplicamos a formula: F = C * 9/5 + 32
    # "fahrenheit" = temperatura em Fahrenheit
    fahrenheit = celsius * 9 / 5 + 32
    # Retornamos o valor convertido
    return fahrenheit

# Funcao que converte Fahrenheit para Celsius
# "fahrenheit_to_celsius" = fahrenheit para celsius
# "fahrenheit" = temperatura em Fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    # Aplicamos a formula: C = (F - 32) * 5/9
    # "celsius" = temperatura em Celsius
    celsius = (fahrenheit - 32) * 5 / 9
    # Retornamos o valor convertido
    return celsius

# Funcao que converte Celsius para Kelvin
# "celsius_to_kelvin" = celsius para kelvin
# "celsius" = temperatura em Celsius
def celsius_to_kelvin(celsius):
    # Aplicamos a formula: K = C + 273.15
    # "kelvin" = temperatura em Kelvin
    kelvin = celsius + 273.15
    # Retornamos o valor convertido
    return kelvin

# Loop principal do programa
while True:
    # Exibimos o menu de opcoes
    print("\n=== Conversor de Temperaturas ===")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Celsius para Kelvin")
    print("4. Sair")

    # Pedimos a opcao ao usuario
    # "option" = opcao
    option = input("Escolha uma opcao: ")

    # Verificamos qual opcao foi escolhida
    if option == "1":
        # Opcao 1: Celsius para Fahrenheit
        try:
            # Pedimos a temperatura em Celsius
            # "temp" = temperatura
            temp = float(input("Digite a temperatura em Celsius: "))
            # Convertemos e exibimos o resultado
            # "result" = resultado
            result = celsius_to_fahrenheit(temp)
            print(f"{result:.2f} F")
        except ValueError:
            # O usuario digitou algo que nao e numero
            print("Erro: digite um numero valido.")
    elif option == "2":
        # Opcao 2: Fahrenheit para Celsius
        try:
            # Pedimos a temperatura em Fahrenheit
            temp = float(input("Digite a temperatura em Fahrenheit: "))
            # Convertemos e exibimos o resultado
            result = fahrenheit_to_celsius(temp)
            print(f"{result:.2f} C")
        except ValueError:
            # O usuario digitou algo que nao e numero
            print("Erro: digite um numero valido.")
    elif option == "3":
        # Opcao 3: Celsius para Kelvin
        try:
            # Pedimos a temperatura em Celsius
            temp = float(input("Digite a temperatura em Celsius: "))
            # Convertemos e exibimos o resultado
            result = celsius_to_kelvin(temp)
            print(f"{result:.2f} K")
        except ValueError:
            # O usuario digitou algo que nao e numero
            print("Erro: digite um numero valido.")
    elif option == "4":
        # Opcao 4: Sair do programa
        print("Ate logo!")
        # Saimos do loop com break
        break
    else:
        # Opcao invalida
        print("Opcao invalida. Escolha de 1 a 4.")
```

---

## Exercício 14 — Organizador de Compras por Categoria — Nível: Intermediario

**Conceitos:** funções, dicionários, listas, loops, condicionais, tuplas

### Enunciado

Crie uma função chamada `organize_by_category` (organizar por categoria) que receba uma lista de tuplas no formato `(produto, categoria, preco)` e retorne um dicionário onde cada chave e uma categoria e o valor e uma lista de tuplas `(produto, preco)` daquela categoria. Exiba os produtos organizados por categoria.

### Dicas

- Percorra a lista de tuplas com `for`
- Para cada tupla, use desempacotamento: `produto, categoria, preco = tupla`
- Verifique se a categoria ja existe no dicionário com `in`
- Se não existir, crie uma lista vazia para aquela categoria

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Lista com `("Arroz", "Alimentos", 5.99)`, `("Sabao", "Limpeza", 3.50)`, `("Feijao", "Alimentos", 7.20)` → saida deve agrupar Arroz e Feijao em "Alimentos" e Sabao em "Limpeza"
- **Caso de borda:** Lista vazia `[]` → saida: `Nenhum produto para organizar`

### Resposta Comentada

```python
# Funcao que organiza produtos por categoria
# "organize_by_category" = organizar por categoria
# "products" = produtos (lista de tuplas)
def organize_by_category(products):
    # Criamos um dicionario vazio para armazenar as categorias
    # "categories" = categorias
    categories = {}
    # Percorremos cada tupla da lista de produtos
    # "product_name" = nome do produto, "category" = categoria, "price" = preco
    for product_name, category, price in products:
        # Verificamos se a categoria ja existe no dicionario
        if category not in categories:
            # Se nao existe, criamos uma lista vazia para essa categoria
            categories[category] = []
        # Adicionamos o produto e preco como tupla na lista da categoria
        categories[category].append((product_name, price))
    # Retornamos o dicionario organizado
    return categories

# Criamos uma lista de produtos como tuplas (nome, categoria, preco)
# "shopping_list" = lista de compras
shopping_list = [
    ("Arroz", "Alimentos", 5.99),
    ("Sabao", "Limpeza", 3.50),
    ("Feijao", "Alimentos", 7.20),
    ("Detergente", "Limpeza", 2.80),
    ("Macarrao", "Alimentos", 4.50),
    ("Caderno", "Papelaria", 12.00)
]

# Verificamos se a lista esta vazia
if len(shopping_list) == 0:
    # Lista vazia, informamos ao usuario
    print("Nenhum produto para organizar")
else:
    # Chamamos a funcao para organizar por categoria
    # "organized" = organizado
    organized = organize_by_category(shopping_list)
    # Percorremos cada categoria e seus produtos
    # "category" = categoria, "items" = itens
    for category, items in organized.items():
        # Exibimos o nome da categoria
        print(f"\n=== {category} ===")
        # Percorremos cada produto da categoria
        # "name" = nome, "price" = preco
        for name, price in items:
            # Exibimos o produto e seu preco formatado
            print(f"  {name}: R$ {price:.2f}")
```

---

## Exercício 15 — Analisador de Texto — Nível: Intermediario

**Conceitos:** funções, strings, dicionários, loops, condicionais, métodos de string

### Enunciado

Crie uma função chamada `analyze_text` (analisar texto) que receba uma string e retorne um dicionário com as seguintes estatisticas: quantidade de caracteres, quantidade de palavras, quantidade de frases (terminadas em `.`, `!` ou `?`), e a palavra mais longa. Exiba todas as estatisticas formatadas.

### Dicas

- Use `len()` para contar caracteres
- Use `.split()` para separar palavras e contar
- Para contar frases, conte os caracteres `.`, `!` e `?`
- Para encontrar a palavra mais longa, percorra a lista de palavras e compare tamanhos

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Texto `"Python e legal. Eu gosto muito!"` → saida: `Caracteres: 31`, `Palavras: 6`, `Frases: 2`, `Palavra mais longa: Python`
- **Caso de borda:** Texto `"Oi"` → saida: `Caracteres: 2`, `Palavras: 1`, `Frases: 0`, `Palavra mais longa: Oi`

### Resposta Comentada

```python
# Funcao que analisa um texto e retorna estatisticas
# "analyze_text" = analisar texto
# "text" = texto
def analyze_text(text):
    # Contamos o total de caracteres no texto
    # "char_count" = contagem de caracteres
    char_count = len(text)
    # Separamos o texto em palavras e contamos
    # "words" = palavras
    words = text.split()
    # "word_count" = contagem de palavras
    word_count = len(words)
    # Contamos as frases (terminadores: ponto, exclamacao, interrogacao)
    # "sentence_count" = contagem de frases
    sentence_count = 0
    # Percorremos cada caractere do texto
    # "char" = caractere
    for char in text:
        # Verificamos se e um terminador de frase
        if char in ".!?":
            # Incrementamos o contador de frases
            sentence_count = sentence_count + 1
    # Encontramos a palavra mais longa
    # "longest_word" = palavra mais longa
    longest_word = ""
    # Percorremos cada palavra da lista
    # "word" = palavra
    for word in words:
        # Removemos pontuacao do final da palavra para comparacao justa
        # "clean_word" = palavra limpa (sem pontuacao)
        clean_word = word.strip(".!?,;:")
        # Comparamos o tamanho com a palavra mais longa encontrada ate agora
        if len(clean_word) > len(longest_word):
            # Atualizamos a palavra mais longa
            longest_word = clean_word
    # Montamos o dicionario com todas as estatisticas
    # "stats" = estatisticas
    stats = {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count,
        "longest_word": longest_word
    }
    # Retornamos o dicionario de estatisticas
    return stats

# Pedimos um texto ao usuario
# "user_text" = texto do usuario
user_text = input("Digite um texto para analisar: ")

# Chamamos a funcao e guardamos o resultado
# "result" = resultado
result = analyze_text(user_text)

# Exibimos as estatisticas formatadas
print(f"\nCaracteres: {result['characters']}")
print(f"Palavras: {result['words']}")
print(f"Frases: {result['sentences']}")
print(f"Palavra mais longa: {result['longest_word']}")
```

---

## Exercício 16 — Classe Produto com Estoque — Nível: Avancado

**Conceitos:** classes, métodos, atributos, condicionais, funções

### Enunciado

Crie uma classe chamada `Product` (Produto) com os atributos `name` (nome), `price` (preco) e `quantity` (quantidade). Implemente os métodos: `total_value` (valor total = preco * quantidade), `sell` (vender — reduz a quantidade se houver estoque) e `restock` (reabastecer — aumenta a quantidade). Crie pelo menos 2 produtos e demonstre o uso dos métodos.

### Dicas

- Use `__init__` para inicializar os atributos
- No método `sell`, verifique se ha estoque suficiente antes de reduzir
- No método `restock`, apenas some a quantidade recebida ao estoque atual
- Use `self` para acessar os atributos dentro dos métodos

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Produto "Arroz", preco 5.99, quantidade 10 → `total_value()` retorna `59.90`
- **Caso de borda:** Tentar vender 15 unidades quando ha apenas 10 → saida: `Estoque insuficiente`

### Resposta Comentada

```python
# Classe que representa um produto com controle de estoque
# "Product" = Produto
class Product:
    # Metodo construtor que inicializa os atributos do produto
    # "self" = referencia ao proprio objeto
    # "name" = nome, "price" = preco, "quantity" = quantidade
    def __init__(self, name, price, quantity):
        # Armazenamos o nome do produto
        self.name = name
        # Armazenamos o preco do produto
        self.price = price
        # Armazenamos a quantidade em estoque
        self.quantity = quantity

    # Metodo que calcula o valor total do estoque deste produto
    # "total_value" = valor total
    def total_value(self):
        # Multiplicamos o preco pela quantidade em estoque
        # "value" = valor
        value = self.price * self.quantity
        # Retornamos o valor total
        return value

    # Metodo que realiza uma venda, reduzindo o estoque
    # "sell" = vender
    # "amount" = quantidade a vender
    def sell(self, amount):
        # Verificamos se ha estoque suficiente
        if amount > self.quantity:
            # Nao ha estoque suficiente para a venda
            print(f"Estoque insuficiente para {self.name}. Disponivel: {self.quantity}")
            # Retornamos False indicando que a venda nao foi realizada
            return False
        # Reduzimos a quantidade em estoque
        self.quantity = self.quantity - amount
        # Informamos que a venda foi realizada
        print(f"Venda realizada: {amount}x {self.name}")
        # Retornamos True indicando sucesso
        return True

    # Metodo que reabastece o estoque do produto
    # "restock" = reabastecer
    # "amount" = quantidade a adicionar
    def restock(self, amount):
        # Somamos a quantidade recebida ao estoque atual
        self.quantity = self.quantity + amount
        # Informamos o novo estoque
        print(f"Estoque de {self.name} atualizado para {self.quantity}")

# Criamos dois produtos
# "product1" = produto 1, "product2" = produto 2
product1 = Product("Arroz", 5.99, 10)
product2 = Product("Feijao", 7.50, 5)

# Exibimos o valor total do estoque de cada produto
print(f"{product1.name}: valor total em estoque = R$ {product1.total_value():.2f}")
print(f"{product2.name}: valor total em estoque = R$ {product2.total_value():.2f}")

# Realizamos uma venda de 3 unidades do produto 1
product1.sell(3)
# Exibimos o estoque atualizado
print(f"{product1.name}: estoque atual = {product1.quantity}")

# Tentamos vender mais do que o estoque do produto 2
product2.sell(15)

# Reabastecemos o produto 2
product2.restock(20)
```

---

## Exercício 17 — Registro de Alunos com Arquivo — Nível: Avancado

**Conceitos:** funções, dicionários, listas, arquivos, tratamento de erros

### Enunciado

Crie um programa que permita cadastrar alunos (nome e nota) e salvar os dados em um arquivo de texto chamado `alunos.txt`. Cada linha do arquivo deve ter o formato `nome;nota`. Implemente funções para: `save_students` (salvar alunos no arquivo), `load_students` (carregar alunos do arquivo) e `show_students` (exibir alunos). Ao iniciar, o programa deve carregar os alunos existentes no arquivo.

### Dicas

- Use `open()` com modo `"w"` para escrever e `"r"` para ler
- Use `with` para garantir que o arquivo sera fechado
- Use `try/except` para tratar o caso do arquivo não existir
- Separe nome e nota com `;` e use `.split(";")` para ler

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Cadastre "Maria;8.5" e "Joao;7.0", feche o programa, abra novamente → os alunos devem ser carregados do arquivo
- **Caso de borda:** Execute o programa pela primeira vez (sem arquivo existente) → deve funcionar sem erro e criar o arquivo ao salvar

### Resposta Comentada

```python
# Funcao que salva a lista de alunos em um arquivo de texto
# "save_students" = salvar alunos
# "students" = alunos (lista de dicionarios), "filename" = nome do arquivo
def save_students(students, filename):
    # Abrimos o arquivo para escrita (modo "w" sobrescreve o conteudo)
    # "file" = arquivo
    with open(filename, "w") as file:
        # Percorremos cada aluno da lista
        # "student" = aluno
        for student in students:
            # Escrevemos o nome e a nota separados por ponto e virgula
            # Adicionamos \n para pular linha
            file.write(f"{student['name']};{student['grade']}\n")
    # Informamos que os dados foram salvos
    print(f"Dados salvos em {filename}")

# Funcao que carrega alunos de um arquivo de texto
# "load_students" = carregar alunos
# "filename" = nome do arquivo
def load_students(filename):
    # Criamos uma lista vazia para armazenar os alunos
    # "students" = alunos
    students = []
    # Tentamos abrir o arquivo para leitura
    try:
        # Abrimos o arquivo no modo leitura ("r")
        with open(filename, "r") as file:
            # Lemos todas as linhas do arquivo
            # "lines" = linhas
            lines = file.readlines()
            # Percorremos cada linha do arquivo
            # "line" = linha
            for line in lines:
                # Removemos espacos e quebras de linha com strip()
                # Separamos o nome e a nota pelo ponto e virgula
                # "parts" = partes (pedacos da linha)
                parts = line.strip().split(";")
                # Verificamos se a linha tem as duas partes (nome e nota)
                if len(parts) == 2:
                    # Criamos um dicionario com os dados do aluno
                    # "student" = aluno
                    student = {
                        "name": parts[0],
                        "grade": float(parts[1])
                    }
                    # Adicionamos o aluno a lista
                    students.append(student)
    except FileNotFoundError:
        # O arquivo nao existe ainda — isso e normal na primeira execucao
        print("Arquivo nao encontrado. Iniciando com lista vazia.")
    # Retornamos a lista de alunos (vazia ou preenchida)
    return students

# Funcao que exibe todos os alunos formatados
# "show_students" = exibir alunos
# "students" = alunos
def show_students(students):
    # Verificamos se a lista esta vazia
    if len(students) == 0:
        # Nenhum aluno cadastrado
        print("Nenhum aluno cadastrado.")
        # Saimos da funcao
        return
    # Exibimos o cabecalho
    print("\n=== Lista de Alunos ===")
    # Percorremos cada aluno com indice numerado
    # "index" = indice, "student" = aluno
    for index, student in enumerate(students, 1):
        # Exibimos o numero, nome e nota do aluno
        print(f"{index}. {student['name']} - Nota: {student['grade']:.1f}")

# Nome do arquivo onde os dados serao salvos
# "data_file" = arquivo de dados
data_file = "alunos.txt"

# Carregamos os alunos existentes do arquivo
# "students_list" = lista de alunos
students_list = load_students(data_file)

# Informamos quantos alunos foram carregados
print(f"{len(students_list)} aluno(s) carregado(s).")

# Pedimos ao usuario quantos alunos quer cadastrar
# "num_students" = numero de alunos
num_students = int(input("Quantos alunos deseja cadastrar? "))

# Loop para cadastrar cada aluno
# "i" = indice (contador)
for i in range(num_students):
    # Pedimos o nome do aluno
    # "name" = nome
    name = input(f"Nome do aluno {i + 1}: ")
    # Pedimos a nota do aluno
    # "grade" = nota
    grade = float(input(f"Nota do aluno {i + 1}: "))
    # Adicionamos o aluno a lista como dicionario
    students_list.append({"name": name, "grade": grade})

# Salvamos todos os alunos no arquivo
save_students(students_list, data_file)

# Exibimos a lista completa de alunos
show_students(students_list)
```

---

## Exercício 18 — Agenda Telefonica com JSON — Nível: Avancado

**Conceitos:** funções, dicionários, listas, JSON, arquivos, tratamento de erros

### Enunciado

Crie um programa de agenda telefonica que armazene contatos em um arquivo JSON. Cada contato deve ter `name` (nome), `phone` (telefone) e `email`. Implemente funções para: `add_contact` (adicionar contato), `search_contact` (buscar contato por nome), `save_to_json` (salvar em JSON) e `load_from_json` (carregar do JSON). O programa deve carregar os contatos ao iniciar e salvar ao adicionar.

### Dicas

- Use `import json` para trabalhar com JSON
- Use `json.dump()` para salvar e `json.load()` para carregar
- Use `indent=4` no `json.dump()` para formatar o arquivo
- Use `try/except` para tratar arquivo inexistente

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Adicione o contato "Ana", telefone "1234-5678", email "ana@email.com" → o arquivo `agenda.json` deve conter os dados formatados
- **Caso de borda:** Busque um contato que não existe → saida: `Contato nao encontrado`

### Resposta Comentada

```python
# Importamos o modulo json para trabalhar com arquivos JSON
# "json" = modulo para manipulacao de dados JSON
import json

# Funcao que salva a lista de contatos em um arquivo JSON
# "save_to_json" = salvar em JSON
# "contacts" = contatos, "filename" = nome do arquivo
def save_to_json(contacts, filename):
    # Abrimos o arquivo para escrita
    # "file" = arquivo
    with open(filename, "w") as file:
        # Salvamos a lista de contatos no formato JSON com indentacao
        # indent=4 formata o JSON com 4 espacos de indentacao
        json.dump(contacts, file, indent=4)
    # Informamos que os dados foram salvos
    print(f"Contatos salvos em {filename}")

# Funcao que carrega contatos de um arquivo JSON
# "load_from_json" = carregar do JSON
# "filename" = nome do arquivo
def load_from_json(filename):
    # Tentamos abrir e ler o arquivo JSON
    try:
        # Abrimos o arquivo para leitura
        with open(filename, "r") as file:
            # Carregamos os dados do JSON para uma lista Python
            # "contacts" = contatos
            contacts = json.load(file)
            # Retornamos a lista de contatos
            return contacts
    except FileNotFoundError:
        # Arquivo nao existe — retornamos lista vazia
        print("Arquivo nao encontrado. Iniciando com agenda vazia.")
        return []

# Funcao que adiciona um novo contato a lista
# "add_contact" = adicionar contato
# "contacts" = contatos, "name" = nome, "phone" = telefone, "email" = email
def add_contact(contacts, name, phone, email):
    # Criamos um dicionario com os dados do contato
    # "new_contact" = novo contato
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    # Adicionamos o contato a lista
    contacts.append(new_contact)
    # Informamos que o contato foi adicionado
    print(f"Contato {name} adicionado com sucesso!")

# Funcao que busca um contato pelo nome
# "search_contact" = buscar contato
# "contacts" = contatos, "search_name" = nome buscado
def search_contact(contacts, search_name):
    # Percorremos cada contato da lista
    # "contact" = contato
    for contact in contacts:
        # Comparamos o nome (ignorando maiusculas/minusculas)
        if contact["name"].lower() == search_name.lower():
            # Encontramos o contato, retornamos o dicionario
            return contact
    # Se nao encontrou, retornamos None (nenhum)
    return None

# Nome do arquivo JSON para armazenar os contatos
# "json_file" = arquivo JSON
json_file = "agenda.json"

# Carregamos os contatos existentes do arquivo
# "contacts_list" = lista de contatos
contacts_list = load_from_json(json_file)

# Informamos quantos contatos foram carregados
print(f"{len(contacts_list)} contato(s) carregado(s).")

# Adicionamos um novo contato de exemplo
# Pedimos os dados ao usuario
# "new_name" = novo nome
new_name = input("Nome do contato: ")
# "new_phone" = novo telefone
new_phone = input("Telefone: ")
# "new_email" = novo email
new_email = input("Email: ")

# Adicionamos o contato a lista
add_contact(contacts_list, new_name, new_phone, new_email)

# Salvamos a lista atualizada no arquivo JSON
save_to_json(contacts_list, json_file)

# Buscamos um contato pelo nome
# "search" = busca
search = input("\nDigite um nome para buscar: ")
# "found" = encontrado
found = search_contact(contacts_list, search)

# Verificamos se o contato foi encontrado
if found is not None:
    # Exibimos os dados do contato
    print(f"Nome: {found['name']}")
    print(f"Telefone: {found['phone']}")
    print(f"Email: {found['email']}")
else:
    # Contato nao encontrado
    print("Contato nao encontrado")
```

---

## Exercício 19 — Classe ContaBancaria — Nível: Avancado

**Conceitos:** classes, métodos, atributos, condicionais, tratamento de erros

### Enunciado

Crie uma classe chamada `BankAccount` (Conta Bancaria) com os atributos `owner` (titular), `balance` (saldo) e `account_number` (número da conta). Implemente os métodos: `deposit` (depositar), `withdraw` (sacar — com verificacao de saldo), `get_statement` (obter extrato — retorna uma string formatada). Crie duas contas e realize operações entre elas.

### Dicas

- Inicialize o saldo com 0.0 no `__init__`
- No método `withdraw`, verifique se o saldo e suficiente
- No método `deposit`, verifique se o valor e positivo
- Use f-strings para formatar o extrato

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Depositar 1000.00 e sacar 300.00 → saldo final: `700.00`
- **Caso de borda:** Tentar sacar 500.00 com saldo de 200.00 → saida: `Saldo insuficiente`

### Resposta Comentada

```python
# Classe que representa uma conta bancaria
# "BankAccount" = Conta Bancaria
class BankAccount:
    # Metodo construtor que inicializa os atributos da conta
    # "owner" = titular, "account_number" = numero da conta
    def __init__(self, owner, account_number):
        # Armazenamos o nome do titular
        self.owner = owner
        # Armazenamos o numero da conta
        self.account_number = account_number
        # Inicializamos o saldo com zero
        # "balance" = saldo
        self.balance = 0.0

    # Metodo que realiza um deposito na conta
    # "deposit" = depositar
    # "amount" = valor a depositar
    def deposit(self, amount):
        # Verificamos se o valor e positivo
        if amount <= 0:
            # Valor invalido para deposito
            print("Erro: o valor do deposito deve ser positivo.")
            # Retornamos False indicando falha
            return False
        # Somamos o valor ao saldo atual
        self.balance = self.balance + amount
        # Informamos o deposito realizado
        print(f"Deposito de R$ {amount:.2f} realizado na conta {self.account_number}")
        # Retornamos True indicando sucesso
        return True

    # Metodo que realiza um saque da conta
    # "withdraw" = sacar
    # "amount" = valor a sacar
    def withdraw(self, amount):
        # Verificamos se o valor e positivo
        if amount <= 0:
            # Valor invalido para saque
            print("Erro: o valor do saque deve ser positivo.")
            # Retornamos False indicando falha
            return False
        # Verificamos se ha saldo suficiente
        if amount > self.balance:
            # Saldo insuficiente para o saque
            print(f"Saldo insuficiente. Saldo atual: R$ {self.balance:.2f}")
            # Retornamos False indicando falha
            return False
        # Subtraimos o valor do saldo
        self.balance = self.balance - amount
        # Informamos o saque realizado
        print(f"Saque de R$ {amount:.2f} realizado da conta {self.account_number}")
        # Retornamos True indicando sucesso
        return True

    # Metodo que retorna o extrato da conta como string formatada
    # "get_statement" = obter extrato
    def get_statement(self):
        # Montamos a string do extrato com os dados da conta
        # "statement" = extrato
        statement = f"Conta: {self.account_number} | Titular: {self.owner} | Saldo: R$ {self.balance:.2f}"
        # Retornamos o extrato
        return statement

# Criamos duas contas bancarias
# "account1" = conta 1, "account2" = conta 2
account1 = BankAccount("Maria Silva", "001-1")
account2 = BankAccount("Joao Santos", "002-2")

# Realizamos depositos
account1.deposit(1000.00)
account2.deposit(500.00)

# Realizamos um saque da conta 1
account1.withdraw(300.00)

# Tentamos sacar mais do que o saldo da conta 2
account2.withdraw(800.00)

# Exibimos o extrato de ambas as contas
print("\n=== Extratos ===")
print(account1.get_statement())
print(account2.get_statement())
```

---

## Exercício 20 — Gerenciador de Tarefas com Arquivo — Nível: Avancado

**Conceitos:** funções, listas, dicionários, arquivos, JSON, loops, condicionais, tratamento de erros

### Enunciado

Crie um gerenciador de tarefas que permita adicionar, listar, marcar como concluida e remover tarefas. Cada tarefa deve ter `description` (descricao), `done` (concluida — True ou False) e `priority` (prioridade — "alta", "media" ou "baixa"). Os dados devem ser salvos em um arquivo JSON chamado `tarefas.json`. Implemente funções separadas para cada operação.

### Dicas

- Use uma lista de dicionários para armazenar as tarefas
- Use `json.dump()` e `json.load()` para persistir os dados
- Para marcar como concluida, altere o campo `done` para `True`
- Para remover, use o índice da tarefa na lista

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Adicione "Estudar Python" com prioridade "alta", liste as tarefas → deve aparecer `[ ] Estudar Python (alta)`
- **Caso de borda:** Tente marcar como concluida uma tarefa com índice inválido → saida: `Tarefa nao encontrada`

### Resposta Comentada

```python
# Importamos o modulo json para salvar e carregar dados
import json

# Funcao que carrega as tarefas do arquivo JSON
# "load_tasks" = carregar tarefas
# "filename" = nome do arquivo
def load_tasks(filename):
    # Tentamos abrir o arquivo
    try:
        # Abrimos o arquivo para leitura
        with open(filename, "r") as file:
            # Carregamos e retornamos os dados do JSON
            return json.load(file)
    except FileNotFoundError:
        # Arquivo nao existe, retornamos lista vazia
        return []

# Funcao que salva as tarefas no arquivo JSON
# "save_tasks" = salvar tarefas
# "tasks" = tarefas, "filename" = nome do arquivo
def save_tasks(tasks, filename):
    # Abrimos o arquivo para escrita
    with open(filename, "w") as file:
        # Salvamos as tarefas no formato JSON com indentacao
        json.dump(tasks, file, indent=4)

# Funcao que adiciona uma nova tarefa
# "add_task" = adicionar tarefa
# "tasks" = tarefas, "description" = descricao, "priority" = prioridade
def add_task(tasks, description, priority):
    # Criamos o dicionario da nova tarefa
    # "new_task" = nova tarefa
    new_task = {
        "description": description,
        "done": False,
        "priority": priority
    }
    # Adicionamos a tarefa a lista
    tasks.append(new_task)
    # Informamos que a tarefa foi adicionada
    print(f"Tarefa adicionada: {description}")

# Funcao que lista todas as tarefas
# "list_tasks" = listar tarefas
# "tasks" = tarefas
def list_tasks(tasks):
    # Verificamos se a lista esta vazia
    if len(tasks) == 0:
        # Nenhuma tarefa cadastrada
        print("Nenhuma tarefa cadastrada.")
        return
    # Percorremos cada tarefa com indice
    # "index" = indice, "task" = tarefa
    for index, task in enumerate(tasks, 1):
        # Definimos o marcador de status: [X] concluida, [ ] pendente
        # "status" = status da tarefa
        status = "[X]" if task["done"] else "[ ]"
        # Exibimos a tarefa formatada
        print(f"{index}. {status} {task['description']} ({task['priority']})")

# Funcao que marca uma tarefa como concluida
# "complete_task" = concluir tarefa
# "tasks" = tarefas, "task_index" = indice da tarefa (comecando em 1)
def complete_task(tasks, task_index):
    # Verificamos se o indice e valido
    if task_index < 1 or task_index > len(tasks):
        # Indice fora do intervalo valido
        print("Tarefa nao encontrada")
        return
    # Marcamos a tarefa como concluida (ajustamos o indice para base 0)
    tasks[task_index - 1]["done"] = True
    # Informamos que a tarefa foi concluida
    print(f"Tarefa {task_index} marcada como concluida!")

# Funcao que remove uma tarefa da lista
# "remove_task" = remover tarefa
# "tasks" = tarefas, "task_index" = indice da tarefa
def remove_task(tasks, task_index):
    # Verificamos se o indice e valido
    if task_index < 1 or task_index > len(tasks):
        # Indice fora do intervalo valido
        print("Tarefa nao encontrada")
        return
    # Removemos a tarefa da lista (ajustamos o indice para base 0)
    # "removed" = removida
    removed = tasks.pop(task_index - 1)
    # Informamos qual tarefa foi removida
    print(f"Tarefa removida: {removed['description']}")

# Nome do arquivo para persistencia
# "data_file" = arquivo de dados
data_file = "tarefas.json"

# Carregamos as tarefas existentes
# "task_list" = lista de tarefas
task_list = load_tasks(data_file)

# Adicionamos algumas tarefas de exemplo
add_task(task_list, "Estudar Python", "alta")
add_task(task_list, "Fazer compras", "media")
add_task(task_list, "Organizar mesa", "baixa")

# Listamos todas as tarefas
print("\n=== Tarefas ===")
list_tasks(task_list)

# Marcamos a primeira tarefa como concluida
complete_task(task_list, 1)

# Tentamos marcar uma tarefa com indice invalido
complete_task(task_list, 99)

# Listamos novamente para ver a atualizacao
print("\n=== Tarefas Atualizadas ===")
list_tasks(task_list)

# Salvamos as tarefas no arquivo
save_tasks(task_list, data_file)
```

---

## Exercício 21 — Classe Biblioteca de Livros — Nível: Avancado

**Conceitos:** classes, métodos, listas, dicionários, loops, condicionais

### Enunciado

Crie uma classe `Book` (Livro) com atributos `title` (título), `author` (autor) e `year` (ano). Crie uma classe `Library` (Biblioteca) que armazene uma lista de livros e tenha os métodos: `add_book` (adicionar livro), `search_by_author` (buscar por autor — retorna lista de livros do autor), `list_books` (listar todos os livros) e `count_books` (contar livros). Demonstre o uso com pelo menos 4 livros.

### Dicas

- A classe `Library` deve ter uma lista como atributo para armazenar os livros
- No método `search_by_author`, percorra a lista e compare o autor (ignorando maiusculas)
- Use `append()` para adicionar livros a lista interna
- Use `len()` para contar os livros

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Adicione 4 livros, busque por autor "Machado de Assis" → deve retornar apenas os livros desse autor
- **Caso de borda:** Busque por autor "Autor Inexistente" → saida: `Nenhum livro encontrado para este autor`

### Resposta Comentada

```python
# Classe que representa um livro
# "Book" = Livro
class Book:
    # Metodo construtor que inicializa os atributos do livro
    # "title" = titulo, "author" = autor, "year" = ano
    def __init__(self, title, author, year):
        # Armazenamos o titulo do livro
        self.title = title
        # Armazenamos o autor do livro
        self.author = author
        # Armazenamos o ano de publicacao
        self.year = year

# Classe que representa uma biblioteca com colecao de livros
# "Library" = Biblioteca
class Library:
    # Metodo construtor que inicializa a lista de livros
    def __init__(self):
        # Criamos uma lista vazia para armazenar os livros
        # "books" = livros
        self.books = []

    # Metodo que adiciona um livro a biblioteca
    # "add_book" = adicionar livro
    # "book" = livro (objeto da classe Book)
    def add_book(self, book):
        # Adicionamos o livro a lista
        self.books.append(book)
        # Informamos que o livro foi adicionado
        print(f"Livro adicionado: {book.title}")

    # Metodo que busca livros por autor
    # "search_by_author" = buscar por autor
    # "author_name" = nome do autor
    def search_by_author(self, author_name):
        # Criamos uma lista para armazenar os livros encontrados
        # "found_books" = livros encontrados
        found_books = []
        # Percorremos cada livro da biblioteca
        # "book" = livro
        for book in self.books:
            # Comparamos o autor (ignorando maiusculas/minusculas)
            if book.author.lower() == author_name.lower():
                # Adicionamos o livro a lista de encontrados
                found_books.append(book)
        # Retornamos a lista de livros encontrados
        return found_books

    # Metodo que lista todos os livros da biblioteca
    # "list_books" = listar livros
    def list_books(self):
        # Verificamos se a biblioteca esta vazia
        if len(self.books) == 0:
            # Nenhum livro cadastrado
            print("A biblioteca esta vazia.")
            return
        # Percorremos cada livro com indice numerado
        # "index" = indice, "book" = livro
        for index, book in enumerate(self.books, 1):
            # Exibimos os dados do livro formatados
            print(f"{index}. {book.title} — {book.author} ({book.year})")

    # Metodo que retorna a quantidade de livros
    # "count_books" = contar livros
    def count_books(self):
        # Retornamos o tamanho da lista de livros
        return len(self.books)

# Criamos uma biblioteca
# "my_library" = minha biblioteca
my_library = Library()

# Adicionamos 4 livros
my_library.add_book(Book("Dom Casmurro", "Machado de Assis", 1899))
my_library.add_book(Book("Memorias Postumas", "Machado de Assis", 1881))
my_library.add_book(Book("O Cortico", "Aluisio Azevedo", 1890))
my_library.add_book(Book("Vidas Secas", "Graciliano Ramos", 1938))

# Listamos todos os livros
print("\n=== Todos os Livros ===")
my_library.list_books()

# Exibimos a quantidade total
print(f"\nTotal de livros: {my_library.count_books()}")

# Buscamos livros de um autor especifico
# "author_search" = busca por autor
author_search = "Machado de Assis"
# "results" = resultados
results = my_library.search_by_author(author_search)

# Verificamos se encontrou livros
print(f"\n=== Livros de {author_search} ===")
if len(results) == 0:
    # Nenhum livro encontrado para este autor
    print("Nenhum livro encontrado para este autor")
else:
    # Exibimos cada livro encontrado
    for book in results:
        # Exibimos titulo e ano
        print(f"  - {book.title} ({book.year})")
```

---

## Exercício 22 — Relatório de Vendas com CSV — Nível: Avancado

**Conceitos:** funções, arquivos, listas, dicionários, loops, tratamento de erros, formatacao

### Enunciado

Crie um programa que leia um arquivo CSV chamado `vendas.csv` com as colunas `produto;quantidade;preco_unitario` e gere um relatório com: total de vendas por produto, produto mais vendido (em quantidade) e valor total geral. Implemente funções separadas para ler o arquivo, calcular estatisticas e exibir o relatório. Se o arquivo não existir, crie um arquivo de exemplo.

### Dicas

- Use `open()` com `split(";")` para ler o CSV manualmente
- Crie um dicionário para acumular vendas por produto
- Para encontrar o mais vendido, percorra o dicionário e compare quantidades
- Use `try/except` para tratar arquivo inexistente

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Arquivo com 3 linhas de vendas → relatório deve mostrar totais corretos por produto
- **Caso de borda:** Arquivo vazio (apenas cabecalho) → saida: `Nenhuma venda registrada`

### Resposta Comentada

```python
# Funcao que cria um arquivo CSV de exemplo para testes
# "create_sample_file" = criar arquivo de exemplo
# "filename" = nome do arquivo
def create_sample_file(filename):
    # Abrimos o arquivo para escrita
    # "file" = arquivo
    with open(filename, "w") as file:
        # Escrevemos o cabecalho do CSV
        file.write("produto;quantidade;preco_unitario\n")
        # Escrevemos algumas linhas de exemplo
        file.write("Arroz;10;5.99\n")
        file.write("Feijao;5;7.50\n")
        file.write("Arroz;8;5.99\n")
        file.write("Macarrao;12;4.20\n")
        file.write("Feijao;3;7.50\n")
    # Informamos que o arquivo foi criado
    print(f"Arquivo de exemplo {filename} criado.")

# Funcao que le o arquivo CSV e retorna uma lista de dicionarios
# "read_sales_file" = ler arquivo de vendas
# "filename" = nome do arquivo
def read_sales_file(filename):
    # Criamos uma lista vazia para armazenar as vendas
    # "sales" = vendas
    sales = []
    # Tentamos abrir o arquivo
    try:
        # Abrimos o arquivo para leitura
        with open(filename, "r") as file:
            # Lemos todas as linhas
            # "lines" = linhas
            lines = file.readlines()
            # Pulamos a primeira linha (cabecalho) e percorremos as demais
            # "line" = linha
            for line in lines[1:]:
                # Removemos espacos e quebras de linha
                # Separamos os campos pelo ponto e virgula
                # "parts" = partes
                parts = line.strip().split(";")
                # Verificamos se a linha tem os 3 campos esperados
                if len(parts) == 3:
                    # Criamos um dicionario com os dados da venda
                    # "sale" = venda
                    sale = {
                        "product": parts[0],
                        "quantity": int(parts[1]),
                        "unit_price": float(parts[2])
                    }
                    # Adicionamos a venda a lista
                    sales.append(sale)
    except FileNotFoundError:
        # Arquivo nao encontrado — criamos um de exemplo
        print("Arquivo nao encontrado. Criando exemplo...")
        create_sample_file(filename)
        # Chamamos a funcao novamente para ler o arquivo recem-criado
        return read_sales_file(filename)
    # Retornamos a lista de vendas
    return sales

# Funcao que calcula estatisticas das vendas
# "calculate_stats" = calcular estatisticas
# "sales" = vendas
def calculate_stats(sales):
    # Criamos um dicionario para acumular dados por produto
    # "product_stats" = estatisticas por produto
    product_stats = {}
    # Percorremos cada venda
    # "sale" = venda
    for sale in sales:
        # Pegamos o nome do produto
        # "product" = produto
        product = sale["product"]
        # Verificamos se o produto ja esta no dicionario
        if product not in product_stats:
            # Se nao esta, criamos uma entrada com valores zerados
            product_stats[product] = {"quantity": 0, "total": 0.0}
        # Somamos a quantidade vendida
        product_stats[product]["quantity"] = product_stats[product]["quantity"] + sale["quantity"]
        # Somamos o valor total (quantidade * preco unitario)
        product_stats[product]["total"] = product_stats[product]["total"] + (sale["quantity"] * sale["unit_price"])
    # Retornamos o dicionario de estatisticas
    return product_stats

# Funcao que exibe o relatorio formatado
# "show_report" = exibir relatorio
# "product_stats" = estatisticas por produto
def show_report(product_stats):
    # Verificamos se ha dados para exibir
    if len(product_stats) == 0:
        # Nenhuma venda registrada
        print("Nenhuma venda registrada")
        return
    # Exibimos o cabecalho do relatorio
    print("\n=== Relatorio de Vendas ===")
    # Variavel para acumular o valor total geral
    # "grand_total" = total geral
    grand_total = 0.0
    # Variaveis para encontrar o produto mais vendido
    # "best_product" = melhor produto, "best_quantity" = melhor quantidade
    best_product = ""
    best_quantity = 0
    # Percorremos cada produto e suas estatisticas
    # "product" = produto, "stats" = estatisticas
    for product, stats in product_stats.items():
        # Exibimos os dados do produto
        print(f"  {product}: {stats['quantity']} unidades — R$ {stats['total']:.2f}")
        # Somamos ao total geral
        grand_total = grand_total + stats["total"]
        # Verificamos se e o mais vendido
        if stats["quantity"] > best_quantity:
            # Atualizamos o mais vendido
            best_product = product
            best_quantity = stats["quantity"]
    # Exibimos o total geral e o mais vendido
    print(f"\nTotal geral: R$ {grand_total:.2f}")
    print(f"Produto mais vendido: {best_product} ({best_quantity} unidades)")

# Nome do arquivo CSV
# "csv_file" = arquivo CSV
csv_file = "vendas.csv"

# Lemos as vendas do arquivo
# "sales_data" = dados de vendas
sales_data = read_sales_file(csv_file)

# Calculamos as estatisticas
# "stats" = estatisticas
stats = calculate_stats(sales_data)

# Exibimos o relatorio
show_report(stats)
```

---

## Exercício 23 — Sistema de Notas com Classes e JSON — Nível: Avancado

**Conceitos:** classes, métodos, listas, dicionários, JSON, arquivos, loops, condicionais, tratamento de erros

### Enunciado

Crie uma classe `Student` (Aluno) com atributos `name` (nome) e `grades` (notas — uma lista). Implemente métodos: `add_grade` (adicionar nota), `average` (calcular media) e `to_dict` (converter para dicionário). Crie uma classe `Classroom` (Turma) que armazene alunos e tenha métodos para: `add_student` (adicionar aluno), `save_to_json` (salvar em JSON), `load_from_json` (carregar do JSON) e `class_report` (relatório da turma com media geral).

### Dicas

- A classe `Student` deve ter uma lista de notas como atributo
- O método `to_dict` deve retornar um dicionário com nome e notas
- A classe `Classroom` deve converter alunos para dicionários antes de salvar em JSON
- Ao carregar do JSON, recrie os objetos `Student` a partir dos dicionários

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Turma com 3 alunos, cada um com 3 notas → relatório deve mostrar media de cada aluno e media geral da turma
- **Caso de borda:** Aluno sem notas → media deve ser `0.00`

### Resposta Comentada

```python
# Importamos o modulo json para persistencia
import json

# Classe que representa um aluno
# "Student" = Aluno
class Student:
    # Metodo construtor que inicializa nome e lista de notas
    # "name" = nome
    def __init__(self, name):
        # Armazenamos o nome do aluno
        self.name = name
        # Inicializamos a lista de notas vazia
        # "grades" = notas
        self.grades = []

    # Metodo que adiciona uma nota a lista
    # "add_grade" = adicionar nota
    # "grade" = nota
    def add_grade(self, grade):
        # Adicionamos a nota a lista de notas
        self.grades.append(grade)

    # Metodo que calcula a media das notas
    # "average" = media
    def average(self):
        # Verificamos se ha notas na lista
        if len(self.grades) == 0:
            # Sem notas, a media e zero
            return 0.0
        # Calculamos a media: soma das notas dividida pela quantidade
        return sum(self.grades) / len(self.grades)

    # Metodo que converte o aluno para dicionario (para salvar em JSON)
    # "to_dict" = para dicionario
    def to_dict(self):
        # Retornamos um dicionario com nome e notas
        return {"name": self.name, "grades": self.grades}

# Classe que representa uma turma de alunos
# "Classroom" = Turma
class Classroom:
    # Metodo construtor que inicializa a lista de alunos
    def __init__(self):
        # Criamos uma lista vazia para armazenar os alunos
        # "students" = alunos
        self.students = []

    # Metodo que adiciona um aluno a turma
    # "add_student" = adicionar aluno
    # "student" = aluno (objeto da classe Student)
    def add_student(self, student):
        # Adicionamos o aluno a lista
        self.students.append(student)
        # Informamos que o aluno foi adicionado
        print(f"Aluno {student.name} adicionado a turma.")

    # Metodo que salva a turma em um arquivo JSON
    # "save_to_json" = salvar em JSON
    # "filename" = nome do arquivo
    def save_to_json(self, filename):
        # Convertemos cada aluno para dicionario
        # "data" = dados
        data = []
        # Percorremos cada aluno
        for student in self.students:
            # Convertemos para dicionario e adicionamos a lista
            data.append(student.to_dict())
        # Salvamos no arquivo JSON
        with open(filename, "w") as file:
            # Escrevemos os dados com indentacao
            json.dump(data, file, indent=4)
        # Informamos que os dados foram salvos
        print(f"Turma salva em {filename}")

    # Metodo que carrega alunos de um arquivo JSON
    # "load_from_json" = carregar do JSON
    # "filename" = nome do arquivo
    def load_from_json(self, filename):
        # Tentamos abrir o arquivo
        try:
            with open(filename, "r") as file:
                # Carregamos os dados do JSON
                data = json.load(file)
                # Percorremos cada dicionario de aluno
                for student_data in data:
                    # Criamos um objeto Student com o nome
                    student = Student(student_data["name"])
                    # Adicionamos cada nota
                    for grade in student_data["grades"]:
                        student.add_grade(grade)
                    # Adicionamos o aluno a turma
                    self.students.append(student)
            # Informamos quantos alunos foram carregados
            print(f"{len(self.students)} aluno(s) carregado(s).")
        except FileNotFoundError:
            # Arquivo nao encontrado
            print("Arquivo nao encontrado. Turma vazia.")

    # Metodo que gera o relatorio da turma
    # "class_report" = relatorio da turma
    def class_report(self):
        # Verificamos se ha alunos na turma
        if len(self.students) == 0:
            print("Turma vazia. Nenhum relatorio para gerar.")
            return
        # Exibimos o cabecalho do relatorio
        print("\n=== Relatorio da Turma ===")
        # Variavel para acumular as medias
        # "total_average" = soma das medias
        total_average = 0.0
        # Percorremos cada aluno
        for student in self.students:
            # Calculamos a media do aluno
            avg = student.average()
            # Somamos a media ao total
            total_average = total_average + avg
            # Exibimos o nome e a media do aluno
            print(f"  {student.name}: media = {avg:.2f}")
        # Calculamos a media geral da turma
        # "class_avg" = media da turma
        class_avg = total_average / len(self.students)
        # Exibimos a media geral
        print(f"\nMedia geral da turma: {class_avg:.2f}")

# Criamos uma turma
# "my_class" = minha turma
my_class = Classroom()

# Criamos alunos e adicionamos notas
# "student1" = aluno 1
student1 = Student("Ana")
student1.add_grade(8.5)
student1.add_grade(9.0)
student1.add_grade(7.5)

# "student2" = aluno 2
student2 = Student("Bruno")
student2.add_grade(6.0)
student2.add_grade(7.0)
student2.add_grade(8.0)

# "student3" = aluno 3 (sem notas — caso de borda)
student3 = Student("Carla")

# Adicionamos os alunos a turma
my_class.add_student(student1)
my_class.add_student(student2)
my_class.add_student(student3)

# Geramos o relatorio
my_class.class_report()

# Salvamos a turma em JSON
my_class.save_to_json("turma.json")
```

---

## Exercício 24 — Menu Interativo de Cadastro de Produtos — Nível: Avancado

**Conceitos:** funções, listas, dicionários, loops, condicionais, tratamento de erros, menus interativos

### Enunciado

Crie um programa com menu interativo para gerenciar um cadastro de produtos. O menu deve oferecer as opcoes: 1) Cadastrar produto, 2) Listar produtos, 3) Buscar produto por nome, 4) Remover produto, 5) Sair. Cada produto deve ter `name` (nome), `price` (preco) e `category` (categoria). Implemente validacoes: preco deve ser positivo, nome não pode ser vazio.

### Dicas

- Use `while True` para manter o menu ativo
- Crie uma função separada para cada operação
- Use `try/except` para validar a entrada de preco
- Para buscar, use `.lower()` para ignorar maiusculas

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Cadastre "Arroz", preco 5.99, categoria "Alimentos" → ao listar, o produto deve aparecer
- **Caso de borda:** Tente cadastrar com preco negativo → saida: `Erro: o preco deve ser positivo`
- **Caso de borda:** Tente cadastrar com nome vazio → saida: `Erro: o nome nao pode ser vazio`

### Resposta Comentada

```python
# Funcao que cadastra um novo produto
# "register_product" = cadastrar produto
# "products" = produtos (lista de dicionarios)
def register_product(products):
    # Pedimos o nome do produto
    # "name" = nome
    name = input("Nome do produto: ").strip()
    # Verificamos se o nome esta vazio
    if len(name) == 0:
        # Nome vazio nao e permitido
        print("Erro: o nome nao pode ser vazio")
        return
    # Pedimos o preco do produto com tratamento de erro
    try:
        # "price" = preco
        price = float(input("Preco: "))
    except ValueError:
        # O usuario digitou algo que nao e numero
        print("Erro: digite um numero valido para o preco.")
        return
    # Verificamos se o preco e positivo
    if price <= 0:
        # Preco deve ser positivo
        print("Erro: o preco deve ser positivo")
        return
    # Pedimos a categoria do produto
    # "category" = categoria
    category = input("Categoria: ").strip()
    # Criamos o dicionario do produto
    # "product" = produto
    product = {"name": name, "price": price, "category": category}
    # Adicionamos o produto a lista
    products.append(product)
    # Informamos que o produto foi cadastrado
    print(f"Produto '{name}' cadastrado com sucesso!")

# Funcao que lista todos os produtos
# "list_products" = listar produtos
# "products" = produtos
def list_products(products):
    # Verificamos se a lista esta vazia
    if len(products) == 0:
        # Nenhum produto cadastrado
        print("Nenhum produto cadastrado.")
        return
    # Exibimos o cabecalho
    print("\n=== Produtos Cadastrados ===")
    # Percorremos cada produto com indice
    # "index" = indice, "product" = produto
    for index, product in enumerate(products, 1):
        # Exibimos os dados do produto formatados
        print(f"{index}. {product['name']} | R$ {product['price']:.2f} | {product['category']}")

# Funcao que busca um produto pelo nome
# "search_product" = buscar produto
# "products" = produtos
def search_product(products):
    # Pedimos o nome para busca
    # "search_name" = nome buscado
    search_name = input("Digite o nome para buscar: ").strip().lower()
    # Variavel para controlar se encontrou algum produto
    # "found" = encontrado
    found = False
    # Percorremos cada produto
    # "product" = produto
    for product in products:
        # Comparamos o nome (ignorando maiusculas)
        if search_name in product["name"].lower():
            # Encontramos um produto correspondente
            print(f"  {product['name']} | R$ {product['price']:.2f} | {product['category']}")
            # Marcamos que encontramos
            found = True
    # Se nao encontrou nenhum produto
    if not found:
        print("Nenhum produto encontrado com esse nome.")

# Funcao que remove um produto pelo indice
# "remove_product" = remover produto
# "products" = produtos
def remove_product(products):
    # Verificamos se ha produtos para remover
    if len(products) == 0:
        print("Nenhum produto para remover.")
        return
    # Listamos os produtos para o usuario escolher
    list_products(products)
    # Pedimos o numero do produto a remover
    try:
        # "choice" = escolha
        choice = int(input("Digite o numero do produto para remover: "))
    except ValueError:
        # O usuario digitou algo que nao e numero
        print("Erro: digite um numero valido.")
        return
    # Verificamos se o numero e valido
    if choice < 1 or choice > len(products):
        # Numero fora do intervalo
        print("Numero invalido.")
        return
    # Removemos o produto (ajustamos o indice para base 0)
    # "removed" = removido
    removed = products.pop(choice - 1)
    # Informamos qual produto foi removido
    print(f"Produto '{removed['name']}' removido com sucesso!")

# Lista para armazenar os produtos
# "product_list" = lista de produtos
product_list = []

# Loop principal do menu
while True:
    # Exibimos o menu de opcoes
    print("\n=== Cadastro de Produtos ===")
    print("1. Cadastrar produto")
    print("2. Listar produtos")
    print("3. Buscar produto")
    print("4. Remover produto")
    print("5. Sair")
    # Pedimos a opcao ao usuario
    # "option" = opcao
    option = input("Escolha uma opcao: ")
    # Verificamos qual opcao foi escolhida
    if option == "1":
        # Opcao 1: Cadastrar
        register_product(product_list)
    elif option == "2":
        # Opcao 2: Listar
        list_products(product_list)
    elif option == "3":
        # Opcao 3: Buscar
        search_product(product_list)
    elif option == "4":
        # Opcao 4: Remover
        remove_product(product_list)
    elif option == "5":
        # Opcao 5: Sair do programa
        print("Ate logo!")
        break
    else:
        # Opcao invalida
        print("Opcao invalida. Escolha de 1 a 5.")
```

---

## Exercício 25 — Sistema Completo de Biblioteca com Persistência — Nível: Avancado

**Conceitos:** classes, métodos, listas, dicionários, JSON, arquivos, loops, condicionais, tratamento de erros, menus interativos

### Enunciado

Crie um sistema completo de biblioteca que combine classes, persistência em JSON e menu interativo. O sistema deve ter: classe `Book` (Livro) com `title` (título), `author` (autor), `year` (ano) e `available` (disponível — True/False). Classe `Library` (Biblioteca) com métodos para: adicionar livro, listar livros, emprestar livro (muda `available` para False), devolver livro (muda `available` para True), salvar em JSON e carregar do JSON. O programa deve ter um menu interativo com todas as opcoes.

### Dicas

- Use `available` como booleano para controlar emprestimos
- Ao emprestar, verifique se o livro esta disponível
- Ao devolver, verifique se o livro esta emprestado
- Salve e carregue os dados automaticamente a cada operação

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Adicione um livro, empreste-o, liste → deve aparecer como "Emprestado"
- **Caso de borda:** Tente emprestar um livro ja emprestado → saida: `Este livro ja esta emprestado`
- **Caso de borda:** Feche e reabra o programa → os livros devem ser carregados do arquivo JSON

### Resposta Comentada

```python
# Importamos o modulo json para persistencia de dados
import json

# Classe que representa um livro
# "Book" = Livro
class Book:
    # Metodo construtor que inicializa os atributos do livro
    # "title" = titulo, "author" = autor, "year" = ano
    def __init__(self, title, author, year):
        # Armazenamos o titulo do livro
        self.title = title
        # Armazenamos o autor do livro
        self.author = author
        # Armazenamos o ano de publicacao
        self.year = year
        # Inicializamos como disponivel (nao emprestado)
        # "available" = disponivel
        self.available = True

    # Metodo que converte o livro para dicionario
    # "to_dict" = para dicionario
    def to_dict(self):
        # Retornamos um dicionario com todos os atributos
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available
        }

# Classe que representa a biblioteca
# "Library" = Biblioteca
class Library:
    # Metodo construtor que inicializa a lista de livros e o arquivo
    # "filename" = nome do arquivo
    def __init__(self, filename):
        # Armazenamos o nome do arquivo para persistencia
        self.filename = filename
        # Inicializamos a lista de livros vazia
        # "books" = livros
        self.books = []
        # Carregamos os livros do arquivo ao iniciar
        self.load_from_json()

    # Metodo que adiciona um livro a biblioteca
    # "add_book" = adicionar livro
    # "title" = titulo, "author" = autor, "year" = ano
    def add_book(self, title, author, year):
        # Criamos um novo objeto Book
        # "book" = livro
        book = Book(title, author, year)
        # Adicionamos o livro a lista
        self.books.append(book)
        # Salvamos os dados no arquivo
        self.save_to_json()
        # Informamos que o livro foi adicionado
        print(f"Livro '{title}' adicionado com sucesso!")

    # Metodo que lista todos os livros
    # "list_books" = listar livros
    def list_books(self):
        # Verificamos se a biblioteca esta vazia
        if len(self.books) == 0:
            print("A biblioteca esta vazia.")
            return
        # Exibimos o cabecalho
        print("\n=== Acervo da Biblioteca ===")
        # Percorremos cada livro com indice
        # "index" = indice, "book" = livro
        for index, book in enumerate(self.books, 1):
            # Definimos o status de disponibilidade
            # "status" = status
            status = "Disponivel" if book.available else "Emprestado"
            # Exibimos os dados do livro
            print(f"{index}. {book.title} — {book.author} ({book.year}) [{status}]")

    # Metodo que empresta um livro pelo indice
    # "lend_book" = emprestar livro
    # "book_index" = indice do livro (comecando em 1)
    def lend_book(self, book_index):
        # Verificamos se o indice e valido
        if book_index < 1 or book_index > len(self.books):
            print("Livro nao encontrado.")
            return
        # Pegamos o livro pelo indice (ajustamos para base 0)
        # "book" = livro
        book = self.books[book_index - 1]
        # Verificamos se o livro esta disponivel
        if not book.available:
            # O livro ja esta emprestado
            print("Este livro ja esta emprestado")
            return
        # Marcamos o livro como emprestado
        book.available = False
        # Salvamos os dados atualizados
        self.save_to_json()
        # Informamos o emprestimo
        print(f"Livro '{book.title}' emprestado com sucesso!")

    # Metodo que devolve um livro pelo indice
    # "return_book" = devolver livro
    # "book_index" = indice do livro
    def return_book(self, book_index):
        # Verificamos se o indice e valido
        if book_index < 1 or book_index > len(self.books):
            print("Livro nao encontrado.")
            return
        # Pegamos o livro pelo indice
        book = self.books[book_index - 1]
        # Verificamos se o livro esta emprestado
        if book.available:
            # O livro ja esta disponivel, nao precisa devolver
            print("Este livro ja esta disponivel.")
            return
        # Marcamos o livro como disponivel
        book.available = True
        # Salvamos os dados atualizados
        self.save_to_json()
        # Informamos a devolucao
        print(f"Livro '{book.title}' devolvido com sucesso!")

    # Metodo que salva os livros em arquivo JSON
    # "save_to_json" = salvar em JSON
    def save_to_json(self):
        # Convertemos cada livro para dicionario
        # "data" = dados
        data = []
        for book in self.books:
            data.append(book.to_dict())
        # Salvamos no arquivo
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Metodo que carrega livros do arquivo JSON
    # "load_from_json" = carregar do JSON
    def load_from_json(self):
        # Tentamos abrir o arquivo
        try:
            with open(self.filename, "r") as file:
                # Carregamos os dados
                data = json.load(file)
                # Recriamos os objetos Book a partir dos dicionarios
                for book_data in data:
                    # Criamos o objeto Book
                    book = Book(book_data["title"], book_data["author"], book_data["year"])
                    # Restauramos o status de disponibilidade
                    book.available = book_data["available"]
                    # Adicionamos a lista
                    self.books.append(book)
                # Informamos quantos livros foram carregados
                print(f"{len(self.books)} livro(s) carregado(s).")
        except FileNotFoundError:
            # Arquivo nao existe — biblioteca vazia
            print("Iniciando biblioteca vazia.")

# Criamos a biblioteca com o arquivo de persistencia
# "my_library" = minha biblioteca
my_library = Library("biblioteca.json")

# Loop principal do menu
while True:
    # Exibimos o menu
    print("\n=== Biblioteca ===")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Sair")
    # Pedimos a opcao
    # "option" = opcao
    option = input("Escolha uma opcao: ")
    # Verificamos a opcao escolhida
    if option == "1":
        # Opcao 1: Adicionar livro
        # Pedimos os dados do livro
        title = input("Titulo: ")
        author = input("Autor: ")
        try:
            year = int(input("Ano: "))
        except ValueError:
            print("Erro: digite um ano valido.")
            continue
        # Adicionamos o livro
        my_library.add_book(title, author, year)
    elif option == "2":
        # Opcao 2: Listar livros
        my_library.list_books()
    elif option == "3":
        # Opcao 3: Emprestar livro
        my_library.list_books()
        try:
            # Pedimos o numero do livro
            num = int(input("Numero do livro para emprestar: "))
            my_library.lend_book(num)
        except ValueError:
            print("Erro: digite um numero valido.")
    elif option == "4":
        # Opcao 4: Devolver livro
        my_library.list_books()
        try:
            # Pedimos o numero do livro
            num = int(input("Numero do livro para devolver: "))
            my_library.return_book(num)
        except ValueError:
            print("Erro: digite um numero valido.")
    elif option == "5":
        # Opcao 5: Sair
        print("Ate logo!")
        break
    else:
        # Opcao invalida
        print("Opcao invalida. Escolha de 1 a 5.")
```

---

## Exercício 26 — Jogo de Forca Simplificado — Nível: Avancado

**Conceitos:** funções, strings, listas, conjuntos, loops, condicionais

### Enunciado

Crie um jogo de forca simplificado. O programa deve ter uma palavra secreta definida no código. O jogador tem 6 tentativas para adivinhar as letras. A cada tentativa, o programa exibe a palavra com as letras acertadas e underscores para as não descobertas. Implemente funções para: `display_word` (exibir palavra com lacunas), `check_letter` (verificar letra) e `play_game` (jogar).

### Dicas

- Use um conjunto (`set`) para armazenar as letras ja tentadas
- Use outro conjunto para as letras corretas
- Na função `display_word`, percorra cada letra da palavra e exiba a letra ou `_`
- Use `.lower()` para tratar maiusculas e minusculas

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Palavra "python", letras `p, y, t, h, o, n` → saida: `Parabens! Voce acertou: python`
- **Caso de borda:** Palavra "python", 6 letras erradas `a, b, c, d, e, f` → saida: `Voce perdeu! A palavra era: python`

### Resposta Comentada

```python
# Funcao que exibe a palavra com lacunas para letras nao descobertas
# "display_word" = exibir palavra
# "word" = palavra, "guessed_letters" = letras adivinhadas
def display_word(word, guessed_letters):
    # Criamos uma string vazia para montar a exibicao
    # "display" = exibicao
    display = ""
    # Percorremos cada letra da palavra
    # "letter" = letra
    for letter in word:
        # Verificamos se a letra ja foi adivinhada
        if letter in guessed_letters:
            # Letra adivinhada — exibimos a letra
            display = display + letter + " "
        else:
            # Letra nao adivinhada — exibimos underscore
            display = display + "_ "
    # Retornamos a string de exibicao
    return display.strip()

# Funcao que verifica se uma letra esta na palavra
# "check_letter" = verificar letra
# "word" = palavra, "letter" = letra, "guessed_letters" = letras adivinhadas
def check_letter(word, letter, guessed_letters):
    # Adicionamos a letra ao conjunto de tentativas
    guessed_letters.add(letter)
    # Verificamos se a letra esta na palavra
    if letter in word:
        # Letra correta
        print(f"Boa! A letra '{letter}' esta na palavra!")
        # Retornamos True indicando acerto
        return True
    else:
        # Letra incorreta
        print(f"A letra '{letter}' nao esta na palavra.")
        # Retornamos False indicando erro
        return False

# Funcao principal que executa o jogo
# "play_game" = jogar
def play_game():
    # Definimos a palavra secreta
    # "secret_word" = palavra secreta
    secret_word = "python"
    # Definimos o maximo de erros permitidos
    # "max_errors" = maximo de erros
    max_errors = 6
    # Contador de erros
    # "errors" = erros
    errors = 0
    # Conjunto para armazenar todas as letras tentadas
    # "guessed_letters" = letras adivinhadas
    guessed_letters = set()
    # Conjunto com as letras unicas da palavra (para verificar vitoria)
    # "word_letters" = letras da palavra
    word_letters = set(secret_word)
    # Exibimos as instrucoes
    print("=== Jogo da Forca ===")
    print(f"A palavra tem {len(secret_word)} letras.")
    print(f"Voce tem {max_errors} tentativas.\n")
    # Loop principal do jogo
    while errors < max_errors:
        # Exibimos a palavra com lacunas
        print(f"Palavra: {display_word(secret_word, guessed_letters)}")
        print(f"Tentativas restantes: {max_errors - errors}")
        # Pedimos uma letra ao jogador
        # "letter" = letra
        letter = input("Digite uma letra: ").lower().strip()
        # Verificamos se o jogador digitou apenas uma letra
        if len(letter) != 1 or not letter.isalpha():
            # Entrada invalida
            print("Digite apenas uma letra.")
            continue
        # Verificamos se a letra ja foi tentada
        if letter in guessed_letters:
            # Letra ja tentada
            print("Voce ja tentou essa letra. Tente outra.")
            continue
        # Verificamos a letra
        if not check_letter(secret_word, letter, guessed_letters):
            # Letra errada — incrementamos os erros
            errors = errors + 1
        # Verificamos se o jogador acertou todas as letras
        # Comparamos as letras adivinhadas com as letras da palavra
        if word_letters.issubset(guessed_letters):
            # Todas as letras foram descobertas
            print(f"\nParabens! Voce acertou: {secret_word}")
            return
    # Se saiu do loop, o jogador perdeu
    print(f"\nVoce perdeu! A palavra era: {secret_word}")

# Iniciamos o jogo
play_game()
```

---

## Exercício 27 — Conversor de Moedas com Dicionário de Taxas — Nível: Avancado

**Conceitos:** funções, dicionários, loops, condicionais, tratamento de erros, formatacao

### Enunciado

Crie um conversor de moedas que use um dicionário com taxas de cambio fixas em relação ao Real (BRL). O dicionário deve conter pelo menos 4 moedas: USD (dolar), EUR (euro), GBP (libra) e JPY (iene). Implemente funções para: `convert_from_brl` (converter de Real para outra moeda), `convert_to_brl` (converter de outra moeda para Real) e `list_rates` (listar taxas disponiveis). O programa deve ter um menu interativo.

### Dicas

- Crie um dicionário onde a chave e o código da moeda e o valor e a taxa de cambio
- Para converter de BRL: `valor_brl / taxa`
- Para converter para BRL: `valor_moeda * taxa`
- Use `in` para verificar se a moeda existe no dicionário

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Converter R$ 500.00 para USD (taxa 5.00) → saida: `100.00 USD`
- **Caso de borda:** Tentar converter para moeda inexistente "ABC" → saida: `Moeda nao encontrada`

### Resposta Comentada

```python
# Funcao que lista todas as taxas de cambio disponiveis
# "list_rates" = listar taxas
# "rates" = taxas de cambio
def list_rates(rates):
    # Exibimos o cabecalho
    print("\n=== Taxas de Cambio (em relacao ao Real) ===")
    # Percorremos cada moeda e sua taxa
    # "currency" = moeda, "rate" = taxa
    for currency, rate in rates.items():
        # Exibimos a moeda e a taxa formatada
        print(f"  {currency}: R$ {rate:.2f}")

# Funcao que converte de Real para outra moeda
# "convert_from_brl" = converter de BRL (Real)
# "amount_brl" = valor em reais, "currency" = moeda destino, "rates" = taxas
def convert_from_brl(amount_brl, currency, rates):
    # Convertemos o codigo da moeda para maiusculas
    # "currency_upper" = moeda em maiusculas
    currency_upper = currency.upper()
    # Verificamos se a moeda existe no dicionario
    if currency_upper not in rates:
        # Moeda nao encontrada
        print("Moeda nao encontrada")
        return None
    # Calculamos o valor na moeda destino
    # "result" = resultado
    result = amount_brl / rates[currency_upper]
    # Retornamos o valor convertido
    return result

# Funcao que converte de outra moeda para Real
# "convert_to_brl" = converter para BRL (Real)
# "amount" = valor na moeda de origem, "currency" = moeda de origem, "rates" = taxas
def convert_to_brl(amount, currency, rates):
    # Convertemos o codigo da moeda para maiusculas
    currency_upper = currency.upper()
    # Verificamos se a moeda existe no dicionario
    if currency_upper not in rates:
        # Moeda nao encontrada
        print("Moeda nao encontrada")
        return None
    # Calculamos o valor em reais
    # "result" = resultado
    result = amount * rates[currency_upper]
    # Retornamos o valor convertido
    return result

# Dicionario com taxas de cambio fixas (valor de 1 unidade em Reais)
# "exchange_rates" = taxas de cambio
exchange_rates = {
    "USD": 5.00,
    "EUR": 5.50,
    "GBP": 6.30,
    "JPY": 0.034
}

# Loop principal do menu
while True:
    # Exibimos o menu
    print("\n=== Conversor de Moedas ===")
    print("1. Ver taxas de cambio")
    print("2. Converter de Real para outra moeda")
    print("3. Converter de outra moeda para Real")
    print("4. Sair")
    # Pedimos a opcao
    # "option" = opcao
    option = input("Escolha uma opcao: ")
    # Verificamos a opcao
    if option == "1":
        # Opcao 1: Listar taxas
        list_rates(exchange_rates)
    elif option == "2":
        # Opcao 2: Converter de BRL
        try:
            # Pedimos o valor em reais
            # "value" = valor
            value = float(input("Valor em Reais: R$ "))
            # Pedimos a moeda destino
            # "target" = destino
            target = input("Moeda destino (ex: USD, EUR): ")
            # Convertemos
            result = convert_from_brl(value, target, exchange_rates)
            # Exibimos o resultado se a conversao foi bem-sucedida
            if result is not None:
                print(f"R$ {value:.2f} = {result:.2f} {target.upper()}")
        except ValueError:
            # Valor invalido
            print("Erro: digite um numero valido.")
    elif option == "3":
        # Opcao 3: Converter para BRL
        try:
            # Pedimos a moeda de origem
            # "source" = origem
            source = input("Moeda de origem (ex: USD, EUR): ")
            # Pedimos o valor
            value = float(input(f"Valor em {source.upper()}: "))
            # Convertemos
            result = convert_to_brl(value, source, exchange_rates)
            # Exibimos o resultado se a conversao foi bem-sucedida
            if result is not None:
                print(f"{value:.2f} {source.upper()} = R$ {result:.2f}")
        except ValueError:
            # Valor invalido
            print("Erro: digite um numero valido.")
    elif option == "4":
        # Opcao 4: Sair
        print("Ate logo!")
        break
    else:
        # Opcao invalida
        print("Opcao invalida. Escolha de 1 a 4.")
```

---

## Exercício 28 — Mini Sistema de Enquetes com Persistência — Nível: Avancado

**Conceitos:** classes, métodos, listas, dicionários, JSON, arquivos, loops, condicionais, tratamento de erros, conjuntos, menus interativos

### Enunciado

Crie um sistema de enquetes que permita criar enquetes com opcoes, votar e ver resultados. Cada enquete deve ter `question` (pergunta), `options` (opcoes — lista de strings) e `votes` (votos — dicionário onde a chave e a opcao e o valor e a quantidade de votos). Implemente uma classe `Poll` (Enquete) e uma classe `PollManager` (Gerenciador de Enquetes) com persistência em JSON. O programa deve ter menu interativo com opcoes para: criar enquete, listar enquetes, votar e ver resultados.

### Dicas

- A classe `Poll` deve ter métodos `vote` (votar) e `results` (resultados)
- A classe `PollManager` deve gerenciar uma lista de enquetes
- Inicialize o dicionário de votos com cada opcao tendo 0 votos
- Use `json.dump()` e `json.load()` para persistência

### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Crie enquete "Melhor linguagem?" com opcoes "Python", "Java", "JavaScript", vote 3 vezes em "Python" → resultados devem mostrar `Python: 3 votos`
- **Caso de borda:** Tente votar em opcao inexistente → saida: `Opcao invalida`

### Resposta Comentada

```python
# Importamos o modulo json para persistencia
import json

# Classe que representa uma enquete
# "Poll" = Enquete
class Poll:
    # Metodo construtor que inicializa a enquete
    # "question" = pergunta, "options" = opcoes
    def __init__(self, question, options):
        # Armazenamos a pergunta da enquete
        self.question = question
        # Armazenamos a lista de opcoes
        self.options = options
        # Inicializamos o dicionario de votos com zero para cada opcao
        # "votes" = votos
        self.votes = {}
        # Percorremos cada opcao para inicializar com zero votos
        for option in options:
            self.votes[option] = 0

    # Metodo que registra um voto em uma opcao
    # "vote" = votar
    # "option" = opcao escolhida
    def vote(self, option):
        # Verificamos se a opcao existe
        if option not in self.votes:
            # Opcao invalida
            print("Opcao invalida")
            return False
        # Incrementamos o voto da opcao
        self.votes[option] = self.votes[option] + 1
        # Informamos que o voto foi registrado
        print(f"Voto registrado em '{option}'!")
        return True

    # Metodo que exibe os resultados da enquete
    # "results" = resultados
    def results(self):
        # Exibimos a pergunta
        print(f"\nResultados: {self.question}")
        # Calculamos o total de votos
        # "total" = total
        total = sum(self.votes.values())
        # Percorremos cada opcao e seus votos
        # "option" = opcao, "count" = contagem
        for option, count in self.votes.items():
            # Calculamos a porcentagem (evitando divisao por zero)
            # "percentage" = porcentagem
            percentage = (count / total * 100) if total > 0 else 0
            # Exibimos a opcao, votos e porcentagem
            print(f"  {option}: {count} votos ({percentage:.1f}%)")
        # Exibimos o total de votos
        print(f"  Total de votos: {total}")

    # Metodo que converte a enquete para dicionario
    # "to_dict" = para dicionario
    def to_dict(self):
        # Retornamos um dicionario com todos os dados
        return {
            "question": self.question,
            "options": self.options,
            "votes": self.votes
        }

# Classe que gerencia multiplas enquetes
# "PollManager" = Gerenciador de Enquetes
class PollManager:
    # Metodo construtor
    # "filename" = nome do arquivo
    def __init__(self, filename):
        # Armazenamos o nome do arquivo
        self.filename = filename
        # Inicializamos a lista de enquetes
        # "polls" = enquetes
        self.polls = []
        # Carregamos enquetes existentes
        self.load_from_json()

    # Metodo que cria uma nova enquete
    # "create_poll" = criar enquete
    # "question" = pergunta, "options" = opcoes
    def create_poll(self, question, options):
        # Criamos um novo objeto Poll
        # "poll" = enquete
        poll = Poll(question, options)
        # Adicionamos a lista
        self.polls.append(poll)
        # Salvamos no arquivo
        self.save_to_json()
        # Informamos que a enquete foi criada
        print(f"Enquete criada: {question}")

    # Metodo que lista todas as enquetes
    # "list_polls" = listar enquetes
    def list_polls(self):
        # Verificamos se ha enquetes
        if len(self.polls) == 0:
            print("Nenhuma enquete cadastrada.")
            return
        # Exibimos cada enquete com indice
        print("\n=== Enquetes ===")
        # "index" = indice, "poll" = enquete
        for index, poll in enumerate(self.polls, 1):
            # Calculamos o total de votos
            total = sum(poll.votes.values())
            # Exibimos a enquete
            print(f"{index}. {poll.question} ({total} votos)")

    # Metodo que salva as enquetes em JSON
    # "save_to_json" = salvar em JSON
    def save_to_json(self):
        # Convertemos cada enquete para dicionario
        data = []
        for poll in self.polls:
            data.append(poll.to_dict())
        # Salvamos no arquivo
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Metodo que carrega enquetes do JSON
    # "load_from_json" = carregar do JSON
    def load_from_json(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                for poll_data in data:
                    # Recriamos o objeto Poll
                    poll = Poll(poll_data["question"], poll_data["options"])
                    # Restauramos os votos
                    poll.votes = poll_data["votes"]
                    # Adicionamos a lista
                    self.polls.append(poll)
                print(f"{len(self.polls)} enquete(s) carregada(s).")
        except FileNotFoundError:
            print("Iniciando sem enquetes.")

# Criamos o gerenciador de enquetes
# "manager" = gerenciador
manager = PollManager("enquetes.json")

# Loop principal do menu
while True:
    # Exibimos o menu
    print("\n=== Sistema de Enquetes ===")
    print("1. Criar enquete")
    print("2. Listar enquetes")
    print("3. Votar")
    print("4. Ver resultados")
    print("5. Sair")
    # Pedimos a opcao
    option = input("Escolha uma opcao: ")
    if option == "1":
        # Opcao 1: Criar enquete
        # Pedimos a pergunta
        question = input("Pergunta da enquete: ")
        # Pedimos as opcoes separadas por virgula
        options_input = input("Opcoes (separadas por virgula): ")
        # Separamos as opcoes e removemos espacos
        options_list = [opt.strip() for opt in options_input.split(",")]
        # Verificamos se ha pelo menos 2 opcoes
        if len(options_list) < 2:
            print("A enquete precisa de pelo menos 2 opcoes.")
            continue
        # Criamos a enquete
        manager.create_poll(question, options_list)
    elif option == "2":
        # Opcao 2: Listar enquetes
        manager.list_polls()
    elif option == "3":
        # Opcao 3: Votar
        manager.list_polls()
        if len(manager.polls) == 0:
            continue
        try:
            # Pedimos o numero da enquete
            poll_num = int(input("Numero da enquete: "))
            if poll_num < 1 or poll_num > len(manager.polls):
                print("Enquete nao encontrada.")
                continue
            # Pegamos a enquete escolhida
            chosen_poll = manager.polls[poll_num - 1]
            # Exibimos as opcoes
            print(f"\n{chosen_poll.question}")
            for i, opt in enumerate(chosen_poll.options, 1):
                print(f"  {i}. {opt}")
            # Pedimos o numero da opcao
            opt_num = int(input("Numero da opcao: "))
            if opt_num < 1 or opt_num > len(chosen_poll.options):
                print("Opcao invalida")
                continue
            # Registramos o voto
            chosen_poll.vote(chosen_poll.options[opt_num - 1])
            # Salvamos
            manager.save_to_json()
        except ValueError:
            print("Erro: digite um numero valido.")
    elif option == "4":
        # Opcao 4: Ver resultados
        manager.list_polls()
        if len(manager.polls) == 0:
            continue
        try:
            poll_num = int(input("Numero da enquete: "))
            if poll_num < 1 or poll_num > len(manager.polls):
                print("Enquete nao encontrada.")
                continue
            # Exibimos os resultados
            manager.polls[poll_num - 1].results()
        except ValueError:
            print("Erro: digite um numero valido.")
    elif option == "5":
        # Opcao 5: Sair
        print("Ate logo!")
        break
    else:
        print("Opcao invalida. Escolha de 1 a 5.")
```

---

## Para Saber Mais

- [W3Schools — Exercícios de Python](https://www.w3schools.com/python/python_exercises.asp)
  _Exercicios interativos organizados por tópico, otimos para praticar além deste modulo_
- [W3Schools — Python Tutorial](https://www.w3schools.com/python/)
  _Tutorial completo de Python com exemplos interativos que você pode executar no navegador_
- [Documentação Oficial Python — Tutorial](https://docs.python.org/pt-br/3/tutorial/)
  _Tutorial oficial do Python em portugues, com explicacoes detalhadas de cada conceito_
- [Documentação Oficial Python — Estruturas de Dados](https://docs.python.org/pt-br/3/tutorial/datastructures.html)
  _Referencia completa sobre listas, dicionários, tuplas e conjuntos_
- [Documentação Oficial Python — Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)
  _Referencia sobre classes e orientacao a objetos em Python_
- [Documentação Oficial Python — Módulo json](https://docs.python.org/pt-br/3/library/json.html)
  _Referencia completa sobre leitura e escrita de dados JSON_
- [W3Schools — Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
  _Tutorial sobre leitura e escrita de arquivos em Python_

> Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Perguntas Frequentes (FAQ)

**P: E normal não conseguir resolver os exercícios avancados de primeira?**
R: Sim, completamente normal. Os exercícios avancados combinam muitos conceitos ao mesmo tempo, e isso exige prática. Volte aos módulos anteriores, releia as explicacoes e tente novamente. Cada tentativa, mesmo que não resulte em sucesso imediato, fortalece seu raciocinio logico.

**P: Preciso resolver todos os 28 exercícios para avancar?**
R: O ideal e resolver pelo menos os exercícios básicos e intermediarios antes de avancar. Os exercícios avancados sao um desafio extra que você pode revisitar depois. O importante e que você se sinta confortavel combinando os conceitos fundamentais.

**P: Posso resolver os exercícios em uma ordem diferente?**
R: Sim, você pode. Porém, a ordem sugerida (básico, intermediario, avancado) foi pensada para que cada exercício prepare você para o próximo. Se pular direto para os avancados e sentir dificuldade, volte para os mais simples.

**P: Meu código funciona mas e diferente da resposta comentada. Isso e um problema?**
R: Não. Em programação, existem muitas formas de resolver o mesmo problema. Se seu código produz a saida correta para todos os casos de teste, ele esta correto. A resposta comentada e apenas uma das possiveis soluções.

**P: O que fazer quando meu programa da erro e eu não entendo a mensagem?**
R: Primeiro, leia a mensagem de erro com calma — ela geralmente indica a linha do problema e o tipo de erro. Consulte o módulo 17 (Debugging) para aprender a interpretar mensagens de erro. Se ainda tiver duvida, copie a mensagem de erro e pesquise na internet — e muito provavel que alguem ja tenha tido o mesmo problema.

**P: Por que os nomes das variáveis e funções estão em ingles?**
R: Essa e uma convencao profissional de desenvolvimento de software. A grande maioria dos projetos reais usa nomes em ingles no código. Nos usamos comentários em portugues para traduzir e explicar cada termo, assim você aprende o significado enquanto se acostuma com o padrão da industria.

**P: Preciso decorar todos os métodos de listas, dicionários e strings?**
R: Não. Programadores profissionais consultam a documentação o tempo todo. O importante e saber que esses métodos existem e onde encontra-los. Com a prática, os mais usados (como `append`, `split`, `lower`) ficam naturais.

**P: Qual a diferença entre usar funções e usar classes?**
R: Funções sao blocos de código reutilizaveis que realizam uma tarefa específica. Classes agrupam dados (atributos) e funções (métodos) que trabalham juntos. Pense assim: uma função e como uma ferramenta individual (um martelo), enquanto uma classe e como uma caixa de ferramentas completa (com martelo, chave de fenda e alicate organizados juntos).

**P: Por que alguns exercícios usam JSON e outros usam arquivos de texto?**
R: Arquivos de texto simples (.txt) sao mais faceis de entender e funcionam bem para dados simples. JSON e melhor para dados estruturados (como listas de dicionários) porque preserva a estrutura dos dados automaticamente. Na prática, JSON e mais usado em aplicações modernas.

**P: O que significa "caso de borda" na proposta de teste?**
R: Um caso de borda (ou "edge case" em ingles) e uma situacao limite ou incomum que pode causar problemas no programa. Por exemplo: uma lista vazia, um número negativo, ou um texto sem caracteres. Testar esses casos garante que seu programa funciona em todas as situacoes, não apenas nas mais comuns.

**P: E normal meu programa funcionar para o caso básico mas falhar no caso de borda?**
R: Sim, isso e muito comum e faz parte do aprendizado. Os casos de borda revelam situacoes que você não pensou inicialmente. Quando isso acontece, análise por que falhou e adicione uma verificacao no seu código. Isso e exatamente o que programadores profissionais fazem.

**P: Posso usar funções que não foram ensinadas nos módulos anteriores?**
R: Nos exercícios integradores, o ideal e usar apenas os conceitos ja aprendidos. Se você conhece uma função ou técnica que não foi ensinada, pode usa-la, mas tente também resolver usando apenas o que foi ensinado — isso fortalece sua base.

**P: Como sei se meu código esta "bom o suficiente"?**
R: Se seu código: (1) produz a saida correta para todos os casos de teste, (2) e legivel (você consegue entender o que faz ao reler), e (3) trata os casos de borda — então esta bom. Com o tempo, você aprendera a escrever código mais elegante e eficiente, mas funcionar corretamente e o mais importante.

**P: O que e `self` que aparece em todos os métodos das classes?**
R: O `self` e uma referência ao proprio objeto. Quando você cria um método dentro de uma classe, o `self` permite que o método acesse os atributos e outros métodos daquele objeto específico. Pense no `self` como "eu mesmo" — quando o objeto diz `self.name`, ele esta dizendo "o meu nome".

**P: Por que usamos `with open()` em vez de apenas `open()`?**
R: O `with` e um gerenciador de contexto que garante que o arquivo sera fechado automaticamente, mesmo se ocorrer um erro durante a leitura ou escrita. Sem o `with`, você precisaria lembrar de chamar `file.close()` manualmente, e se esquecesse, o arquivo poderia ficar aberto e causar problemas.

**P: Qual a diferença entre `return` e `print` dentro de uma função?**
R: O `print()` exibe um valor na tela para o usuario ver, mas a função não "entrega" esse valor para quem a chamou. O `return` entrega o valor de volta para quem chamou a função, permitindo que esse valor seja armazenado em uma variável ou usado em outra operação. Pense assim: `print` e como falar em voz alta, `return` e como entregar um papel com a resposta.

**P: Por que alguns exercícios pedem para criar o arquivo de exemplo se ele não existir?**
R: Isso simula uma situacao real de programação. Quando você cria um programa que depende de um arquivo, precisa considerar que o arquivo pode não existir na primeira execução. Tratar essa situacao com `try/except` e criar o arquivo automaticamente torna seu programa mais robusto e amigavel.

**P: O que significa "persistência de dados"?**
R: Persistência significa que os dados continuam existindo mesmo depois que o programa e fechado. Quando você salva dados em um arquivo (texto, CSV ou JSON), eles ficam "persistidos" no disco. Sem persistência, os dados existem apenas na memória do computador e desaparecem quando o programa termina — como escrever na areia versus escrever em um caderno.

**P: Posso combinar os exercícios para criar um programa maior?**
R: Com certeza! Essa e uma otima forma de praticar. Por exemplo, você pode combinar o cadastro de produtos (exercício 24) com a persistência em JSON (exercício 18) e adicionar um relatório (exercício 22). Combinar exercícios e exatamente o que programadores fazem ao construir sistemas reais.

**P: Estou demorando muito para resolver cada exercício. Isso e normal?**
R: Sim, especialmente no inicio. Programar e uma habilidade que se desenvolve com prática, como aprender a tocar um instrumento musical. Não se compare com outros — cada pessoa tem seu proprio ritmo. O importante e não desistir e celebrar cada exercício que você consegue resolver.

**P: O que fazer se eu travar em um exercício e não conseguir avancar?**
R: Primeiro, releia o enunciado com calma e verifique as dicas. Depois, tente resolver uma parte menor do problema (por exemplo, so a função principal). Se ainda travar, consulte a resposta comentada para entender a lógica, feche a resposta e tente resolver sozinho novamente. Aprender com a resposta não e trapaca — e uma estrategia de estudo valida.

---

[<- Anterior: Classes e Objetos](22-classes-objetos.md) | [Glossário](00-glossário.md) | [Próximo: Módulos e Imports ->](24-módulos-imports.md)
