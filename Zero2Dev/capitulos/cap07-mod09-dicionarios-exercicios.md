# 7.9 — Exercícios: Dicionários e Tabelas Hash

[← Voltar ao conteúdo: Dicionários e Tabelas Hash](cap07-mod09-dicionarios-conteudo.md)

---

## Sobre os Exercícios

Estes exercícios cobrem os conceitos de dicionários e tabelas hash apresentados no módulo 7.9. Como a implementação completa de tabelas hash em C é complexa, alguns exercícios usam Python para focar no conceito. Os exercícios em C usam a implementação simplificada do módulo.

---

## Exercício 1: Conceitos Fundamentais

Responda sem consultar o material:

a) O que é uma tabela hash? Qual problema ela resolve?

b) O que é uma função hash? Quais propriedades uma boa função hash deve ter?

c) O que é uma colisão? Por que colisões são inevitáveis?

d) Explique a diferença entre encadeamento e endereçamento aberto para resolver colisões.

e) O que é fator de carga? Por que ele importa?

f) Qual a complexidade média de busca em uma tabela hash? E no pior caso?

---

## Exercício 2: Calculando Hashes no Papel

Dada uma tabela hash de tamanho 7 e a função hash `h(chave) = chave % 7`, calcule o índice para cada chave e identifique colisões:

| Chave | h(chave) = chave % 7 | Índice | Colisao com |
|-------|----------------------|--------|-------------|
| 10 | 10 % 7 = ? | ? | — |
| 22 | 22 % 7 = ? | ? | ? |
| 31 | 31 % 7 = ? | ? | ? |
| 4 | 4 % 7 = ? | ? | ? |
| 15 | 15 % 7 = ? | ? | ? |
| 28 | 28 % 7 = ? | ? | ? |
| 17 | 17 % 7 = ? | ? | ? |
| 88 | 88 % 7 = ? | ? | ? |

Depois, desenhe a tabela hash resultante usando:
a) Encadeamento (lista encadeada em cada posição)
b) Sondagem linear (próxima posição livre)

**Respostas:**

| Chave | h(chave) | Índice | Colisao com |
|-------|----------|--------|-------------|
| 10 | 10 % 7 = 3 | 3 | — |
| 22 | 22 % 7 = 1 | 1 | — |
| 31 | 31 % 7 = 3 | 3 | 10 |
| 4 | 4 % 7 = 4 | 4 | — |
| 15 | 15 % 7 = 1 | 1 | 22 |
| 28 | 28 % 7 = 0 | 0 | — |
| 17 | 17 % 7 = 3 | 3 | 10, 31 |
| 88 | 88 % 7 = 4 | 4 | 4 |

---

## Exercício 3: Contador de Caracteres (C)

Usando a tabela hash do módulo, crie um programa que conta a frequência de cada caractere em uma string.

Dica: use o caractere como chave (convertido para string de 1 caractere) e a contagem como valor.

Teste:

```c
int main() {
    contar_caracteres("abracadabra");
    // Saida esperada (ordem pode variar):
    // 'a': 5
    // 'b': 2
    // 'r': 2
    // 'c': 1
    // 'd': 1

    printf("\n");
    contar_caracteres("mississippi");
    // 'm': 1
    // 'i': 4
    // 's': 4
    // 'p': 2

    return 0;
}
```

---

## Exercício 4: Verificador de Anagramas (Python)

Escreva uma função em Python que verifica se duas palavras são anagramas usando dicionários para contar a frequência de cada letra.

```python
def sao_anagramas(palavra1, palavra2):
    # Sua implementacao aqui
    pass

# Testes
print(sao_anagramas("listen", "silent"))    # True
print(sao_anagramas("hello", "world"))      # False
print(sao_anagramas("anagram", "nagaram"))  # True
print(sao_anagramas("rat", "car"))          # False
print(sao_anagramas("abc", "abcd"))         # False
```

Dica: crie um dicionário para cada palavra contando as letras. Compare os dois dicionários. Em Python, `dict1 == dict2` compara conteúdo.

**Resposta:**

