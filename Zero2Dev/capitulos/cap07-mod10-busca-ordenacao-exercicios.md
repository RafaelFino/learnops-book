# 7.10 — Exercícios: Algoritmos de Busca e Ordenação

[← Voltar ao conteúdo: Busca e Ordenação](cap07-mod10-busca-ordenacao-conteudo.md)

---

## Sobre os Exercícios

Estes exercícios cobrem busca linear, busca binária e os algoritmos de ordenação apresentados no módulo 7.10.

```bash
gcc -o exercicio exercicio.c
./exercicio
```

---

## Exercício 1: Conceitos Fundamentais

Responda sem consultar o material:

a) Qual a diferença entre busca linear e busca binária? Qual o requisito da busca binária?

b) Qual a complexidade da busca linear no pior caso? E da busca binária?

c) Para um array de 1 milhão de elementos, quantas comparações a busca binária faz no máximo?

d) Explique a diferença entre Bubble Sort, Selection Sort e Insertion Sort em uma frase cada.

e) O que significa um algoritmo de ordenação ser "estável"?

---

## Exercício 2: Busca Binária no Papel

Dado o array ordenado `[3, 7, 11, 15, 19, 23, 27, 31, 35, 39]`, rastreie a busca binária para os seguintes alvos. Mostre esquerda, meio, direita a cada passo:

a) Buscar 23
b) Buscar 3
c) Buscar 40 (não existe)

**Resposta para (a) — Buscar 23:**

| Passo | Esquerda | Meio | Valor do meio | Direita | Ação |
|-------|----------|------|---------------|---------|------|
| 1 | 0 | 4 | 19 | 9 | 23 > 19, ir para direita |
| 2 | 5 | 7 | 31 | 9 | 23 < 31, ir para esquerda |
| 3 | 5 | 5 | 23 | 6 | 23 == 23, encontrado! |

---

## Exercício 3: Implementar Busca Binária Recursiva

Implemente a busca binária usando recursão:

```c
int busca_binaria_rec(int arr[], int esquerda, int direita, int alvo) {
    // Sua implementacao aqui
}
```

Teste:

```c
int main() {
    int arr[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int tam = 10;

    printf("Buscar 23: posicao %d\n", busca_binaria_rec(arr, 0, tam-1, 23));  // 5
    printf("Buscar 2: posicao %d\n", busca_binaria_rec(arr, 0, tam-1, 2));    // 0
    printf("Buscar 91: posicao %d\n", busca_binaria_rec(arr, 0, tam-1, 91));  // 9
    printf("Buscar 50: posicao %d\n", busca_binaria_rec(arr, 0, tam-1, 50));  // -1

    return 0;
}
```

**Resposta:**

```c
int busca_binaria_rec(int arr[], int esquerda, int direita, int alvo) {
    if (esquerda > direita) return -1;  // caso base: nao encontrou

    int meio = esquerda + (direita - esquerda) / 2;

    if (arr[meio] == alvo) return meio;
    if (arr[meio] < alvo) return busca_binaria_rec(arr, meio + 1, direita, alvo);
    return busca_binaria_rec(arr, esquerda, meio - 1, alvo);
}
```

---

## Exercício 4: Contar Comparações dos Algoritmos

Modifique Bubble Sort, Selection Sort e Insertion Sort para contar comparações. Teste com o array `{64, 34, 25, 12, 22, 11, 90, 45, 78, 33}` e compare:

```c
int main() {
    int arr1[] = {64, 34, 25, 12, 22, 11, 90, 45, 78, 33};
    int arr2[] = {64, 34, 25, 12, 22, 11, 90, 45, 78, 33};
    int arr3[] = {64, 34, 25, 12, 22, 11, 90, 45, 78, 33};
    int tam = 10;

    int comp_bubble = bubble_sort_contando(arr1, tam);
    int comp_selection = selection_sort_contando(arr2, tam);
    int comp_insertion = insertion_sort_contando(arr3, tam);

    printf("Bubble Sort: %d comparacoes\n", comp_bubble);
    printf("Selection Sort: %d comparacoes\n", comp_selection);
    printf("Insertion Sort: %d comparacoes\n", comp_insertion);

    return 0;
}
```

Dica: adicione um contador que incrementa a cada `if (arr[i] > arr[j])`.

---

## Exercício 5: Ordenar Structs com qsort

Crie um array de structs `Aluno` com nome e nota. Use `qsort` para ordenar por nota decrescente. Em caso de empate, ordenar por nome crescente.

