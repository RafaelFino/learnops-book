# Exercícios — Módulo 13: Seletores match/case

[<- Voltar ao Módulo 13](13-seletores-match-case.md) | [Glossário](00-glossário.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-13/` e execute com `python3 nome_do_arquivo.py`.
>
> **Nota:** Se sua versão do Python for anterior a 3.10, resolva os exercícios usando `if/elif/else` como alternativa.

---

## Exercício 1 — Menu de Opcoes — Nível: Básico

### Enunciado
Crie um menu com 3 opcoes (1-Cadastrar, 2-Consultar, 3-Sair). Peca ao usuario que escolha uma opcao e exiba a ação correspondente.

### Dicas
- Use `match/case` com números inteiros
- Inclua o caso padrão `_` para opcoes invalidas

### Proposta de Teste
- **Caso básico:** Opcao: `1` — Saida: `Cadastrando...`
- **Caso de borda:** Opcao: `5` — Saida: `Opcao invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Exibimos o menu
print("=== Menu ===")
print("1 - Cadastrar")
print("2 - Consultar")
print("3 - Sair")

# Pedimos a opcao do usuario
# "option" = opcao
option = int(input("Escolha uma opcao: "))

# Usamos match/case para verificar a opcao escolhida
match option:
    case 1:
        # Opcao 1 selecionada
        print("Cadastrando...")
    case 2:
        # Opcao 2 selecionada
        print("Consultando...")
    case 3:
        # Opcao 3 selecionada
        print("Saindo do sistema. Ate logo!")
    case _:
        # Qualquer outro valor — opcao invalida
        # _ e o caso padrao (coringa)
        print("Opcao invalida! Escolha 1, 2 ou 3.")
```

---

## Exercício 2 — Dia da Semana — Nível: Básico

### Enunciado
Peca um número de 1 a 7 e exiba o dia da semana correspondente usando match/case.

### Dicas
- 1=Segunda, 2=Terca, ..., 7=Domingo
- Use `case _:` para números invalidos

### Proposta de Teste
- **Caso básico:** Número: `4` — Saida: `Quinta-feira`
- **Caso de borda:** Número: `0` — Saida: `Numero invalido`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o numero do dia
# "day" = dia
day = int(input("Numero do dia (1-7): "))

# match/case para cada dia da semana
match day:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terca-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        # Caso padrao para numeros fora de 1-7
        print("Numero invalido! Digite de 1 a 7.")
```

---

## Exercício 3 — Estacao do Ano — Nível: Básico

### Enunciado
Peca o número do mes (1-12) e exiba a estacao do ano correspondente. Use `|` para combinar meses na mesma estacao.

### Dicas
- Verao: meses 1, 2, 3. Outono: 4, 5, 6. Inverno: 7, 8, 9. Primavera: 10, 11, 12.
- Use `case 1 | 2 | 3:` para combinar

### Proposta de Teste
- **Caso básico:** Mes: `7` — Saida: `Inverno`
- **Caso de borda:** Mes: `13` — Saida: `Mes invalido`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o numero do mes
# "month" = mes
month = int(input("Numero do mes (1-12): "))

# Usamos | para combinar varios valores no mesmo case
match month:
    case 1 | 2 | 3:
        # Meses 1, 2 ou 3 = Verao (no Brasil)
        print("Verao")
    case 4 | 5 | 6:
        # Meses 4, 5 ou 6 = Outono
        print("Outono")
    case 7 | 8 | 9:
        # Meses 7, 8 ou 9 = Inverno
        print("Inverno")
    case 10 | 11 | 12:
        # Meses 10, 11 ou 12 = Primavera
        print("Primavera")
    case _:
        print("Mes invalido! Digite de 1 a 12.")
```

---

## Exercício 4 — Conversor de Notas — Nível: Básico

### Enunciado
Peca uma nota de 0 a 10 (inteira) e converta para conceito usando match/case: 10=A+, 9=A, 8=B+, 7=B, 6=C, 5=D, abaixo de 5=F.

### Dicas
- Use `int()` para garantir número inteiro
- Use `case _:` para notas abaixo de 5

### Proposta de Teste
- **Caso básico:** Nota: `8` — Saida: `Conceito: B+`
- **Caso de borda:** Nota: `3` — Saida: `Conceito: F`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a nota (inteira)
# "grade" = nota
grade = int(input("Nota (0 a 10): "))

# Convertemos para conceito
match grade:
    case 10:
        # "concept" = conceito
        concept = "A+"
    case 9:
        concept = "A"
    case 8:
        concept = "B+"
    case 7:
        concept = "B"
    case 6:
        concept = "C"
    case 5:
        concept = "D"
    case _:
        # Qualquer nota abaixo de 5 (ou invalida)
        concept = "F"

print(f"Nota: {grade} — Conceito: {concept}")
```

---

## Exercício 5 — Calculadora com match/case — Nível: Intermediario

### Enunciado
Crie uma calculadora que peca dois números e a operação (+, -, *, /). Use match/case para a operação.

### Dicas
- Leia a operação como string
- Trate divisao por zero dentro do case da divisao

### Proposta de Teste
- **Caso básico:** 10 * 3 — Saida: `30.0`
- **Caso de borda:** 10 / 0 — Saida: `Erro: divisao por zero`
- **Caso de borda:** Operação: `%` — Saida: `Operacao invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos os dados
# "num_a" = primeiro numero, "num_b" = segundo numero
num_a = float(input("Primeiro numero: "))
num_b = float(input("Segundo numero: "))

# "op" = operacao (abreviacao de operation)
op = input("Operacao (+, -, *, /): ")

# Usamos match/case para a operacao
match op:
    case "+":
        print(f"Resultado: {num_a + num_b}")
    case "-":
        print(f"Resultado: {num_a - num_b}")
    case "*":
        print(f"Resultado: {num_a * num_b}")
    case "/":
        # Verificamos divisao por zero com if dentro do case
        if num_b != 0:
            print(f"Resultado: {num_a / num_b}")
        else:
            print("Erro: divisao por zero!")
    case _:
        print(f"Operacao '{op}' invalida! Use +, -, * ou /")
```

---

## Exercício 6 — Tipo Sanguineo — Nível: Intermediario

### Enunciado
Peca o tipo sanguineo do usuario (A, B, AB, O) e exiba para quais tipos ele pode doar. Use match/case.

### Dicas
- A: doa para A e AB. B: doa para B e AB. AB: doa para AB. O: doa para todos.
- Converta para maiusculas com `.upper()` para aceitar minusculas

### Proposta de Teste
- **Caso básico:** Tipo: `O` — Saida: `Pode doar para: A, B, AB, O`
- **Caso de borda:** Tipo: `ab` (minusculo) — Saida: `Pode doar para: AB`
- **Caso de borda:** Tipo: `X` — Saida: `Tipo sanguineo invalido`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o tipo sanguineo e convertemos para maiusculas
# "blood_type" = tipo sanguineo
blood_type = input("Tipo sanguineo (A, B, AB, O): ").upper()

# Verificamos o tipo e exibimos para quem pode doar
match blood_type:
    case "A":
        print("Pode doar para: A, AB")
    case "B":
        print("Pode doar para: B, AB")
    case "AB":
        print("Pode doar para: AB")
    case "O":
        # Tipo O e doador universal
        print("Pode doar para: A, B, AB, O (doador universal)")
    case _:
        print(f"Tipo sanguineo '{blood_type}' invalido!")
```

---

## Exercício 7 — Classificação de Filme — Nível: Intermediario

### Enunciado
Peca a classificação indicativa de um filme (L, 10, 12, 14, 16, 18) e a idade do espectador. Verifique se pode assistir.

### Dicas
- Use match/case para a classificação
- Dentro de cada case, compare a idade com o limite

### Proposta de Teste
- **Caso básico:** Classificação: `14`, Idade: `16` — Saida: `Pode assistir`
- **Caso de borda:** Classificação: `18`, Idade: `15` — Saida: `Nao pode assistir`
- **Caso de borda:** Classificação: `L` — Saida: `Pode assistir` (livre para todos)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos a classificacao e a idade
# "rating" = classificacao indicativa
rating = input("Classificacao indicativa (L, 10, 12, 14, 16, 18): ").upper()

# "viewer_age" = idade do espectador (viewer = espectador)
viewer_age = int(input("Idade do espectador: "))

# Verificamos a classificacao
# "min_age" = idade minima
match rating:
    case "L":
        min_age = 0  # Livre para todos
    case "10":
        min_age = 10
    case "12":
        min_age = 12
    case "14":
        min_age = 14
    case "16":
        min_age = 16
    case "18":
        min_age = 18
    case _:
        min_age = -1  # Classificacao invalida

# Verificamos se pode assistir
if min_age == -1:
    print("Classificacao invalida!")
elif viewer_age >= min_age:
    print("Pode assistir!")
else:
    print(f"Nao pode assistir. Idade minima: {min_age} anos.")
```

---

## Exercício 8 — Conversor de Unidades — Nível: Intermediario

### Enunciado
Peca um valor e a unidade de origem (km, m, cm). Converta para as outras duas unidades usando match/case.

### Dicas
- km para m: multiplicar por 1000. m para cm: multiplicar por 100.
- Use match/case para identificar a unidade de origem

### Proposta de Teste
- **Caso básico:** Valor: `1.5`, Unidade: `km` — m: 1500.0, cm: 150000.0
- **Caso de borda:** Unidade: `mm` — Saida: `Unidade nao suportada`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o valor e a unidade
# "value" = valor, "unit" = unidade
value = float(input("Valor: "))
unit = input("Unidade (km, m, cm): ").lower()

# Convertemos usando match/case
match unit:
    case "km":
        # Quilometros para metros e centimetros
        # "meters" = metros, "centimeters" = centimetros
        meters = value * 1000
        centimeters = meters * 100
        print(f"{value} km = {meters} m = {centimeters} cm")
    case "m":
        # Metros para quilometros e centimetros
        # "kilometers" = quilometros
        kilometers = value / 1000
        centimeters = value * 100
        print(f"{value} m = {kilometers} km = {centimeters} cm")
    case "cm":
        # Centimetros para metros e quilometros
        meters = value / 100
        kilometers = meters / 1000
        print(f"{value} cm = {meters} m = {kilometers} km")
    case _:
        print(f"Unidade '{unit}' nao suportada. Use km, m ou cm.")
```

---

## Exercício 9 — Pedra, Papel, Tesoura — Nível: Avancado

### Enunciado
Crie o jogo Pedra, Papel, Tesoura. O computador sempre escolhe "pedra" (por enquanto — quando aprendermos o módulo random, poderemos tornar aleatorio). O usuario escolhe sua jogada e o programa determina o resultado.

### Dicas
- Use match/case para a jogada do usuario
- Dentro de cada case, compare com a jogada do computador
- Pedra ganha de tesoura, tesoura ganha de papel, papel ganha de pedra

### Proposta de Teste
- **Caso básico:** Jogada: `papel` — Saida: `Voce ganhou!` (papel ganha de pedra)
- **Caso de borda:** Jogada: `pedra` — Saida: `Empate!`
- **Caso de borda:** Jogada: `tesoura` — Saida: `Voce perdeu!`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# O computador sempre escolhe pedra (por enquanto)
# "computer_choice" = escolha do computador
computer_choice = "pedra"

# Pedimos a jogada do usuario
# "player_choice" = escolha do jogador (player = jogador)
player_choice = input("Sua jogada (pedra/papel/tesoura): ").lower()

print(f"Computador escolheu: {computer_choice}")

# Verificamos o resultado usando match/case
match player_choice:
    case "pedra":
        # Pedra vs pedra = empate
        print("Empate!")
    case "papel":
        # Papel vs pedra = jogador ganha (papel cobre pedra)
        print("Voce ganhou! Papel cobre pedra.")
    case "tesoura":
        # Tesoura vs pedra = computador ganha (pedra quebra tesoura)
        print("Voce perdeu! Pedra quebra tesoura.")
    case _:
        print(f"Jogada '{player_choice}' invalida! Use pedra, papel ou tesoura.")
```

---

## Exercício 10 — Sistema de Atendimento — Nível: Avancado

### Enunciado
Crie um sistema de atendimento com as opcoes: 1-Suporte Técnico, 2-Financeiro, 3-Comercial, 4-Ouvidoria, 0-Sair. Exiba uma mensagem personalizada para cada departamento, incluindo horario de atendimento e telefone ficticio.

### Dicas
- Use match/case para cada opcao
- Cada case pode ter várias linhas de print

### Proposta de Teste
- **Caso básico:** Opcao: `2` — Saida: informações do departamento Financeiro
- **Caso de borda:** Opcao: `0` — Saida: mensagem de despedida
- **Caso de borda:** Opcao: `9` — Saida: `Opcao invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Exibimos o menu de atendimento
print("=== Central de Atendimento ===")
print("1 - Suporte Tecnico")
print("2 - Financeiro")
print("3 - Comercial")
print("4 - Ouvidoria")
print("0 - Sair")
print("==============================")

# Pedimos a opcao
# "option" = opcao
option = int(input("Escolha um departamento: "))

# Direcionamos para o departamento escolhido
match option:
    case 1:
        print("\n--- Suporte Tecnico ---")
        print("Horario: Segunda a Sexta, 8h as 18h")
        print("Telefone: (11) 1234-0001")
        print("Aguarde, voce sera atendido em breve.")
    case 2:
        print("\n--- Financeiro ---")
        print("Horario: Segunda a Sexta, 9h as 17h")
        print("Telefone: (11) 1234-0002")
        print("Para boletos e pagamentos, tenha seu CPF em maos.")
    case 3:
        print("\n--- Comercial ---")
        print("Horario: Segunda a Sabado, 8h as 20h")
        print("Telefone: (11) 1234-0003")
        print("Conheca nossos planos e promocoes!")
    case 4:
        print("\n--- Ouvidoria ---")
        print("Horario: Segunda a Sexta, 10h as 16h")
        print("Telefone: (11) 1234-0004")
        print("Sua opiniao e muito importante para nos.")
    case 0:
        print("\nObrigado por ligar! Ate a proxima.")
    case _:
        print("\nOpcao invalida! Escolha de 0 a 4.")
```

---

[<- Voltar ao Módulo 13](13-seletores-match-case.md) | [Glossário](00-glossário.md)
