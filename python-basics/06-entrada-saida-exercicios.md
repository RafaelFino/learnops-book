# Exercícios — Módulo 06: Entrada e Saída de Dados

[← Voltar ao Módulo 06](06-entrada-saida.md) · [Glossário](00-glossário.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar cada exercício:**
> 1. Escreva seu código no VSCode
> 2. Salve o arquivo (ex: `exercicio_01.py`) na pasta `~/meus-projetos/python-curso/modulo-06/`
> 3. Abra o terminal (`Ctrl + Alt + T`)
> 4. Navegue ate a pasta: `cd ~/meus-projetos/python-curso/modulo-06`
> 5. Execute: `python3 exercicio_01.py`
> 6. Compare a saida com a Proposta de Teste

---

## Exercício 1 — Saudacao Personalizada — Nível: Básico

### Enunciado
Crie um programa que pergunte o nome do usuário e exiba uma mensagem de boas-vindas personalizada.

### Dicas
- Use `input()` para perguntar o nome
- Use `print()` para exibir a mensagem
- Guarde o nome em uma variável

### Proposta de Teste
- **Caso básico:** Digite `Ana` → saída deve ser `Bem-vindo(a), Ana - Bons estudos!`
- **Caso de borda:** Digite `Maria José` (nome com espaço) → saída deve ser `Bem-vindo(a), Maria José - Bons estudos!`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos o nome do usuário usando input()
# "name" = nome
# input() exibe a mensagem e espera o usuário digitar
name = input("Digite seu nome: ")

# Exibimos a mensagem de boas-vindas usando print()
# Usamos vírgulas para separar os textos e a variável
# O print() coloca espaço automaticamente entre cada valor
print("Bem-vindo(a),", name, "- Bons estudos!")
```

> **Nota:** Perceba que usamos apenas **vírgulas** para separar os valores no print(). Cada valor separado por vírgula recebe um espaço automático entre eles.

---

## Exercício 2 — Dados Pessoais — Nível: Básico

### Enunciado
Crie um programa que pergunte o nome, a idade e a cidade do usuário, e depois exiba todos os dados formatados.

### Dicas
- Use três chamadas de `input()`, uma para cada dado
- Guarde cada resposta em uma variável diferente
- Use `print()` para exibir os dados organizados

### Proposta de Teste
- **Caso básico:** Nome: `João`, Idade: `30`, Cidade: `Curitiba` → saída deve mostrar os três dados
- **Caso de borda:** Nome: `Ana Maria`, Idade: `8`, Cidade: `São Paulo` → deve funcionar com nomes compostos e idades baixas

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Coletamos os dados do usuário
# "name" = nome
name = input("Digite seu nome: ")

# "age" = idade (aqui não precisamos converter, pois vamos apenas exibir)
age = input("Digite sua idade: ")

# "city" = cidade
city = input("Digite sua cidade: ")

# Exibimos os dados formatados
# Usamos print() com múltiplos valores separados por vírgula
print("--- Seus Dados ---")
print("Nome:", name)
print("Idade:", age, "anos")
print("Cidade:", city)
```

---

## Exercício 3 — Soma de Dois Números — Nível: Básico

### Enunciado
Crie um programa que peça dois números inteiros ao usuário e exiba a soma deles.

### Dicas
- Lembre-se: `input()` retorna texto (string)!
- Use `int()` para converter o texto em número antes de somar
- Guarde cada número em uma variável

### Proposta de Teste
- **Caso básico:** Números `10` e `5` → saída deve ser `A soma é: 15`
- **Caso de borda:** Números `0` e `0` → saída deve ser `A soma é: 0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos o primeiro número e convertemos para inteiro com int()
# "first_number" = primeiro número
# int() transforma o texto digitado em número inteiro
first_number = int(input("Digite o primeiro número: "))

# Pedimos o segundo número e convertemos para inteiro
# "second_number" = segundo número
second_number = int(input("Digite o segundo número: "))

# Calculamos a soma
# "result" = resultado
# O operador + soma os dois números
result = first_number + second_number

# Exibimos o resultado
print("A soma é:", result)
```

---

## Exercício 4 — Calculadora de Troco — Nível: Básico

### Enunciado
Crie um programa que pergunte o valor total da compra e o valor pago pelo cliente, e exiba o troco.

### Dicas
- Use `float()` para converter, pois valores monetários têm decimais
- O troco é: valor pago menos valor da compra
- Pense: o que acontece se o cliente pagar o valor exato?

### Proposta de Teste
- **Caso básico:** Compra: `25.50`, Pago: `50.00` → saída deve ser `Troco: R$ 24.5`
- **Caso de borda:** Compra: `10.00`, Pago: `10.00` → saída deve ser `Troco: R$ 0.0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos o valor da compra e convertemos para decimal com float()
# "purchase_total" = total da compra
# float() converte texto para número decimal
purchase_total = float(input("Valor total da compra: R$ "))

# Pedimos o valor pago pelo cliente
# "amount_paid" = valor pago
amount_paid = float(input("Valor pago: R$ "))

# Calculamos o troco subtraindo o total do valor pago
# "change" = troco
change = amount_paid - purchase_total

# Exibimos o troco
print("Troco: R$", change)
```

---

## Exercício 5 — Conversor de Horas para Minutos — Nível: Básico

### Enunciado
Crie um programa que pergunte uma quantidade de horas e converta para minutos. (Lembre-se: 1 hora = 60 minutos. Isso significa que para saber quantos minutos tem em um número de horas, basta multiplicar as horas por 60.)

### Dicas
- Peça o número de horas ao usuário
- Multiplique por 60 para obter os minutos
- Use `int()` ou `float()` para converter

### Proposta de Teste
- **Caso básico:** Horas: `2` → saída deve ser `2 hora(s) = 120 minutos`
- **Caso de borda:** Horas: `0` → saída deve ser `0 hora(s) = 0 minutos`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos a quantidade de horas
# "hours" = horas
# int() converte para número inteiro
hours = int(input("Digite a quantidade de horas: "))

# Calculamos os minutos multiplicando horas por 60
# "minutes" = minutos
# Multiplicação: cada hora tem 60 minutos
minutes = hours * 60

# Exibimos o resultado
print(hours, "hora(s) =", minutes, "minutos")
```

---

## Exercício 6 — Media de Tres Notas — Nível: Intermediario

### Enunciado
Crie um programa que peça três notas ao usuário e calcule a média. (Média é a soma de todos os valores dividida pela quantidade de valores. Exemplo: a média de 7, 8 e 9 é (7+8+9)/3 = 8.0)

### Dicas
- Use `float()` para as notas (podem ter decimais)
- Some as três notas e divida por 3
- Guarde cada nota em uma variável diferente

### Proposta de Teste
- **Caso básico:** Notas `7`, `8`, `9` → saída deve ser `Média: 8.0`
- **Caso de borda:** Notas `10`, `10`, `10` → saída deve ser `Média: 10.0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos as três notas e convertemos para decimal
# "grade" = nota (grade_1 = nota 1, grade_2 = nota 2, grade_3 = nota 3)
grade_1 = float(input("Digite a primeira nota: "))
grade_2 = float(input("Digite a segunda nota: "))
grade_3 = float(input("Digite a terceira nota: "))

# Calculamos a média: soma das notas dividida por 3
# "average" = média
# Divisão: o operador / divide um número por outro
average = (grade_1 + grade_2 + grade_3) / 3

# Exibimos o resultado
print("Média:", average)
```

---

## Exercício 7 — Separador Personalizado — Nível: Intermediario

### Enunciado
Crie um programa que peça três palavras ao usuário e exiba-as separadas por ` * ` (asterisco com espaços).

### Dicas
- Use o parâmetro `sep` do `print()`
- Lembre-se: `sep` muda o separador entre os valores

### Proposta de Teste
- **Caso básico:** Palavras `sol`, `lua`, `estrela` → saída deve ser `sol * lua * estrela`
- **Caso de borda:** Palavras `a`, `b`, `c` → saída deve ser `a * b * c`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos três palavras ao usuário
# "word" = palavra (word_1 = palavra 1, etc.)
word_1 = input("Digite a primeira palavra: ")
word_2 = input("Digite a segunda palavra: ")
word_3 = input("Digite a terceira palavra: ")

# Exibimos as palavras separadas por " * "
# sep=" * " define que o separador entre os valores será " * "
print(word_1, word_2, word_3, sep=" * ")
```

---

## Exercício 8 — Contagem Regressiva na Mesma Linha — Nível: Intermediario

### Enunciado
Crie um programa que exiba os números 5, 4, 3, 2, 1 todos na mesma linha, separados por espaço, e depois exiba "Fogo!" na linha seguinte.

### Dicas
- Use `end=" "` para manter os números na mesma linha
- O último `print()` (com "Fogo!") não precisa de `end`

### Proposta de Teste
- **Caso único:** A saída deve ser exatamente:
  ```
  5 4 3 2 1 
  Fogo!
  ```

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Exibimos cada número na mesma linha usando end=" "
# end=" " faz o print() colocar um espaço no final em vez de pular linha
print(5, end=" ")
print(4, end=" ")
print(3, end=" ")
print(2, end=" ")
print(1, end=" ")

# Este print() pula para a próxima linha normalmente
# porque não tem end= definido
print()

# Exibimos "Fogo!" na nova linha
print("Fogo!")
```

> **Dica:** **Alternativa mais simples:** Você também poderia resolver com uma única linha:
> **Nota:** `print(5, 4, 3, 2, 1)` — isso exibe todos os números separados por espaço.
> **Nota:** Mas o objetivo deste exercício é praticar o uso de `end`, por isso usamos vários `print()`.

---

## Exercício 9 — Ficha de Produto — Nível: Intermediario

### Enunciado
Crie um programa que peça o nome, o preço e a quantidade em estoque de um produto, e exiba uma ficha formatada.

### Dicas
- Use `float()` para o preço e `int()` para a quantidade
- Organize a saída com `print()` para ficar visualmente agradável
- Use `\t` (tabulação) ou espaços para alinhar

### Proposta de Teste
- **Caso básico:** Nome: `Arroz`, Preço: `5.99`, Quantidade: `100` → saída formatada com os três dados
- **Caso de borda:** Nome: `Óleo de Soja`, Preço: `8.50`, Quantidade: `0` → deve funcionar com nome longo e quantidade zero

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Coletamos os dados do produto
# "product_name" = nome do produto
product_name = input("Nome do produto: ")

# "price" = preço — convertemos para decimal com float()
price = float(input("Preço: R$ "))

# "stock_quantity" = quantidade em estoque — convertemos para inteiro com int()
stock_quantity = int(input("Quantidade em estoque: "))

# Exibimos a ficha formatada
# Usamos print() com \t para alinhar as informações
print("\n=== Ficha do Produto ===")  # \n pula uma linha antes
print("Nome:\t\t", product_name)     # \t\t = duas tabulações para alinhar
print("Preço:\t\t R$", price)
print("Estoque:\t", stock_quantity, "unidades")
print("========================")
```

---

## Exercício 10 — Calculadora de IMC — Nível: Avancado

### Enunciado
Crie um programa que peça o peso (em kg) e a altura (em metros) do usuário e calcule o IMC (Índice de Massa Corporal). A fórmula do IMC é: peso dividido pela altura multiplicada por ela mesma (peso ÷ (altura × altura)).

### Dicas
- Use `float()` para peso e altura (são valores decimais)
- A fórmula é: `imc = weight / (height * height)`
- Ou use `height ** 2` (altura elevada ao quadrado — que é a mesma coisa que altura vezes altura)

### Proposta de Teste
- **Caso básico:** Peso: `70`, Altura: `1.75` → saída deve ser aproximadamente `IMC: 22.857142857142858`
- **Caso de borda:** Peso: `50`, Altura: `1.50` → saída deve ser aproximadamente `IMC: 22.22222222222222`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos o peso em quilogramas
# "weight" = peso
weight = float(input("Digite seu peso em kg: "))

# Pedimos a altura em metros
# "height" = altura
height = float(input("Digite sua altura em metros (ex: 1.75): "))

# Calculamos o IMC: peso dividido pela altura ao quadrado
# "bmi" = BMI = Body Mass Index = Índice de Massa Corporal (IMC)
# height ** 2 significa "altura elevada ao quadrado" (altura × altura)
# ** é o operador de exponenciação (potência)
bmi = weight / (height ** 2)

# Exibimos o resultado
print("Seu IMC é:", bmi)
```

---

## Exercício 11 — Lista de Compras com Total — Nível: Avancado

### Enunciado
Crie um programa que peça o nome e o preço de 3 produtos e exiba uma lista de compras com o total.

### Dicas
- Use variáveis diferentes para cada produto e preço
- Some os três preços para obter o total
- Formate a saída como uma tabela simples

### Proposta de Teste
- **Caso básico:** Arroz R$5.00, Feijão R$8.00, Macarrão R$3.00 → Total: R$16.0
- **Caso de borda:** Três produtos com preço R$0.00 → Total: R$0.0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Coletamos nome e preço de 3 produtos
# "product" = produto, "price" = preço
# Produto 1
product_1 = input("Nome do produto 1: ")
price_1 = float(input("Preço do produto 1: R$ "))

# Produto 2
product_2 = input("Nome do produto 2: ")
price_2 = float(input("Preço do produto 2: R$ "))

# Produto 3
product_3 = input("Nome do produto 3: ")
price_3 = float(input("Preço do produto 3: R$ "))

# Calculamos o total somando os três preços
# "total" = total
total = price_1 + price_2 + price_3

# Exibimos a lista de compras formatada
print("\n=== Lista de Compras ===")
print(product_1, "\t R$", price_1)
print(product_2, "\t R$", price_2)
print(product_3, "\t R$", price_3)
print("------------------------")
print("Total:\t\t R$", total)
```

---

## Exercício 12 — Conversor de Moeda — Nível: Avancado

### Enunciado
Crie um programa que pergunte um valor em reais e a cotação do dólar, e converta o valor para dólares. (Para converter reais em dólares, divida o valor em reais pela cotação do dólar.)

### Dicas
- Use `float()` para ambos os valores
- Divida o valor em reais pela cotação
- Exiba o resultado com as duas moedas

### Proposta de Teste
- **Caso básico:** Valor: `100`, Cotação: `5.00` → saída deve ser `100.0 reais = 20.0 dólares`
- **Caso de borda:** Valor: `0`, Cotação: `5.00` → saída deve ser `0.0 reais = 0.0 dólares`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos o valor em reais
# "amount_brl" = valor em reais (BRL = Brazilian Real)
amount_brl = float(input("Digite o valor em reais: R$ "))

# Pedimos a cotação do dólar
# "exchange_rate" = taxa de câmbio (cotação)
exchange_rate = float(input("Cotação do dólar (ex: 5.20): R$ "))

# Calculamos o valor em dólares dividindo reais pela cotação
# "amount_usd" = valor em dólares (USD = United States Dollar)
# Divisão: reais dividido pela cotação = dólares
amount_usd = amount_brl / exchange_rate

# Exibimos o resultado
print(amount_brl, "reais =", amount_usd, "dólares")
```

---

## Exercício 13 — Separando Secoes com Linhas em Branco — Nível: Básico

### Enunciado
Crie um programa que exiba seu nome, uma linha em branco, e depois sua cidade. Use `print()` vazio para criar a linha em branco.

### Dicas
- `print()` sem nenhum argumento apenas pula uma linha
- Use três chamadas de `print()`

### Proposta de Teste
- **Caso único:** A saída deve ter uma linha em branco entre o nome e a cidade:
  ```
  João Silva

  São Paulo
  ```

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Exibimos o nome
print("João Silva")

# print() sem argumentos pula uma linha em branco
# É útil para separar visualmente partes da saída
print()

# Exibimos a cidade
print("São Paulo")
```

---

## Exercício 14 — Combinando sep e end — Nível: Avancado

### Enunciado
Crie um programa que exiba uma data no formato `DD/MM/AAAA` usando `sep`, e na mesma linha exiba " - " seguido do dia da semana. Use `sep` e `end` juntos.

### Dicas
- Use `sep="/"` para formatar a data
- Use `end=" - "` para continuar na mesma linha
- O segundo `print()` exibe o dia da semana

### Proposta de Teste
- **Caso único:** A saída deve ser exatamente: `15/01/2025 - Quarta-feira`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Exibimos a data usando sep="/" para separar dia, mês e ano com barras
# end=" - " faz o print() NAO pular linha e colocar " - " no final
# Assim o próximo print() continua na mesma linha
print("15", "01", "2025", sep="/", end=" - ")

# Exibimos o dia da semana na mesma linha
# Este print() pula linha normalmente (comportamento padrão)
print("Quarta-feira")
```

> **Nota:** Este exercício mostra que `sep` e `end` podem ser usados **juntos** no mesmo `print()`. O `sep` controla o que vai entre os valores, e o `end` controla o que vai no final.

---

## Exercício 15 — Recibo de Compra Completo — Nível: Avancado

### Enunciado
Crie um programa que peça o nome do cliente, o nome de 2 produtos com seus preços, e exiba um recibo formatado com subtotal, desconto de 10% (desconto é um valor que se subtrai do total — 10% significa que você paga 90% do valor) e total final.

### Dicas
- Use `float()` para os preços
- Calcule o subtotal (soma dos preços)
- Calcule o desconto: `subtotal * 0.10` (10% do subtotal — multiplicar por 0.10 é o mesmo que calcular 10 de cada 100)
- Total final: `subtotal - desconto` (subtotal menos o desconto)
- Formate a saída como um recibo

### Proposta de Teste
- **Caso básico:** Cliente: `Maria`, Produto1: `Arroz` R$5.00, Produto2: `Feijão` R$8.00 → Subtotal: 13.0, Desconto: 1.3, Total: 11.7
- **Caso de borda:** Dois produtos com preço R$0.00 → Subtotal: 0.0, Desconto: 0.0, Total: 0.0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Pedimos o nome do cliente
# "customer_name" = nome do cliente
customer_name = input("Nome do cliente: ")

# Pedimos o primeiro produto e seu preço
# "product" = produto, "price" = preço
product_1 = input("Nome do produto 1: ")
price_1 = float(input("Preço do produto 1: R$ "))

# Pedimos o segundo produto e seu preço
product_2 = input("Nome do produto 2: ")
price_2 = float(input("Preço do produto 2: R$ "))

# Calculamos o subtotal: soma dos preços dos dois produtos
# "subtotal" = subtotal (soma parcial antes do desconto)
subtotal = price_1 + price_2

# Calculamos o desconto de 10%
# "discount" = desconto
# Multiplicar por 0.10 é calcular 10% (10 de cada 100)
# Exemplo: 10% de 100 = 100 * 0.10 = 10
discount = subtotal * 0.10

# Calculamos o total final subtraindo o desconto do subtotal
# "total" = total final
total = subtotal - discount

# Exibimos o recibo formatado
print("\n========== RECIBO ==========")
print("Cliente:", customer_name)
print("----------------------------")
print(product_1, "\t\t R$", price_1)
print(product_2, "\t\t R$", price_2)
print("----------------------------")
print("Subtotal:\t R$", subtotal)
print("Desconto (10%):\t R$", discount)
print("TOTAL:\t\t R$", total)
print("============================")
```

---

[← Voltar ao Módulo 06](06-entrada-saida.md) · [Glossário](00-glossário.md)
