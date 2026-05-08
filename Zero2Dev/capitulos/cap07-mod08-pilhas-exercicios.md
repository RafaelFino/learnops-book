# 7.8 — Exercícios: Pilhas (LIFO)

[← Voltar ao conteúdo: Pilhas](cap07-mod08-pilhas-conteudo.md)

---

## Sobre os Exercícios

Estes exercícios cobrem os conceitos de pilhas LIFO apresentados no módulo 7.8. Estão organizados em ordem crescente de dificuldade: os primeiros reforçam conceitos básicos, os últimos desafiam você a aplicar pilhas em cenários mais complexos.

Para todos os exercícios com código, compile e execute:

```bash
gcc -o exercicio exercicio.c
./exercicio
```

---

## Exercício 1: Conceitos Fundamentais

Responda sem consultar o material:

a) O que significa LIFO? Dê um exemplo do dia a dia.

b) Quais são as duas operações fundamentais de uma pilha? Qual a complexidade de cada uma?

c) Por que a pilha precisa de apenas um ponteiro (top) enquanto a fila precisa de dois (front e rear)?

d) Qual a diferença entre `peek` e `pop`?

e) O que é stack overflow? Quando acontece?

---

## Exercício 2: Rastreando Operações no Papel

Dada a seguinte sequência de operações em uma pilha inicialmente vazia, desenhe o estado da pilha (top) após cada operação e indique o valor retornado quando aplicável:

```
1. push(5)
2. push(10)
3. push(15)
4. pop()        → retorna ?
5. push(20)
6. pop()        → retorna ?
7. pop()        → retorna ?
8. push(25)
9. push(30)
10. pop()       → retorna ?
11. pop()       → retorna ?
12. pop()       → retorna ?
13. pop()       → retorna ? (o que acontece?)
```

**Respostas esperadas:**

| Passo | Operação | Retorno | Estado da pilha (top ... fundo) |
|-------|----------|---------|-------------------------------|
| 1 | push(5) | — | [5] |
| 2 | push(10) | — | [10] → [5] |
| 3 | push(15) | — | [15] → [10] → [5] |
| 4 | pop() | 15 | [10] → [5] |
| 5 | push(20) | — | [20] → [10] → [5] |
| 6 | pop() | 20 | [10] → [5] |
| 7 | pop() | 10 | [5] |
| 8 | push(25) | — | [25] → [5] |
| 9 | push(30) | — | [30] → [25] → [5] |
| 10 | pop() | 30 | [25] → [5] |
| 11 | pop() | 25 | [5] |
| 12 | pop() | 5 | (vazia) |
| 13 | pop() | erro | Pilha vazia — não ha o que remover |

Compare com o exercício equivalente de filas (exercício 2 do módulo 7.7). Na fila, os valores saíam na ordem 5, 10, 15... Na pilha, saem na ordem 15, 10, 5... — ordem inversa.

---
## Exercício 3: Implementar Pilha Básica do Zero

Implemente uma pilha de inteiros com lista encadeada, sem consultar o módulo. Escreva todas as funções:

- `criar_pilha()` — cria e retorna uma pilha vazia
- `push(pilha, valor)` — insere no topo
- `pop(pilha)` — remove do topo e retorna o valor
- `peek(pilha)` — retorna o topo sem remover
- `esta_vazia(pilha)` — retorna 1 se vazia, 0 se não
- `imprimir_pilha(pilha)` — mostra todos os elementos
- `liberar_pilha(pilha)` — libera toda a memória

Teste com este `main`:

```c
int main() {
    Pilha *pilha = criar_pilha();

    push(pilha, 100);
    push(pilha, 200);
    push(pilha, 300);
    imprimir_pilha(pilha);  // TOP -> [300] -> [200] -> [100] <- FUNDO

    printf("Peek: %d\n", peek(pilha));    // 300
    printf("Pop: %d\n", pop(pilha));      // 300
    printf("Pop: %d\n", pop(pilha));      // 200
    imprimir_pilha(pilha);  // TOP -> [100] <- FUNDO

    push(pilha, 400);
    push(pilha, 500);
    imprimir_pilha(pilha);  // TOP -> [500] -> [400] -> [100] <- FUNDO

    // Esvaziar
    while (!esta_vazia(pilha)) {
        printf("Pop: %d\n", pop(pilha));
    }
    imprimir_pilha(pilha);  // (vazia)

    pop(pilha);  // Erro: pilha vazia!

    liberar_pilha(pilha);
    return 0;
}
```

