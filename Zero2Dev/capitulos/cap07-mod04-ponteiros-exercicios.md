# 7.4 — Exercícios: Ponteiros

[← Voltar ao conteúdo: Ponteiros](cap07-mod04-ponteiros-conteudo.md)

---

## Sobre Estes Exercícios

Ponteiros são o conceito mais desafiador de C para quem vem de Python. Estes exercícios foram pensados para construir confiança progressivamente — começando com o básico (ler endereços, derreferenciar) e avançando até alocação dinâmica e funções com ponteiros. Compile sempre com `gcc -Wall` para ver avisos úteis.

Dica importante: para muitos destes exercícios, **desenhe o estado da memória no papel** antes de executar o código. Isso treina sua capacidade de "pensar como o computador" e é a habilidade mais valiosa que você pode desenvolver neste módulo.

---

## Exercício 1 — Meu Primeiro Ponteiro (Básico)

### Enunciado

Crie um programa `primeiro_ponteiro.c` que:

1. Declare uma variável `int número = 42`
2. Declare um ponteiro `int *ptr` que aponte para `número`
3. Imprima as seguintes informações em formato de tabela:
   - O valor de `número`
   - O endereço de `número` (usando `&`)
   - O valor de `ptr` (o endereço que ele guarda)
   - O valor acessado via `*ptr` (dereferência)
   - O endereço do próprio `ptr` (usando `&ptr`)
   - O tamanho de `ptr` em bytes (usando `sizeof`)

### Exemplo de saída esperada

```
=== Meu Primeiro Ponteiro ===
Valor de numero:          42
Endereco de numero (&):   0x7ffeefbff3fc
Valor de ptr:             0x7ffeefbff3fc
Valor via *ptr:           42
Endereco do proprio ptr:  0x7ffeefbff3f0
Tamanho de ptr:           8 bytes
```

### Dicas

- O endereço de `número` e o valor de `ptr` devem ser iguais
- O endereço do próprio `ptr` é diferente — `ptr` é uma variável separada que ocupa 8 bytes
- Use `%p` para imprimir endereços e `(void*)` para o casting

---

## Exercício 2 — Modificando Via Ponteiro (Básico)

### Enunciado

Crie um programa `modifica_ponteiro.c` que:

1. Declare `int x = 10`
2. Declare um ponteiro `int *ptr = &x`
3. Imprima o valor de `x`
4. Modifique o valor usando `*ptr = 50`
5. Imprima `x` novamente (deve ter mudado)
6. Modifique `x` diretamente para 100
7. Imprima `*ptr` (deve refletir a mudança)

O objetivo é comprovar que `x` e `*ptr` se referem ao mesmo espaço de memória.

### Exemplo de saída esperada

```
=== Modificando Via Ponteiro ===
Passo 1 - x = 10, *ptr = 10
Passo 2 - Modificando *ptr para 50...
           x = 50, *ptr = 50
Passo 3 - Modificando x para 100...
           x = 100, *ptr = 100
Conclusao: x e *ptr sao o mesmo espaco de memoria!
```

---

## Exercício 3 — Ponteiro Viajante (Básico)

### Enunciado

Crie um programa `ponteiro_viajante.c` que:

1. Declare três variáveis: `int a = 10, b = 20, c = 30`
2. Declare um ponteiro `int *ptr`
3. Faça `ptr` apontar para `a`, imprima `*ptr`
4. Faça `ptr` apontar para `b`, imprima `*ptr`
5. Faça `ptr` apontar para `c`, imprima `*ptr`
6. Modifique o valor de `c` através de `*ptr` para 999
7. Imprima `a`, `b` e `c` para mostrar que só `c` mudou

### Exemplo de saída esperada

```
=== Ponteiro Viajante ===
ptr -> a: *ptr = 10
ptr -> b: *ptr = 20
ptr -> c: *ptr = 30

Modificando *ptr = 999 (ptr aponta para c)
a = 10 (nao mudou)
b = 20 (nao mudou)
c = 999 (mudou!)
```

---

## Exercício 4 — Swap Completo (Intermediário)

### Enunciado

Crie um programa `swap_completo.c` que implemente e teste uma função `swap`:

