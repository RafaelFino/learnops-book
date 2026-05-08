# 7.7 — Exercícios: Filas (FIFO)

[← Voltar ao conteúdo: Filas](cap07-mod07-filas-conteudo.md)

---

## Sobre os Exercícios

Estes exercícios cobrem os conceitos de filas FIFO apresentados no módulo 7.7. Eles estão organizados em ordem crescente de dificuldade: os primeiros reforçam os conceitos básicos, e os últimos desafiam você a aplicar filas em cenários mais complexos.

Para todos os exercícios com código, compile e execute para verificar se a saída está correta:

```bash
gcc -o exercicio exercicio.c
./exercicio
```

---

## Exercício 1: Conceitos Fundamentais

Responda sem consultar o material:

a) O que significa FIFO? Dê um exemplo do dia a dia.

b) Quais são as duas operações fundamentais de uma fila? Qual a complexidade de cada uma?

c) Por que a fila mantém dois ponteiros (front e rear) em vez de apenas um?

d) Qual a diferença entre `peek` e `dequeue`?

e) Em qual situação uma fila com lista encadeada é melhor que uma fila com array circular? E o contrário?

---

## Exercício 2: Rastreando Operações no Papel

Dada a seguinte sequência de operações em uma fila inicialmente vazia, desenhe o estado da fila (front e rear) após cada operação e indique o valor retornado quando aplicável:

```
1. enqueue(5)
2. enqueue(10)
3. enqueue(15)
4. dequeue()       → retorna ?
5. enqueue(20)
6. dequeue()       → retorna ?
7. dequeue()       → retorna ?
8. enqueue(25)
9. enqueue(30)
10. dequeue()      → retorna ?
11. dequeue()      → retorna ?
12. dequeue()      → retorna ?
13. dequeue()      → retorna ? (o que acontece?)
```

Dica: desenhe a fila como uma sequência de caixas com setas. Marque onde está o front e o rear. A cada operação, atualize o desenho.

**Respostas esperadas:**

| Passo | Operação | Retorno | Estado da fila (front ... rear) |
|-------|----------|---------|-------------------------------|
| 1 | enqueue(5) | — | [5] |
| 2 | enqueue(10) | — | [5] → [10] |
| 3 | enqueue(15) | — | [5] → [10] → [15] |
| 4 | dequeue() | 5 | [10] → [15] |
| 5 | enqueue(20) | — | [10] → [15] → [20] |
| 6 | dequeue() | 10 | [15] → [20] |
| 7 | dequeue() | 15 | [20] |
| 8 | enqueue(25) | — | [20] → [25] |
| 9 | enqueue(30) | — | [20] → [25] → [30] |
| 10 | dequeue() | 20 | [25] → [30] |
| 11 | dequeue() | 25 | [30] |
| 12 | dequeue() | 30 | (vazia) |
| 13 | dequeue() | erro | Fila vazia — não ha o que remover |

---

## Exercício 3: Implementar Fila Básica do Zero

Implemente uma fila de inteiros com lista encadeada, sem consultar o módulo. Escreva todas as funções:

- `criar_fila()` — cria e retorna uma fila vazia
- `enqueue(fila, valor)` — insere no final
- `dequeue(fila)` — remove do início e retorna o valor
- `peek(fila)` — retorna o primeiro sem remover
- `esta_vazia(fila)` — retorna 1 se vazia, 0 se não
- `imprimir_fila(fila)` — mostra todos os elementos
- `liberar_fila(fila)` — libera toda a memória

Teste com este `main`:

```c
int main() {
    Fila *fila = criar_fila();

    enqueue(fila, 100);
    enqueue(fila, 200);
    enqueue(fila, 300);
    imprimir_fila(fila);  // FRONT -> [100] -> [200] -> [300] <- REAR

    printf("Peek: %d\n", peek(fila));      // 100
    printf("Dequeue: %d\n", dequeue(fila)); // 100
    printf("Dequeue: %d\n", dequeue(fila)); // 200
    imprimir_fila(fila);  // FRONT -> [300] <- REAR

    enqueue(fila, 400);
    enqueue(fila, 500);
    imprimir_fila(fila);  // FRONT -> [300] -> [400] -> [500] <- REAR

    // Esvaziar
    while (!esta_vazia(fila)) {
        printf("Dequeue: %d\n", dequeue(fila));
    }
    imprimir_fila(fila);  // (vazia)

    dequeue(fila);  // Erro: fila vazia!

    liberar_fila(fila);
    return 0;
}
```