Saída esperada:
```
Pilha: TOP -> [300] -> [200] -> [100] <- FUNDO
Peek: 300
Pop: 300
Pop: 200
Pilha: TOP -> [100] <- FUNDO
Pilha: TOP -> [500] -> [400] -> [100] <- FUNDO
Pop: 500
Pop: 400
Pop: 100
Pilha: (vazia)
Erro: pilha vazia!
```

Dica: push é inserir no início da lista (novo->next = top, top = novo). Pop é remover do início (salvar top, avançar top, free).

---

## Exercício 4: Encontrar o Bug

Cada trecho de código abaixo tem um bug relacionado a pilhas. Identifique o problema, explique a consequência e corrija.

### Bug A:

```c
void push(Pilha *pilha, int valor) {
    No *novo = (No*)malloc(sizeof(No));
    novo->dado = valor;
    novo->next = NULL;  // BUG: deveria apontar para o topo atual
    pilha->top = novo;
    pilha->tamanho++;
}
```

Pergunta: o que acontece com os elementos que já estavam na pilha?

### Bug B:

```c
int pop(Pilha *pilha) {
    int valor = pilha->top->dado;
    pilha->top = pilha->top->next;
    pilha->tamanho--;
    return valor;
}
```

Pergunta: quais são os dois problemas neste código?

### Bug C:

```c
void liberar_pilha(Pilha *pilha) {
    while (pilha->top != NULL) {
        pilha->top = pilha->top->next;
    }
    free(pilha);
}
```

Pergunta: por que esse código causa memory leak?

### Respostas Comentadas

**Bug A:** `novo->next = NULL` faz o novo nó não apontar para nenhum outro nó. Quando `pilha->top = novo`, todos os nós anteriores ficam inacessíveis — memory leak. A correção é `novo->next = pilha->top` — o novo nó aponta para o antigo topo, mantendo a cadeia.

```c
void push(Pilha *pilha, int valor) {
    No *novo = (No*)malloc(sizeof(No));
    novo->dado = valor;
    novo->next = pilha->top;  // CORRETO: aponta para o topo atual
    pilha->top = novo;
    pilha->tamanho++;
}
```

**Bug B:** Dois problemas. Primeiro: não verifica se a pilha está vazia — se `pilha->top` é NULL, `pilha->top->dado` causa segfault. Segundo: não libera a memória do nó removido — memory leak a cada pop.

```c
int pop(Pilha *pilha) {
    if (pilha->top == NULL) {  // verificar pilha vazia
        printf("Erro: pilha vazia!\n");
        return -1;
    }
    No *temp = pilha->top;     // salvar referencia
    int valor = temp->dado;
    pilha->top = pilha->top->next;
    free(temp);                // liberar memoria!
    pilha->tamanho--;
    return valor;
}
```

**Bug C:** O loop avança `pilha->top` para o próximo nó, mas nunca chama `free` nos nós. Os nós ficam perdidos na memória. A correção é salvar o nó atual, avançar, e depois liberar:

```c
void liberar_pilha(Pilha *pilha) {
    while (pilha->top != NULL) {
        No *temp = pilha->top;
        pilha->top = pilha->top->next;
        free(temp);  // liberar cada no!
    }
    free(pilha);
}
```

---

## Exercício 5: Inverter uma String com Pilha

Escreva uma função `void inverter_string(const char *original, char *resultado)` que usa uma pilha de caracteres para inverter uma string.

Algoritmo:
1. Percorra a string original e empilhe cada caractere
2. Desempilhe todos os caracteres e coloque no resultado

Teste:

