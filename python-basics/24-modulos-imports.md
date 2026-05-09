# 24 — Módulos e Imports: Reutilizando Código em Python

[<- Anterior: Exercícios Integradores](23-exercícios-integradores.md) | [Glossário](00-glossário.md) | [Próximo: Estruturação de Projetos ->](25-estruturação-projetos.md)

---

## Introdução

Ate agora, você escreveu todo o seu código em um único arquivo Python. Isso funciona bem para programas pequenos, mas conforme seus projetos crescem, manter tudo em um único arquivo se torna confuso e difícil de gerenciar.

Imagine que você tem uma cozinha enorme onde guarda **todos** os utensilios, ingredientes, receitas e temperos em uma única gaveta gigante. Encontrar algo seria um pesadelo. A solução natural e **organizar**: utensilios em uma gaveta, temperos em outra, receitas em um caderno separado. Quando você precisa de algo, sabe exatamente onde procurar.

Em programação, **módulos** sao essa forma de organização. Um módulo e simplesmente um arquivo Python (`.py`) que contem funções, classes e variáveis que você pode **importar** e usar em outros arquivos. O Python ja vem com centenas de módulos prontos (a **biblioteca padrão**), e você também pode criar os seus proprios.

Neste módulo, você vai aprender:

- Como importar módulos usando `import`, `from...import` e `import...as`
- Como usar módulos da biblioteca padrão do Python (`math`, `random`, `datetime`, `os`)
- Como criar seus proprios arquivos e importa-los como módulos
- A diferença entre importacao absoluta e relativa
- O papel do arquivo `__init__.py`

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-24/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-24`
4. Execute: `python3 nome_do_arquivo.py`

---

## O Que e um Módulo

Um **módulo** (module) e simplesmente um arquivo Python com a extensão `.py`. Qualquer arquivo Python que você ja criou ate agora e, tecnicamente, um módulo.

A diferença e que, quando falamos de módulos, estamos pensando em arquivos que foram **projetados para serem reutilizados** por outros arquivos. Em vez de copiar e colar o mesmo código em vários lugares, você escreve uma vez e **importa** onde precisar.

### Analogia: Biblioteca Pública

Pense em uma **biblioteca pública**. Ela tem milhares de livros organizados por assunto. Quando você precisa de informação sobre culinaria, vai ate a secao de culinaria e pega o livro que precisa. Você não precisa escrever o livro — ele ja esta la, pronto para uso.

Em Python:
- A **biblioteca padrão** e como a biblioteca pública — cheia de módulos prontos
- Cada **módulo** e como um livro — contem funções e ferramentas sobre um assunto
- O comando **import** e como ir ate a estante e pegar o livro que você precisa

---

## As Tres Formas de Importar

O Python oferece tres formas principais de importar módulos. Vamos aprender cada uma com calma.

### Forma 1: import (Importar o Módulo Inteiro)

A forma mais simples e usar `import` seguido do nome do módulo. Isso traz o módulo inteiro para o seu programa:

```python
# Importamos o modulo math (matematica)
# "math" = matematica — modulo com funcoes matematicas
import math

# Para usar uma funcao do modulo, escrevemos: modulo.funcao()
# math.sqrt() calcula a raiz quadrada (square root = raiz quadrada)
# "result" = resultado
result = math.sqrt(25)

# Exibimos o resultado
print(result)
```

Saida esperada:
```
5.0
```

Quando usamos `import math`, precisamos sempre escrever `math.` antes de cada função. Isso e como dizer: "quero a função `sqrt` que esta dentro do módulo `math`".

### Forma 2: from...import (Importar Algo Específico)

Se você precisa de apenas uma ou duas funções de um módulo, pode importar diretamente:

```python
# Importamos apenas a funcao sqrt (raiz quadrada) do modulo math
# "from" = de, "import" = importar
# "sqrt" = square root = raiz quadrada
from math import sqrt

# Agora podemos usar sqrt() diretamente, sem escrever math.
# "result" = resultado
result = sqrt(36)

# Exibimos o resultado
print(result)
```

Saida esperada:
```
6.0
```

A vantagem e que o código fica mais curto — você escreve `sqrt(36)` em vez de `math.sqrt(36)`. A desvantagem e que, se você importar muitas funções de módulos diferentes, pode ficar confuso saber de onde cada função veio.

### Importando Multiplas Funções

Você pode importar várias funções de uma vez, separando por virgula:

```python
# Importamos sqrt (raiz quadrada) e pow (potencia) do modulo math
# "sqrt" = raiz quadrada, "pow" = power = potencia
from math import sqrt, pow

# Calculamos a raiz quadrada de 49
# "square_root" = raiz quadrada
square_root = sqrt(49)
print(f"Raiz quadrada de 49: {square_root}")

