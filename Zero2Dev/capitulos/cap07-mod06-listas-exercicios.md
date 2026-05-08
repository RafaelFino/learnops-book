# 7.6 — Exercícios: Listas Encadeadas

[← Voltar ao conteúdo: Listas Encadeadas](cap07-mod06-listas-conteudo.md)

---

## Instruções Gerais

Todos os exercícios devem ser implementados em C. Compile com `gcc -Wall` para ver avisos do compilador. Use `valgrind ./programa` (se disponível) para verificar memory leaks.

Para cada exercício:
1. Crie um arquivo `.c` separado
2. Compile e teste
3. Verifique que toda memória alocada com `malloc` é liberada com `free`

Use esta estrutura base em todos os exercícios:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) {
        printf("Erro: memoria insuficiente!\n");
        return NULL;
    }
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

void imprimir_lista(No *head) {
    No *atual = head;
    printf("Lista: ");
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}
```

---

## Exercício 1 — Construir e Percorrer (Nível: Básico)

Crie uma lista encadeada inserindo os valores 10, 20, 30, 40 e 50 no final. Depois, implemente uma função que percorre a lista e calcula:
- A soma de todos os elementos
- O maior valor
- O menor valor

Saída esperada:
```
Lista: 10 -> 20 -> 30 -> 40 -> 50 -> NULL
Soma: 150
Maior: 50
Menor: 10
```

Dica: percorra a lista com `while (atual != NULL)` e acumule os valores, assim como fizemos com arrays no módulo 7.5.

<details>
<summary>Resposta comentada</summary>

```c
// ex01_percorrer.c — Construir lista e calcular estatisticas
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

void inserir_final(No **head, int valor) {
    No *novo = criar_no(valor);
    if (novo == NULL) return;
    if (*head == NULL) {
        *head = novo;
        return;
    }
    No *atual = *head;
    while (atual->next != NULL) atual = atual->next;
    atual->next = novo;
}

void imprimir_lista(No *head) {
    No *atual = head;
    printf("Lista: ");
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}

// Calcular soma percorrendo a lista
int soma_lista(No *head) {
    int soma = 0;
    No *atual = head;
    while (atual != NULL) {
        soma += atual->dado;  // acumula o valor de cada no
        atual = atual->next;
    }
    return soma;
}

// Encontrar o maior valor
int maior_lista(No *head) {
    if (head == NULL) return 0;
    int maior = head->dado;  // comeca com o primeiro
    No *atual = head->next;
    while (atual != NULL) {
        if (atual->dado > maior) maior = atual->dado;
        atual = atual->next;
    }
    return maior;
}