1. Implemente `void swap(int *a, int *b)` que troca os valores de duas variáveis
2. No `main`, declare três pares de variáveis e troque cada par:
   - `x = 10, y = 20`
   - `p = -5, q = 100`
   - `m = 0, n = 0` (caso especial: trocar valores iguais)
3. Para cada par, imprima "Antes" e "Depois"

### Exemplo de saída esperada

```
=== Swap Completo ===

Par 1: x=10, y=20
  Antes:  x=10, y=20
  Depois: x=20, y=10

Par 2: p=-5, q=100
  Antes:  p=-5, q=100
  Depois: p=100, q=-5

Par 3: m=0, n=0
  Antes:  m=0, n=0
  Depois: m=0, n=0 (valores iguais, nada muda)
```

### Dicas

- A função `swap` usa uma variável temporária `temp` para não perder um dos valores
- Lembre-se: passe `&x` e `&y` na chamada, não `x` e `y`

---

## Exercício 5 — Calculadora com Ponteiros (Intermediário)

### Enunciado

Crie um programa `calculadora_ptr.c` com uma função que recebe dois números e retorna os quatro resultados das operações básicas via ponteiros:

```c
void calcular(int a, int b, int *soma, int *sub, int *mult, float *divisao);
```

A função deve:
- Calcular soma, subtração, multiplicação e divisão
- Guardar os resultados nos endereços recebidos
- Tratar divisão por zero (se `b == 0`, guardar 0.0 em `*divisao` e imprimir aviso)

No `main`, peça dois números ao usuário e mostre os resultados.

### Exemplo de saída esperada

```
=== Calculadora com Ponteiros ===
Digite o primeiro numero: 15
Digite o segundo numero: 4

Resultados:
  15 + 4 = 19
  15 - 4 = 11
  15 * 4 = 60
  15 / 4 = 3.75
```

---

## Exercício 6 — Alocação Dinâmica Básica (Intermediário)

### Enunciado

Crie um programa `aloca_numeros.c` que:

1. Pergunte ao usuário quantos números ele quer guardar
2. Use `malloc` para alocar espaço para essa quantidade de inteiros
3. Verifique se `malloc` retornou NULL (tratar erro)
4. Peça cada número ao usuário
5. Imprima todos os números
6. Calcule e imprima a soma e a média
7. Libere a memória com `free`

### Exemplo de saída esperada

```
=== Alocacao Dinamica ===
Quantos numeros? 4
Digite o numero 1: 10
Digite o numero 2: 20
Digite o numero 3: 30
Digite o numero 4: 40

Numeros digitados: 10 20 30 40
Soma: 100
Media: 25.00

Memoria liberada com sucesso.
```

### Dicas

- Use `int *números = (int*)malloc(quantidade * sizeof(int));`
- Acesse cada posição com `números[i]`
- Não esqueça de `free(números)` no final

---

## Exercício 7 — Encontrar Extremos (Intermediário)

### Enunciado

Crie um programa `extremos.c` com uma função que encontra o maior e o menor valor de um conjunto de números usando ponteiros:

```c
void encontrar_extremos(int *valores, int quantidade, int *maior, int *menor);
```

No `main`:
1. Aloque dinamicamente um array de 6 inteiros
2. Preencha com os valores: 45, 12, 78, 3, 56, 91
3. Chame a função `encontrar_extremos`
4. Imprima o maior e o menor valor
5. Libere a memória

### Exemplo de saída esperada

```
=== Encontrar Extremos ===
Valores: 45 12 78 3 56 91
Maior: 91
Menor: 3
```

---

## Exercício 8 — Trace de Ponteiros (Avançado)

### Enunciado

Sem executar o programa abaixo, determine o valor de cada variável nos pontos marcados com `// TRACE`. Desenhe o estado da memória (variáveis e ponteiros) em cada ponto. Depois execute e compare.

```c
#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int *p1 = &a;
    int *p2 = &b;

    // TRACE 1: Quais os valores de a, b, *p1, *p2?

    *p1 = 20;
    // TRACE 2: Quais os valores de a, b, *p1, *p2?

    *p2 = *p1 + 3;
    // TRACE 3: Quais os valores de a, b, *p1, *p2?

    p1 = p2;
    // TRACE 4: Quais os valores de a, b, *p1, *p2?

    *p1 = 100;
    // TRACE 5: Quais os valores de a, b, *p1, *p2?

    printf("a=%d, b=%d, *p1=%d, *p2=%d\n", a, b, *p1, *p2);

    return 0;
}
```

