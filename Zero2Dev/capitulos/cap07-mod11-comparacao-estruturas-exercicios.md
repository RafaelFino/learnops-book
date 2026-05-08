# 7.11 — Exercícios: Comparando Estruturas de Dados

[← Voltar ao conteúdo: Comparando Estruturas](cap07-mod11-comparacao-estruturas-conteudo.md)

---

## Sobre os Exercícios

Estes exercícios consolidam todo o capítulo 7. Aqui você vai praticar a habilidade mais importante que um programador pode ter com estruturas de dados: **escolher a estrutura certa para cada problema**.

Alguns exercícios são de análise (pensar e justificar), outros são de código (implementar e comparar). Todos exigem que você conecte os conceitos dos módulos 7.5 a 7.11.

```bash
# Para exercícios em C
gcc -o exercicio exercicio.c
./exercicio

# Para exercícios em Python
python3 exercicio.py
```

---

## Exercício 1: Escolha Rápida — Justifique em Uma Frase

Para cada cenário, indique a estrutura de dados mais adequada e justifique em uma frase:

a) Um sistema de impressão que processa documentos na ordem em que foram enviados.

b) Um aplicativo de calculadora que precisa avaliar expressões com parênteses aninhados.

c) Um sistema de login que precisa verificar se um email já está cadastrado entre 500.000 usuários.

d) Um jogo de cartas que precisa armazenar as 52 cartas do baralho em ordem.

e) Um editor de texto que precisa permitir Ctrl+Z (desfazer) com até 100 níveis.

f) Um sistema de streaming de vídeo que armazena os próximos 10 segundos de conteúdo em buffer.

g) Uma rede social que precisa encontrar rapidamente o perfil de um usuário pelo username.

h) Um sistema de hospital que atende pacientes por ordem de chegada, mas emergências passam na frente.

i) Um navegador GPS que precisa armazenar o caminho percorrido para permitir "voltar ao ponto anterior".

j) Um compilador que precisa verificar se todas as chaves `{` e `}` estão balanceadas no código.

k) Um sistema de e-commerce que precisa manter um catálogo de 10.000 produtos com busca por código.

l) Um programa que precisa armazenar as temperaturas dos últimos 365 dias e calcular a média.

**Respostas:**

| Cenário | Estrutura | Justificativa |
|---------|-----------|---------------|
| a) Impressao | Fila | FIFO — documentos processados na ordem de envio |
| b) Calculadora | Pilha | Parenteses são LIFO — último aberto e primeiro fechado |
| c) Login 500k | Dicionário (HashSet) | Busca por chave O(1) — essencial com 500k registros |
| d) Baralho 52 cartas | Array | Tamanho fixo conhecido, acesso por índice |
| e) Ctrl+Z | Pilha | LIFO — última ação e a primeira desfeita |
| f) Buffer video | Fila circular (array) | FIFO com tamanho fixo, sem alocação dinâmica |
| g) Perfil por username | Dicionário | Busca por chave (username) em O(1) |
| h) Hospital com prioridade | Fila de prioridade | FIFO com exceção para emergencias |
| i) GPS voltar | Pilha | LIFO — último ponto visitado e o primeiro a voltar |
| j) Chaves balanceadas | Pilha | Mesmo problema dos parenteses — LIFO |
| k) Catalogo 10k produtos | Dicionário | Busca por código (chave) em O(1) |
| l) Temperaturas 365 dias | Array | Tamanho fixo, acesso por índice (dia do ano) |

---

## Exercício 2: Análise de Trade-offs

Para cada par de estruturas, explique quando você escolheria a primeira e quando escolheria a segunda. Dê um exemplo concreto para cada caso.

a) Array vs Lista Encadeada

b) Fila vs Pilha

c) Array vs Dicionário

d) Lista Encadeada vs Dicionário

e) Pilha com Array vs Pilha com Lista Encadeada

**Respostas sugeridas:**

