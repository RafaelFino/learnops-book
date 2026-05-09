# 11 — Operadores Logicos e Matematicos

[<- Anterior: Indentacao e Escopo](10-indentacao-escopo.md) | [Glossário](00-glossario.md) | [Próximo: Condicionais ->](12-condicionais.md)

---

## Introdução

Neste módulo, vamos aprender a fazer o computador calcular e comparar valores. Operadores sao símbolos que dizem ao Python o que fazer com os valores: somar, subtrair, comparar, verificar condições.

Pense nos operadores como as ações que você faz na cozinha: cortar, misturar, medir. Os valores (números, textos) sao os ingredientes, e os operadores sao as ações que você aplica sobre eles para obter um resultado.

Se você não tem muita familiaridade com matemática, não se preocupe. Cada operação sera explicada com calma, usando exemplos do dia a dia, antes de mostrar como funciona no Python.

> **Dica:** Consulte o [Glossário](00-glossario.md) e a [Referência de Operadores](00-glossario-comandos.md#operadores-matematicos) sempre que precisar.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-11/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-11`
4. Execute: `python3 nome_do_arquivo.py`

---

## Operadores Matematicos

Operadores matematicos realizam cálculos com números. Antes de cada operador, vamos explicar a operação matemática em termos simples.

### Soma (+) — Adicao

Somar e juntar quantidades. Se você tem 3 macas e ganha mais 2, fica com 5. Em Python, usamos o sinal `+`:

```python
# Soma: juntar dois valores
# "apples" = macas
apples = 3 + 2
print("3 + 2 =", apples)

# Somando variaveis
# "price_a" = preco do item A, "price_b" = preco do item B
price_a = 10.50
price_b = 7.30
# "total" = total (soma dos precos)
total = price_a + price_b
print("Total:", total)
```

**Saida esperada:**
```
3 + 2 = 5
Total: 17.8
```

### Subtracao (-) — Tirar de um valor

Subtrair e tirar uma quantidade de outra. Se você tem 10 reais e gasta 3, sobram 7. Em Python, usamos o sinal `-`:

```python
# Subtracao: tirar um valor de outro
# "balance" = saldo, "expense" = despesa, "remaining" = restante
balance = 100.00
expense = 35.50
remaining = balance - expense
print("Saldo restante:", remaining)
```

**Saida esperada:**
```
Saldo restante: 64.5
```

### Multiplicacao (*) — Repetir um valor

Multiplicar e somar um número várias vezes. Se você compra 4 pacotes de cafe a 8 reais cada, o total e 4 vezes 8 = 32 reais. Em Python, usamos o asterisco `*`:

```python
# Multiplicacao: repetir um valor varias vezes
# "unit_price" = preco unitario, "quantity" = quantidade
unit_price = 8.00
quantity = 4
# "total" = total (preco vezes quantidade)
total = unit_price * quantity
print("Total:", total)
```

**Saida esperada:**
```
Total: 32.0
```

### Divisao (/) — Repartir igualmente

Dividir e repartir um valor em partes iguais. Se você tem 20 reais e quer dividir entre 4 pessoas, cada uma recebe 5 reais. Em Python, usamos a barra `/`. O resultado sempre e um número decimal (float):

```python
# Divisao: repartir um valor em partes iguais
# "total_amount" = valor total, "people" = pessoas
total_amount = 20.00
people = 4
# "share" = parte de cada um
share = total_amount / people
print("Cada pessoa recebe:", share)
print("Tipo do resultado:", type(share))
```

**Saida esperada:**
```
Cada pessoa recebe: 5.0
Tipo do resultado: <class 'float'>
```

> **Nota:** A divisao com `/` sempre retorna um float, mesmo quando o resultado e um número "redondo". `20 / 4` resulta em `5.0`, não `5`.

### Divisao Inteira (//) — Apenas a parte inteira

A [divisao inteira](00-glossario-a-d.md#divisao-inteira) e como a divisao normal, mas descarta a parte decimal — fica apenas com o número inteiro. Imagine que você tem 7 pizzas para dividir entre 2 pessoas: cada uma fica com 3 pizzas inteiras (o pedaco que sobra e ignorado). Em Python, usamos `//`:

```python
# Divisao inteira: resultado sem casas decimais
# "pizzas" = pizzas, "people" = pessoas
pizzas = 7
people = 2
# "whole_pizzas" = pizzas inteiras por pessoa
# // descarta a parte decimal
whole_pizzas = pizzas // people
print("Pizzas inteiras por pessoa:", whole_pizzas)
```

**Saida esperada:**
```
Pizzas inteiras por pessoa: 3
```

### Módulo (%) — O resto da divisao

O [módulo](00-glossario-j-p.md#módulo-operação-matemática) retorna o **resto** de uma divisao. Quando você divide 10 balas entre 3 amigos, cada um fica com 3 balas e **sobra 1**. Esse 1 que sobra e o módulo. Em Python, usamos `%`:

```python
# Modulo: o resto da divisao
# "candies" = balas, "friends" = amigos
candies = 10
friends = 3
# "leftover" = sobra (o resto)
# 10 dividido por 3 = 3 com resto 1
leftover = candies % friends
print("Sobram", leftover, "bala(s)")
```

**Saida esperada:**
```
Sobram 1 bala(s)
```

> **Dica prática:** O módulo e muito útil para verificar se um número e par ou impar. Se `numero % 2` resulta em `0`, o número e par (divisivel por 2 sem resto). Se resulta em `1`, e impar.

### Exponenciacao (**) — Potência

A [exponenciacao](00-glossario-e-i.md#exponenciacao) e multiplicar um número por ele mesmo várias vezes. "2 elevado a 3" significa 2 vezes 2 vezes 2, que da 8. Em Python, usamos `**`:

```python
# Exponenciacao: multiplicar um numero por ele mesmo
# "base" = base (o numero), "exponent" = expoente (quantas vezes)
base = 2
exponent = 3
# 2 ** 3 = 2 * 2 * 2 = 8
# "result" = resultado
result = base ** exponent
print(f"{base} elevado a {exponent} = {result}")

# Outro exemplo: area de um quadrado
# A area de um quadrado e o lado vezes o lado (lado ao quadrado)
# "side" = lado
side = 5
# "area" = area
# side ** 2 = side * side = 5 * 5 = 25
area = side ** 2
print(f"Area do quadrado de lado {side}: {area}")
```

**Saida esperada:**
```
2 elevado a 3 = 8
Area do quadrado de lado 5: 25
```

### Tabela resumo dos operadores matematicos

| Operador | Nome | O que faz | Exemplo | Resultado |
|----------|------|-----------|---------|-----------|
| `+` | Soma | Junta valores | `5 + 3` | `8` |
| `-` | Subtracao | Tira um valor | `10 - 4` | `6` |
| `*` | Multiplicacao | Repete um valor | `3 * 4` | `12` |
| `/` | Divisao | Reparte igualmente | `7 / 2` | `3.5` |
| `//` | Divisao inteira | Parte inteira da divisao | `7 // 2` | `3` |
| `%` | Módulo | Resto da divisao | `10 % 3` | `1` |
| `**` | Exponenciacao | Potência | `2 ** 3` | `8` |

---

## Operadores de Comparação

Operadores de comparação comparam dois valores e retornam `True` (verdadeiro) ou `False` (falso). Sao essenciais para tomar decisoes no programa (que veremos no módulo 12).

```python
# Operadores de comparacao — todos retornam True ou False
# "a" e "b" sao os valores que estamos comparando
a = 10
b = 5

# == verifica se sao IGUAIS (dois sinais de igual)
print("a == b:", a == b)    # 10 e igual a 5? Nao -> False

# != verifica se sao DIFERENTES (! significa "nao")
print("a != b:", a != b)    # 10 e diferente de 5? Sim -> True

# > verifica se o primeiro e MAIOR que o segundo
print("a > b:", a > b)      # 10 e maior que 5? Sim -> True

# < verifica se o primeiro e MENOR que o segundo
print("a < b:", a < b)      # 10 e menor que 5? Nao -> False

# >= verifica se e MAIOR OU IGUAL
print("a >= b:", a >= b)    # 10 e maior ou igual a 5? Sim -> True

# <= verifica se e MENOR OU IGUAL
print("a <= b:", a <= b)    # 10 e menor ou igual a 5? Nao -> False
```

**Saida esperada:**
```
a == b: False
a != b: True
a > b: True
a < b: False
a >= b: True
a <= b: False
```

> **Atenção:** Não confunda `=` (atribuição — guarda valor) com `==` (comparação — verifica igualdade). `age = 25` guarda o valor 25. `age == 25` pergunta "age e igual a 25?".

---

## Operadores Logicos

Operadores logicos combinam condições. Sao usados quando você precisa verificar mais de uma coisa ao mesmo tempo.

### and — E (ambos verdadeiros)

`and` retorna `True` apenas quando **ambas** as condições sao verdadeiras. E como dizer "preciso de guarda-chuva E casaco" — so levo os dois se estiver chovendo E frio ao mesmo tempo:

```python
# and: ambas as condicoes precisam ser verdadeiras
# "age" = idade, "has_id" = tem documento
age = 20
has_id = True

# A pessoa pode entrar se tiver 18+ E tiver documento
# "can_enter" = pode entrar
can_enter = age >= 18 and has_id
print("Pode entrar:", can_enter)
```

**Saida esperada:**
```
Pode entrar: True
```

### or — Ou (pelo menos um verdadeiro)

`or` retorna `True` quando **pelo menos uma** das condições e verdadeira. E como dizer "aceito pagar com dinheiro OU cartao" — qualquer um dos dois serve:

```python
# or: pelo menos uma condicao precisa ser verdadeira
# "has_cash" = tem dinheiro, "has_card" = tem cartao
has_cash = False
has_card = True

# Pode pagar se tiver dinheiro OU cartao
# "can_pay" = pode pagar
can_pay = has_cash or has_card
print("Pode pagar:", can_pay)
```

**Saida esperada:**
```
Pode pagar: True
```

### not — Não (inverte o valor)

`not` inverte o valor: `True` vira `False` e `False` vira `True`. E como dizer "não esta chovendo" — se esta chovendo (True), "não esta chovendo" e False:

```python
# not: inverte o valor logico
# "is_raining" = esta chovendo
is_raining = False

# not inverte: se nao esta chovendo, podemos sair
# "can_go_out" = pode sair
can_go_out = not is_raining
print("Pode sair:", can_go_out)
```

**Saida esperada:**
```
Pode sair: True
```

### Combinando operadores logicos

Você pode combinar `and`, `or` e `not` em expressoes mais complexas:

```python
# Combinando operadores logicos
# "age" = idade, "is_student" = e estudante, "has_coupon" = tem cupom
age = 16
is_student = True
has_coupon = False

# Tem desconto se: (for estudante E menor de 18) OU tiver cupom
# "has_discount" = tem desconto
has_discount = (is_student and age < 18) or has_coupon
print("Tem desconto:", has_discount)
```

**Saida esperada:**
```
Tem desconto: True
```

> **Nota:** Use parenteses `()` para deixar claro qual parte da expressao deve ser avaliada primeiro. Isso evita confusao e torna o código mais legivel.

---

## Precedencia de Operadores — Quem Vem Primeiro?

Quando uma expressao tem vários operadores, o Python segue uma ordem de prioridade (precedencia) para decidir qual operação fazer primeiro. E como na matemática: multiplicacao vem antes da soma.

Pense em uma fila de prioridade no banco: alguns clientes tem prioridade e sao atendidos primeiro, independente de quando chegaram.

### Ordem de precedencia (do mais prioritario ao menos)

| Prioridade | Operador | Exemplo |
|-----------|----------|---------|
| 1 (mais alta) | `**` | Exponenciacao |
| 2 | `*`, `/`, `//`, `%` | Multiplicacao, divisao, módulo |
| 3 | `+`, `-` | Soma, subtracao |
| 4 | `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparação |
| 5 | `not` | Negacao lógica |
| 6 | `and` | E logico |
| 7 (mais baixa) | `or` | Ou logico |

### Exemplo prático

```python
# Sem parenteses: Python segue a precedencia
# Multiplicacao (*) vem antes da soma (+)
# "result" = resultado
result = 2 + 3 * 4
# Python calcula: 3 * 4 = 12, depois 2 + 12 = 14
print("2 + 3 * 4 =", result)

# Com parenteses: voce controla a ordem
# Os parenteses forcam a soma a ser feita primeiro
result_with_parens = (2 + 3) * 4
# Python calcula: (2 + 3) = 5, depois 5 * 4 = 20
print("(2 + 3) * 4 =", result_with_parens)
```

**Saida esperada:**
```
2 + 3 * 4 = 14
(2 + 3) * 4 = 20
```

> **Dica:** Na duvida, use parenteses. Eles tornam o código mais claro e evitam erros de precedencia. Mesmo quando não sao obrigatórios, parenteses ajudam quem esta lendo o código a entender a intencao.

---

## Resumo Geral

| Categoria | Operadores | Retorna |
|-----------|-----------|---------|
| Matematicos | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Número |
| Comparação | `==`, `!=`, `>`, `<`, `>=`, `<=` | True/False |
| Logicos | `and`, `or`, `not` | True/False |

---

## Para Saber Mais

- [W3Schools — Python Operators](https://www.w3schools.com/python/python_operators.asp) — _Todos os operadores_
- [W3Schools — Python Arithmetic Operators](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp) — _Operadores matematicos_
- [W3Schools — Python Comparison Operators](https://www.w3schools.com/python/gloss_python_comparison_operators.asp) — _Operadores de comparacao_
- [Documentação Python — Expressoes](https://docs.python.org/pt-br/3/reference/expressions.html) — _Referencia completa_

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre `/` e `//`?**
R: `/` e a divisao normal que retorna decimal: `7 / 2 = 3.5`. `//` e a divisao inteira que descarta os decimais: `7 // 2 = 3`. Use `/` quando precisa do resultado exato e `//` quando so quer a parte inteira.

**P: O que e "módulo" na programação?**
R: E o resto de uma divisao. Quando você divide 10 por 3, o resultado e 3 com resto 1. Esse resto (1) e o módulo. Em Python: `10 % 3 = 1`. E como dividir balas entre amigos — o módulo e o que sobra.

**P: Como sei se um número e par ou impar?**
R: Use o módulo: `numero % 2`. Se o resultado for `0`, o número e par (divisivel por 2 sem resto). Se for `1`, e impar. Exemplo: `8 % 2 = 0` (par), `7 % 2 = 1` (impar).

**P: O que e "exponenciacao"?**
R: E multiplicar um número por ele mesmo várias vezes. "2 elevado a 3" (escrito `2 ** 3`) significa 2 x 2 x 2 = 8. O primeiro número e a base e o segundo e o expoente (quantas vezes multiplicar).

**P: O que e um "operando"?**
R: E o valor sobre o qual o operador atua. Na expressao `5 + 3`, os operandos sao `5` e `3`, e o operador e `+`. Pense nos operandos como os ingredientes e no operador como a ação (misturar, cortar).

**P: O que e uma "expressao"?**
R: E uma combinacao de valores, variáveis e operadores que o Python avalia para produzir um resultado. `2 + 3` e uma expressao que resulta em `5`. `age >= 18` e uma expressao que resulta em `True` ou `False`.

**P: Por que `=` e `==` sao diferentes?**
R: `=` e atribuição (guarda um valor): `age = 25`. `==` e comparação (verifica igualdade): `age == 25` retorna True ou False. Confundir os dois e um dos erros mais comuns entre iniciantes.

**P: Posso comparar strings?**
R: Sim! `"abc" == "abc"` retorna `True`. `"abc" != "xyz"` retorna `True`. Você também pode comparar com `<` e `>`, que comparam pela ordem alfabetica.

**P: O que significa "precedencia"?**
R: E a ordem em que o Python resolve as operações. Multiplicacao tem precedencia sobre soma, então `2 + 3 * 4` resulta em `14` (3*4 primeiro, depois 2+12). Use parenteses para mudar a ordem.

**P: Quando devo usar parenteses?**
R: Sempre que quiser garantir a ordem das operações ou quando a expressao ficar confusa. `(2 + 3) * 4` e mais claro que depender da precedencia. Na duvida, use parenteses — nunca e demais.

**P: O que `and` faz exatamente?**
R: `and` retorna `True` apenas quando AMBOS os lados sao verdadeiros. `True and True = True`. `True and False = False`. `False and False = False`. E como dizer "preciso de A E B" — so funciona se tiver os dois.

**P: O que `or` faz exatamente?**
R: `or` retorna `True` quando PELO MENOS UM lado e verdadeiro. `True or False = True`. `False or True = True`. `False or False = False`. E como dizer "aceito A OU B" — qualquer um serve.

**P: O que `not` faz?**
R: `not` inverte o valor logico. `not True = False`. `not False = True`. E como dizer "não" — inverte a afirmacao.

**P: Posso dividir por zero?**
R: Não! `10 / 0` gera um `ZeroDivisionError`. Dividir por zero não faz sentido matematicamente, e o Python avisa com um erro. Sempre verifique se o divisor não e zero antes de dividir.

**P: O que e "divisao inteira"?**
R: E uma divisao que retorna apenas a parte inteira do resultado, descartando os decimais. `7 // 2 = 3` (e não 3.5). E como dividir pizzas inteiras entre pessoas — cada um fica com pizzas completas, sem fatias.

**P: Posso usar operadores com strings?**
R: Alguns! `+` concatena (junta) strings: `"Ola" + " " + "Mundo"`. `*` repete: `"ha" * 3 = "hahaha"`. Mas `-`, `/` e outros não funcionam com strings.

**P: O que e `!=`?**
R: Significa "diferente de" ou "não igual a". `5 != 3` retorna `True` porque 5 e diferente de 3. O `!` e lido como "não", então `!=` e "não igual".

**P: Posso combinar operadores matematicos e logicos na mesma expressao?**
R: Sim! Exemplo: `age >= 18 and balance > 0`. Primeiro o Python resolve as comparacoes (`age >= 18` e `balance > 0`), depois aplica o `and`. A precedencia garante a ordem correta.

**P: O que acontece se eu esquecer um operador?**
R: O Python mostra um `SyntaxError`. Por exemplo, `5 3` (sem operador entre os números) gera erro porque o Python não sabe o que fazer com dois números lado a lado.

**P: E normal achar operadores confusos no inicio?**
R: Sim, especialmente módulo (`%`), divisao inteira (`//`) e exponenciacao (`**`). Com prática, você vai se acostumar. Consulte a tabela de referência sempre que precisar e faca os exercícios — a prática e o melhor caminho.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

**[Acessar Exercícios do Módulo 11](11-operadores-exercicios.md)**

---

[<- Anterior: Indentacao e Escopo](10-indentacao-escopo.md) | [Glossário](00-glossario.md) | [Próximo: Condicionais ->](12-condicionais.md)
