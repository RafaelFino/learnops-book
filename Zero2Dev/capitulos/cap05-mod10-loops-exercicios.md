# 5.10 — Exercícios: Loops: for e while

[← Voltar ao conteúdo do módulo](cap05-mod10-loops-conteudo.md)

---

## Orientações

- Resolva cada exercício em um arquivo separado (ex: `exercicio_10_01.py`)
- Execute e teste antes de passar para o próximo
- Use `print()` para verificar o que está acontecendo a cada iteração
- Se travar, releia a seção correspondente do módulo

---

## Exercício 1 — Contagem de 1 a 20

Crie um programa que exibe os números de 1 a 20, um por linha, usando `for` com `range()`.

**Dica:** Lembre-se que `range(1, 21)` gera de 1 a 20.

**Saída esperada:**
```
1
2
3
...
20
```

---

## Exercício 2 — Soma dos Pares

Crie um programa que soma todos os números pares de 1 a 100 usando um loop `for` e um acumulador.

**Dica:** Use `if number % 2 == 0` para verificar se é par, ou use `range(2, 101, 2)` para gerar apenas pares.

**Saída esperada:**
```
Soma dos pares de 1 a 100: 2550
```

---

## Exercício 3 — Tabuada de um Número

Crie um programa que pede um número ao usuário e exibe a tabuada completa (de 1 a 10) desse número.

**Dica:** Use `for i in range(1, 11)` e multiplique pelo número informado.

**Exemplo de saída (se o usuário digitar 7):**
```
Tabuada do 7:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
```

---

## Exercício 4 — Contagem Regressiva

Crie um programa que pede um número ao usuário e faz uma contagem regressiva até zero.

**Dica:** Use `range(número, -1, -1)` ou um `while`.

**Exemplo de saída (se o usuário digitar 5):**
```
5
4
3
2
1
0
Fim!
```

---

## Exercício 5 — Validação de Senha

Crie um programa que pede uma senha ao usuário. A senha correta é "python123". O programa deve continuar pedindo até o usuário acertar. Use `while`.

**Dica:** Use o padrão `while True` com `break` quando a senha estiver correta.

**Exemplo de saída:**
```
Digite a senha: abc
Senha incorreta! Tente novamente.
Digite a senha: 123
Senha incorreta! Tente novamente.
Digite a senha: python123
Senha correta! Acesso liberado.
```

---

## Exercício 6 — Calculadora Repetitiva

Crie um programa com `while True` que:
1. Pede dois números ao usuário
2. Pede uma operação (+, -, *, /)
3. Mostra o resultado
4. Pergunta se quer continuar (s/n)
5. Se o usuário digitar "n", encerra

**Dica:** Use `break` quando o usuário digitar "n". Trate divisão por zero.

---

## Exercício 7 — Maior e Menor

Crie um programa que pede 5 números ao usuário (um por vez, usando `for`) e no final mostra qual foi o maior e o menor número digitado.

**Dica:** Use o padrão de maior/menor valor do módulo. Inicialize `biggest` e `smallest` com o primeiro número digitado.

**Exemplo de saída:**
```
Digite o numero 1: 45
Digite o numero 2: 12
Digite o numero 3: 78
Digite o numero 4: 3
Digite o numero 5: 56
Maior: 78
Menor: 3
```

---

## Exercício 8 — Triângulo Invertido

Crie um programa que desenha um triângulo invertido de asteriscos com 7 linhas:

**Saída esperada:**
```
*******
******
*****
****
***
**
*
```

**Dica:** Use `"*" * n` para repetir o caractere. O número de asteriscos diminui a cada linha.

---

## Exercício 9 — Fibonacci

Os primeiros números da sequência de Fibonacci são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

Cada número é a soma dos dois anteriores. Crie um programa que exibe os primeiros 15 números da sequência usando um loop.

**Dica:** Use duas variáveis (`a` e `b`) e a cada iteração faça: `a, b = b, a + b`.

**Saída esperada:**
```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

---

## Exercício 10 — Menu Interativo

Crie um programa com um menu que oferece 4 opções:
1. Somar dois números
2. Verificar se um número é par ou ímpar
3. Exibir tabuada de um número
4. Sair

O programa deve repetir o menu até o usuário escolher "Sair". Use `while True` e `if/elif/else` para as opções.

**Dica:** Combine tudo que você aprendeu: loops, condicionais, input, operadores.

---

## Desafio Extra — Números Primos

Um número primo é divisível apenas por 1 e por ele mesmo. Crie um programa que exibe todos os números primos de 2 a 50.

**Dica:** Para cada número, use um loop interno para verificar se ele é divisível por algum número entre 2 e ele mesmo. Se não for divisível por nenhum, é primo. Use uma variável `is_prime` (é primo) como flag.

**Saída esperada:**
```
Numeros primos de 2 a 50:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
```


### Dicas Gerais para os Exercícios

- Comece pelo exercício mais simples e avance gradualmente
- Teste cada parte do código separadamente antes de juntar tudo
- Use `print()` para verificar valores intermediários quando algo não funcionar
- Releia o enunciado se o resultado não for o esperado — às vezes o problema está na interpretação
- Não tenha medo de errar — cada erro é uma oportunidade de aprender como Python funciona

### Tabela de Referência Rápida

| Conceito | Exemplo | Resultado |
|----------|---------|-----------|
| Criar variável | `x = 10` | x vale 10 |
| Ler entrada | `nome = input("Nome: ")` | Espera digitação |
| Converter para inteiro | `int("42")` | 42 |
| Converter para decimal | `float("3.14")` | 3.14 |
| Converter para texto | `str(42)` | "42" |
| Formatar com f-string | `f"Valor: {x}"` | "Valor: 10" |
| Formatar decimais | `f"{x:.2f}"` | "10.00" |


---

[← Voltar ao conteúdo do módulo](cap05-mod10-loops-conteudo.md)
