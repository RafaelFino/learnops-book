# 06 — Entrada e Saída de Dados: input() e print()

[← Anterior: História do Python](05-historia-python.md) · [Glossário](00-glossario.md) · [Próximo: Variáveis e Tipos Básicos →](07-variaveis-tipos.md)

---

## Introdução

Agora que seu ambiente está pronto, vamos começar a programar de verdade!

Neste módulo, você vai aprender as duas funções mais básicas e importantes do Python:

- **`print()`** — faz o programa "falar" com você, exibindo informações na tela
- **`input()`** — faz o programa "ouvir" você, recebendo dados que você digita

Pense assim: `print()` é a boca do programa (ele fala) e `input()` é o ouvido (ele escuta). Com essas duas funções, seus programas já conseguem conversar com você!

> **Dica:** Termos novos? Consulte o [Glossário](00-glossario.md) a qualquer momento.

---

## Como Executar os Exemplos Deste Módulo

Este é o primeiro módulo com código para executar! Aqui vai um lembrete rápido:

1. Copie o código de exemplo
2. Abra o VSCode e cole em um novo arquivo
3. Salve com extensão `.py` (exemplo: `exemplo_print.py`)
4. Abra o terminal (`Ctrl + Alt + T`)
5. Navegue até a pasta onde salvou: `cd ~/meus-projetos/python-curso/modulo-06`
6. Execute: `python3 exemplo_print.py`

> **Dica:** Se precisar de mais detalhes, consulte o [Módulo 03 — Preparação do Ambiente](03-preparacao-ambiente.md) e o [Módulo 04 — Execução e Pastas](04-execucao-permissoes-pastas.md).

---

## A Função print() — Exibindo Dados no Terminal

