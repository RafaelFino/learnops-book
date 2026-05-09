# Exercícios — Módulo 10: Indentacao e Escopo

[<- Voltar ao Módulo 10](10-indentacao-escopo.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve seu código na pasta `~/meus-projetos/python-curso/modulo-10/` e execute com `python3 nome_do_arquivo.py`.
>
> **Nota:** Alguns exercícios usam `if` e `for`, que serao aprofundados nos módulos 12 e 14. Aqui o foco e praticar a indentacao — entenda que `if condicao:` executa o bloco indentado quando a condição e verdadeira, e `for item in lista:` repete o bloco para cada item.

---

## Exercício 1 — Identificando Blocos — Nível: Básico

### Enunciado
Observe o código abaixo e, sem executar, diga qual sera a saida. Depois execute para conferir.

```python
age = 20
if age >= 18:
    print("Maior de idade")
    print("Pode votar")
print("Fim")
```

### Dicas
- As duas primeiras linhas de print estão indentadas — pertencem ao bloco do if
- A ultima linha não esta indentada — executa sempre
- A condição `age >= 18` e verdadeira (20 >= 18)

### Proposta de Teste
- **Caso único:** A saida deve ser tres linhas: `Maior de idade`, `Pode votar`, `Fim`

### Resposta Comentada

> **Importante:** Tente prever a saida antes de executar!

```python
# "age" = idade — definimos a idade como 20
age = 20

# if verifica se age e maior ou igual a 18
# Como 20 >= 18 e verdadeiro, o bloco indentado sera executado
if age >= 18:
    # Esta linha pertence ao bloco do if (esta indentada com 4 espacos)
    print("Maior de idade")
    # Esta linha tambem pertence ao bloco do if (mesma indentacao)
    print("Pode votar")

# Esta linha NAO pertence ao bloco do if (nao esta indentada)
# Ela executa sempre, independente da condicao
print("Fim")
```

---

## Exercício 2 — Corrigindo IndentationError — Nível: Básico

### Enunciado
O código abaixo tem um erro de indentacao. Identifique o erro e corrija.

```python
name = "Maria"
if name == "Maria":
print("Ola, Maria!")
```

### Dicas
- Depois de `if condicao:`, a proxima linha precisa estar indentada
- Use 4 espacos de indentacao

### Proposta de Teste
- **Caso único:** Apos a correcao, a saida deve ser `Ola, Maria!`

### Resposta Comentada

> **Importante:** Tente corrigir sozinho primeiro!

```python
# "name" = nome
name = "Maria"

# Depois do if e dos dois pontos (:), o bloco precisa estar indentado
# O erro original era: a linha do print nao estava indentada
if name == "Maria":
    # CORRECAO: adicionamos 4 espacos de indentacao
    # Agora esta linha pertence ao bloco do if
    print("Ola, Maria!")
```

---

## Exercício 3 — Dentro e Fora do Bloco — Nível: Básico

### Enunciado
Crie um programa que defina uma variável `temperature` (temperatura) com valor 35. Se a temperatura for maior que 30, exiba "Esta quente!" (dentro do bloco). Independente da temperatura, exiba "Tenha um bom dia!" (fora do bloco).

### Dicas
- A mensagem "Esta quente!" deve estar indentada (dentro do if)
- A mensagem "Tenha um bom dia!" não deve estar indentada (fora do if)

### Proposta de Teste
- **Caso básico:** Com temperature=35 — Saida: `Esta quente!` e `Tenha um bom dia!`
- **Caso de borda:** Mude para temperature=20 — Saida: apenas `Tenha um bom dia!`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# "temperature" = temperatura
temperature = 35

# Verificamos se a temperatura e maior que 30
if temperature > 30:
    # Esta linha esta DENTRO do bloco do if (indentada)
    # So executa se a temperatura for maior que 30
    print("Esta quente!")

# Esta linha esta FORA do bloco do if (nao indentada)
# Executa sempre, independente da condicao
print("Tenha um bom dia!")
```

---

## Exercício 4 — Multiplas Linhas no Bloco — Nível: Básico

### Enunciado
Crie um programa com uma variável `is_raining` (esta chovendo) com valor `True`. Se estiver chovendo, exiba tres mensagens (todas dentro do bloco): "Esta chovendo!", "Leve um guarda-chuva!" e "Cuidado com as pocas!". Depois, fora do bloco, exiba "Ate logo!".

### Dicas
- Todas as tres mensagens de chuva devem estar no mesmo nível de indentacao
- A mensagem "Ate logo!" não deve estar indentada

### Proposta de Teste
- **Caso básico:** Com is_raining=True — Saida: 4 linhas (3 sobre chuva + "Ate logo!")
- **Caso de borda:** Mude para is_raining=False — Saida: apenas "Ate logo!"

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# "is_raining" = esta chovendo — True significa verdadeiro (sim, esta chovendo)
is_raining = True

# Verificamos se esta chovendo
if is_raining:
    # Todas estas linhas pertencem ao bloco do if
    # Todas tem a mesma indentacao (4 espacos)
    print("Esta chovendo!")
    print("Leve um guarda-chuva!")
    print("Cuidado com as pocas!")

# Esta linha esta fora do bloco — executa sempre
print("Ate logo!")
```

---

## Exercício 5 — Encontrando o Erro — Nível: Intermediario

### Enunciado
O código abaixo tem um erro de indentacao que não gera erro, mas muda o comportamento. Identifique o problema e explique o que acontece.

```python
score = 50
if score >= 60:
    print("Aprovado!")
print("Parabens!")
```

### Dicas
- Análise: "Parabéns!" deveria aparecer apenas para aprovados ou sempre?
- A indentacao de "Parabéns!" determina se ela pertence ao bloco do if ou não

### Proposta de Teste
- **Caso único:** Com score=50, a saida e apenas `Parabens!` — mas provavelmente a intencao era que "Parabéns!" so aparecesse para aprovados

### Resposta Comentada

> **Importante:** Tente analisar sozinho primeiro!

```python
# "score" = pontuacao
score = 50

# O if verifica se a pontuacao e >= 60
# Como 50 < 60, o bloco do if NAO executa
if score >= 60:
    # Esta linha so executa se score >= 60
    print("Aprovado!")

# PROBLEMA: esta linha NAO esta indentada, entao executa SEMPRE
# Provavelmente a intencao era que "Parabens!" so aparecesse para aprovados
# Se fosse esse o caso, deveria estar indentada dentro do bloco do if
print("Parabens!")

# CORRECAO (se "Parabens!" deveria ser so para aprovados):
# if score >= 60:
#     print("Aprovado!")
#     print("Parabens!")  # <-- agora esta dentro do bloco
```

---

## Exercício 6 — Blocos Aninhados — Nível: Intermediario

### Enunciado
Crie um programa com duas variáveis: `has_ticket` (tem ingresso) com valor `True` e `age` (idade) com valor 15. Verifique se a pessoa tem ingresso. Se tiver, verifique se a idade e maior ou igual a 18. Exiba mensagens apropriadas em cada nível.

### Dicas
- O segundo if fica dentro do primeiro (indentacao dupla: 8 espacos)
- Cada nível de bloco adiciona 4 espacos

### Proposta de Teste
- **Caso básico:** has_ticket=True, age=15 — Saida: "Tem ingresso!" e "Menor de idade — entrada não permitida"
- **Caso de borda:** has_ticket=True, age=20 — Saida: "Tem ingresso!" e "Maior de idade — pode entrar!"

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# "has_ticket" = tem ingresso
has_ticket = True

# "age" = idade
age = 15

# Primeiro nivel: verificamos se tem ingresso
if has_ticket:
    # Nivel 1 de indentacao (4 espacos)
    print("Tem ingresso!")

    # Segundo nivel: verificamos a idade (if dentro de if)
    if age >= 18:
        # Nivel 2 de indentacao (8 espacos)
        print("Maior de idade — pode entrar!")
    else:
        # Nivel 2 de indentacao (8 espacos)
        # else = "senao" — executa quando a condicao do if e falsa
        print("Menor de idade — entrada nao permitida")

# Fora de todos os blocos (sem indentacao)
print("Fim da verificacao")
```

---

## Exercício 7 — Corrigindo Código Baguncado — Nível: Intermediario

### Enunciado
O código abaixo esta com a indentacao toda errada. Corrija para que funcione corretamente.

```python
name = input("Seu nome: ")
    age = int(input("Sua idade: "))
if age >= 18:
print("Ola,", name)
    print("Voce e maior de idade")
        print("Fim")
```

### Dicas
- Linhas de código principal (fora de blocos) não devem ter indentacao
- Apenas linhas dentro de blocos (if, for, def) devem ser indentadas
- O `print("Fim")` provavelmente deveria estar fora do bloco

### Proposta de Teste
- **Caso básico:** Nome: `Ana`, Idade: `20` — Saida: `Ola, Ana`, `Voce e maior de idade`, `Fim`

### Resposta Comentada

> **Importante:** Tente corrigir sozinho primeiro!

```python
# Linha principal — sem indentacao (nivel 0)
# "name" = nome
name = input("Seu nome: ")

# Linha principal — sem indentacao (nivel 0)
# CORRECAO: removemos a indentacao que nao deveria existir
# "age" = idade
age = int(input("Sua idade: "))

# Condicional — sem indentacao (nivel 0)
if age >= 18:
    # Dentro do bloco do if — indentacao de 4 espacos (nivel 1)
    # CORRECAO: adicionamos indentacao ao primeiro print
    print("Ola,", name)
    # Dentro do bloco do if — mesma indentacao (nivel 1)
    print("Voce e maior de idade")

# Fora do bloco — sem indentacao (nivel 0)
# CORRECAO: removemos a indentacao excessiva
print("Fim")
```

---

## Exercício 8 — Usando pass — Nível: Intermediario

### Enunciado
Crie um programa que verifique se um número e positivo, negativo ou zero. Para o caso positivo, exiba "Positivo". Para negativo e zero, use `pass` (placeholder — ainda não implementado) e exiba uma mensagem dizendo que a funcionalidade sera implementada depois.

### Dicas
- `pass` e uma palavra-chave que não faz nada — serve como placeholder
- Use if/elif/else (sera aprofundado no módulo 12)

### Proposta de Teste
- **Caso básico:** Número: `5` — Saida: `Positivo`
- **Caso de borda:** Número: `0` — Saida: `(funcionalidade para zero sera implementada depois)`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# "number" = numero
number = int(input("Digite um numero: "))

# Verificamos se e positivo
if number > 0:
    # Bloco implementado — exibe "Positivo"
    print("Positivo")

# elif = "else if" = "senao se" — verifica outra condicao
elif number < 0:
    # Bloco com pass — placeholder para implementacao futura
    # pass nao faz nada, mas evita o IndentationError
    pass
    print("(funcionalidade para negativo sera implementada depois)")

# else = "senao" — quando nenhuma condicao anterior e verdadeira
else:
    # Bloco com pass — placeholder
    pass
    print("(funcionalidade para zero sera implementada depois)")
```

---

## Exercício 9 — Prevendo a Saida — Nível: Avancado

### Enunciado
Sem executar o código, preveja qual sera a saida. Depois execute para conferir.

```python
x = 10
y = 5

if x > y:
    print("A")
    if x > 8:
        print("B")
    print("C")
print("D")
```

### Dicas
- Análise nível por nível de indentacao
- x=10, y=5: x > y e verdadeiro, x > 8 e verdadeiro
- Identifique quais prints estão dentro de qual bloco

### Proposta de Teste
- **Caso único:** A saida deve ser: `A`, `B`, `C`, `D` (nessa ordem, cada um em uma linha)

### Resposta Comentada

> **Importante:** Tente prever a saida antes de executar!

```python
# Definimos duas variaveis
x = 10
y = 5

# Primeiro if: x > y? 10 > 5? Sim! Entra no bloco
if x > y:
    # Nivel 1 — pertence ao primeiro if
    # Executa porque x > y e verdadeiro
    print("A")

    # Segundo if (aninhado): x > 8? 10 > 8? Sim! Entra no bloco
    if x > 8:
        # Nivel 2 — pertence ao segundo if
        # Executa porque x > 8 e verdadeiro
        print("B")

    # Nivel 1 — pertence ao primeiro if (nao ao segundo!)
    # Executa porque x > y e verdadeiro
    print("C")

# Nivel 0 — fora de todos os blocos
# Executa sempre
print("D")

# Saida: A, B, C, D
```

---

## Exercício 10 — Criando Estrutura Completa — Nível: Avancado

### Enunciado
Crie um programa que peca o nome e a nota de um aluno. Se a nota for maior ou igual a 7, exiba "Aprovado" e uma mensagem de parabéns. Se for menor que 7 mas maior ou igual a 5, exiba "Recuperacao". Se for menor que 5, exiba "Reprovado". No final, sempre exiba "Resultado processado".

### Dicas
- Use if/elif/else com indentacao correta
- Cada bloco pode ter mais de uma linha
- A mensagem final deve estar fora de todos os blocos

### Proposta de Teste
- **Caso básico:** Nota: `8` — Saida: `Aprovado`, `Parabens, [nome]!`, `Resultado processado`
- **Caso de borda:** Nota: `5` — Saida: `Recuperacao`, `Resultado processado`
- **Caso de borda:** Nota: `3` — Saida: `Reprovado`, `Resultado processado`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Pedimos o nome e a nota do aluno
# "student_name" = nome do aluno
student_name = input("Nome do aluno: ")

# "grade" = nota — convertemos para float (notas podem ter decimais)
grade = float(input("Nota: "))

# Verificamos a faixa da nota usando if/elif/else
# Cada bloco esta indentado com 4 espacos
if grade >= 7:
    # Bloco para aprovados (nota >= 7)
    print("Aprovado")
    print(f"Parabens, {student_name}!")

elif grade >= 5:
    # Bloco para recuperacao (nota >= 5 e < 7)
    # elif = "else if" = "senao se"
    print("Recuperacao")

else:
    # Bloco para reprovados (nota < 5)
    # else = "senao" — quando nenhuma condicao anterior e verdadeira
    print("Reprovado")

# Esta linha esta FORA de todos os blocos (sem indentacao)
# Executa sempre, independente da nota
print("Resultado processado")
```

---

[<- Voltar ao Módulo 10](10-indentacao-escopo.md) | [Glossário](00-glossario.md)
