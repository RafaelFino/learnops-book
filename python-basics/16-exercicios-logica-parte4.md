# Exercícios de Lógica — Parte 4: Busca e Filtragem

[<- Parte 3](16-exercícios-lógica-parte3.md) | [Voltar ao Módulo 16](16-exercícios-lógica.md) | [Parte 5 ->](16-exercícios-lógica-parte5.md)

---

## Exercício 16 — Buscar Número na Lista — Nível: Básico
**Conceitos praticados:** loops, condicionais, busca linear

### Enunciado
Crie uma função `find_number` que receba uma lista de números e um número alvo. Retorne True se o número estiver na lista, False caso contrario. Não use o operador `in`.

### Dicas
- Percorra a lista com for
- Compare cada item com o alvo
- Se encontrar, retorne True imediatamente

### Proposta de Teste
- Lista: `[3, 7, 1, 9, 4]`, Alvo: `9` — Retorno: `True`
- Lista: `[3, 7, 1, 9, 4]`, Alvo: `5` — Retorno: `False`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que busca um numero em uma lista
# "find_number" = encontrar numero
# "numbers" = lista de numeros, "target" = alvo (o que procuramos)
def find_number(numbers, target):
    # Percorremos cada numero da lista
    for number in numbers:
        # "number" = cada numero da lista
        # Se encontramos o alvo, retornamos True imediatamente
        if number == target:
            return True
    # Se percorremos toda a lista sem encontrar, retornamos False
    return False

# Testamos a funcao
# "my_list" = minha lista
my_list = [3, 7, 1, 9, 4]
print(f"9 esta na lista? {find_number(my_list, 9)}")
print(f"5 esta na lista? {find_number(my_list, 5)}")
```

---

## Exercício 17 — Filtrar Números Pares — Nível: Básico
**Conceitos praticados:** loops, condicionais, listas, filtragem

### Enunciado
Crie uma função `filter_even` que receba uma lista de números e retorne uma nova lista contendo apenas os números pares.

### Dicas
- Crie uma lista vazia para o resultado
- Percorra a original e adicione apenas os pares

### Proposta de Teste
- Lista: `[1, 2, 3, 4, 5, 6, 7, 8]` — Retorno: `[2, 4, 6, 8]`
- Lista: `[1, 3, 5]` — Retorno: `[]` (lista vazia)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que filtra apenas os numeros pares
# "filter_even" = filtrar pares (even = par)
# "numbers" = lista de numeros
def filter_even(numbers):
    # Lista para guardar os pares encontrados
    # "even_numbers" = numeros pares
    even_numbers = []

    # Percorremos cada numero
    for number in numbers:
        # Verificamos se e par (resto da divisao por 2 e zero)
        if number % 2 == 0:
            # E par — adicionamos a lista de resultados
            even_numbers.append(number)

    return even_numbers

# Testamos a funcao
print(f"Pares: {filter_even([1, 2, 3, 4, 5, 6, 7, 8])}")
print(f"Pares: {filter_even([1, 3, 5])}")
```

---

## Exercício 18 — Filtrar por Faixa de Valor — Nível: Intermediario
**Conceitos praticados:** loops, condicionais, funções com multiplos parametros

### Enunciado
Crie uma função `filter_by_range` que receba uma lista de números, um valor mínimo e um valor máximo. Retorne uma nova lista com os números que estão dentro da faixa (inclusive).

### Dicas
- Verifique se cada número e >= mínimo e <= máximo
- Use `and` para combinar as condições

### Proposta de Teste
- Lista: `[1, 5, 10, 15, 20, 25]`, Min: `5`, Max: `20` — Retorno: `[5, 10, 15, 20]`
- Lista: `[1, 2, 3]`, Min: `10`, Max: `20` — Retorno: `[]`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que filtra numeros dentro de uma faixa
# "filter_by_range" = filtrar por faixa
# "numbers" = numeros, "min_value" = valor minimo, "max_value" = valor maximo
def filter_by_range(numbers, min_value, max_value):
    # Lista para os numeros dentro da faixa
    # "filtered" = filtrados
    filtered = []

    for number in numbers:
        # Verificamos se o numero esta dentro da faixa (inclusive)
        # and = E — ambas as condicoes precisam ser verdadeiras
        if number >= min_value and number <= max_value:
            filtered.append(number)

    return filtered

