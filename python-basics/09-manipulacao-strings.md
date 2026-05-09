# 09 — Manipulação de Strings

[<- Anterior: Conversão de Tipos](08-conversao-tipos.md) | [Glossário](00-glossario.md) | [Próximo: Indentacao e Escopo ->](10-indentacao-escopo.md)

---

## Introdução

Strings (textos) sao um dos tipos de dados mais usados em programação. Praticamente todo programa trabalha com textos de alguma forma: nomes de usuarios, mensagens, enderecos, senhas, descricoes de produtos. Saber manipular strings e uma habilidade fundamental.

Neste módulo, você vai aprender a formatar, fatiar e transformar textos em Python. Pense nas strings como um colar de contas: cada conta e um caractere (letra, número ou símbolo), e você pode acessar contas individuais, cortar pedacos do colar ou trocar contas de lugar.

> **Dica:** Consulte o [Glossário](00-glossario.md) e a [Referência de Métodos de String](00-glossario-comandos.md#métodos-de-string) sempre que precisar.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código de exemplo e cole em um novo arquivo no VSCode
2. Salve com extensão `.py` (exemplo: `strings.py`)
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-09`
4. Execute: `python3 strings.py`

---

## Concatenacao — Juntando Textos

Concatenar e juntar dois ou mais textos em um so. Em Python, usamos o operador `+` para concatenar strings:

```python
# Concatenando (juntando) dois textos com o operador +
# "first_name" = primeiro nome, "last_name" = sobrenome
first_name = "Maria"
last_name = "Silva"

# O operador + junta os textos sem espaco entre eles
# "full_name" = nome completo
full_name = first_name + " " + last_name

print("Nome completo:", full_name)
```

**Saida esperada:**
```
Nome completo: Maria Silva
```

> **Nota:** O `+` entre strings junta os textos literalmente, sem adicionar espaco. Por isso colocamos `" "` (um espaco entre aspas) no meio.

---

## f-strings — A Forma Mais Prática de Formatar Textos

As f-strings sao a forma mais moderna e prática de inserir valores de variáveis dentro de um texto. Basta colocar um `f` antes das aspas e usar chaves `{}` para indicar onde os valores devem aparecer:

```python
# Usando f-string para formatar texto
# Coloque f antes das aspas e use {} para inserir variaveis
# "name" = nome, "age" = idade, "city" = cidade
name = "Carlos"
age = 40
city = "Belo Horizonte"

# A f-string substitui {name}, {age} e {city} pelos valores das variaveis
# "message" = mensagem
message = f"Meu nome e {name}, tenho {age} anos e moro em {city}."

print(message)
```

**Saida esperada:**
```
Meu nome e Carlos, tenho 40 anos e moro em Belo Horizonte.
```

Você também pode fazer cálculos dentro das chaves:

```python
# Fazendo calculos dentro da f-string
# "price" = preco, "quantity" = quantidade
price = 12.50
quantity = 3

# {price * quantity} calcula o total diretamente dentro do texto
print(f"Preco: R$ {price} x {quantity} = R$ {price * quantity}")
```

**Saida esperada:**
```
Preco: R$ 12.5 x 3 = R$ 37.5
```

### f-string vs concatenacao: qual usar?

| Abordagem | Exemplo | Quando usar |
|-----------|---------|-------------|
| Concatenacao (`+`) | `"Ola " + name` | Textos simples, sem muitas variáveis |
| f-string (`f""`) | `f"Ola {name}"` | Textos com variáveis e cálculos (recomendado) |
| print com virgulas | `print("Ola", name)` | Apenas para exibir no terminal |

Na maioria dos casos, **f-strings sao a melhor opcao** por serem mais legiveis e práticas.

---

## Fatiamento (Slicing) — Cortando Pedacos de Texto

Cada caractere de uma string tem uma posição (índice), comecando do zero. Você pode acessar caracteres individuais ou cortar pedacos da string usando colchetes `[]`:

### Acessando caracteres individuais

```python
# Cada caractere tem uma posicao (indice), comecando do 0
# "word" = palavra
word = "Python"

# Posicoes: P=0, y=1, t=2, h=3, o=4, n=5
print("Primeiro caractere (posicao 0):", word[0])
print("Segundo caractere (posicao 1):", word[1])
print("Ultimo caractere (posicao 5):", word[5])
```

**Saida esperada:**
```
Primeiro caractere (posicao 0): P
Segundo caractere (posicao 1): y
Ultimo caractere (posicao 5): n
```

> **Atenção:** Em programação, a contagem comeca do **zero**, não do um. O primeiro caractere esta na posição 0, o segundo na posição 1, e assim por diante. E como os andares de um predio que comeca do terreo (andar 0).

### Indices negativos

Você pode usar indices negativos para contar de tras para frente. O último caractere e `-1`, o penultimo e `-2`, e assim por diante:

```python
# Indices negativos contam de tras para frente
# "word" = palavra
word = "Python"

# -1 = ultimo, -2 = penultimo, -3 = antepenultimo
print("Ultimo caractere:", word[-1])
print("Penultimo caractere:", word[-2])
print("Primeiro caractere (de tras):", word[-6])
```

**Saida esperada:**
```
Ultimo caractere: n
Penultimo caractere: o
Primeiro caractere (de tras): P
```

### Fatiando (cortando pedacos)

Use `[inicio:fim]` para cortar um pedaco da string. O caractere na posição `inicio` e incluido, mas o da posição `fim` não e:

```python
# Fatiamento: texto[inicio:fim]
# O inicio e incluido, o fim NAO e incluido
# "text" = texto
text = "Programacao"

# text[0:7] pega da posicao 0 ate a 6 (7 nao e incluido)
print("Primeiros 7 caracteres:", text[0:7])

# text[7:11] pega da posicao 7 ate a 10
print("Ultimos 4 caracteres:", text[7:11])

# Atalhos: omitir inicio ou fim
print("Do inicio ate posicao 4:", text[:5])   # mesmo que text[0:5]
print("Da posicao 5 ate o fim:", text[5:])    # vai ate o ultimo caractere
```

**Saida esperada:**
```
Primeiros 7 caracteres: Program
Ultimos 4 caracteres: acao
Do inicio ate posicao 4: Progr
Da posicao 5 ate o fim: amacao
```

---

## Métodos de String — Transformando Textos

Strings em Python possuem **métodos** — funções prontas que realizam operações sobre o texto. Você usa métodos com a sintaxe `texto.metodo()`.

### upper() e lower() — Maiusculas e minusculas

```python
# upper() converte todo o texto para MAIUSCULAS
# lower() converte todo o texto para minusculas
# "greeting" = saudacao
greeting = "Bom Dia, Mundo!"

# upper() = "para cima" = maiusculas
print("Maiusculas:", greeting.upper())

# lower() = "para baixo" = minusculas
print("Minusculas:", greeting.lower())

# O texto original NAO e alterado
print("Original:", greeting)
```

**Saida esperada:**
```
Maiusculas: BOM DIA, MUNDO!
Minusculas: bom dia, mundo!
Original: Bom Dia, Mundo!
```

> **Nota:** Os métodos de string **não alteram o texto original**. Eles retornam um novo texto modificado. O original permanece intacto.

### strip() — Removendo espacos extras

```python
# strip() remove espacos em branco do inicio e do fim do texto
# Muito util para limpar dados digitados pelo usuario
# "user_input" = entrada do usuario
user_input = "   Maria Silva   "

# strip() = "descascar" = remove espacos das bordas
# "clean_input" = entrada limpa
clean_input = user_input.strip()

print("Com espacos: '" + user_input + "'")
print("Sem espacos: '" + clean_input + "'")
```

**Saida esperada:**
```
Com espacos: '   Maria Silva   '
Sem espacos: 'Maria Silva'
```

### split() — Dividindo texto em partes

```python
# split() divide um texto em uma lista de partes
# Por padrao, divide nos espacos
# "sentence" = frase
sentence = "Python e uma linguagem incrivel"

# split() = "dividir" = separa o texto em pedacos
# "words" = palavras (lista de palavras)
words = sentence.split()

print("Frase:", sentence)
print("Palavras:", words)
print("Primeira palavra:", words[0])
print("Ultima palavra:", words[-1])
```

**Saida esperada:**
```
Frase: Python e uma linguagem incrivel
Palavras: ['Python', 'e', 'uma', 'linguagem', 'incrivel']
Primeira palavra: Python
Ultima palavra: incrivel
```

Você pode especificar qual caractere usar para dividir:

```python
# Dividindo por virgula
# "csv_data" = dados separados por virgula
csv_data = "arroz,feijao,macarrao,cafe"

# split(",") divide no caractere virgula
# "items" = itens
items = csv_data.split(",")

print("Itens:", items)
```

**Saida esperada:**
```
Itens: ['arroz', 'feijao', 'macarrao', 'cafe']
```

### replace() — Substituindo partes do texto

```python
# replace() substitui uma parte do texto por outra
# replace(antigo, novo) = substituir(o_que_trocar, pelo_que_trocar)
# "message" = mensagem
message = "Eu gosto de Java"

# Substituimos "Java" por "Python"
# "new_message" = nova mensagem
new_message = message.replace("Java", "Python")

print("Original:", message)
print("Modificada:", new_message)
```

**Saida esperada:**
```
Original: Eu gosto de Java
Modificada: Eu gosto de Python
```

### find() e count() — Buscando no texto

```python
# find() encontra a posicao de um texto dentro de outro
# count() conta quantas vezes um texto aparece
# "text" = texto
text = "banana e uma fruta, banana e amarela"

# find() retorna a posicao da primeira ocorrencia
# find() = "encontrar"
# "position" = posicao
position = text.find("banana")
print("Primeira ocorrencia de 'banana' na posicao:", position)

# count() conta quantas vezes aparece
# count() = "contar"
# "occurrences" = ocorrencias (quantas vezes aparece)
occurrences = text.count("banana")
print("'banana' aparece", occurrences, "vezes")

# find() retorna -1 se nao encontrar
not_found = text.find("laranja")
print("'laranja' encontrada na posicao:", not_found)
```

**Saida esperada:**
```
Primeira ocorrencia de 'banana' na posicao: 0
'banana' aparece 2 vezes
'laranja' encontrada na posicao: -1
```

### startswith() e endswith() — Verificando inicio e fim

```python
# startswith() verifica se o texto comeca com algo
# endswith() verifica se o texto termina com algo
# Retornam True ou False
# "filename" = nome do arquivo
filename = "relatorio.pdf"

# startswith() = "comeca com"
print("Comeca com 'relatorio':", filename.startswith("relatorio"))

# endswith() = "termina com"
print("Termina com '.pdf':", filename.endswith(".pdf"))
print("Termina com '.txt':", filename.endswith(".txt"))
```

**Saida esperada:**
```
Comeca com 'relatorio': True
Termina com '.pdf': True
Termina com '.txt': False
```

---

## Função len() — Contando Caracteres

A função `len()` (abreviacao de "length", que significa "comprimento" em ingles) retorna o número de caracteres de uma string:

```python
# len() conta quantos caracteres tem no texto
# "name" = nome
name = "Maria Silva"

# len() = length = comprimento
# "name_length" = comprimento do nome
name_length = len(name)

print("Nome:", name)
print("Quantidade de caracteres:", name_length)
```

**Saida esperada:**
```
Nome: Maria Silva
Quantidade de caracteres: 11
```

> **Nota:** `len()` conta todos os caracteres, incluindo espacos. "Maria Silva" tem 11 caracteres: 5 letras + 1 espaco + 5 letras.

---

## Resumo dos Métodos de String

| Método | O que faz | Exemplo | Resultado |
|--------|-----------|---------|-----------|
| `.upper()` | Converte para maiusculas | `"ola".upper()` | `"OLA"` |
| `.lower()` | Converte para minusculas | `"OLA".lower()` | `"ola"` |
| `.strip()` | Remove espacos das bordas | `" ola ".strip()` | `"ola"` |
| `.split()` | Divide em lista | `"a,b".split(",")` | `["a", "b"]` |
| `.replace(a, b)` | Substitui a por b | `"ola".replace("o","a")` | `"ala"` |
| `.find(x)` | Posição de x | `"abc".find("b")` | `1` |
| `.count(x)` | Quantas vezes x aparece | `"banana".count("a")` | `3` |
| `.startswith(x)` | Comeca com x? | `"abc".startswith("a")` | `True` |
| `.endswith(x)` | Termina com x? | `"abc".endswith("c")` | `True` |
| `len(texto)` | Número de caracteres | `len("abc")` | `3` |

---

## Para Saber Mais

- [W3Schools — Python Strings](https://www.w3schools.com/python/python_strings.asp) — _Trabalhando com textos_
- [W3Schools — Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) — _Todos os métodos de string_
- [W3Schools — Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp) — _f-strings e formatacao_
- [W3Schools — Python Slicing Strings](https://www.w3schools.com/python/python_strings_slicing.asp) — _Fatiamento de strings_
- [Documentação Python — Métodos de String](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods) — _Referencia completa_

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre aspas simples e duplas?**
R: Nenhuma diferença funcional. `'texto'` e `"texto"` sao identicos. A vantagem de ter as duas e poder usar uma dentro da outra: `"Ele disse 'ola'"` ou `'Ele disse "ola"'`.

**P: O que e uma f-string?**
R: E uma string que comeca com a letra `f` antes das aspas e permite inserir variáveis diretamente no texto usando chaves `{}`. Exemplo: `f"Nome: {name}"`. E a forma mais prática de formatar textos em Python.

**P: Por que a contagem comeca do zero?**
R: E uma convencao da computacao. O primeiro elemento esta na posição 0, o segundo na posição 1, e assim por diante. Pode parecer estranho no inicio, mas você se acostuma rapidamente. Pense no terreo de um predio: o terreo e o andar 0, o primeiro andar e o 1.

**P: O que acontece se eu acessar uma posição que não existe?**
R: O Python mostra um `IndexError`. Por exemplo, se a string tem 5 caracteres e você tenta acessar a posição 10, vai dar erro. Sempre verifique o tamanho com `len()` antes.

**P: Os métodos alteram a string original?**
R: Não! Strings em Python sao imutaveis — não podem ser alteradas depois de criadas. Métodos como `upper()` e `replace()` retornam uma nova string. A original permanece intacta.

**P: O que significa "imutavel"?**
R: Significa que não pode ser modificado depois de criado. Você não pode trocar um caractere individual de uma string. Se precisar de uma versão modificada, crie uma nova string.

**P: Posso usar f-string com aspas simples?**
R: Sim! `f'Nome: {name}'` funciona da mesma forma que `f"Nome: {name}"`.

**P: O que e o `\n` dentro de uma string?**
R: E um caractere especial que representa uma quebra de linha. Quando o Python encontra `\n`, ele pula para a proxima linha. Exemplo: `print("Linha 1\nLinha 2")` exibe em duas linhas.

**P: Posso concatenar string com número usando +?**
R: Não diretamente. `"Idade: " + 25` gera erro. Você precisa converter o número para string primeiro: `"Idade: " + str(25)`. Ou use f-string: `f"Idade: {25}"`.

**P: O que e fatiamento (slicing)?**
R: E a técnica de extrair uma parte de uma string usando indices. `texto[2:5]` pega os caracteres das posicoes 2, 3 e 4. O inicio e incluido, o fim não.

**P: Posso fatiar com passo (step)?**
R: Sim! `texto[::2]` pega um caractere sim, um não (de 2 em 2). `texto[::-1]` inverte a string. Mas isso e mais avancado — por enquanto, foque no fatiamento básico.

**P: O que split() retorna?**
R: Retorna uma lista (que vamos estudar no módulo 19). Por enquanto, saiba que e uma coleção de pedacos do texto. Você pode acessar cada pedaco pelo índice: `palavras[0]` pega o primeiro pedaco.

**P: strip() remove espacos do meio do texto?**
R: Não! `strip()` remove apenas espacos do inicio e do fim. Espacos no meio do texto permanecem. `"  ola  mundo  ".strip()` resulta em `"ola  mundo"`.

**P: Posso encadear métodos?**
R: Sim! Você pode chamar um método no resultado de outro: `"  OLA  ".strip().lower()` resulta em `"ola"`. Primeiro remove espacos, depois converte para minusculas.

**P: find() e index() sao a mesma coisa?**
R: Quase. Ambos encontram a posição de um texto. A diferença e que `find()` retorna `-1` se não encontrar, enquanto `index()` gera um erro. Para iniciantes, `find()` e mais seguro.

**P: Como verifico se um texto contem outro?**
R: Use o operador `in`: `"Python" in "Eu amo Python"` retorna `True`. E a forma mais simples e legivel.

**P: O que e o método join()?**
R: E o oposto de `split()`. Junta uma lista de textos em um so, usando um separador: `", ".join(["a", "b", "c"])` resulta em `"a, b, c"`. Vamos usar mais quando aprendermos listas.

**P: Posso comparar strings?**
R: Sim! Use `==` para verificar se sao iguais: `"abc" == "abc"` retorna `True`. Cuidado: a comparação diferencia maiusculas de minusculas. `"Abc" == "abc"` retorna `False`.

**P: Como faco para ignorar maiusculas/minusculas na comparação?**
R: Converta ambas para o mesmo caso antes de comparar: `"Abc".lower() == "abc".lower()` retorna `True`.

**P: E normal achar strings confusas no inicio?**
R: Sim, strings tem muitos detalhes. O segredo e praticar bastante. Faca os exercícios, experimente os métodos no terminal e consulte a tabela de referência sempre que precisar. Com o tempo, manipular textos se torna natural.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

**[Acessar Exercícios do Módulo 09](09-manipulacao-strings-exercicios.md)**

---

[<- Anterior: Conversão de Tipos](08-conversao-tipos.md) | [Glossário](00-glossario.md) | [Próximo: Indentacao e Escopo ->](10-indentacao-escopo.md)
