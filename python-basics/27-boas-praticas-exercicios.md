# 27 — Exercícios: Boas Práticas de Programação em Python

[<- Voltar para o módulo](27-boas-praticas.md) | [Glossário](00-glossario.md)

---

> **Antes de começar:** Estes exercícios vao ajudar você a praticar as boas práticas que aprendeu neste módulo. Em muitos exercícios, você vai receber código "ruim" e precisara reescreve-lo seguindo as convencoes da PEP 8. Tente resolver cada exercício sozinho antes de consultar a resposta.

---

### Exercício 1 — Corrigindo Nomes de Variáveis

#### Enunciado

O código abaixo usa nomes de variáveis que não seguem as convencoes do Python. Reescreva o código usando snake_case para variáveis e nomes descritivos em ingles, com comentários em portugues traduzindo cada termo.

```python
NomeAluno = "Maria"
IDADEALUNO = 25
notaFinal = 8.5
print(f"{NomeAluno} tem {IDADEALUNO} anos e tirou {notaFinal}")
```

#### Dicas

- Variáveis em Python usam snake_case (letras minusculas com underline)
- Use nomes em ingles seguindo a convencao profissional
- Adicione comentários em portugues traduzindo os termos em ingles

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve ser `Maria tem 25 anos e tirou 8.5`
- **Caso de borda:** Altere o nome para "Joao" e a idade para 60 — a saida deve ser `Joao tem 60 anos e tirou 8.5`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Armazenamos o nome do estudante
# "student" = estudante, "name" = nome
student_name = "Maria"
# Armazenamos a idade do estudante
# "student" = estudante, "age" = idade
student_age = 25
# Armazenamos a nota final do estudante
# "final" = final, "grade" = nota
final_grade = 8.5
# Exibimos os dados formatados usando f-string
# print() mostra o texto no terminal
print(f"{student_name} tem {student_age} anos e tirou {final_grade}")
```

Saida esperada:
```
Maria tem 25 anos e tirou 8.5
```

---

### Exercício 2 — Corrigindo Nomes de Funções

#### Enunciado

O código abaixo tem funções com nomes que não seguem as convencoes do Python. Reescreva o código usando snake_case para funções, nomes descritivos em ingles e adicione docstrings.

```python
def CalcMedia(notas):
    s = 0
    for n in notas:
        s += n
    return s / len(notas)

def MostraResultado(nome, media):
    print(f"{nome}: {media:.2f}")