a) **Array** quando o tamanho é conhecido e precisa de acesso por índice (ex: notas de 30 alunos). **Lista encadeada** quando o tamanho é desconhecido e há muitas inserções/remoções no meio (ex: playlist de música editável).

b) **Fila** quando a ordem de chegada importa (ex: fila de atendimento). **Pilha** quando a ordem inversa importa (ex: desfazer operações).

c) **Array** quando as chaves são inteiros sequenciais (ex: temperaturas por dia do ano). **Dicionário** quando as chaves são arbitrárias (ex: buscar usuário por email).

d) **Lista encadeada** quando precisa percorrer sequencialmente e inserir/remover no meio (ex: editor de texto). **Dicionário** quando precisa de busca rápida por chave (ex: cache de páginas web).

e) **Pilha com array** quando o tamanho máximo é conhecido e performance é crítica (ex: call stack com limite fixo — melhor localidade de cache). **Pilha com lista** quando o tamanho é imprevisível (ex: histórico de navegação sem limite).

---

## Exercício 3: Calcule a Complexidade Total

Um programa faz as seguintes operações em uma coleção de N elementos:
- 100 inserções no final
- 10.000 buscas por valor
- 50 remoções do início

Calcule o número total de operações (em termos de N) para cada estrutura e determine qual é a melhor escolha para N = 1.000 e N = 100.000.

Complete a tabela:

| Operação | Array | Lista Encadeada | Dicionário |
|----------|-------|-----------------|------------|
| 100 insercoes no final | ? | ? | ? |
| 10.000 buscas por valor | ? | ? | ? |
| 50 remocoes do inicio | ? | ? | ? |
| Total | ? | ? | ? |

**Resposta:**

| Operação | Array | Lista Encadeada | Dicionário |
|----------|-------|-----------------|------------|
| 100 insercoes no final | 100 (O(1) amortizado) | 100*N (O(N) sem tail) ou 100 (com tail) | 100 (O(1)) |
| 10.000 buscas por valor | 10.000*N (O(N) cada) | 10.000*N (O(N) cada) | 10.000 (O(1) cada) |
| 50 remocoes do inicio | 50*N (O(N) cada) | 50 (O(1) cada) | 50 (O(1) cada) |
| Total (N=1.000) | ~10.050.100 | ~10.000.150 | ~10.150 |
| Total (N=100.000) | ~1.005.000.100 | ~1.000.000.150 | ~10.150 |

Para ambos os valores de N, o dicionário é a melhor escolha por causa das 10.000 buscas. A busca O(1) domina o resultado. A diferença entre array e lista encadeada é pequena — ambos sofrem com busca O(N).

---

## Exercício 4: Identificar o Erro de Estrutura

Cada trecho de código abaixo usa uma estrutura de dados inadequada. Identifique o problema e sugira a estrutura correta.

### Caso A: Verificação de duplicatas

```python
# Verificar se um produto ja existe no catalogo (50.000 produtos)
catalogo = []  # lista de codigos de produto

def produto_existe(codigo):
    for c in catalogo:
        if c == codigo:
            return True
    return False

# Chamado 100.000 vezes por dia
```

**Problema:** Busca linear O(n) em lista com 50.000 elementos, chamada 100.000 vezes por dia = 5 bilhões de comparações por dia.

**Solução:** Usar `set` (HashSet/dicionário) — busca O(1):

```python
catalogo = set()  # conjunto de codigos

def produto_existe(codigo):
    return codigo in catalogo  # O(1)
```

### Caso B: Fila com array

```c
// Fila de atendimento usando array
int fila[1000];
int tamanho = 0;

void enqueue(int valor) {
    fila[tamanho++] = valor;  // O(1) — OK
}

int dequeue() {
    int primeiro = fila[0];
    // Mover todos os elementos uma posicao para a esquerda
    for (int i = 0; i < tamanho - 1; i++) {
        fila[i] = fila[i + 1];  // O(n)!
    }
    tamanho--;
    return primeiro;
}
```

