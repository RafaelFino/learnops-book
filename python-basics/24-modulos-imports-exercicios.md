# Exercícios — Módulo 24: Módulos e Imports

[<- Voltar ao Módulo 24](24-modulos-imports.md) | [Glossário](00-glossario.md)

> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-24/` e execute com `python3 nome_do_arquivo.py`.

---

## Exercício 1 — Usar o Módulo math — Nível: Básico
**Conceitos:** import, math.sqrt, math.pow

### Enunciado
Crie um programa que importe o módulo `math` e calcule: a raiz quadrada de 169, o valor de 5 elevado a 3, e o valor de pi. Exiba os tres resultados.

### Dicas
- Use `import math` para importar o módulo
- `math.sqrt()` calcula a raiz quadrada
- `math.pow()` calcula a potência
- `math.pi` contem o valor de pi

### Proposta de Teste
- Saida esperada:
  ```
  Raiz quadrada de 169: 13.0
  5 elevado a 3: 125.0
  Valor de pi: 3.141592653589793
  ```
- Caso de borda: calcule também `math.sqrt(0)` — o resultado deve ser `0.0`

### Resposta Comentada
```python
# Importamos o modulo math (matematica)
import math

# Calculamos a raiz quadrada de 169
# math.sqrt() = square root = raiz quadrada
# "square_root" = raiz quadrada
square_root = math.sqrt(169)
# Exibimos o resultado
print(f"Raiz quadrada de 169: {square_root}")

# Calculamos 5 elevado a 3
# math.pow() = power = potencia
# "power" = potencia
power = math.pow(5, 3)
# Exibimos o resultado
print(f"5 elevado a 3: {power}")

# Exibimos o valor de pi
# math.pi = constante pi (3.14159...)
print(f"Valor de pi: {math.pi}")
```

---

## Exercício 2 — Usar from...import — Nível: Básico
**Conceitos:** from...import, randint, choice

### Enunciado
Crie um programa que importe `randint` e `choice` do módulo `random`. Use `randint` para gerar um número aleatorio entre 1 e 100, e `choice` para sortear uma cor de uma lista com pelo menos 5 cores.

### Dicas
- Use `from random import randint, choice`
- `randint(1, 100)` gera um número entre 1 e 100
- `choice(lista)` escolhe um item aleatorio da lista
- Lembre-se: os resultados serao diferentes a cada execução

### Proposta de Teste
- Saida esperada (exemplo — seus valores serao diferentes):
  ```
  Número sorteado: 42
  Cor sorteada: azul
  ```
- Caso de borda: crie uma lista com apenas 1 cor — `choice` deve retornar sempre essa cor

### Resposta Comentada
```python
# Importamos randint e choice do modulo random (aleatorio)
# "randint" = random integer = inteiro aleatorio
# "choice" = escolha
from random import randint, choice

# Geramos um numero aleatorio entre 1 e 100
# "random_number" = numero aleatorio
random_number = randint(1, 100)
# Exibimos o numero sorteado
print(f"Numero sorteado: {random_number}")

# Criamos uma lista de cores
# "colors" = cores
colors = ["vermelho", "azul", "verde", "amarelo", "roxo"]
# Sorteamos uma cor da lista
# "chosen_color" = cor escolhida
chosen_color = choice(colors)
# Exibimos a cor sorteada
print(f"Cor sorteada: {chosen_color}")
```

---

## Exercício 3 — Usar import...as — Nível: Básico
**Conceitos:** import...as, datetime

### Enunciado
Crie um programa que importe o módulo `datetime` com o apelido `dt`. Use-o para exibir a data de hoje, o ano atual e o mes atual.

### Dicas
- Use `import datetime as dt`
- `dt.date.today()` retorna a data de hoje
- O objeto de data tem atributos `.year` (ano) e `.month` (mes)

### Proposta de Teste
- Saida esperada (exemplo — a data sera a do dia da execução):
  ```
  Data de hoje: 2025-01-15
  Ano atual: 2025
  Mes atual: 1
  ```
- Caso de borda: verifique que o programa funciona em qualquer dia do ano

### Resposta Comentada
```python
# Importamos o modulo datetime com o apelido "dt"
# "datetime" = data e hora
# "as" = como (apelido)
import datetime as dt

