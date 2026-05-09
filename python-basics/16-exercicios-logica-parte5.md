# Exercícios de Lógica — Parte 5: Manipulação de Strings

[<- Parte 4](16-exercícios-lógica-parte4.md) | [Voltar ao Módulo 16](16-exercícios-lógica.md)

---

## Exercício 21 — Contar Palavras — Nível: Básico
**Conceitos praticados:** strings, split, len, funções

### Enunciado
Crie uma função `count_words` que receba uma frase e retorne a quantidade de palavras.

### Dicas
- Use `.split()` para dividir a frase em palavras
- Use `len()` para contar quantas palavras resultaram

### Proposta de Teste
- Frase: `"Python e uma linguagem incrivel"` — Retorno: `5`
- Frase: `"Ola"` — Retorno: `1`
- Frase: `""` — Retorno: `0`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que conta palavras em uma frase
# "count_words" = contar palavras
# "sentence" = frase
def count_words(sentence):
    # Se a frase estiver vazia, retorna 0
    if sentence.strip() == "":
        return 0
    # split() divide a frase nos espacos e retorna uma lista de palavras
    # "words" = palavras
    words = sentence.split()
    # len() conta quantos itens tem na lista
    return len(words)

# Testamos a funcao
print(f"Palavras: {count_words('Python e uma linguagem incrivel')}")
print(f"Palavras: {count_words('Ola')}")
print(f"Palavras: {count_words('')}")
```

---

## Exercício 22 — Verificar Palindromo — Nível: Intermediario
**Conceitos praticados:** strings, fatiamento, comparação, funções

### Enunciado
Crie uma função `is_palindrome` que receba uma palavra e retorne True se for um palindromo (se le igual de tras para frente). Ignore maiusculas/minusculas. (Exemplos de palindromos: "aba", "arara", "racecar".)

### Dicas
- Converta para minusculas com `.lower()`
- Inverta com `[::-1]`
- Compare a original com a invertida

### Proposta de Teste
- Palavra: `"arara"` — Retorno: `True`
- Palavra: `"Python"` — Retorno: `False`
- Palavra: `"Aba"` — Retorno: `True` (ignora maiusculas)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que verifica se uma palavra e palindromo
# "is_palindrome" = e palindromo
# "word" = palavra
def is_palindrome(word):
    # Convertemos para minusculas para ignorar maiusculas/minusculas
    # "clean_word" = palavra limpa (padronizada)
    clean_word = word.lower()
    # Invertemos a palavra usando fatiamento com passo negativo
    # [::-1] percorre a string de tras para frente
    # "reversed_word" = palavra invertida
    reversed_word = clean_word[::-1]
    # Comparamos: se a original e igual a invertida, e palindromo
    return clean_word == reversed_word

# Testamos a funcao
print(f"'arara' e palindromo? {is_palindrome('arara')}")
print(f"'Python' e palindromo? {is_palindrome('Python')}")
print(f"'Aba' e palindromo? {is_palindrome('Aba')}")
print(f"'racecar' e palindromo? {is_palindrome('racecar')}")
```

---

## Exercício 23 — Censurar Palavra — Nível: Intermediario
**Conceitos praticados:** strings, replace, funções

### Enunciado
Crie uma função `censor_word` que receba uma frase e uma palavra a censurar. Substitua todas as ocorrências da palavra por asteriscos (`*`) do mesmo tamanho.

### Dicas
- Use `len()` para saber o tamanho da palavra
- Crie uma string de asteriscos: `"*" * tamanho`
- Use `.replace()` para substituir

### Proposta de Teste
- Frase: `"O gato comeu o peixe do gato"`, Censurar: `"gato"` — Retorno: `"O **** comeu o peixe do ****"`
- Frase: `"Ola mundo"`, Censurar: `"xyz"` — Retorno: `"Ola mundo"` (palavra não encontrada)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que censura uma palavra em uma frase
# "censor_word" = censurar palavra
# "sentence" = frase, "word_to_censor" = palavra a censurar
def censor_word(sentence, word_to_censor):
    # Criamos a string de asteriscos com o mesmo tamanho da palavra
    # "censored" = censurado
    # "*" * len(word_to_censor) repete * pelo numero de caracteres da palavra
    censored = "*" * len(word_to_censor)
    # Substituimos todas as ocorrencias da palavra pelos asteriscos
    # replace(antigo, novo) troca todas as ocorrencias
    # "result" = resultado
    result = sentence.replace(word_to_censor, censored)
    return result

