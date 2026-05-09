# Exercícios — Módulo 17: Debugging Básico

[<- Voltar ao Módulo 17](17-debugging.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> Neste módulo, os exercícios sao diferentes: você recebe código com erros e precisa encontrar e corrigir. E como ser um detetive investigando pistas.
>
> 1. Leia o código com erro
> 2. Tente identificar o problema sem executar
> 3. Execute para ver a mensagem de erro
> 4. Corrija o erro
> 5. Consulte a resposta comentada

---

## Exercício 1 — Encontrar o SyntaxError — Nível: Básico
**Conceitos praticados:** leitura de erros, sintaxe

### Enunciado
O código abaixo tem um erro de sintaxe. Encontre e corrija.

```python
name = input("Seu nome: ")
print("Ola, " + name
```

### Dicas
- Olhe os parenteses — estão todos fechados?

### Proposta de Teste
- Apos correcao, digite `Ana` — Saida: `Ola, Ana`

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO: faltava fechar o parentese do print na linha 2
# O Python mostrou: SyntaxError: unexpected EOF while parsing
# "EOF" = End Of File = o Python chegou ao fim do arquivo sem encontrar o )

# CORRECAO: adicionamos o parentese de fechamento
# "name" = nome
name = input("Seu nome: ")
print("Ola, " + name)  # <-- parentese fechado corretamente
```

---

## Exercício 2 — Encontrar o NameError — Nível: Básico
**Conceitos praticados:** leitura de erros, nomes de variáveis

### Enunciado
O código abaixo tem um erro. Encontre e corrija.

```python
product_name = "Arroz"
product_price = 5.99
print(f"Produto: {product_name} - Preco: R$ {product_prce}")
```

### Dicas
- Compare os nomes das variáveis com cuidado — letra por letra

### Proposta de Teste
- Apos correcao — Saida: `Produto: Arroz - Preco: R$ 5.99`

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO: na linha 3, "product_prce" esta escrito errado (falta o "i")
# O Python mostrou: NameError: name 'product_prce' is not defined
# A variavel correta e "product_price" (com "i")

# CORRECAO: corrigimos a digitacao
# "product_name" = nome do produto, "product_price" = preco do produto
product_name = "Arroz"
product_price = 5.99
print(f"Produto: {product_name} - Preco: R$ {product_price}")  # <-- corrigido: price
```

---

## Exercício 3 — Encontrar o TypeError — Nível: Básico
**Conceitos praticados:** leitura de erros, tipos de dados

### Enunciado
O código abaixo tem um erro. Encontre e corrija.

```python
age = input("Sua idade: ")
next_year_age = age + 1
print(f"No proximo ano voce tera {next_year_age} anos")
```

### Dicas
- Lembre-se: input() retorna sempre string
- Você pode somar string com número?

### Proposta de Teste
- Digite `25` — Saida: `No proximo ano voce tera 26 anos`

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO: input() retorna string, e nao podemos somar string + int
# O Python mostrou: TypeError: can only concatenate str (not "int") to str
# Precisamos converter a idade para int antes de somar

# CORRECAO: adicionamos int() para converter
# "age" = idade — agora e int, nao str
age = int(input("Sua idade: "))  # <-- int() converte para numero
# "next_year_age" = idade no proximo ano
next_year_age = age + 1
print(f"No proximo ano voce tera {next_year_age} anos")
```

---

## Exercício 4 — Encontrar o ValueError — Nível: Básico
**Conceitos praticados:** leitura de erros, conversão de tipos

### Enunciado
O código abaixo funciona se o usuario digitar um número, mas da erro se digitar texto. Identifique qual erro aparece e explique por que.

```python
number = int(input("Digite um numero: "))
print(f"O dobro e {number * 2}")
```

### Dicas
- Execute e digite "abc" em vez de um número
- Que tipo de erro aparece?

### Proposta de Teste
- Digite `abc` — Deve aparecer `ValueError`
- Digite `5` — Saida: `O dobro e 10`

### Resposta Comentada

> **Importante:** Execute e observe o erro primeiro!

```python
# Quando o usuario digita "abc", o Python tenta fazer int("abc")
# Isso gera: ValueError: invalid literal for int() with base 10: 'abc'
# Traducao: "abc" nao e um valor valido para converter em numero inteiro

# O codigo em si nao tem erro de programacao — o problema e que
# nao estamos tratando a possibilidade do usuario digitar algo invalido
# No modulo 18, vamos aprender a usar try/except para tratar isso

# Por enquanto, a "correcao" e informar ao usuario o que digitar:
# "number" = numero
number = int(input("Digite um numero inteiro (apenas digitos): "))
# "double" = dobro
double = number * 2
print(f"O dobro e {double}")
```

---

## Exercício 5 — Encontrar o IndexError — Nível: Intermediario
**Conceitos praticados:** leitura de erros, indices, listas

### Enunciado
O código abaixo tem um erro. Encontre e corrija.

```python
colors = ["vermelho", "azul", "verde"]
print(f"Primeira cor: {colors[0]}")
print(f"Segunda cor: {colors[1]}")
print(f"Terceira cor: {colors[2]}")
print(f"Quarta cor: {colors[3]}")
```

### Dicas
- A lista tem 3 itens. Quais posicoes existem?
- Lembre-se: a contagem comeca do zero

### Proposta de Teste
- Apos correcao — Deve exibir apenas as 3 cores sem erro

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO: a lista tem 3 itens nas posicoes 0, 1 e 2
# colors[3] tenta acessar a posicao 3, que nao existe
# O Python mostrou: IndexError: list index out of range

# CORRECAO: removemos a linha que acessa a posicao inexistente
# "colors" = cores
colors = ["vermelho", "azul", "verde"]
print(f"Primeira cor: {colors[0]}")   # posicao 0 = vermelho
print(f"Segunda cor: {colors[1]}")    # posicao 1 = azul
print(f"Terceira cor: {colors[2]}")   # posicao 2 = verde
# A linha colors[3] foi removida porque a posicao 3 nao existe
```

---

## Exercício 6 — Erro de Lógica (Sem Mensagem) — Nível: Intermediario
**Conceitos praticados:** debugging com print, erro de lógica

### Enunciado
O programa abaixo deveria calcular a media de 3 notas, mas o resultado esta errado. Use print() de depuracao para encontrar o problema.

```python
grade_1 = float(input("Nota 1: "))
grade_2 = float(input("Nota 2: "))
grade_3 = float(input("Nota 3: "))
average = grade_1 + grade_2 + grade_3 / 3
print(f"Media: {average}")
```

### Dicas
- Adicione prints para ver os valores intermediarios
- Preste atenção na precedencia dos operadores

### Proposta de Teste
- Notas: `6, 8, 10` — Media esperada: `8.0`, mas o programa mostra `17.33...`

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO DE LOGICA: a divisao tem precedencia sobre a soma
# Na expressao: grade_1 + grade_2 + grade_3 / 3
# O Python calcula: grade_3 / 3 primeiro (10/3 = 3.33)
# Depois soma: 6 + 8 + 3.33 = 17.33
# O correto seria: (grade_1 + grade_2 + grade_3) / 3

# Usando print de depuracao para investigar:
# "grade" = nota
grade_1 = float(input("Nota 1: "))
grade_2 = float(input("Nota 2: "))
grade_3 = float(input("Nota 3: "))

# DEBUG: vamos ver o que acontece passo a passo
print(f"DEBUG - grade_3 / 3 = {grade_3 / 3}")  # mostra que so divide a terceira nota
print(f"DEBUG - soma sem parenteses = {grade_1 + grade_2 + grade_3 / 3}")

# CORRECAO: adicionamos parenteses para somar ANTES de dividir
# "average" = media
average = (grade_1 + grade_2 + grade_3) / 3  # <-- parenteses corrigem a precedencia
print(f"Media: {average}")
```

---

## Exercício 7 — Multiplos Erros — Nível: Intermediario
**Conceitos praticados:** debugging sistematico, multiplos tipos de erro

### Enunciado
O código abaixo tem 3 erros. Encontre e corrija todos.

```python
# Programa que calcula o preco total com desconto
prce = float(input("Preco: "))
quantity = int(input("Quantidade: ")
discount = 10

total = prce * quantity
total_with_discount = total - (total * discount / 100
print(f"Total: R$ {total_with_discount}")
```

### Dicas
- Execute o programa e corrija um erro por vez
- Apos corrigir um, execute novamente para encontrar o próximo

### Proposta de Teste
- Preco: `100`, Quantidade: `2` — Total com desconto: `180.0`

### Resposta Comentada

> **Importante:** Tente encontrar todos os erros sozinho!

```python
# ERRO 1 (linha 2): variavel "prce" — falta o "i" (deveria ser "price")
#   Isso nao gera erro imediato, mas causa NameError quando usamos "price" depois
#   Na verdade, o codigo usa "prce" consistentemente, entao funciona mas o nome esta errado

# ERRO 2 (linha 3): falta fechar o parentese do input
#   SyntaxError: unexpected EOF while parsing

# ERRO 3 (linha 6): falta fechar o parentese da expressao
#   SyntaxError: unexpected EOF while parsing

# CORRECAO COMPLETA:
# "price" = preco (corrigido o nome da variavel)
price = float(input("Preco: "))
# "quantity" = quantidade (corrigido o parentese)
quantity = int(input("Quantidade: "))
# "discount" = desconto (em porcentagem)
discount = 10

# "total" = total sem desconto
total = price * quantity
# "total_with_discount" = total com desconto (corrigido o parentese)
total_with_discount = total - (total * discount / 100)
print(f"Total: R$ {total_with_discount}")
```

---

## Exercício 8 — Debug de Função — Nível: Intermediario
**Conceitos praticados:** debugging de funções, escopo

### Enunciado
A função abaixo deveria retornar o maior de dois números, mas sempre retorna o primeiro. Encontre o erro.

```python
def find_larger(a, b):
    if a > b:
        result = a
    if b > a:
        result = b
    return result

print(find_larger(5, 10))
print(find_larger(10, 5))
print(find_larger(7, 7))
```

### Dicas
- O que acontece quando a == b?
- Use print de depuracao dentro da função

### Proposta de Teste
- `find_larger(5, 10)` — Retorno: `10`
- `find_larger(10, 5)` — Retorno: `10`
- `find_larger(7, 7)` — Deve retornar `7` sem erro

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO: quando a == b, nenhum if e verdadeiro e "result" nunca e criada
# Isso gera: UnboundLocalError: local variable 'result' referenced before assignment
# Alem disso, usar dois if separados em vez de if/else pode causar problemas

# CORRECAO: usar if/elif/else para cobrir todos os casos
# "find_larger" = encontrar o maior
def find_larger(a, b):
    # Usamos if/elif/else para garantir que result sempre recebe um valor
    if a > b:
        # "result" = resultado — a e maior
        result = a
    elif b > a:
        # b e maior
        result = b
    else:
        # a == b — sao iguais, retornamos qualquer um
        result = a
    return result

# Testamos
print(find_larger(5, 10))   # 10
print(find_larger(10, 5))   # 10
print(find_larger(7, 7))    # 7
```

---

## Exercício 9 — Debug de Loop — Nível: Avancado
**Conceitos praticados:** debugging de loops, lógica de acumulador

### Enunciado
O programa abaixo deveria calcular o fatorial de um número, mas o resultado esta errado. Encontre o erro usando print de depuracao.

```python
def calculate_factorial(n):
    result = 0
    for i in range(1, n + 1):
        result *= i
    return result

print(f"Fatorial de 5: {calculate_factorial(5)}")
```

### Dicas
- Adicione print dentro do loop para ver o valor de result a cada iteração
- Qual deveria ser o valor inicial de result para multiplicacao?

### Proposta de Teste
- `calculate_factorial(5)` — Esperado: `120`, mas retorna `0`

### Resposta Comentada

> **Importante:** Tente encontrar o erro sozinho primeiro!

```python
# ERRO: result comeca em 0, e qualquer numero multiplicado por 0 e 0
# Na primeira iteracao: 0 * 1 = 0. Na segunda: 0 * 2 = 0. Sempre 0.
# Para multiplicacao, o acumulador deve comecar em 1, nao em 0

# CORRECAO: mudar o valor inicial de result para 1
# "calculate_factorial" = calcular fatorial
def calculate_factorial(n):
    # "result" = resultado — comeca em 1 (nao 0!) porque estamos multiplicando
    result = 1  # <-- CORRECAO: era 0, agora e 1
    for i in range(1, n + 1):
        # "i" = cada numero de 1 ate n
        result *= i  # result = result * i
        # DEBUG (remover depois): print(f"  i={i}, result={result}")
    return result

print(f"Fatorial de 5: {calculate_factorial(5)}")  # 120
print(f"Fatorial de 0: {calculate_factorial(0)}")  # 1
```

---

## Exercício 10 — Debug Completo — Nível: Avancado
**Conceitos praticados:** debugging sistematico, multiplos erros, lógica

### Enunciado
O programa abaixo e uma calculadora de notas com 4 erros (sintaxe, tipo, lógica e nome). Encontre e corrija todos.

```python
def calculate_average(grades)
    total = 0
    for grade in grades:
        total = total + grade
    average = total / len(grade)
    return average

student_grades = [7, 8, "9", 6]
result = calculate_average(student_grades)
print(f"Media: {reslt}")
```

### Dicas
- Execute e corrija um erro por vez
- Erro 1: sintaxe. Erro 2: tipo. Erro 3: nome de variável. Erro 4: nome de variável

### Proposta de Teste
- Apos correcao — Media: `7.5`

### Resposta Comentada

> **Importante:** Tente encontrar todos os erros sozinho!

```python
# ERRO 1 (linha 1): faltam os dois-pontos (:) no final do def
#   SyntaxError: expected ':'

# ERRO 2 (linha 8): "9" e string, nao int — causa TypeError na soma
#   TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ERRO 3 (linha 5): len(grade) deveria ser len(grades) — grade e a variavel do loop
#   Isso usaria o ultimo valor de grade (um numero), nao a lista

# ERRO 4 (linha 10): "reslt" deveria ser "result"
#   NameError: name 'reslt' is not defined

# CORRECAO COMPLETA:
# "calculate_average" = calcular media
# "grades" = notas (lista de notas)
def calculate_average(grades):  # <-- CORRECAO 1: adicionados os dois-pontos
    # "total" = total (acumulador)
    total = 0
    for grade in grades:
        # "grade" = cada nota individual
        total = total + grade
    # "average" = media
    average = total / len(grades)  # <-- CORRECAO 3: grades (lista), nao grade (variavel do loop)
    return average

# "student_grades" = notas do aluno
student_grades = [7, 8, 9, 6]  # <-- CORRECAO 2: "9" mudado para 9 (int, nao str)
# "result" = resultado
result = calculate_average(student_grades)
print(f"Media: {result}")  # <-- CORRECAO 4: "reslt" corrigido para "result"
```

---

[<- Voltar ao Módulo 17](17-debugging.md) | [Glossário](00-glossario.md)