### Formato da resposta

Preencha antes de executar:

```
TRACE 1: a=5,  b=10, *p1=?,  *p2=?
TRACE 2: a=?,  b=10, *p1=?,  *p2=?
TRACE 3: a=?,  b=?,  *p1=?,  *p2=?
TRACE 4: a=?,  b=?,  *p1=?,  *p2=?
TRACE 5: a=?,  b=?,  *p1=?,  *p2=?
```

### Dica

O passo mais traiçoeiro é o TRACE 4: `p1 = p2` faz `p1` apontar para o mesmo lugar que `p2` (para `b`). A partir daí, `*p1` e `*p2` acessam a mesma variável.

---

## Exercício 9 — Detector de Memory Leak (Avançado)

### Enunciado

Análise o código abaixo e identifique todos os memory leaks. Para cada leak encontrado, explique o problema e mostre a correção. Não execute o código — faça a análise mentalmente.

```c
#include <stdio.h>
#include <stdlib.h>

void funcao_a() {
    int *p = (int*)malloc(sizeof(int));
    *p = 42;
    printf("funcao_a: %d\n", *p);
    // Fim da funcao — p e destruido, mas a memoria alocada nao
}

void funcao_b() {
    int *p = (int*)malloc(10 * sizeof(int));
    int i;
    for (i = 0; i < 10; i++) {
        p[i] = i * 10;
    }
    p = (int*)malloc(5 * sizeof(int));  // Novo malloc sem free do anterior
    int j;
    for (j = 0; j < 5; j++) {
        p[j] = j;
    }
    free(p);
}

void funcao_c(int condicao) {
    int *p = (int*)malloc(sizeof(int));
    *p = 100;
    if (condicao) {
        printf("Condicao verdadeira: %d\n", *p);
        return;  // Retorna sem free!
    }
    free(p);
}

int main() {
    funcao_a();
    funcao_b();
    funcao_c(1);
    funcao_c(0);
    return 0;
}
```

### Formato da resposta

Para cada leak, indique:
1. Qual função tem o problema
2. Qual linha causa o leak
3. Quantos bytes são vazados
4. Como corrigir

---

## Exercício 10 — Função Estatísticas (Avançado)

### Enunciado

Crie um programa `estatisticas.c` com uma função que calcula múltiplas estatísticas de um array de números, retornando tudo via ponteiros:

```c
void estatisticas(int *valores, int n, int *soma, float *media, int *maior, int *menor, int *amplitude);
```

Onde `amplitude` = maior - menor.

No `main`:
1. Peça ao usuário quantos números quer digitar
2. Aloque memória dinamicamente
3. Peça os números
4. Chame a função `estatisticas`
5. Imprima todos os resultados formatados
6. Libere a memória

### Exemplo de saída esperada

```
=== Estatisticas ===
Quantos numeros? 5
Numero 1: 85
Numero 2: 92
Numero 3: 78
Numero 4: 95
Numero 5: 88

=== Resultados ===
Numeros: 85 92 78 95 88
Soma:      438
Media:     87.60
Maior:     95
Menor:     78
Amplitude: 17
```

---

## Exercício 11 — Ordenar com Swap (Avançado)

### Enunciado

Crie um programa `ordenar_swap.c` que:

1. Aloque dinamicamente um array de 8 inteiros
2. Preencha com valores desordenados: 64, 25, 12, 22, 11, 90, 45, 33
3. Implemente a função `void swap(int *a, int *b)` para trocar dois valores
4. Use a função `swap` dentro de um algoritmo simples de ordenação (bubble sort):
   - Percorra o array comparando pares vizinhos
   - Se o anterior for maior que o próximo, troque com `swap`
   - Repita até não haver mais trocas
5. Imprima o array antes e depois da ordenação
6. Libere a memória

### Exemplo de saída esperada

```
=== Ordenar com Swap ===
Antes:  64 25 12 22 11 90 45 33
Depois: 11 12 22 25 33 45 64 90
```

### Dicas

- Bubble sort: dois loops aninhados, o externo repete n-1 vezes, o interno compara vizinhos
- Use `swap(&arr[j], &arr[j+1])` para trocar elementos vizinhos
- Este exercício é uma prévia do módulo 7.10 (Busca e Ordenação)