MostraResultado("Maria", CalcMedia([8, 7, 9, 6]))
```

#### Dicas

- Funções em Python usam snake_case (letras minusculas com underline)
- Adicione uma docstring (texto entre `"""`) na primeira linha de cada função
- Use nomes descritivos em ingles para parametros também
- Adicione comentários em portugues traduzindo os termos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve ser `Maria: 7.50`
- **Caso de borda:** Troque as notas para `[10, 10, 10, 10]` — a saida deve ser `Maria: 10.00`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que calcula a media de uma lista de notas
# "calculate" = calcular, "average" = media, "grades" = notas
def calculate_average(grades):
    """Calcula a media aritmetica de uma lista de notas."""
    # "total" = total (soma de todas as notas)
    total = 0
    # Percorremos cada nota na lista de notas
    for grade in grades:
        # Somamos a nota ao total
        total = total + grade
    # Retornamos a media dividindo o total pela quantidade de notas
    # len() retorna o tamanho (length = comprimento) da lista
    return total / len(grades)


# Funcao que exibe o resultado formatado
# "display" = exibir, "result" = resultado
# "name" = nome, "average" = media
def display_result(name, average):
    """Exibe o nome e a media formatada com duas casas decimais."""
    # Usamos f-string para formatar a saida
    # :.2f formata o numero com 2 casas decimais
    print(f"{name}: {average:.2f}")


# Chamamos as funcoes com os dados de teste
# "grades" = notas
grades = [8, 7, 9, 6]
# Calculamos a media e exibimos o resultado
display_result("Maria", calculate_average(grades))
```

Saida esperada:
```
Maria: 7.50
```

---

### Exercício 3 — Corrigindo Nome de Classe

#### Enunciado

O código abaixo tem uma classe com nome que não segue as convencoes do Python. Reescreva o código usando CamelCase para a classe, snake_case para métodos e variáveis, e nomes em ingles com comentários em portugues.

```python
class conta_bancaria:
    def __init__(self, dono, saldo):
        self.dono = dono
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def mostrar(self):
        print(f"Dono: {self.dono}, Saldo: R$ {self.saldo:.2f}")

c = conta_bancaria("Maria", 1000)
c.depositar(500)
c.mostrar()
```

#### Dicas

- Classes em Python usam CamelCase (cada palavra com letra maiuscula)
- Métodos e variáveis usam snake_case
- Use nomes em ingles para a classe, métodos e atributos
- Adicione docstrings na classe e nos métodos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve ser `Titular: Maria, Saldo: R$ 1500.00`
- **Caso de borda:** Crie uma conta com saldo 0 e deposite 100 — a saida deve ser `Titular: Joao, Saldo: R$ 100.00`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Classe que representa uma conta bancaria
# "Bank" = banco, "Account" = conta
class BankAccount:
    """Representa uma conta bancaria com titular e saldo."""

    # Metodo construtor que inicializa a conta
    # "owner" = titular/dono, "balance" = saldo
    def __init__(self, owner, balance):
        """Inicializa a conta com titular e saldo inicial."""
        # Armazenamos o nome do titular
        self.owner = owner
        # Armazenamos o saldo inicial
        self.balance = balance

    # Metodo que adiciona um valor ao saldo
    # "deposit" = depositar, "amount" = valor/quantia
    def deposit(self, amount):
        """Adiciona um valor ao saldo da conta."""
        # Somamos o valor depositado ao saldo atual
        self.balance = self.balance + amount

    # Metodo que exibe os dados da conta
    # "display" = exibir, "info" = informacoes
    def display_info(self):
        """Exibe o titular e o saldo formatado."""
        # Exibimos os dados formatados com f-string
        print(f"Titular: {self.owner}, Saldo: R$ {self.balance:.2f}")


# Criamos uma conta bancaria para Maria com saldo de R$ 1000
# "account" = conta
account = BankAccount("Maria", 1000)
# Depositamos R$ 500 na conta
account.deposit(500)
# Exibimos as informacoes da conta
account.display_info()
```

Saida esperada:
```
Titular: Maria, Saldo: R$ 1500.00
```

---

### Exercício 4 — Extraindo Constantes

#### Enunciado

O código abaixo usa "números magicos" — valores numericos sem explicacao. Reescreva o código substituindo os números magicos por constantes nomeadas em UPPER_CASE, com comentários explicando cada constante.

```python
def calcular_salario(horas):
    salario = horas * 45.50
    if salario > 5000:
        imposto = salario * 0.275
    else:
        imposto = salario * 0.15
    return salario - imposto

print(f"Salario liquido: R$ {calcular_salario(160):.2f}")
```

#### Dicas

- Identifique todos os números que aparecem no código sem explicacao
- Crie constantes UPPER_CASE no topo do arquivo para cada valor
- Escolha nomes descritivos em ingles que expliquem o significado de cada número
- Adicione comentários em portugues traduzindo os termos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com 160 horas, a saida deve ser `Salario liquido: R$ 5278.00`
- **Caso de borda:** Com 80 horas, a saida deve ser `Salario liquido: R$ 3094.00`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Constante com o valor da hora de trabalho
# "HOURLY" = por hora, "RATE" = taxa/valor
HOURLY_RATE = 45.50

# Constante com o limite para a faixa de imposto mais alta
# "HIGH" = alta, "TAX" = imposto, "THRESHOLD" = limite
HIGH_TAX_THRESHOLD = 5000

# Constante com a taxa de imposto para salarios acima do limite
# "HIGH" = alta, "TAX" = imposto, "RATE" = taxa
HIGH_TAX_RATE = 0.275

# Constante com a taxa de imposto para salarios abaixo do limite
# "LOW" = baixa, "TAX" = imposto, "RATE" = taxa
LOW_TAX_RATE = 0.15


# Funcao que calcula o salario liquido
# "calculate" = calcular, "net" = liquido, "salary" = salario
# "hours" = horas
def calculate_net_salary(hours):
    """Calcula o salario liquido com base nas horas trabalhadas."""
    # Calculamos o salario bruto multiplicando horas pelo valor da hora
    # "gross" = bruto, "salary" = salario
    gross_salary = hours * HOURLY_RATE
    # Verificamos em qual faixa de imposto o salario se enquadra
    if gross_salary > HIGH_TAX_THRESHOLD:
        # Salario acima do limite: aplica taxa mais alta
        # "tax" = imposto
        tax = gross_salary * HIGH_TAX_RATE
    else:
        # Salario abaixo do limite: aplica taxa mais baixa
        tax = gross_salary * LOW_TAX_RATE
    # Retornamos o salario liquido (bruto menos imposto)
    return gross_salary - tax


# Testamos a funcao com 160 horas trabalhadas
# "net_salary" = salario liquido
net_salary = calculate_net_salary(160)
# Exibimos o resultado formatado com 2 casas decimais
print(f"Salario liquido: R$ {net_salary:.2f}")
```

Saida esperada:
```
Salario liquido: R$ 5278.00
```

---

### Exercício 5 — Organizando Imports

#### Enunciado

O código abaixo tem imports desorganizados. Reorganize-os seguindo a PEP 8: primeiro biblioteca padrão, depois bibliotecas de terceiros, depois módulos locais. Separe os grupos com uma linha em branco e ordene alfabeticamente dentro de cada grupo.

```python
from datetime import datetime
import requests
import json
import os
from math import sqrt, pi
import random
```

#### Dicas

- Grupo 1: Biblioteca padrão do Python (módulos que ja vem com o Python)
- Grupo 2: Bibliotecas de terceiros (instaladas com pip)
- Separe os grupos com uma linha em branco
- Dentro de cada grupo, ordene em ordem alfabetica
- `import` simples vem antes de `from ... import`

#### Proposta de Teste

Verifique visualmente seu código:
- **Caso básico:** Os imports da biblioteca padrão (`json`, `os`, `random`) devem vir antes de `requests`
- **Caso de borda:** Os imports com `from` (`from datetime import datetime`, `from math import sqrt, pi`) devem estar no grupo correto (biblioteca padrão) e em ordem alfabetica

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Grupo 1: Biblioteca padrao do Python (em ordem alfabetica)
# "import" = importar (trazer modulos para uso)
import json        # "json" = formato de dados para troca de informacoes
import os          # "os" = sistema operacional (operating system)
import random      # "random" = aleatorio (gerar valores aleatorios)
from datetime import datetime  # "datetime" = data e hora
from math import sqrt, pi     # "sqrt" = raiz quadrada (square root), "pi" = numero pi

# Grupo 2: Bibliotecas de terceiros (instaladas com pip)
import requests    # "requests" = requisicoes HTTP
```

Saida esperada:
```
(este codigo apenas importa modulos — nao produz saida por si so)
```

---

### Exercício 6 — Reescrevendo Comentários

#### Enunciado

O código abaixo tem comentários desnecessarios que repetem o obvio. Reescreva o código removendo os comentários ruins e adicionando comentários úteis que expliquem o "por que" das decisoes, além de traduzir os termos em ingles.

```python
# Cria uma lista vazia
items = []
# Adiciona "Arroz" a lista
items.append("Arroz")
# Adiciona "Feijao" a lista
items.append("Feijao")
# Percorre a lista
for item in items:
    # Imprime o item
    print(item)
# Verifica se a lista tem mais de 5 itens
if len(items) > 5:
    # Imprime "Lista grande"
    print("Lista grande")
```

#### Dicas

- Remova comentários que apenas repetem o que o código ja diz
- Adicione comentários que expliquem o "por que" de uma decisao
- Mantenha comentários que traduzem termos em ingles
- Se o código e claro com nomes descritivos, ele não precisa de comentário

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve mostrar "Arroz" e "Feijao" em linhas separadas
- **Caso de borda:** Adicione mais 4 itens a lista (totalizando 6) — a mensagem "Lista grande" deve aparecer

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Criamos uma lista de compras para o almoco de domingo
# "shopping_items" = itens de compras
shopping_items = []

# Adicionamos os itens basicos que precisamos comprar
# "append" = adicionar ao final da lista
shopping_items.append("Arroz")
shopping_items.append("Feijao")

# Exibimos cada item para conferir a lista antes de ir ao mercado
# "item" = item/produto
for item in shopping_items:
    print(item)

# Alertamos se a lista ficou grande demais para carregar sozinho
# Limite de 5 itens baseado na capacidade de uma sacola
if len(shopping_items) > 5:
    print("Lista grande")
```

Saida esperada:
```
Arroz
Feijao
```

---

### Exercício 7 — Adicionando Docstrings

#### Enunciado

O código abaixo tem funções sem docstrings. Adicione docstrings apropriadas a cada função, descrevendo o que ela faz, quais parametros recebe e o que retorna. Mantenha os nomes em ingles e adicione comentários em portugues.

```python
def calculate_rectangle_area(width, height):
    return width * height

def is_even(number):
    return number % 2 == 0

def format_currency(value):
    return f"R$ {value:.2f}"

print(format_currency(calculate_rectangle_area(5, 3)))
print(f"10 e par? {is_even(10)}")
```

#### Dicas

- Docstrings ficam na primeira linha dentro da função, entre tres aspas (`"""`)
- Para funções simples, uma linha e suficiente
- Inclua descricao dos parametros e do retorno
- Escreva as docstrings em portugues

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A primeira saida deve ser `R$ 15.00` e a segunda `10 e par? True`
- **Caso de borda:** Teste `is_even(7)` — deve retornar `False`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que calcula a area de um retangulo
# "calculate" = calcular, "rectangle" = retangulo, "area" = area
def calculate_rectangle_area(width, height):
    """Calcula a area de um retangulo multiplicando largura por altura.

    Parametros:
        width (float): Largura do retangulo.
        height (float): Altura do retangulo.

    Retorna:
        float: Area do retangulo.
    """
    # "width" = largura, "height" = altura
    # Multiplicamos largura por altura para obter a area
    return width * height


# Funcao que verifica se um numero e par
# "is" = e/esta, "even" = par
def is_even(number):
    """Verifica se um numero e par.

    Parametros:
        number (int): Numero a ser verificado.

    Retorna:
        bool: True se o numero e par, False se e impar.
    """
    # "number" = numero
    # O operador % (modulo) retorna o resto da divisao
    # Se o resto da divisao por 2 e zero, o numero e par
    return number % 2 == 0


# Funcao que formata um valor como moeda brasileira
# "format" = formatar, "currency" = moeda
def format_currency(value):
    """Formata um valor numerico como moeda brasileira (R$).

    Parametros:
        value (float): Valor a ser formatado.

    Retorna:
        str: Valor formatado como "R$ X.XX".
    """
    # "value" = valor
    # :.2f formata o numero com 2 casas decimais
    return f"R$ {value:.2f}"


# Testamos as funcoes combinadas
# Calculamos a area de um retangulo 5x3 e formatamos como moeda
print(format_currency(calculate_rectangle_area(5, 3)))
# Verificamos se 10 e par
print(f"10 e par? {is_even(10)}")
```

