# 5.17 — Exercícios: Noções de Complexidade: Big O

[← Voltar ao Módulo 5.17](cap05-mod17-big-o-conteudo.md)

---

## Como usar estes exercícios

1. Leia o enunciado com atenção
2. Tente resolver sozinho antes de olhar as respostas
3. Salve cada exercício em um arquivo separado na pasta `~/meus-projetos/python-curso/módulo-17/`
4. Execute com `python3 nome_do_arquivo.py`

---

## Exercício 1 — Identificar complexidade (Nível: Fácil)

Para cada trecho de código abaixo, identifique a complexidade Big O e justifique.

### Trecho A

```python
def get_first(items):
    return items[0]
```

### Trecho B

```python
def find_item(items, target):
    for item in items:
        if item == target:
            return True
    return False
```

### Trecho C

```python
def has_duplicates(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False
```

### Trecho D

```python
def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### Trecho E

```python
def print_pairs(items):
    for i in items:
        for j in items:
            print(i, j)
```


### Respostas Comentadas

<details>
<summary>Clique para ver as respostas</summary>

**Trecho A — O(1):** Acessa diretamente o primeiro elemento por índice. Não importa o tamanho da lista, sempre é 1 operação.

**Trecho B — O(n):** No pior caso, percorre todos os n elementos da lista antes de encontrar (ou não encontrar) o alvo. Um loop simples.

**Trecho C — O(n²):** Dois loops aninhados. O loop externo percorre n elementos, e para cada um, o loop interno percorre os restantes. No total, faz aproximadamente n²/2 comparações, que em Big O simplifica para O(n²).

**Trecho D — O(log n):** Busca binária. A cada iteração, divide o espaço de busca pela metade. Para n elementos, precisa de no máximo log₂(n) iterações.

**Trecho E — O(n²):** Dois loops aninhados, cada um percorrendo todos os n elementos. Total: n * n = n² operações.

</details>

---

## Exercício 2 — Otimizar de O(n²) para O(n) (Nível: Médio)

O código abaixo verifica se uma lista tem algum par de números que soma um valor alvo. A versão atual é O(n²). Reescreva para O(n) usando um conjunto (set).

```python
# Versao O(n^2) — lenta para listas grandes
# "has_pair_sum" = tem par que soma
def has_pair_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False

# Teste
print(has_pair_sum([1, 3, 5, 7, 9], 10))  # True (1+9 ou 3+7)
print(has_pair_sum([1, 3, 5, 7, 9], 20))  # False
```

**Dica:** Para cada número, calcule qual número falta para atingir o alvo (`target - number`). Verifique se esse número já foi visto usando um conjunto (set), onde a busca é O(1).

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# Versao O(n) — rapida mesmo para listas grandes
def has_pair_sum(numbers, target):
    # "seen" = numeros ja vistos
    seen = set()
    for number in numbers:
        # "complement" = complemento (o que falta para atingir o alvo)
        complement = target - number
        if complement in seen:  # Busca em set e O(1)
            return True
        seen.add(number)
    return False

# Teste
print(has_pair_sum([1, 3, 5, 7, 9], 10))  # True
print(has_pair_sum([1, 3, 5, 7, 9], 20))  # False
```

A versão otimizada percorre a lista uma única vez (O(n)). Para cada número, verifica se o complemento já foi visto no conjunto (O(1)). Total: O(n).

</details>

---

## Exercício 3 — Medir na prática (Nível: Difícil)

Crie um programa que mede o tempo de execução de busca linear vs busca binária para listas de diferentes tamanhos. O programa deve:

1. Criar listas ordenadas de tamanhos: 1.000, 10.000, 100.000 e 1.000.000
2. Buscar o último elemento (pior caso) com busca linear e binária
3. Repetir cada busca 100 vezes para ter uma medição mais precisa
4. Mostrar os tempos em uma tabela formatada

**Saída esperada (tempos aproximados):**
```
| Tamanho     | Linear (ms) | Binaria (ms) | Linear/Binaria |
|-------------|-------------|--------------|----------------|
| 1.000       | 2.5         | 0.1          | 25x            |
| 10.000      | 25.0        | 0.1          | 250x           |
| 100.000     | 250.0       | 0.1          | 2500x          |
| 1.000.000   | 2500.0      | 0.2          | 12500x         |
```

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
import time

def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1

def binary_search(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# "sizes" = tamanhos para testar
sizes = [1000, 10000, 100000, 1000000]
# "repetitions" = repeticoes
repetitions = 100

print(f"| {'Tamanho':>11} | {'Linear (ms)':>11} | {'Binaria (ms)':>12} | {'Linear/Binaria':>14} |")
print(f"|{'-' * 13}|{'-' * 13}|{'-' * 14}|{'-' * 16}|")

for size in sizes:
    # "data" = dados
    data = list(range(size))
    target = size - 1  # Ultimo elemento (pior caso para linear)

    # Medir busca linear
    start = time.time()
    for _ in range(repetitions):
        linear_search(data, target)
    linear_time = (time.time() - start) * 1000  # Em milissegundos

    # Medir busca binaria
    start = time.time()
    for _ in range(repetitions):
        binary_search(data, target)
    binary_time = (time.time() - start) * 1000

    # "ratio" = proporcao
    ratio = linear_time / binary_time if binary_time > 0 else 0
    print(f"| {size:>11,} | {linear_time:>11.1f} | {binary_time:>12.1f} | {ratio:>13.0f}x |")
```

</details>

---

[← Voltar ao Módulo 5.17](cap05-mod17-big-o-conteudo.md)
