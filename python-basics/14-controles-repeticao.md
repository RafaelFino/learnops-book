# 14 — Controles de Repetição: for e while

[<- Anterior: Seletores match/case](13-seletores-match-case.md) | [Glossário](00-glossário.md) | [Próximo: Funções ->](15-funções.md)

---

## Introdução

Ate agora, cada instrução do seu programa executa apenas uma vez. Mas e se você precisar repetir uma ação várias vezes? Por exemplo: exibir os números de 1 a 100, somar todos os itens de uma lista de compras, ou pedir ao usuario que digite dados ate que ele decida parar.

Fazer isso manualmente (escrevendo 100 linhas de print) seria impraticavel. Para isso existem os **loops** (lacos de repetição) — estruturas que repetem um bloco de código automaticamente.

Pense nos loops como dar voltas em uma pista de corrida. Cada volta e uma **iteração** (repetição). Você continua dando voltas ate completar o número desejado (loop `for`) ou ate cansar (loop `while`).

Neste módulo, vamos aprender dois tipos de loop:
- **for** — repete um número definido de vezes ou para cada item de uma coleção
- **while** — repete enquanto uma condição for verdadeira

> **Dica:** Este módulo depende dos módulos 10 (indentacao), 11 (operadores) e 12 (condicionais). Revise-os se necessário.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-14/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-14`
4. Execute: `python3 nome_do_arquivo.py`

---

## Termos Importantes

Antes de começar, vamos explicar alguns termos que aparecem muito quando falamos de loops:

- **Iteração** (do ingles "iteration"): cada repetição do loop. Se o loop executa 5 vezes, ele faz 5 iteracoes. E como cada volta que você da em uma pista de corrida.

- **Contador** (do ingles "counter"): uma variável que conta quantas vezes algo aconteceu. Comeca em um valor (geralmente 0) e aumenta a cada iteração. E como contar nos dedos.

- **Incremento** (do ingles "increment"): a ação de aumentar o valor de uma variável, geralmente de 1 em 1. E como subir um degrau de cada vez em uma escada.

- **Acumulador** (do ingles "accumulator"): uma variável que vai somando valores ao longo do loop. E como um cofrinho onde você coloca moedas a cada volta — no final, tem o total acumulado.

---

## Loop for — Repetir para Cada Item

O loop `for` repete um bloco de código **para cada item** de uma sequência (lista, string, range). E o loop mais usado em Python.

### for com range() — Repetir um número de vezes

A função `range()` gera uma sequência de números. Combinada com `for`, permite repetir algo um número específico de vezes:

```python
# Repetindo 5 vezes usando for com range()
# range(5) gera os numeros: 0, 1, 2, 3, 4
# "i" e a variavel que recebe cada numero a cada iteracao (volta)
# "i" vem de "index" (indice) — e uma convencao comum em programacao
for i in range(5):
    # Este bloco executa 5 vezes (uma para cada numero de 0 a 4)
    print(f"Iteracao {i}")
```

**Saida esperada:**
```
Iteracao 0
Iteracao 1
Iteracao 2
Iteracao 3
Iteracao 4
```

> **Nota:** `range(5)` gera números de 0 ate 4 (5 números no total). O número 5 não e incluido. E como a regra do fatiamento de strings: o fim não e incluido.

### range() com inicio e fim

Você pode especificar onde começar e onde terminar:

```python
# range(inicio, fim) — gera numeros de inicio ate fim-1
# Contando de 1 a 10
for number in range(1, 11):
    # "number" = numero — recebe cada valor de 1 a 10
    print(number, end=" ")
```

**Saida esperada:**
```
1 2 3 4 5 6 7 8 9 10 
```

### range() com passo

Você pode definir o incremento (passo) entre os números:

```python
# range(inicio, fim, passo) — pula de "passo" em "passo"
# Contando de 0 a 20 de 2 em 2 (numeros pares)
# "step" = passo
for number in range(0, 21, 2):
    print(number, end=" ")
```

**Saida esperada:**
```
0 2 4 6 8 10 12 14 16 18 20 
```

```python
# Contagem regressiva: passo negativo
for number in range(10, 0, -1):
    # range(10, 0, -1) gera: 10, 9, 8, ..., 1
    print(number, end=" ")
