# 5.11 — Exercícios: Funções

[← Voltar ao conteúdo do módulo](cap05-mod11-funcoes-conteudo.md)

---

## Orientações

- Resolva cada exercício em um arquivo separado (ex: `exercicio_11_01.py`)
- Defina as funções no início do arquivo e o programa principal no final
- Teste cada função individualmente antes de integrá-las
- Use nomes descritivos para suas funções (comece com verbo)

---

## Exercício 1 — Saudação Personalizada

Crie uma função `greet(name)` que recebe um nome e exibe uma saudação. Crie outra função `greet_formal(name, title)` com um parâmetro `title` (título) com valor padrão "Sr./Sra.". Teste ambas.

**Saída esperada:**
```
Ola, Maria! Bem-vindo(a)!
Ola, Sr./Sra. Carlos! Bem-vindo(a)!
Ola, Dr. Ana! Bem-vindo(a)!
```

---

## Exercício 2 — Calculadora com Funções

Crie 4 funções: `add(a, b)`, `subtract(a, b)`, `multiply(a, b)`, `divide(a, b)`. Cada uma retorna o resultado da operação. A função `divide` deve retornar "Erro: divisao por zero" se `b` for 0. Crie um menu interativo com `while True`.

---

## Exercício 3 — Conversor de Temperatura

Crie duas funções:
- `celsius_to_fahrenheit(celsius)` — converte Celsius para Fahrenheit (F = C * 9/5 + 32)
- `fahrenheit_to_celsius(fahrenheit)` — converte Fahrenheit para Celsius (C = (F - 32) * 5/9)

Crie um menu que permite ao usuário escolher a conversão e digitar o valor.

---

## Exercício 4 — Validador de Dados

Crie as seguintes funções de validação:
- `validate_name(name)` — retorna True se o nome tem pelo menos 2 caracteres
- `validate_age(age)` — retorna True se a idade está entre 0 e 150
- `validate_email(email)` — retorna True se contém "@" e "."

Use as três funções em um programa de cadastro que pede nome, idade e e-mail, validando cada campo.

---

## Exercício 5 — Fatorial

Crie uma função `factorial(n)` que calcula o fatorial de um número usando um loop `for`. O fatorial de 5 é: 5 x 4 x 3 x 2 x 1 = 120. O fatorial de 0 é 1.

**Saída esperada:**
```
Fatorial de 0: 1
Fatorial de 5: 120
Fatorial de 10: 3628800
```

---

## Exercício 6 — Números Primos com Função

Crie uma função `is_prime(number)` que retorna True se o número é primo e False caso contrário. Use essa função em um loop para exibir todos os primos de 2 a 100.

**Dica:** Um número é primo se não é divisível por nenhum número entre 2 e sua raiz quadrada. Para simplificar, verifique divisibilidade de 2 até `number - 1`.

---

## Exercício 7 — Jogo de Adivinhação Organizado

Refatore o jogo de adivinhação do módulo 5.10 usando funções:
- `get_guess()` — pede e válida o palpite do usuário
- `check_guess(guess, secret)` — compara e retorna "alto", "baixo" ou "correto"
- `play_game()` — função principal que controla o jogo

---

## Exercício 8 — Relatório de Notas

Crie um programa que:
1. Pede o nome e 3 notas de 5 alunos (use um loop)
2. Para cada aluno, calcula a média usando uma função `calculate_average()`
3. Determina a situação usando uma função `get_status()`
4. No final, exibe um relatório com todos os alunos

---

## Desafio Extra — Mini Biblioteca de Matemática

Crie um arquivo com as seguintes funções:
- `is_even(n)` — retorna True se par
- `is_odd(n)` — retorna True se ímpar
- `absolute(n)` — retorna o valor absoluto (sem usar `abs()`)
- `power(base, exp)` — calcula potência usando loop (sem usar `**`)
- `gcd(a, b)` — calcula o maior divisor comum (MDC) usando o algoritmo de Euclides

Teste todas as funções com diferentes valores.



---

## Exercicio 7 — Funcao com Multiplos Retornos — Nivel: Intermediario

### Enunciado

Crie uma funcao `analyze_numbers(numbers)` que recebe uma lista de numeros e retorna uma tupla com: (menor, maior, media, soma, quantidade). Teste com pelo menos 3 listas diferentes.

### Dicas

1. Use `min()` e `max()` para menor e maior
2. Use `sum()` e `len()` para soma e quantidade
3. Media = soma / quantidade
4. Retorne tudo como tupla: `return (menor, maior, media, soma, qtd)`

### Proposta de Teste

- **Caso basico:** `[10, 20, 30]` -> (10, 30, 20.0, 60, 3)
- **Caso de borda:** `[5]` -> (5, 5, 5.0, 5, 1)
- **Caso de borda:** Lista vazia -> tratar com mensagem de erro

---

## Exercicio 8 — Funcao como Parametro — Nivel: Avancado

### Enunciado

Crie uma funcao `apply_to_list(numbers, operation)` que recebe uma lista e uma funcao, e retorna uma nova lista com a funcao aplicada a cada elemento. Teste com funcoes que dobram, triplicam e calculam o quadrado.

### Dicas

1. `operation` e uma funcao passada como parametro
2. Crie funcoes simples: `def double(x): return x * 2`
3. Use um loop para aplicar a funcao a cada elemento
4. Retorne a nova lista

### Proposta de Teste

- **Caso basico:** `apply_to_list([1, 2, 3], double)` -> [2, 4, 6]
- **Caso basico:** `apply_to_list([1, 2, 3], square)` -> [1, 4, 9]


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


### Exercício Extra: Funções com Valor Padrão

Crie uma função que calcule o preço com desconto, usando valor padrão para o percentual:

```python
# "calculate_discount" = calcular desconto
def calculate_discount(price, discount_percent=10):
    """Calcula preco com desconto. Padrao: 10%."""
    # "discount_value" = valor do desconto
    discount_value = price * discount_percent / 100
    # "final_price" = preco final
    final_price = price - discount_value
    return final_price

# Testar com desconto padrao (10%)
print(f"R$ 100 com desconto padrao: R$ {calculate_discount(100):.2f}")

# Testar com desconto especifico (25%)
print(f"R$ 100 com 25% desconto: R$ {calculate_discount(100, 25):.2f}")

# Testar com desconto zero
print(f"R$ 100 sem desconto: R$ {calculate_discount(100, 0):.2f}")
```

Saída esperada:

```
R$ 100 com desconto padrao: R$ 90.00
R$ 100 com 25% desconto: R$ 75.00
R$ 100 sem desconto: R$ 100.00
```

**Dica:** Parâmetros com valor padrão (`discount_percent=10`) permitem chamar a função sem passar aquele argumento. Isso torna a função mais flexível.

### Erros Comuns com Funções

| Erro | Causa | Solução |
|------|-------|---------|
| `TypeError: missing argument` | Chamou função sem argumento obrigatório | Passar todos os argumentos necessários |
| Função retorna `None` | Esqueceu o `return` | Adicionar `return valor` |
| Variável não existe fora da função | Escopo local | Usar `return` para devolver o valor |
| Função não executa | Definiu mas não chamou | Adicionar `nome_funcao()` após a definição |

---

[← Voltar ao conteúdo do módulo](cap05-mod11-funcoes-conteudo.md)
