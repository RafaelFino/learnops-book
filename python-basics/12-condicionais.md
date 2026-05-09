# 12 — Condicionais: if, elif e else

[<- Anterior: Operadores](11-operadores.md) | [Glossário](00-glossário.md) | [Próximo: Seletores match/case ->](13-seletores-match-case.md)

---

## Introdução

Ate agora, todos os nossos programas executavam as instruções de cima para baixo, uma apos a outra, sem desvios. Mas na vida real, tomamos decisoes o tempo todo: "se estiver chovendo, levo guarda-chuva; senao, levo oculos de sol". Programas também precisam tomar decisoes.

Neste módulo, você vai aprender a fazer seus programas **escolherem caminhos diferentes** dependendo de condições. Isso e feito com as estruturas `if` (se), `elif` (senao se) e `else` (senao).

Pense nas condicionais como uma encruzilhada: o programa chega a um ponto onde precisa decidir qual caminho seguir, e a decisao depende de uma condição ser verdadeira ou falsa.

> **Dica:** Este módulo depende dos módulos 10 (indentacao) e 11 (operadores). Se não se sentir seguro nesses temas, revise-os antes de continuar.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-12/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-12`
4. Execute: `python3 nome_do_arquivo.py`

---

## if — "Se" (Uma Condição Simples)

A estrutura `if` executa um bloco de código **apenas quando a condição e verdadeira**. Se a condição for falsa, o bloco e ignorado e o programa continua.

Pense assim: "Se estiver chovendo, leve o guarda-chuva." Se não estiver chovendo, você simplesmente ignora essa instrução e segue em frente.

```python
# Exemplo basico de if
# "temperature" = temperatura
temperature = 35

# if verifica se a condicao e verdadeira
# Se temperature > 30 for True, o bloco indentado executa
# Se for False, o bloco e ignorado
if temperature > 30:
    # Este bloco so executa se a temperatura for maior que 30
    print("Esta muito quente hoje!")
    print("Beba bastante agua.")

# Esta linha esta fora do if — executa sempre
print("Tenha um bom dia!")
```

**Saida esperada (com temperature = 35):**
```
Esta muito quente hoje!
Beba bastante agua.
Tenha um bom dia!
```

**Se mudarmos para temperature = 20:**
```
Tenha um bom dia!
```

> **Nota:** Lembre-se do módulo 10: o bloco do `if` e definido pela indentacao. Todas as linhas indentadas apos o `if:` pertencem ao bloco. Quando a indentacao volta ao nível anterior, o bloco terminou.

### Anatomia do if

```
if condicao:          <-- a condicao e uma expressao que resulta em True ou False
    instrucao_1       <-- bloco indentado: executa apenas se a condicao for True
    instrucao_2       <-- ainda dentro do bloco
codigo_fora           <-- fora do bloco: executa sempre
```

A condição pode ser qualquer expressao que resulte em `True` ou `False`:
- Comparacoes: `age >= 18`, `name == "Maria"`, `price < 100`
- Variáveis booleanas: `is_active`, `has_discount`
- Combinacoes com operadores logicos: `age >= 18 and has_id`

---

## if/else — "Se... Senao" (Dois Caminhos)

Quando você precisa de dois caminhos — um para quando a condição e verdadeira e outro para quando e falsa — use `if/else`:

Pense assim: "Se estiver chovendo, leve guarda-chuva; **senao**, leve oculos de sol."

```python
# if/else: dois caminhos possiveis
# "age" = idade
age = int(input("Digite sua idade: "))

# Se a idade for >= 18, executa o primeiro bloco
# Senao (else), executa o segundo bloco
if age >= 18:
    # Bloco do if — executa quando a condicao e verdadeira
    print("Voce e maior de idade.")
    print("Pode tirar carteira de motorista.")
else:
    # Bloco do else — executa quando a condicao e falsa
    print("Voce e menor de idade.")
    print("Ainda nao pode tirar carteira.")