```c
int main() {
    char resultado[100];

    inverter_string("Hello", resultado);
    printf("'Hello' invertida: '%s'\n", resultado);  // olleH

    inverter_string("abcde", resultado);
    printf("'abcde' invertida: '%s'\n", resultado);  // edcba

    inverter_string("12345", resultado);
    printf("'12345' invertida: '%s'\n", resultado);  // 54321

    inverter_string("a", resultado);
    printf("'a' invertida: '%s'\n", resultado);  // a

    inverter_string("", resultado);
    printf("'' invertida: '%s'\n", resultado);  // (vazio)

    return 0;
}
```

Saída esperada:
```
'Hello' invertida: 'olleH'
'abcde' invertida: 'edcba'
'12345' invertida: '54321'
'a' invertida: 'a'
'' invertida: ''
```

Dica: crie uma pilha de `char`. Use `strlen` para saber o tamanho da string. Lembre-se de colocar `'\0'` no final do resultado.

---

## Exercício 6: Converter Decimal para Binário com Pilha

Escreva uma função que converte um número decimal para binário usando uma pilha. O algoritmo é:
1. Divida o número por 2 repetidamente
2. Empilhe o resto de cada divisão
3. Desempilhe todos os restos — o resultado é o número em binário

Exemplo: 13 em binário
- 13 / 2 = 6, resto 1 (push 1)
- 6 / 2 = 3, resto 0 (push 0)
- 3 / 2 = 1, resto 1 (push 1)
- 1 / 2 = 0, resto 1 (push 1)
- Desempilhar: 1, 1, 0, 1 → 1101

Teste:

```c
int main() {
    printf("13 em binario: ");
    decimal_para_binario(13);  // 1101

    printf("42 em binario: ");
    decimal_para_binario(42);  // 101010

    printf("255 em binario: ");
    decimal_para_binario(255);  // 11111111

    printf("1 em binario: ");
    decimal_para_binario(1);  // 1

    printf("0 em binario: ");
    decimal_para_binario(0);  // 0

    return 0;
}
```

Saída esperada:
```
13 em binario: 1101
42 em binario: 101010
255 em binario: 11111111
1 em binario: 1
0 em binario: 0
```

Dica: use `número % 2` para obter o resto e `número / 2` para a próxima divisão. Trate o caso especial de `número == 0`.

---

## Exercício 7: Pilha com Mínimo em O(1)

Implemente uma pilha que, além de push e pop, tem uma operação `mínimo()` que retorna o menor valor da pilha em O(1) — sem percorrer todos os elementos.

Estratégia: use duas pilhas — a pilha principal e uma pilha auxiliar que guarda o mínimo atual. A cada push, se o valor é menor ou igual ao topo da pilha de mínimos, empilhe na pilha de mínimos também. A cada pop, se o valor removido é igual ao topo da pilha de mínimos, desempilhe da pilha de mínimos.

Teste:

```c
int main() {
    PilhaMinimo *pm = criar_pilha_minimo();

    push_min(pm, 5);
    printf("Minimo: %d\n", minimo(pm));  // 5

    push_min(pm, 3);
    printf("Minimo: %d\n", minimo(pm));  // 3

    push_min(pm, 7);
    printf("Minimo: %d\n", minimo(pm));  // 3

    push_min(pm, 1);
    printf("Minimo: %d\n", minimo(pm));  // 1

    pop_min(pm);  // remove 1
    printf("Minimo: %d\n", minimo(pm));  // 3

    pop_min(pm);  // remove 7
    printf("Minimo: %d\n", minimo(pm));  // 3

    pop_min(pm);  // remove 3
    printf("Minimo: %d\n", minimo(pm));  // 5

    liberar_pilha_minimo(pm);
    return 0;
}
```

Dica: a pilha de mínimos sempre tem no topo o menor valor atual da pilha principal. Quando o menor valor é removido da pilha principal, ele também é removido da pilha de mínimos, revelando o próximo menor.

---

## Exercício 8: Ordenar uma Pilha usando Outra Pilha

Escreva uma função `void ordenar_pilha(Pilha *pilha)` que ordena os elementos da pilha em ordem crescente (menor no topo) usando apenas uma pilha auxiliar. Não use arrays nem outras estruturas.