Saída esperada:
```
Fila: FRONT -> [100] -> [200] -> [300] <- REAR
Peek: 100
Dequeue: 100
Dequeue: 200
Fila: FRONT -> [300] <- REAR
Fila: FRONT -> [300] -> [400] -> [500] <- REAR
Dequeue: 300
Dequeue: 400
Dequeue: 500
Fila: (vazia)
Erro: fila vazia!
```

Dica: lembre-se dos dois casos especiais — enqueue em fila vazia (front e rear apontam para o mesmo nó) e dequeue que esvazia a fila (rear precisa ser atualizado para NULL).

---

## Exercício 4: Encontrar o Bug

Cada trecho de código abaixo tem um bug relacionado a filas. Identifique o problema, explique a consequência e corrija.

### Bug A:

```c
void enqueue(Fila *fila, int valor) {
    No *novo = (No*)malloc(sizeof(No));
    novo->dado = valor;
    novo->next = NULL;
    fila->rear->next = novo;
    fila->rear = novo;
    fila->tamanho++;
}
```

Pergunta: o que acontece se a fila estiver vazia quando chamamos `enqueue`?

### Bug B:

```c
int dequeue(Fila *fila) {
    No *temp = fila->front;
    int valor = temp->dado;
    fila->front = fila->front->next;
    free(temp);
    fila->tamanho--;
    return valor;
}
```

Pergunta: o que acontece quando removemos o último elemento da fila? E se a fila já estiver vazia?

### Bug C:

```c
void liberar_fila(Fila *fila) {
    No *atual = fila->front;
    while (atual != NULL) {
        free(atual);
        atual = atual->next;
    }
    free(fila);
}
```

Pergunta: por que esse código causa comportamento indefinido?

### Respostas Comentadas

**Bug A:** Quando a fila está vazia, `fila->rear` é NULL. Acessar `fila->rear->next` causa segmentation fault. A correção é verificar se a fila está vazia antes:

```c
void enqueue(Fila *fila, int valor) {
    No *novo = (No*)malloc(sizeof(No));
    novo->dado = valor;
    novo->next = NULL;

    if (fila->rear == NULL) {
        // Fila vazia — novo e o primeiro e o ultimo
        fila->front = novo;
        fila->rear = novo;
    } else {
        fila->rear->next = novo;
        fila->rear = novo;
    }
    fila->tamanho++;
}
```

**Bug B:** Dois problemas. Primeiro: quando removemos o último elemento, `fila->front` fica NULL, mas `fila->rear` continua apontando para o nó que acabamos de liberar (dangling pointer). O próximo `enqueue` vai acessar `rear->next` e causar crash. Segundo: se a fila já estiver vazia, `fila->front` é NULL e `temp->dado` causa segfault. Correção:

```c
int dequeue(Fila *fila) {
    if (fila->front == NULL) {
        printf("Erro: fila vazia!\n");
        return -1;
    }

    No *temp = fila->front;
    int valor = temp->dado;
    fila->front = fila->front->next;

    if (fila->front == NULL) {
        fila->rear = NULL;  // Fila ficou vazia
    }

    free(temp);
    fila->tamanho--;
    return valor;
}
```

**Bug C:** Após `free(atual)`, a memória do nó é liberada. Acessar `atual->next` na linha seguinte é "use after free" — o dado pode ter sido sobrescrito. A correção é salvar o próximo antes de liberar:

```c
void liberar_fila(Fila *fila) {
    No *atual = fila->front;
    while (atual != NULL) {
        No *proximo = atual->next;  // salvar ANTES de liberar
        free(atual);
        atual = proximo;
    }
    free(fila);
}
```

---

## Exercício 5: Fila de Strings

Implemente uma fila que armazena nomes (strings) em vez de inteiros. A struct do nó deve ter um campo `char nome[50]` em vez de `int dado`.

Implemente:
- `enqueue_str(fila, nome)` — insere um nome no final
- `dequeue_str(fila, resultado)` — remove do início e copia o nome para `resultado`
- `imprimir_fila_str(fila)` — mostra todos os nomes

Teste com:

```c
int main() {
    // Crie a fila aqui

    enqueue_str(fila, "Alice");
    enqueue_str(fila, "Bob");
    enqueue_str(fila, "Carol");
    enqueue_str(fila, "David");
    imprimir_fila_str(fila);

    char nome[50];
    dequeue_str(fila, nome);
    printf("Atendido: %s\n", nome);  // Alice

    dequeue_str(fila, nome);
    printf("Atendido: %s\n", nome);  // Bob

    enqueue_str(fila, "Eva");
    imprimir_fila_str(fila);

    // Liberar memoria
    return 0;
}
```

Saída esperada:
```
Fila: [Alice] -> [Bob] -> [Carol] -> [David]
Atendido: Alice
Atendido: Bob
Fila: [Carol] -> [David] -> [Eva]
```

Dica: use `strncpy(destino, origem, 49)` para copiar strings com segurança. Lembre-se de colocar o terminador `'\0'` no final.

---

## Exercício 6: Fila Circular com Array

Implemente uma fila circular com array de tamanho 6. Use a operação módulo (`%`) para fazer os índices voltarem ao início quando passam do final.

Sua struct deve ter:

```c
#define MAX 6

typedef struct FilaCircular {
    int dados[MAX];
    int front;
    int rear;
    int tamanho;
} FilaCircular;
```

Implemente:
- `inicializar(fila)` — front=0, rear=0, tamanho=0
- `enqueue_circ(fila, valor)` — insere no rear, avança rear com módulo
- `dequeue_circ(fila)` — remove do front, avança front com módulo
- `imprimir_circ(fila)` — mostra os elementos na ordem correta

Teste com esta sequência:

```c
int main() {
    FilaCircular fila;
    inicializar(&fila);

    // Encher a fila
    for (int i = 1; i <= 6; i++) {
        enqueue_circ(&fila, i * 10);
    }
    imprimir_circ(&fila);  // [10] [20] [30] [40] [50] [60]

    // Tentar inserir em fila cheia
    enqueue_circ(&fila, 70);  // Erro: fila cheia!

    // Remover 3 elementos
    printf("Removido: %d\n", dequeue_circ(&fila));  // 10
    printf("Removido: %d\n", dequeue_circ(&fila));  // 20
    printf("Removido: %d\n", dequeue_circ(&fila));  // 30

    // Inserir mais 3 (rear volta ao inicio do array)
    enqueue_circ(&fila, 70);
    enqueue_circ(&fila, 80);
    enqueue_circ(&fila, 90);
    imprimir_circ(&fila);  // [40] [50] [60] [70] [80] [90]

    return 0;
}
```

Saída esperada:
```
Fila: [10] -> [20] -> [30] -> [40] -> [50] -> [60] (6/6)
Erro: fila cheia!
Removido: 10
Removido: 20
Removido: 30
Fila: [40] -> [50] -> [60] -> [70] -> [80] -> [90] (6/6)
```

Dica: o truque está em `(índice + 1) % MAX`. Quando `índice` é 5 (último do array de tamanho 6), `(5 + 1) % 6 = 0` — volta para o início.

---

## Exercício 7: Contar Elementos e Somar Valores

Adicione duas funções à fila de inteiros com lista encadeada:

- `contar(fila)` — retorna quantos elementos tem na fila (sem usar o campo `tamanho`, percorrendo os nós)
- `somar(fila)` — retorna a soma de todos os valores na fila

Teste:

```c
int main() {
    Fila *fila = criar_fila();

    enqueue(fila, 10);
    enqueue(fila, 20);
    enqueue(fila, 30);
    enqueue(fila, 40);

    printf("Quantidade: %d\n", contar(fila));  // 4
    printf("Soma: %d\n", somar(fila));          // 100

    dequeue(fila);  // remove 10
    dequeue(fila);  // remove 20

    printf("Quantidade: %d\n", contar(fila));  // 2
    printf("Soma: %d\n", somar(fila));          // 70

    liberar_fila(fila);
    return 0;
}
```

Dica: percorra a fila do `front` ao final usando `atual = atual->next`, acumulando a contagem ou a soma. Não modifique a fila — apenas leia os valores.

---

## Exercício 8: Inverter uma Fila

Escreva uma função `void inverter_fila(Fila *fila)` que inverte a ordem dos elementos. Se a fila tem [10, 20, 30, 40], após inverter deve ter [40, 30, 20, 10].