# Calculamos 2 elevado a 10
# "power_result" = resultado da potencia
power_result = pow(2, 10)
print(f"2 elevado a 10: {power_result}")
```

Saida esperada:
```
Raiz quadrada de 49: 7.0
2 elevado a 10: 1024.0
```

### Forma 3: import...as (Importar com Apelido)

As vezes, o nome de um módulo e longo ou você quer usar um nome mais curto. O `as` permite criar um **apelido** (alias) para o módulo:

```python
# Importamos o modulo datetime com o apelido "dt"
# "datetime" = data e hora
# "as" = como (apelido)
import datetime as dt

# Usamos o apelido "dt" em vez do nome completo "datetime"
# dt.date.today() retorna a data de hoje
# "today" = hoje
today = dt.date.today()

# Exibimos a data de hoje
print(f"Data de hoje: {today}")
```

Saida esperada:
```
Data de hoje: 2025-01-15
```

> **Nota:** A data exibida sera a data real do dia em que você executar o programa.

Você também pode usar `as` com `from...import`:

```python
# Importamos a funcao sqrt com o apelido "raiz"
# "sqrt" = square root = raiz quadrada
# Usamos "raiz" como apelido em portugues
from math import sqrt as raiz

# Agora podemos usar "raiz()" em vez de "sqrt()"
# "result" = resultado
result = raiz(100)
print(f"Raiz quadrada de 100: {result}")
```

Saida esperada:
```
Raiz quadrada de 100: 10.0
```

### Comparação das Tres Formas

Vamos ver o mesmo exemplo usando as tres formas para comparar:

```python
# FORMA 1: import modulo
# Importamos o modulo math inteiro
import math
# Precisamos escrever math. antes de cada funcao
print(math.sqrt(16))

# FORMA 2: from modulo import funcao
# Importamos apenas a funcao sqrt
from math import sqrt
# Usamos a funcao diretamente
print(sqrt(16))

# FORMA 3: import modulo as apelido
# Importamos o modulo math com apelido "m"
import math as m
# Usamos o apelido
print(m.sqrt(16))
```

Saida esperada:
```
4.0
4.0
4.0
```

| Forma | Sintaxe | Quando Usar |
|-------|---------|-------------|
| `import modulo` | `math.sqrt(16)` | Quando você usa várias funções do módulo |
| `from modulo import funcao` | `sqrt(16)` | Quando você usa poucas funções especificas |
| `import modulo as apelido` | `m.sqrt(16)` | Quando o nome do módulo e longo |

---

## Módulos da Biblioteca Padrão

O Python vem com uma enorme coleção de módulos prontos chamada **biblioteca padrão** (standard library). Esses módulos ja estão instalados junto com o Python — você não precisa instalar nada extra.

Vamos conhecer quatro dos módulos mais úteis para iniciantes.

### Módulo math — Funções Matematicas

O módulo `math` contem funções matematicas avancadas. Aqui estão as mais usadas:

```python
# Importamos o modulo math (matematica)
import math

# sqrt() — raiz quadrada (square root)
# "square_root" = raiz quadrada
square_root = math.sqrt(144)
print(f"Raiz quadrada de 144: {square_root}")

# ceil() — arredonda para cima (ceiling = teto)
# "rounded_up" = arredondado para cima
rounded_up = math.ceil(4.2)
print(f"4.2 arredondado para cima: {rounded_up}")

# floor() — arredonda para baixo (floor = chao)
# "rounded_down" = arredondado para baixo
rounded_down = math.floor(4.8)
print(f"4.8 arredondado para baixo: {rounded_down}")

# pi — o valor de pi (3.14159...)
# "pi" = pi (constante matematica)
print(f"Valor de pi: {math.pi}")

# pow() — potencia (power = potencia)
# "power" = potencia
power = math.pow(3, 4)
print(f"3 elevado a 4: {power}")

# fabs() — valor absoluto (absolute = absoluto)
# "absolute" = valor absoluto
absolute = math.fabs(-15)
print(f"Valor absoluto de -15: {absolute}")
```

Saida esperada:
```
Raiz quadrada de 144: 12.0
4.2 arredondado para cima: 5
4.8 arredondado para baixo: 4
Valor de pi: 3.141592653589793
3 elevado a 4: 81.0
Valor absoluto de -15: 15.0
```

### Módulo random — Números Aleatorios

O módulo `random` permite gerar números aleatorios e fazer escolhas aleatorias. E muito útil para jogos, sorteios e simulacoes.

```python
# Importamos o modulo random (aleatorio)
# "random" = aleatorio
import random

# randint() — gera um numero inteiro aleatorio entre dois valores
# "random_number" = numero aleatorio
# randint(1, 10) gera um numero entre 1 e 10 (incluindo ambos)
random_number = random.randint(1, 10)
print(f"Numero aleatorio entre 1 e 10: {random_number}")

