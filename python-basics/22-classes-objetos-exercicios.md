# Exercícios — Módulo 22: Classes e Objetos

[<- Voltar ao Módulo 22](22-classes-objetos.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-22/` e execute com `python3 nome_do_arquivo.py`.

---

## Exercício 1 — Criar uma Classe Simples — Nível: Básico
**Conceitos:** class, __init__, atributos, print

### Enunciado
Crie uma classe chamada `Book` (livro) com os atributos `title` (título), `author` (autor) e `pages` (páginas). Crie um objeto dessa classe e exiba as informações do livro.

### Dicas
- Use `class Book:` para criar a classe
- Defina o `__init__` com `self`, `title`, `author` e `pages`
- Guarde os valores com `self.title`, `self.author` e `self.pages`
- Crie o objeto passando os valores entre parenteses

### Proposta de Teste
- Crie um livro com título "O Pequeno Principe", autor "Antoine de Saint-Exupery" e 96 páginas
- Saida esperada:
  ```
  Título: O Pequeno Principe
  Autor: Antoine de Saint-Exupery
  Páginas: 96
  ```
- Caso de borda: crie outro livro com 0 páginas — o programa deve funcionar normalmente

### Resposta Comentada
```python
# Classe Book (livro)
# "Book" = livro
class Book:
    # Construtor: define os atributos do livro
    # "self" = este livro
    # "title" = titulo, "author" = autor, "pages" = paginas
    def __init__(self, title, author, pages):
        # Guardamos o titulo no objeto
        self.title = title
        # Guardamos o autor no objeto
        self.author = author
        # Guardamos o numero de paginas no objeto
        self.pages = pages

# Criamos um objeto Book com os dados do livro
# "my_book" = meu livro
my_book = Book("O Pequeno Principe", "Antoine de Saint-Exupery", 96)

# Exibimos as informacoes acessando os atributos com ponto (.)
print(f"Titulo: {my_book.title}")
print(f"Autor: {my_book.author}")
print(f"Paginas: {my_book.pages}")
```

---

## Exercício 2 — Classe com Método Simples — Nível: Básico
**Conceitos:** class, __init__, método, self

### Enunciado
Crie uma classe chamada `Pet` (animal de estimacao) com os atributos `name` (nome) e `species` (especie). Adicione um método chamado `introduce` (apresentar) que exiba uma mensagem de apresentacao do animal.

### Dicas
- O método `introduce` deve usar `self.name` e `self.species` para acessar os dados
- Lembre-se de colocar `self` como primeiro parametro do método
- Chame o método usando `objeto.introduce()`

### Proposta de Teste
- Crie um pet com nome "Thor" e especie "Cachorro"
- Saida esperada:
  ```
  Ola! Eu sou o Thor e sou um Cachorro.
  ```
- Caso de borda: crie um pet com nome "Nemo" e especie "Peixe" — a mensagem deve se adaptar

### Resposta Comentada
```python
# Classe Pet (animal de estimacao)
# "Pet" = animal de estimacao
class Pet:
    # Construtor: define nome e especie
    # "self" = este animal
    # "name" = nome, "species" = especie
    def __init__(self, name, species):
        # Guardamos o nome do animal
        self.name = name
        # Guardamos a especie do animal
        self.species = species

    # Metodo: apresentar o animal
    # "introduce" = apresentar
    def introduce(self):
        # Usamos self.name e self.species para acessar os dados deste animal
        print(f"Ola! Eu sou o {self.name} e sou um {self.species}.")

# Criamos um animal de estimacao
# "my_pet" = meu animal de estimacao
my_pet = Pet("Thor", "Cachorro")

# Chamamos o metodo introduce — nao passamos self, o Python faz isso
my_pet.introduce()
```

---

## Exercício 3 — Classe com Método que Recebe Parametro — Nível: Básico
**Conceitos:** class, __init__, método com parametro, self

### Enunciado
Crie uma classe chamada `Counter` (contador) com um atributo `value` (valor) que comeca em 0. Adicione um método `increment` (incrementar) que receba um número e some ao valor atual. Adicione um método `show` (mostrar) que exiba o valor atual.

### Dicas
- No `__init__`, defina `self.value = 0` (sem receber parametro)
- O método `increment` recebe `self` e `amount` (quantia)
- Use `self.value = self.value + amount` para somar

### Proposta de Teste
- Crie um contador, incremente 5, depois incremente 3, e mostre o valor
- Saida esperada:
  ```
  Valor atual: 5
  Valor atual: 8
  ```
- Caso de borda: incremente 0 — o valor deve permanecer o mesmo

### Resposta Comentada
```python
# Classe Counter (contador)
# "Counter" = contador
class Counter:
    # Construtor: inicia o valor em zero
    # "self" = este contador
    def __init__(self):
        # Atributo: valor do contador, comeca em 0
        # "value" = valor
        self.value = 0

    # Metodo: incrementar o valor
    # "increment" = incrementar
    # "amount" = quantia a adicionar
    def increment(self, amount):
        # Somamos a quantia ao valor atual
        self.value = self.value + amount

    # Metodo: mostrar o valor atual
    # "show" = mostrar
    def show(self):
        # Exibimos o valor atual do contador
        print(f"Valor atual: {self.value}")

# Criamos um contador
# "my_counter" = meu contador
my_counter = Counter()

# Incrementamos 5 e mostramos
my_counter.increment(5)
my_counter.show()

# Incrementamos mais 3 e mostramos
my_counter.increment(3)
my_counter.show()
```

---

## Exercício 4 — Classe com Método que Retorna Valor — Nível: Básico
**Conceitos:** class, __init__, método com return, cálculo

### Enunciado
Crie uma classe chamada `Circle` (circulo) com o atributo `radius` (raio). Adicione um método `calculate_area` (calcular area) que retorne a area do circulo. Use a formula: area = 3.14159 * raio * raio.

### Dicas
- O método `calculate_area` deve usar `return` para devolver o resultado
- Use `self.radius` para acessar o raio dentro do método
- Guarde o resultado em uma variável antes de imprimir

### Proposta de Teste
- Crie um circulo com raio 5
- Saida esperada:
  ```
  Raio: 5
  Area: 78.54
  ```
- Caso de borda: crie um circulo com raio 1 — a area deve ser aproximadamente 3.14

### Resposta Comentada
```python
# Classe Circle (circulo)
# "Circle" = circulo
class Circle:
    # Construtor: define o raio do circulo
    # "self" = este circulo
    # "radius" = raio
    def __init__(self, radius):
        # Guardamos o raio no objeto
        self.radius = radius

    # Metodo: calcular a area do circulo
    # "calculate_area" = calcular area
    # Formula: area = pi * raio * raio (pi = 3.14159)
    def calculate_area(self):
        # Calculamos e retornamos a area
        # "area" = area
        area = 3.14159 * self.radius * self.radius
        return area

# Criamos um circulo com raio 5
# "my_circle" = meu circulo
my_circle = Circle(5)

# Chamamos o metodo e guardamos o resultado
# "area" = area
area = my_circle.calculate_area()

# Exibimos o raio e a area formatada com 2 casas decimais
print(f"Raio: {my_circle.radius}")
print(f"Area: {area:.2f}")
```

---

## Exercício 5 — Classe Produto com Desconto — Nível: Intermediario
**Conceitos:** class, __init__, método com cálculo, validação

### Enunciado
Crie uma classe chamada `Product` (produto) com os atributos `name` (nome) e `price` (preco). Adicione um método `apply_discount` (aplicar desconto) que receba uma porcentagem de desconto e retorne o preco com desconto. O desconto deve ser entre 0 e 100.

### Dicas
- O desconto e uma porcentagem: 10 significa 10%
- Formula: preco com desconto = preco * (1 - desconto / 100)
- Verifique se o desconto esta entre 0 e 100 antes de calcular

### Proposta de Teste
- Crie um produto "Notebook" com preco 2500.00 e aplique 15% de desconto
- Saida esperada:
  ```
  Produto: Notebook
  Preco original: R$ 2500.00
  Desconto: 15%
  Preco com desconto: R$ 2125.00
  ```
- Caso de borda: aplique 0% de desconto — o preco deve permanecer o mesmo

### Resposta Comentada
```python
# Classe Product (produto)
# "Product" = produto
class Product:
    # Construtor: define nome e preco
    # "self" = este produto
    # "name" = nome, "price" = preco
    def __init__(self, name, price):
        # Guardamos o nome do produto
        self.name = name
        # Guardamos o preco do produto
        self.price = price

    # Metodo: aplicar desconto e retornar o preco com desconto
    # "apply_discount" = aplicar desconto
    # "percentage" = porcentagem
    def apply_discount(self, percentage):
        # Verificamos se a porcentagem e valida (entre 0 e 100)
        if percentage < 0 or percentage > 100:
            # Se nao for valida, retornamos o preco original
            print("Erro: desconto deve ser entre 0 e 100.")
            return self.price
        # Calculamos o preco com desconto
        # "discounted_price" = preco com desconto
        # Formula: preco * (1 - porcentagem / 100)
        discounted_price = self.price * (1 - percentage / 100)
        return discounted_price

# Criamos um produto
# "notebook" = notebook/caderno (neste caso, computador portatil)
notebook = Product("Notebook", 2500.00)

# Aplicamos 15% de desconto
# "discount" = desconto
discount = 15
# "final_price" = preco final
final_price = notebook.apply_discount(discount)

# Exibimos as informacoes
print(f"Produto: {notebook.name}")
print(f"Preco original: R$ {notebook.price:.2f}")
print(f"Desconto: {discount}%")
print(f"Preco com desconto: R$ {final_price:.2f}")
```

---

## Exercício 6 — Classe com Lista como Atributo — Nível: Intermediario
**Conceitos:** class, __init__, lista, append, método

### Enunciado
Crie uma classe chamada `ShoppingList` (lista de compras) com um atributo `items` (itens) que comeca como uma lista vazia. Adicione um método `add_item` (adicionar item) e um método `show_items` (mostrar itens) que exiba todos os itens numerados.

### Dicas
- No `__init__`, defina `self.items = []`
- Use `self.items.append(item)` para adicionar
- Use `enumerate()` com `start=1` para numerar os itens

### Proposta de Teste
- Adicione "Arroz", "Feijao" e "Leite" a lista
- Saida esperada:
  ```
  Lista de Compras:
  1. Arroz
  2. Feijao
  3. Leite
  Total de itens: 3
  ```
- Caso de borda: chame `show_items` com a lista vazia — deve exibir "A lista esta vazia."

### Resposta Comentada
```python
# Classe ShoppingList (lista de compras)
# "ShoppingList" = lista de compras
class ShoppingList:
    # Construtor: cria uma lista vazia de itens
    # "self" = esta lista de compras
    def __init__(self):
        # Atributo: lista de itens, comeca vazia
        # "items" = itens
        self.items = []

    # Metodo: adicionar um item a lista
    # "add_item" = adicionar item
    # "item" = item/produto
    def add_item(self, item):
        # Adicionamos o item na lista
        self.items.append(item)
        print(f"'{item}' adicionado a lista.")

    # Metodo: mostrar todos os itens da lista
    # "show_items" = mostrar itens
    def show_items(self):
        # Verificamos se a lista esta vazia
        if len(self.items) == 0:
            print("A lista esta vazia.")
            return
        # Exibimos o cabecalho
        print("Lista de Compras:")
        # Percorremos a lista com enumerate para numerar
        # enumerate() retorna o indice e o valor de cada item
        # start=1 faz a numeracao comecar em 1
        for index, item in enumerate(self.items, start=1):
            # "index" = indice/numero, "item" = item
            print(f"{index}. {item}")
        # Exibimos o total de itens
        # len() conta quantos itens tem na lista
        print(f"Total de itens: {len(self.items)}")

# Criamos uma lista de compras
# "my_list" = minha lista
my_list = ShoppingList()

# Adicionamos itens
my_list.add_item("Arroz")
my_list.add_item("Feijao")
my_list.add_item("Leite")

# Exibimos a lista completa
print()
my_list.show_items()
```

---

## Exercício 7 — Classe Conta Bancaria — Nível: Intermediario
**Conceitos:** class, __init__, métodos, validação, atributos

### Enunciado
Crie uma classe chamada `BankAccount` (conta bancaria) com os atributos `owner` (titular) e `balance` (saldo, comecando em 0). Adicione métodos `deposit` (depositar), `withdraw` (sacar) e `show_balance` (mostrar saldo). O saque não deve permitir saldo negativo.

### Dicas
- No `withdraw`, verifique se o saldo e suficiente antes de sacar
- Use `self.balance` para acessar e modificar o saldo
- Exiba mensagens informativas em cada operação

### Proposta de Teste
- Crie uma conta para "Maria", deposite 500, saque 200, e mostre o saldo
- Saida esperada:
  ```
  Deposito de R$ 500.00 realizado.
  Saque de R$ 200.00 realizado.
  Saldo de Maria: R$ 300.00
  ```
- Caso de borda: tente sacar 1000 de uma conta com saldo 300 — deve exibir mensagem de erro

### Resposta Comentada
```python
# Classe BankAccount (conta bancaria)
# "BankAccount" = conta bancaria
class BankAccount:
    # Construtor: define o titular e o saldo inicial (zero)
    # "self" = esta conta
    # "owner" = titular/dono
    def __init__(self, owner):
        # Guardamos o nome do titular
        self.owner = owner
        # Saldo comeca em zero
        # "balance" = saldo
        self.balance = 0

    # Metodo: depositar dinheiro
    # "deposit" = depositar
    # "amount" = quantia
    def deposit(self, amount):
        # Verificamos se a quantia e positiva
        if amount > 0:
            # Somamos ao saldo
            self.balance = self.balance + amount
            print(f"Deposito de R$ {amount:.2f} realizado.")
        else:
            # Quantia invalida
            print("Erro: valor de deposito deve ser positivo.")

    # Metodo: sacar dinheiro
    # "withdraw" = sacar
    # "amount" = quantia
    def withdraw(self, amount):
        # Verificamos se ha saldo suficiente
        if amount > self.balance:
            print(f"Erro: saldo insuficiente. Saldo atual: R$ {self.balance:.2f}")
        elif amount <= 0:
            # Quantia invalida
            print("Erro: valor de saque deve ser positivo.")
        else:
            # Subtraimos do saldo
            self.balance = self.balance - amount
            print(f"Saque de R$ {amount:.2f} realizado.")

    # Metodo: mostrar o saldo
    # "show_balance" = mostrar saldo
    def show_balance(self):
        # Exibimos o saldo formatado
        print(f"Saldo de {self.owner}: R$ {self.balance:.2f}")

# Criamos uma conta bancaria
# "account" = conta
account = BankAccount("Maria")

# Depositamos R$ 500
account.deposit(500)

# Sacamos R$ 200
account.withdraw(200)

# Mostramos o saldo
account.show_balance()
```

---

## Exercício 8 — Classe Retangulo com Perimetro e Area — Nível: Intermediario
**Conceitos:** class, __init__, métodos com return, cálculo

### Enunciado
Crie uma classe chamada `Rectangle` (retangulo) com os atributos `width` (largura) e `height` (altura). Adicione métodos `calculate_area` (calcular area), `calculate_perimeter` (calcular perimetro) e `is_square` (e quadrado) que retorne `True` se largura e altura forem iguais.

### Dicas
- Area = largura * altura
- Perimetro = 2 * (largura + altura)
- Um quadrado tem largura igual a altura

### Proposta de Teste
- Crie um retangulo 8 por 5
- Saida esperada:
  ```
  Largura: 8 | Altura: 5
  Area: 40
  Perimetro: 26
  E quadrado? Não
  ```
- Caso de borda: crie um retangulo 4 por 4 — deve indicar que e quadrado

### Resposta Comentada
```python
# Classe Rectangle (retangulo)
# "Rectangle" = retangulo
class Rectangle:
    # Construtor: define largura e altura
    # "self" = este retangulo
    # "width" = largura, "height" = altura
    def __init__(self, width, height):
        # Guardamos a largura
        self.width = width
        # Guardamos a altura
        self.height = height

    # Metodo: calcular a area
    # "calculate_area" = calcular area
    def calculate_area(self):
        # Area = largura multiplicada pela altura
        return self.width * self.height

    # Metodo: calcular o perimetro
    # "calculate_perimeter" = calcular perimetro
    def calculate_perimeter(self):
        # Perimetro = 2 vezes a soma de largura e altura
        return 2 * (self.width + self.height)

    # Metodo: verificar se e um quadrado
    # "is_square" = e quadrado
    def is_square(self):
        # Um quadrado tem largura igual a altura
        return self.width == self.height

# Criamos um retangulo 8 por 5
# "rect" = retangulo (abreviacao)
rect = Rectangle(8, 5)

# Exibimos as dimensoes
print(f"Largura: {rect.width} | Altura: {rect.height}")

# Calculamos e exibimos area e perimetro
print(f"Area: {rect.calculate_area()}")
print(f"Perimetro: {rect.calculate_perimeter()}")

# Verificamos se e quadrado
# Usamos "Sim" ou "Nao" baseado no resultado booleano
# "square_text" = texto sobre ser quadrado
square_text = "Sim" if rect.is_square() else "Nao"
print(f"E quadrado? {square_text}")
```

---

## Exercício 9 — Classe Aluno com Media — Nível: Intermediario
**Conceitos:** class, __init__, lista, método com cálculo, len, sum

### Enunciado
Crie uma classe chamada `Student` (estudante) com os atributos `name` (nome) e `grades` (notas, lista vazia). Adicione métodos `add_grade` (adicionar nota), `calculate_average` (calcular media) e `status` que retorne "Aprovado" se a media for >= 7.0 ou "Reprovado" caso contrario.

### Dicas
- Use `self.grades = []` no `__init__`
- No `calculate_average`, verifique se a lista não esta vazia antes de dividir
- No `status`, chame `self.calculate_average()` para obter a media

### Proposta de Teste
- Crie um aluno "Pedro" com notas 8.0, 6.5 e 9.0
- Saida esperada:
  ```
  Aluno: Pedro
  Notas: [8.0, 6.5, 9.0]
  Media: 7.83
  Situacao: Aprovado
  ```
- Caso de borda: crie um aluno com notas 4.0, 5.0 e 3.0 — deve ser "Reprovado"

### Resposta Comentada
```python
# Classe Student (estudante)
# "Student" = estudante
class Student:
    # Construtor: define o nome e cria lista vazia de notas
    # "self" = este estudante
    # "name" = nome
    def __init__(self, name):
        # Guardamos o nome do estudante
        self.name = name
        # Lista de notas comeca vazia
        # "grades" = notas
        self.grades = []

    # Metodo: adicionar uma nota
    # "add_grade" = adicionar nota
    # "grade" = nota
    def add_grade(self, grade):
        # Adicionamos a nota na lista
        self.grades.append(grade)

    # Metodo: calcular a media das notas
    # "calculate_average" = calcular media
    def calculate_average(self):
        # Verificamos se existem notas
        if len(self.grades) == 0:
            # Se nao houver notas, retornamos 0
            return 0
        # Calculamos a media: soma das notas dividida pela quantidade
        # sum() soma todos os valores, len() conta quantos tem
        return sum(self.grades) / len(self.grades)

    # Metodo: verificar a situacao do aluno
    # "status" = situacao
    def status(self):
        # Calculamos a media chamando o outro metodo
        # "average" = media
        average = self.calculate_average()
        # Se a media for maior ou igual a 7.0, esta aprovado
        if average >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"

# Criamos um estudante
# "student" = estudante
student = Student("Pedro")

# Adicionamos notas
student.add_grade(8.0)
student.add_grade(6.5)
student.add_grade(9.0)

# Exibimos o boletim
print(f"Aluno: {student.name}")
print(f"Notas: {student.grades}")
print(f"Media: {student.calculate_average():.2f}")
print(f"Situacao: {student.status()}")
```

---

## Exercício 10 — Criar Multiplos Objetos e Percorrer com For — Nível: Intermediario
**Conceitos:** class, __init__, lista de objetos, for, método

### Enunciado
Crie uma classe chamada `Fruit` (fruta) com os atributos `name` (nome) e `price_per_kg` (preco por quilo). Crie uma lista com 4 frutas diferentes e percorra a lista exibindo o nome e preco de cada uma. Ao final, exiba a fruta mais cara.

### Dicas
- Crie os objetos e coloque-os em uma lista
- Use um loop `for` para percorrer a lista
- Para encontrar a mais cara, compare os precos dentro do loop

### Proposta de Teste
- Frutas: Maca (R$ 6.50), Banana (R$ 3.99), Uva (R$ 12.00), Laranja (R$ 4.50)
- Saida esperada:
  ```
  Maca: R$ 6.50/kg
  Banana: R$ 3.99/kg
  Uva: R$ 12.00/kg
  Laranja: R$ 4.50/kg
  Fruta mais cara: Uva (R$ 12.00/kg)
  ```
- Caso de borda: se duas frutas tiverem o mesmo preco mais alto, exiba a primeira encontrada

### Resposta Comentada
```python
# Classe Fruit (fruta)
# "Fruit" = fruta
class Fruit:
    # Construtor: define nome e preco por quilo
    # "self" = esta fruta
    # "name" = nome, "price_per_kg" = preco por quilo
    def __init__(self, name, price_per_kg):
        # Guardamos o nome da fruta
        self.name = name
        # Guardamos o preco por quilo
        self.price_per_kg = price_per_kg

# Criamos uma lista de frutas
# "fruits" = frutas
fruits = [
    Fruit("Maca", 6.50),
    Fruit("Banana", 3.99),
    Fruit("Uva", 12.00),
    Fruit("Laranja", 4.50)
]

# Variavel para guardar a fruta mais cara
# "most_expensive" = mais cara
most_expensive = fruits[0]

# Percorremos a lista de frutas
# "fruit" = fruta (cada item da lista)
for fruit in fruits:
    # Exibimos o nome e preco de cada fruta
    print(f"{fruit.name}: R$ {fruit.price_per_kg:.2f}/kg")
    # Verificamos se esta fruta e mais cara que a atual mais cara
    if fruit.price_per_kg > most_expensive.price_per_kg:
        # Atualizamos a fruta mais cara
        most_expensive = fruit

# Exibimos a fruta mais cara
print(f"Fruta mais cara: {most_expensive.name} (R$ {most_expensive.price_per_kg:.2f}/kg)")
```

---

## Exercício 11 — Classe Tarefa com Status — Nível: Avancado
**Conceitos:** class, __init__, métodos, atributo booleano, lógica condicional

### Enunciado
Crie uma classe chamada `Task` (tarefa) com os atributos `description` (descricao) e `done` (concluida, comecando como `False`). Adicione métodos `complete` (concluir) que marque a tarefa como feita, e `show` (mostrar) que exiba a tarefa com um indicador de status: `[X]` para concluida e `[ ]` para pendente. Crie 3 tarefas, conclua apenas uma, e exiba todas.

### Dicas
- No `__init__`, defina `self.done = False`
- No método `complete`, mude `self.done` para `True`
- No método `show`, use um condicional para escolher `[X]` ou `[ ]`

### Proposta de Teste
- Tarefas: "Estudar Python", "Fazer exercícios", "Revisar código"
- Conclua apenas "Estudar Python"
- Saida esperada:
  ```
  [X] Estudar Python
  [ ] Fazer exercícios
  [ ] Revisar código
  Concluidas: 1 de 3
  ```
- Caso de borda: conclua todas as tarefas — todas devem mostrar `[X]`

### Resposta Comentada
```python
# Classe Task (tarefa)
# "Task" = tarefa
class Task:
    # Construtor: define a descricao e o status (pendente)
    # "self" = esta tarefa
    # "description" = descricao da tarefa
    def __init__(self, description):
        # Guardamos a descricao da tarefa
        self.description = description
        # A tarefa comeca como nao concluida
        # "done" = concluida/feita
        self.done = False

    # Metodo: marcar a tarefa como concluida
    # "complete" = concluir/completar
    def complete(self):
        # Mudamos o status para True (concluida)
        self.done = True

    # Metodo: exibir a tarefa com indicador de status
    # "show" = mostrar
    def show(self):
        # Escolhemos o indicador baseado no status
        # "status_icon" = icone de status
        if self.done:
            status_icon = "[X]"
        else:
            status_icon = "[ ]"
        # Exibimos o indicador seguido da descricao
        print(f"{status_icon} {self.description}")

# Criamos uma lista de tarefas
# "tasks" = tarefas
tasks = [
    Task("Estudar Python"),
    Task("Fazer exercicios"),
    Task("Revisar codigo")
]

# Concluimos apenas a primeira tarefa
tasks[0].complete()

# Exibimos todas as tarefas
# "task" = tarefa (cada item da lista)
for task in tasks:
    task.show()

# Contamos quantas foram concluidas
# "completed_count" = contagem de concluidas
completed_count = 0
for task in tasks:
    if task.done:
        completed_count = completed_count + 1

# Exibimos o resumo
print(f"Concluidas: {completed_count} de {len(tasks)}")
```

---

## Exercício 12 — Classe Turma com Alunos — Nível: Avancado
**Conceitos:** class, __init__, objetos dentro de objetos, lista de objetos, métodos

### Enunciado
Crie duas classes: `Student` (estudante) com `name` (nome) e `grade` (nota), e `Classroom` (turma) com `name` (nome da turma) e `students` (lista de alunos). A classe `Classroom` deve ter métodos `add_student` (adicionar aluno), `calculate_class_average` (calcular media da turma) e `show_report` (mostrar relatório). Adicione 3 alunos a turma e exiba o relatório.

### Dicas
- A classe `Classroom` guarda objetos `Student` na sua lista
- No `calculate_class_average`, percorra a lista de alunos e some as notas
- Um objeto pode conter outros objetos — isso e muito comum em programação

### Proposta de Teste
- Turma "Python Básico" com alunos: Ana (8.5), Bruno (6.0), Carla (9.5)
- Saida esperada:
  ```
  Turma: Python Básico
  Alunos:
    Ana - Nota: 8.5
    Bruno - Nota: 6.0
    Carla - Nota: 9.5
  Media da turma: 8.00
  ```
- Caso de borda: turma sem alunos — a media deve ser 0 e a lista deve indicar "Nenhum aluno"

### Resposta Comentada
```python
# Classe Student (estudante)
# "Student" = estudante
class Student:
    # Construtor: define nome e nota
    # "self" = este estudante
    # "name" = nome, "grade" = nota
    def __init__(self, name, grade):
        # Guardamos o nome do estudante
        self.name = name
        # Guardamos a nota do estudante
        self.grade = grade

# Classe Classroom (turma/sala de aula)
# "Classroom" = turma/sala de aula
class Classroom:
    # Construtor: define o nome da turma e cria lista vazia de alunos
    # "self" = esta turma
    # "name" = nome da turma
    def __init__(self, name):
        # Guardamos o nome da turma
        self.name = name
        # Lista de alunos comeca vazia
        # "students" = estudantes/alunos
        self.students = []

    # Metodo: adicionar um aluno a turma
    # "add_student" = adicionar estudante
    # "student" = estudante (um objeto da classe Student)
    def add_student(self, student):
        # Adicionamos o objeto estudante na lista
        self.students.append(student)

    # Metodo: calcular a media da turma
    # "calculate_class_average" = calcular media da turma
    def calculate_class_average(self):
        # Verificamos se ha alunos na turma
        if len(self.students) == 0:
            return 0
        # Somamos todas as notas
        # "total" = total
        total = 0
        # "student" = estudante (cada aluno da lista)
        for student in self.students:
            # Somamos a nota de cada aluno
            total = total + student.grade
        # Dividimos pelo numero de alunos
        return total / len(self.students)

    # Metodo: exibir o relatorio da turma
    # "show_report" = mostrar relatorio
    def show_report(self):
        # Exibimos o nome da turma
        print(f"Turma: {self.name}")
        print("Alunos:")
        # Verificamos se ha alunos
        if len(self.students) == 0:
            print("  Nenhum aluno")
        else:
            # Percorremos a lista de alunos
            for student in self.students:
                # Exibimos nome e nota de cada aluno
                print(f"  {student.name} - Nota: {student.grade}")
        # Calculamos e exibimos a media
        # "average" = media
        average = self.calculate_class_average()
        print(f"Media da turma: {average:.2f}")

# Criamos a turma
# "classroom" = turma
classroom = Classroom("Python Basico")

# Criamos alunos e adicionamos a turma
# Cada aluno e um objeto Student que e adicionado a lista da turma
classroom.add_student(Student("Ana", 8.5))
classroom.add_student(Student("Bruno", 6.0))
classroom.add_student(Student("Carla", 9.5))

# Exibimos o relatorio completo
classroom.show_report()
```

---

[<- Voltar ao Módulo 22](22-classes-objetos.md) | [Glossário](00-glossario.md)