```c
typedef struct {
    char nome[50];
    float nota;
} Aluno;

int main() {
    Aluno alunos[] = {
        {"Carol", 8.5},
        {"Ana", 9.2},
        {"Bruno", 7.8},
        {"David", 9.2},
        {"Eva", 8.5}
    };
    int tam = 5;

    qsort(alunos, tam, sizeof(Aluno), comparar_alunos);

    printf("Ranking:\n");
    for (int i = 0; i < tam; i++) {
        printf("  %d. %s — %.1f\n", i+1, alunos[i].nome, alunos[i].nota);
    }
    // 1. Ana — 9.2
    // 2. David — 9.2
    // 3. Carol — 8.5
    // 4. Eva — 8.5
    // 5. Bruno — 7.8

    return 0;
}
```

Dica: na função de comparação, primeiro compare as notas (decrescente). Se forem iguais, compare os nomes com `strcmp` (crescente).

---

## Exercício 6: Busca Linear com Condição

Implemente uma função que encontra todos os elementos de um array que satisfazem uma condição (ex: maiores que um valor). Retorne quantos foram encontrados.

```c
int buscar_maiores(int arr[], int tam, int limite, int resultados[]) {
    // Sua implementacao
}

int main() {
    int arr[] = {42, 17, 93, 8, 56, 31, 74, 25, 60, 12};
    int resultados[10];

    int count = buscar_maiores(arr, 10, 50, resultados);
    printf("Maiores que 50: ");
    for (int i = 0; i < count; i++) printf("%d ", resultados[i]);
    printf("(%d encontrados)\n", count);
    // 93 56 74 60 (4 encontrados)

    return 0;
}
```

---

## Exercício 7: Verificar se Array está Ordenado

Escreva uma função que verifica se um array está ordenado em ordem crescente. Retorna 1 se sim, 0 se não.

```c
int esta_ordenado(int arr[], int tam) {
    // Sua implementacao
}

int main() {
    int a[] = {1, 2, 3, 4, 5};
    int b[] = {1, 3, 2, 4, 5};
    int c[] = {5, 4, 3, 2, 1};

    printf("a: %s\n", esta_ordenado(a, 5) ? "ordenado" : "nao ordenado");  // ordenado
    printf("b: %s\n", esta_ordenado(b, 5) ? "ordenado" : "nao ordenado");  // nao ordenado
    printf("c: %s\n", esta_ordenado(c, 5) ? "ordenado" : "nao ordenado");  // nao ordenado

    return 0;
}
```

---

## Exercício 8: Insertion Sort para Strings

Adapte o Insertion Sort para ordenar um array de strings em ordem alfabética.

```c
int main() {
    char *nomes[] = {"Eva", "Ana", "David", "Bruno", "Carol"};
    int tam = 5;

    insertion_sort_strings(nomes, tam);

    for (int i = 0; i < tam; i++) printf("%s ", nomes[i]);
    // Ana Bruno Carol David Eva

    return 0;
}
```

Dica: use `strcmp` para comparar strings e troque ponteiros (não copie strings inteiras).

---

## Exercício 9 (Desafio): Merge de Dois Arrays Ordenados

Dados dois arrays já ordenados, crie um terceiro array que contém todos os elementos dos dois, também ordenado. Faça isso em O(n + m) — sem reordenar.

```c
int main() {
    int a[] = {1, 5, 9, 13, 17};
    int b[] = {2, 6, 10, 14};
    int resultado[9];

    merge(a, 5, b, 4, resultado);

    printf("Merge: ");
    for (int i = 0; i < 9; i++) printf("%d ", resultado[i]);
    // 1 2 5 6 9 10 13 14 17

    return 0;
}
```

Dica: use dois índices (um para cada array). Compare os elementos atuais e copie o menor para o resultado. Avance o índice do array de onde copiou.

---

## Exercício 10 (Desafio): Encontrar o K-ésimo Menor Elemento

Dado um array não ordenado, encontre o k-ésimo menor elemento sem ordenar o array inteiro.

Estratégia simples: use Selection Sort parcial — encontre o menor k vezes.

```c
int main() {
    int arr[] = {42, 17, 93, 8, 56, 31, 74};

    printf("1o menor: %d\n", k_esimo_menor(arr, 7, 1));  // 8
    printf("3o menor: %d\n", k_esimo_menor(arr, 7, 3));  // 31
    printf("5o menor: %d\n", k_esimo_menor(arr, 7, 5));  // 56

    return 0;
}
```

---

[← Voltar ao conteúdo: Busca e Ordenação](cap07-mod10-busca-ordenacao-conteudo.md)