# choice() — escolhe um item aleatorio de uma lista
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva", "manga"]
# "chosen_fruit" = fruta escolhida
chosen_fruit = random.choice(fruits)
print(f"Fruta sorteada: {chosen_fruit}")

# shuffle() — embaralha uma lista (shuffle = embaralhar)
# "numbers" = numeros
numbers = [1, 2, 3, 4, 5]
print(f"Lista original: {numbers}")
# shuffle() modifica a lista diretamente (nao retorna nada)
random.shuffle(numbers)
print(f"Lista embaralhada: {numbers}")

# uniform() — gera um numero decimal aleatorio entre dois valores
# "random_price" = preco aleatorio
random_price = random.uniform(1.00, 50.00)
print(f"Preco aleatorio: R$ {random_price:.2f}")
```

Saida esperada:
```
Numero aleatorio entre 1 e 10: 7
Fruta sorteada: laranja
Lista original: [1, 2, 3, 4, 5]
Lista embaralhada: [3, 1, 5, 2, 4]
Preco aleatorio: R$ 23.47
```

> **Nota:** Como os valores sao aleatorios, a saida do seu programa sera diferente a cada execução. Isso e normal e esperado.

### Módulo datetime — Data e Hora

O módulo `datetime` permite trabalhar com datas e horarios:

```python
# Importamos o modulo datetime (data e hora)
# "datetime" = data e hora
import datetime

# date.today() — retorna a data de hoje
# "today" = hoje
today = datetime.date.today()
print(f"Data de hoje: {today}")

# Acessamos partes da data separadamente
# "year" = ano, "month" = mes, "day" = dia
print(f"Ano: {today.year}")
print(f"Mes: {today.month}")
print(f"Dia: {today.day}")

# datetime.now() — retorna a data e hora atuais
# "now" = agora
now = datetime.datetime.now()
print(f"Data e hora atuais: {now}")

# Criamos uma data especifica
# "birthday" = aniversario/data de nascimento
birthday = datetime.date(1990, 5, 15)
print(f"Data de nascimento: {birthday}")

# Calculamos a diferenca entre duas datas
# "difference" = diferenca
# A diferenca entre datas resulta em um objeto timedelta
difference = today - birthday
# .days retorna a diferenca em dias
print(f"Dias vividos: {difference.days}")
```

Saida esperada:
```
Data de hoje: 2025-01-15
Ano: 2025
Mes: 1
Dia: 15
Data e hora atuais: 2025-01-15 14:30:00.123456
Data de nascimento: 1990-05-15
Dias vividos: 12663
```

> **Nota:** A data e hora exibidas serao as do momento em que você executar o programa.

### Módulo os — Interação com o Sistema Operacional

O módulo `os` (operating system = sistema operacional) permite interagir com o sistema de arquivos e pastas do computador:

```python
# Importamos o modulo os (sistema operacional)
# "os" = operating system = sistema operacional
import os

# getcwd() — retorna o diretorio atual (get current working directory)
# "current_directory" = diretorio atual
current_directory = os.getcwd()
print(f"Diretorio atual: {current_directory}")

# listdir() — lista os arquivos e pastas de um diretorio
# "files" = arquivos
# listdir(".") lista o diretorio atual ("." = diretorio atual)
files = os.listdir(".")
print(f"Arquivos no diretorio atual: {files}")

# path.exists() — verifica se um arquivo ou pasta existe
# "exists" = existe
# path.exists() retorna True ou False
exists = os.path.exists("meu_arquivo.txt")
print(f"O arquivo meu_arquivo.txt existe? {exists}")

# path.join() — junta partes de um caminho de forma segura
# "full_path" = caminho completo
# path.join() usa o separador correto do sistema operacional
full_path = os.path.join("pasta", "subpasta", "arquivo.py")
print(f"Caminho completo: {full_path}")
```

Saida esperada:
```
Diretorio atual: /home/usuario/meus-projetos/python-curso/modulo-24
Arquivos no diretorio atual: ['exemplo.py']
O arquivo meu_arquivo.txt existe? False
Caminho completo: pasta/subpasta/arquivo.py
```

> **Nota:** A saida do `getcwd()` e `listdir()` depende do seu computador e da pasta onde você esta executando o programa.

---

## Criando e Importando Seus Proprios Módulos

Uma das coisas mais poderosas do Python e que você pode criar seus proprios módulos. Qualquer arquivo `.py` pode ser importado por outro arquivo.

### Passo a Passo: Criando um Módulo

Vamos criar um módulo chamado `calculator.py` (calculadora) com funções matematicas simples.

**Passo 1:** Crie um arquivo chamado `calculator.py` com o seguinte conteúdo:

```python
# Arquivo: calculator.py
# Este arquivo e um modulo com funcoes de calculadora
# "calculator" = calculadora

