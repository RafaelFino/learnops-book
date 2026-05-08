# 7.5 — Exercícios: Arrays

[← Voltar ao conteúdo: Arrays](cap07-mod05-arrays-conteudo.md)

---

## Sobre Estes Exercícios

Arrays são a estrutura de dados mais fundamental — e a que você mais vai usar na carreira. Estes exercícios cobrem desde operações básicas (criar, preencher, percorrer) até padrões mais avançados (busca, filtro, transformação). Compile sempre com `gcc -Wall` para ver avisos úteis.

Dica: antes de escrever código, pense no algoritmo. Pergunte-se: "preciso percorrer o array inteiro ou posso parar antes?", "preciso de um array auxiliar ou posso modificar o original?", "qual o tamanho máximo que o array pode ter?".

---

## Exercício 1 — Preencher e Imprimir (Básico)

### Enunciado

Crie um programa `preencher_array.c` que:

1. Declare um array de 10 inteiros
2. Preencha cada posição com o valor `(i + 1) * 10` usando um loop (10, 20, 30, ..., 100)
3. Imprima todos os valores em uma linha, separados por espaço
4. Imprima todos os valores na ordem inversa
5. Imprima apenas os valores nas posições pares (0, 2, 4, 6, 8)

### Exemplo de saída esperada

```
=== Preencher e Imprimir ===
Original:       10 20 30 40 50 60 70 80 90 100
Invertido:      100 90 80 70 60 50 40 30 20 10
Posicoes pares: 10 30 50 70 90
```

---

## Exercício 2 — Soma e Média com Entrada do Usuário (Básico)

### Enunciado

Crie um programa `soma_media.c` que:

1. Pergunte ao usuário quantos números ele quer digitar (use `malloc`)
2. Leia cada número
3. Imprima todos os números digitados
4. Calcule e imprima a soma e a média (com 2 casas decimais)
5. Libere a memória

### Exemplo de saída esperada

```
=== Soma e Media ===
Quantos numeros? 4
Numero 1: 15
Numero 2: 22
Numero 3: 8
Numero 4: 35

Numeros: 15 22 8 35
Soma:  80
Media: 20.00

Memoria liberada.
```

### Dicas

- Verifique se `malloc` retornou NULL
- Use `(float)soma / n` para a média (casting para evitar divisão inteira)

---

## Exercício 3 — Maior, Menor e Amplitude (Básico)

### Enunciado

Crie um programa `extremos_array.c` que:

1. Declare um array com os valores: `{45, 12, 78, 3, 56, 91, 34, 67, 23, 89}`
2. Encontre o maior valor e em qual posição ele está
3. Encontre o menor valor e em qual posição ele está
4. Calcule a amplitude (maior - menor)
5. Imprima tudo formatado

### Exemplo de saída esperada

```
=== Extremos ===
Array: 45 12 78 3 56 91 34 67 23 89
Maior: 91 (posicao 5)
Menor: 3 (posicao 3)
Amplitude: 88
```

### Dicas

- Comece assumindo que o primeiro elemento é o maior e o menor
- Guarde tanto o valor quanto o índice ao encontrar um novo extremo

---

## Exercício 4 — Busca Linear Completa (Intermediário)

### Enunciado

Crie um programa `busca_completa.c` que:

1. Declare um array com os valores: `{10, 25, 10, 40, 25, 10, 60, 25, 80, 10}`
2. Peça ao usuário um valor para buscar
3. Imprima:
   - Se o valor existe no array
   - Em quais posições ele aparece (todas, não apenas a primeira)
   - Quantas vezes ele aparece no total

### Exemplo de saída esperada

```
=== Busca Completa ===
Array: 10 25 10 40 25 10 60 25 80 10
Buscar valor: 10

Valor 10 encontrado!
Posicoes: 0 2 5 9
Total de ocorrencias: 4
```

```
Buscar valor: 99

Valor 99 nao encontrado.
```

### Dicas

- Percorra o array inteiro mesmo depois de encontrar a primeira ocorrência
- Use um contador para as ocorrências

---

## Exercício 5 — Filtrar Aprovados (Intermediário)

### Enunciado

Crie um programa `filtrar_aprovados.c` que:

1. Declare um array com 12 notas: `{85, 42, 92, 55, 78, 95, 38, 88, 70, 61, 49, 73}`
2. Crie dois arrays auxiliares: um para aprovados (nota >= 60) e outro para reprovados
3. Preencha os arrays auxiliares percorrendo o original
4. Imprima as três listas e as estatísticas

### Exemplo de saída esperada

```
=== Filtrar Aprovados ===
Todas as notas: 85 42 92 55 78 95 38 88 70 61 49 73
Aprovados (8):  85 92 78 95 88 70 61 73
Reprovados (4): 42 55 38 49

Taxa de aprovacao: 66.7%
Media dos aprovados:  80.3
Media dos reprovados: 46.0
```

