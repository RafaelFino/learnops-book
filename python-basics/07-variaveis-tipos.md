# 07 — Variáveis e Tipos Básicos

[<- Anterior: Entrada e Saida de Dados](06-entrada-saida.md) | [Glossário](00-glossario.md) | [Próximo: Conversão de Tipos ->](08-conversao-tipos.md)

---

## Introdução

No módulo anterior, você aprendeu a usar `input()` e `print()` para conversar com o usuario. Agora vamos dar um passo adiante e entender como o Python **guarda informações na memória** do computador.

Imagine que você esta organizando uma mudanca. Você tem várias caixas, e em cada caixa coloca um tipo de objeto diferente: roupas em uma, livros em outra, utensilios de cozinha em outra. Cada caixa tem uma **etiqueta** com o nome do que esta dentro. Em programação, essas caixas sao as **variáveis** — e as etiquetas sao os **nomes** que damos a elas.

> **Dica:** Termos novos? Consulte o [Glossário](00-glossario.md) a qualquer momento.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código de exemplo
2. Cole em um novo arquivo no VSCode
3. Salve com extensão `.py` (exemplo: `variaveis.py`)
4. Abra o terminal (`Ctrl + Alt + T`)
5. Navegue ate a pasta: `cd ~/meus-projetos/python-curso/modulo-07`
6. Execute: `python3 variaveis.py`

---

## O que e uma Variável?