---

## Gabarito Parcial

### Exercício 1 — Meu Primeiro Ponteiro

```c
// primeiro_ponteiro.c — Explorando ponteiros
#include <stdio.h>

int main() {
    int numero = 42;
    int *ptr = &numero;  // ptr aponta para numero

    printf("=== Meu Primeiro Ponteiro ===\n");
    printf("Valor de numero:          %d\n", numero);
    printf("Endereco de numero (&):   %p\n", (void*)&numero);
    printf("Valor de ptr:             %p\n", (void*)ptr);
    printf("Valor via *ptr:           %d\n", *ptr);
    printf("Endereco do proprio ptr:  %p\n", (void*)&ptr);
    printf("Tamanho de ptr:           %lu bytes\n", sizeof(ptr));

    return 0;
}
```

### Exercício 4 — Swap Completo

```c
// swap_completo.c — Funcao swap com ponteiros
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;  // Guarda o valor apontado por a
    *a = *b;        // Coloca o valor de b no endereco de a
    *b = temp;      // Coloca o valor original de a no endereco de b
}

int main() {
    printf("=== Swap Completo ===\n\n");

    // Par 1
    int x = 10, y = 20;
    printf("Par 1: x=10, y=20\n");
    printf("  Antes:  x=%d, y=%d\n", x, y);
    swap(&x, &y);
    printf("  Depois: x=%d, y=%d\n\n", x, y);

    // Par 2
    int p = -5, q = 100;
    printf("Par 2: p=-5, q=100\n");
    printf("  Antes:  p=%d, q=%d\n", p, q);
    swap(&p, &q);
    printf("  Depois: p=%d, q=%d\n\n", p, q);

    // Par 3
    int m = 0, n = 0;
    printf("Par 3: m=0, n=0\n");
    printf("  Antes:  m=%d, n=%d\n", m, n);
    swap(&m, &n);
    printf("  Depois: m=%d, n=%d (valores iguais, nada muda)\n", m, n);

    return 0;
}
```

### Exercício 8 — Trace de Ponteiros

```
TRACE 1: a=5,   b=10,  *p1=5,   *p2=10   (p1->a, p2->b)
TRACE 2: a=20,  b=10,  *p1=20,  *p2=10   (*p1=20 modifica a)
TRACE 3: a=20,  b=23,  *p1=20,  *p2=23   (*p2 = *p1+3 = 20+3 = 23, modifica b)
TRACE 4: a=20,  b=23,  *p1=23,  *p2=23   (p1=p2, agora p1 tambem aponta para b)
TRACE 5: a=20,  b=100, *p1=100, *p2=100  (*p1=100 modifica b, pois p1 aponta para b)

Saida: a=20, b=100, *p1=100, *p2=100
```

O ponto-chave é o TRACE 4: quando fazemos `p1 = p2`, não estamos copiando o valor de `b` para `a`. Estamos fazendo `p1` apontar para o mesmo lugar que `p2` (para `b`). A variável `a` fica "órfã" — nenhum ponteiro aponta mais para ela, mas ela continua existindo com o valor 20.

### Exercício 9 — Detector de Memory Leak

**Leak 1 — funcao_a:**
- Linha: fim da função (falta `free(p)`)
- Bytes vazados: 4 (sizeof(int))
- Correção: adicionar `free(p);` antes do fim da função

**Leak 2 — funcao_b:**
- Linha: `p = (int*)malloc(5 * sizeof(int));` — o ponteiro `p` é reatribuído sem liberar a memória anterior
- Bytes vazados: 40 (10 * sizeof(int))
- Correção: adicionar `free(p);` antes do segundo `malloc`

**Leak 3 — funcao_c:**
- Linha: `return;` dentro do `if` — retorna sem chamar `free(p)`
- Bytes vazados: 4 (sizeof(int)) — apenas quando `condição` é verdadeira
- Correção: adicionar `free(p);` antes do `return` dentro do `if`

Total de leaks por execução: 4 + 40 + 4 = 48 bytes vazados.

---

[← Voltar ao conteúdo: Ponteiros](cap07-mod04-ponteiros-conteudo.md) · [Próximo: Arrays →](cap07-mod05-arrays-conteudo.md)