# Funcao que soma dois numeros
# "add" = somar/adicionar
def add(a, b):
    # Retorna a soma de a e b
    return a + b

# Funcao que subtrai dois numeros
# "subtract" = subtrair
def subtract(a, b):
    # Retorna a subtracao de a por b
    return a - b

# Funcao que multiplica dois numeros
# "multiply" = multiplicar
def multiply(a, b):
    # Retorna a multiplicacao de a por b
    return a * b

# Funcao que divide dois numeros
# "divide" = dividir
def divide(a, b):
    # Verificamos se o divisor e zero para evitar erro
    if b == 0:
        # Retornamos uma mensagem de erro
        return "Erro: divisao por zero"
    # Retorna a divisao de a por b
    return a / b
```

**Passo 2:** Crie outro arquivo chamado `main.py` (principal) **na mesma pasta**:

```python
# Arquivo: main.py
# Este arquivo usa o modulo calculator que criamos
# "main" = principal

# Importamos o modulo calculator (nosso arquivo calculator.py)
# O Python procura o arquivo calculator.py na mesma pasta
import calculator

# Usamos as funcoes do nosso modulo
# "result" = resultado
result = calculator.add(10, 5)
print(f"10 + 5 = {result}")

result = calculator.subtract(10, 5)
print(f"10 - 5 = {result}")

result = calculator.multiply(10, 5)
print(f"10 * 5 = {result}")

result = calculator.divide(10, 5)
print(f"10 / 5 = {result}")

# Testamos a divisao por zero
result = calculator.divide(10, 0)
print(f"10 / 0 = {result}")
```

Saida esperada:
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 / 0 = Erro: divisao por zero
```

**Como executar:**

1. Salve ambos os arquivos na mesma pasta (por exemplo, `~/meus-projetos/python-curso/modulo-24/`)
2. No terminal, navegue ate a pasta:
   ```bash
   cd ~/meus-projetos/python-curso/módulo-24
   ```
3. Execute o arquivo principal:
   ```bash
   python3 main.py
   ```

> **Importante:** Os dois arquivos devem estar **na mesma pasta** para que o import funcione. O Python procura o módulo na pasta onde o arquivo principal esta sendo executado.

### Usando from...import com Módulos Proprios

Você também pode importar funções especificas dos seus módulos:

```python
# Arquivo: main2.py
# Importamos apenas as funcoes add e multiply do nosso modulo calculator
# "add" = somar, "multiply" = multiplicar
from calculator import add, multiply

# Usamos as funcoes diretamente, sem escrever calculator.
# "sum_result" = resultado da soma
sum_result = add(20, 30)
print(f"20 + 30 = {sum_result}")

# "product_result" = resultado da multiplicacao
product_result = multiply(6, 7)
print(f"6 * 7 = {product_result}")
```

Saida esperada:
```
20 + 30 = 50
6 * 7 = 42
```

### Exemplo Prático: Módulo de Validação

Vamos criar um exemplo mais realista — um módulo com funções de validação de dados que pode ser reutilizado em vários programas:

**Arquivo `validators.py`** (validadores):

```python
# Arquivo: validators.py
# Modulo com funcoes de validacao de dados
# "validators" = validadores

# Funcao que verifica se um nome e valido (nao vazio)
# "is_valid_name" = e um nome valido
# "name" = nome
def is_valid_name(name):
    # strip() remove espacos em branco do inicio e fim
    # Se o nome ficar vazio apos remover espacos, e invalido
    if name.strip() == "":
        return False
    return True

# Funcao que verifica se um preco e valido (maior que zero)
# "is_valid_price" = e um preco valido
# "price" = preco
def is_valid_price(price):
    # O preco deve ser um numero maior que zero
    if price > 0:
        return True
    return False

# Funcao que verifica se uma quantidade e valida (zero ou mais)
# "is_valid_quantity" = e uma quantidade valida
# "quantity" = quantidade
def is_valid_quantity(quantity):
    # A quantidade deve ser zero ou mais (nao pode ser negativa)
    if quantity >= 0:
        return True
    return False
```

**Arquivo `register_product.py`** (cadastrar produto):