Saida esperada:
```
R$ 15.00
10 e par? True
```

---

### Exercício 8 — Quebrando Linhas Longas

#### Enunciado

O código abaixo tem linhas que ultrapassam 79 caracteres. Reescreva o código quebrando as linhas longas de forma legivel, seguindo a PEP 8.

```python
resultado = calcular_preco_final_com_desconto_e_imposto(preco_original, percentual_desconto, taxa_imposto, quantidade_itens)

mensagem = "O produto " + nome_produto + " custa R$ " + str(preco) + " e esta disponivel em " + str(quantidade) + " unidades"

lista_de_compras = [{"nome": "Arroz", "preco": 5.99, "quantidade": 2}, {"nome": "Feijao", "preco": 8.50, "quantidade": 1}, {"nome": "Macarrao", "preco": 3.75, "quantidade": 3}]
```

#### Dicas

- Use parenteses para quebrar chamadas de função em multiplas linhas
- Use f-strings em vez de concatenacao com `+`
- Quebre listas e dicionários colocando cada item em uma linha separada
- Mantenha a indentacao consistente nas linhas continuadas

#### Proposta de Teste

Verifique visualmente seu código:
- **Caso básico:** Nenhuma linha deve ultrapassar 79 caracteres
- **Caso de borda:** Conte os caracteres da linha mais longa — deve ter no máximo 79

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Quebrando chamada de funcao longa usando parenteses
# "result" = resultado
# "calculate" = calcular, "final" = final, "price" = preco
result = calculate_final_price(
    original_price,       # preco original
    discount_percent,     # percentual de desconto
    tax_rate,             # taxa de imposto
    item_quantity          # quantidade de itens
)

