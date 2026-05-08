# 7.2 — Exercícios: Ambiente C

[← Voltar ao conteúdo: Ambiente C](cap07-mod02-ambiente-c-conteudo.md)

---

## Sobre Estes Exercícios

Agora sim vamos escrever código em C. Para cada exercício:

1. Crie o arquivo `.c` na pasta `~/meus-projetos/curso/cap07/`
2. Compile com `gcc -Wall arquivo.c -o arquivo`
3. Execute com `./arquivo`
4. Se der erro de compilação, leia a mensagem com atenção — ela indica a linha e o tipo do problema

Lembre-se: sempre compile com `-Wall` para ver todos os avisos.

---

## Exercício 1 — Cartão de Visita (Básico)

### Enunciado

Crie um programa `cartao.c` que imprima um cartão de visita formatado com:
- Seu nome
- Sua idade (como inteiro)
- Sua altura (como float, com 2 casas decimais)
- Sua linguagem de programação favorita

Use variáveis para todos os dados (não coloque os valores diretamente no printf).

### Exemplo de saída esperada

```
================================
       CARTAO DE VISITA
================================
Nome:      Maria Silva
Idade:     25 anos
Altura:    1.68 metros
Linguagem: Python
================================
```

### Dicas

- Use `char nome[] = "Maria Silva";` para strings
- Use `%s` para imprimir strings, `%d` para inteiros, `%.2f` para floats
- Use `\n` para quebras de linha

---

## Exercício 2 — Conversor de Temperatura (Básico)

### Enunciado

Crie um programa `temperatura.c` que:
1. Peça ao usuário uma temperatura em Celsius
2. Converta para Fahrenheit usando a fórmula: `F = C * 9.0 / 5.0 + 32.0`
3. Converta para Kelvin usando a fórmula: `K = C + 273.15`
4. Imprima as três temperaturas com 1 casa decimal

### Exemplo de saída esperada

```
Digite a temperatura em Celsius: 100
100.0 C = 212.0 F = 373.1 K
```

### Dicas

- Use `float` para todas as variáveis de temperatura
- Use `%.1f` para imprimir com 1 casa decimal
- Cuidado: `9/5` em C resulta em `1` (divisão inteira). Use `9.0/5.0` para divisão decimal

---

## Exercício 3 — Calculadora de IMC (Intermediário)

### Enunciado

Crie um programa `imc.c` que:
1. Peça o peso em kg (float) e a altura em metros (float)
2. Calcule o IMC: `IMC = peso / (altura * altura)`
3. Classifique o resultado usando if/else:
   - Abaixo de 18.5: "Abaixo do peso"
   - 18.5 a 24.9: "Peso normal"
   - 25.0 a 29.9: "Sobrepeso"
   - 30.0 ou mais: "Obesidade"
4. Imprima o IMC com 1 casa decimal e a classificação

### Exemplo de saída esperada

```
Digite seu peso (kg): 70
Digite sua altura (m): 1.75

Seu IMC: 22.9
Classificacao: Peso normal
```

### Dicas

- Use `&&` para combinar condições: `if (imc >= 18.5 && imc <= 24.9)`
- Lembre que em C, comparações usam `>=` e `<=` (igual a Python)

---

## Exercício 4 — Tabuada (Intermediário)

### Enunciado

Crie um programa `tabuada.c` que:
1. Peça ao usuário um número inteiro
2. Imprima a tabuada desse número de 1 a 10
3. Use um loop `for`

### Exemplo de saída esperada

```
Digite um numero: 7

Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

### Dicas

- O loop `for` em C: `for (int i = 1; i <= 10; i++)`
- Use `%d` para imprimir inteiros

---

## Exercício 5 — Contador de Pares e Ímpares (Intermediário)

### Enunciado

Crie um programa `pares_impares.c` que:
1. Peça ao usuário quantos números ele quer digitar
2. Leia cada número usando um loop
3. Conte quantos são pares e quantos são ímpares
4. No final, imprima os totais

### Exemplo de saída esperada

```
Quantos numeros voce quer digitar? 5
Digite o numero 1: 10
Digite o numero 2: 7
Digite o numero 3: 4
Digite o numero 4: 3
Digite o numero 5: 8