**Problema:** Dequeue é O(n) porque move todos os elementos. Para uma fila com 1.000 elementos, cada dequeue faz 999 cópias.

**Solução:** Usar fila com lista encadeada (dequeue O(1)) ou fila circular com array (dequeue O(1) sem mover elementos):

```c
// Fila circular — dequeue O(1)
int fila[1000];
int inicio = 0, fim = 0, tamanho = 0;

void enqueue(int valor) {
    fila[fim] = valor;
    fim = (fim + 1) % 1000;
    tamanho++;
}

int dequeue() {
    int valor = fila[inicio];
    inicio = (inicio + 1) % 1000;
    tamanho--;
    return valor;
}
```

### Caso C: Dicionário para dados sequenciais

```python
# Armazenar notas de 30 alunos
notas = {}
for i in range(30):
    notas[i] = float(input(f"Nota do aluno {i+1}: "))

# Calcular media
soma = sum(notas.values())
media = soma / len(notas)
```

**Problema:** As chaves são inteiros sequenciais (0, 1, 2, ..., 29). Dicionário usa mais memória e é mais lento que array para esse caso. Não há benefício em usar hash quando o índice já é a chave.

**Solução:** Usar lista (array dinâmico):

```python
notas = []
for i in range(30):
    notas.append(float(input(f"Nota do aluno {i+1}: ")))

media = sum(notas) / len(notas)
```

---

## Exercício 5: Projetar Estruturas para um Sistema Real

Você vai projetar as estruturas de dados para um **sistema de suporte técnico**. O sistema tem as seguintes funcionalidades:

1. Clientes abrem chamados (ticket) com descrição e prioridade (baixa, média, alta)
2. Chamados são atendidos por ordem de prioridade (alta primeiro), e dentro da mesma prioridade, por ordem de chegada
3. Cada atendente pode "desfazer" a última ação realizada em um chamado
4. O sistema mantém um cadastro de clientes com busca rápida por CPF
5. Cada cliente tem um histórico de chamados anteriores

Para cada funcionalidade, indique:
- Qual estrutura de dados usar
- Por que essa estrutura é a melhor escolha
- Qual seria a complexidade das operações principais

**Resposta sugerida:**

| Funcionalidade | Estrutura | Justificativa | Complexidade |
|----------------|-----------|---------------|-------------|
| Fila de chamados por prioridade | 3 filas (uma por prioridade) | FIFO dentro de cada nível, atender alta primeiro | Enqueue O(1), Dequeue O(1) |
| Desfazer última ação | Pilha por chamado | LIFO — última ação desfeita primeiro | Push O(1), Pop O(1) |
| Cadastro de clientes por CPF | Dicionário (CPF -> cliente) | Busca por chave O(1) | Busca O(1), Inserção O(1) |
| Histórico de chamados | Lista encadeada por cliente | Ordem cronologica, tamanho variável | Inserção O(1), Percorrer O(n) |

---

## Exercício 6: Benchmark — Medir na Prática

Implemente um programa em C que compara o tempo de busca em três estruturas diferentes: array não ordenado (busca linear), array ordenado (busca binária) e "hash set" simples.

O programa deve:
1. Criar uma coleção com 50.000 números aleatórios
2. Buscar 5.000 números aleatórios em cada estrutura
3. Medir e imprimir o tempo de cada abordagem

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 50000
#define BUSCAS 5000
#define HASH_SIZE 100003  // numero primo para melhor distribuicao

// --- Busca linear em array ---
int busca_linear(int arr[], int tam, int alvo) {
    for (int i = 0; i < tam; i++) {
        if (arr[i] == alvo) return 1;
    }
    return 0;
}