print("Fogo!")
```

**Saida esperada:**
```
10 9 8 7 6 5 4 3 2 1 Fogo!
```

### for com strings — Percorrendo cada caractere

```python
# Percorrendo cada caractere de uma string
# "word" = palavra
word = "Python"

# "char" = caractere (abreviacao de character)
# A cada iteracao, char recebe o proximo caractere da string
for char in word:
    print(char)
```

**Saida esperada:**
```
P
y
t
h
o
n
```

### for com listas — Percorrendo cada item

```python
# Percorrendo cada item de uma lista
# "fruits" = frutas
fruits = ["maca", "banana", "laranja", "uva"]

# "fruit" = fruta — recebe cada item da lista a cada iteracao
for fruit in fruits:
    print(f"Eu gosto de {fruit}")
```

**Saida esperada:**
```
Eu gosto de maca
Eu gosto de banana
Eu gosto de laranja
Eu gosto de uva
```

> **Nota:** Listas serao aprofundadas no módulo 19. Por enquanto, saiba que uma lista e uma coleção de itens entre colchetes `[]`, separados por virgula.

---

## Loop while — Repetir Enquanto uma Condição For Verdadeira

O loop `while` repete um bloco **enquanto** uma condição for verdadeira. Quando a condição se torna falsa, o loop para.

Pense assim: "enquanto a panela não estiver fervendo, continue mexendo". Você não sabe quantas vezes vai mexer — depende de quando a agua ferver.

```python
# Contando de 1 a 5 com while
# "counter" = contador — comeca em 1
counter = 1

# while verifica a condicao antes de cada iteracao
# Enquanto counter for <= 5, o bloco executa
while counter <= 5:
    print(f"Contagem: {counter}")
    # Incrementamos o contador em 1 a cada iteracao
    # Sem isso, o loop nunca pararia (loop infinito!)
    counter = counter + 1

print("Fim da contagem!")
```

**Saida esperada:**
```
Contagem: 1
Contagem: 2
Contagem: 3
Contagem: 4
Contagem: 5
Fim da contagem!
```

> **Atenção:** Sempre garanta que a condição do while vai se tornar falsa em algum momento. Se a condição nunca mudar, o loop roda para sempre (loop infinito) e o programa trava. Se isso acontecer, pressione `Ctrl + C` no terminal para interromper.

### while com input — Repetir ate o usuario decidir parar

```python
# Programa que repete ate o usuario digitar "sair"
# "user_input" = entrada do usuario
user_input = ""

# Enquanto o usuario nao digitar "sair", continua pedindo
while user_input != "sair":
    user_input = input("Digite algo (ou 'sair' para encerrar): ")
    print(f"Voce digitou: {user_input}")

print("Programa encerrado.")
```

---

## break — Interrompendo o Loop

O comando `break` ("quebrar/interromper") para o loop imediatamente, independente da condição:

```python
# Procurando um numero especifico
# "target" = alvo (o numero que estamos procurando)
target = 7

for number in range(1, 20):
    print(f"Verificando {number}...")
    if number == target:
        # Encontramos! Paramos o loop com break
        print(f"Encontrei o {target}!")
        break

print("Busca encerrada.")
```

**Saida esperada:**
```
Verificando 1...
Verificando 2...
...
Verificando 7...
Encontrei o 7!
Busca encerrada.
```

---

## continue — Pulando para a Proxima Iteração

O comando `continue` ("continuar") pula o restante do bloco atual e vai direto para a proxima iteração:

```python
# Exibindo apenas numeros impares de 1 a 10
for number in range(1, 11):
    # Se o numero for par, pula para o proximo
    if number % 2 == 0:
        continue  # Pula o print abaixo e vai para a proxima iteracao
    print(number, end=" ")
```

**Saida esperada:**
```
1 3 5 7 9 
```

---

## Padrões Comuns com Loops

### Padrão 1: Contador

```python
# Contando quantos numeros pares existem de 1 a 20
# "even_count" = contagem de pares (even = par, count = contagem)
even_count = 0

for number in range(1, 21):
    if number % 2 == 0:
        # Incrementamos o contador quando encontramos um par
        even_count = even_count + 1
        # Forma abreviada: even_count += 1 (faz a mesma coisa)