# Testamos a funcao
print(censor_word("O gato comeu o peixe do gato", "gato"))
print(censor_word("Ola mundo", "xyz"))
```

---

## Exercício 24 — Contar Cada Vogal — Nível: Avancado
**Conceitos praticados:** strings, loops, contadores multiplos, funções

### Enunciado
Crie uma função `count_each_vowel` que receba um texto e retorne a contagem de cada vogal separadamente (a, e, i, o, u).

### Dicas
- Use 5 contadores, um para cada vogal
- Percorra cada caractere e incremente o contador correspondente
- Use `.lower()` para tratar maiusculas

### Proposta de Teste
- Texto: `"Programacao em Python"` — a:3, e:1, i:1, o:3, u:0

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que conta cada vogal separadamente
# "count_each_vowel" = contar cada vogal
# "text" = texto
def count_each_vowel(text):
    # Contadores individuais para cada vogal
    # "count_a" = contagem de A, etc.
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    # Percorremos cada caractere do texto em minusculas
    for char in text.lower():
        # "char" = caractere
        # Verificamos qual vogal e e incrementamos o contador correspondente
        if char == "a":
            count_a += 1
        elif char == "e":
            count_e += 1
        elif char == "i":
            count_i += 1
        elif char == "o":
            count_o += 1
        elif char == "u":
            count_u += 1

    # Exibimos os resultados
    print(f"a: {count_a}")
    print(f"e: {count_e}")
    print(f"i: {count_i}")
    print(f"o: {count_o}")
    print(f"u: {count_u}")

# Testamos a funcao
print("Vogais em 'Programacao em Python':")
count_each_vowel("Programacao em Python")
```

---

## Exercício 25 — Gerador de Sigla — Nível: Avancado
**Conceitos praticados:** strings, split, loops, concatenacao, funções

### Enunciado
Crie uma função `generate_acronym` que receba um nome composto (ex: "Instituto Federal de Educação") e retorne a sigla formada pelas primeiras letras de cada palavra em maiusculas, ignorando palavras com 2 letras ou menos (como "de", "do", "em").

### Dicas
- Use `.split()` para separar as palavras
- Percorra cada palavra e pegue a primeira letra com `[0]`
- Ignore palavras curtas (len <= 2)
- Use `.upper()` para maiusculas

### Proposta de Teste
- Nome: `"Instituto Federal de Educacao"` — Sigla: `"IFE"`
- Nome: `"Universidade de Sao Paulo"` — Sigla: `"USP"`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que gera uma sigla a partir de um nome composto
# "generate_acronym" = gerar sigla (acronym = sigla)
# "full_name" = nome completo
def generate_acronym(full_name):
    # Separamos o nome em palavras
    # "words" = palavras
    words = full_name.split()

    # Variavel para construir a sigla
    # "acronym" = sigla — comeca vazia
    acronym = ""

    # Percorremos cada palavra
    for word in words:
        # "word" = cada palavra
        # Ignoramos palavras com 2 letras ou menos (preposicoes como "de", "do", "em")
        if len(word) > 2:
            # Pegamos a primeira letra e convertemos para maiuscula
            # word[0] = primeiro caractere da palavra
            # .upper() converte para maiuscula
            acronym = acronym + word[0].upper()

    return acronym

# Testamos a funcao
print(f"Sigla: {generate_acronym('Instituto Federal de Educacao')}")
print(f"Sigla: {generate_acronym('Universidade de Sao Paulo')}")
print(f"Sigla: {generate_acronym('Organizacao das Nacoes Unidas')}")
```

---

[<- Parte 4](16-exercícios-lógica-parte4.md) | [Voltar ao Módulo 16](16-exercícios-lógica.md)