// --- Busca binaria em array ordenado ---
int busca_binaria(int arr[], int tam, int alvo) {
    int esq = 0, dir = tam - 1;
    while (esq <= dir) {
        int meio = esq + (dir - esq) / 2;
        if (arr[meio] == alvo) return 1;
        if (arr[meio] < alvo) esq = meio + 1;
        else dir = meio - 1;
    }
    return 0;
}

// --- Hash set simples ---
int hash_tabela[HASH_SIZE];
int hash_usado[HASH_SIZE];

void hash_limpar() {
    memset(hash_usado, 0, sizeof(hash_usado));
}

void hash_inserir(int valor) {
    int idx = abs(valor) % HASH_SIZE;
    while (hash_usado[idx]) {
        if (hash_tabela[idx] == valor) return;
        idx = (idx + 1) % HASH_SIZE;
    }
    hash_tabela[idx] = valor;
    hash_usado[idx] = 1;
}

int hash_buscar(int valor) {
    int idx = abs(valor) % HASH_SIZE;
    while (hash_usado[idx]) {
        if (hash_tabela[idx] == valor) return 1;
        idx = (idx + 1) % HASH_SIZE;
    }
    return 0;
}

int comparar(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int dados[N];
    int ordenado[N];
    int alvos[BUSCAS];

    srand(42);

    // Gerar dados
    for (int i = 0; i < N; i++) {
        dados[i] = rand() % 1000000;
    }

    // Preparar array ordenado
    memcpy(ordenado, dados, sizeof(dados));
    qsort(ordenado, N, sizeof(int), comparar);

    // Preparar hash set
    hash_limpar();
    for (int i = 0; i < N; i++) {
        hash_inserir(dados[i]);
    }

    // Gerar alvos de busca
    for (int i = 0; i < BUSCAS; i++) {
        alvos[i] = rand() % 1000000;
    }

    // Medir busca linear
    clock_t inicio = clock();
    int enc_linear = 0;
    for (int i = 0; i < BUSCAS; i++) {
        enc_linear += busca_linear(dados, N, alvos[i]);
    }
    double t_linear = (double)(clock() - inicio) / CLOCKS_PER_SEC * 1000;

    // Medir busca binaria
    inicio = clock();
    int enc_binaria = 0;
    for (int i = 0; i < BUSCAS; i++) {
        enc_binaria += busca_binaria(ordenado, N, alvos[i]);
    }
    double t_binaria = (double)(clock() - inicio) / CLOCKS_PER_SEC * 1000;

    // Medir busca hash
    inicio = clock();
    int enc_hash = 0;
    for (int i = 0; i < BUSCAS; i++) {
        enc_hash += hash_buscar(alvos[i]);
    }
    double t_hash = (double)(clock() - inicio) / CLOCKS_PER_SEC * 1000;

    printf("=== Benchmark: %d elementos, %d buscas ===\n\n", N, BUSCAS);
    printf("Busca Linear:  %7.2f ms — %d encontrados\n", t_linear, enc_linear);
    printf("Busca Binaria: %7.2f ms — %d encontrados\n", t_binaria, enc_binaria);
    printf("Busca Hash:    %7.2f ms — %d encontrados\n", t_hash, enc_hash);
    printf("\nRazao Linear/Binaria: %.1fx\n", t_linear / (t_binaria > 0 ? t_binaria : 0.01));
    printf("Razao Linear/Hash:    %.1fx\n", t_linear / (t_hash > 0 ? t_hash : 0.01));

    return 0;
}
```

Saída esperada (valores aproximados — variam por máquina):

```
=== Benchmark: 50000 elementos, 5000 buscas ===

Busca Linear:  312.45 ms — 234 encontrados
Busca Binaria:   0.42 ms — 234 encontrados
Busca Hash:      0.08 ms — 234 encontrados