Pares: 3
Impares: 2
```

### Dicas

- Use o operador `%` (módulo) para verificar se é par: `if (número % 2 == 0)`
- Declare contadores: `int pares = 0, impares = 0;`

---

## Exercício 6 — Fatorial (Intermediário)

### Enunciado

Crie um programa `fatorial.c` que:
1. Peça ao usuário um número inteiro positivo
2. Calcule o fatorial desse número (n! = n * (n-1) * ... * 1)
3. Imprima o resultado

Lembre: 0! = 1 e 1! = 1.

### Exemplo de saída esperada

```
Digite um numero: 5
5! = 120
```

### Dicas

- Use um loop `for` decrescente: `for (int i = n; i > 1; i--)`
- Ou crescente: `for (int i = 1; i <= n; i++)`
- Use `long` em vez de `int` para o resultado (fatoriais crescem rápido)
- Teste com números pequenos primeiro (3! = 6, 4! = 24, 5! = 120)

---

## Exercício 7 — Funções: Área de Figuras (Avançado)

### Enunciado

Crie um programa `areas.c` com funções separadas para calcular:
1. Área do quadrado: `lado * lado`
2. Área do retângulo: `base * altura`
3. Área do triângulo: `base * altura / 2`
4. Área do círculo: `3.14159 * raio * raio`

O programa deve:
- Ter uma função para cada cálculo (4 funções)
- Mostrar um menu para o usuário escolher a figura
- Pedir as medidas necessárias
- Chamar a função correspondente e imprimir o resultado

### Exemplo de saída esperada

```
Calculadora de Areas
1 - Quadrado
2 - Retangulo
3 - Triangulo
4 - Circulo
Escolha: 4

Digite o raio: 5
Area do circulo: 78.54
```

### Dicas

- Declare os protótipos das funções antes de `main`
- Cada função recebe os parâmetros necessários e retorna um `float`
- Use `switch` ou `if/else if` para o menu

---

## Exercício 8 — Conversor Python para C (Desafio)

### Enunciado

Pegue o programa abaixo em Python e reescreva em C:

```python
# Programa que encontra o maior e o menor numero de uma lista
numeros = []
quantidade = int(input("Quantos numeros? "))

for i in range(quantidade):
    num = int(input(f"Numero {i + 1}: "))
    numeros.append(num)

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Diferenca: {maior - menor}")
```

### Dicas

- Em C, use um array de tamanho fixo: `int números[100];` (limite de 100 números)
- Leia a quantidade primeiro, depois use um loop para ler cada número
- Use dois loops: um para ler e outro para encontrar maior/menor (ou faça tudo em um loop só)
- Não se preocupe com o `append` — em C, você acessa posições do array diretamente: `números[i] = valor;`

---

## Exercício 9 — Depuração: Encontre os Erros (Desafio)

### Enunciado

O programa abaixo tem 6 erros. Encontre e corrija todos:

```c
#include <stdio.h>

int main() {
    int idade
    float altura = 1.75

    printf("Digite sua idade: ")
    scanf("%d", idade);

    printf("Idade: %f\n", idade);
    printf("Altura: %d\n", altura);

    if idade >= 18 {
        printf("Maior de idade\n")
    }

    return 0
}
```

### Dicas

- Compile com `gcc -Wall` e leia as mensagens de erro uma por uma
- Os erros incluem: ponto e vírgula faltando, `&` faltando no scanf, códigos de formato errados, parênteses faltando no if
- Corrija um erro por vez e recompile — às vezes um erro causa mensagens de erro em cascata

---

## Gabarito Parcial

### Exercício 2 — Conversor de Temperatura

```c
// temperatura.c — Conversor de temperatura
#include <stdio.h>

int main() {
    float celsius, fahrenheit, kelvin;

    printf("Digite a temperatura em Celsius: ");
    scanf("%f", &celsius);

    fahrenheit = celsius * 9.0 / 5.0 + 32.0;
    kelvin = celsius + 273.15;

    printf("%.1f C = %.1f F = %.1f K\n", celsius, fahrenheit, kelvin);

    return 0;
}
```

### Exercício 9 — Erros Corrigidos

Os 6 erros são:
1. Linha 4: falta `;` depois de `int idade`
2. Linha 5: falta `;` depois de `float altura = 1.75`
3. Linha 8: falta `&` no scanf: `scanf("%d", &idade);`
4. Linha 10: código errado — `%f` deveria ser `%d` para int
5. Linha 11: código errado — `%d` deveria ser `%.2f` para float
6. Linha 13: falta `()` na condição do if: `if (idade >= 18)`
7. Linha 14: falta `;` depois do printf
8. Linha 17: falta `;` depois de `return 0`

(Na verdade são 8 erros — bônus para quem encontrou todos.)

---

[← Voltar ao conteúdo: Ambiente C](cap07-mod02-ambiente-c-conteudo.md) · [Próximo: Variáveis e Memória em C →](cap07-mod03-variaveis-memoria-c-conteudo.md)
