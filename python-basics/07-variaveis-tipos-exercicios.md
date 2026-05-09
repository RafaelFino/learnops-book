# Exercícios — Módulo 07: Variáveis e Tipos Básicos

[<- Voltar ao Módulo 07](07-variáveis-tipos.md) | [Glossário](00-glossário.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve seu código em um arquivo `.py` na pasta `~/meus-projetos/python-curso/modulo-07/`, abra o terminal, navegue ate a pasta com `cd ~/meus-projetos/python-curso/modulo-07` e execute com `python3 nome_do_arquivo.py`.

---

## Exercício 1 — Criando Variáveis Simples — Nível: Básico

### Enunciado
Crie um programa que defina tres variáveis (nome, idade e cidade) e exiba os valores no terminal.

### Dicas
- Crie uma variável para cada informação
- Use nomes em ingles: `name`, `age`, `city`
- Use `print()` para exibir cada valor

### Proposta de Teste
- **Caso básico:** Se você definir name="Ana", age=20, city="Curitiba", a saida deve mostrar os tres valores
- **Caso de borda:** Tente com age=0 e city="" (vazio) — o programa deve funcionar sem erros

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Criamos uma variavel para guardar o nome
# "name" = nome — tipo str (texto)
name = "Ana"

# Criamos uma variavel para guardar a idade
# "age" = idade — tipo int (numero inteiro)
age = 20

# Criamos uma variavel para guardar a cidade
# "city" = cidade — tipo str (texto)
city = "Curitiba"

# Exibimos os valores usando print()
# Cada print() mostra o rotulo e o valor da variavel
print("Nome:", name)
print("Idade:", age)
print("Cidade:", city)
```

---

## Exercício 2 — Verificando Tipos com type() — Nível: Básico

### Enunciado
Crie variáveis de cada um dos quatro tipos básicos (int, float, str, bool) e exiba o valor e o tipo de cada uma.

### Dicas
- Crie uma variável de cada tipo
- Use `type()` para verificar o tipo
- Exiba com `print()` o valor e o tipo juntos

### Proposta de Teste
- **Caso básico:** A saida deve mostrar quatro linhas, cada uma com o valor e o tipo correspondente (`<class 'int'>`, `<class 'float'>`, `<class 'str'>`, `<class 'bool'>`)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Variavel do tipo int (numero inteiro)
# "quantity" = quantidade
quantity = 42

# Variavel do tipo float (numero decimal)
# "price" = preco
price = 9.99

# Variavel do tipo str (texto)
# "product" = produto
product = "Cafe"

# Variavel do tipo bool (verdadeiro ou falso)
# "available" = disponivel
available = True

# Exibimos cada variavel com seu tipo
# type() retorna o tipo do valor armazenado na variavel
print("quantity:", quantity, "- Tipo:", type(quantity))
print("price:", price, "- Tipo:", type(price))
print("product:", product, "- Tipo:", type(product))
print("available:", available, "- Tipo:", type(available))
```

---

## Exercício 3 — Trocando Valores — Nível: Básico

### Enunciado
Crie uma variável com um valor inicial, exiba o valor, depois troque o valor e exiba novamente.

### Dicas
- Crie a variável com um valor
- Use `print()` para mostrar o valor
- Atribua um novo valor a mesma variável
- Use `print()` novamente

### Proposta de Teste
- **Caso básico:** Variável `score` comeca com 0, depois muda para 100. Saida: `Pontuacao inicial: 0` e `Pontuacao final: 100`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Criamos a variavel "score" (pontuacao) com valor inicial 0
# "score" = pontuacao
score = 0

# Exibimos o valor inicial
print("Pontuacao inicial:", score)

# Trocamos o valor da variavel para 100
# O valor antigo (0) e substituido pelo novo (100)
score = 100

# Exibimos o novo valor
print("Pontuacao final:", score)
```

---

## Exercício 4 — Dados do Usuario com Tipos — Nível: Básico

### Enunciado
Crie um programa que peca o nome e a idade do usuario, guarde em variáveis e exiba os dados junto com o tipo de cada variável.

### Dicas
- Use `input()` para ler os dados
- Converta a idade para `int` com `int()`
- Use `type()` para mostrar os tipos

### Proposta de Teste
- **Caso básico:** Nome: "Pedro", Idade: "25" — a saida deve mostrar nome como `<class 'str'>` e idade como `<class 'int'>`
- **Caso de borda:** Nome: "Ana Maria", Idade: "8" — deve funcionar com nomes compostos

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o nome do usuario — input() retorna str (texto)
# "name" = nome
name = input("Digite seu nome: ")

# Pedimos a idade e convertemos para int (numero inteiro)
# "age" = idade
# int() transforma o texto digitado em numero
age = int(input("Digite sua idade: "))

# Exibimos os dados com seus tipos
print("Nome:", name, "- Tipo:", type(name))
print("Idade:", age, "- Tipo:", type(age))
```

---

## Exercício 5 — Ficha de Produto — Nível: Intermediario

### Enunciado
Crie um programa que defina variáveis para um produto (nome, preco, quantidade em estoque e se esta disponível) e exiba uma ficha formatada.

### Dicas
- Use os quatro tipos básicos: str, float, int, bool
- Nomes em ingles: `product_name`, `price`, `stock_quantity`, `is_available`
- Formate a saida de forma organizada

### Proposta de Teste
- **Caso básico:** Produto: "Arroz", Preco: 5.99, Estoque: 100, Disponível: True — saida deve mostrar todos os dados
- **Caso de borda:** Estoque: 0, Disponível: False — deve funcionar com estoque zerado

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos as variaveis do produto usando os quatro tipos basicos
# "product_name" = nome do produto — tipo str
product_name = "Arroz"

# "price" = preco — tipo float (decimal, pois precos tem centavos)
price = 5.99

# "stock_quantity" = quantidade em estoque — tipo int (inteiro, pois contamos unidades)
stock_quantity = 100

# "is_available" = esta disponivel — tipo bool (sim ou nao)
is_available = True

# Exibimos a ficha formatada
print("=== Ficha do Produto ===")
print("Nome:", product_name)
print("Preco: R$", price)
print("Estoque:", stock_quantity, "unidades")
print("Disponivel:", is_available)
print("========================")
```

---

## Exercício 6 — Calculando com Variáveis — Nível: Intermediario

### Enunciado
Crie um programa que peca o preco de um produto e a quantidade desejada, guarde em variáveis e calcule o total.

### Dicas
- Use `float()` para o preco e `int()` para a quantidade
- Multiplique preco pela quantidade para obter o total
- Guarde o resultado em uma variável `total`

### Proposta de Teste
- **Caso básico:** Preco: 12.50, Quantidade: 3 — Total: 37.5
- **Caso de borda:** Preco: 0.01, Quantidade: 1 — Total: 0.01

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o preco do produto e convertemos para float (decimal)
# "price" = preco
price = float(input("Preco do produto: R$ "))

# Pedimos a quantidade e convertemos para int (inteiro)
# "quantity" = quantidade
quantity = int(input("Quantidade desejada: "))

# Calculamos o total multiplicando preco pela quantidade
# "total" = total
# O operador * realiza a multiplicacao
total = price * quantity

# Exibimos o resultado
print("Preco unitario: R$", price)
print("Quantidade:", quantity)
print("Total: R$", total)
```

---

## Exercício 7 — Troca de Variáveis — Nível: Intermediario

### Enunciado
Crie duas variáveis `a` e `b` com valores diferentes. Troque os valores entre elas (o valor de `a` vai para `b` e vice-versa) e exiba os valores antes e depois da troca.

### Dicas
- Você vai precisar de uma variável temporária para guardar um dos valores durante a troca
- Ou use a troca simultanea do Python: `a, b = b, a`

### Proposta de Teste
- **Caso básico:** a=10, b=20 — Depois da troca: a=20, b=10

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos duas variaveis com valores iniciais
a = 10
b = 20

# Exibimos os valores antes da troca
print("Antes da troca:")
print("a =", a)
print("b =", b)

# Trocamos os valores usando uma variavel temporaria
# "temp" = temporario — guarda o valor de a enquanto fazemos a troca
temp = a    # temp recebe o valor de a (10)
a = b       # a recebe o valor de b (20)
b = temp    # b recebe o valor que estava em temp (10, o antigo valor de a)

# Exibimos os valores depois da troca
print("\nDepois da troca:")
print("a =", a)
print("b =", b)

# Nota: Python tambem permite trocar de forma mais simples:
# a, b = b, a
# Isso faz a mesma coisa em uma unica linha!
```

---

## Exercício 8 — Cadastro Completo — Nível: Intermediario

### Enunciado
Crie um programa que peca ao usuario: nome, idade, altura e se e estudante (sim/não). Guarde cada dado no tipo correto e exiba tudo formatado.

### Dicas
- Nome: str (input direto)
- Idade: int (converter com int())
- Altura: float (converter com float())
- Estudante: leia como texto e compare com "sim"

### Proposta de Teste
- **Caso básico:** Nome: "Carlos", Idade: "35", Altura: "1.78", Estudante: "sim" — deve exibir todos os dados com tipos corretos
- **Caso de borda:** Estudante: "não" — is_student deve ser False

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o nome — input() ja retorna str
# "name" = nome
name = input("Nome: ")

# Pedimos a idade e convertemos para int
# "age" = idade
age = int(input("Idade: "))

# Pedimos a altura e convertemos para float
# "height" = altura
height = float(input("Altura (em metros, ex: 1.75): "))

# Pedimos se e estudante — lemos como texto
# "student_input" = entrada sobre ser estudante
student_input = input("E estudante? (sim/nao): ")

# Convertemos a resposta para booleano
# "is_student" = e estudante
# Se o usuario digitou "sim", is_student sera True; caso contrario, False
# O operador == compara dois valores e retorna True ou False
is_student = student_input == "sim"

# Exibimos os dados formatados com seus tipos
print("\n=== Cadastro ===")
print("Nome:", name, "- Tipo:", type(name))
print("Idade:", age, "- Tipo:", type(age))
print("Altura:", height, "m - Tipo:", type(height))
print("Estudante:", is_student, "- Tipo:", type(is_student))
```

---

## Exercício 9 — Calculadora de Area — Nível: Intermediario

### Enunciado
Crie um programa que peca a largura e o comprimento de um terreno retangular e calcule a area. (Area de um retangulo: largura multiplicada pelo comprimento. Exemplo: um terreno de 10 metros de largura por 20 metros de comprimento tem area de 10 x 20 = 200 metros quadrados.)

### Dicas
- Use `float()` para largura e comprimento
- Multiplique os dois valores
- Exiba o resultado com a unidade (metros quadrados)

### Proposta de Teste
- **Caso básico:** Largura: 10, Comprimento: 20 — Area: 200.0 metros quadrados
- **Caso de borda:** Largura: 0.5, Comprimento: 0.5 — Area: 0.25 metros quadrados

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a largura do terreno
# "width" = largura
width = float(input("Largura do terreno (metros): "))

# Pedimos o comprimento do terreno
# "length" = comprimento
length = float(input("Comprimento do terreno (metros): "))

# Calculamos a area multiplicando largura pelo comprimento
# "area" = area
# Area de um retangulo = largura x comprimento
area = width * length

# Exibimos o resultado
print("Largura:", width, "m")
print("Comprimento:", length, "m")
print("Area:", area, "metros quadrados")
```

---

## Exercício 10 — Perfil com Todos os Tipos — Nível: Avancado

### Enunciado
Crie um programa que peca ao usuario todos os dados de um perfil: nome completo, ano de nascimento, peso, altura e se prática esportes. Calcule a idade aproximada e o IMC, e exiba um perfil completo com todos os dados e tipos.

### Dicas
- Idade aproximada: 2025 menos o ano de nascimento
- IMC: peso dividido pela altura ao quadrado (peso / (altura * altura))
- Use todos os quatro tipos básicos
- Exiba o tipo de cada variável calculada

### Proposta de Teste
- **Caso básico:** Nome: "Maria", Ano: "1990", Peso: "65", Altura: "1.65", Esportes: "sim" — deve calcular idade 35 e IMC aproximadamente 23.87
- **Caso de borda:** Ano: "2020", Peso: "30", Altura: "1.20" — deve funcionar com valores de crianca

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Coletamos todos os dados do perfil
# "full_name" = nome completo
full_name = input("Nome completo: ")

# "birth_year" = ano de nascimento — convertemos para int
birth_year = int(input("Ano de nascimento: "))

# "weight" = peso — convertemos para float (pode ter decimais)
weight = float(input("Peso (kg): "))

# "height" = altura — convertemos para float
height = float(input("Altura (metros, ex: 1.65): "))

# "sports_input" = entrada sobre esportes
sports_input = input("Pratica esportes? (sim/nao): ")

# Convertemos para booleano
# "practices_sports" = pratica esportes
practices_sports = sports_input == "sim"

# Calculamos a idade aproximada
# "approximate_age" = idade aproximada
# Subtraimos o ano de nascimento do ano atual
approximate_age = 2025 - birth_year

# Calculamos o IMC (Indice de Massa Corporal)
# "bmi" = BMI = Body Mass Index = IMC
# Formula: peso dividido pela altura ao quadrado
# height * height e o mesmo que "altura vezes altura" (altura ao quadrado)
bmi = weight / (height * height)

# Exibimos o perfil completo
print("\n=== Perfil Completo ===")
print("Nome:", full_name)
print("Ano de nascimento:", birth_year)
print("Idade aproximada:", approximate_age, "anos")
print("Peso:", weight, "kg")
print("Altura:", height, "m")
print("IMC:", bmi)
print("Pratica esportes:", practices_sports)
print("========================")
```

---

## Exercício 11 — Conversor de Unidades — Nível: Avancado

### Enunciado
Crie um programa que peca uma distancia em quilometros e converta para metros, centimetros e milimetros. (1 quilometro = 1000 metros. 1 metro = 100 centimetros. 1 centimetro = 10 milimetros.)

### Dicas
- Metros: quilometros multiplicado por 1000
- Centimetros: metros multiplicado por 100
- Milimetros: centimetros multiplicado por 10
- Use `float()` para a entrada

### Proposta de Teste
- **Caso básico:** Distancia: 1.5 km — Metros: 1500.0, Centimetros: 150000.0, Milimetros: 1500000.0
- **Caso de borda:** Distancia: 0 — Todos os valores devem ser 0.0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a distancia em quilometros
# "distance_km" = distancia em quilometros
distance_km = float(input("Distancia em quilometros: "))

# Convertemos para metros: 1 km = 1000 metros
# "distance_m" = distancia em metros
distance_m = distance_km * 1000

# Convertemos para centimetros: 1 metro = 100 centimetros
# "distance_cm" = distancia em centimetros
distance_cm = distance_m * 100

# Convertemos para milimetros: 1 centimetro = 10 milimetros
# "distance_mm" = distancia em milimetros
distance_mm = distance_cm * 10

# Exibimos todas as conversoes
print("Distancia em km:", distance_km)
print("Distancia em metros:", distance_m)
print("Distancia em centimetros:", distance_cm)
print("Distancia em milimetros:", distance_mm)
```

---

## Exercício 12 — Orcamento Domestico — Nível: Avancado

### Enunciado
Crie um programa que peca o salario mensal e os valores de tres despesas (aluguel, alimentacao e transporte). Calcule o total de despesas, o valor que sobra e a porcentagem gasta. (Porcentagem gasta: total de despesas dividido pelo salario, multiplicado por 100.)

### Dicas
- Use `float()` para todos os valores
- Total de despesas: soma das tres despesas
- Sobra: salario menos total de despesas
- Porcentagem: (total / salario) * 100

### Proposta de Teste
- **Caso básico:** Salario: 3000, Aluguel: 1000, Alimentacao: 800, Transporte: 400 — Total: 2200, Sobra: 800, Porcentagem: 73.33...
- **Caso de borda:** Todas as despesas 0 — Sobra: 3000, Porcentagem: 0.0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o salario mensal
# "salary" = salario
salary = float(input("Salario mensal: R$ "))

# Pedimos as tres despesas
# "rent" = aluguel
rent = float(input("Aluguel: R$ "))

# "food" = alimentacao
food = float(input("Alimentacao: R$ "))

# "transport" = transporte
transport = float(input("Transporte: R$ "))

# Calculamos o total de despesas somando as tres
# "total_expenses" = total de despesas
total_expenses = rent + food + transport

# Calculamos quanto sobra subtraindo as despesas do salario
# "remaining" = restante/sobra
remaining = salary - total_expenses

# Calculamos a porcentagem gasta
# "spent_percentage" = porcentagem gasta
# Porcentagem: (parte / total) * 100
# Exemplo: se gastou 2200 de 3000, a porcentagem e (2200/3000)*100 = 73.33%
spent_percentage = (total_expenses / salary) * 100

# Exibimos o orcamento
print("\n=== Orcamento Mensal ===")
print("Salario: R$", salary)
print("Aluguel: R$", rent)
print("Alimentacao: R$", food)
print("Transporte: R$", transport)
print("------------------------")
print("Total de despesas: R$", total_expenses)
print("Sobra: R$", remaining)
print("Porcentagem gasta:", spent_percentage, "%")
```

---

[<- Voltar ao Módulo 07](07-variáveis-tipos.md) | [Glossário](00-glossário.md)
