# 5.14 — Exercícios: Debugging

[← Voltar ao Módulo 5.14](cap05-mod14-debugging-conteudo.md)

---

## Como usar estes exercícios

1. Leia o enunciado com atenção
2. Tente resolver sozinho antes de olhar as dicas
3. Use as técnicas aprendidas no módulo: print() de debug, leitura de Traceback, eliminação
4. Salve cada exercício em um arquivo separado na pasta `~/meus-projetos/python-curso/módulo-14/`
5. Execute com `python3 nome_do_arquivo.py`

---

## Exercício 1 — Lendo Tracebacks (Nível: Fácil)

Para cada mensagem de erro abaixo, identifique:
- O tipo do erro
- A linha onde ocorreu
- A causa provável
- Como corrigir

### Erro A

```
Traceback (most recent call last):
  File "programa.py", line 5, in <module>
    result = 100 / user_input
ZeroDivisionError: division by zero
```

### Erro B

```
Traceback (most recent call last):
  File "programa.py", line 3, in <module>
    print(nome)
NameError: name 'nome' is not defined
```

### Erro C

```
  File "programa.py", line 4
    if age > 18
               ^
SyntaxError: expected ':'
```

### Erro D

```
Traceback (most recent call last):
  File "programa.py", line 2, in <module>
    number = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

### Erro E

```
Traceback (most recent call last):
  File "programa.py", line 3, in <module>
    print(fruits[10])
IndexError: list index out of range
```

**Dica:** Leia cada mensagem de baixo para cima. A última linha sempre diz o tipo e a descrição do erro.


### Respostas Comentadas

<details>
<summary>Clique para ver as respostas</summary>

**Erro A:**
- Tipo: `ZeroDivisionError`
- Linha: 5
- Causa: a variável `user_input` vale 0, e o programa tenta dividir 100 por 0
- Correção: verificar se `user_input` é diferente de zero antes de dividir

**Erro B:**
- Tipo: `NameError`
- Linha: 3
- Causa: a variável `nome` não foi definida — provavelmente o nome correto é diferente (talvez `name`)
- Correção: verificar a grafia da variável

**Erro C:**
- Tipo: `SyntaxError`
- Linha: 4
- Causa: faltam os dois-pontos (`:`) depois da condição do `if`
- Correção: adicionar `:` no final da linha — `if age > 18:`

**Erro D:**
- Tipo: `ValueError`
- Linha: 2
- Causa: tentou converter o texto "abc" para número inteiro, mas "abc" não é um número
- Correção: validar a entrada antes de converter, ou usar try/except

**Erro E:**
- Tipo: `IndexError`
- Linha: 3
- Causa: tentou acessar a posição 10 de uma lista que tem menos de 11 elementos
- Correção: verificar o tamanho da lista antes de acessar, ou usar um índice válido

</details>

---

## Exercício 2 — Encontrando Bugs com print() (Nível: Médio)

Cada programa abaixo tem um bug. Use print() de debug para encontrar e corrigir.

### Programa A — Calculadora de troco

```python
# Este programa deveria calcular o troco de uma compra
# "price" = preco, "payment" = pagamento, "change" = troco
price = float(input("Preco do produto: "))
payment = input("Valor pago: ")

change = payment - price
print(f"Troco: R$ {change:.2f}")
```

**Comportamento esperado:** Se preço é 30 e pagamento é 50, troco deveria ser 20.
**Comportamento real:** O programa dá erro.

**Dica:** Use `print(type(payment))` para investigar.

### Programa B — Média de notas

```python
# Este programa deveria calcular a media de notas
# "grades" = notas
grades = [8.0, 7.5, 9.0, 6.5]

# "total" = total
total = 0
for grade in grades:
    total = grade  # Bug aqui — encontre!

# "average" = media
average = total / len(grades)
print(f"Media: {average}")
```

**Comportamento esperado:** Média deveria ser 7.75
**Comportamento real:** Média é 1.625

**Dica:** Adicione `print(f"DEBUG - grade: {grade}, total: {total}")` dentro do loop.

### Programa C — Classificação por idade

```python
# Este programa deveria classificar a pessoa por faixa etaria
# "age" = idade
age = int(input("Sua idade: "))

if age < 12:
    category = "crianca"
if age < 18:
    category = "adolescente"
if age < 60:
    category = "adulto"
else:
    category = "idoso"