# Fora dos blocos — executa sempre
print("Obrigado por usar o sistema!")
```

**Saida esperada (se digitar 20):**
```
Voce e maior de idade.
Pode tirar carteira de motorista.
Obrigado por usar o sistema!
```

**Saida esperada (se digitar 15):**
```
Voce e menor de idade.
Ainda nao pode tirar carteira.
Obrigado por usar o sistema!
```

> **Nota:** O `else` não tem condição — ele e o "caso contrario". Tudo que não entrou no `if` cai no `else`.

---

## if/elif/else — "Se... Senao Se... Senao" (Multiplos Caminhos)

Quando você tem mais de duas opcoes, use `elif` (abreviacao de "else if", que significa "senao se") para criar caminhos adicionais:

Pense assim: "Se a nota for >= 9, conceito A; senao se for >= 7, conceito B; senao se for >= 5, conceito C; senao, conceito D."

```python
# if/elif/else: multiplos caminhos
# "grade" = nota
grade = float(input("Digite sua nota (0 a 10): "))

# O Python verifica cada condicao de cima para baixo
# Quando encontra a primeira verdadeira, executa o bloco e pula o resto
if grade >= 9:
    # Executa se nota >= 9
    # "concept" = conceito
    concept = "A"
    print("Excelente!")
elif grade >= 7:
    # Executa se nota >= 7 (e < 9, porque a condicao anterior ja foi verificada)
    concept = "B"
    print("Bom trabalho!")
elif grade >= 5:
    # Executa se nota >= 5 (e < 7)
    concept = "C"
    print("Pode melhorar.")
else:
    # Executa se nenhuma condicao anterior for verdadeira (nota < 5)
    concept = "D"
    print("Precisa estudar mais.")

# Fora dos blocos — executa sempre
print(f"Sua nota: {grade} — Conceito: {concept}")
```

**Saida esperada (se digitar 8.5):**
```
Bom trabalho!
Sua nota: 8.5 — Conceito: B
```

### Como o Python avalia as condições

O Python verifica as condições **de cima para baixo**. Quando encontra a primeira condição verdadeira, executa o bloco correspondente e **pula todas as outras**. Se nenhuma condição for verdadeira, executa o `else` (se existir).

E como um funil: o valor "cai" pela primeira abertura que encontra.

---

## Condicionais Aninhadas — if Dentro de if

Você pode colocar um `if` dentro de outro `if`. Isso se chama "aninhamento" e e útil quando você precisa verificar uma condição dentro de outra:

```python
# Condicionais aninhadas: if dentro de if
# "has_ticket" = tem ingresso, "age" = idade
has_ticket = input("Tem ingresso? (sim/nao): ")
age = int(input("Sua idade: "))

# Primeiro verificamos se tem ingresso
if has_ticket == "sim":
    # Dentro do primeiro if: verificamos a idade
    print("Ingresso verificado.")

    if age >= 18:
        # Dentro do segundo if (8 espacos de indentacao)
        print("Entrada permitida. Boa diversao!")
    else:
        # Dentro do else do segundo if
        print("Entrada permitida com acompanhante adulto.")
else:
    # Bloco do else do primeiro if
    print("Voce precisa de um ingresso para entrar.")

print("Fim da verificacao.")
```

> **Atenção:** Condicionais aninhadas podem ficar confusas se tiverem muitos níveis. Tente limitar a dois níveis de aninhamento. Se precisar de mais, considere reorganizar a lógica.

---

## Condições Compostas — Combinando com and, or, not

Em vez de aninhar vários `if`, você pode combinar condições usando os operadores logicos que aprendeu no módulo 11:

```python
# Condicoes compostas com and e or
# "age" = idade, "has_id" = tem documento
age = int(input("Idade: "))
has_id_input = input("Tem documento? (sim/nao): ")
has_id = has_id_input == "sim"

# Usando and: ambas as condicoes precisam ser verdadeiras
if age >= 18 and has_id:
    print("Acesso liberado.")
else:
    print("Acesso negado.")

    # Explicamos o motivo usando not
    if not (age >= 18):
        # not inverte: se NAO tem 18+, e menor de idade
        print("Motivo: menor de idade.")
    if not has_id:
        # not inverte: se NAO tem documento
        print("Motivo: sem documento.")