Razao Linear/Binaria: 743.9x
Razao Linear/Hash:    3905.6x
```

Depois de rodar, responda:
- Quantas vezes a busca binária foi mais rápida que a linear?
- Quantas vezes a busca hash foi mais rápida que a linear?
- Por que a busca hash é mais rápida que a binária, mesmo ambas sendo "rápidas"?

---

## Exercício 7: Combinar Estruturas — Projeto no Papel

Projete as estruturas de dados para um **sistema de streaming de música** (tipo Spotify simplificado). O sistema precisa de:

1. Catálogo de músicas (busca por título ou artista)
2. Playlist do usuário (adicionar, remover, reordenar músicas)
3. Fila de reprodução (próxima música a tocar)
4. Histórico de músicas ouvidas (para o botão "voltar")
5. Músicas curtidas (verificar rapidamente se uma música foi curtida)

Para cada funcionalidade:
- Escolha a estrutura de dados
- Justifique a escolha
- Indique a complexidade das operações principais
- Explique por que as alternativas seriam piores

**Resposta sugerida:**

| Funcionalidade | Estrutura | Justificativa | Alternativa descartada |
|----------------|-----------|---------------|----------------------|
| Catalogo (busca) | Dicionário (título -> musica) | Busca O(1) por título | Array com busca linear seria O(n) |
| Playlist | Lista duplamente encadeada | Inserir/remover em qualquer posição O(1), navegar frente/tras | Array exigiria mover elementos O(n) |
| Fila de reproducao | Fila | FIFO — próxima musica e a primeira da fila | Pilha tocaria na ordem inversa |
| Histórico | Pilha | LIFO — última musica ouvida e a primeira ao voltar | Fila mostraria a mais antiga primeiro |
| Musicas curtidas | Dicionário (HashSet) | Verificar se curtiu em O(1) | Lista exigiria busca O(n) |

---

## Exercício 8: Trace de Memória — Múltiplas Estruturas

Dado o código abaixo, desenhe o estado da memória após cada bloco de operações:

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No *prox;
} No;

// Pilha
No *topo = NULL;

void push(int valor) {
    No *novo = (No*)malloc(sizeof(No));
    novo->valor = valor;
    novo->prox = topo;
    topo = novo;
}

int pop() {
    if (topo == NULL) return -1;
    No *temp = topo;
    int valor = temp->valor;
    topo = topo->prox;
    free(temp);
    return valor;
}

int main() {
    // Bloco 1: empilhar 3 valores
    push(10);
    push(20);
    push(30);
    // Desenhe a pilha aqui

    // Bloco 2: desempilhar 1 valor
    int x = pop();
    printf("Pop: %d\n", x);
    // Desenhe a pilha aqui

    // Bloco 3: empilhar mais 1 valor
    push(40);
    // Desenhe a pilha aqui

    // Bloco 4: desempilhar tudo
    while (topo != NULL) {
        printf("Pop: %d\n", pop());
    }
    // Desenhe a pilha aqui

    return 0;
}
```

**Resposta:**

Bloco 1 — após push(10), push(20), push(30):
```
topo -> [30|*] -> [20|*] -> [10|NULL]
```

Bloco 2 — após pop() retorna 30:
```
topo -> [20|*] -> [10|NULL]
x = 30
```

Bloco 3 — após push(40):
```
topo -> [40|*] -> [20|*] -> [10|NULL]
```

Bloco 4 — após desempilhar tudo (pop 40, pop 20, pop 10):
```
topo -> NULL  (pilha vazia, toda memoria liberada)
```

Saída do programa:
```
Pop: 30
Pop: 40
Pop: 20
Pop: 10
```

---

## Exercício 9: Refatorar com Estrutura Melhor

O código abaixo implementa um sistema de cache que verifica se uma URL já foi visitada. Está usando uma lista (array) e busca linear. Refatore para usar um dicionário (set em Python).

### Versão original (lenta):