print(f"Quantidade de numeros pares de 1 a 20: {even_count}")
```

**Saida esperada:**
```
Quantidade de numeros pares de 1 a 20: 10
```

### Padrão 2: Acumulador (Soma)

```python
# Somando todos os numeros de 1 a 100
# "total" = total (acumulador — comeca em 0 e vai somando)
total = 0

for number in range(1, 101):
    # A cada iteracao, somamos o numero atual ao total
    total = total + number
    # Forma abreviada: total += number

print(f"Soma de 1 a 100: {total}")
```

**Saida esperada:**
```
Soma de 1 a 100: 5050
```

### Padrão 3: Busca

```python
# Procurando se um nome esta na lista
# "names" = nomes
names = ["Ana", "Carlos", "Maria", "Pedro", "Julia"]

# "search_name" = nome a buscar (search = busca)
search_name = input("Qual nome voce procura? ")

# "found" = encontrado — comeca como False
found = False

for name in names:
    if name.lower() == search_name.lower():
        found = True
        break  # Encontrou, nao precisa continuar procurando

if found:
    print(f"{search_name} esta na lista!")
else:
    print(f"{search_name} nao foi encontrado.")
```

---

## Loops Aninhados — Loop Dentro de Loop

Você pode colocar um loop dentro de outro. O loop interno executa completamente para cada iteração do loop externo:

```python
# Tabuada de multiplicacao (1 a 5)
for i in range(1, 6):
    # Para cada valor de i, o loop interno executa completamente
    for j in range(1, 6):
        # "result" = resultado da multiplicacao
        result = i * j
        print(f"{i} x {j} = {result}", end="\t")
    # Pula linha apos cada linha da tabuada
    print()
