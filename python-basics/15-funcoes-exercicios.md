# Exercícios — Módulo 15: Funções

[<- Voltar ao Módulo 15](15-funções.md) | [Glossário](00-glossário.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-15/` e execute com `python3 nome_do_arquivo.py`.
>
> Este e um módulo complexo. Os exercícios estão em ordem crescente de dificuldade.

---

## Exercício 1 — Função de Saudacao — Nível: Básico

### Enunciado
Crie uma função `greet` que receba um nome e exiba "Ola, [nome]!".

### Dicas
- Use `def greet(name):` para definir
- Use f-string para formatar a mensagem
- Chame a função com diferentes nomes

### Proposta de Teste
- **Caso básico:** `greet("Ana")` — Saida: `Ola, Ana!`
- **Caso de borda:** `greet("")` — Saida: `Ola, !` (nome vazio)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao greet (saudar)
# "name" = nome — parametro que recebe o nome da pessoa
def greet(name):
    # Exibimos a saudacao usando f-string
    # {name} e substituido pelo valor do parametro
    print(f"Ola, {name}!")

# Chamamos a funcao com diferentes argumentos
greet("Ana")
greet("Carlos")
greet("Maria")
```

---

## Exercício 2 — Função que Retorna o Dobro — Nível: Básico

### Enunciado
Crie uma função `calculate_double` que receba um número e retorne o dobro dele.

### Dicas
- Use `return` para devolver o resultado
- Guarde o resultado em uma variável ao chamar

### Proposta de Teste
- **Caso básico:** `calculate_double(5)` — Retorno: `10`
- **Caso de borda:** `calculate_double(0)` — Retorno: `0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao calculate_double (calcular dobro)
# "number" = numero — o valor que queremos dobrar
def calculate_double(number):
    # Calculamos o dobro multiplicando por 2
    # "result" = resultado
    result = number * 2
    # return devolve o resultado para quem chamou a funcao
    return result

# Chamamos a funcao e guardamos o resultado
# "my_result" = meu resultado
my_result = calculate_double(5)
print(f"O dobro de 5 e {my_result}")

# Podemos usar diretamente no print
print(f"O dobro de 12 e {calculate_double(12)}")
```

---

## Exercício 3 — Soma de Dois Números — Nível: Básico

### Enunciado
Crie uma função `add` que receba dois números e retorne a soma.

### Dicas
- Dois parametros: `def add(a, b):`
- Retorne `a + b`

### Proposta de Teste
- **Caso básico:** `add(10, 5)` — Retorno: `15`
- **Caso de borda:** `add(-3, 3)` — Retorno: `0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao add (somar)
# "number_a" = primeiro numero, "number_b" = segundo numero
def add(number_a, number_b):
    # Somamos os dois numeros e retornamos o resultado
    # return devolve a soma para quem chamou
    return number_a + number_b

# Testamos a funcao
print(f"10 + 5 = {add(10, 5)}")
print(f"-3 + 3 = {add(-3, 3)}")
print(f"0.5 + 0.5 = {add(0.5, 0.5)}")
```

---

## Exercício 4 — Verificar Par ou Impar — Nível: Básico

### Enunciado
Crie uma função `is_even` que receba um número e retorne `True` se for par ou `False` se for impar.

### Dicas
- Use `numero % 2 == 0` para verificar se e par
- Retorne True ou False

### Proposta de Teste
- **Caso básico:** `is_even(8)` — Retorno: `True`
- **Caso de borda:** `is_even(7)` — Retorno: `False`
- **Caso de borda:** `is_even(0)` — Retorno: `True`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao is_even (e par)
# "number" = numero
def is_even(number):
    # Verificamos se o resto da divisao por 2 e zero
    # Se for zero, o numero e par (divisivel por 2)
    # A expressao number % 2 == 0 ja retorna True ou False
    return number % 2 == 0

# Testamos a funcao
print(f"8 e par? {is_even(8)}")
print(f"7 e par? {is_even(7)}")
print(f"0 e par? {is_even(0)}")
```

---

## Exercício 5 — Função com Valor Padrão — Nível: Básico

### Enunciado
Crie uma função `greet_with_title` que receba um nome e um título (com valor padrão "Sr./Sra."). Exiba a saudacao com o título.

### Dicas
- Use valor padrão: `def funcao(nome, titulo="Sr./Sra."):`
- Chame com e sem o segundo argumento

### Proposta de Teste
- **Caso básico:** `greet_with_title("Maria")` — Saida: `Ola, Sr./Sra. Maria!`
- **Caso de borda:** `greet_with_title("Carlos", "Dr.")` — Saida: `Ola, Dr. Carlos!`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao com valor padrao no segundo parametro
# "name" = nome, "title" = titulo
# Se title nao for passado, usa "Sr./Sra." como padrao
def greet_with_title(name, title="Sr./Sra."):
    # Exibimos a saudacao com titulo e nome
    print(f"Ola, {title} {name}!")

# Chamando sem o titulo — usa o padrao
greet_with_title("Maria")

# Chamando com titulo especifico
greet_with_title("Carlos", "Dr.")
greet_with_title("Ana", "Profa.")
```

---

## Exercício 6 — Calculadora de Area do Retangulo — Nível: Intermediario

### Enunciado
Crie uma função `calculate_rectangle_area` que receba largura e comprimento e retorne a area. (Area do retangulo = largura multiplicada pelo comprimento.)

### Dicas
- Dois parametros: largura e comprimento
- Retorne o resultado da multiplicacao

### Proposta de Teste
- **Caso básico:** `calculate_rectangle_area(5, 10)` — Retorno: `50`
- **Caso de borda:** `calculate_rectangle_area(0, 10)` — Retorno: `0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao calculate_rectangle_area (calcular area do retangulo)
# "width" = largura, "length" = comprimento
def calculate_rectangle_area(width, length):
    # Area = largura x comprimento
    # "area" = area
    area = width * length
    # Retornamos o resultado
    return area

# Testamos a funcao
# "result" = resultado
result = calculate_rectangle_area(5, 10)
print(f"Area de 5 x 10: {result}")
print(f"Area de 3.5 x 7: {calculate_rectangle_area(3.5, 7)}")
```

---

## Exercício 7 — Função de Validação de Nota — Nível: Intermediario

### Enunciado
Crie uma função `is_valid_grade` que receba uma nota e retorne `True` se estiver entre 0 e 10, ou `False` caso contrario.

### Dicas
- Verifique se a nota e >= 0 e <= 10
- Retorne True ou False

### Proposta de Teste
- **Caso básico:** `is_valid_grade(7.5)` — Retorno: `True`
- **Caso de borda:** `is_valid_grade(-1)` — Retorno: `False`
- **Caso de borda:** `is_valid_grade(11)` — Retorno: `False`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao is_valid_grade (e nota valida)
# "grade" = nota
def is_valid_grade(grade):
    # Verificamos se a nota esta no intervalo valido (0 a 10)
    # A expressao retorna True se ambas as condicoes forem verdadeiras
    return grade >= 0 and grade <= 10

# Testamos a funcao
print(f"7.5 e valida? {is_valid_grade(7.5)}")
print(f"-1 e valida? {is_valid_grade(-1)}")
print(f"11 e valida? {is_valid_grade(11)}")
print(f"0 e valida? {is_valid_grade(0)}")
print(f"10 e valida? {is_valid_grade(10)}")
```

---

## Exercício 8 — Função de Desconto — Nível: Intermediario

### Enunciado
Crie uma função `apply_discount` que receba um preco e uma porcentagem de desconto (padrão 10%) e retorne o preco com desconto aplicado.

### Dicas
- Use valor padrão para a porcentagem
- Calcule o desconto e subtraia do preco

### Proposta de Teste
- **Caso básico:** `apply_discount(100, 20)` — Retorno: `80.0`
- **Caso de borda:** `apply_discount(100)` — Retorno: `90.0` (usa padrão 10%)
- **Caso de borda:** `apply_discount(50, 0)` — Retorno: `50.0` (sem desconto)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao apply_discount (aplicar desconto)
# "price" = preco, "discount_percent" = porcentagem de desconto (padrao: 10)
def apply_discount(price, discount_percent=10):
    # Calculamos o valor do desconto
    # "discount_value" = valor do desconto
    # Porcentagem: preco * (porcentagem / 100)
    discount_value = price * (discount_percent / 100)
    # Subtraimos o desconto do preco original
    # "final_price" = preco final
    final_price = price - discount_value
    # Retornamos o preco final
    return final_price

# Testamos a funcao
print(f"R$ 100 com 20% desconto: R$ {apply_discount(100, 20)}")
print(f"R$ 100 com desconto padrao: R$ {apply_discount(100)}")
print(f"R$ 50 sem desconto: R$ {apply_discount(50, 0)}")
```

---

## Exercício 9 — Conversor de Temperatura — Nível: Intermediario

### Enunciado
Crie duas funções: `celsius_to_fahrenheit` (Celsius para Fahrenheit) e `fahrenheit_to_celsius` (Fahrenheit para Celsius). Formulas: F = C * 1.8 + 32 e C = (F - 32) / 1.8.

### Dicas
- Cada função recebe um parametro e retorna o resultado
- Use as formulas fornecidas

### Proposta de Teste
- **Caso básico:** `celsius_to_fahrenheit(100)` — Retorno: `212.0`
- **Caso básico:** `fahrenheit_to_celsius(32)` — Retorno: `0.0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que converte Celsius para Fahrenheit
# "celsius" = temperatura em Celsius
def celsius_to_fahrenheit(celsius):
    # Formula: F = C * 1.8 + 32
    # "fahrenheit" = temperatura em Fahrenheit
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

# Funcao que converte Fahrenheit para Celsius
# "fahrenheit" = temperatura em Fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    # Formula: C = (F - 32) / 1.8
    # "celsius" = temperatura em Celsius
    celsius = (fahrenheit - 32) / 1.8
    return celsius

# Testamos as funcoes
print(f"100 C = {celsius_to_fahrenheit(100)} F")
print(f"32 F = {fahrenheit_to_celsius(32)} C")
print(f"0 C = {celsius_to_fahrenheit(0)} F")
print(f"212 F = {fahrenheit_to_celsius(212)} C")
```

---

## Exercício 10 — Função que Conta Vogais — Nível: Intermediario

### Enunciado
Crie uma função `count_vowels` que receba um texto e retorne a quantidade de vogais.

### Dicas
- Percorra cada caractere com for
- Verifique se e vogal com `if char in "aeiou"`
- Use `.lower()` para ignorar maiusculas

### Proposta de Teste
- **Caso básico:** `count_vowels("Python")` — Retorno: `1` (apenas o 'o')
- **Caso de borda:** `count_vowels("aeiou")` — Retorno: `5`
- **Caso de borda:** `count_vowels("xyz")` — Retorno: `0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao count_vowels (contar vogais)
# "text" = texto
def count_vowels(text):
    # Contador de vogais — comeca em 0
    # "count" = contagem
    count = 0
    # Percorremos cada caractere do texto em minusculas
    for char in text.lower():
        # "char" = caractere
        # Verificamos se o caractere e uma vogal
        if char in "aeiou":
            # Se for vogal, incrementamos o contador
            count += 1
    # Retornamos a contagem total
    return count

# Testamos a funcao
print(f"Vogais em 'Python': {count_vowels('Python')}")
print(f"Vogais em 'aeiou': {count_vowels('aeiou')}")
print(f"Vogais em 'xyz': {count_vowels('xyz')}")
print(f"Vogais em 'Programacao': {count_vowels('Programacao')}")
```

---

## Exercício 11 — Função de Máximo — Nível: Avancado

### Enunciado
Crie uma função `find_maximum` que receba tres números e retorne o maior deles. Não use a função `max()` do Python — implemente a lógica você mesmo.

### Dicas
- Compare os tres números usando if/elif/else
- Retorne o maior encontrado

### Proposta de Teste
- **Caso básico:** `find_maximum(5, 9, 3)` — Retorno: `9`
- **Caso de borda:** `find_maximum(7, 7, 7)` — Retorno: `7`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao find_maximum (encontrar maximo)
# "a", "b", "c" = os tres numeros a comparar
def find_maximum(a, b, c):
    # Comecamos assumindo que "a" e o maior
    # "largest" = maior
    largest = a
    # Se "b" for maior que o atual maior, atualizamos
    if b > largest:
        largest = b
    # Se "c" for maior que o atual maior, atualizamos
    if c > largest:
        largest = c
    # Retornamos o maior encontrado
    return largest

# Testamos a funcao
print(f"Maior entre 5, 9, 3: {find_maximum(5, 9, 3)}")
print(f"Maior entre 7, 7, 7: {find_maximum(7, 7, 7)}")
print(f"Maior entre -1, -5, -2: {find_maximum(-1, -5, -2)}")
```

---

## Exercício 12 — Calculadora Completa com Funções — Nível: Avancado

### Enunciado
Crie funções separadas para cada operação (add, subtract, multiply, divide) e uma função `calculator` que peca os dados ao usuario e chame a função correta.

### Dicas
- Cada operação e uma função que recebe dois números e retorna o resultado
- A função calculator usa if/elif para escolher qual função chamar

### Proposta de Teste
- **Caso básico:** Operação: `+`, Números: `10` e `3` — Saida: `13.0`
- **Caso de borda:** Operação: `/`, Números: `10` e `0` — Saida: mensagem de erro

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcoes para cada operacao
# "add" = somar
def add(a, b):
    return a + b

# "subtract" = subtrair
def subtract(a, b):
    return a - b

# "multiply" = multiplicar
def multiply(a, b):
    return a * b

# "divide" = dividir
def divide(a, b):
    # Verificamos se o divisor nao e zero
    if b != 0:
        return a / b
    else:
        # Retornamos None para indicar erro
        return None

# Funcao principal da calculadora
# "calculator" = calculadora
def calculator():
    # Pedimos os dados ao usuario
    num_a = float(input("Primeiro numero: "))
    num_b = float(input("Segundo numero: "))
    op = input("Operacao (+, -, *, /): ")

    # Chamamos a funcao correta baseado na operacao
    if op == "+":
        result = add(num_a, num_b)
    elif op == "-":
        result = subtract(num_a, num_b)
    elif op == "*":
        result = multiply(num_a, num_b)
    elif op == "/":
        result = divide(num_a, num_b)
        if result is None:
            print("Erro: divisao por zero!")
            return  # Encerra a funcao sem exibir resultado
    else:
        print("Operacao invalida!")
        return

    # Exibimos o resultado
    print(f"{num_a} {op} {num_b} = {result}")

# Chamamos a calculadora
calculator()
```

---

## Exercício 13 — Função de Senha Forte — Nível: Avancado

### Enunciado
Crie uma função `is_strong_password` que receba uma senha e retorne `True` se ela tiver pelo menos 8 caracteres e conter pelo menos um número. Caso contrario, retorne `False`.

### Dicas
- Use `len()` para verificar o tamanho
- Percorra cada caractere e verifique se e digito com `.isdigit()`

### Proposta de Teste
- **Caso básico:** `is_strong_password("abc12345")` — Retorno: `True`
- **Caso de borda:** `is_strong_password("abc")` — Retorno: `False` (muito curta)
- **Caso de borda:** `is_strong_password("abcdefgh")` — Retorno: `False` (sem número)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao is_strong_password (e senha forte)
# "password" = senha
def is_strong_password(password):
    # Verificamos se tem pelo menos 8 caracteres
    if len(password) < 8:
        return False

    # Verificamos se contem pelo menos um numero
    # "has_number" = tem numero
    has_number = False
    for char in password:
        # "char" = caractere
        # .isdigit() retorna True se o caractere for um digito (0-9)
        if char.isdigit():
            has_number = True
            break  # Encontrou um numero, nao precisa continuar

    # Retornamos True apenas se tiver numero
    return has_number

# Testamos a funcao
print(f"'abc12345' e forte? {is_strong_password('abc12345')}")
print(f"'abc' e forte? {is_strong_password('abc')}")
print(f"'abcdefgh' e forte? {is_strong_password('abcdefgh')}")
print(f"'12345678' e forte? {is_strong_password('12345678')}")
```

---

## Exercício 14 — Função de Fatorial — Nível: Avancado

### Enunciado
Crie uma função `calculate_factorial` que receba um número inteiro positivo e retorne o fatorial dele. (Fatorial de N = N x (N-1) x (N-2) x ... x 1. Fatorial de 0 = 1.)

### Dicas
- Use um loop for de 1 a N
- Use um acumulador que comeca em 1

### Proposta de Teste
- **Caso básico:** `calculate_factorial(5)` — Retorno: `120`
- **Caso de borda:** `calculate_factorial(0)` — Retorno: `1`
- **Caso de borda:** `calculate_factorial(1)` — Retorno: `1`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a funcao calculate_factorial (calcular fatorial)
# "n" = o numero cujo fatorial queremos calcular
def calculate_factorial(n):
    # O acumulador comeca em 1 (porque estamos multiplicando)
    # "result" = resultado
    result = 1
    # Multiplicamos por cada numero de 1 ate n
    for i in range(1, n + 1):
        # "i" = cada numero de 1 ate n
        result *= i  # result = result * i
    # Retornamos o fatorial calculado
    return result

# Testamos a funcao
print(f"Fatorial de 5: {calculate_factorial(5)}")
print(f"Fatorial de 0: {calculate_factorial(0)}")
print(f"Fatorial de 1: {calculate_factorial(1)}")
print(f"Fatorial de 10: {calculate_factorial(10)}")
```

---

## Exercício 15 — Sistema de Cadastro com Funções — Nível: Avancado

### Enunciado
Crie um programa com funções separadas para: ler dados do usuario (`read_user_data`), validar a idade (`validate_age`), e exibir o cadastro (`display_registration`). A função principal coordena as chamadas.

### Dicas
- `read_user_data` retorna nome, idade e cidade
- `validate_age` recebe idade e retorna True/False
- `display_registration` recebe os dados e exibe formatado

### Proposta de Teste
- **Caso básico:** Nome: `Ana`, Idade: `25`, Cidade: `SP` — Exibe cadastro completo
- **Caso de borda:** Idade: `-5` — Exibe mensagem de idade inválida

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que le os dados do usuario
# "read_user_data" = ler dados do usuario
def read_user_data():
    # Pedimos os dados
    # "name" = nome, "age" = idade, "city" = cidade
    name = input("Nome: ")
    age = int(input("Idade: "))
    city = input("Cidade: ")
    # Retornamos os tres valores (Python permite retornar multiplos valores)
    return name, age, city

# Funcao que valida a idade
# "validate_age" = validar idade
def validate_age(age):
    # Idade valida: entre 0 e 150
    return age >= 0 and age <= 150

# Funcao que exibe o cadastro formatado
# "display_registration" = exibir cadastro
def display_registration(name, age, city):
    print("\n=== Cadastro ===")
    print(f"Nome: {name}")
    print(f"Idade: {age} anos")
    print(f"Cidade: {city}")
    print("================")

# Funcao principal que coordena tudo
# "main" = principal — convencao para a funcao principal do programa
def main():
    print("--- Sistema de Cadastro ---\n")

    # Lemos os dados usando a funcao read_user_data
    # Recebemos os tres valores retornados
    name, age, city = read_user_data()

    # Validamos a idade usando a funcao validate_age
    if validate_age(age):
        # Idade valida — exibimos o cadastro
        display_registration(name, age, city)
    else:
        # Idade invalida
        print(f"\nIdade {age} e invalida! Digite um valor entre 0 e 150.")

# Chamamos a funcao principal
main()
```

---

[<- Voltar ao Módulo 15](15-funções.md) | [Glossário](00-glossário.md)