```

```python
# Usando or: pelo menos uma condicao precisa ser verdadeira
# "payment_method" = forma de pagamento
payment_method = input("Forma de pagamento (dinheiro/cartao/pix): ")

if payment_method == "dinheiro" or payment_method == "cartao" or payment_method == "pix":
    print("Pagamento aceito!")
else:
    print("Forma de pagamento nao aceita.")
```

---

## Exemplos Práticos

### Exemplo 1: Classificação de idade

```python
# Classificando uma pessoa pela faixa etaria
# "age" = idade
age = int(input("Digite a idade: "))

if age < 0:
    # Idade negativa nao faz sentido
    print("Idade invalida!")
elif age <= 12:
    # 0 a 12 anos
    # "category" = categoria
    category = "Crianca"
elif age <= 17:
    # 13 a 17 anos
    category = "Adolescente"
elif age <= 59:
    # 18 a 59 anos
    category = "Adulto"
else:
    # 60 anos ou mais
    category = "Idoso"

if age >= 0:
    print(f"Idade: {age} — Categoria: {category}")
```

### Exemplo 2: Calculadora com operação escolhida

```python
# Calculadora que pede a operacao ao usuario
# "number_a" = primeiro numero, "number_b" = segundo numero
number_a = float(input("Primeiro numero: "))
number_b = float(input("Segundo numero: "))

# "operation" = operacao
operation = input("Operacao (+, -, *, /): ")

if operation == "+":
    # "result" = resultado
    result = number_a + number_b
    print(f"{number_a} + {number_b} = {result}")
elif operation == "-":
    result = number_a - number_b
    print(f"{number_a} - {number_b} = {result}")
elif operation == "*":
    result = number_a * number_b
    print(f"{number_a} * {number_b} = {result}")
elif operation == "/":
    # Verificamos se o divisor nao e zero antes de dividir
    if number_b != 0:
        result = number_a / number_b
        print(f"{number_a} / {number_b} = {result}")
    else:
        print("Erro: nao e possivel dividir por zero!")
else:
    print("Operacao invalida! Use +, -, * ou /")