# Obtemos a data de hoje
# dt.date.today() retorna a data atual
# "today" = hoje
today = dt.date.today()

# Exibimos a data completa
print(f"Data de hoje: {today}")

# Exibimos o ano atual
# .year = ano
print(f"Ano atual: {today.year}")

# Exibimos o mes atual
# .month = mes
print(f"Mes atual: {today.month}")
```

---

## Exercício 4 — Criar um Módulo Simples — Nível: Básico
**Conceitos:** criar módulo, import, funções

### Enunciado
Crie um módulo chamado `greetings.py` (saudacoes) com duas funções: `say_hello` (dizer ola) que recebe um nome e retorna uma saudacao, e `say_goodbye` (dizer adeus) que recebe um nome e retorna uma despedida. Depois, crie um arquivo `main.py` que importe e use essas funções.

### Dicas
- Crie o arquivo `greetings.py` com as duas funções
- Cada função recebe um parametro `name` (nome)
- No `main.py`, use `import greetings` ou `from greetings import ...`
- Os dois arquivos devem estar na mesma pasta

### Proposta de Teste
- Execute `python3 main.py` e a saida esperada deve ser:
  ```
  Ola, Maria! Seja bem-vinda!
  Ate logo, Maria! Volte sempre!
  ```
- Caso de borda: teste com um nome vazio `""` — o programa deve funcionar sem erro

### Resposta Comentada

**Arquivo `greetings.py`:**
```python
# Arquivo: greetings.py
# Modulo com funcoes de saudacao
# "greetings" = saudacoes

# Funcao que retorna uma saudacao
# "say_hello" = dizer ola
# "name" = nome
def say_hello(name):
    # Retornamos uma mensagem de boas-vindas
    # f-string formata o texto com o nome recebido
    return f"Ola, {name}! Seja bem-vinda!"

# Funcao que retorna uma despedida
# "say_goodbye" = dizer adeus
# "name" = nome
def say_goodbye(name):
    # Retornamos uma mensagem de despedida
    return f"Ate logo, {name}! Volte sempre!"
```

**Arquivo `main.py`:**
```python
# Arquivo: main.py
# Programa principal que usa o modulo greetings

# Importamos as funcoes do modulo greetings (saudacoes)
# "say_hello" = dizer ola, "say_goodbye" = dizer adeus
from greetings import say_hello, say_goodbye

# Usamos as funcoes importadas
# "greeting" = saudacao
greeting = say_hello("Maria")
# Exibimos a saudacao
print(greeting)

# "farewell" = despedida
farewell = say_goodbye("Maria")
# Exibimos a despedida
print(farewell)
```

---

## Exercício 5 — Calculadora de Idade com datetime — Nível: Intermediario
**Conceitos:** datetime, date, cálculo com datas

### Enunciado
Crie um programa que peca ao usuario o ano, mes e dia de nascimento. Use o módulo `datetime` para calcular a idade aproximada em anos e exiba o resultado.

### Dicas
- Use `from datetime import date` para importar a classe date
- `date.today()` retorna a data de hoje
- `date(ano, mes, dia)` cria uma data específica
- Para calcular a idade, subtraia as datas e divida os dias por 365

### Proposta de Teste
- Digite ano `1990`, mes `6`, dia `15` — a saida deve ser algo como:
  ```
  Sua idade aproximada: 34 anos
  ```
- Caso de borda: digite a data de hoje — a saida deve ser `0 anos`

### Resposta Comentada
```python
# Importamos a classe date do modulo datetime
# "date" = data
from datetime import date

# Pedimos o ano de nascimento ao usuario
# "birth_year" = ano de nascimento
birth_year = int(input("Digite o ano de nascimento: "))
# Pedimos o mes de nascimento
# "birth_month" = mes de nascimento
birth_month = int(input("Digite o mes de nascimento: "))
# Pedimos o dia de nascimento
# "birth_day" = dia de nascimento
birth_day = int(input("Digite o dia de nascimento: "))