```python
# Arquivo: register_product.py
# Programa que cadastra um produto usando o modulo de validacao
# "register_product" = cadastrar produto

# Importamos as funcoes de validacao do nosso modulo
from validators import is_valid_name, is_valid_price, is_valid_quantity

# Pedimos os dados do produto ao usuario
# "name" = nome
name = input("Digite o nome do produto: ")

# Verificamos se o nome e valido usando nossa funcao de validacao
if not is_valid_name(name):
    print("Erro: o nome nao pode ser vazio.")
else:
    # Pedimos o preco e convertemos para float
    # "price" = preco
    price = float(input("Digite o preco: "))

    # Verificamos se o preco e valido
    if not is_valid_price(price):
        print("Erro: o preco deve ser maior que zero.")
    else:
        # Pedimos a quantidade e convertemos para int
        # "quantity" = quantidade
        quantity = int(input("Digite a quantidade: "))

        # Verificamos se a quantidade e valida
        if not is_valid_quantity(quantity):
            print("Erro: a quantidade nao pode ser negativa.")
        else:
            # Todos os dados sao validos — exibimos o produto
            print(f"Produto cadastrado: {name} - R$ {price:.2f} ({quantity} unidades)")
```

Saida esperada (com entradas validas):
```
Digite o nome do produto: Arroz
Digite o preco: 5.99
Digite a quantidade: 100
Produto cadastrado: Arroz - R$ 5.99 (100 unidades)
```

---

## Importacao Absoluta vs Relativa

Quando seus projetos crescem e você organiza o código em **pastas** (também chamadas de **pacotes**), existem duas formas de importar módulos: **absoluta** e **relativa**.

### Importacao Absoluta

Na importacao absoluta, você escreve o **caminho completo** do módulo a partir da raiz do projeto. E a forma mais comum e recomendada:

Imagine a seguinte estrutura de pastas:

```
meu_projeto/
    main.py
    utils/
        __init__.py
        helpers.py
        validators.py
```

Para importar `helpers.py` a partir de `main.py`:

```python
# Arquivo: main.py
# Importacao absoluta — caminho completo a partir da raiz do projeto
# "utils" = utilitarios (nome da pasta)
# "helpers" = auxiliares (nome do arquivo)
from utils.helpers import format_price

# Usamos a funcao importada
# "formatted" = formatado
formatted = format_price(29.90)
print(formatted)
```

Saida esperada:
```
R$ 29.90
```

### Importacao Relativa

Na importacao relativa, você usa **pontos** (`.`) para indicar a posição relativa do módulo em relação ao arquivo atual. Um ponto (`.`) significa "na mesma pasta":

```python
# Arquivo: utils/validators.py
# Importacao relativa — o ponto (.) significa "nesta mesma pasta"
# Importamos a funcao format_price do arquivo helpers.py que esta na mesma pasta
from .helpers import format_price
```

> **Nota para iniciantes:** A importacao relativa e mais avancada e pode causar confusao. Para projetos simples, **use sempre importacao absoluta**. A importacao relativa so e necessária em projetos maiores com muitas pastas aninhadas.

### Quando Usar Cada Uma

| Tipo | Quando Usar | Exemplo |
|------|-------------|---------|
| Absoluta | Sempre que possível (recomendado) | `from utils.helpers import format_price` |
| Relativa | Dentro de pacotes grandes, entre arquivos da mesma pasta | `from .helpers import format_price` |

---

## O Papel do __init__.py

Quando você organiza seus módulos em pastas, o Python precisa saber que aquela pasta e um **pacote** (package) — ou seja, uma coleção de módulos. O arquivo `__init__.py` e o que transforma uma pasta comum em um pacote Python.

### O Que e o __init__.py?

O `__init__.py` (leia "init" ou "dunder init") e um arquivo especial que o Python procura dentro de uma pasta para reconhece-la como um pacote. Ele pode estar **vazio** ou conter código de inicialização.

### Analogia: Placa na Porta

Pense em um predio comercial com várias salas. Cada sala tem uma placa na porta dizendo o que tem la dentro: "Contabilidade", "Recursos Humanos", "Vendas". Sem a placa, você não sabe o que tem na sala.

O `__init__.py` e como essa placa. Ele diz ao Python: "esta pasta contem módulos Python que podem ser importados".

### Exemplo Prático

Vamos criar um projeto com a seguinte estrutura:

```
meu_projeto/
    main.py
    utils/
        __init__.py
        math_helpers.py
        text_helpers.py
```

**Arquivo `utils/__init__.py`** (pode estar vazio):

```python
# Arquivo: utils/__init__.py
# Este arquivo transforma a pasta "utils" em um pacote Python
# Pode estar vazio — sua simples existencia ja e suficiente
```

**Arquivo `utils/math_helpers.py`** (auxiliares matematicos):

```python
# Arquivo: utils/math_helpers.py
# Modulo com funcoes auxiliares de matematica
# "math_helpers" = auxiliares de matematica

# Funcao que calcula a media de uma lista de numeros
# "calculate_average" = calcular media
# "numbers" = numeros
def calculate_average(numbers):
    # Verificamos se a lista nao esta vazia
    if len(numbers) == 0:
        return 0
    # Somamos todos os numeros e dividimos pela quantidade
    return sum(numbers) / len(numbers)

# Funcao que encontra o maior valor de uma lista
# "find_maximum" = encontrar maximo
def find_maximum(numbers):
    # Verificamos se a lista nao esta vazia
    if len(numbers) == 0:
        return None
    # max() retorna o maior valor da lista
    return max(numbers)
```

