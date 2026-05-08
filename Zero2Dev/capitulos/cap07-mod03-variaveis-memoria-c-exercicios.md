# 7.3 — Exercícios: Variáveis, Tipos e Alocação de Memória em C

[← Voltar ao conteúdo: Variáveis e Memória](cap07-mod03-variaveis-memoria-c-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios focam em entender como variáveis funcionam na memória. Muitos pedem que você observe endereços, tamanhos e comportamentos que Python esconde de você. Compile sempre com `gcc -Wall` para ver avisos úteis.

---

## Exercício 1 — Tabela de Tipos (Básico)

### Enunciado

Crie um programa `tabela_tipos.c` que imprima uma tabela formatada com o tamanho de cada tipo básico de C. Use `sizeof` para obter os valores.

A tabela deve incluir: `char`, `short`, `int`, `long`, `float`, `double`, `unsigned char`, `unsigned int`, `unsigned long`.

### Exemplo de saída esperada

```
===========================================
  TIPO              TAMANHO (bytes)
===========================================
  char              1
  short             2
  int               4
  long              8
  float             4
  double            8
  unsigned char     1
  unsigned int      4
  unsigned long     8
===========================================
```

### Dicas

- Use `%-20s` no printf para alinhar texto à esquerda com 20 caracteres
- `sizeof` retorna `size_t`, use `%lu` para imprimir

---

## Exercício 2 — Mapa de Memória (Básico)

### Enunciado

Crie um programa `mapa_memoria.c` que declare as seguintes variáveis e imprima o valor, tamanho e endereço de cada uma:

```c
char inicial = 'R';
int idade = 30;
float altura = 1.82;
double saldo = 15750.50;
long cpf = 12345678901;
```

Depois de ver a saída, responda nos comentários do código:
1. Os endereços são consecutivos?
2. A diferença entre endereços corresponde ao sizeof de cada variável?
3. Por que pode haver "buracos" entre os endereços?

### Exemplo de saída esperada

```
=== Mapa de Memoria ===
Variavel    Valor              Tamanho    Endereco
inicial     R                  1 bytes    0x7ffeefbff3ff
idade       30                 4 bytes    0x7ffeefbff3f8
altura      1.82               4 bytes    0x7ffeefbff3f4
saldo       15750.50           8 bytes    0x7ffeefbff3e8
cpf         12345678901        8 bytes    0x7ffeefbff3e0
```

---

## Exercício 3 — Overflow Explorer (Intermediário)

### Enunciado

Crie um programa `overflow.c` que demonstre overflow em diferentes tipos:

1. Declare um `char` com valor 127 (CHAR_MAX), some 1 e imprima
2. Declare um `int` com valor INT_MAX, some 1 e imprima
3. Declare um `unsigned char` com valor 255, some 1 e imprima
4. Declare um `unsigned int` com valor UINT_MAX, some 1 e imprima

Para cada caso, imprima o valor antes e depois da soma, e adicione um comentário explicando o que aconteceu.

### Exemplo de saída esperada

```
=== Overflow em char ===
Antes: 127
Depois: -128 (deu a volta para o minimo!)

=== Overflow em int ===
Antes: 2147483647
Depois: -2147483648 (deu a volta para o minimo!)

=== Overflow em unsigned char ===
Antes: 255
Depois: 0 (deu a volta para zero!)

=== Overflow em unsigned int ===
Antes: 4294967295
Depois: 0 (deu a volta para zero!)
```

### Dicas

- Inclua `<limits.h>` para usar CHAR_MAX, INT_MAX, UINT_MAX
- Para unsigned int, use `%u` no printf
- O compilador pode dar warnings sobre overflow — isso é esperado

---

## Exercício 4 — Precisão de Float vs Double (Intermediário)

### Enunciado

Crie um programa `precisao.c` que demonstre a diferença de precisão entre `float` e `double`:

1. Calcule `1.0 / 3.0` com float e com double, imprima com 20 casas decimais
2. Calcule `1.0 / 7.0` com float e com double, imprima com 20 casas decimais
3. Some `0.1` cem vezes com float e com double, compare com 10.0
4. Some `0.01` mil vezes com float e com double, compare com 10.0

Para cada caso, mostre a diferença entre o valor obtido e o valor esperado.

### Exemplo de saída esperada

```
=== 1/3 ===
float:  0.33333334326744079590
double: 0.33333333333333331483

=== 1/7 ===
float:  0.14285714924335479736
double: 0.14285714285714284921

=== Somando 0.1 cem vezes (esperado: 10.0) ===
float:  10.0000009537 (erro: 0.0000009537)
double: 9.9999999999 (erro: 0.0000000001)

=== Somando 0.01 mil vezes (esperado: 10.0) ===
float:  10.0000476837 (erro: 0.0000476837)
double: 10.0000000000 (erro: 0.0000000000)
```

### Dicas

- Use `%.20f` para ver muitas casas decimais
- Para calcular o erro, use a função `fabs()` de `<math.h>` (valor absoluto para float)
- Compile com `-lm` para usar math.h: `gcc -Wall -lm precisao.c -o precisao`

---

## Exercício 5 — Conversão de Tipos (Intermediário)

### Enunciado

Crie um programa `conversao.c` que demonstre diferentes conversões de tipo:

1. Divida 7 por 2 de três formas: `int/int`, `float/int`, `(float)int/int`
2. Converta a temperatura 98.6°F para Celsius: `C = (F - 32) * 5 / 9` — faça com int e com float, mostre a diferença
3. Converta o caractere '7' para o número 7 (dica: `'7' - '0'`)
4. Converta o número 65 para o caractere correspondente na tabela ASCII

### Exemplo de saída esperada

```
=== Divisao 7/2 ===
int/int:           3
float/int:         3.50
(float)int/int:    3.50

=== Temperatura 98.6F para Celsius ===
Com int:    33 (impreciso!)
Com float:  37.00 (correto)

=== Char para numero ===
Caractere '7' = numero 7

=== Numero para char ===
Numero 65 = caractere 'A'
```

---

## Exercício 6 — Tabela ASCII (Intermediário)

### Enunciado

Crie um programa `ascii.c` que imprima a tabela ASCII dos caracteres imprimíveis (32 a 126). Para cada caractere, mostre:
- O código decimal
- O código hexadecimal
- O caractere

Organize em colunas para facilitar a leitura (4 colunas por linha).

### Exemplo de saída esperada

```
=== Tabela ASCII (caracteres imprimiveis) ===
 32 0x20 ' '    33 0x21 '!'    34 0x22 '"'    35 0x23 '#'
 36 0x24 '$'    37 0x25 '%'    38 0x26 '&'    39 0x27 '''
 40 0x28 '('    41 0x29 ')'    42 0x2a '*'    43 0x2b '+'
...
```

### Dicas

- Use um loop de 32 a 126
- Use `%3d` para decimal alinhado, `0x%02x` para hexadecimal, `'%c'` para o caractere
- Para organizar em 4 colunas, use `if (i % 4 == 3) printf("\n");`

---

## Exercício 7 — Calculadora de Memória (Avançado)

### Enunciado

Crie um programa `calc_memoria.c` que funcione como uma calculadora de uso de memória. O programa deve:

1. Perguntar quantas variáveis de cada tipo o usuário quer criar:
   - Quantos char?
   - Quantos int?
   - Quantos float?
   - Quantos double?
   - Quantos long?

2. Calcular e mostrar:
   - Memória total usada por cada tipo
   - Memória total de todas as variáveis
   - Porcentagem de uso em relação a 2KB (memória de um Arduino Uno)

### Exemplo de saída esperada

```
=== Calculadora de Memoria ===
Quantos char? 100
Quantos int? 50
Quantos float? 20
Quantos double? 10
Quantos long? 5

=== Resultado ===
100 char   x 1 byte  = 100 bytes
50  int    x 4 bytes = 200 bytes
20  float  x 4 bytes = 80 bytes
10  double x 8 bytes = 80 bytes
5   long   x 8 bytes = 40 bytes
---------------------------------
Total: 500 bytes

Em um Arduino Uno (2048 bytes):
Uso: 24.4% da memoria disponivel
Restante: 1548 bytes livres
```

---

## Exercício 8 — Trace de Memória (Avançado)

### Enunciado

Sem executar o programa abaixo, desenhe o estado da memória após cada linha marcada com `// TRACE`. Depois execute e compare com suas previsões.

```c
#include <stdio.h>

int main() {
    int a = 10;          // TRACE 1: qual o valor de a?
    int b = 20;          // TRACE 2: quais os valores de a e b?
    int c = a + b;       // TRACE 3: quais os valores de a, b e c?

    a = c - b;           // TRACE 4: qual o novo valor de a?
    b = a * 2;           // TRACE 5: qual o novo valor de b?
    c = a + b + c;       // TRACE 6: qual o novo valor de c?

    printf("a=%d, b=%d, c=%d\n", a, b, c);

    return 0;
}
```

### Formato da resposta

```
TRACE 1: a=10
TRACE 2: a=10, b=20
TRACE 3: a=10, b=20, c=30
TRACE 4: a=?, b=20, c=30
TRACE 5: a=?, b=?, c=30
TRACE 6: a=?, b=?, c=?
```

Preencha os `?` antes de executar o programa.

---

## Exercício 9 — Variáveis Não Inicializadas (Avançado)

### Enunciado

Crie um programa `lixo_memoria.c` que:

1. Declare 5 variáveis `int` SEM inicializar
2. Imprima o valor de cada uma (será lixo)
3. Execute o programa 3 vezes e anote os valores
4. Nos comentários, responda: os valores foram iguais nas 3 execuções? Por quê?

Depois, modifique o programa para inicializar todas as variáveis com 0 e execute novamente.

### Dicas

- Compile com `gcc -Wall` — o compilador vai avisar sobre variáveis não inicializadas
- Os valores de lixo podem ser diferentes a cada execução por causa do ASLR e do estado da memória

---

## Gabarito Parcial

### Exercício 3 — Overflow

```c
// overflow.c — Demonstracao de overflow
#include <stdio.h>
#include <limits.h>

int main() {
    // Overflow em char (signed)
    char c = CHAR_MAX;  // 127
    printf("=== Overflow em char ===\n");
    printf("Antes: %d\n", c);
    c = c + 1;  // 127 + 1 = -128 (overflow!)
    printf("Depois: %d (deu a volta para o minimo!)\n\n", c);

    // Overflow em int (signed)
    int i = INT_MAX;  // 2147483647
    printf("=== Overflow em int ===\n");
    printf("Antes: %d\n", i);
    i = i + 1;  // Overflow!
    printf("Depois: %d (deu a volta para o minimo!)\n\n", i);

    // Overflow em unsigned char
    unsigned char uc = 255;
    printf("=== Overflow em unsigned char ===\n");
    printf("Antes: %u\n", uc);
    uc = uc + 1;  // 255 + 1 = 0 (volta para zero)
    printf("Depois: %u (deu a volta para zero!)\n\n", uc);

    // Overflow em unsigned int
    unsigned int ui = UINT_MAX;  // 4294967295
    printf("=== Overflow em unsigned int ===\n");
    printf("Antes: %u\n", ui);
    ui = ui + 1;  // Overflow!
    printf("Depois: %u (deu a volta para zero!)\n", ui);

    return 0;
}
```

### Exercício 8 — Trace

```
TRACE 1: a=10
TRACE 2: a=10, b=20
TRACE 3: a=10, b=20, c=30
TRACE 4: a=10 (c-b = 30-20), b=20, c=30
TRACE 5: a=10, b=20 (a*2 = 10*2), c=30
TRACE 6: a=10, b=20, c=60 (a+b+c = 10+20+30)
Saida: a=10, b=20, c=60
```

---

[← Voltar ao conteúdo: Variáveis e Memória](cap07-mod03-variaveis-memoria-c-conteudo.md) · [Próximo: Ponteiros →](cap07-mod04-ponteiros-conteudo.md)