# Criamos a data de nascimento
# "birthday" = data de nascimento
birthday = date(birth_year, birth_month, birth_day)

# Obtemos a data de hoje
# "today" = hoje
today = date.today()

# Calculamos a diferenca em dias
# "difference" = diferenca
difference = today - birthday

# Calculamos a idade aproximada dividindo os dias por 365
# "age" = idade
age = difference.days // 365

# Exibimos o resultado
print(f"Sua idade aproximada: {age} anos")
```

---

## Exercício 6 — Módulo com Funções de Texto — Nível: Intermediario
**Conceitos:** criar módulo, from...import, manipulação de strings

### Enunciado
Crie um módulo chamado `text_tools.py` (ferramentas de texto) com tres funções: `count_vowels` (contar vogais) que conta as vogais em um texto, `reverse_text` (inverter texto) que inverte uma string, e `is_palindrome` (e palindromo) que verifica se uma palavra e um palindromo. Crie um `main.py` que teste as tres funções.

### Dicas
- Vogais: a, e, i, o, u (considere maiusculas e minusculas)
- Para inverter um texto, use fatiamento: `text[::-1]`
- Um palindromo e uma palavra que se le igual de tras para frente (ex: "arara")
- Use `.lower()` para comparar sem diferenciar maiusculas de minusculas

### Proposta de Teste
- Saida esperada:
  ```
  Vogais em 'Python e legal': 4
  'Python' invertido: nohtyP
  'arara' e palindromo? True
  'python' e palindromo? False
  ```
- Caso de borda: teste com texto vazio `""` — vogais devem ser 0, invertido deve ser `""`, palindromo deve ser `True`

### Resposta Comentada

**Arquivo `text_tools.py`:**
```python
# Arquivo: text_tools.py
# Modulo com ferramentas de manipulacao de texto
# "text_tools" = ferramentas de texto

# Funcao que conta as vogais em um texto
# "count_vowels" = contar vogais
# "text" = texto
def count_vowels(text):
    # Definimos as vogais (maiusculas e minusculas)
    # "vowels" = vogais
    vowels = "aeiouAEIOU"
    # Iniciamos o contador em zero
    # "count" = contagem
    count = 0
    # Percorremos cada caractere do texto
    # "char" = character = caractere
    for char in text:
        # Se o caractere for uma vogal, incrementamos o contador
        if char in vowels:
            count = count + 1
    # Retornamos a contagem total de vogais
    return count

# Funcao que inverte um texto
# "reverse_text" = inverter texto
# "text" = texto
def reverse_text(text):
    # Usamos fatiamento com passo -1 para inverter
    # [::-1] le o texto de tras para frente
    return text[::-1]

# Funcao que verifica se uma palavra e palindromo
# "is_palindrome" = e palindromo
# "word" = palavra
def is_palindrome(word):
    # Convertemos para minusculas para comparar sem diferenciar
    # "clean_word" = palavra limpa
    clean_word = word.lower()
    # Comparamos a palavra com ela mesma invertida
    return clean_word == clean_word[::-1]
```

**Arquivo `main.py`:**
```python
# Arquivo: main.py
# Programa que testa as funcoes do modulo text_tools

# Importamos as funcoes do nosso modulo
# "count_vowels" = contar vogais
# "reverse_text" = inverter texto
# "is_palindrome" = e palindromo
from text_tools import count_vowels, reverse_text, is_palindrome

# Testamos a contagem de vogais
# "vowel_count" = contagem de vogais
vowel_count = count_vowels("Python e legal")
print(f"Vogais em 'Python e legal': {vowel_count}")

# Testamos a inversao de texto
# "reversed_word" = palavra invertida
reversed_word = reverse_text("Python")
print(f"'Python' invertido: {reversed_word}")

# Testamos o verificador de palindromo
# "result" = resultado
result = is_palindrome("arara")
print(f"'arara' e palindromo? {result}")