A função [print()](00-glossario-j-p.md#print) exibe informações no terminal. É a forma mais simples de fazer o programa mostrar algo para você.

### Uso básico

```python
# print() exibe o texto entre aspas no terminal
# "Hello, World!" = "Olá, Mundo!" — é a tradição do primeiro programa
print("Olá, mundo!")
```

**Saída esperada:**
```
Olá, mundo!
```

> **Nota:** O texto entre aspas é chamado de **string** (texto). Pode usar aspas simples `'texto'` ou duplas `"texto"` — ambas funcionam.

### Exibindo números

```python
# print() também exibe números sem aspas
print(42)
print(3.14)
```

**Saída esperada:**
```
42
3.14
```

### Exibindo múltiplos valores

Você pode passar vários valores para `print()`, separados por vírgula:

```python
# Exibindo nome e idade juntos
# "name" = nome, "age" = idade
name = "Maria"
age = 25
print("Nome:", name, "- Idade:", age)
```

**Saída esperada:**
```
Nome: Maria - Idade: 25
```

> **Nota:** O `print()` automaticamente coloca um **espaço** entre cada valor separado por vírgula.

### O parâmetro `sep` — Alterando o separador

Por padrão, `print()` separa os valores com espaço. O parâmetro `sep` ("separator" = separador) permite mudar isso:

```python
# Usando sep para mudar o separador entre valores
# "sep" = separator = separador
print("Python", "é", "incrível", sep="-")
print("01", "01", "2025", sep="/")
print("Maria", "25", "São Paulo", sep=" | ")
```

**Saída esperada:**
```
Python-é-incrível
01/01/2025
Maria | 25 | São Paulo
```

### O parâmetro `end` — Alterando o final da linha

Por padrão, `print()` pula para a próxima linha depois de exibir. O parâmetro `end` ("end" = fim) permite mudar isso:

```python
# Sem end: cada print vai para uma nova linha
print("Olá")
print("Mundo")
```

**Saída esperada:**
```
Olá
Mundo
```

```python
# Com end: controlamos o que aparece no final
# end=" " coloca um espaço em vez de pular linha
print("Olá", end=" ")
print("Mundo")
```

**Saída esperada:**
```
Olá Mundo
```

```python
# end="..." coloca reticências no final
print("Carregando", end="...")
print("Pronto!")
```

**Saída esperada:**
```
Carregando...Pronto!
```

### Formatando tabelas simples

Você pode usar `print()` para criar saídas organizadas como tabelas:

```python
# Criando uma tabela simples de produtos
# "product" = produto, "price" = preço
print("Produto", "Preço", sep="\t")  # \t = tabulação (tab)
print("-------", "-----", sep="\t")
print("Arroz", "R$ 5.99", sep="\t")
print("Feijão", "R$ 8.50", sep="\t")
print("Macarrão", "R$ 3.75", sep="\t")
```

**Saída esperada:**
```
Produto	Preço
-------	-----
Arroz	R$ 5.99
Feijão	R$ 8.50
Macarrão	R$ 3.75
```

> **Nota:** `\t` é um caractere especial que representa uma **tabulação** (tab) — um espaçamento maior que ajuda a alinhar colunas.

---

## A Função input() — Recebendo Dados do Usuário

A função [input()](00-glossario-e-i.md#input) faz o programa parar e esperar que o usuário digite algo no terminal. O valor digitado é capturado e pode ser guardado em uma variável.

### Uso básico

```python
# input() exibe a mensagem e espera o usuário digitar
# "name" = nome
name = input("Digite seu nome: ")

# Exibe o nome que o usuário digitou
print("Olá,", name)
```

**Como funciona:**
1. O programa exibe "Digite seu nome: " e espera
2. O usuário digita algo (por exemplo: `Maria`) e pressiona Enter
3. O valor digitado é guardado na variável `name`
4. O programa exibe "Olá, Maria"

**Saída esperada (se o usuário digitar "Maria"):**
```
Digite seu nome: Maria
Olá, Maria
```

### IMPORTANTE: input() sempre retorna uma string!

Mesmo que o usuário digite um número, o `input()` retorna o valor como **texto (string)**, não como número. Isso é muito importante:

```python
# O usuário digita 25, mas age recebe o TEXTO "25", não o número 25
# "age" = idade
age = input("Digite sua idade: ")

# Vamos verificar o tipo do valor
# type() mostra o tipo de dado
print("Valor:", age)
print("Tipo:", type(age))
```

**Saída esperada (se o usuário digitar "25"):**
```
Digite sua idade: 25
Valor: 25
Tipo: <class 'str'>
```

> **Nota:** `<class 'str'>` significa que o valor é uma **string** (texto). Mesmo parecendo um número, para o Python é texto!

### Convertendo input() para número

Para fazer cálculos com valores digitados pelo usuário, você precisa **converter** o texto para número:

```python
# int() converte texto para número inteiro
# "age" = idade
age = int(input("Digite sua idade: "))

# Agora age é um número e podemos fazer cálculos
# "birth_year" = ano de nascimento
birth_year = 2025 - age

print("Você nasceu aproximadamente em", birth_year)
```

**Saída esperada (se o usuário digitar "30"):**
```
Digite sua idade: 30
Você nasceu aproximadamente em 1995
```

```python
# float() converte texto para número decimal
# "price" = preço
price = float(input("Digite o preço do produto: R$ "))

# "quantity" = quantidade
quantity = int(input("Digite a quantidade: "))

# "total" = total
total = price * quantity

print("Total da compra: R$", total)
```

**Saída esperada (se digitar 5.99 e 3):**
```
Digite o preço do produto: R$ 5.99
Digite a quantidade: 3
Total da compra: R$ 17.97
```

> **Dica:** `int()` converte para número inteiro (sem decimais). `float()` converte para número decimal (com ponto). Vamos aprofundar isso no [Módulo 08 — Conversão de Tipos](08-conversao-tipos.md).

### O que acontece quando a conversão falha?

Se o usuário digitar algo que não é um número quando o programa espera um número, o Python vai mostrar um erro. Veja o que acontece:

```python
# Se o usuário digitar "abc" em vez de um número...
age = int(input("Digite sua idade: "))
```

**Se o usuário digitar "abc":**
```
Digite sua idade: abc
Traceback (most recent call last):
  File "exemplo.py", line 2, in <module>
    age = int(input("Digite sua idade: "))
ValueError: invalid literal for int() with base 10: 'abc'
```

> **Atenção:** Não se assuste com essa mensagem! Ela está dizendo: "Erro de Valor: não consegui converter 'abc' para número inteiro". Isso é normal e acontece quando o usuário digita algo inesperado. No [Módulo 18 — Tratamento de Erros](18-tratamento-erros.md), vamos aprender a lidar com essas situações para que o programa não pare.

---

## Exemplos Práticos: Programas Interativos

### Exemplo 1: Calculadora simples

```python
# Calculadora que soma dois números
# "first_number" = primeiro número
# "second_number" = segundo número
# "result" = resultado

# Lê os dois números do usuário e converte para decimal
first_number = float(input("Digite o primeiro número: "))
second_number = float(input("Digite o segundo número: "))

# Calcula a soma
result = first_number + second_number

# Exibe o resultado
print("A soma de", first_number, "+", second_number, "é:", result)
```

**Saída esperada (se digitar 10 e 5.5):**
```
Digite o primeiro número: 10
Digite o segundo número: 5.5
A soma de 10.0 + 5.5 é: 15.5
```

### Exemplo 2: Cadastro simples

```python
# Programa de cadastro que coleta informações do usuário
# "name" = nome, "age" = idade, "city" = cidade

print("=== Cadastro ===")
name = input("Nome completo: ")
# "age" = idade
# Aqui NÃO precisamos converter para int() porque vamos apenas EXIBIR a idade,
# não fazer cálculos com ela. Se fôssemos calcular algo, precisaríamos converter.
age = input("Idade: ")
city = input("Cidade: ")

print("\n=== Dados Cadastrados ===")  # \n = pula uma linha
print("Nome:", name)
print("Idade:", age, "anos")
print("Cidade:", city)
```

**Saída esperada:**
```
=== Cadastro ===
Nome completo: João Silva
Idade: 45
Cidade: São Paulo

=== Dados Cadastrados ===
Nome: João Silva
Idade: 45 anos
Cidade: São Paulo
```

> **Nota:** `\n` é um caractere especial que **pula uma linha**. É útil para separar visualmente as seções da saída.

### Exemplo 3: Conversor de temperatura

```python
# Converte temperatura de Celsius para Fahrenheit
# "celsius" = temperatura em Celsius
# "fahrenheit" = temperatura em Fahrenheit
# A fórmula é: F = C × 1.8 + 32

# Lê a temperatura em Celsius
celsius = float(input("Digite a temperatura em Celsius: "))

# Calcula a conversão
# Multiplicação: celsius vezes 1.8
# Soma: o resultado mais 32
fahrenheit = celsius * 1.8 + 32

# Exibe o resultado
print(celsius, "°C equivale a", fahrenheit, "°F")
```

**Saída esperada (se digitar 30):**
```
Digite a temperatura em Celsius: 30
30.0 °C equivale a 86.0 °F
```

---

## Resumo das Funções

| Função | O que faz | Exemplo |
|--------|-----------|---------|
| `print("texto")` | Exibe texto no terminal | `print("Olá")` |
| `print(a, b)` | Exibe múltiplos valores | `print("Nome:", nome)` |
| `print(a, sep="-")` | Muda o separador | `print("a", "b", sep="-")` |
| `print(a, end=" ")` | Muda o final da linha | `print("Olá", end=" ")` |
| `input("mensagem")` | Lê texto do usuário | `nome = input("Nome: ")` |
| `int(input(...))` | Lê número inteiro | `idade = int(input("Idade: "))` |
| `float(input(...))` | Lê número decimal | `preco = float(input("Preço: "))` |

---

## Para Saber Mais

-  [W3Schools — Python Output](https://www.w3schools.com/python/python_syntax.asp) — _Função print() e saída de dados_
-  [W3Schools — Python User Input](https://www.w3schools.com/python/python_user_input.asp) — _Função input() e entrada de dados_
-  [W3Schools — Python Print](https://www.w3schools.com/python/ref_func_print.asp) — _Referência completa do print()_
-  [Documentação Python — Funções Built-in](https://docs.python.org/pt-br/3/library/functions.html) — _Todas as funções embutidas_

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre aspas simples e duplas?**
R: Em Python, `'texto'` e `"texto"` são a mesma coisa. Use a que preferir. A vantagem de ter as duas é poder usar uma dentro da outra: `print("Ele disse 'olá'")`.

**P: O que acontece se eu esquecer as aspas no print?**
R: Se você escrever `print(Olá)` sem aspas, o Python vai pensar que `Olá` é o nome de uma variável e vai dar erro (`NameError`), porque essa variável não existe.

**P: Por que input() retorna sempre string?**
R: Porque o Python não tem como adivinhar se o que o usuário digitou é um número, um nome ou qualquer outra coisa. Ele trata tudo como texto e deixa você decidir o que fazer com o valor.

**P: O que acontece se eu tentar converter uma letra para int()?**
R: Vai dar erro! `int("abc")` gera um `ValueError` porque "abc" não é um número. Vamos aprender a tratar esses erros no módulo 18.

**P: Posso usar print() sem nada dentro?**
R: Sim! `print()` sem argumentos apenas pula uma linha em branco. É útil para separar visualmente partes da saída.

**P: O que é `\n`?**
R: É um caractere especial que representa uma "nova linha" (new line). Quando o Python encontra `\n` dentro de uma string, ele pula para a linha seguinte.

**P: O que é `\t`?**
R: É um caractere especial que representa uma "tabulação" (tab). Cria um espaçamento maior, útil para alinhar colunas em tabelas simples.

**P: Posso usar input() para ler mais de um valor de uma vez?**
R: Não diretamente. Cada `input()` lê um valor. Para ler vários, use vários `input()` em sequência, como nos exemplos de cadastro.

**P: O que é uma "variável"?**
R: É um nome que guarda um valor na memória do computador. Vamos aprofundar isso no próximo módulo (07). Por enquanto, pense nela como uma caixa etiquetada onde você guarda informações.

**P: Por que o resultado de float aparece com .0?**
R: Quando você converte um número inteiro para float (ou faz operações com float), o Python sempre mostra o ponto decimal. `10` vira `10.0`. Isso é normal.

**P: Posso misturar texto e números no print()?**
R: Sim! Basta separar por vírgula: `print("Idade:", 25)`. O print() aceita qualquer tipo de valor.

**P: O que é `type()`?**
R: É uma função que mostra o tipo de um valor. `type(42)` retorna `<class 'int'>` (inteiro), `type("olá")` retorna `<class 'str'>` (string). Útil para verificar se uma conversão funcionou.

**P: Posso usar acentos e caracteres especiais no print()?**
R: Sim! Python 3 suporta Unicode, então acentos (á, é, ã), cedilha (ç) e emojis funcionam normalmente.

**P: O que acontece se o usuário não digitar nada e apertar Enter?**
R: O `input()` retorna uma string vazia `""`. O programa continua normalmente, mas a variável terá um valor vazio.

**P: Como faço para o programa esperar antes de continuar?**
R: Você pode usar `input("Pressione Enter para continuar...")`. O programa vai parar e esperar o usuário pressionar Enter.

**P: O que é "concatenar"?**
R: É juntar textos. Você pode concatenar com `+`: `"Olá" + " " + "Mundo"` resulta em `"Olá Mundo"`. Mas usar `print()` com vírgulas é mais simples para exibir.

**P: Posso salvar o resultado do print() em uma variável?**
R: Não. `print()` apenas exibe na tela e retorna `None`. Para guardar um valor, use uma variável: `resultado = 2 + 3` e depois `print(resultado)`.

**P: O que é `end=""` (vazio)?**
R: `end=""` faz o print() não colocar nada no final — nem espaço, nem nova linha. O próximo print() continua na mesma linha, colado ao anterior.

**P: Posso usar f-strings com print()?**
R: Sim! f-strings são uma forma elegante de formatar texto: `print(f"Nome: {name}, Idade: {age}")`. Vamos aprender sobre elas no módulo 09.

**P: É normal achar confuso no início?**
R: Completamente normal! input() e print() parecem simples, mas têm muitos detalhes. Com prática, vai se tornar automático. Faça os exercícios e releia os exemplos quantas vezes precisar.

---

## Exercícios de Fixação

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

  **[Acessar Exercícios do Módulo 06](06-entrada-saida-exercicios.md)**

---

[← Anterior: História do Python](05-historia-python.md) · [Glossário](00-glossario.md) · [Próximo: Variáveis e Tipos Básicos →](07-variaveis-tipos.md)
