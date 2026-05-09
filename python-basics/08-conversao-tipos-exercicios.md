# Exercícios — Módulo 08: Conversão entre Tipos de Dados

[<- Voltar ao Módulo 08](08-conversão-tipos.md) | [Glossário](00-glossário.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve seu código em um arquivo `.py` na pasta `~/meus-projetos/python-curso/modulo-08/`, abra o terminal, navegue ate a pasta e execute com `python3 nome_do_arquivo.py`.

---

## Exercício 1 — Convertendo Texto para Inteiro — Nível: Básico

### Enunciado
Crie um programa que peca um número inteiro ao usuario, converta para int e exiba o dobro desse número.

### Dicas
- Use `input()` para ler o valor (lembre-se: retorna texto)
- Use `int()` para converter o texto em número
- Multiplique por 2 para obter o dobro

### Proposta de Teste
- **Caso básico:** Digite `5` — saida deve ser `O dobro de 5 e 10`
- **Caso de borda:** Digite `0` — saida deve ser `O dobro de 0 e 0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos um numero ao usuario e convertemos para inteiro
# "number" = numero
# input() retorna texto, int() converte para numero inteiro
number = int(input("Digite um numero inteiro: "))

# Calculamos o dobro multiplicando por 2
# "double" = dobro
double = number * 2

# Exibimos o resultado
print("O dobro de", number, "e", double)
```

---

## Exercício 2 — Convertendo Texto para Decimal — Nível: Básico

### Enunciado
Crie um programa que peca o preco de um produto e calcule o preco com 10% de acrescimo. (Acrescimo de 10% significa somar 10% do valor original ao preco. Para calcular 10% de um valor, multiplique por 0.10.)

### Dicas
- Use `float()` para converter o preco (tem casas decimais)
- Calcule o acrescimo: preco multiplicado por 0.10
- Some o acrescimo ao preco original

### Proposta de Teste
- **Caso básico:** Preco: `100.00` — Acrescimo: 10.0, Preco final: 110.0
- **Caso de borda:** Preco: `0` — Acrescimo: 0.0, Preco final: 0.0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o preco e convertemos para float (numero decimal)
# "price" = preco
price = float(input("Preco do produto: R$ "))

# Calculamos o acrescimo de 10%
# "surcharge" = acrescimo
# Multiplicar por 0.10 e o mesmo que calcular 10 de cada 100
surcharge = price * 0.10

# Calculamos o preco final somando o acrescimo
# "final_price" = preco final
final_price = price + surcharge

# Exibimos os resultados
print("Preco original: R$", price)
print("Acrescimo (10%): R$", surcharge)
print("Preco final: R$", final_price)
```

---

## Exercício 3 — Verificando o Tipo Antes e Depois — Nível: Básico

### Enunciado
Crie um programa que peca um número ao usuario, mostre o tipo do valor recebido (antes da conversão), converta para int e mostre o tipo novamente (depois da conversão).

### Dicas
- Guarde o valor do input() em uma variável antes de converter
- Use `type()` para mostrar o tipo
- Depois converta e mostre o tipo novamente

### Proposta de Teste
- **Caso básico:** Digite `42` — deve mostrar tipo `<class 'str'>` antes e `<class 'int'>` depois

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Lemos o valor do usuario SEM converter
# "raw_value" = valor bruto (como veio do input)
raw_value = input("Digite um numero: ")

# Mostramos o valor e o tipo ANTES da conversao
# Neste ponto, raw_value e uma string (texto)
print("Antes da conversao:")
print("Valor:", raw_value, "- Tipo:", type(raw_value))

# Convertemos para inteiro
# "converted_value" = valor convertido
converted_value = int(raw_value)

# Mostramos o valor e o tipo DEPOIS da conversao
# Agora converted_value e um int (numero inteiro)
print("\nDepois da conversao:")
print("Valor:", converted_value, "- Tipo:", type(converted_value))
```

---

## Exercício 4 — Somando Valores do Usuario — Nível: Básico

### Enunciado
Crie um programa que peca tres números decimais ao usuario e exiba a soma deles.

### Dicas
- Use `float()` para converter cada valor
- Some os tres valores
- Exiba o resultado

### Proposta de Teste
- **Caso básico:** Números: `1.5`, `2.3`, `3.2` — Soma: 7.0
- **Caso de borda:** Números: `0`, `0`, `0` — Soma: 0.0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos tres numeros e convertemos cada um para float
# "number_1" = primeiro numero, "number_2" = segundo, "number_3" = terceiro
number_1 = float(input("Primeiro numero: "))
number_2 = float(input("Segundo numero: "))
number_3 = float(input("Terceiro numero: "))

# Calculamos a soma dos tres numeros
# "total" = total (soma)
total = number_1 + number_2 + number_3

# Exibimos o resultado
print("Soma:", total)
```

---

## Exercício 5 — Divisao com Resultado Inteiro e Decimal — Nível: Intermediario

### Enunciado
Crie um programa que peca dois números inteiros e exiba o resultado da divisao de duas formas: como número decimal (divisao normal) e como número inteiro (apenas a parte inteira, sem decimais).

### Dicas
- Leia os números com `int()`
- Divisao decimal: use o operador `/`
- Para obter apenas a parte inteira do resultado, converta com `int()`
- Ou use o operador `//` (divisao inteira, que veremos no módulo 11)

### Proposta de Teste
- **Caso básico:** Números: `7` e `2` — Decimal: 3.5, Inteiro: 3
- **Caso de borda:** Números: `10` e `3` — Decimal: 3.333..., Inteiro: 3

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos dois numeros inteiros
# "dividend" = dividendo (numero que sera dividido)
dividend = int(input("Primeiro numero (dividendo): "))

# "divisor" = divisor (numero pelo qual vamos dividir)
divisor = int(input("Segundo numero (divisor): "))

# Divisao decimal: o operador / retorna float
# "decimal_result" = resultado decimal
decimal_result = dividend / divisor

# Resultado inteiro: convertemos o resultado decimal para int
# int() corta as casas decimais (nao arredonda)
# "integer_result" = resultado inteiro
integer_result = int(decimal_result)

# Exibimos os dois resultados
print("Divisao decimal:", decimal_result)
print("Parte inteira:", integer_result)
```

---

## Exercício 6 — Conversão em Cadeia — Nível: Intermediario

### Enunciado
Crie um programa que peca um número decimal ao usuario (como texto), converta para float, depois para int, e depois para string novamente. Exiba o valor e o tipo em cada etapa.

### Dicas
- Comece com o texto do input()
- Converta: str -> float -> int -> str
- Use `type()` em cada etapa

### Proposta de Teste
- **Caso básico:** Digite `7.89` — deve mostrar: str "7.89", float 7.89, int 7, str "7"

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Etapa 1: Texto original (str)
# "original" = valor original como texto
original = input("Digite um numero decimal: ")
print("Etapa 1 - str:", original, "- Tipo:", type(original))

# Etapa 2: Convertemos para float
# "as_float" = como decimal
as_float = float(original)
print("Etapa 2 - float:", as_float, "- Tipo:", type(as_float))

# Etapa 3: Convertemos para int (corta as casas decimais)
# "as_int" = como inteiro
as_int = int(as_float)
print("Etapa 3 - int:", as_int, "- Tipo:", type(as_int))

# Etapa 4: Convertemos de volta para str
# "as_str" = como texto novamente
as_str = str(as_int)
print("Etapa 4 - str:", as_str, "- Tipo:", type(as_str))
```

---

## Exercício 7 — Calculadora de Parcelas — Nível: Intermediario

### Enunciado
Crie um programa que peca o valor total de uma compra e o número de parcelas, e calcule o valor de cada parcela. (Parcela e o valor que você paga a cada mes quando divide uma compra. Para calcular, divida o valor total pelo número de parcelas.)

### Dicas
- Valor total: use `float()`
- Número de parcelas: use `int()`
- Valor da parcela: total dividido pelo número de parcelas

### Proposta de Teste
- **Caso básico:** Total: `300`, Parcelas: `3` — Valor da parcela: 100.0
- **Caso de borda:** Total: `100`, Parcelas: `7` — Valor da parcela: 14.285714...

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o valor total da compra
# "total_amount" = valor total
total_amount = float(input("Valor total da compra: R$ "))

# Pedimos o numero de parcelas
# "installments" = parcelas (numero de vezes para dividir)
installments = int(input("Numero de parcelas: "))

# Calculamos o valor de cada parcela
# "installment_value" = valor da parcela
# Dividimos o total pelo numero de parcelas
installment_value = total_amount / installments

# Exibimos o resultado
print("Valor total: R$", total_amount)
print("Numero de parcelas:", installments)
print("Valor de cada parcela: R$", installment_value)
```

---

## Exercício 8 — Separando Reais e Centavos — Nível: Intermediario

### Enunciado
Crie um programa que peca um valor monetario (ex: 45.73) e separe a parte dos reais (inteira) e a parte dos centavos (decimal).

### Dicas
- Use `float()` para ler o valor
- A parte inteira: use `int()` para cortar os decimais
- Os centavos: subtraia a parte inteira do valor original e multiplique por 100

### Proposta de Teste
- **Caso básico:** Valor: `45.73` — Reais: 45, Centavos: 73
- **Caso de borda:** Valor: `10.00` — Reais: 10, Centavos: 0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o valor monetario
# "amount" = valor/quantia
amount = float(input("Digite um valor em reais (ex: 45.73): R$ "))

# Separamos a parte inteira (reais)
# int() corta as casas decimais
# "reais" = parte inteira do valor
reais = int(amount)

# Separamos os centavos
# Subtraimos a parte inteira do valor original
# Multiplicamos por 100 para obter os centavos como numero inteiro
# "centavos" = parte decimal convertida para centavos
centavos = int((amount - reais) * 100)

# Exibimos o resultado
print("Valor: R$", amount)
print("Reais:", reais)
print("Centavos:", centavos)
```

---

## Exercício 9 — Conversor de Temperatura Completo — Nível: Avancado

### Enunciado
Crie um programa que peca uma temperatura em Celsius e converta para Fahrenheit e Kelvin. Exiba os resultados como números inteiros (arredondados). (Formulas: Fahrenheit = Celsius vezes 1.8 mais 32. Kelvin = Celsius mais 273.15.)

### Dicas
- Leia a temperatura com `float()`
- Calcule Fahrenheit: `celsius * 1.8 + 32`
- Calcule Kelvin: `celsius + 273.15`
- Use `round()` para arredondar (ou `int()` para truncar)

### Proposta de Teste
- **Caso básico:** Celsius: `100` — Fahrenheit: 212, Kelvin: 373
- **Caso de borda:** Celsius: `0` — Fahrenheit: 32, Kelvin: 273

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a temperatura em Celsius
# "celsius" = temperatura em graus Celsius
celsius = float(input("Temperatura em Celsius: "))

# Calculamos Fahrenheit: C * 1.8 + 32
# "fahrenheit" = temperatura em Fahrenheit
fahrenheit = celsius * 1.8 + 32

# Calculamos Kelvin: C + 273.15
# Kelvin e uma escala de temperatura usada em ciencia
# "kelvin" = temperatura em Kelvin
kelvin = celsius + 273.15

# Exibimos os resultados arredondados para numeros inteiros
# round() arredonda o numero para o inteiro mais proximo
print("Celsius:", celsius)
print("Fahrenheit:", round(fahrenheit))
print("Kelvin:", round(kelvin))
```

---

## Exercício 10 — Calculadora de Notas com Media — Nível: Avancado

### Enunciado
Crie um programa que peca 4 notas ao usuario, calcule a media (soma dividida por 4) e exiba a media como número decimal e como número inteiro (truncado).

### Dicas
- Use `float()` para cada nota
- Media: soma das 4 notas dividida por 4
- Use `int()` para mostrar a media truncada

### Proposta de Teste
- **Caso básico:** Notas: `7`, `8`, `9`, `6` — Media decimal: 7.5, Media inteira: 7
- **Caso de borda:** Notas: `10`, `10`, `10`, `10` — Media decimal: 10.0, Media inteira: 10

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos as 4 notas e convertemos para float
# "grade" = nota
grade_1 = float(input("Nota 1: "))
grade_2 = float(input("Nota 2: "))
grade_3 = float(input("Nota 3: "))
grade_4 = float(input("Nota 4: "))

# Calculamos a media: soma das notas dividida pela quantidade
# "average" = media
# Media e a soma de todos os valores dividida por quantos valores existem
average = (grade_1 + grade_2 + grade_3 + grade_4) / 4

# Convertemos a media para inteiro (truncando as casas decimais)
# "average_truncated" = media truncada (sem casas decimais)
average_truncated = int(average)

# Exibimos os resultados
print("Notas:", grade_1, grade_2, grade_3, grade_4)
print("Media (decimal):", average)
print("Media (inteira):", average_truncated)
```

---

## Exercício 11 — Formatando CPF — Nível: Avancado

### Enunciado
Crie um programa que peca ao usuario os 11 digitos de um CPF (apenas números, sem pontos ou tracos) e exiba o CPF formatado no padrão XXX.XXX.XXX-XX. Use conversão para string e fatiamento (cortar partes do texto).

### Dicas
- Leia o CPF como texto (não converta para número!)
- Use fatiamento de string: `texto[0:3]` pega os 3 primeiros caracteres
- Junte as partes com pontos e traco

### Proposta de Teste
- **Caso básico:** CPF: `12345678900` — Saida: `123.456.789-00`
- **Caso de borda:** CPF: `00000000000` — Saida: `000.000.000-00`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o CPF como texto (11 digitos sem formatacao)
# "cpf_raw" = CPF bruto (sem formatacao)
# Nao convertemos para int porque queremos manter os zeros a esquerda
cpf_raw = input("Digite os 11 digitos do CPF (sem pontos ou tracos): ")

# Fatiamos o texto para separar as partes do CPF
# cpf_raw[0:3] pega os caracteres da posicao 0 ate 2 (3 caracteres)
# cpf_raw[3:6] pega os caracteres da posicao 3 ate 5 (3 caracteres)
# cpf_raw[6:9] pega os caracteres da posicao 6 ate 8 (3 caracteres)
# cpf_raw[9:11] pega os caracteres da posicao 9 ate 10 (2 caracteres)
# "formatted_cpf" = CPF formatado
formatted_cpf = cpf_raw[0:3] + "." + cpf_raw[3:6] + "." + cpf_raw[6:9] + "-" + cpf_raw[9:11]

# Exibimos o CPF formatado
print("CPF formatado:", formatted_cpf)
```

> **Nota:** Este exercício usa fatiamento de strings (slicing), que sera aprofundado no próximo módulo. Aqui e apenas uma introdução prática.

---

## Exercício 12 — Calculadora Completa — Nível: Avancado

### Enunciado
Crie um programa que peca dois números ao usuario e exiba o resultado das quatro operações básicas (soma, subtracao, multiplicacao e divisao), mostrando cada resultado como decimal e como inteiro.

### Dicas
- Use `float()` para os números (aceita inteiros e decimais)
- Calcule as 4 operações
- Use `int()` para mostrar a versão inteira de cada resultado

### Proposta de Teste
- **Caso básico:** Números: `10` e `3` — Soma: 13.0/13, Subtracao: 7.0/7, Multiplicacao: 30.0/30, Divisao: 3.333.../3
- **Caso de borda:** Números: `0` e `5` — Soma: 5.0/5, Subtracao: -5.0/-5, Multiplicacao: 0.0/0, Divisao: 0.0/0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos dois numeros ao usuario
# "number_a" = primeiro numero, "number_b" = segundo numero
number_a = float(input("Primeiro numero: "))
number_b = float(input("Segundo numero: "))

# Calculamos as quatro operacoes basicas
# "sum_result" = resultado da soma (sum = soma)
sum_result = number_a + number_b

# "sub_result" = resultado da subtracao (subtraction = subtracao)
sub_result = number_a - number_b

# "mul_result" = resultado da multiplicacao (multiplication = multiplicacao)
mul_result = number_a * number_b

# "div_result" = resultado da divisao (division = divisao)
div_result = number_a / number_b

# Exibimos cada resultado como decimal e como inteiro
print("=== Resultados ===")
print("Soma:", sum_result, "| Inteiro:", int(sum_result))
print("Subtracao:", sub_result, "| Inteiro:", int(sub_result))
print("Multiplicacao:", mul_result, "| Inteiro:", int(mul_result))
print("Divisao:", div_result, "| Inteiro:", int(div_result))
```

---

[<- Voltar ao Módulo 08](08-conversão-tipos.md) | [Glossário](00-glossário.md)