# Usando f-string em vez de concatenacao
# "message" = mensagem
# "product_name" = nome do produto
# "price" = preco, "quantity" = quantidade
message = (
    f"O produto {product_name} custa "
    f"R$ {price:.2f} e esta disponivel "
    f"em {quantity} unidades"
)

# Quebrando lista de dicionarios em multiplas linhas
# "shopping_list" = lista de compras
shopping_list = [
    # Cada item em uma linha separada para facilitar a leitura
    {"name": "Arroz", "price": 5.99, "quantity": 2},
    {"name": "Feijao", "price": 8.50, "quantity": 1},
    {"name": "Macarrao", "price": 3.75, "quantity": 3},
]
```

Saida esperada:
```
(este codigo define variaveis — a saida depende dos valores das variaveis usadas)
```

---

### Exercício 9 — Separando Responsabilidades

#### Enunciado

O código abaixo tem uma única função que faz muitas coisas: le dados, valida, calcula e imprime. Reescreva o código dividindo em funções menores, cada uma com uma única responsabilidade.

```python
def processar(produtos):
    total = 0
    for p in produtos:
        if p["preco"] < 0:
            print(f"Erro: {p['nome']} tem preco negativo")
            continue
        if p["qtd"] < 0:
            print(f"Erro: {p['nome']} tem quantidade negativa")
            continue
        subtotal = p["preco"] * p["qtd"]
        total += subtotal
        print(f"{p['nome']}: R$ {subtotal:.2f}")
    print(f"Total: R$ {total:.2f}")

produtos = [
    {"nome": "Arroz", "preco": 5.99, "qtd": 2},
    {"nome": "Feijao", "preco": -1, "qtd": 1},
    {"nome": "Macarrao", "preco": 3.75, "qtd": 3},
]
processar(produtos)
```

#### Dicas

- Crie uma função para validar um produto
- Crie uma função para calcular o subtotal de um produto
- Crie uma função para calcular o total de todos os produtos
- Crie uma função para exibir o relatório
- Use nomes em ingles com comentários em portugues

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve mostrar Arroz (R$ 11.98), pular Feijao (erro), mostrar Macarrao (R$ 11.25) e total R$ 23.23
- **Caso de borda:** Adicione um produto com quantidade negativa — deve exibir mensagem de erro e não incluir no total

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Funcao que valida os dados de um produto
# "validate" = validar, "product" = produto
def validate_product(product):
    """Verifica se os dados do produto sao validos.

    Parametros:
        product (dict): Dicionario com dados do produto.

    Retorna:
        bool: True se valido, False se invalido.
    """
    # Verificamos se o preco e negativo
    # "price" = preco
    if product["price"] < 0:
        # Exibimos mensagem de erro com o nome do produto
        print(f"Erro: {product['name']} tem preco negativo")
        return False
    # Verificamos se a quantidade e negativa
    # "quantity" = quantidade
    if product["quantity"] < 0:
        # Exibimos mensagem de erro com o nome do produto
        print(f"Erro: {product['name']} tem quantidade negativa")
        return False
    # Produto valido
    return True


# Funcao que calcula o subtotal de um produto
# "calculate" = calcular, "subtotal" = subtotal
def calculate_subtotal(product):
    """Calcula o subtotal de um produto (preco x quantidade)."""
    # Multiplicamos preco pela quantidade
    return product["price"] * product["quantity"]


# Funcao que calcula o total de uma lista de produtos validos
# "calculate" = calcular, "total" = total
def calculate_total(products):
    """Calcula o total de todos os produtos validos.

    Parametros:
        products (list): Lista de dicionarios com produtos.

    Retorna:
        float: Valor total dos produtos validos.
    """
    # "total" = total (soma dos subtotais)
    total = 0
    # Percorremos cada produto da lista
    for product in products:
        # Validamos o produto antes de calcular
        if validate_product(product):
            # Calculamos o subtotal e somamos ao total
            # "subtotal" = subtotal
            subtotal = calculate_subtotal(product)
            # Exibimos o subtotal do produto
            print(f"{product['name']}: R$ {subtotal:.2f}")
            # Somamos ao total geral
            total = total + subtotal
    # Retornamos o total calculado
    return total


# Lista de produtos para processar
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99, "quantity": 2},
    {"name": "Feijao", "price": -1, "quantity": 1},
    {"name": "Macarrao", "price": 3.75, "quantity": 3},
]

# Calculamos o total e exibimos o resultado
# "total" = total
total = calculate_total(products)
# Exibimos o total geral
print(f"Total: R$ {total:.2f}")
```

Saida esperada:
```
Arroz: R$ 11.98
Erro: Feijao tem preco negativo
Macarrao: R$ 11.25
Total: R$ 23.23
```

---

### Exercício 10 — Refatorando Código Completo (Antes e Depois)

#### Enunciado

O código abaixo e funcional mas não segue nenhuma boa prática. Reescreva-o completamente aplicando todas as boas práticas que você aprendeu: snake_case, CamelCase, constantes UPPER_CASE, docstrings, comentários úteis, nomes descritivos em ingles, espacamento correto e organização de imports.

```python
import random
import os
import math
class a:
 def __init__(self,n,v):
  self.n=n
  self.v=[]
  for i in range(v):
   self.v.append(random.randint(0,100))
 def m(self):
  return sum(self.v)/len(self.v)
 def mx(self):
  return max(self.v)
 def mn(self):
  return min(self.v)
 def r(self):
  print(f"{self.n}: media={self.m():.1f}, max={self.mx()}, min={self.mn()}")
t=a("Turma A",5)
t.r()
```

#### Dicas