result = is_palindrome("python")
print(f"'python' e palindromo? {result}")
```

---

## Exercício 7 — Jogo de Adivinhacao com random — Nível: Intermediario
**Conceitos:** random.randint, while, input, comparação

### Enunciado
Crie um jogo de adivinhacao. O programa deve gerar um número aleatorio entre 1 e 50 usando o módulo `random`. O usuario tem 5 tentativas para adivinhar. A cada tentativa, o programa diz se o número e maior ou menor.

### Dicas
- Use `from random import randint` para importar a função
- Use um loop `while` com um contador de tentativas
- Compare o palpite com o número secreto usando `if/elif/else`
- Converta a entrada do usuario com `int(input(...))`

### Proposta de Teste
- O programa gera o número 25. O usuario digita: 10, 30, 20, 25
  ```
  Tentativa 1/5 - Seu palpite: 10
  O número e MAIOR que 10.
  Tentativa 2/5 - Seu palpite: 30
  O número e MENOR que 30.
  Tentativa 3/5 - Seu palpite: 20
  O número e MAIOR que 20.
  Tentativa 4/5 - Seu palpite: 25
  Parabéns! Você acertou em 4 tentativas!
  ```
- Caso de borda: o usuario não acerta em 5 tentativas — o programa deve revelar o número:
  ```
  Suas tentativas acabaram! O número era 25.
  ```

### Resposta Comentada
```python
# Importamos randint do modulo random (aleatorio)
# "randint" = random integer = inteiro aleatorio
from random import randint

# Geramos um numero aleatorio entre 1 e 50
# "secret_number" = numero secreto
secret_number = randint(1, 50)

# Definimos o numero maximo de tentativas
# "max_attempts" = maximo de tentativas
max_attempts = 5

# Variavel para controlar se o usuario acertou
# "guessed" = adivinhou
guessed = False

# Loop para as tentativas
# "attempt" = tentativa
attempt = 1
# Enquanto houver tentativas e o usuario nao tiver acertado
while attempt <= max_attempts and not guessed:
    # Pedimos o palpite do usuario
    # "guess" = palpite
    guess = int(input(f"Tentativa {attempt}/{max_attempts} - Seu palpite: "))

    # Comparamos o palpite com o numero secreto
    if guess == secret_number:
        # O usuario acertou
        print(f"Parabens! Voce acertou em {attempt} tentativas!")
        guessed = True
    elif guess < secret_number:
        # O numero secreto e maior
        print(f"O numero e MAIOR que {guess}.")
    else:
        # O numero secreto e menor
        print(f"O numero e MENOR que {guess}.")

    # Incrementamos o contador de tentativas
    attempt = attempt + 1

# Se o usuario nao acertou, revelamos o numero
if not guessed:
    print(f"Suas tentativas acabaram! O numero era {secret_number}.")
```

---

## Exercício 8 — Listar Arquivos com os — Nível: Intermediario
**Conceitos:** import os, listdir, path.exists

### Enunciado
Crie um programa que use o módulo `os` para: exibir o diretório atual, listar todos os arquivos do diretório atual, e verificar se um arquivo chamado `dados.txt` existe.

### Dicas
- Use `import os` para importar o módulo
- `os.getcwd()` retorna o diretório atual
- `os.listdir(".")` lista os arquivos do diretório atual
- `os.path.exists("dados.txt")` verifica se o arquivo existe

### Proposta de Teste
- Saida esperada (os valores dependem do seu computador):
  ```
  Diretório atual: /home/usuario/meus-projetos/python-curso/módulo-24
  Arquivos encontrados: ['main.py', 'greetings.py']
  O arquivo dados.txt existe? False
  ```
- Caso de borda: crie um arquivo `dados.txt` vazio na pasta e execute novamente — a ultima linha deve mostrar `True`

### Resposta Comentada
```python
# Importamos o modulo os (sistema operacional)
# "os" = operating system = sistema operacional
import os

# Obtemos o diretorio atual
# os.getcwd() = get current working directory = obter diretorio de trabalho atual
# "current_dir" = diretorio atual
current_dir = os.getcwd()
# Exibimos o diretorio atual
print(f"Diretorio atual: {current_dir}")

# Listamos os arquivos do diretorio atual
# os.listdir(".") = list directory = listar diretorio
# "." significa "diretorio atual"
# "files" = arquivos
files = os.listdir(".")
# Exibimos a lista de arquivos
print(f"Arquivos encontrados: {files}")