Restrição: você pode usar uma estrutura auxiliar (como um array ou uma pilha — que é basicamente um array onde você insere e remove do final).

Estratégia sugerida:
1. Faça dequeue de todos os elementos e guarde em um array
2. Faça enqueue de todos os elementos na ordem inversa (do último para o primeiro)

Teste:

```c
int main() {
    Fila *fila = criar_fila();

    enqueue(fila, 10);
    enqueue(fila, 20);
    enqueue(fila, 30);
    enqueue(fila, 40);

    printf("Antes: ");
    imprimir_fila(fila);  // FRONT -> [10] -> [20] -> [30] -> [40] <- REAR

    inverter_fila(fila);

    printf("Depois: ");
    imprimir_fila(fila);  // FRONT -> [40] -> [30] -> [20] -> [10] <- REAR

    liberar_fila(fila);
    return 0;
}
```

Dica: defina um array temporário com tamanho suficiente (ex: `int temp[1000]`). Faça dequeue em loop guardando no array. Depois faça enqueue do array de trás para frente.

---

## Exercício 9: Simulador de Fila de Supermercado

Crie um simulador de supermercado com 2 caixas e uma fila única de clientes. Cada cliente tem um nome e uma quantidade de itens.

Structs sugeridas:

```c
typedef struct Cliente {
    char nome[50];
    int itens;
    struct Cliente *next;
} Cliente;

typedef struct FilaSupermercado {
    Cliente *front;
    Cliente *rear;
    int tamanho;
} FilaSupermercado;

typedef struct Caixa {
    int id;
    char cliente_atual[50];
    int tempo_restante;     // itens restantes para processar
    int clientes_atendidos;
} Caixa;
```

Simule a seguinte sequência:

1. Chegam: Ana (3 itens), Bruno (5 itens), Carol (2 itens), David (8 itens), Eva (1 item)
2. A cada "tick" (unidade de tempo), cada caixa processa 1 item do cliente atual
3. Quando um caixa termina (tempo_restante chega a 0), ele pega o próximo da fila
4. Quando a fila esvazia e os caixas terminam, a simulação acaba

A cada tick, imprima:
- O estado de cada caixa (quem está atendendo, quantos itens faltam)
- O estado da fila (quem está esperando)

No final, imprima:
- Quantos clientes cada caixa atendeu
- Tempo total da simulação

Saída esperada (resumida):
```
=== Tick 1 ===
  Caixa 1: Ana (2 itens restantes)
  Caixa 2: Bruno (4 itens restantes)
  Fila: Carol(2) -> David(8) -> Eva(1)

=== Tick 2 ===
  Caixa 1: Ana (1 item restante)
  Caixa 2: Bruno (3 itens restantes)
  Fila: Carol(2) -> David(8) -> Eva(1)

=== Tick 3 ===
  Caixa 1: Ana concluido! Proximo: Carol
  ...
```

Dica: use um loop `while` que continua enquanto a fila não estiver vazia OU algum caixa estiver atendendo. A cada iteração, decremente o `tempo_restante` de cada caixa. Quando chegar a 0, faça dequeue do próximo cliente.

---

## Exercício 10: Intercalar Duas Filas

Escreva uma função `Fila* intercalar(Fila *fila1, Fila *fila2)` que cria uma nova fila intercalando os elementos das duas filas de entrada. Se uma fila for maior que a outra, os elementos restantes são adicionados no final.

Exemplo:
- Fila 1: [1, 3, 5, 7]
- Fila 2: [2, 4, 6]
- Resultado: [1, 2, 3, 4, 5, 6, 7]

Teste:

```c
int main() {
    Fila *fila1 = criar_fila();
    Fila *fila2 = criar_fila();

    enqueue(fila1, 1);
    enqueue(fila1, 3);
    enqueue(fila1, 5);
    enqueue(fila1, 7);

    enqueue(fila2, 2);
    enqueue(fila2, 4);
    enqueue(fila2, 6);

    printf("Fila 1: ");
    imprimir_fila(fila1);

    printf("Fila 2: ");
    imprimir_fila(fila2);

    Fila *resultado = intercalar(fila1, fila2);
    printf("Intercalada: ");
    imprimir_fila(resultado);
    // FRONT -> [1] -> [2] -> [3] -> [4] -> [5] -> [6] -> [7] <- REAR

    liberar_fila(fila1);
    liberar_fila(fila2);
    liberar_fila(resultado);
    return 0;
}
```