- Renomeie a classe para um nome descritivo em CamelCase
- Renomeie todos os métodos e variáveis para snake_case descritivo
- Adicione docstrings na classe e nos métodos
- Adicione constantes para os valores magicos (0 e 100)
- Organize os imports (remova os que não sao usados)
- Adicione espacamento correto (linhas em branco, espacos ao redor de operadores)

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** A saida deve mostrar o nome da turma com media, nota maxima e nota minima (os valores variam porque sao aleatorios)
- **Caso de borda:** Crie uma turma com 1 aluno — media, máximo e mínimo devem ser iguais

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos apenas o modulo que realmente usamos
# "random" = aleatorio (gerar valores aleatorios)
import random

# Constante com a nota minima possivel
# "MIN" = minimo, "GRADE" = nota
MIN_GRADE = 0
# Constante com a nota maxima possivel
# "MAX" = maximo, "GRADE" = nota
MAX_GRADE = 100


# Classe que representa uma turma de estudantes com notas
# "Student" = estudante, "Group" = grupo/turma
class StudentGroup:
    """Representa uma turma com notas geradas aleatoriamente."""

    # Metodo construtor que inicializa a turma
    # "name" = nome, "student_count" = quantidade de estudantes
    def __init__(self, name, student_count):
        """Inicializa a turma com nome e notas aleatorias.

        Parametros:
            name (str): Nome da turma.
            student_count (int): Quantidade de estudantes.
        """
        # Armazenamos o nome da turma
        self.name = name
        # Geramos notas aleatorias para cada estudante
        # "grades" = notas
        self.grades = []
        # Criamos uma nota aleatoria para cada estudante
        for i in range(student_count):
            # randint gera um numero inteiro aleatorio no intervalo
            grade = random.randint(MIN_GRADE, MAX_GRADE)
            # Adicionamos a nota a lista
            self.grades.append(grade)

    # Metodo que calcula a media das notas
    # "calculate" = calcular, "average" = media
    def calculate_average(self):
        """Calcula a media aritmetica das notas da turma."""
        # Somamos todas as notas e dividimos pela quantidade
        return sum(self.grades) / len(self.grades)

    # Metodo que retorna a nota mais alta
    # "get" = obter, "highest" = mais alta, "grade" = nota
    def get_highest_grade(self):
        """Retorna a maior nota da turma."""
        return max(self.grades)

    # Metodo que retorna a nota mais baixa
    # "get" = obter, "lowest" = mais baixa, "grade" = nota
    def get_lowest_grade(self):
        """Retorna a menor nota da turma."""
        return min(self.grades)

    # Metodo que exibe o relatorio da turma
    # "display" = exibir, "report" = relatorio
    def display_report(self):
        """Exibe o relatorio com media, maior e menor nota."""
        # Calculamos a media
        # "average" = media
        average = self.calculate_average()
        # Obtemos a maior nota
        # "highest" = mais alta
        highest = self.get_highest_grade()
        # Obtemos a menor nota
        # "lowest" = mais baixa
        lowest = self.get_lowest_grade()
        # Exibimos o relatorio formatado
        print(f"{self.name}: media={average:.1f}, max={highest}, min={lowest}")


# Criamos uma turma com 5 estudantes
# "group" = grupo/turma
group = StudentGroup("Turma A", 5)
# Exibimos o relatorio da turma
group.display_report()
```

Saida esperada:
```
Turma A: media=52.4, max=89, min=12
```

> Os valores variam a cada execução porque as notas sao geradas aleatoriamente. O importante e que o formato da saida esteja correto.

---

### Exercício 11 — Identificando Problemas de Estilo

#### Enunciado

O código abaixo tem **8 problemas de estilo** segundo a PEP 8. Identifique todos os problemas e reescreva o código corrigido. Os problemas podem ser de nomenclatura, espacamento, comentários, organização de imports ou outros.

```python
from math import sqrt
import os
import json
import requests
MaxValue=100
def CheckValue(x):
 if x>MaxValue:
  return True
 else:
  return False
# verifica se o valor e maior que 100
result=CheckValue(150)
print( result )
```

#### Dicas

- Verifique a ordem e organização dos imports
- Verifique os nomes de variáveis, funções e constantes
- Verifique o espacamento ao redor de operadores
- Verifique a indentacao (4 espacos)
- Verifique se ha comentários desnecessarios ou mal posicionados
- Verifique se a lógica pode ser simplificada

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com o valor 150, a saida deve ser `True`
- **Caso de borda:** Altere para testar com o valor 50 — a saida deve ser `False`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Problema 1: imports desorganizados (corrigido: padrao antes de terceiros)
# Problema 2: import nao utilizado (os e json removidos)
# Grupo 1: Biblioteca padrao
from math import sqrt  # "sqrt" = raiz quadrada (square root)

# Grupo 2: Bibliotecas de terceiros
import requests  # "requests" = requisicoes HTTP

# Problema 3: constante nao estava em UPPER_CASE (corrigido)
# "MAX" = maximo, "VALUE" = valor
MAX_VALUE = 100


# Problema 4: funcao nao estava em snake_case (corrigido)
# Problema 5: indentacao com 1 espaco em vez de 4 (corrigido)
# "exceeds" = excede/ultrapassa, "max" = maximo
def exceeds_max(value):
    """Verifica se o valor ultrapassa o limite maximo."""
    # Problema 6: logica desnecessariamente complexa (simplificado)
    # "value" = valor
    # Retornamos diretamente o resultado da comparacao
    return value > MAX_VALUE


# Problema 7: comentario deslocado (movido para antes da funcao)
# Problema 8: espacos incorretos ao redor de operadores e em print()
# "result" = resultado
result = exceeds_max(150)
# Exibimos o resultado
print(result)
```

Saida esperada:
```
True
```

---

### Exercício 12 — Aplicando Boas Práticas em um Programa Completo