# Verificamos se o arquivo dados.txt existe
# os.path.exists() = verificar se o caminho existe
# "file_exists" = arquivo existe
file_exists = os.path.exists("dados.txt")
# Exibimos o resultado
print(f"O arquivo dados.txt existe? {file_exists}")
```

---

## Exercício 9 — Módulo de Conversão de Unidades — Nível: Intermediario
**Conceitos:** criar módulo, funções com return, import

### Enunciado
Crie um módulo chamado `converters.py` (conversores) com tres funções: `km_to_miles` (quilometros para milhas), `celsius_to_fahrenheit` (celsius para fahrenheit) e `kg_to_pounds` (quilos para libras). Crie um `main.py` que peca ao usuario um valor em quilometros, converta e exiba o resultado em milhas. Faca o mesmo para temperatura e peso.

### Dicas
- 1 km = 0.621371 milhas
- Fahrenheit = (Celsius * 9/5) + 32
- 1 kg = 2.20462 libras
- Use `float(input(...))` para ler valores decimais

### Proposta de Teste
- Digite 10 km, 30 graus Celsius, 75 kg:
  ```
  10.0 km = 6.21 milhas
  30.0 C = 86.00 F
  75.0 kg = 165.35 libras
  ```
- Caso de borda: digite 0 para todos — os resultados devem ser `0.00 milhas`, `32.00 F`, `0.00 libras`

### Resposta Comentada

**Arquivo `converters.py`:**
```python
# Arquivo: converters.py
# Modulo com funcoes de conversao de unidades
# "converters" = conversores

# Funcao que converte quilometros para milhas
# "km_to_miles" = quilometros para milhas
# "km" = quilometros
def km_to_miles(km):
    # 1 quilometro equivale a 0.621371 milhas
    # "miles" = milhas
    miles = km * 0.621371
    # Retornamos o valor em milhas
    return miles

# Funcao que converte Celsius para Fahrenheit
# "celsius_to_fahrenheit" = celsius para fahrenheit
# "celsius" = temperatura em graus Celsius
def celsius_to_fahrenheit(celsius):
    # Formula: Fahrenheit = (Celsius * 9/5) + 32
    # "fahrenheit" = temperatura em Fahrenheit
    fahrenheit = (celsius * 9 / 5) + 32
    # Retornamos o valor em Fahrenheit
    return fahrenheit

# Funcao que converte quilogramas para libras
# "kg_to_pounds" = quilogramas para libras
# "kg" = quilogramas
def kg_to_pounds(kg):
    # 1 quilograma equivale a 2.20462 libras
    # "pounds" = libras
    pounds = kg * 2.20462
    # Retornamos o valor em libras
    return pounds
```

**Arquivo `main.py`:**
```python
# Arquivo: main.py
# Programa que usa o modulo de conversao de unidades

# Importamos as funcoes do modulo converters (conversores)
from converters import km_to_miles, celsius_to_fahrenheit, kg_to_pounds

# Pedimos a distancia em quilometros
# "km" = quilometros
km = float(input("Digite a distancia em km: "))
# Convertemos e exibimos
# "miles" = milhas
miles = km_to_miles(km)
print(f"{km} km = {miles:.2f} milhas")

# Pedimos a temperatura em Celsius
# "celsius" = graus Celsius
celsius = float(input("Digite a temperatura em Celsius: "))
# Convertemos e exibimos
# "fahrenheit" = graus Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} C = {fahrenheit:.2f} F")