Dica: use um loop que alterna entre dequeue de fila1 e dequeue de fila2, fazendo enqueue no resultado. Quando uma fila esvaziar, continue com a outra.

---

## Exercício 11: Fila com Tamanho Máximo

Modifique a fila com lista encadeada para ter um tamanho máximo. Adicione um campo `int max_tamanho` à struct `Fila`. O `enqueue` deve recusar novos elementos quando a fila atingir o limite.

```c
typedef struct Fila {
    No *front;
    No *rear;
    int tamanho;
    int max_tamanho;  // novo campo
} Fila;
```

Implemente:
- `criar_fila_limitada(max)` — cria uma fila com tamanho máximo
- `enqueue` modificado — retorna 0 se a fila está cheia, 1 se inseriu com sucesso
- `esta_cheia(fila)` — retorna 1 se tamanho == max_tamanho

Teste:

```c
int main() {
    Fila *fila = criar_fila_limitada(3);

    printf("Enqueue 10: %s\n", enqueue(fila, 10) ? "OK" : "CHEIA");  // OK
    printf("Enqueue 20: %s\n", enqueue(fila, 20) ? "OK" : "CHEIA");  // OK
    printf("Enqueue 30: %s\n", enqueue(fila, 30) ? "OK" : "CHEIA");  // OK
    printf("Enqueue 40: %s\n", enqueue(fila, 40) ? "OK" : "CHEIA");  // CHEIA
    imprimir_fila(fila);  // [10] -> [20] -> [30]

    dequeue(fila);  // remove 10
    printf("Enqueue 40: %s\n", enqueue(fila, 40) ? "OK" : "CHEIA");  // OK
    imprimir_fila(fila);  // [20] -> [30] -> [40]

    liberar_fila(fila);
    return 0;
}
```

Dica: a única mudança no `enqueue` é adicionar uma verificação no início: `if (fila->tamanho >= fila->max_tamanho) return 0;`

---

## Exercício 12 (Desafio): Fila de Prioridade Simples

Implemente uma fila de prioridade simples usando 3 filas internas — uma para cada nível de prioridade (alta, média, baixa). O dequeue sempre retira da fila de alta prioridade primeiro. Se estiver vazia, tenta a média. Se também estiver vazia, tenta a baixa.

```c
typedef struct FilaPrioridade {
    Fila *alta;
    Fila *media;
    Fila *baixa;
} FilaPrioridade;
```

Implemente:
- `criar_fila_prioridade()` — cria as 3 filas internas
- `enqueue_prioridade(fp, valor, prioridade)` — prioridade: 1=alta, 2=media, 3=baixa
- `dequeue_prioridade(fp)` — retira da fila de maior prioridade não vazia
- `imprimir_prioridade(fp)` — mostra as 3 filas

Teste:

```c
int main() {
    FilaPrioridade *fp = criar_fila_prioridade();

    enqueue_prioridade(fp, 100, 3);  // baixa
    enqueue_prioridade(fp, 200, 1);  // alta
    enqueue_prioridade(fp, 300, 2);  // media
    enqueue_prioridade(fp, 400, 1);  // alta
    enqueue_prioridade(fp, 500, 3);  // baixa
    enqueue_prioridade(fp, 600, 2);  // media

    imprimir_prioridade(fp);

    // Dequeue deve sair: 200, 400 (alta), 300, 600 (media), 100, 500 (baixa)
    while (!todas_vazias(fp)) {
        printf("Dequeue: %d\n", dequeue_prioridade(fp));
    }

    liberar_fila_prioridade(fp);
    return 0;
}
```

Saída esperada:
```
Alta:  [200] -> [400]
Media: [300] -> [600]
Baixa: [100] -> [500]
Dequeue: 200
Dequeue: 400
Dequeue: 300
Dequeue: 600
Dequeue: 100
Dequeue: 500
```

Dica: reutilize a implementação de fila que você já tem. A fila de prioridade é apenas um "gerenciador" que decide de qual fila interna fazer dequeue.

---

[← Voltar ao conteúdo: Filas](cap07-mod07-filas-conteudo.md)