#### Enunciado

Crie um programa do zero que gerência uma lista de tarefas (to-do list). O programa deve permitir adicionar tarefas, listar tarefas e marcar tarefas como concluidas. Aplique todas as boas práticas desde o inicio: snake_case, constantes, docstrings, comentários úteis, nomes descritivos em ingles e espacamento correto.

O programa deve:
1. Ter uma lista de tarefas (cada tarefa e um dicionário com "description" e "done")
2. Ter uma função para adicionar tarefa
3. Ter uma função para listar tarefas (mostrando se esta concluida ou pendente)
4. Ter uma função para marcar uma tarefa como concluida
5. Demonstrar o uso com pelo menos 3 tarefas

#### Dicas

- Planeje as funções antes de escrever o código
- Cada função deve ter uma única responsabilidade
- Use constantes para textos que se repetem (como marcadores de status)
- Adicione docstrings em todas as funções
- Use nomes em ingles com comentários em portugues

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Apos adicionar 3 tarefas e marcar a primeira como concluida, a listagem deve mostrar a primeira com marcador de concluida e as outras como pendentes
- **Caso de borda:** Tente marcar uma tarefa com índice inválido (como 10) — o programa deve tratar o erro sem quebrar

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Marcador visual para tarefas concluidas
# "DONE" = concluido, "MARKER" = marcador
DONE_MARKER = "[x]"
# Marcador visual para tarefas pendentes
# "PENDING" = pendente, "MARKER" = marcador
PENDING_MARKER = "[ ]"


# Funcao que adiciona uma tarefa a lista
# "add" = adicionar, "task" = tarefa
def add_task(task_list, description):
    """Adiciona uma nova tarefa a lista.

    Parametros:
        task_list (list): Lista de tarefas atual.
        description (str): Descricao da tarefa.
    """
    # Criamos um dicionario representando a tarefa
    # "task" = tarefa
    # "description" = descricao, "done" = concluido
    task = {
        "description": description,
        "done": False
    }
    # Adicionamos a tarefa a lista
    task_list.append(task)
    # Confirmamos a adicao
    print(f"Tarefa adicionada: {description}")


# Funcao que lista todas as tarefas
# "display" = exibir, "tasks" = tarefas
def display_tasks(task_list):
    """Exibe todas as tarefas com seu status."""
    # Verificamos se a lista esta vazia
    if len(task_list) == 0:
        print("Nenhuma tarefa cadastrada.")
        return
    # Exibimos o cabecalho da lista
    print("\n--- Lista de Tarefas ---")
    # Percorremos cada tarefa com seu indice
    # "index" = indice, "task" = tarefa
    # enumerate() retorna o indice e o valor de cada item
    for index, task in enumerate(task_list):
        # Escolhemos o marcador baseado no status da tarefa
        if task["done"]:
            # Tarefa concluida: usa marcador [x]
            marker = DONE_MARKER
        else:
            # Tarefa pendente: usa marcador [ ]
            marker = PENDING_MARKER
        # Exibimos o indice, marcador e descricao
        print(f"  {index + 1}. {marker} {task['description']}")
    # Linha em branco apos a lista
    print()


# Funcao que marca uma tarefa como concluida
# "complete" = concluir/completar, "task" = tarefa
def complete_task(task_list, task_number):
    """Marca uma tarefa como concluida pelo numero.

    Parametros:
        task_list (list): Lista de tarefas.
        task_number (int): Numero da tarefa (comecando em 1).
    """
    # Convertemos o numero da tarefa para indice (comeca em 0)
    # "index" = indice
    index = task_number - 1
    # Verificamos se o indice e valido
    if index < 0 or index >= len(task_list):
        print(f"Erro: tarefa {task_number} nao existe.")
        return
    # Marcamos a tarefa como concluida
    # "done" = concluido
    task_list[index]["done"] = True
    # Confirmamos a conclusao
    # "description" = descricao
    print(f"Tarefa concluida: {task_list[index]['description']}")


# Criamos a lista de tarefas vazia
# "task_list" = lista de tarefas
task_list = []

# Adicionamos 3 tarefas
add_task(task_list, "Estudar boas praticas do Python")
add_task(task_list, "Fazer os exercicios do modulo 27")
add_task(task_list, "Revisar o codigo do projeto")

# Listamos as tarefas (todas pendentes)
display_tasks(task_list)

# Marcamos a primeira tarefa como concluida
complete_task(task_list, 1)

# Tentamos marcar uma tarefa com indice invalido
complete_task(task_list, 10)

# Listamos novamente para ver a atualizacao
display_tasks(task_list)
```

Saida esperada:
```
Tarefa adicionada: Estudar boas praticas do Python
Tarefa adicionada: Fazer os exercicios do modulo 27
Tarefa adicionada: Revisar o codigo do projeto

--- Lista de Tarefas ---
  1. [ ] Estudar boas praticas do Python
  2. [ ] Fazer os exercicios do modulo 27
  3. [ ] Revisar o codigo do projeto

Tarefa concluida: Estudar boas praticas do Python
Erro: tarefa 10 nao existe.

--- Lista de Tarefas ---
  1. [x] Estudar boas praticas do Python
  2. [ ] Fazer os exercicios do modulo 27
  3. [ ] Revisar o codigo do projeto

```

---

### Exercício 13 — Espacamento e Linhas em Branco

#### Enunciado

O código abaixo tem problemas de espacamento: faltam linhas em branco entre funções, faltam espacos ao redor de operadores e ha espacos desnecessarios. Corrija todos os problemas de espacamento seguindo a PEP 8.

```python
import math
def calculate_circle_area( radius ):
    area=math.pi*radius**2
    return area
