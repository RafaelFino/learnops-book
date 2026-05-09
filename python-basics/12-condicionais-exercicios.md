# Exercícios — Módulo 12: Condicionais

[<- Voltar ao Módulo 12](12-condicionais.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve seu código na pasta `~/meus-projetos/python-curso/modulo-12/` e execute com `python3 nome_do_arquivo.py`.
>
> Este e um módulo complexo e fundamental. Os exercícios estão organizados em ordem crescente de dificuldade. Não pule os básicos — eles constroem a base para os mais avancados.

---

## Exercício 1 — Maior de Idade — Nível: Básico

### Enunciado
Peca a idade do usuario e exiba se ele e maior ou menor de idade (18 anos).

### Dicas
- Use `if/else` com a condição `age >= 18`

### Proposta de Teste
- **Caso básico:** Idade: `20` — Saida: `Maior de idade`
- **Caso de borda:** Idade: `18` — Saida: `Maior de idade` (18 e maior de idade)
- **Caso de borda:** Idade: `17` — Saida: `Menor de idade`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a idade do usuario
# "age" = idade
age = int(input("Digite sua idade: "))

# Verificamos se e maior ou menor de idade
# >= significa "maior ou igual a"
if age >= 18:
    # Bloco executado quando a idade e 18 ou mais
    print("Maior de idade")
else:
    # Bloco executado quando a idade e menor que 18
    print("Menor de idade")
```

---

## Exercício 2 — Número Positivo, Negativo ou Zero — Nível: Básico

### Enunciado
Peca um número ao usuario e exiba se e positivo, negativo ou zero.

### Dicas
- Use `if/elif/else` com tres caminhos
- Positivo: maior que zero. Negativo: menor que zero. Zero: igual a zero.

### Proposta de Teste
- **Caso básico:** Número: `5` — Saida: `Positivo`
- **Caso de borda:** Número: `0` — Saida: `Zero`
- **Caso de borda:** Número: `-3` — Saida: `Negativo`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos um numero ao usuario
# "number" = numero
number = float(input("Digite um numero: "))

# Verificamos se e positivo, negativo ou zero
if number > 0:
    # Maior que zero = positivo
    print("Positivo")
elif number < 0:
    # Menor que zero = negativo
    print("Negativo")
else:
    # Se nao e positivo nem negativo, e zero
    print("Zero")
```

---

## Exercício 3 — Par ou Impar — Nível: Básico

### Enunciado
Peca um número inteiro e exiba se e par ou impar.

### Dicas
- Use o operador módulo `%`: se `numero % 2 == 0`, e par

### Proposta de Teste
- **Caso básico:** Número: `8` — Saida: `Par`
- **Caso de borda:** Número: `7` — Saida: `Impar`
- **Caso de borda:** Número: `0` — Saida: `Par` (zero e par)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos um numero inteiro
# "number" = numero
number = int(input("Digite um numero inteiro: "))

# Verificamos se e par ou impar usando o operador modulo (%)
# Se o resto da divisao por 2 for zero, o numero e par
if number % 2 == 0:
    print("Par")
else:
    print("Impar")
```

---

## Exercício 4 — Classificação de Nota — Nível: Básico

### Enunciado
Peca uma nota de 0 a 10 e exiba o conceito: A (9-10), B (7-8.9), C (5-6.9), D (abaixo de 5).

### Dicas
- Use `if/elif/elif/else`
- Comece pela nota mais alta e va descendo

### Proposta de Teste
- **Caso básico:** Nota: `8.5` — Saida: `Conceito B`
- **Caso de borda:** Nota: `9.0` — Saida: `Conceito A`
- **Caso de borda:** Nota: `4.9` — Saida: `Conceito D`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a nota
# "grade" = nota
grade = float(input("Digite a nota (0 a 10): "))

# Classificamos usando if/elif/else
# O Python verifica de cima para baixo e para na primeira condicao verdadeira
if grade >= 9:
    # Nota 9 ou mais = conceito A
    print("Conceito A")
elif grade >= 7:
    # Nota 7 a 8.9 = conceito B (ja sabemos que e < 9 porque o if anterior falhou)
    print("Conceito B")
elif grade >= 5:
    # Nota 5 a 6.9 = conceito C
    print("Conceito C")
else:
    # Nota abaixo de 5 = conceito D
    print("Conceito D")
```

---

## Exercício 5 — Calculadora de Desconto — Nível: Básico

### Enunciado
Peca o valor de uma compra. Se o valor for maior que 100, aplique 10% de desconto. Exiba o valor original e o valor final.

### Dicas
- Desconto de 10%: `valor * 0.10`
- Valor final: `valor - desconto`
- Se não tiver desconto, o valor final e o mesmo que o original

### Proposta de Teste
- **Caso básico:** Valor: `150` — Desconto: 15.0, Final: 135.0
- **Caso de borda:** Valor: `80` — Sem desconto, Final: 80.0
- **Caso de borda:** Valor: `100` — Sem desconto (não e MAIOR que 100)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o valor da compra
# "purchase_value" = valor da compra
purchase_value = float(input("Valor da compra: R$ "))

# Verificamos se tem direito a desconto
if purchase_value > 100:
    # Compras acima de R$ 100 tem 10% de desconto
    # "discount" = desconto
    discount = purchase_value * 0.10
    # "final_value" = valor final (original menos desconto)
    final_value = purchase_value - discount
    print(f"Valor original: R$ {purchase_value}")
    print(f"Desconto (10%): R$ {discount}")
    print(f"Valor final: R$ {final_value}")
else:
    # Sem desconto
    print(f"Valor da compra: R$ {purchase_value}")
    print("Sem desconto (compras acima de R$ 100 tem 10% de desconto)")
```

---

## Exercício 6 — Verificacao de Senha — Nível: Intermediario

### Enunciado
Defina uma senha correta no código (ex: "python123"). Peca ao usuario que digite a senha e verifique se esta correta.

### Dicas
- Compare a entrada do usuario com a senha definida usando `==`
- Exiba mensagens diferentes para senha correta e incorreta

### Proposta de Teste
- **Caso básico:** Senha: `python123` — Saida: `Acesso liberado!`
- **Caso de borda:** Senha: `Python123` — Saida: `Senha incorreta!` (diferencia maiusculas)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos a senha correta
# "correct_password" = senha correta
correct_password = "python123"

# Pedimos a senha ao usuario
# "user_password" = senha digitada pelo usuario
user_password = input("Digite a senha: ")

# Comparamos as senhas
# == verifica se sao exatamente iguais (incluindo maiusculas/minusculas)
if user_password == correct_password:
    print("Acesso liberado!")
else:
    print("Senha incorreta!")
```

---

## Exercício 7 — Faixa Etaria — Nível: Intermediario

### Enunciado
Peca a idade e classifique: bebe (0-1), crianca (2-12), adolescente (13-17), adulto (18-59), idoso (60+). Trate idades invalidas (negativas).

### Dicas
- Use `if/elif/elif/elif/elif/else`
- Comece verificando se a idade e inválida (negativa)

### Proposta de Teste
- **Caso básico:** Idade: `25` — Saida: `Adulto`
- **Caso de borda:** Idade: `0` — Saida: `Bebe`
- **Caso de borda:** Idade: `-5` — Saida: `Idade invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a idade
# "age" = idade
age = int(input("Digite a idade: "))

# Classificamos por faixa etaria
# Comecamos verificando o caso invalido
if age < 0:
    # Idade negativa nao existe
    print("Idade invalida!")
elif age <= 1:
    # 0 a 1 ano = bebe
    print("Bebe")
elif age <= 12:
    # 2 a 12 anos = crianca
    print("Crianca")
elif age <= 17:
    # 13 a 17 anos = adolescente
    print("Adolescente")
elif age <= 59:
    # 18 a 59 anos = adulto
    print("Adulto")
else:
    # 60 anos ou mais = idoso
    print("Idoso")
```

---

## Exercício 8 — Dia da Semana — Nível: Intermediario

### Enunciado
Peca um número de 1 a 7 e exiba o dia da semana correspondente (1=segunda, 2=terca, ..., 7=domingo). Se o número for inválido, exiba uma mensagem de erro.

### Dicas
- Use `if/elif/elif/.../else`
- O else trata números fora do intervalo 1-7

### Proposta de Teste
- **Caso básico:** Número: `3` — Saida: `Quarta-feira`
- **Caso de borda:** Número: `1` — Saida: `Segunda-feira`
- **Caso de borda:** Número: `8` — Saida: `Numero invalido`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o numero do dia
# "day_number" = numero do dia
day_number = int(input("Digite um numero de 1 a 7: "))

# Verificamos qual dia corresponde ao numero
if day_number == 1:
    print("Segunda-feira")
elif day_number == 2:
    print("Terca-feira")
elif day_number == 3:
    print("Quarta-feira")
elif day_number == 4:
    print("Quinta-feira")
elif day_number == 5:
    print("Sexta-feira")
elif day_number == 6:
    print("Sabado")
elif day_number == 7:
    print("Domingo")
else:
    # Qualquer numero fora de 1-7
    print("Numero invalido! Digite um numero de 1 a 7.")
```

---

## Exercício 9 — Calculadora com Validação — Nível: Intermediario

### Enunciado
Peca dois números e uma operação (+, -, *, /). Realize o cálculo e exiba o resultado. Se a operação for divisao, verifique se o divisor não e zero.

### Dicas
- Use `if/elif/elif/elif/else` para as operações
- Dentro da divisao, use um if aninhado para verificar o zero

### Proposta de Teste
- **Caso básico:** 10 + 5 — Saida: `15.0`
- **Caso de borda:** 10 / 0 — Saida: `Erro: divisao por zero!`
- **Caso de borda:** Operação: `x` — Saida: `Operacao invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos os dados da operacao
# "num_a" = primeiro numero, "num_b" = segundo numero
num_a = float(input("Primeiro numero: "))
num_b = float(input("Segundo numero: "))

# "operation" = operacao
operation = input("Operacao (+, -, *, /): ")

# Verificamos qual operacao foi escolhida
if operation == "+":
    # Soma
    print(f"Resultado: {num_a + num_b}")
elif operation == "-":
    # Subtracao
    print(f"Resultado: {num_a - num_b}")
elif operation == "*":
    # Multiplicacao
    print(f"Resultado: {num_a * num_b}")
elif operation == "/":
    # Divisao — precisamos verificar se o divisor nao e zero
    if num_b != 0:
        # Divisor diferente de zero — podemos dividir
        print(f"Resultado: {num_a / num_b}")
    else:
        # Divisor e zero — nao podemos dividir
        print("Erro: divisao por zero!")
else:
    # Operacao nao reconhecida
    print("Operacao invalida! Use +, -, * ou /")
```

---

## Exercício 10 — Triangulo Válido — Nível: Intermediario

### Enunciado
Peca tres valores representando os lados de um triangulo. Verifique se formam um triangulo válido. (Regra: a soma de dois lados quaisquer deve ser maior que o terceiro lado. Ou seja: a+b > c, a+c > b, b+c > a — todas as tres condições precisam ser verdadeiras.)

### Dicas
- Use `and` para combinar as tres condições
- Se for válido, exiba "Triangulo válido"; senao, "Não forma triangulo"

### Proposta de Teste
- **Caso básico:** Lados: `3`, `4`, `5` — Saida: `Triangulo valido`
- **Caso de borda:** Lados: `1`, `1`, `10` — Saida: `Nao forma triangulo`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos os tres lados do triangulo
# "side_a" = lado A, "side_b" = lado B, "side_c" = lado C
side_a = float(input("Lado A: "))
side_b = float(input("Lado B: "))
side_c = float(input("Lado C: "))

# Verificamos a regra do triangulo:
# A soma de dois lados quaisquer deve ser MAIOR que o terceiro
# Precisamos verificar as tres combinacoes com and (todas devem ser verdadeiras)
if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    print("Triangulo valido!")
else:
    print("Nao forma um triangulo.")
```

---

## Exercício 11 — Classificação de IMC — Nível: Intermediario

### Enunciado
Peca peso e altura, calcule o IMC e classifique: Abaixo do peso (< 18.5), Normal (18.5-24.9), Sobrepeso (25-29.9), Obesidade (>= 30).

### Dicas
- IMC = peso / (altura * altura)
- Use `if/elif/elif/else` para classificar

### Proposta de Teste
- **Caso básico:** Peso: `70`, Altura: `1.75` — IMC: ~22.86, Classificação: Normal
- **Caso de borda:** Peso: `50`, Altura: `1.80` — IMC: ~15.43, Classificação: Abaixo do peso

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos peso e altura
# "weight" = peso, "height" = altura
weight = float(input("Peso (kg): "))
height = float(input("Altura (metros): "))

# Calculamos o IMC
# "bmi" = BMI = Body Mass Index = Indice de Massa Corporal
# Formula: peso dividido pela altura ao quadrado
bmi = weight / (height ** 2)

# Classificamos o IMC
if bmi < 18.5:
    # "classification" = classificacao
    classification = "Abaixo do peso"
elif bmi < 25:
    classification = "Normal"
elif bmi < 30:
    classification = "Sobrepeso"
else:
    classification = "Obesidade"

# Exibimos o resultado
print(f"IMC: {bmi:.1f}")  # :.1f mostra apenas 1 casa decimal
print(f"Classificacao: {classification}")
```

---

## Exercício 12 — Ano Bissexto — Nível: Avancado

### Enunciado
Peca um ano e verifique se e bissexto. (Um ano e bissexto se for divisivel por 4, exceto se for divisivel por 100 — a menos que também seja divisivel por 400. Divisivel significa que o resto da divisao e zero.)

### Dicas
- Divisivel por 4: `ano % 4 == 0`
- Divisivel por 100: `ano % 100 == 0`
- Divisivel por 400: `ano % 400 == 0`
- Regra: (divisivel por 400) OU (divisivel por 4 E não divisivel por 100)

### Proposta de Teste
- **Caso básico:** Ano: `2024` — Saida: `Bissexto` (divisivel por 4, não por 100)
- **Caso de borda:** Ano: `1900` — Saida: `Nao bissexto` (divisivel por 100, não por 400)
- **Caso de borda:** Ano: `2000` — Saida: `Bissexto` (divisivel por 400)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o ano
# "year" = ano
year = int(input("Digite um ano: "))

# Verificamos se e bissexto
# A regra e: divisivel por 400 OU (divisivel por 4 E nao divisivel por 100)
# "is_leap" = e bissexto (leap year = ano bissexto)
# % e o operador modulo — se o resto for 0, e divisivel
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

# Exibimos o resultado
if is_leap:
    print(f"{year} e um ano bissexto.")
else:
    print(f"{year} nao e um ano bissexto.")
```

---

## Exercício 13 — Sistema de Login — Nível: Avancado

### Enunciado
Defina um usuario e senha corretos no código. Peca ao usuario que digite usuario e senha. Verifique se ambos estão corretos. Exiba mensagens especificas: se o usuario estiver errado, se a senha estiver errada, ou se ambos estiverem corretos.

### Dicas
- Use `and` para verificar se ambos estão corretos
- Use condicionais aninhadas ou compostas para identificar qual esta errado

### Proposta de Teste
- **Caso básico:** Usuario: `admin`, Senha: `1234` — Saida: `Login bem-sucedido!`
- **Caso de borda:** Usuario: `admin`, Senha: `errada` — Saida: `Senha incorreta`
- **Caso de borda:** Usuario: `outro`, Senha: `1234` — Saida: `Usuario nao encontrado`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Definimos as credenciais corretas
# "correct_user" = usuario correto, "correct_pass" = senha correta
correct_user = "admin"
correct_pass = "1234"

# Pedimos as credenciais ao usuario
# "input_user" = usuario digitado, "input_pass" = senha digitada
input_user = input("Usuario: ")
input_pass = input("Senha: ")

# Verificamos as credenciais
if input_user == correct_user and input_pass == correct_pass:
    # Ambos corretos — login bem-sucedido
    print("Login bem-sucedido! Bem-vindo!")
elif input_user != correct_user:
    # Usuario incorreto
    print("Usuario nao encontrado.")
else:
    # Usuario correto mas senha errada
    # (se chegou aqui, o usuario esta certo porque a condicao anterior falhou)
    print("Senha incorreta.")
```

---

## Exercício 14 — Classificação de Temperatura — Nível: Avancado

### Enunciado
Peca a temperatura em Celsius e classifique: Congelante (< 0), Muito frio (0-10), Frio (11-17), Agradavel (18-25), Quente (26-35), Muito quente (> 35). Exiba também uma recomendacao de roupa.

### Dicas
- Use `if/elif/elif/.../else` com várias faixas
- Cada faixa tem uma classificação e uma recomendacao

### Proposta de Teste
- **Caso básico:** Temperatura: `22` — Saida: `Agradavel` + recomendacao
- **Caso de borda:** Temperatura: `-5` — Saida: `Congelante` + recomendacao
- **Caso de borda:** Temperatura: `0` — Saida: `Muito frio` (0 esta na faixa 0-10)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a temperatura
# "temp" = temperatura (abreviacao de temperature)
temp = float(input("Temperatura em Celsius: "))

# Classificamos e recomendamos roupa
if temp < 0:
    # "classification" = classificacao, "clothing" = roupa
    classification = "Congelante"
    clothing = "Casaco pesado, luvas e cachecol"
elif temp <= 10:
    classification = "Muito frio"
    clothing = "Casaco pesado"
elif temp <= 17:
    classification = "Frio"
    clothing = "Casaco leve ou blusa de la"
elif temp <= 25:
    classification = "Agradavel"
    clothing = "Roupa leve e confortavel"
elif temp <= 35:
    classification = "Quente"
    clothing = "Roupa leve, protetor solar"
else:
    classification = "Muito quente"
    clothing = "Roupa muito leve, muita agua!"

# Exibimos o resultado
print(f"Temperatura: {temp} C")
print(f"Classificacao: {classification}")
print(f"Recomendacao: {clothing}")
```

---

## Exercício 15 — Verificacao de Acesso Completa — Nível: Avancado

### Enunciado
Um sistema de acesso verifica tres condições: idade (>= 18), ter documento (sim/não) e não estar na lista de bloqueados. Peca os dados e verifique se o acesso e permitido. Se não for, exiba todos os motivos da negacao.

### Dicas
- Use variáveis booleanas para cada condição
- Verifique cada condição separadamente para listar os motivos
- Use `and` para a verificacao final

### Proposta de Teste
- **Caso básico:** Idade: `20`, Documento: `sim`, Bloqueado: `nao` — Saida: `Acesso permitido`
- **Caso de borda:** Idade: `16`, Documento: `nao`, Bloqueado: `sim` — Saida: tres motivos de negacao

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Coletamos os dados
# "age" = idade
age = int(input("Idade: "))

# "has_document" = tem documento
doc_input = input("Tem documento? (sim/nao): ")
has_document = doc_input == "sim"

# "is_blocked" = esta bloqueado
blocked_input = input("Esta na lista de bloqueados? (sim/nao): ")
is_blocked = blocked_input == "sim"

# Verificamos o acesso
# Precisa: ter 18+, ter documento e NAO estar bloqueado
# "access_granted" = acesso concedido
access_granted = age >= 18 and has_document and not is_blocked

if access_granted:
    print("Acesso permitido! Bem-vindo.")
else:
    print("Acesso negado. Motivos:")
    # Verificamos cada condicao para listar os motivos
    if age < 18:
        print("  - Menor de idade (minimo 18 anos)")
    if not has_document:
        print("  - Sem documento de identificacao")
    if is_blocked:
        print("  - Nome na lista de bloqueados")
```

---

[<- Voltar ao Módulo 12](12-condicionais.md) | [Glossário](00-glossario.md)