```python
# Cache de URLs visitadas — versao LENTA
urls_visitadas = []

def visitar_url(url):
    # Verificar se ja visitou — O(n)
    for u in urls_visitadas:
        if u == url:
            print(f"Cache hit: {url}")
            return
    # Nao visitou — adicionar
    urls_visitadas.append(url)
    print(f"Visitando: {url}")

# Simular navegacao
urls = [
    "https://exemplo.com",
    "https://google.com",
    "https://exemplo.com",  # repetida
    "https://github.com",
    "https://google.com",   # repetida
    "https://python.org",
    "https://exemplo.com",  # repetida
]

for url in urls:
    visitar_url(url)
```

### Sua tarefa:

Reescreva usando `set` para que a verificação seja O(1):

**Resposta:**

```python
# Cache de URLs visitadas — versao RAPIDA
urls_visitadas = set()

def visitar_url(url):
    if url in urls_visitadas:  # O(1)
        print(f"Cache hit: {url}")
        return
    urls_visitadas.add(url)  # O(1)
    print(f"Visitando: {url}")

urls = [
    "https://exemplo.com",
    "https://google.com",
    "https://exemplo.com",
    "https://github.com",
    "https://google.com",
    "https://python.org",
    "https://exemplo.com",
]

for url in urls:
    visitar_url(url)
```

Saída esperada (igual nas duas versões):
```
Visitando: https://exemplo.com
Visitando: https://google.com
Cache hit: https://exemplo.com
Visitando: https://github.com
Cache hit: https://google.com
Visitando: https://python.org
Cache hit: https://exemplo.com
```

A diferença: com 1 milhão de URLs, a versão com lista levaria minutos. A versão com set leva milissegundos.

---

## Exercício 10 (Desafio): Sistema Integrado em C

Implemente um programa em C que simula um **sistema de atendimento de restaurante** usando múltiplas estruturas:

- **Fila de pedidos**: clientes fazem pedidos que entram na fila (FIFO)
- **Pilha de pratos**: pratos limpos são empilhados (LIFO) — o último lavado é o primeiro usado
- **Array de mesas**: 10 mesas, cada uma pode estar livre ou ocupada
- **Contador**: dicionário simples (array de contadores) para contar quantos pedidos de cada tipo foram feitos

O programa deve ter um menu:
```
=== Restaurante ===
1. Novo pedido (entra na fila)
2. Preparar proximo pedido (sai da fila)
3. Lavar prato (empilha)
4. Usar prato (desempilha)
5. Ocupar mesa
6. Liberar mesa
7. Ver estatisticas
0. Sair
```

Esqueleto para começar:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// --- Estrutura de No (para fila e pilha) ---
typedef struct No {
    char descricao[100];
    struct No *prox;
} No;

// --- Fila de pedidos ---
typedef struct {
    No *inicio;
    No *fim;
    int tamanho;
} Fila;

void fila_iniciar(Fila *f) {
    f->inicio = NULL;
    f->fim = NULL;
    f->tamanho = 0;
}

void fila_enqueue(Fila *f, const char *desc) {
    No *novo = (No*)malloc(sizeof(No));
    strncpy(novo->descricao, desc, 99);
    novo->descricao[99] = '\0';
    novo->prox = NULL;
    if (f->fim != NULL) {
        f->fim->prox = novo;
    } else {
        f->inicio = novo;
    }
    f->fim = novo;
    f->tamanho++;
}

char* fila_dequeue(Fila *f, char *resultado) {
    if (f->inicio == NULL) return NULL;
    No *temp = f->inicio;
    strncpy(resultado, temp->descricao, 99);
    resultado[99] = '\0';
    f->inicio = temp->prox;
    if (f->inicio == NULL) f->fim = NULL;
    free(temp);
    f->tamanho--;
    return resultado;
}

// --- Pilha de pratos ---
typedef struct {
    No *topo;
    int tamanho;
} Pilha;

void pilha_iniciar(Pilha *p) {
    p->topo = NULL;
    p->tamanho = 0;
}