def calculate_circle_perimeter( radius ):
    perimeter=2*math.pi*radius
    return perimeter
def display_circle_info( radius ):
    area=calculate_circle_area(radius)
    perimeter=calculate_circle_perimeter(radius)
    print(f"Raio: {radius}")
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimeter:.2f}")
display_circle_info( 5 )
```

#### Dicas

- Coloque duas linhas em branco entre funções no nível do módulo
- Coloque um espaco antes e depois de operadores (`=`, `*`, `**`)
- Remova espacos dentro dos parenteses de funções
- Adicione comentários em portugues traduzindo os termos em ingles

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Com raio 5, a area deve ser `78.54` e o perimetro `31.42`
- **Caso de borda:** Com raio 0, a area deve ser `0.00` e o perimetro `0.00`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Importamos o modulo math para usar o valor de pi
# "math" = matematica
import math


# Funcao que calcula a area de um circulo
# "calculate" = calcular, "circle" = circulo, "area" = area
def calculate_circle_area(radius):
    """Calcula a area de um circulo dado o raio."""
    # "radius" = raio
    # A area do circulo e pi multiplicado pelo raio ao quadrado
    # "area" = area
    area = math.pi * radius ** 2
    return area


# Funcao que calcula o perimetro de um circulo
# "calculate" = calcular, "perimeter" = perimetro
def calculate_circle_perimeter(radius):
    """Calcula o perimetro (circunferencia) de um circulo dado o raio."""
    # "radius" = raio
    # O perimetro e 2 vezes pi vezes o raio
    # "perimeter" = perimetro
    perimeter = 2 * math.pi * radius
    return perimeter


# Funcao que exibe as informacoes do circulo
# "display" = exibir, "info" = informacoes
def display_circle_info(radius):
    """Exibe a area e o perimetro de um circulo."""
    # Calculamos a area usando a funcao dedicada
    # "area" = area
    area = calculate_circle_area(radius)
    # Calculamos o perimetro usando a funcao dedicada
    # "perimeter" = perimetro
    perimeter = calculate_circle_perimeter(radius)
    # Exibimos os resultados formatados
    print(f"Raio: {radius}")
    print(f"Area: {area:.2f}")
    print(f"Perimetro: {perimeter:.2f}")


# Testamos com raio 5
display_circle_info(5)
```

Saida esperada:
```
Raio: 5
Area: 78.54
Perimetro: 31.42
```

---

### Exercício 14 — Criando um Módulo com Boas Práticas

#### Enunciado

Crie dois arquivos Python seguindo todas as boas práticas. O primeiro arquivo (`string_utils.py`) deve conter funções utilitarias para manipulação de strings. O segundo arquivo (`main.py`) deve importar e usar essas funções. Aplique todas as convencoes: snake_case, docstrings, imports organizados, comentários úteis e nomes descritivos.

O módulo `string_utils.py` deve ter:
1. Uma função que conta quantas vogais tem em um texto
2. Uma função que inverte uma string
3. Uma função que verifica se uma string e um palindromo

#### Dicas

- Cada função deve ter docstring com descricao, parametros e retorno
- Use nomes em ingles para funções e variáveis
- Adicione comentários em portugues traduzindo os termos
- No arquivo `main.py`, importe as funções usando `from string_utils import ...`

#### Proposta de Teste

Execute `python3 main.py` e verifique:
- **Caso básico:** "Python" deve ter 1 vogal, invertido deve ser "nohtyP"
- **Caso de borda:** "arara" deve ser palindromo, "python" não deve ser palindromo

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

Arquivo `string_utils.py`:

```python
# Modulo com funcoes utilitarias para manipulacao de strings
# "string" = texto/cadeia de caracteres, "utils" = utilitarios

# Constante com as vogais para verificacao
# "VOWELS" = vogais
VOWELS = "aeiouAEIOU"


# Funcao que conta as vogais em um texto
# "count" = contar, "vowels" = vogais
def count_vowels(text):
    """Conta quantas vogais existem em um texto.

    Parametros:
        text (str): Texto a ser analisado.

    Retorna:
        int: Quantidade de vogais encontradas.
    """
    # "text" = texto
    # "count" = contador
    count = 0
    # Percorremos cada caractere do texto
    # "char" = caractere (character)
    for char in text:
        # Verificamos se o caractere e uma vogal
        if char in VOWELS:
            # Incrementamos o contador
            count = count + 1
    # Retornamos a quantidade de vogais
    return count


# Funcao que inverte uma string
# "reverse" = inverter, "string" = texto
def reverse_string(text):
    """Inverte a ordem dos caracteres de um texto.

    Parametros:
        text (str): Texto a ser invertido.

    Retorna:
        str: Texto com caracteres na ordem inversa.
    """
    # "text" = texto
    # Usamos fatiamento com passo -1 para inverter
    # [::-1] percorre o texto de tras para frente
    return text[::-1]


# Funcao que verifica se um texto e palindromo
# "is" = e/esta, "palindrome" = palindromo
def is_palindrome(text):
    """Verifica se um texto e palindromo (lido igual de tras para frente).

    Parametros:
        text (str): Texto a ser verificado.

    Retorna:
        bool: True se e palindromo, False caso contrario.
    """
    # "text" = texto
    # Convertemos para minusculas para comparacao sem diferenciar maiusculas
    # "lower_text" = texto em minusculas
    lower_text = text.lower()
    # Comparamos o texto com sua versao invertida
    return lower_text == reverse_string(lower_text)
```

Arquivo `main.py`:

```python
# Arquivo principal que demonstra o uso do modulo string_utils
# "main" = principal

# Importamos as funcoes do nosso modulo utilitario
# "string_utils" = utilitarios de texto
from string_utils import count_vowels, reverse_string, is_palindrome

# Testamos a funcao de contar vogais
# "text" = texto
text = "Python"
# "vowel_count" = contagem de vogais
vowel_count = count_vowels(text)
print(f"Vogais em '{text}': {vowel_count}")

# Testamos a funcao de inverter string
# "reversed_text" = texto invertido
reversed_text = reverse_string(text)
print(f"'{text}' invertido: {reversed_text}")

# Testamos a funcao de palindromo com diferentes textos
# "word" = palavra
word = "arara"
print(f"'{word}' e palindromo? {is_palindrome(word)}")

# Testamos com uma palavra que nao e palindromo
word = "python"
print(f"'{word}' e palindromo? {is_palindrome(word)}")
```

Saida esperada:
```
Vogais em 'Python': 1
'Python' invertido: nohtyP
'arara' e palindromo? True
'python' e palindromo? False
```

> **Nota:** "Python" tem apenas 1 vogal (o "o"). As letras "P", "y", "t", "h" e "n" sao consoantes. A letra "y" não e considerada vogal neste exercício.

---

### Exercício 15 — Revisao Completa de Boas Práticas

#### Enunciado

Crie um programa completo do zero que funciona como uma calculadora de notas escolares. O programa deve receber uma lista de alunos com suas notas, calcular a media de cada aluno, determinar a situacao (aprovado, recuperacao ou reprovado) e exibir um relatório formatado. Aplique TODAS as boas práticas aprendidas neste módulo.

O programa deve:
1. Usar constantes para as notas de corte
2. Ter funções separadas para cada responsabilidade
3. Usar nomes descritivos em ingles com comentários em portugues
4. Ter docstrings em todas as funções
5. Seguir a PEP 8 (espacamento, linhas em branco, comprimento de linhas)

#### Dicas

- Defina constantes no topo: nota minima para aprovacao e para recuperacao
- Crie uma função para calcular a media
- Crie uma função para determinar a situacao
- Crie uma função para exibir o relatório
- Use uma lista de dicionários para representar os alunos

#### Proposta de Teste

Execute seu programa e verifique:
- **Caso básico:** Um aluno com notas [8, 7, 9] deve ter media 8.00 e estar "Aprovado"
- **Caso de borda:** Um aluno com notas [4, 3, 5] deve ter media 4.00 e estar "Reprovado". Um aluno com notas [5, 6, 5] deve ter media 5.33 e estar "Recuperacao"

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```python
# Constante com a nota minima para aprovacao direta
# "MIN" = minimo, "PASSING" = aprovacao, "GRADE" = nota
MIN_PASSING_GRADE = 7.0

# Constante com a nota minima para recuperacao
# "MIN" = minimo, "RECOVERY" = recuperacao, "GRADE" = nota
MIN_RECOVERY_GRADE = 5.0


def calculate_average(grades):
    """Calcula a media aritmetica de uma lista de notas.

    Parametros:
        grades (list): Lista de notas (float ou int).

    Retorna:
        float: Media aritmetica das notas.
    """
    # "grades" = notas
    # Somamos todas as notas e dividimos pela quantidade
    # "total" = total
    total = sum(grades)
    # "average" = media
    average = total / len(grades)
    return average


def determine_status(average):
    """Determina a situacao do aluno com base na media.

    Parametros:
        average (float): Media do aluno.

    Retorna:
        str: Situacao do aluno.
    """
    # "average" = media
    # Verificamos se a media atinge o minimo para aprovacao
    if average >= MIN_PASSING_GRADE:
        return "Aprovado"
    # Verificamos se a media atinge o minimo para recuperacao
    elif average >= MIN_RECOVERY_GRADE:
        return "Recuperacao"
    # Se nao atingiu nenhum minimo, esta reprovado
    else:
        return "Reprovado"


def display_report(students):
    """Exibe o relatorio de notas de todos os alunos.

    Parametros:
        students (list): Lista de dicionarios com dados dos alunos.
    """
    # "students" = estudantes/alunos
    # Exibimos o cabecalho do relatorio
    print("=" * 50)
    print("       RELATORIO DE NOTAS")
    print("=" * 50)

    # Percorremos cada aluno da lista
    # "student" = estudante
    for student in students:
        # Calculamos a media do aluno
        # "average" = media, "grades" = notas
        average = calculate_average(student["grades"])
        # Determinamos a situacao do aluno
        # "status" = situacao
        status = determine_status(average)
        # Exibimos os dados formatados
        # "name" = nome
        print(f"Aluno: {student['name']}")
        print(f"  Notas: {student['grades']}")
        print(f"  Media: {average:.2f}")
        print(f"  Situacao: {status}")
        # Linha separadora entre alunos
        print("-" * 50)


# Lista de alunos com suas notas
# "students" = estudantes
students = [
    {
        "name": "Maria",    # nome da aluna
        "grades": [8, 7, 9]  # notas da aluna
    },
    {
        "name": "Joao",     # nome do aluno
        "grades": [4, 3, 5]  # notas do aluno
    },
    {
        "name": "Ana",      # nome da aluna
        "grades": [5, 6, 5]  # notas da aluna
    },
]

# Exibimos o relatorio completo
display_report(students)
```

Saida esperada:
```
==================================================
       RELATORIO DE NOTAS
==================================================
Aluno: Maria
  Notas: [8, 7, 9]
  Media: 8.00
  Situacao: Aprovado
--------------------------------------------------
Aluno: Joao
  Notas: [4, 3, 5]
  Media: 4.00
  Situacao: Reprovado
--------------------------------------------------
Aluno: Ana
  Notas: [5, 6, 5]
  Media: 5.33
  Situacao: Recuperacao
--------------------------------------------------
```

---

[<- Voltar para o módulo](27-boas-praticas.md) | [Glossário](00-glossario.md)