# Pedimos o peso em quilogramas
# "kg" = quilogramas
kg = float(input("Digite o peso em kg: "))
# Convertemos e exibimos
# "pounds" = libras
pounds = kg_to_pounds(kg)
print(f"{kg} kg = {pounds:.2f} libras")
```

---

## Exercício 10 — Sorteio de Equipes com random — Nível: Intermediario
**Conceitos:** random.shuffle, listas, loops, módulos

### Enunciado
Crie um programa que receba nomes de 6 participantes e use o módulo `random` para embaralhar a lista e dividir em 2 equipes de 3 pessoas cada. Exiba as equipes formadas.

### Dicas
- Use `random.shuffle(lista)` para embaralhar a lista
- Apos embaralhar, use fatiamento para dividir: `lista[:3]` e `lista[3:]`
- Use um loop `for` com `range(6)` para pedir os 6 nomes

### Proposta de Teste
- Digite os nomes: Ana, Bruno, Carlos, Diana, Eduardo, Fernanda
- Saida esperada (a ordem sera diferente a cada execução):
  ```
  Equipe 1: ['Carlos', 'Ana', 'Fernanda']
  Equipe 2: ['Bruno', 'Diana', 'Eduardo']
  ```
- Caso de borda: digite nomes iguais — o programa deve funcionar normalmente, mesmo com nomes repetidos

### Resposta Comentada
```python
# Importamos a funcao shuffle do modulo random (aleatorio)
# "shuffle" = embaralhar
from random import shuffle

# Criamos uma lista vazia para os participantes
# "participants" = participantes
participants = []

# Pedimos 6 nomes ao usuario
# "i" = indice do loop
for i in range(6):
    # Pedimos o nome do participante
    # "name" = nome
    name = input(f"Digite o nome do participante {i + 1}: ")
    # Adicionamos o nome a lista
    participants.append(name)

# Embaralhamos a lista de participantes
# shuffle() modifica a lista diretamente
shuffle(participants)

# Dividimos em duas equipes usando fatiamento
# "team_one" = equipe um (primeiros 3 nomes)
team_one = participants[:3]
# "team_two" = equipe dois (ultimos 3 nomes)
team_two = participants[3:]

# Exibimos as equipes formadas
print(f"Equipe 1: {team_one}")
print(f"Equipe 2: {team_two}")
```

---

## Exercício 11 — Gerador de Senhas com random e string — Nível: Avancado
**Conceitos:** import, random.choice, string, loops, funções

### Enunciado
Crie um módulo chamado `password_generator.py` (gerador de senhas) com uma função `generate_password` (gerar senha) que receba o tamanho desejado e retorne uma senha aleatoria contendo letras maiusculas, minusculas e números. Crie um `main.py` que peca ao usuario o tamanho da senha e exiba a senha gerada.

### Dicas
- O módulo `string` tem constantes úteis: `string.ascii_letters` (letras) e `string.digits` (digitos)
- Use `random.choice()` dentro de um loop para escolher caracteres aleatorios
- Junte os caracteres com `"".join(lista)`
- Importe ambos os módulos: `import random` e `import string`

### Proposta de Teste
- Digite tamanho 8 — a saida deve ser algo como:
  ```
  Senha gerada: kR7mP2xN
  ```
- Caso de borda: digite tamanho 1 — a senha deve ter exatamente 1 caractere

### Resposta Comentada

**Arquivo `password_generator.py`:**
```python
# Arquivo: password_generator.py
# Modulo para geracao de senhas aleatorias
# "password_generator" = gerador de senhas

# Importamos o modulo random (aleatorio) para escolhas aleatorias
import random
# Importamos o modulo string para acessar letras e digitos
import string

# Funcao que gera uma senha aleatoria
# "generate_password" = gerar senha
# "length" = comprimento/tamanho
def generate_password(length):
    # Criamos o conjunto de caracteres possiveis
    # string.ascii_letters = todas as letras (maiusculas e minusculas)
    # string.digits = todos os digitos (0-9)
    # "characters" = caracteres
    characters = string.ascii_letters + string.digits

    # Criamos uma lista vazia para guardar os caracteres da senha
    # "password_chars" = caracteres da senha
    password_chars = []

    # Escolhemos caracteres aleatorios ate atingir o tamanho desejado
    # "i" = indice do loop
    for i in range(length):
        # random.choice() escolhe um caractere aleatorio do conjunto
        # "char" = character = caractere
        char = random.choice(characters)
        # Adicionamos o caractere a lista
        password_chars.append(char)

    # Juntamos todos os caracteres em uma unica string
    # "".join() une os itens da lista sem separador
    # "password" = senha
    password = "".join(password_chars)

    # Retornamos a senha gerada
    return password