void pilha_push(Pilha *p, const char *desc) {
    No *novo = (No*)malloc(sizeof(No));
    strncpy(novo->descricao, desc, 99);
    novo->descricao[99] = '\0';
    novo->prox = p->topo;
    p->topo = novo;
    p->tamanho++;
}

char* pilha_pop(Pilha *p, char *resultado) {
    if (p->topo == NULL) return NULL;
    No *temp = p->topo;
    strncpy(resultado, temp->descricao, 99);
    resultado[99] = '\0';
    p->topo = temp->prox;
    free(temp);
    p->tamanho--;
    return resultado;
}

// --- Mesas (array) ---
#define NUM_MESAS 10
int mesas[NUM_MESAS];  // 0 = livre, 1 = ocupada

// --- Contadores de pedidos por tipo ---
#define NUM_TIPOS 5
const char *tipos[] = {"Pizza", "Hamburguer", "Salada", "Suco", "Sobremesa"};
int contadores[NUM_TIPOS];

int main() {
    Fila pedidos;
    Pilha pratos;
    fila_iniciar(&pedidos);
    pilha_iniciar(&pratos);
    memset(mesas, 0, sizeof(mesas));
    memset(contadores, 0, sizeof(contadores));

    int opcao;
    char buffer[100];

    do {
        printf("\n=== Restaurante ===\n");
        printf("1. Novo pedido\n");
        printf("2. Preparar proximo pedido\n");
        printf("3. Lavar prato\n");
        printf("4. Usar prato\n");
        printf("5. Ocupar mesa\n");
        printf("6. Liberar mesa\n");
        printf("7. Ver estatisticas\n");
        printf("0. Sair\n");
        printf("Opcao: ");
        scanf("%d", &opcao);
        getchar();  // limpar newline

        switch (opcao) {
            case 1:
                printf("Descricao do pedido: ");
                fgets(buffer, sizeof(buffer), stdin);
                buffer[strcspn(buffer, "\n")] = '\0';
                fila_enqueue(&pedidos, buffer);
                printf("Pedido adicionado! Fila: %d pedidos\n", pedidos.tamanho);
                break;

            case 2:
                if (fila_dequeue(&pedidos, buffer)) {
                    printf("Preparando: %s\n", buffer);
                    printf("Pedidos restantes: %d\n", pedidos.tamanho);
                } else {
                    printf("Nenhum pedido na fila!\n");
                }
                break;

            case 3:
                printf("Tipo do prato lavado: ");
                fgets(buffer, sizeof(buffer), stdin);
                buffer[strcspn(buffer, "\n")] = '\0';
                pilha_push(&pratos, buffer);
                printf("Prato empilhado! Pilha: %d pratos\n", pratos.tamanho);
                break;

            case 4:
                if (pilha_pop(&pratos, buffer)) {
                    printf("Usando prato: %s\n", buffer);
                    printf("Pratos restantes: %d\n", pratos.tamanho);
                } else {
                    printf("Nenhum prato limpo disponivel!\n");
                }
                break;

            case 5: {
                printf("Numero da mesa (1-%d): ", NUM_MESAS);
                int mesa;
                scanf("%d", &mesa);
                if (mesa >= 1 && mesa <= NUM_MESAS) {
                    if (mesas[mesa-1] == 0) {
                        mesas[mesa-1] = 1;
                        printf("Mesa %d ocupada!\n", mesa);
                    } else {
                        printf("Mesa %d ja esta ocupada!\n", mesa);
                    }
                } else {
                    printf("Mesa invalida!\n");
                }
                break;
            }

            case 6: {
                printf("Numero da mesa (1-%d): ", NUM_MESAS);
                int mesa;
                scanf("%d", &mesa);
                if (mesa >= 1 && mesa <= NUM_MESAS) {
                    if (mesas[mesa-1] == 1) {
                        mesas[mesa-1] = 0;
                        printf("Mesa %d liberada!\n", mesa);
                    } else {
                        printf("Mesa %d ja esta livre!\n", mesa);
                    }
                } else {
                    printf("Mesa invalida!\n");
                }
                break;
            }

            case 7: {
                printf("\n--- Estatisticas ---\n");
                printf("Pedidos na fila: %d\n", pedidos.tamanho);
                printf("Pratos limpos: %d\n", pratos.tamanho);
                int ocupadas = 0;
                for (int i = 0; i < NUM_MESAS; i++) {
                    if (mesas[i]) ocupadas++;
                }
                printf("Mesas ocupadas: %d/%d\n", ocupadas, NUM_MESAS);
                printf("Mesas: ");
                for (int i = 0; i < NUM_MESAS; i++) {
                    printf("[%d:%s] ", i+1, mesas[i] ? "X" : " ");
                }
                printf("\n");
                break;
            }
        }
    } while (opcao != 0);

    // Liberar memoria restante
    while (pedidos.inicio != NULL) {
        fila_dequeue(&pedidos, buffer);
    }
    while (pratos.topo != NULL) {
        pilha_pop(&pratos, buffer);
    }

    printf("Restaurante fechado!\n");
    return 0;
}
```

Compile e teste:
```bash
gcc -o restaurante restaurante.c
./restaurante
```

Depois de implementar, responda:
- Por que a fila de pedidos usa fila (FIFO) e não pilha (LIFO)?
- Por que os pratos usam pilha (LIFO) e não fila (FIFO)?
- Por que as mesas usam array e não lista encadeada?
- Se quiséssemos buscar um pedido específico na fila pelo nome do cliente, qual estrutura adicional ajudaria?

---

## Exercício 11 (Desafio): Análise de Cenário Complexo

Uma empresa de logística precisa de um sistema para gerenciar entregas. Análise os requisitos e projete as estruturas:

**Requisitos:**
1. 50.000 pacotes por dia, cada um com código de rastreamento único
2. Pacotes são processados na ordem de chegada ao centro de distribuição
3. Cada motorista tem uma rota com paradas ordenadas
4. O sistema precisa verificar rapidamente se um pacote já foi entregue
5. Clientes consultam o status do pacote pelo código de rastreamento
6. Se um pacote é devolvido, ele volta para o início da fila de processamento

Para cada requisito, indique a estrutura, justifique e análise a complexidade:

**Resposta sugerida:**

| Requisito | Estrutura | Justificativa | Complexidade |
|-----------|-----------|---------------|-------------|
| 1. Pacotes por código | Dicionário (código -> pacote) | Busca por chave única O(1) | Inserção O(1), Busca O(1) |
| 2. Ordem de chegada | Fila | FIFO — primeiro a chegar, primeiro processado | Enqueue O(1), Dequeue O(1) |
| 3. Rota do motorista | Array | Paradas em ordem fixa, acesso por índice | Acesso O(1) |
| 4. Verificar se entregue | Dicionário (HashSet de codigos entregues) | Verificacao O(1) | Busca O(1) |
| 5. Status por código | Mesmo dicionário do req 1 | Já temos busca O(1) por código | Busca O(1) |
| 6. Devolucao volta ao inicio | Fila com deque (inserção no inicio) | Permite inserir no inicio quando devolvido | Inserção inicio O(1) |

**Pergunta extra:** Se a empresa crescer para 500.000 pacotes por dia, alguma estrutura precisaria mudar? Por quê?

**Resposta:** Não. Todas as operações são O(1), então escalar de 50.000 para 500.000 não muda a complexidade. O dicionário pode precisar de mais memória e um tamanho de tabela hash maior para manter o fator de carga baixo, mas a complexidade permanece O(1). Essa é a beleza de escolher as estruturas certas desde o início.

---

[← Voltar ao conteúdo: Comparando Estruturas](cap07-mod11-comparacao-estruturas-conteudo.md)