# Testamos a funcao
print(f"Faixa 5-20: {filter_by_range([1, 5, 10, 15, 20, 25], 5, 20)}")
print(f"Faixa 10-20: {filter_by_range([1, 2, 3], 10, 20)}")
```

---

## Exercício 19 — Encontrar Posição do Maior — Nível: Intermediario
**Conceitos praticados:** loops, comparação, indices, lógica de busca

### Enunciado
Crie uma função `find_max_position` que receba uma lista de números e retorne a posição (índice) do maior valor.

### Dicas
- Guarde o índice do maior encontrado
- Use `range(len(lista))` para ter acesso ao índice

### Proposta de Teste
- Lista: `[3, 7, 1, 9, 4]` — Retorno: `3` (posição do 9)
- Lista: `[10, 5, 3]` — Retorno: `0` (posição do 10)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que encontra a posicao do maior valor
# "find_max_position" = encontrar posicao do maximo
# "numbers" = numeros
def find_max_position(numbers):
    # Comecamos assumindo que o maior esta na posicao 0
    # "max_position" = posicao do maximo
    max_position = 0

    # Percorremos a lista usando indices
    # range(len(numbers)) gera indices de 0 ate o ultimo
    for i in range(len(numbers)):
        # "i" = indice atual
        # Se o numero na posicao i for maior que o atual maximo
        if numbers[i] > numbers[max_position]:
            # Atualizamos a posicao do maximo
            max_position = i

    return max_position

# Testamos a funcao
# "my_list" = minha lista
my_list = [3, 7, 1, 9, 4]
# "pos" = posicao
pos = find_max_position(my_list)
print(f"Maior valor: {my_list[pos]} na posicao {pos}")
```

---

## Exercício 20 — Números Unicos Ordenados — Nível: Avancado
**Conceitos praticados:** loops, listas, lógica de ordenação simples, remoção de duplicatas

### Enunciado
Crie uma função que receba uma lista de números, remova duplicatas e retorne os números unicos em ordem crescente. Não use `set()` ou `.sort()`.

### Dicas
- Primeiro remova duplicatas (como no exercício 10)
- Depois ordene usando "selection sort": encontre o menor, coloque na primeira posição, repita

### Proposta de Teste
- Lista: `[5, 3, 8, 3, 1, 5, 8]` — Retorno: `[1, 3, 5, 8]`
- Lista: `[1, 1, 1]` — Retorno: `[1]`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que retorna numeros unicos em ordem crescente
# "unique_sorted" = unicos ordenados
# "numbers" = numeros
def unique_sorted(numbers):
    # Passo 1: Remover duplicatas
    # "unique" = unicos
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)

    # Passo 2: Ordenar (selection sort — ordenacao por selecao)
    # A ideia: encontrar o menor, colocar na primeira posicao, repetir
    # "sorted_list" = lista ordenada
    sorted_list = []

    # Enquanto a lista de unicos tiver itens
    while len(unique) > 0:
        # Encontramos o menor valor
        # "minimum" = menor valor atual
        minimum = unique[0]
        # "min_index" = indice do menor valor
        min_index = 0

        for i in range(len(unique)):
            if unique[i] < minimum:
                minimum = unique[i]
                min_index = i

        # Adicionamos o menor a lista ordenada
        sorted_list.append(minimum)
        # Removemos o menor da lista de unicos
        # .pop(indice) remove o item na posicao indicada
        unique.pop(min_index)

    return sorted_list

# Testamos a funcao
print(f"Resultado: {unique_sorted([5, 3, 8, 3, 1, 5, 8])}")
print(f"Resultado: {unique_sorted([1, 1, 1])}")
```

---

[<- Parte 3](16-exercícios-lógica-parte3.md) | [Voltar ao Módulo 16](16-exercícios-lógica.md) | [Parte 5 ->](16-exercícios-lógica-parte5.md)