**Arquivo `utils/text_helpers.py`** (auxiliares de texto):

```python
# Arquivo: utils/text_helpers.py
# Modulo com funcoes auxiliares de texto
# "text_helpers" = auxiliares de texto

# Funcao que formata um nome com a primeira letra maiuscula
# "format_name" = formatar nome
# "name" = nome
def format_name(name):
    # title() coloca a primeira letra de cada palavra em maiuscula
    return name.strip().title()

# Funcao que conta as palavras em um texto
# "count_words" = contar palavras
# "text" = texto
def count_words(text):
    # split() divide o texto em uma lista de palavras
    # len() conta quantos itens tem na lista
    words = text.split()
    return len(words)
```

**Arquivo `main.py`** (principal):

```python
# Arquivo: main.py
# Programa principal que usa os modulos da pasta utils

# Importamos funcoes dos nossos modulos usando importacao absoluta
# "utils" = pasta de utilitarios
# "math_helpers" = arquivo de auxiliares matematicos
from utils.math_helpers import calculate_average, find_maximum
# "text_helpers" = arquivo de auxiliares de texto
from utils.text_helpers import format_name, count_words

# Testamos as funcoes de matematica
# "grades" = notas
grades = [8.0, 7.5, 9.0, 6.5, 8.5]
# "average" = media
average = calculate_average(grades)
print(f"Media das notas: {average}")

# "highest" = mais alta
highest = find_maximum(grades)
print(f"Maior nota: {highest}")

# Testamos as funcoes de texto
# "name" = nome
name = format_name("  maria da silva  ")
print(f"Nome formatado: {name}")

# "word_count" = contagem de palavras
word_count = count_words("Python e uma linguagem de programacao")
print(f"Numero de palavras: {word_count}")
```

Saida esperada:
```
Media das notas: 7.9
Maior nota: 9.0
Nome formatado: Maria Da Silva
Numero de palavras: 6
```

### Quando o __init__.py e Necessário?

- **Python 3.3+:** Tecnicamente, o `__init__.py` não e mais obrigatório para pacotes simples (o Python reconhece "namespace packages" sem ele). Porém, **e uma boa prática sempre criar o arquivo**, mesmo que vazio, para deixar claro que a pasta e um pacote.
- **Projetos profissionais:** Sempre usam `__init__.py` em todas as pastas de pacotes.

---

## Cuidados Importantes com Imports

### Evite import * (Importar Tudo)

Existe uma forma de importar **tudo** de um módulo usando o asterisco (`*`):

```python
# NAO RECOMENDADO — importa tudo do modulo math
# O asterisco (*) significa "tudo"
from math import *

# Funciona, mas voce nao sabe de onde veio cada funcao
print(sqrt(25))
print(pi)
```

Saida esperada:
```
5.0
3.141592653589793
```

**Por que evitar?** Quando você usa `import *`, todas as funções do módulo sao despejadas no seu programa. Se dois módulos tiverem funções com o mesmo nome, uma vai sobrescrever a outra sem aviso. Isso causa erros dificeis de encontrar.

**Regra:** Sempre importe apenas o que você precisa, ou importe o módulo inteiro com um nome claro.

### Onde Colocar os Imports

Os imports devem ficar **no inicio do arquivo**, antes de qualquer outro código. Isso e uma convencao do Python (PEP 8) que facilita a leitura:

```python
# CORRETO — imports no inicio do arquivo
# Primeiro: modulos da biblioteca padrao
import math
import random
from datetime import date

# Depois: modulos de terceiros (instalados com pip)
# (veremos isso no modulo 26)

# Por ultimo: modulos do seu proprio projeto
from utils.helpers import format_price

# Agora sim, o codigo do programa
# "result" = resultado
result = math.sqrt(64)
print(result)
```

Saida esperada:
```
8.0
```

### Nomes de Arquivos: Cuidado com Conflitos

Nunca nomeie seus arquivos com o mesmo nome de um módulo da biblioteca padrão. Por exemplo, se você criar um arquivo chamado `math.py` ou `random.py`, o Python vai importar o **seu** arquivo em vez do módulo oficial, causando erros.

**Nomes a evitar para seus arquivos:**
- `math.py`
- `random.py`
- `datetime.py`
- `os.py`
- `json.py`
- `csv.py`

**Dica:** Use nomes descritivos para seus arquivos, como `calculator.py`, `validators.py`, `helpers.py`, `utils.py`.

---

## Resumo