Algoritmo:
1. Crie uma pilha auxiliar (temporária)
2. Enquanto a pilha original não estiver vazia:
   - Pop um elemento da original (chame de `temp`)
   - Enquanto a auxiliar não estiver vazia E o topo da auxiliar for maior que `temp`:
     - Pop da auxiliar e push na original
   - Push `temp` na auxiliar
3. Mova tudo da auxiliar de volta para a original

Teste:

```c
int main() {
    Pilha *pilha = criar_pilha();

    push(pilha, 34);
    push(pilha, 3);
    push(pilha, 31);
    push(pilha, 98);
    push(pilha, 92);
    push(pilha, 23);

    printf("Antes: ");
    imprimir_pilha(pilha);
    // TOP -> [23] -> [92] -> [98] -> [31] -> [3] -> [34] <- FUNDO

    ordenar_pilha(pilha);

    printf("Depois: ");
    imprimir_pilha(pilha);
    // TOP -> [3] -> [23] -> [31] -> [34] -> [92] -> [98] <- FUNDO

    liberar_pilha(pilha);
    return 0;
}
```

Dica: a pilha auxiliar funciona como uma "área de ordenação". Cada elemento da original é inserido na posição correta da auxiliar, movendo elementos maiores de volta para a original temporariamente.

---

## Exercício 9: Simulador de Navegador (Voltar/Avançar)

Crie um simulador de navegador web com pilhas de "voltar" e "avançar". O navegador deve suportar:

- `visitar(url)` — navegar para uma nova URL (empilha na pilha de voltar, limpa a pilha de avançar)
- `voltar()` — voltar para a página anterior (move da pilha de voltar para a de avançar)
- `avancar()` — avançar para a página seguinte (move da pilha de avançar para a de voltar)
- `pagina_atual()` — mostrar a URL atual (topo da pilha de voltar)

Teste:

```c
int main() {
    // Crie as pilhas aqui

    visitar("google.com");
    visitar("github.com");
    visitar("stackoverflow.com");
    visitar("youtube.com");
    printf("Atual: %s\n", pagina_atual());  // youtube.com

    voltar();  // volta para stackoverflow.com
    printf("Atual: %s\n", pagina_atual());  // stackoverflow.com

    voltar();  // volta para github.com
    printf("Atual: %s\n", pagina_atual());  // github.com

    avancar();  // avanca para stackoverflow.com
    printf("Atual: %s\n", pagina_atual());  // stackoverflow.com

    visitar("reddit.com");  // nova visita limpa o historico de avancar
    printf("Atual: %s\n", pagina_atual());  // reddit.com

    avancar();  // nada para avancar
    // Mensagem: Nao ha pagina para avancar

    // Liberar memoria
    return 0;
}
```

Saída esperada:
```
[VISITAR] google.com
[VISITAR] github.com
[VISITAR] stackoverflow.com
[VISITAR] youtube.com
Atual: youtube.com
[VOLTAR] youtube.com -> stackoverflow.com
Atual: stackoverflow.com
[VOLTAR] stackoverflow.com -> github.com
Atual: github.com
[AVANCAR] github.com -> stackoverflow.com
Atual: stackoverflow.com
[VISITAR] reddit.com (historico de avancar limpo)
Atual: reddit.com
Nao ha pagina para avancar.
```

Dica: use duas pilhas de strings. `visitar` faz push na pilha de voltar e limpa a pilha de avançar. `voltar` faz pop da pilha de voltar e push na de avançar. `avancar` faz o inverso.

---

## Exercício 10: Avaliar Expressão Infixa Simples

Escreva um programa que avalia expressões infixas simples (sem parênteses) com apenas soma e multiplicação, respeitando a precedência (* antes de +).

Estratégia com duas pilhas:
- Pilha de números
- Pilha de operadores
- Quando encontrar `*`, aplique imediatamente (desempilhe dois números, multiplique, empilhe resultado)
- Quando encontrar `+`, empilhe o operador
- No final, aplique todos os `+` restantes

Teste:

```c
int main() {
    printf("3 + 4 = %d\n", avaliar("3 + 4"));          // 7
    printf("3 * 4 = %d\n", avaliar("3 * 4"));          // 12
    printf("3 + 4 * 2 = %d\n", avaliar("3 + 4 * 2"));  // 11 (nao 14!)
    printf("2 * 3 + 4 = %d\n", avaliar("2 * 3 + 4"));  // 10
    printf("2 * 3 + 4 * 5 = %d\n", avaliar("2 * 3 + 4 * 5"));  // 26

    return 0;
}
```

Dica: este é um exercício avançado. A chave é que `*` tem precedência sobre `+`. Quando encontrar `*`, resolva imediatamente. Quando encontrar `+`, guarde para resolver depois.

---

## Exercício 11: Pilha com Tamanho Máximo

Modifique a pilha com lista encadeada para ter um tamanho máximo. O `push` deve recusar novos elementos quando a pilha atingir o limite.

```c
typedef struct Pilha {
    No *top;
    int tamanho;
    int max_tamanho;  // novo campo
} Pilha;
```

Teste:

```c
int main() {
    Pilha *pilha = criar_pilha_limitada(3);

    printf("Push 10: %s\n", push(pilha, 10) ? "OK" : "CHEIA");  // OK
    printf("Push 20: %s\n", push(pilha, 20) ? "OK" : "CHEIA");  // OK
    printf("Push 30: %s\n", push(pilha, 30) ? "OK" : "CHEIA");  // OK
    printf("Push 40: %s\n", push(pilha, 40) ? "OK" : "CHEIA");  // CHEIA
    imprimir_pilha(pilha);  // [30] -> [20] -> [10]

    pop(pilha);  // remove 30
    printf("Push 40: %s\n", push(pilha, 40) ? "OK" : "CHEIA");  // OK
    imprimir_pilha(pilha);  // [40] -> [20] -> [10]

    liberar_pilha(pilha);
    return 0;
}
```

---

## Exercício 12 (Desafio): Implementar uma Fila usando Duas Pilhas

Implemente uma fila (FIFO) usando apenas duas pilhas (LIFO). Não use listas encadeadas nem arrays diretamente — apenas as operações push e pop das pilhas.

Estratégia:
- Pilha de entrada: onde novos elementos são inseridos (enqueue = push na pilha de entrada)
- Pilha de saída: de onde elementos são removidos (dequeue = pop da pilha de saída)
- Quando a pilha de saída estiver vazia e precisar fazer dequeue, transfira todos os elementos da pilha de entrada para a pilha de saída (pop de uma, push na outra). Isso inverte a ordem — LIFO vira FIFO.

Teste:

```c
int main() {
    FilaComPilhas *fila = criar_fila_com_pilhas();

    enqueue_fp(fila, 10);
    enqueue_fp(fila, 20);
    enqueue_fp(fila, 30);

    printf("Dequeue: %d\n", dequeue_fp(fila));  // 10 (FIFO!)
    printf("Dequeue: %d\n", dequeue_fp(fila));  // 20

    enqueue_fp(fila, 40);
    enqueue_fp(fila, 50);

    printf("Dequeue: %d\n", dequeue_fp(fila));  // 30
    printf("Dequeue: %d\n", dequeue_fp(fila));  // 40
    printf("Dequeue: %d\n", dequeue_fp(fila));  // 50

    liberar_fila_com_pilhas(fila);
    return 0;
}
```

Saída esperada:
```
Dequeue: 10
Dequeue: 20
Dequeue: 30
Dequeue: 40
Dequeue: 50
```

Dica: a transferência da pilha de entrada para a de saída inverte a ordem. Se a entrada tem [30, 20, 10] (30 no topo), após transferir a saída tem [10, 20, 30] (10 no topo). Agora pop da saída retorna 10 — que foi o primeiro a entrar. FIFO usando LIFO.

Este exercício é uma pergunta clássica de entrevistas técnicas em empresas de tecnologia.

---

[← Voltar ao conteúdo: Pilhas](cap07-mod08-pilhas-conteudo.md)