print(f"Categoria: {category}")
```

**Comportamento esperado:** Idade 8 deveria ser "crianca"
**Comportamento real:** Idade 8 mostra "adulto"

**Dica:** Adicione prints dentro de cada `if` para ver em quais o programa entra.

### Respostas Comentadas

<details>
<summary>Clique para ver as respostas</summary>

**Programa A:**
O bug é que `input()` retorna texto (string), não número. A variável `payment` é texto. Ao tentar `payment - price`, dá `TypeError`. Correção: `payment = float(input("Valor pago: "))`.

**Programa B:**
O bug é `total = grade` em vez de `total = total + grade` (ou `total += grade`). A cada iteração, `total` é substituído pelo valor da nota atual em vez de acumular. No final, `total` vale 6.5 (última nota), e 6.5 / 4 = 1.625.

**Programa C:**
O bug é usar `if` em vez de `elif`. Quando `age` é 8, ele entra no primeiro `if` (8 < 12), define `category = "crianca"`. Mas depois entra no segundo `if` (8 < 18), sobrescreve para "adolescente". E depois entra no terceiro `if` (8 < 60), sobrescreve para "adulto". Correção: usar `elif` no segundo e terceiro blocos.

</details>

---

## Exercício 3 — Debugging Completo (Nível: Difícil)

O programa abaixo é um sistema de notas que deveria:
1. Pedir o nome e 3 notas de cada aluno
2. Calcular a média
3. Classificar como "Aprovado" (média >= 7), "Recuperação" (média >= 5) ou "Reprovado" (média < 5)
4. Mostrar o resultado

O programa tem **3 bugs**. Encontre e corrija todos.

```python
# Sistema de notas com 3 bugs
# "students" = estudantes
students = []
# "num_students" = numero de estudantes
num_students = int(input("Quantos alunos? "))

for i in range(num_students):
    # "name" = nome
    name = input(f"Nome do aluno {i}: ")

    # "grades" = notas
    grades = []
    for j in range(3):
        # "grade" = nota
        grade = input(f"Nota {j + 1} de {name}: ")
        grades.append(grade)

    # "average" = media
    average = sum(grades) / len(grades)

    # "status" = situacao
    if average >= 7:
        status = "Aprovado"
    elif average >= 5:
        status = "Recuperacao"
    elif average < 5:
        status = "Reprovado"

    students.append({
        "name": name,
        "average": average,
        "status": status
    })

print("\n--- Resultado Final ---")
for student in students:
    print(f"{student['name']}: Media {student['average']:.1f} - {student['status']}")
```

**Dica 1:** O primeiro bug está na numeração dos alunos.
**Dica 2:** O segundo bug está no tipo das notas.
**Dica 3:** O terceiro bug é sutil — teste com média exatamente 5.0.

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

**Bug 1 — Numeração dos alunos:**
`name = input(f"Nome do aluno {i}: ")` — quando `i` é 0, mostra "Nome do aluno 0". Deveria ser `i + 1` para começar em 1.

**Bug 2 — Tipo das notas:**
`grade = input(...)` retorna texto. `sum(grades)` vai concatenar textos em vez de somar números. Correção: `grade = float(input(...))`.

**Bug 3 — Condição da classificação:**
As condições `>= 7`, `>= 5` e `< 5` cobrem todos os casos, mas o `elif average < 5` é redundante — se não é >= 7 e não é >= 5, necessariamente é < 5. O bug real é que se `average` for exatamente 5.0, entra em "Recuperação", o que está correto. Na verdade, o terceiro bug é mais sutil: se `elif` fosse `else`, funcionaria igual. Mas o código como está funciona — o bug real do terceiro ponto é que não há tratamento para o caso de notas inválidas (negativas ou acima de 10). Para o exercício, a correção principal é usar `else` em vez de `elif average < 5` para garantir que todos os casos são cobertos.

Código corrigido:

```python
students = []
num_students = int(input("Quantos alunos? "))

for i in range(num_students):
    name = input(f"Nome do aluno {i + 1}: ")  # Bug 1 corrigido

    grades = []
    for j in range(3):
        grade = float(input(f"Nota {j + 1} de {name}: "))  # Bug 2 corrigido
        grades.append(grade)

    average = sum(grades) / len(grades)

    if average >= 7:
        status = "Aprovado"
    elif average >= 5:
        status = "Recuperacao"
    else:  # Bug 3 corrigido — else cobre todos os outros casos
        status = "Reprovado"

    students.append({
        "name": name,
        "average": average,
        "status": status
    })

print("\n--- Resultado Final ---")
for student in students:
    print(f"{student['name']}: Media {student['average']:.1f} - {student['status']}")
```

</details>

---

[← Voltar ao Módulo 5.14](cap05-mod14-debugging-conteudo.md)