Neste módulo, você aprendeu como reutilizar código em Python usando módulos e imports:

| Conceito | O Que E | Exemplo |
|----------|---------|---------|
| Módulo | Um arquivo `.py` com funções e classes reutilizaveis | `calculator.py` |
| `import` | Importa o módulo inteiro | `import math` |
| `from...import` | Importa funções especificas | `from math import sqrt` |
| `import...as` | Importa com apelido | `import datetime as dt` |
| Biblioteca padrão | Módulos que ja vem com o Python | `math`, `random`, `datetime`, `os` |
| Pacote | Pasta com `__init__.py` contendo módulos | `utils/` |
| `__init__.py` | Arquivo que transforma pasta em pacote | `utils/__init__.py` |
| Importacao absoluta | Caminho completo desde a raiz | `from utils.helpers import func` |
| Importacao relativa | Caminho relativo com pontos | `from .helpers import func` |

Pontos importantes para lembrar:

- Imports ficam **no inicio do arquivo**
- Evite `from modulo import *` — importe apenas o que precisa
- Nunca nomeie seus arquivos com nomes de módulos da biblioteca padrão
- Para importar seus proprios arquivos, eles devem estar na mesma pasta ou em um pacote com `__init__.py`
- Prefira importacao **absoluta** para projetos simples

---

## Para Saber Mais