```

**Arquivo `main.py`:**
```python
# Arquivo: main.py
# Programa que gera senhas usando o modulo password_generator

# Importamos a funcao do nosso modulo
# "generate_password" = gerar senha
from password_generator import generate_password

# Pedimos o tamanho da senha ao usuario
# "length" = comprimento/tamanho
length = int(input("Digite o tamanho da senha desejada: "))

# Geramos a senha
# "password" = senha
password = generate_password(length)

# Exibimos a senha gerada
print(f"Senha gerada: {password}")
```

---

## Exercício 12 — Pacote com __init__.py — Nível: Avancado
**Conceitos:** pacote, __init__.py, importacao absoluta, estrutura de pastas

### Enunciado
Crie um pacote chamado `shop` (loja) com dois módulos: `products.py` (produtos) com uma função `format_product` que formata as informações de um produto, e `pricing.py` (precos) com uma função `apply_discount` que aplica um desconto percentual a um preco. Crie o `__init__.py` e um `main.py` que use ambos os módulos.

### Dicas
- Crie uma pasta chamada `shop/` com tres arquivos: `__init__.py`, `products.py`, `pricing.py`
- O `__init__.py` pode estar vazio
- No `main.py`, use `from shop.products import format_product`
- A função de desconto: `preco_final = preco * (1 - desconto / 100)`

### Proposta de Teste
- Saida esperada:
  ```
  Produto: Arroz - R$ 5.99
  Preco com 10% de desconto: R$ 5.39
  ```
- Caso de borda: aplique desconto de 0% — o preco deve permanecer o mesmo. Aplique desconto de 100% — o preco deve ser R$ 0.00

### Resposta Comentada

**Estrutura de pastas:**
```
modulo-24/
    main.py
    shop/
        __init__.py
        products.py
        pricing.py
```

**Arquivo `shop/__init__.py`:**
```python
# Arquivo: shop/__init__.py
# Este arquivo transforma a pasta "shop" em um pacote Python
# Pode estar vazio — sua existencia ja e suficiente
```

**Arquivo `shop/products.py`:**
```python
# Arquivo: shop/products.py
# Modulo com funcoes relacionadas a produtos
# "products" = produtos

# Funcao que formata as informacoes de um produto
# "format_product" = formatar produto
# "name" = nome, "price" = preco
def format_product(name, price):
    # Retornamos uma string formatada com nome e preco
    # :.2f formata o preco com 2 casas decimais
    return f"Produto: {name} - R$ {price:.2f}"
```

**Arquivo `shop/pricing.py`:**
```python
# Arquivo: shop/pricing.py
# Modulo com funcoes relacionadas a precos
# "pricing" = precificacao

# Funcao que aplica um desconto percentual a um preco
# "apply_discount" = aplicar desconto
# "price" = preco, "discount_percent" = percentual de desconto
def apply_discount(price, discount_percent):
    # Calculamos o preco final aplicando o desconto
    # Formula: preco * (1 - desconto/100)
    # "final_price" = preco final
    final_price = price * (1 - discount_percent / 100)
    # Retornamos o preco final
    return final_price
```

**Arquivo `main.py`:**
```python
# Arquivo: main.py
# Programa que usa o pacote shop (loja)

# Importamos funcoes dos modulos dentro do pacote shop
# "shop" = loja (nome do pacote/pasta)
# "products" = modulo de produtos
# "format_product" = formatar produto
from shop.products import format_product
# "pricing" = modulo de precos
# "apply_discount" = aplicar desconto
from shop.pricing import apply_discount

# Formatamos um produto
# "product_info" = informacoes do produto
product_info = format_product("Arroz", 5.99)
# Exibimos as informacoes formatadas
print(product_info)

# Aplicamos um desconto de 10%
# "discounted_price" = preco com desconto
discounted_price = apply_discount(5.99, 10)
# Exibimos o preco com desconto
print(f"Preco com 10% de desconto: R$ {discounted_price:.2f}")
```

---

[<- Voltar ao Módulo 24](24-modulos-imports.md) | [Glossário](00-glossario.md)