Uma [variável](00-glossario-q-z.md#variável) e um espaco na memória do computador que guarda um valor e tem um nome. Você cria uma variável, da um nome a ela e coloca um valor dentro. Depois, pode usar esse nome para acessar o valor guardado.

Pense em uma variável como uma **caixa etiquetada**:

- A **etiqueta** e o nome da variável (por exemplo: `age`)
- O **conteúdo** da caixa e o valor guardado (por exemplo: `25`)
- Você pode **trocar o conteúdo** a qualquer momento (a caixa continua a mesma, mas o que esta dentro muda)

### Criando uma variável

Em Python, você cria uma variável simplesmente atribuindo um valor a um nome usando o sinal de igual (`=`):

```python
# Criando uma variavel chamada "name" (nome)
# O sinal = significa "recebe" ou "guarda o valor"
# "name" = nome — a variavel guarda o texto "Maria"
name = "Maria"

# Criando uma variavel chamada "age" (idade)
# "age" = idade — a variavel guarda o numero 30
age = 30

# Exibindo os valores guardados nas variaveis
print("Nome:", name)
print("Idade:", age)
```

**Saida esperada:**
```
Nome: Maria
Idade: 30
```

> **Nota:** O sinal `=` em programação não significa "igual a" como na matemática. Ele significa **"recebe"** ou **"guarda o valor"**. Quando escrevemos `age = 30`, estamos dizendo: "a variável age recebe o valor 30".

### Trocando o valor de uma variável

Você pode mudar o valor de uma variável a qualquer momento. O valor antigo e substituido pelo novo:

```python
# Criando a variavel "price" (preco) com valor inicial
# "price" = preco
price = 10.50
print("Preco original:", price)

# Trocando o valor da variavel
# Agora price guarda 8.99 em vez de 10.50
price = 8.99
print("Preco com desconto:", price)
```

**Saida esperada:**
```
Preco original: 10.5
Preco com desconto: 8.99
```

> **Nota:** Quando você atribui um novo valor a uma variável, o valor anterior e perdido. A caixa so guarda um valor por vez.

---

## Os Quatro Tipos Básicos de Dados

Em Python, cada valor tem um **tipo** que define que tipo de informação ele representa. Os quatro tipos básicos sao:

### 1. int — Números Inteiros

O tipo `int` (abreviacao de "integer", que significa "inteiro" em ingles) representa números sem casas decimais. Podem ser positivos, negativos ou zero.

```python
# Exemplos de numeros inteiros (int)
# "quantity" = quantidade, "temperature" = temperatura, "year" = ano
quantity = 10
temperature = -5
year = 2025
zero = 0

print("Quantidade:", quantity)
print("Temperatura:", temperature)
print("Ano:", year)
print("Zero:", zero)
```

**Saida esperada:**
```
Quantidade: 10
Temperatura: -5
Ano: 2025
Zero: 0
```

Números inteiros sao usados para contar coisas: quantidade de produtos, idade, ano, número de alunos em uma sala.

### 2. float — Números Decimais

O tipo `float` (abreviacao de "floating point", que significa "ponto flutuante" em ingles) representa números com casas decimais. Em Python, usamos **ponto** (não virgula) para separar a parte inteira da decimal.

```python
# Exemplos de numeros decimais (float)
# "price" = preco, "height" = altura, "weight" = peso
price = 19.99
height = 1.75
weight = 68.5

print("Preco:", price)
print("Altura:", height, "metros")
print("Peso:", weight, "kg")
```

**Saida esperada:**
```
Preco: 19.99
Altura: 1.75 metros
Peso: 68.5 kg
```

> **Atenção:** Em Python, o separador decimal e o **ponto** (`.`), não a virgula. Escrevemos `19.99` e não `19,99`. Isso e diferente do que usamos no dia a dia no Brasil, mas e o padrão em programação.

### 3. str — Textos (Strings)

O tipo `str` (abreviacao de "string", que significa "cadeia de caracteres" em ingles) representa textos. Strings sao criadas colocando o texto entre aspas simples ou duplas.

```python
# Exemplos de textos (str / string)
# "greeting" = saudacao, "city" = cidade, "document" = documento
greeting = "Bom dia!"
city = 'Sao Paulo'
document = "123.456.789-00"

print("Saudacao:", greeting)
print("Cidade:", city)
print("Documento:", document)
```

**Saida esperada:**
```
Saudacao: Bom dia!
Cidade: Sao Paulo
Documento: 123.456.789-00
```

> **Nota:** Mesmo que uma string contenha números (como "123.456.789-00"), ela continua sendo texto. O Python não faz cálculos com strings — ele as trata como sequencias de caracteres.

### 4. bool — Verdadeiro ou Falso

O tipo `bool` (abreviacao de "boolean", que significa "booleano" em ingles — em homenagem ao matemático George Boole) representa apenas dois valores possiveis: `True` (verdadeiro) ou `False` (falso).

```python
# Exemplos de booleanos (bool)
# "is_active" = esta ativo, "has_discount" = tem desconto
# "is_student" = e estudante
is_active = True
has_discount = False
is_student = True

print("Ativo:", is_active)
print("Tem desconto:", has_discount)
print("E estudante:", is_student)
```

**Saida esperada:**
```
Ativo: True
Tem desconto: False
E estudante: True
```

> **Atenção:** `True` e `False` comecam com letra **maiuscula**. Escrever `true` ou `false` (com minuscula) causa erro no Python.

Booleanos sao como interruptores de luz: ou esta ligado (`True`) ou desligado (`False`). Sao muito usados em condições e decisoes, que vamos aprender no módulo 12.

---

## Verificando o Tipo de uma Variável com type()

A função `type()` mostra qual e o tipo de um valor ou variável. E muito útil para verificar se uma variável contem o tipo de dado que você espera:

```python
# Verificando o tipo de cada variavel
# type() retorna o tipo do valor
name = "Carlos"
age = 28
height = 1.80
is_enrolled = True

# Exibindo o valor e o tipo de cada variavel
print("name:", name, "- Tipo:", type(name))
print("age:", age, "- Tipo:", type(age))
print("height:", height, "- Tipo:", type(height))
print("is_enrolled:", is_enrolled, "- Tipo:", type(is_enrolled))
```

**Saida esperada:**
```
name: Carlos - Tipo: <class 'str'>
age: 28 - Tipo: <class 'int'>
height: 1.8 - Tipo: <class 'float'>
is_enrolled: True - Tipo: <class 'bool'>
```

O que cada resultado significa:

| Resultado | Tipo | Significado |
|-----------|------|-------------|
| `<class 'str'>` | str | Texto (string) |
| `<class 'int'>` | int | Número inteiro |
| `<class 'float'>` | float | Número decimal |
| `<class 'bool'>` | bool | Verdadeiro ou falso |

---

## Regras e Convencoes para Nomes de Variáveis

Nem todo nome e válido para uma variável em Python. Existem regras obrigatorias e convencoes recomendadas.

### Regras obrigatorias (se não seguir, da erro)

| Regra | Exemplo válido | Exemplo inválido | Por que |
|-------|---------------|-----------------|---------|
| Deve começar com letra ou `_` | `name`, `_total` | `1name` | Não pode começar com número |
| Não pode conter espacos | `first_name` | `first name` | Espacos não sao permitidos |
| Não pode usar palavras reservadas | `my_class` | `class` | `class` e uma palavra reservada do Python |
| Diferencia maiusculas de minusculas | `Name` e `name` sao diferentes | — | Python e case-sensitive |

### Convencoes recomendadas (boas práticas)

| Convencao | Exemplo | Quando usar |
|-----------|---------|-------------|
| snake_case | `product_name`, `total_price` | Variáveis e funções |
| CamelCase | `ProductManager`, `ShoppingCart` | Classes (vamos ver no módulo 22) |
| MAIUSCULAS | `MAX_ATTEMPTS`, `TAX_RATE` | Constantes (valores que não mudam) |

> **Nota:** [snake_case](00-glossario-q-z.md#snake_case) significa escrever tudo em minusculas e separar palavras com underscore (`_`). E o padrão do Python para variáveis e funções.

```python
# Bons nomes de variaveis (snake_case, descritivos)
# "product_name" = nome do produto
product_name = "Arroz"

# "unit_price" = preco unitario
unit_price = 5.99

# "stock_quantity" = quantidade em estoque
stock_quantity = 150

# Nomes ruins (evite estes)
# x = "Arroz"        # O que e "x"? Nao diz nada
# p = 5.99           # O que e "p"? Impossivel saber
# n = 150            # O que e "n"? Confuso

print("Produto:", product_name)
print("Preco:", unit_price)
print("Estoque:", stock_quantity)
```

**Saida esperada:**
```
Produto: Arroz
Preco: 5.99
Estoque: 150
```

Dar nomes claros e descritivos as variáveis e uma das práticas mais importantes em programação. Um bom nome de variável funciona como uma etiqueta bem escrita: qualquer pessoa que leia o código entende o que aquela variável guarda.

---

## Resumo dos Tipos Básicos

| Tipo | Nome em ingles | O que guarda | Exemplos |
|------|---------------|-------------|----------|
| `int` | integer (inteiro) | Números sem decimais | `10`, `-3`, `0`, `2025` |
| `float` | floating point (ponto flutuante) | Números com decimais | `3.14`, `19.99`, `-0.5` |
| `str` | string (cadeia de caracteres) | Textos | `"Ola"`, `'Python'`, `"123"` |
| `bool` | boolean (booleano) | Verdadeiro ou falso | `True`, `False` |

---

## Para Saber Mais

- [W3Schools — Python Variables](https://www.w3schools.com/python/python_variables.asp) — _Como criar e usar variaveis_
- [W3Schools — Python Data Types](https://www.w3schools.com/python/python_datatypes.asp) — _Todos os tipos de dados do Python_
- [W3Schools — Python Numbers](https://www.w3schools.com/python/python_numbers.asp) — _Tipos numericos em detalhes_
- [W3Schools — Python Strings](https://www.w3schools.com/python/python_strings.asp) — _Trabalhando com textos_
- [W3Schools — Python Booleans](https://www.w3schools.com/python/python_booleans.asp) — _Valores verdadeiro e falso_
- [Documentação Oficial Python — Tipos Built-in](https://docs.python.org/pt-br/3/library/stdtypes.html) — _Referencia completa_

---

## Perguntas Frequentes (FAQ)

**P: O que acontece se eu usar uma variável que não existe?**
R: O Python mostra um erro chamado `NameError`. Por exemplo, se você escrever `print(nome)` sem ter criado a variável `nome` antes, vai aparecer: `NameError: name 'nome' is not defined`. Isso significa que o Python não encontrou nenhuma variável com esse nome.

**P: Posso usar acentos nos nomes de variáveis?**
R: Tecnicamente sim, o Python 3 aceita. Mas não e recomendado. Siga a convencao de usar nomes em ingles sem acentos, como `product_name` em vez de `nome_produto`. Isso segue o padrão profissional.

**P: Qual a diferença entre `=` e `==`?**
R: `=` e o operador de **atribuição** — ele guarda um valor em uma variável (`age = 25`). `==` e o operador de **comparação** — ele verifica se dois valores sao iguais (`age == 25` retorna `True` ou `False`). Vamos aprender sobre `==` no módulo 11.

**P: Posso guardar qualquer coisa em uma variável?**
R: Sim! Variáveis em Python podem guardar qualquer tipo de dado: números, textos, booleanos, listas, dicionários e muito mais. O Python e flexível nesse sentido.

**P: O que e "case-sensitive"?**
R: Significa que o Python diferencia letras maiusculas de minusculas. `Name`, `name` e `NAME` sao tres variáveis diferentes. Tenha cuidado com isso ao escrever seus programas.

**P: Por que usar nomes em ingles para variáveis?**
R: E a convencao profissional no mundo todo. Quando você trabalhar em equipe ou ler código de outras pessoas, os nomes estarao em ingles. Neste curso, todos os nomes de variáveis sao em ingles com traducao nos comentários para você se acostumar.

**P: O que sao "palavras reservadas"?**
R: Sao palavras que o Python ja usa para funções especificas e que você não pode usar como nomes de variáveis. Exemplos: `if`, `for`, `while`, `class`, `def`, `return`, `True`, `False`, `None`. Se tentar usar, o Python mostra um erro de sintaxe.

**P: Posso criar uma variável sem dar valor a ela?**
R: Não diretamente. Em Python, uma variável so existe quando você atribui um valor a ela. Mas você pode usar `None` como valor inicial: `result = None` significa "a variável result existe, mas ainda não tem um valor definido".

**P: O que e `None`?**
R: `None` e um valor especial do Python que significa "nada" ou "vazio". E diferente de zero (`0`) ou de texto vazio (`""`). `None` significa que a variável existe mas não tem valor atribuido.

**P: Por que `"123"` e string e não int?**
R: Porque esta entre aspas. Tudo que esta entre aspas e tratado como texto (string) pelo Python, mesmo que pareca um número. Para o Python, `"123"` e uma sequência de caracteres, não um número. Se quiser usar como número, precisa converter com `int("123")`.

**P: Posso usar uma variável antes de cria-la?**
R: Não. O Python le o código de cima para baixo. Se você tentar usar uma variável antes de atribuir um valor a ela, vai receber um `NameError`. Sempre crie a variável antes de usa-la.

**P: O que acontece se eu escrever `True` com t minusculo?**
R: O Python não vai reconhecer `true` como booleano — vai pensar que e o nome de uma variável. Como essa variável provavelmente não existe, vai dar `NameError`. Sempre use `True` e `False` com a primeira letra maiuscula.

**P: Posso mudar o tipo de uma variável?**
R: Sim! Em Python, você pode atribuir um valor de tipo diferente a uma variável que ja existe. Por exemplo: `x = 10` (int) e depois `x = "dez"` (str). Isso funciona, mas pode causar confusao. Evite mudar o tipo de uma variável no meio do programa.

**P: O que e "ponto flutuante"?**
R: E o nome técnico para números decimais em computacao. O "ponto" se refere ao ponto decimal (`.`), e "flutuante" porque o ponto pode "flutuar" para diferentes posicoes (1.5, 15.0, 0.15). Na prática, `float` e simplesmente um número com casas decimais.

**P: Por que o Python mostra `10.0` em vez de `10` quando uso float?**
R: Porque `float` sempre mostra o ponto decimal para indicar que e um número decimal, mesmo quando não tem casas decimais significativas. `10.0` e `10` tem o mesmo valor, mas sao de tipos diferentes (`float` e `int`).

**P: Posso usar underscore no meio de números?**
R: Sim! O Python permite usar `_` para separar grupos de digitos e facilitar a leitura: `1_000_000` e o mesmo que `1000000`. E como usar ponto para separar milhares no dia a dia.

**P: O que e uma constante?**
R: E uma variável cujo valor não deveria mudar durante o programa. Em Python, não existe uma forma de impedir a mudanca, mas a convencao e usar nomes em MAIUSCULAS: `TAX_RATE = 0.10`. Isso sinaliza para outros programadores que aquele valor não deve ser alterado.

**P: Quantas variáveis posso criar?**
R: Não ha limite prático. Você pode criar quantas variáveis precisar. O importante e dar nomes claros e descritivos para não se perder.

**P: Posso criar várias variáveis na mesma linha?**
R: Sim! Python permite atribuição multipla: `name, age, city = "Ana", 25, "SP"`. Mas para iniciantes, e mais claro criar uma variável por linha para facilitar a leitura.

**P: E normal confundir os tipos no inicio?**
R: Completamente normal. Com o tempo, você vai identificar os tipos naturalmente. Use `type()` sempre que tiver duvida — e para isso que ela existe. Não tenha vergonha de verificar.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

**[Acessar Exercícios do Módulo 07](07-variaveis-tipos-exercicios.md)**

---

[<- Anterior: Entrada e Saida de Dados](06-entrada-saida.md) | [Glossário](00-glossario.md) | [Próximo: Conversão de Tipos ->](08-conversao-tipos.md)