---

## Exercício 6 — Inverter Array In-Place (Intermediário)

### Enunciado

Crie um programa `inverter_inplace.c` que:

1. Peça ao usuário quantos números quer digitar (use `malloc`)
2. Leia os números
3. Inverta o array **sem usar um array auxiliar** (troque elementos usando a técnica do swap)
4. Imprima o array antes e depois da inversão
5. Libere a memória

### Exemplo de saída esperada

```
=== Inverter In-Place ===
Quantos numeros? 6
Numero 1: 10
Numero 2: 20
Numero 3: 30
Numero 4: 40
Numero 5: 50
Numero 6: 60

Antes:  10 20 30 40 50 60
Depois: 60 50 40 30 20 10
```

### Dicas

- Use dois índices: um no início (`i = 0`) e outro no fim (`j = n - 1`)
- Troque `arr[i]` com `arr[j]`, depois avance `i` e recue `j`
- Pare quando `i >= j`
- Crie uma função `void swap(int *a, int *b)` para a troca

---

## Exercício 7 — Array Dinâmico Crescente (Intermediário)

### Enunciado

Crie um programa `array_crescente.c` que simule o comportamento de `append()` do Python:

1. Comece com capacidade 2 (aloque com `malloc`)
2. Peça números ao usuário em loop (digite 0 para parar)
3. Quando o array estiver cheio, dobre a capacidade com `realloc`
4. Imprima uma mensagem cada vez que o array for redimensionado
5. No final, imprima todos os números e a capacidade final

### Exemplo de saída esperada

```
=== Array Crescente ===
Capacidade inicial: 2
Digite numeros (0 para parar):
> 10
> 20
  [Redimensionando: capacidade 2 -> 4]
> 30
> 40
  [Redimensionando: capacidade 4 -> 8]
> 50
> 0

Numeros digitados: 10 20 30 40 50
Quantidade: 5
Capacidade final: 8
```

### Dicas

- Mantenha duas variáveis: `quantidade` (quantos elementos tem) e `capacidade` (quantos cabem)
- Antes de adicionar, verifique se `quantidade == capacidade`
- Use variável temporária para `realloc` (para não perder dados se falhar)

---

## Exercício 8 — Tabela de Notas 2D (Intermediário)

### Enunciado

Crie um programa `tabela_notas.c` que:

1. Declare um array 2D `int notas[4][3]` representando 4 alunos com 3 provas cada
2. Preencha com os valores:
   - Aluno 0: 85, 92, 78
   - Aluno 1: 70, 65, 88
   - Aluno 2: 95, 87, 91
   - Aluno 3: 60, 72, 68
3. Imprima uma tabela formatada com a média de cada aluno
4. Calcule e imprima a média geral da turma
5. Identifique o aluno com a maior média

### Exemplo de saída esperada

```
=== Tabela de Notas ===
          P1   P2   P3   Media
Aluno 0:  85   92   78   85.0
Aluno 1:  70   65   88   74.3
Aluno 2:  95   87   91   91.0
Aluno 3:  60   72   68   66.7

Media geral da turma: 79.3
Melhor aluno: Aluno 2 (media 91.0)
```

---

## Exercício 9 — Manipulação de Strings (Intermediário)

### Enunciado

Crie um programa `manipula_string.c` que:

1. Peça ao usuário uma frase (use `fgets` com buffer de 100 caracteres)
2. Conte quantos caracteres a frase tem (sem contar `'\n'` e `'\0'`)
3. Conte quantas vogais (a, e, i, o, u — maiúsculas e minúsculas)
4. Conte quantos espaços
5. Imprima a frase em maiúsculas (percorra o array e converta cada caractere)

### Exemplo de saída esperada

```
=== Manipulacao de Strings ===
Digite uma frase: Estruturas de dados com C

Caracteres: 25
Vogais: 9
Espacos: 4
Maiusculas: ESTRUTURAS DE DADOS COM C
```

### Dicas

- Para converter minúscula em maiúscula: se o caractere está entre 'a' e 'z', subtraia 32 (diferença ASCII)
- Ou use a função `toupper()` de `<ctype.h>`
- Lembre que `fgets` inclui o `'\n'` — remova-o se necessário

---

## Exercício 10 — Merge de Arrays Ordenados (Avançado)

### Enunciado

Crie um programa `merge_arrays.c` que:

1. Declare dois arrays já ordenados:
   - `a[] = {3, 8, 15, 22, 40}`
   - `b[] = {5, 10, 18, 25, 30, 45, 50}`
2. Crie um terceiro array `resultado` que contenha todos os elementos de `a` e `b` em ordem crescente
3. Use o algoritmo de merge: compare os menores elementos de cada array e coloque o menor no resultado