```python
def sao_anagramas(palavra1, palavra2):
    # Se tamanhos diferentes, nao pode ser anagrama
    if len(palavra1) != len(palavra2):
        return False

    # Contar frequencia de cada letra
    freq1 = {}
    for letra in palavra1.lower():
        freq1[letra] = freq1.get(letra, 0) + 1

    freq2 = {}
    for letra in palavra2.lower():
        freq2[letra] = freq2.get(letra, 0) + 1

    return freq1 == freq2
```

---

## Exercício 5: Primeiro Caractere Não Repetido (Python)

Escreva uma função que encontra o primeiro caractere que não se repete em uma string.

```python
def primeiro_unico(texto):
    # Sua implementacao aqui
    pass

# Testes
print(primeiro_unico("aabccbd"))    # 'd'
print(primeiro_unico("abcabc"))     # None (todos repetem)
print(primeiro_unico("abcdef"))     # 'a' (nenhum repete, primeiro e 'a')
print(primeiro_unico("aabbccd"))    # 'd'
```

Dica: primeiro passe conta a frequência de cada caractere (dicionário). Segundo passe percorre a string e retorna o primeiro com frequência 1.

**Resposta:**

```python
def primeiro_unico(texto):
    # Contar frequencia
    freq = {}
    for c in texto:
        freq[c] = freq.get(c, 0) + 1

    # Encontrar primeiro com frequencia 1
    for c in texto:
        if freq[c] == 1:
            return c

    return None
```

---

## Exercício 6: Tabela Hash com Endereçamento Aberto (C)

Implemente uma tabela hash de inteiros usando sondagem linear. Quando há colisão, tente a próxima posição `(índice + 1) % tamanho`.

```c
#define TABLE_SIZE 10

typedef struct {
    int chaves[TABLE_SIZE];
    int ocupado[TABLE_SIZE];  // 0 = vazio, 1 = ocupado
} HashTableLinear;
```

Implemente:
- `inicializar(tabela)` — marcar todas as posições como vazias
- `inserir_linear(tabela, chave)` — inserir com sondagem linear
- `buscar_linear(tabela, chave)` — buscar com sondagem linear
- `imprimir_linear(tabela)` — mostrar a tabela

Teste:

```c
int main() {
    HashTableLinear tabela;
    inicializar(&tabela);

    inserir_linear(&tabela, 10);  // 10 % 10 = 0
    inserir_linear(&tabela, 20);  // 20 % 10 = 0 → colisao → 1
    inserir_linear(&tabela, 30);  // 30 % 10 = 0 → colisao → 2
    inserir_linear(&tabela, 15);  // 15 % 10 = 5
    inserir_linear(&tabela, 25);  // 25 % 10 = 5 → colisao → 6

    imprimir_linear(&tabela);
    // [0]: 10
    // [1]: 20
    // [2]: 30
    // [3]: (vazio)
    // [4]: (vazio)
    // [5]: 15
    // [6]: 25
    // ...

    printf("Buscar 20: %s\n", buscar_linear(&tabela, 20) ? "encontrado" : "nao encontrado");
    printf("Buscar 99: %s\n", buscar_linear(&tabela, 99) ? "encontrado" : "nao encontrado");

    return 0;
}
```

---

## Exercício 7: Dois Números que Somam um Alvo (Python)

Dado um array de números e um valor alvo, encontre dois números que somam o alvo. Use um dicionário para resolver em O(n).

```python
def dois_somam(numeros, alvo):
    # Sua implementacao aqui
    pass

# Testes
print(dois_somam([2, 7, 11, 15], 9))     # (2, 7)
print(dois_somam([3, 2, 4], 6))           # (2, 4)
print(dois_somam([1, 5, 3, 8], 11))       # (3, 8)
print(dois_somam([1, 2, 3], 10))          # None
```

Dica: para cada número, calcule o complemento (alvo - número). Verifique se o complemento já está no dicionário. Se sim, encontrou o par. Se não, guarde o número no dicionário.

**Resposta:**

```python
def dois_somam(numeros, alvo):
    vistos = {}  # numero → indice
    for num in numeros:
        complemento = alvo - num
        if complemento in vistos:
            return (complemento, num)
        vistos[num] = True
    return None
```