- [W3Schools — Módulos em Python](https://www.w3schools.com/python/python_modules.asp)
  _Aqui você encontra mais exemplos de como criar e usar módulos em Python, com explicacoes em ingles simples_
- [W3Schools — Módulo math](https://www.w3schools.com/python/module_math.asp)
  _Lista completa de funções do módulo math com exemplos praticos_
- [W3Schools — Módulo random](https://www.w3schools.com/python/module_random.asp)
  _Todas as funções do módulo random para gerar números aleatorios_
- [W3Schools — Módulo datetime](https://www.w3schools.com/python/python_datetime.asp)
  _Como trabalhar com datas e horarios em Python_
- [W3Schools — pip e Pacotes](https://www.w3schools.com/python/python_pip.asp)
  _Introducao ao gerenciador de pacotes pip (você aprendera mais no módulo 26)_
- [Documentação Oficial Python — Módulos](https://docs.python.org/pt-br/3/tutorial/modules.html)
  _Referencia completa sobre módulos e pacotes em Python, em portugues_
- [Documentação Oficial Python — Biblioteca Padrão](https://docs.python.org/pt-br/3/library/index.html)
  _Indice completo de todos os módulos da biblioteca padrão do Python_

---

## Perguntas Frequentes (FAQ)

**P: O que e um módulo em Python?**
R: Um módulo e simplesmente um arquivo Python (`.py`) que contem funções, classes e variáveis. Qualquer arquivo Python pode ser usado como módulo — basta importa-lo em outro arquivo. Pense em um módulo como um livro em uma biblioteca: ele contem informações organizadas sobre um assunto, e você pode consulta-lo quando precisar.

**P: Qual a diferença entre import e from...import?**
R: Com `import math`, você importa o módulo inteiro e precisa escrever `math.sqrt()` para usar uma função. Com `from math import sqrt`, você importa apenas a função `sqrt` e pode usa-la diretamente como `sqrt()`. A primeira forma e mais clara sobre a origem da função; a segunda e mais curta para escrever.

**P: Quando devo usar import...as?**
R: Use `import...as` quando o nome do módulo e longo e você quer um apelido mais curto. Por exemplo, `import datetime as dt` permite escrever `dt.date.today()` em vez de `datetime.date.today()`. Também e útil quando dois módulos tem nomes parecidos e você quer diferencia-los.

**P: O que e a biblioteca padrão do Python?**
R: A biblioteca padrão e uma coleção enorme de módulos que ja vem instalados com o Python. Você não precisa instalar nada extra para usa-los — basta importar. Ela inclui módulos para matemática (`math`), números aleatorios (`random`), datas (`datetime`), arquivos (`os`), JSON (`json`), e muitos outros.

**P: Preciso decorar todas as funções de todos os módulos?**
R: Não. Programadores profissionais consultam a documentação o tempo todo. O importante e saber que os módulos existem e como importa-los. Quando precisar de uma função específica, consulte a documentação oficial ou o W3Schools.

**P: Como sei quais funções um módulo tem?**
R: Você pode usar a função `dir(modulo)` para listar tudo que um módulo contem. Por exemplo, `import math` e depois `print(dir(math))` mostra todas as funções do módulo math. Também pode usar `help(math)` para ver a documentação completa.

**P: Posso importar um módulo dentro de uma função?**
R: Sim, e possível, mas não e recomendado. A convencao do Python (PEP 8) e colocar todos os imports no inicio do arquivo. Importar dentro de funções pode tornar o código mais difícil de entender e pode causar problemas de desempenho se a função for chamada muitas vezes.

**P: O que acontece se eu importar o mesmo módulo duas vezes?**
R: Nada de ruim. O Python e inteligente: ele carrega o módulo na primeira vez e, nas vezes seguintes, simplesmente reutiliza o que ja foi carregado. Não ha desperdicio de memória ou tempo.

**P: O que e um pacote em Python?**
R: Um pacote e uma pasta que contem módulos Python e um arquivo `__init__.py`. Enquanto um módulo e um único arquivo `.py`, um pacote e uma coleção de módulos organizados em uma pasta. Pense em um módulo como um livro e um pacote como uma estante com vários livros.

**P: O __init__.py precisa ter conteúdo?**
R: Não, ele pode estar completamente vazio. Sua simples existência ja e suficiente para transformar a pasta em um pacote Python. Porém, você pode colocar código nele para executar inicializacoes ou para facilitar imports.

**P: Qual a diferença entre importacao absoluta e relativa?**
R: Na importacao absoluta, você escreve o caminho completo do módulo a partir da raiz do projeto (por exemplo, `from utils.helpers import func`). Na importacao relativa, você usa pontos para indicar a posição relativa (por exemplo, `from .helpers import func`). Para iniciantes, a importacao absoluta e mais simples e recomendada.

**P: Por que não devo usar from módulo import *?**
R: Porque o asterisco (`*`) importa **tudo** do módulo para o seu programa. Se dois módulos tiverem funções com o mesmo nome, uma vai sobrescrever a outra sem aviso. Além disso, fica impossivel saber de onde cada função veio quando você le o código. Sempre importe apenas o que precisa.

**P: Posso criar um módulo com qualquer nome?**
R: Quase. O nome do arquivo deve seguir as regras de nomes de variáveis em Python: so pode conter letras, números e underscores, e não pode começar com número. Use snake_case (letras minusculas separadas por underscores). E muito importante **não usar nomes de módulos da biblioteca padrão** como `math.py`, `random.py` ou `os.py`.

**P: O que acontece se eu nomear meu arquivo de math.py?**
R: O Python vai importar o **seu** arquivo `math.py` em vez do módulo oficial `math` da biblioteca padrão. Isso causa erros confusos porque seu arquivo não tem as funções que você espera (como `sqrt`). Sempre use nomes descritivos e unicos para seus arquivos.

**P: Meus dois arquivos precisam estar na mesma pasta para o import funcionar?**
R: Para imports simples (como `import calculator`), sim, os arquivos precisam estar na mesma pasta. Para projetos maiores com pastas, você precisa criar pacotes com `__init__.py` e usar importacao absoluta ou relativa.

**P: E normal achar imports confusos no comeco?**
R: Sim, completamente normal. O sistema de imports do Python e um dos tópicos que mais confunde iniciantes. Com a prática, você vai se acostumar. Comece com imports simples (dois arquivos na mesma pasta) e va avancando aos poucos.

**P: O que e o módulo os e para que serve?**
R: O módulo `os` (operating system = sistema operacional) permite que seu programa Python interaja com o sistema de arquivos do computador. Com ele, você pode listar arquivos em uma pasta, verificar se um arquivo existe, criar pastas, e muito mais. E muito útil para programas que precisam trabalhar com arquivos e diretórios.

**P: Posso importar módulos que não sao da biblioteca padrão?**
R: Sim. Existem milhares de módulos criados pela comunidade Python que você pode instalar usando o `pip` (gerenciador de pacotes). Você aprendera sobre isso no módulo 26 (pip e Dependências). Exemplos populares incluem `requests` (para fazer requisicoes HTTP) e `fastapi` (para criar APIs).

**P: O que e o __name__ == "__main__"?**
R: Quando o Python executa um arquivo diretamente, ele define a variável especial `__name__` como `"__main__"`. Quando o arquivo e importado como módulo, `__name__` recebe o nome do módulo. O teste `if __name__ == "__main__":` permite que um arquivo funcione tanto como programa principal quanto como módulo importavel.

**P: Preciso me preocupar com a ordem dos imports?**
R: A PEP 8 (guia de estilo do Python) recomenda organizar os imports em tres grupos, nesta ordem: (1) módulos da biblioteca padrão, (2) módulos de terceiros (instalados com pip), (3) módulos do seu projeto. Dentro de cada grupo, organize em ordem alfabetica. Isso facilita a leitura do código.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a navegação.

[Ir para os Exercícios do Módulo 24 ->](24-módulos-imports-exercícios.md)

---

[<- Anterior: Exercícios Integradores](23-exercícios-integradores.md) | [Glossário](00-glossário.md) | [Próximo: Estruturação de Projetos ->](25-estruturação-projetos.md)