```

**Saida esperada:**
```
1 x 1 = 1	1 x 2 = 2	1 x 3 = 3	1 x 4 = 4	1 x 5 = 5	
2 x 1 = 2	2 x 2 = 4	2 x 3 = 6	2 x 4 = 8	2 x 5 = 10	
...
```

---

## for vs while — Quando Usar Cada Um?

| Situacao | Melhor opcao | Motivo |
|----------|-------------|--------|
| Sabe quantas vezes repetir | `for` | `range()` define o número exato |
| Percorrer uma coleção | `for` | Itera naturalmente sobre cada item |
| Não sabe quantas vezes | `while` | Repete ate a condição mudar |
| Esperar entrada do usuario | `while` | Repete ate o usuario decidir parar |

---

## Resumo

| Conceito | Descricao |
|----------|-----------|
| `for i in range(n):` | Repete n vezes (0 a n-1) |
| `for item in colecao:` | Repete para cada item |
| `while condicao:` | Repete enquanto condição for True |
| `break` | Interrompe o loop imediatamente |
| `continue` | Pula para a proxima iteração |
| Contador | Variável que conta ocorrências |
| Acumulador | Variável que soma valores |

---

## Para Saber Mais

- [W3Schools — Python For Loops](https://www.w3schools.com/python/python_for_loops.asp) — _Loops for_
- [W3Schools — Python While Loops](https://www.w3schools.com/python/python_while_loops.asp) — _Loops while_
- [W3Schools — Python Range](https://www.w3schools.com/python/ref_func_range.asp) — _Funcao range()_
- [Documentação Python — Controle de Fluxo](https://docs.python.org/pt-br/3/tutorial/controlflow.html) — _Referencia oficial_

---

## Perguntas Frequentes (FAQ)

**P: O que e um "loop infinito"?**
R: E quando o loop nunca para porque a condição nunca se torna falsa. Exemplo: `while True: print("ola")` roda para sempre. Se isso acontecer, pressione `Ctrl + C` no terminal para interromper o programa.

**P: Qual a diferença entre for e while?**
R: O `for` e ideal quando você sabe quantas vezes quer repetir ou quando quer percorrer uma coleção. O `while` e ideal quando você não sabe quantas vezes vai repetir — depende de uma condição que pode mudar a qualquer momento.

**P: Por que range(5) gera 0, 1, 2, 3, 4 e não 1, 2, 3, 4, 5?**
R: Porque em Python (e na maioria das linguagens), a contagem comeca do zero. `range(5)` gera 5 números comecando do 0. Se quiser começar do 1, use `range(1, 6)`.

**P: O que e "iteração"?**
R: E cada repetição (volta) do loop. Se o loop executa 10 vezes, ele faz 10 iteracoes. E como cada volta que você da em uma pista de corrida.

**P: O que e um "contador"?**
R: E uma variável que conta quantas vezes algo aconteceu. Comeca em 0 (ou outro valor) e aumenta de 1 em 1 a cada vez. E como contar nos dedos.

**P: O que e um "acumulador"?**
R: E uma variável que vai somando valores ao longo do loop. Comeca em 0 e a cada iteração soma mais um valor. No final, tem o total acumulado. E como um cofrinho.

**P: O que e "incremento"?**
R: E aumentar o valor de uma variável, geralmente de 1 em 1. `counter = counter + 1` ou `counter += 1` incrementa o contador. E como subir um degrau.

**P: O que `+=` significa?**
R: E uma forma abreviada de somar e atribuir. `x += 5` e o mesmo que `x = x + 5`. Também existem `-=`, `*=`, `/=` para outras operações.

**P: Posso usar break no for e no while?**
R: Sim! O `break` funciona em ambos os tipos de loop. Ele interrompe o loop imediatamente, independente da condição ou do range.

**P: Posso usar continue no for e no while?**
R: Sim! O `continue` funciona em ambos. Ele pula o restante do bloco atual e vai para a proxima iteração.

**P: O que acontece se eu esquecer de incrementar o contador no while?**
R: O loop nunca para — vira um loop infinito. A condição nunca muda, então o while continua executando para sempre. Sempre garanta que algo dentro do while muda a condição.

**P: Posso ter um loop dentro de outro?**
R: Sim, isso se chama "loops aninhados". O loop interno executa completamente para cada iteração do loop externo. Use com cuidado — muitos níveis de aninhamento tornam o código confuso.

**P: O que e `range(inicio, fim, passo)`?**
R: `range()` pode receber ate 3 argumentos: inicio (onde começar), fim (onde parar, não incluido) e passo (de quanto em quanto pular). Exemplo: `range(0, 10, 2)` gera 0, 2, 4, 6, 8.

**P: Posso contar de tras para frente com range?**
R: Sim! Use passo negativo: `range(10, 0, -1)` gera 10, 9, 8, ..., 1. O inicio deve ser maior que o fim quando o passo e negativo.

**P: O que e `enumerate()`?**
R: E uma função que adiciona um contador automático ao loop for: `for i, item in enumerate(lista):` da acesso ao índice (i) e ao item ao mesmo tempo. Muito útil, mas e um conceito intermediario.

**P: Posso usar else com for ou while?**
R: Sim! Python permite `for...else` e `while...else`. O bloco do `else` executa quando o loop termina normalmente (sem `break`). E um recurso avancado que não e muito comum.

**P: Como faco um loop que pede dados ate o usuario acertar?**
R: Use `while` com uma condição que verifica se a resposta esta correta. Exemplo: `while resposta != "correta": resposta = input("Tente novamente: ")`.

**P: Posso modificar a variável do for dentro do loop?**
R: Você pode, mas não e recomendado. O `for` vai sobrescrever o valor na proxima iteração de qualquer forma. Se precisa controlar a variável manualmente, use `while`.

**P: O que e "iterar"?**
R: E o ato de percorrer uma coleção item por item. Quando você usa `for item in lista:`, você esta "iterando" sobre a lista — visitando cada item, um por um.

**P: E normal achar loops confusos no inicio?**
R: Muito normal! Loops sao um dos conceitos mais desafiadores para iniciantes. A chave e praticar bastante. Faca os exercícios, experimente variacoes e use `print()` dentro do loop para ver o que esta acontecendo a cada iteração. Com o tempo, loops se tornam naturais.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado. Este e um módulo complexo — os exercícios sao mais numerosos e progressivos.

**[Acessar Exercícios do Módulo 14](14-controles-repetição-exercícios.md)**

---

[<- Anterior: Seletores match/case](13-seletores-match-case.md) | [Glossário](00-glossário.md) | [Próximo: Funções ->](15-funções.md)