// Encontrar o menor valor
int menor_lista(No *head) {
    if (head == NULL) return 0;
    int menor = head->dado;
    No *atual = head->next;
    while (atual != NULL) {
        if (atual->dado < menor) menor = atual->dado;
        atual = atual->next;
    }
    return menor;
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

int main() {
    No *lista = NULL;

    inserir_final(&lista, 10);
    inserir_final(&lista, 20);
    inserir_final(&lista, 30);
    inserir_final(&lista, 40);
    inserir_final(&lista, 50);

    imprimir_lista(lista);
    printf("Soma: %d\n", soma_lista(lista));
    printf("Maior: %d\n", maior_lista(lista));
    printf("Menor: %d\n", menor_lista(lista));

    liberar_lista(&lista);
    return 0;
}
```

O padrão é o mesmo dos arrays: percorrer todos os elementos acumulando valores. A diferença é que em vez de `for (i = 0; i < n; i++)` com `arr[i]`, usamos `while (atual != NULL)` com `atual->dado` e `atual = atual->next`.

</details>

---

## Exercício 2 — Inverter a Lista (Nível: Intermediário)

Escreva uma função `void inverter(No **head)` que inverte a ordem dos elementos. Se a lista é 10 → 20 → 30 → 40, após inverter deve ser 40 → 30 → 20 → 10.

Saída esperada:
```
Original:  10 -> 20 -> 30 -> 40 -> NULL
Invertida: 40 -> 30 -> 20 -> 10 -> NULL
```

Dica: use três ponteiros — `anterior`, `atual` e `próximo`. Para cada nó, faça `atual->next` apontar para `anterior`. Avance os três ponteiros. No final, `head` aponta para `anterior` (que é o último nó original).

<details>
<summary>Resposta comentada</summary>

```c
// ex02_inverter.c — Inverter uma lista encadeada
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

void inserir_final(No **head, int valor) {
    No *novo = criar_no(valor);
    if (novo == NULL) return;
    if (*head == NULL) { *head = novo; return; }
    No *atual = *head;
    while (atual->next != NULL) atual = atual->next;
    atual->next = novo;
}

void imprimir_lista(No *head) {
    No *atual = head;
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}

// Inverter a lista mudando a direcao dos ponteiros
void inverter(No **head) {
    No *anterior = NULL;   // no anterior (comeca sem nenhum)
    No *atual = *head;     // no atual (comeca no primeiro)
    No *proximo = NULL;    // proximo no (salvo antes de mudar)

    while (atual != NULL) {
        proximo = atual->next;    // 1. salvar o proximo
        atual->next = anterior;   // 2. inverter o ponteiro
        anterior = atual;         // 3. avancar anterior
        atual = proximo;          // 4. avancar atual
    }
    *head = anterior;  // o ultimo no visitado e o novo head
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

int main() {
    No *lista = NULL;
    inserir_final(&lista, 10);
    inserir_final(&lista, 20);
    inserir_final(&lista, 30);
    inserir_final(&lista, 40);

    printf("Original:  ");
    imprimir_lista(lista);

    inverter(&lista);

    printf("Invertida: ");
    imprimir_lista(lista);

    liberar_lista(&lista);
    return 0;
}
```

A inversão funciona assim: para cada nó, em vez de `next` apontar para o próximo, fazemos apontar para o anterior. Precisamos salvar o `próximo` antes de mudar o ponteiro, senão perdemos a referência ao resto da lista. No final, o último nó visitado (`anterior`) se torna o novo `head`.

</details>

---

## Exercício 3 — Encontrar o Meio (Nível: Intermediário)

Escreva uma função que encontra o elemento do meio de uma lista encadeada usando a técnica dos dois ponteiros (tartaruga e lebre). O ponteiro `lento` avança 1 nó por vez, o `rápido` avança 2 nós por vez. Quando o rápido chegar ao final, o lento estará no meio.

Teste com listas de tamanho ímpar e par:
```
Lista: 10 -> 20 -> 30 -> 40 -> 50 -> NULL
Meio: 30

Lista: 10 -> 20 -> 30 -> 40 -> NULL
Meio: 30
```

Dica: o loop continua enquanto `rápido != NULL && rápido->next != NULL`.

<details>
<summary>Resposta comentada</summary>

```c
// ex03_meio.c — Encontrar o elemento do meio
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

void inserir_final(No **head, int valor) {
    No *novo = criar_no(valor);
    if (novo == NULL) return;
    if (*head == NULL) { *head = novo; return; }
    No *atual = *head;
    while (atual->next != NULL) atual = atual->next;
    atual->next = novo;
}

void imprimir_lista(No *head) {
    No *atual = head;
    printf("Lista: ");
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}

// Encontrar o meio usando dois ponteiros
int encontrar_meio(No *head) {
    if (head == NULL) {
        printf("Lista vazia!\n");
        return -1;
    }

    No *lento = head;   // avanca 1 no por vez (tartaruga)
    No *rapido = head;  // avanca 2 nos por vez (lebre)

    // Quando rapido chegar ao fim, lento esta no meio
    while (rapido != NULL && rapido->next != NULL) {
        lento = lento->next;          // 1 passo
        rapido = rapido->next->next;  // 2 passos
    }

    return lento->dado;
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

int main() {
    // Teste com lista impar (5 elementos)
    No *lista1 = NULL;
    inserir_final(&lista1, 10);
    inserir_final(&lista1, 20);
    inserir_final(&lista1, 30);
    inserir_final(&lista1, 40);
    inserir_final(&lista1, 50);
    imprimir_lista(lista1);
    printf("Meio: %d\n\n", encontrar_meio(lista1));
    liberar_lista(&lista1);

    // Teste com lista par (4 elementos)
    No *lista2 = NULL;
    inserir_final(&lista2, 10);
    inserir_final(&lista2, 20);
    inserir_final(&lista2, 30);
    inserir_final(&lista2, 40);
    imprimir_lista(lista2);
    printf("Meio: %d\n", encontrar_meio(lista2));
    liberar_lista(&lista2);

    return 0;
}
```

A técnica funciona porque o ponteiro rápido percorre a lista 2x mais rápido. Quando ele chega ao final (percorreu N nós), o lento percorreu N/2 — exatamente o meio. Para lista ímpar (5 elementos), o meio é o 3o. Para lista par (4 elementos), o meio é o 2o ou 3o dependendo da convenção — nossa implementação retorna o segundo dos dois centrais.

</details>

---

## Exercício 4 — Remover Duplicatas (Nível: Intermediário)

Escreva uma função que remove todos os valores duplicados de uma lista encadeada, mantendo apenas a primeira ocorrência de cada valor.

Saída esperada:
```
Original:   10 -> 20 -> 10 -> 30 -> 20 -> 40 -> 10 -> NULL
Sem duplic: 10 -> 20 -> 30 -> 40 -> NULL
```

Dica: para cada nó, percorra o restante da lista removendo nós com o mesmo valor. Isso é O(n²), mas é a abordagem mais simples sem usar estruturas auxiliares.

<details>
<summary>Resposta comentada</summary>

```c
// ex04_duplicatas.c — Remover valores duplicados
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

void inserir_final(No **head, int valor) {
    No *novo = criar_no(valor);
    if (novo == NULL) return;
    if (*head == NULL) { *head = novo; return; }
    No *atual = *head;
    while (atual->next != NULL) atual = atual->next;
    atual->next = novo;
}

void imprimir_lista(No *head) {
    No *atual = head;
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}

// Remover duplicatas — para cada no, remover ocorrencias seguintes
void remover_duplicatas(No *head) {
    No *atual = head;

    while (atual != NULL) {
        // Para cada no, percorrer o restante removendo duplicatas
        No *verificador = atual;
        while (verificador->next != NULL) {
            if (verificador->next->dado == atual->dado) {
                // Encontrou duplicata — remover
                No *duplicata = verificador->next;
                verificador->next = duplicata->next;
                free(duplicata);  // liberar memoria do no removido
            } else {
                verificador = verificador->next;
            }
        }
        atual = atual->next;
    }
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

int main() {
    No *lista = NULL;
    inserir_final(&lista, 10);
    inserir_final(&lista, 20);
    inserir_final(&lista, 10);
    inserir_final(&lista, 30);
    inserir_final(&lista, 20);
    inserir_final(&lista, 40);
    inserir_final(&lista, 10);

    printf("Original:   ");
    imprimir_lista(lista);

    remover_duplicatas(lista);

    printf("Sem duplic: ");
    imprimir_lista(lista);

    liberar_lista(&lista);
    return 0;
}
```

Para cada nó, percorremos o restante da lista procurando nós com o mesmo valor. Quando encontramos, removemos (ajustando o ponteiro do anterior e liberando a memória). Note que quando removemos um nó, NÃO avançamos `verificador` — porque o próximo nó mudou e precisa ser verificado também.

</details>

---

## Exercício 5 — Detectar Ciclo (Nível: Avançado)

Escreva uma função `int tem_ciclo(No *head)` que detecta se uma lista encadeada tem um ciclo (o último nó aponta para algum nó anterior em vez de NULL). Use a técnica da tartaruga e lebre: se os dois ponteiros se encontrarem, há um ciclo.

```c
// Criar um ciclo para teste:
// 10 -> 20 -> 30 -> 40 -> 20 (volta para o no com 20)
```

Saída esperada:
```
Lista normal: sem ciclo
Lista com ciclo: ciclo detectado!
```

Dica: se `lento == rápido` em algum momento (e ambos não são NULL), há um ciclo. Se `rápido` chegar a NULL, não há ciclo. Cuidado: não tente imprimir uma lista com ciclo — será um loop infinito.

<details>
<summary>Resposta comentada</summary>

```c
// ex05_ciclo.c — Detectar ciclo em lista encadeada
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

// Detectar ciclo usando tartaruga e lebre (Floyd)
int tem_ciclo(No *head) {
    if (head == NULL) return 0;  // lista vazia, sem ciclo

    No *lento = head;   // tartaruga — 1 passo
    No *rapido = head;  // lebre — 2 passos

    while (rapido != NULL && rapido->next != NULL) {
        lento = lento->next;
        rapido = rapido->next->next;

        if (lento == rapido) {
            return 1;  // se encontraram — ha ciclo!
        }
    }

    return 0;  // rapido chegou ao fim — sem ciclo
}

int main() {
    // Lista normal (sem ciclo)
    No *normal = criar_no(10);
    normal->next = criar_no(20);
    normal->next->next = criar_no(30);

    printf("Lista normal: %s\n",
           tem_ciclo(normal) ? "ciclo detectado!" : "sem ciclo");

    // Lista com ciclo: 10 -> 20 -> 30 -> 40 -> volta para 20
    No *ciclica = criar_no(10);
    No *no20 = criar_no(20);
    ciclica->next = no20;
    no20->next = criar_no(30);
    no20->next->next = criar_no(40);
    no20->next->next->next = no20;  // 40 aponta para 20 — ciclo!

    printf("Lista com ciclo: %s\n",
           tem_ciclo(ciclica) ? "ciclo detectado!" : "sem ciclo");

    // Liberar lista normal
    free(normal->next->next);
    free(normal->next);
    free(normal);

    // Liberar lista ciclica (quebrar o ciclo primeiro!)
    no20->next->next->next = NULL;  // 40->next = NULL
    No *atual = ciclica;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }

    return 0;
}
```

O algoritmo de Floyd funciona porque, se há um ciclo, o ponteiro rápido eventualmente "alcança" o lento dentro do ciclo — como dois corredores em uma pista circular, o mais rápido sempre alcança o mais lento. Se não há ciclo, o rápido chega ao final (NULL) e o loop termina.

Note que para liberar uma lista com ciclo, primeiro precisamos quebrar o ciclo (definir o ponteiro que causa o ciclo como NULL), senão o `free` entra em loop infinito.

</details>

---

## Exercício 6 — Mesclar Duas Listas Ordenadas (Nível: Avançado)

Escreva uma função que recebe duas listas encadeadas ordenadas e retorna uma nova lista ordenada contendo todos os elementos das duas.

Saída esperada:
```
Lista 1: 10 -> 30 -> 50 -> NULL
Lista 2: 20 -> 40 -> 60 -> NULL
Mesclada: 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> NULL
```

Dica: compare os primeiros elementos de cada lista. O menor vai para a lista resultado. Avance o ponteiro da lista de onde veio o menor. Repita até uma das listas acabar, depois anexe o restante da outra.

<details>
<summary>Resposta comentada</summary>

```c
// ex06_mesclar.c — Mesclar duas listas ordenadas
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int dado;
    struct No *next;
} No;

No* criar_no(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    novo->dado = valor;
    novo->next = NULL;
    return novo;
}

void inserir_final(No **head, int valor) {
    No *novo = criar_no(valor);
    if (novo == NULL) return;
    if (*head == NULL) { *head = novo; return; }
    No *atual = *head;
    while (atual->next != NULL) atual = atual->next;
    atual->next = novo;
}

void imprimir_lista(No *head) {
    No *atual = head;
    while (atual != NULL) {
        printf("%d", atual->dado);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}

// Mesclar duas listas ordenadas em uma nova lista ordenada
No* mesclar(No *lista1, No *lista2) {
    No *resultado = NULL;
    No *p1 = lista1;  // ponteiro para percorrer lista 1
    No *p2 = lista2;  // ponteiro para percorrer lista 2

    // Enquanto ambas as listas tiverem elementos
    while (p1 != NULL && p2 != NULL) {
        if (p1->dado <= p2->dado) {
            inserir_final(&resultado, p1->dado);
            p1 = p1->next;
        } else {
            inserir_final(&resultado, p2->dado);
            p2 = p2->next;
        }
    }

    // Anexar o restante da lista que ainda tem elementos
    while (p1 != NULL) {
        inserir_final(&resultado, p1->dado);
        p1 = p1->next;
    }
    while (p2 != NULL) {
        inserir_final(&resultado, p2->dado);
        p2 = p2->next;
    }

    return resultado;
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

int main() {
    No *lista1 = NULL;
    inserir_final(&lista1, 10);
    inserir_final(&lista1, 30);
    inserir_final(&lista1, 50);

    No *lista2 = NULL;
    inserir_final(&lista2, 20);
    inserir_final(&lista2, 40);
    inserir_final(&lista2, 60);

    printf("Lista 1: ");
    imprimir_lista(lista1);
    printf("Lista 2: ");
    imprimir_lista(lista2);

    No *mesclada = mesclar(lista1, lista2);
    printf("Mesclada: ");
    imprimir_lista(mesclada);

    liberar_lista(&lista1);
    liberar_lista(&lista2);
    liberar_lista(&mesclada);
    return 0;
}
```

A mesclagem compara os primeiros elementos de cada lista e sempre pega o menor. Como ambas as listas já estão ordenadas, o resultado também fica ordenado. Esse é o mesmo princípio do Merge Sort — um dos algoritmos de ordenação mais eficientes, que veremos no módulo 7.10.

</details>

---

## Exercício 7 — Lista de Strings (Nível: Intermediário)

Modifique a estrutura do nó para guardar uma string (nome) em vez de um inteiro. Implemente inserção no final, impressão e busca por nome.

Saída esperada:
```
Nomes: Maria -> Carlos -> Ana -> Fino -> NULL
Buscando 'Ana': encontrado!
Buscando 'Pedro': nao encontrado
```

Dica: use `char nome[50]` no nó, `strncpy` para copiar e `strcmp` para comparar.

<details>
<summary>Resposta comentada</summary>

```c
// ex07_strings.c — Lista encadeada de strings
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct No {
    char nome[50];      // dado agora e uma string
    struct No *next;
} No;

No* criar_no(const char *nome) {
    No *novo = (No*)malloc(sizeof(No));
    if (novo == NULL) return NULL;
    strncpy(novo->nome, nome, 49);  // copiar ate 49 chars
    novo->nome[49] = '\0';          // garantir terminador
    novo->next = NULL;
    return novo;
}

void inserir_final(No **head, const char *nome) {
    No *novo = criar_no(nome);
    if (novo == NULL) return;
    if (*head == NULL) { *head = novo; return; }
    No *atual = *head;
    while (atual->next != NULL) atual = atual->next;
    atual->next = novo;
}

void imprimir_lista(No *head) {
    No *atual = head;
    printf("Nomes: ");
    while (atual != NULL) {
        printf("%s", atual->nome);
        if (atual->next != NULL) printf(" -> ");
        atual = atual->next;
    }
    printf(" -> NULL\n");
}

// Buscar por nome — retorna 1 se encontrou, 0 se nao
int buscar_nome(No *head, const char *nome) {
    No *atual = head;
    while (atual != NULL) {
        if (strcmp(atual->nome, nome) == 0) return 1;
        atual = atual->next;
    }
    return 0;
}

void liberar_lista(No **head) {
    No *atual = *head;
    while (atual != NULL) {
        No *proximo = atual->next;
        free(atual);
        atual = proximo;
    }
    *head = NULL;
}

int main() {
    No *lista = NULL;
    inserir_final(&lista, "Maria");
    inserir_final(&lista, "Carlos");
    inserir_final(&lista, "Ana");
    inserir_final(&lista, "Fino");

    imprimir_lista(lista);

    printf("Buscando 'Ana': %s\n",
           buscar_nome(lista, "Ana") ? "encontrado!" : "nao encontrado");
    printf("Buscando 'Pedro': %s\n",
           buscar_nome(lista, "Pedro") ? "encontrado!" : "nao encontrado");

    liberar_lista(&lista);
    return 0;
}
```

A estrutura é a mesma — a única diferença é o tipo do dado. Em vez de `int dado`, usamos `char nome[50]`. Em vez de `=` para atribuir, usamos `strncpy`. Em vez de `==` para comparar, usamos `strcmp`. O restante (ponteiros, inserção, percorrimento) é idêntico.

</details>

---

## Desafio Extra — Implementar uma Lista com Menu Interativo

Crie um programa com menu interativo que permite ao usuário:
1. Inserir no início
2. Inserir no final
3. Remover por valor
4. Buscar por valor
5. Imprimir a lista
6. Contar elementos
7. Inverter a lista
0. Sair

Use `scanf` para ler a opção e o valor. Libere toda a memória ao sair.

Este exercício consolida todas as operações do módulo em um programa único e interativo. Não há resposta pronta — combine as funções que você já implementou nos exercícios anteriores.

---

[← Voltar ao conteúdo: Listas Encadeadas](cap07-mod06-listas-conteudo.md)