```

---

## Resumo

| Estrutura | Quando usar | Exemplo |
|-----------|-------------|---------|
| `if` | Uma condição, um caminho | `if age >= 18:` |
| `if/else` | Dois caminhos (sim ou não) | `if age >= 18: ... else: ...` |
| `if/elif/else` | Multiplos caminhos | `if grade >= 9: ... elif grade >= 7: ...` |
| Aninhado | Condição dentro de condição | `if has_ticket: if age >= 18:` |
| Composto | Combinar condições | `if age >= 18 and has_id:` |

---

## Para Saber Mais

- [W3Schools — Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — _Condicionais em Python_
- [W3Schools — Python Operators](https://www.w3schools.com/python/python_operators.asp) — _Operadores de comparação e logicos_
- [Documentação Python — Controle de Fluxo](https://docs.python.org/pt-br/3/tutorial/controlflow.html) — _Referencia oficial_

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre if e elif?**
R: `if` inicia uma nova verificacao de condição. `elif` (else if = senao se) e uma condição alternativa que so e verificada se o `if` anterior foi falso. Pense no `elif` como "se a primeira opcao não serviu, tente esta".

**P: Posso ter if sem else?**
R: Sim! O `else` e opcional. Se você so precisa fazer algo quando a condição e verdadeira e nada quando e falsa, use apenas `if` sem `else`.

**P: Posso ter vários elif?**
R: Sim, quantos precisar! Você pode ter `if`, seguido de quantos `elif` quiser, e opcionalmente um `else` no final. O Python verifica cada condição de cima para baixo.

**P: O else e obrigatório?**
R: Não. O `else` e opcional. Use-o quando precisar de um "caso contrario" — algo que acontece quando nenhuma condição anterior foi verdadeira.

**P: O que acontece se duas condições forem verdadeiras ao mesmo tempo?**
R: O Python executa apenas o bloco da **primeira** condição verdadeira que encontrar (de cima para baixo) e pula todas as outras. Por isso a ordem das condições importa.

**P: Posso usar if sem elif, direto com else?**
R: Sim! `if/else` (sem elif) e a forma mais simples: dois caminhos, um para verdadeiro e outro para falso.

**P: O que sao "condicionais aninhadas"?**
R: E quando você coloca um `if` dentro de outro `if`. O if interno so e verificado se o if externo for verdadeiro. Use com moderacao — muitos níveis de aninhamento tornam o código difícil de ler.

**P: Quando devo usar aninhamento vs condições compostas (and/or)?**
R: Se as condições sao independentes (verificar A e depois verificar B dentro de A), use aninhamento. Se as condições precisam ser verdadeiras ao mesmo tempo, use `and`. Na duvida, prefira `and/or` — e mais legivel.

**P: Posso comparar strings com if?**
R: Sim! `if name == "Maria":` verifica se o nome e exatamente "Maria". Cuidado: a comparação diferencia maiusculas de minusculas. "Maria" e "maria" sao diferentes.

**P: Como ignoro maiusculas/minusculas na comparação?**
R: Converta para minusculas antes de comparar: `if name.lower() == "maria":`. Assim, "Maria", "MARIA" e "maria" sao todos aceitos.

**P: O que e o operador ternario?**
R: E uma forma de escrever um if/else em uma única linha: `resultado = "par" if numero % 2 == 0 else "impar"`. E útil para expressoes simples, mas para iniciantes, o if/else normal e mais claro.

**P: Posso colocar if dentro de elif?**
R: Sim, você pode aninhar condicionais em qualquer nível. Mas tente manter no máximo 2-3 níveis para não perder a legibilidade.

**P: O que acontece se eu esquecer os dois pontos (:) depois do if?**
R: O Python mostra um `SyntaxError`. Os dois pontos sao obrigatórios — eles indicam que um bloco indentado vem a seguir.

**P: Posso ter um bloco vazio no if?**
R: Sim, usando `pass`. Se você ainda não sabe o que colocar no bloco, use `if condicao: pass` como placeholder. Isso evita o `IndentationError`.

**P: O que e "curto-circuito" em condições?**
R: Quando o Python usa `and`, se a primeira condição for `False`, ele nem verifica a segunda (porque o resultado ja sera `False`). Com `or`, se a primeira for `True`, ele nem verifica a segunda. Isso e chamado de avaliacao em curto-circuito.

**P: Posso usar números como condição no if?**
R: Sim! O Python converte automaticamente para booleano. `if 0:` nunca executa (0 e False). `if 1:` ou `if 42:` sempre executa (qualquer número diferente de zero e True). Mas para clareza, prefira condições explicitas.

**P: Posso usar strings como condição?**
R: Sim! String vazia `""` e `False`, qualquer string com conteúdo e `True`. `if nome:` verifica se o nome não esta vazio. Mas `if nome != "":` e mais explicito para iniciantes.

**P: Qual a diferença entre `=` e `==` dentro do if?**
R: `=` e atribuição (guarda valor) e NAO pode ser usado dentro do if. `==` e comparação (verifica igualdade) e e o que você usa no if. Escrever `if age = 18:` gera erro — o correto e `if age == 18:`.

**P: Posso ter código antes e depois do if na mesma linha?**
R: Não antes, mas o bloco pode estar na mesma linha: `if True: print("ola")`. Porém, para legibilidade, prefira colocar o bloco na linha seguinte com indentacao.

**P: E normal errar a lógica das condições no inicio?**
R: Muito normal! Condições sao um dos pontos onde mais se erra no inicio. Teste seu programa com diferentes valores para garantir que todos os caminhos funcionam. Use a proposta de teste de cada exercício para verificar.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta. Este e um módulo complexo — os exercícios sao mais numerosos e progressivos.

**[Acessar Exercícios do Módulo 12](12-condicionais-exercícios.md)**

---

[<- Anterior: Operadores](11-operadores.md) | [Glossário](00-glossário.md) | [Próximo: Seletores match/case ->](13-seletores-match-case.md)