### Exemplo de saída esperada

```
=== Merge de Arrays Ordenados ===
Array A: 3 8 15 22 40
Array B: 5 10 18 25 30 45 50
Merge:   3 5 8 10 15 18 22 25 30 40 45 50
```

### Dicas

- Use três índices: `i` para array A, `j` para array B, `k` para resultado
- Compare `a[i]` com `b[j]`: coloque o menor em `resultado[k]` e avance o índice correspondente
- Quando um array acabar, copie o restante do outro
- Este é o mesmo algoritmo usado no Merge Sort — prévia do módulo 7.10

---

## Exercício 11 — Rotacionar Array (Avançado)

### Enunciado

Crie um programa `rotacionar.c` com uma função que rotaciona um array `k` posições para a direita:

```c
void rotacionar_direita(int arr[], int n, int k);
```

Exemplo: rotacionar `{1, 2, 3, 4, 5}` por 2 posições resulta em `{4, 5, 1, 2, 3}`.

No `main`:
1. Declare `int arr[] = {10, 20, 30, 40, 50, 60, 70}`
2. Imprima o array original
3. Rotacione 3 posições para a direita
4. Imprima o resultado

### Exemplo de saída esperada

```
=== Rotacionar Array ===
Original:    10 20 30 40 50 60 70
Rotacionado: 50 60 70 10 20 30 40
```

### Dicas

- Abordagem simples: use um array auxiliar temporário
- Abordagem elegante: inverta o array inteiro, depois inverta os primeiros `k` elementos, depois inverta os restantes
- Trate o caso `k > n` usando `k = k % n`

---

## Gabarito Parcial

### Exercício 1 — Preencher e Imprimir

```c
// preencher_array.c — Operacoes basicas com array
#include <stdio.h>

int main() {
    int arr[10];
    int i;

    // Preencher: 10, 20, 30, ..., 100
    for (i = 0; i < 10; i++) {
        arr[i] = (i + 1) * 10;
    }

    printf("=== Preencher e Imprimir ===\n");

    // Original
    printf("Original:       ");
    for (i = 0; i < 10; i++) printf("%d ", arr[i]);
    printf("\n");

    // Invertido
    printf("Invertido:      ");
    for (i = 9; i >= 0; i--) printf("%d ", arr[i]);
    printf("\n");

    // Posicoes pares
    printf("Posicoes pares: ");
    for (i = 0; i < 10; i += 2) printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

### Exercício 6 — Inverter In-Place

```c
// inverter_inplace.c — Inverter array sem array auxiliar
#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void inverter(int arr[], int n) {
    int i = 0;
    int j = n - 1;
    while (i < j) {
        swap(&arr[i], &arr[j]);
        i++;
        j--;
    }
}

void imprimir(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int n;
    printf("=== Inverter In-Place ===\n");
    printf("Quantos numeros? ");
    scanf("%d", &n);

    int *arr = (int*)malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("Erro ao alocar memoria!\n");
        return 1;
    }

    int i;
    for (i = 0; i < n; i++) {
        printf("Numero %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    printf("\nAntes:  ");
    imprimir(arr, n);

    inverter(arr, n);

    printf("Depois: ");
    imprimir(arr, n);

    free(arr);
    arr = NULL;

    return 0;
}
```

### Exercício 10 — Merge de Arrays Ordenados

```c
// merge_arrays.c — Merge de dois arrays ordenados
#include <stdio.h>

void imprimir(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

void merge(int a[], int na, int b[], int nb, int resultado[]) {
    int i = 0, j = 0, k = 0;

    // Comparar elementos dos dois arrays
    while (i < na && j < nb) {
        if (a[i] <= b[j]) {
            resultado[k] = a[i];
            i++;
        } else {
            resultado[k] = b[j];
            j++;
        }
        k++;
    }

    // Copiar restante de a (se houver)
    while (i < na) {
        resultado[k] = a[i];
        i++;
        k++;
    }

    // Copiar restante de b (se houver)
    while (j < nb) {
        resultado[k] = b[j];
        j++;
        k++;
    }
}

int main() {
    int a[] = {3, 8, 15, 22, 40};
    int b[] = {5, 10, 18, 25, 30, 45, 50};
    int na = 5, nb = 7;
    int resultado[12];  // na + nb

    printf("=== Merge de Arrays Ordenados ===\n");
    printf("Array A: ");
    imprimir(a, na);
    printf("Array B: ");
    imprimir(b, nb);

    merge(a, na, b, nb, resultado);

    printf("Merge:   ");
    imprimir(resultado, na + nb);

    return 0;
}
```

---

[← Voltar ao conteúdo: Arrays](cap07-mod05-arrays-conteudo.md) · [Próximo: Listas Encadeadas →](cap07-mod06-listas-conteudo.md)