Este é um dos problemas mais clássicos de entrevistas técnicas (Two Sum no LeetCode). A solução com dicionário é O(n), enquanto a solução ingênua (dois loops) é O(n²).

---

## Exercício 8: Agrupar Anagramas (Python)

Dado uma lista de palavras, agrupe as que são anagramas entre si.

```python
def agrupar_anagramas(palavras):
    # Sua implementacao aqui
    pass

# Teste
resultado = agrupar_anagramas(["eat", "tea", "tan", "ate", "nat", "bat"])
print(resultado)
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
```

Dica: para cada palavra, ordene as letras (ex: "eat" → "aet") e use como chave do dicionário. O valor é a lista de palavras que têm a mesma chave ordenada.

**Resposta:**

```python
def agrupar_anagramas(palavras):
    grupos = {}
    for palavra in palavras:
        chave = ''.join(sorted(palavra))  # "eat" → "aet"
        if chave not in grupos:
            grupos[chave] = []
        grupos[chave].append(palavra)
    return list(grupos.values())
```

---

## Exercício 9: Cache Simples com Tabela Hash (C)

Implemente um cache simples usando a tabela hash do módulo. O cache armazena resultados de cálculos caros (simulados com uma função que demora).

```c
// Simular calculo caro
int calculo_caro(int n) {
    printf("    [CALCULANDO %d... demora!]\n", n);
    // Em um sistema real, isso seria uma query ao banco ou calculo complexo
    return n * n + 2 * n + 1;  // (n+1)^2
}
```

Implemente:
- `buscar_cache(cache, chave)` — retorna o resultado se estiver no cache
- `guardar_cache(cache, chave, valor)` — guarda um resultado no cache
- `calcular_com_cache(cache, n)` — verifica o cache antes de calcular

Teste:

```c
int main() {
    // Criar cache

    printf("Resultado de 5: %d\n", calcular_com_cache(cache, 5));   // calcula
    printf("Resultado de 10: %d\n", calcular_com_cache(cache, 10)); // calcula
    printf("Resultado de 5: %d\n", calcular_com_cache(cache, 5));   // usa cache!
    printf("Resultado de 10: %d\n", calcular_com_cache(cache, 10)); // usa cache!
    printf("Resultado de 7: %d\n", calcular_com_cache(cache, 7));   // calcula

    return 0;
}
```

Saída esperada:
```
    [CALCULANDO 5... demora!]
Resultado de 5: 36
    [CALCULANDO 10... demora!]
Resultado de 10: 121
Resultado de 5: 36 (cache)
Resultado de 10: 121 (cache)
    [CALCULANDO 7... demora!]
Resultado de 7: 64
```

---

## Exercício 10 (Desafio): Implementar um Dicionário Genérico em C

Implemente uma tabela hash que aceita chaves string e valores string (em vez de inteiros). Isso é mais próximo de um dicionário real.

```c
typedef struct Entry {
    char chave[50];
    char valor[100];
    struct Entry *next;
} Entry;
```

Implemente inserir, buscar, remover e imprimir. Teste com um "mini banco de dados" de contatos:

```c
int main() {
    HashTable *contatos = criar_tabela();

    inserir(contatos, "Ana", "ana@email.com");
    inserir(contatos, "Bruno", "bruno@email.com");
    inserir(contatos, "Carol", "carol@email.com");

    char *email = buscar(contatos, "Bruno");
    if (email) printf("Bruno: %s\n", email);  // bruno@email.com

    inserir(contatos, "Bruno", "bruno.novo@email.com");  // atualizar
    email = buscar(contatos, "Bruno");
    if (email) printf("Bruno: %s\n", email);  // bruno.novo@email.com

    remover(contatos, "Carol");
    email = buscar(contatos, "Carol");
    if (!email) printf("Carol: nao encontrada\n");

    liberar_tabela(contatos);
    return 0;
}
```

---

[← Voltar ao conteúdo: Dicionários e Tabelas Hash](cap07-mod09-dicionarios-conteudo.md)
