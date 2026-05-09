# 22 — Classes e Objetos: Introdução a Orientacao a Objetos

[<- Anterior: Manipulação JSON](21-manipulacao-json.md) | [Glossário](00-glossario.md) | [Próximo: Exercícios Integradores ->](23-exercicios-integradores.md)

---

## Introdução

Ate agora, você aprendeu a usar variáveis, listas, dicionários, funções e ate a trabalhar com arquivos e JSON. Todos esses conceitos sao ferramentas poderosas, mas existe uma forma de organizar seu código que junta **dados** e **ações** em um único lugar. Essa forma se chama **Orientacao a Objetos**.

Imagine que você esta organizando uma cozinha. Você tem ingredientes (dados) espalhados pela bancada e receitas (ações) escritas em papeis separados. Funciona, mas pode ficar confuso. Agora imagine que você tem um **caderno de receitas** onde cada receita ja vem com a lista de ingredientes necessários e o passo a passo para preparar o prato. Tudo junto, organizado em um único lugar. Isso e o que a Orientacao a Objetos faz com o seu código.

Neste módulo, você vai aprender os conceitos **básicos** de Orientacao a Objetos:

- O que e uma **classe** (o molde/receita)
- O que e um **objeto** (o produto criado a partir do molde)
- Como definir **atributos** (os dados do objeto)
- Como criar **métodos** (as ações do objeto)
- O que e o **self** (a referência ao proprio objeto)
- Como usar o **__init__** (o construtor da classe)

> **Nota importante:** Orientacao a Objetos e um tema vasto. Neste módulo, vamos cobrir apenas o essencial para que você consiga entender e usar classes simples. Conceitos avancados como herança, polimorfismo e classes abstratas existem, mas estão fora do escopo deste curso. Não se preocupe com eles agora.

> **Dica:** Consulte o [Glossário](00-glossario.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-22/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-22`
4. Execute: `python3 nome_do_arquivo.py`

---

## O Que e uma Classe

Vamos começar com uma analogia que todo mundo conhece: uma **receita de bolo**.

Quando você tem uma receita de bolo, você tem um **papel** que descreve:

- **Ingredientes:** farinha, ovos, açúcar, leite (esses sao os **dados**)
- **Modo de preparo:** misturar, bater, assar (essas sao as **ações**)

A receita em si **não e um bolo**. Ela e um **molde**, um **modelo**, um **conjunto de instruções** que explica como criar um bolo. A partir de uma única receita, você pode fazer 1 bolo, 5 bolos, 100 bolos — todos seguindo o mesmo modelo.

Em programação, uma **classe** e exatamente isso: um **molde** que descreve quais dados um objeto vai ter e quais ações ele pode realizar.

Outros exemplos de "moldes" no dia a dia:

- Uma **planta de casa** e um molde. A partir dela, você pode construir várias casas iguais.
- Um **formulário de cadastro** e um molde. Cada pessoa preenche com seus proprios dados.
- Uma **ficha de produto** e um molde. Cada produto tem seu nome, preco e quantidade.

### Classe em Python

Em Python, criamos uma classe usando a palavra `class`:

```python
# Criamos uma classe chamada Cake (bolo)
# "Cake" = bolo
# Uma classe e como uma receita — um molde para criar objetos
class Cake:
    pass
```

> **Nota:** A palavra `pass` significa "não faca nada". Usamos ela quando queremos criar uma classe vazia por enquanto. Vamos preencher a classe aos poucos.

> **Convencao de nome:** Classes em Python usam o formato **CamelCase** (cada palavra comeca com letra maiuscula, sem espacos ou underscores). Exemplos: `Cake`, `Product`, `StudentRecord`. Isso e diferente de variáveis e funções, que usam **snake_case** (letras minusculas separadas por underscores).

---

## O Que e um Objeto

Se a classe e a **receita**, o objeto e o **bolo pronto**.

Quando você segue uma receita e faz um bolo, você criou um **objeto** a partir daquela receita. Cada bolo e independente: você pode comer um e guardar o outro. Se você colocar cobertura de chocolate em um bolo, o outro não muda.

Em programação, um **objeto** e uma **instância** de uma classe. "Instância" e so uma palavra técnica que significa "um exemplar criado a partir do molde".

Vamos criar objetos a partir da nossa classe `Cake`:

```python
# Criamos uma classe chamada Cake (bolo)
# "Cake" = bolo
class Cake:
    pass

# Criamos dois objetos (instancias) a partir da classe Cake
# "chocolate_cake" = bolo de chocolate
# "vanilla_cake" = bolo de baunilha
# Para criar um objeto, usamos o nome da classe seguido de parenteses
chocolate_cake = Cake()
vanilla_cake = Cake()

# Cada objeto e independente — sao bolos diferentes
# type() mostra de qual classe o objeto foi criado
print(type(chocolate_cake))
print(type(vanilla_cake))

# Verificamos se sao objetos diferentes
# "is" verifica se sao o mesmo objeto na memoria
print(chocolate_cake is vanilla_cake)
```

Saida esperada:
```
<class '__main__.Cake'>
<class '__main__.Cake'>
False
```

Repare que ambos os objetos sao do tipo `Cake`, mas sao objetos **diferentes** (por isso `False` na ultima linha). E como dois bolos feitos com a mesma receita — sao bolos iguais no formato, mas sao bolos separados.

---

## Criando a Primeira Classe com Dados: O Método __init__

Uma classe vazia não e muito útil. Precisamos que nossos objetos guardem **dados**. Para isso, usamos um método especial chamado `__init__`.

### O Que e o __init__?

O `__init__` (leia "init" ou "dunder init") e o **construtor** da classe. Ele e um método especial que o Python chama **automaticamente** toda vez que você cria um novo objeto.

Pense no `__init__` como o momento em que você **preenche a ficha** de um novo produto na loja. Quando um produto novo chega, você precisa anotar o nome, o preco e a quantidade. O `__init__` e o momento em que essas informações sao registradas.

> **Por que tem dois underscores de cada lado?** Em Python, métodos com dois underscores no inicio e no fim (como `__init__`) sao chamados de **métodos especiais** ou **métodos magicos** (magic methods). O Python os reconhece e os chama automaticamente em situacoes especificas. O `__init__` e chamado quando um objeto e criado.

Vamos criar uma classe `Product` (produto) com dados:

```python
# Criamos a classe Product (produto)
# "Product" = produto
class Product:
    # O metodo __init__ e o construtor — e chamado automaticamente
    # quando criamos um novo objeto
    # "self" = referencia ao proprio objeto que esta sendo criado
    # "name" = nome do produto
    # "price" = preco do produto
    def __init__(self, name, price):
        # Guardamos o nome dentro do objeto
        # self.name = o atributo "name" deste objeto recebe o valor do parametro "name"
        self.name = name
        # Guardamos o preco dentro do objeto
        # self.price = o atributo "price" deste objeto recebe o valor do parametro "price"
        self.price = price

# Criamos um objeto Product passando nome e preco
# "rice" = arroz
rice = Product("Arroz", 5.99)

# Acessamos os dados do objeto usando ponto (.)
# rice.name = o nome do objeto rice
# rice.price = o preco do objeto rice
print(rice.name)
print(rice.price)
```

Saida esperada:
```
Arroz
5.99
```

### Passo a Passo do Que Acontece

Vamos entender exatamente o que acontece quando escrevemos `rice = Product("Arroz", 5.99)`:

1. O Python ve que você quer criar um novo objeto da classe `Product`
2. O Python cria um objeto vazio na memória
3. O Python chama o método `__init__` automaticamente, passando:
   - `self` = o objeto recem-criado (o Python faz isso sozinho)
   - `name` = `"Arroz"` (o primeiro valor que você passou)
   - `price` = `5.99` (o segundo valor que você passou)
4. Dentro do `__init__`, os valores sao guardados no objeto com `self.name` e `self.price`
5. O objeto pronto e guardado na variável `rice`

---

## O Parametro self — Explicacao Detalhada

O `self` e provavelmente a parte mais confusa para quem esta aprendendo Orientacao a Objetos. Vamos explicar com muita calma.

### O Que e o self?

O `self` e uma **referência ao proprio objeto**. Quando você cria um método dentro de uma classe, o primeiro parametro e sempre `self`. Ele representa o objeto que esta "usando" aquele método.

### Analogia: Crachá de Identificacao

Imagine que você trabalha em uma empresa grande com muitos funcionarios. Cada pessoa tem um **crachá** com seu nome e cargo. Quando alguem pergunta "qual e o seu nome?", você olha para o **seu proprio** crachá e responde.

O `self` e como esse crachá. Ele permite que o objeto "olhe para si mesmo" e acesse seus proprios dados.

### Por Que o self e Necessário?

Quando você cria uma classe, você esta escrevendo um **molde** que sera usado por **muitos objetos diferentes**. O Python precisa saber: "quando eu disser `name`, estou falando do nome de **qual** objeto?"

O `self` resolve isso. Ele diz: "estou falando dos dados **deste** objeto específico".

```python
# Classe Animal (animal)
# "Animal" = animal
class Animal:
    # O construtor recebe o nome e o som do animal
    # "self" = este animal especifico
    # "name" = nome do animal
    # "sound" = som que o animal faz
    def __init__(self, name, sound):
        # self.name = o nome DESTE animal
        self.name = name
        # self.sound = o som DESTE animal
        self.sound = sound

# Criamos dois animais diferentes
# "dog" = cachorro
dog = Animal("Rex", "Au au")
# "cat" = gato
cat = Animal("Mimi", "Miau")

# Cada objeto tem seus proprios dados
# dog.name e o nome do cachorro, cat.name e o nome do gato
print(f"{dog.name} faz {dog.sound}")
print(f"{cat.name} faz {cat.sound}")
```

Saida esperada:
```
Rex faz Au au
Mimi faz Miau
```

Quando o Python executa `dog.name`, ele sabe que deve buscar o `name` do objeto `dog` (que e "Rex"). Quando executa `cat.name`, busca o `name` do objeto `cat` (que e "Mimi"). O `self` e o mecanismo que permite essa separacao.

### Regra Importante

O `self` e **sempre** o primeiro parametro de qualquer método dentro de uma classe. Você **não** passa o `self` quando chama o método — o Python faz isso automaticamente. Você so precisa declara-lo na definição do método.

---

## Atributos — Os Dados do Objeto

**Atributos** sao os **dados** que um objeto carrega. Sao como os campos de uma ficha cadastral: cada objeto tem seus proprios valores.

No exemplo anterior, `name` e `price` sao atributos da classe `Product`. Cada objeto `Product` tem seu proprio `name` e seu proprio `price`.

### Atributos Sao Definidos no __init__

A forma padrão de criar atributos e dentro do método `__init__`, usando `self.nome_do_atributo`:

```python
# Classe Student (estudante/aluno)
# "Student" = estudante
class Student:
    # O construtor define os atributos do estudante
    # "self" = este estudante especifico
    # "name" = nome do estudante
    # "age" = idade do estudante
    # "grade" = nota do estudante
    def __init__(self, name, age, grade):
        # Atributo: nome do estudante
        self.name = name
        # Atributo: idade do estudante
        self.age = age
        # Atributo: nota do estudante
        self.grade = grade

# Criamos um estudante
# "student_one" = estudante um
student_one = Student("Ana", 18, 8.5)

# Acessamos os atributos com ponto (.)
print(f"Nome: {student_one.name}")
print(f"Idade: {student_one.age}")
print(f"Nota: {student_one.grade}")
```

Saida esperada:
```
Nome: Ana
Idade: 18
Nota: 8.5
```

### Modificando Atributos

Você pode alterar o valor de um atributo a qualquer momento, usando o ponto (.) e o operador de atribuição (=):

```python
# Classe Student (estudante)
# "Student" = estudante
class Student:
    # Construtor com nome e nota
    # "self" = este estudante
    # "name" = nome, "grade" = nota
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Criamos um estudante com nota 7.0
# "student" = estudante
student = Student("Carlos", 7.0)
print(f"Nota antes: {student.grade}")

# Alteramos a nota do estudante
student.grade = 9.0
print(f"Nota depois: {student.grade}")
```

Saida esperada:
```
Nota antes: 7.0
Nota depois: 9.0
```

---

## Métodos — As Ações do Objeto

**Métodos** sao **funções** que pertencem a uma classe. Eles definem as **ações** que um objeto pode realizar.

Voltando a analogia da receita de bolo: os ingredientes sao os **atributos** (dados) e o modo de preparo sao os **métodos** (ações).

### Criando Métodos

Um método e criado da mesma forma que uma função (com `def`), mas dentro da classe e com `self` como primeiro parametro:

```python
# Classe Dog (cachorro)
# "Dog" = cachorro
class Dog:
    # Construtor: define o nome e a raca do cachorro
    # "self" = este cachorro
    # "name" = nome, "breed" = raca
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    # Metodo: o cachorro late
    # "bark" = latir
    # self e o primeiro parametro — referencia ao proprio cachorro
    def bark(self):
        # Usamos self.name para acessar o nome DESTE cachorro
        print(f"{self.name} diz: Au au!")

    # Metodo: apresentar o cachorro
    # "introduce" = apresentar
    def introduce(self):
        # Usamos self.name e self.breed para acessar os dados DESTE cachorro
        # "breed" = raca
        print(f"Ola! Eu sou o {self.name} e sou da raca {self.breed}.")

# Criamos um cachorro
# "my_dog" = meu cachorro
my_dog = Dog("Rex", "Labrador")

# Chamamos os metodos do objeto
# Repare que NAO passamos o self — o Python faz isso automaticamente
my_dog.bark()
my_dog.introduce()
```

Saida esperada:
```
Rex diz: Au au!
Ola! Eu sou o Rex e sou da raca Labrador.
```

### Métodos com Parametros Adicionais

Métodos podem receber parametros além do `self`, assim como funções normais:

```python
# Classe BankAccount (conta bancaria)
# "BankAccount" = conta bancaria
class BankAccount:
    # Construtor: define o titular e o saldo inicial
    # "self" = esta conta
    # "owner" = titular/dono da conta
    # "balance" = saldo
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # Metodo: depositar dinheiro na conta
    # "deposit" = depositar
    # "amount" = quantia/valor
    def deposit(self, amount):
        # Somamos a quantia ao saldo atual
        self.balance = self.balance + amount
        print(f"Deposito de R$ {amount:.2f} realizado.")

    # Metodo: exibir o saldo atual
    # "show_balance" = mostrar saldo
    def show_balance(self):
        # "balance" = saldo
        print(f"Saldo de {self.owner}: R$ {self.balance:.2f}")

# Criamos uma conta bancaria
# "account" = conta
account = BankAccount("Maria", 100.00)

# Exibimos o saldo inicial
account.show_balance()

# Fazemos um deposito de R$ 50.00
account.deposit(50.00)

# Exibimos o saldo atualizado
account.show_balance()
```

Saida esperada:
```
Saldo de Maria: R$ 100.00
Deposito de R$ 50.00 realizado.
Saldo de Maria: R$ 150.00
```

Repare que quando chamamos `account.deposit(50.00)`, passamos apenas o valor `50.00`. O Python automaticamente passa o objeto `account` como `self`. Dentro do método, `self.balance` se refere ao saldo **desta** conta específica.

---

## Métodos Que Retornam Valores

Assim como funções, métodos podem **retornar** valores usando `return`. Nem todo método precisa imprimir algo na tela — muitas vezes, queremos que o método faca um cálculo e nos devolva o resultado.

```python
# Classe Rectangle (retangulo)
# "Rectangle" = retangulo
class Rectangle:
    # Construtor: define a largura e a altura
    # "self" = este retangulo
    # "width" = largura
    # "height" = altura
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Metodo: calcular a area do retangulo
    # "calculate_area" = calcular area
    # Area = largura multiplicada pela altura
    def calculate_area(self):
        # Retornamos o resultado do calculo
        return self.width * self.height

    # Metodo: calcular o perimetro do retangulo
    # "calculate_perimeter" = calcular perimetro
    # Perimetro = soma de todos os lados = 2 * (largura + altura)
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Criamos um retangulo de 5 por 3
# "my_rectangle" = meu retangulo
my_rectangle = Rectangle(5, 3)

# Chamamos os metodos e guardamos os resultados em variaveis
# "area" = area
area = my_rectangle.calculate_area()
# "perimeter" = perimetro
perimeter = my_rectangle.calculate_perimeter()

print(f"Largura: {my_rectangle.width}")
print(f"Altura: {my_rectangle.height}")
print(f"Area: {area}")
print(f"Perimetro: {perimeter}")
```

Saida esperada:
```
Largura: 5
Altura: 3
Area: 15
Perimetro: 16
```

---

## Criando Multiplos Objetos

Uma das grandes vantagens das classes e que você pode criar **quantos objetos quiser** a partir do mesmo molde. Cada objeto e independente e tem seus proprios dados.

Pense em uma fábrica de carros: o **projeto do carro** e a classe, e cada **carro que sai da linha de montagem** e um objeto. Todos seguem o mesmo projeto, mas cada um tem sua propria cor, placa e quilometragem.

```python
# Classe Product (produto)
# "Product" = produto
class Product:
    # Construtor: define nome, preco e quantidade
    # "self" = este produto
    # "name" = nome, "price" = preco, "quantity" = quantidade
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Metodo: exibir informacoes do produto
    # "display_info" = exibir informacoes
    def display_info(self):
        print(f"Produto: {self.name}")
        print(f"  Preco: R$ {self.price:.2f}")
        print(f"  Quantidade: {self.quantity}")

# Criamos tres produtos diferentes a partir da mesma classe
# "rice" = arroz
rice = Product("Arroz", 5.99, 100)
# "beans" = feijao
beans = Product("Feijao", 8.49, 50)
# "pasta" = macarrao
pasta = Product("Macarrao", 3.29, 200)

# Cada objeto tem seus proprios dados
rice.display_info()
print()
beans.display_info()
print()
pasta.display_info()
```

Saida esperada:
```
Produto: Arroz
  Preco: R$ 5.99
  Quantidade: 100

Produto: Feijao
  Preco: R$ 8.49
  Quantidade: 50

Produto: Macarrao
  Preco: R$ 3.29
  Quantidade: 200
```

### Objetos em Listas

Você pode guardar objetos dentro de listas, assim como faz com números ou strings:

```python
# Classe Product (produto)
# "Product" = produto
class Product:
    # Construtor com nome e preco
    # "self" = este produto
    # "name" = nome, "price" = preco
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Criamos uma lista de produtos
# "products" = produtos
products = [
    Product("Arroz", 5.99),
    Product("Feijao", 8.49),
    Product("Macarrao", 3.29)
]

# Percorremos a lista e exibimos cada produto
# "product" = produto (cada item da lista)
for product in products:
    print(f"{product.name}: R$ {product.price:.2f}")

# Calculamos o total
# "total" = total
total = 0
for product in products:
    # Somamos o preco de cada produto ao total
    total = total + product.price

print(f"Total: R$ {total:.2f}")
```

Saida esperada:
```
Arroz: R$ 5.99
Feijao: R$ 8.49
Macarrao: R$ 3.29
Total: R$ 17.77
```

---

## Exemplo Prático Completo: Classe Aluno com Notas

Vamos criar um exemplo mais completo que combina tudo o que aprendemos. Vamos modelar um **aluno** que tem nome, uma lista de notas, e métodos para adicionar notas e calcular a media.

Este exemplo mostra como uma classe pode usar uma **lista** como atributo — combinando o que você aprendeu no módulo de estruturas de dados com Orientacao a Objetos.

```python
# Classe Student (estudante/aluno)
# "Student" = estudante
class Student:
    # Construtor: define o nome e cria uma lista vazia de notas
    # "self" = este estudante
    # "name" = nome do estudante
    def __init__(self, name):
        # Atributo: nome do estudante
        self.name = name
        # Atributo: lista de notas — comeca vazia
        # "grades" = notas
        self.grades = []

    # Metodo: adicionar uma nota a lista
    # "add_grade" = adicionar nota
    # "grade" = nota
    def add_grade(self, grade):
        # Adicionamos a nota na lista de notas deste estudante
        self.grades.append(grade)
        print(f"Nota {grade} adicionada para {self.name}.")

    # Metodo: calcular a media das notas
    # "calculate_average" = calcular media
    def calculate_average(self):
        # Verificamos se existem notas na lista
        if len(self.grades) == 0:
            # Se nao houver notas, retornamos 0
            return 0
        # Somamos todas as notas e dividimos pela quantidade
        # sum() = soma todos os valores da lista
        # len() = conta quantos itens tem na lista
        total = sum(self.grades)
        average = total / len(self.grades)
        return average

    # Metodo: exibir o boletim do estudante
    # "show_report" = mostrar boletim/relatorio
    def show_report(self):
        print(f"Aluno: {self.name}")
        print(f"Notas: {self.grades}")
        # Chamamos o metodo calculate_average() usando self
        # Um metodo pode chamar outro metodo da mesma classe
        average = self.calculate_average()
        print(f"Media: {average:.1f}")

# Criamos um estudante
# "student" = estudante
student = Student("Ana")

# Adicionamos notas
student.add_grade(8.0)
student.add_grade(7.5)
student.add_grade(9.0)

# Exibimos o boletim
print()
student.show_report()
```

Saida esperada:
```
Nota 8.0 adicionada para Ana.
Nota 7.5 adicionada para Ana.
Nota 9.0 adicionada para Ana.

Aluno: Ana
Notas: [8.0, 7.5, 9.0]
Media: 8.2
```

### O Que Este Exemplo Ensina

1. Um atributo pode ser uma **lista** (como `self.grades = []`)
2. Métodos podem **modificar** os atributos do objeto (como `add_grade` que adiciona a lista)
3. Métodos podem **chamar outros métodos** da mesma classe (como `show_report` que chama `calculate_average`)
4. Cada objeto tem sua **propria lista** de notas — se criarmos outro estudante, ele tera notas diferentes

---

## Exemplo Prático Completo: Classe Produto para o CRUD

Este exemplo e especialmente importante porque a classe `Product` sera a base do projeto CRUD que você vai construir nos proximos módulos. Aqui, criamos uma classe completa para representar um produto de uma loja.

```python
# Classe Product (produto)
# "Product" = produto
# Esta classe sera a base do projeto CRUD
class Product:
    # Construtor: define os dados do produto
    # "self" = este produto
    # "product_id" = identificador unico do produto
    # "name" = nome do produto
    # "price" = preco do produto
    # "quantity" = quantidade em estoque
    # "category" = categoria do produto
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    # Metodo: exibir informacoes completas do produto
    # "display_info" = exibir informacoes
    def display_info(self):
        print(f"ID: {self.product_id}")
        print(f"Nome: {self.name}")
        print(f"Preco: R$ {self.price:.2f}")
        print(f"Quantidade: {self.quantity}")
        print(f"Categoria: {self.category}")

    # Metodo: calcular o valor total em estoque
    # "calculate_stock_value" = calcular valor do estoque
    # Valor total = preco multiplicado pela quantidade
    def calculate_stock_value(self):
        return self.price * self.quantity

    # Metodo: atualizar o preco do produto
    # "update_price" = atualizar preco
    # "new_price" = novo preco
    def update_price(self, new_price):
        # Verificamos se o novo preco e valido (maior que zero)
        if new_price > 0:
            # Guardamos o preco antigo para exibir a mudanca
            # "old_price" = preco antigo
            old_price = self.price
            # Atualizamos o preco
            self.price = new_price
            print(f"Preco de {self.name} atualizado: R$ {old_price:.2f} -> R$ {new_price:.2f}")
        else:
            print("Erro: o preco deve ser maior que zero.")

    # Metodo: adicionar unidades ao estoque
    # "add_stock" = adicionar estoque
    # "amount" = quantidade a adicionar
    def add_stock(self, amount):
        # Verificamos se a quantidade e valida
        if amount > 0:
            self.quantity = self.quantity + amount
            print(f"{amount} unidades de {self.name} adicionadas. Estoque: {self.quantity}")
        else:
            print("Erro: a quantidade deve ser maior que zero.")

# Criamos um produto
# "product" = produto
product = Product(1, "Arroz Integral", 8.99, 50, "Alimentos")

# Exibimos as informacoes
product.display_info()

# Calculamos o valor total em estoque
# "stock_value" = valor do estoque
stock_value = product.calculate_stock_value()
print(f"Valor total em estoque: R$ {stock_value:.2f}")

# Atualizamos o preco
print()
product.update_price(9.49)

# Adicionamos estoque
product.add_stock(30)

# Exibimos as informacoes atualizadas
print()
product.display_info()
```

Saida esperada:
```
ID: 1
Nome: Arroz Integral
Preco: R$ 8.99
Quantidade: 50
Categoria: Alimentos
Valor total em estoque: R$ 449.50

Preco de Arroz Integral atualizado: R$ 8.99 -> R$ 9.49
30 unidades de Arroz Integral adicionadas. Estoque: 80

ID: 1
Nome: Arroz Integral
Preco: R$ 9.49
Quantidade: 80
Categoria: Alimentos
```

---

## O Que Existe Além — Conceitos Avancados (Fora do Escopo)

Orientacao a Objetos e um tema muito amplo. Neste módulo, você aprendeu o essencial: classes, objetos, atributos, métodos, `__init__` e `self`. Esses conceitos sao suficientes para o que você precisa neste curso.

Porém, e importante que você saiba que existem conceitos mais avancados que você pode estudar no futuro, quando se sentir confortavel com o básico:

- **Herança:** Criar uma classe nova baseada em outra classe existente (como criar uma receita de "bolo de chocolate" baseada na receita de "bolo simples")
- **Polimorfismo:** Objetos de classes diferentes responderem ao mesmo método de formas diferentes
- **Classes abstratas:** Classes que servem apenas como modelo e não podem ser usadas diretamente
- **Métodos estaticos:** Métodos que pertencem a classe, não a um objeto específico
- **Propriedades (properties):** Formas especiais de acessar e modificar atributos
- **Decoradores:** Funções que modificam o comportamento de outras funções ou métodos

Não se preocupe com esses conceitos agora. O importante e dominar o básico antes de avancar. Quando você se sentir seguro criando classes simples com atributos e métodos, estara pronto para explorar esses tópicos por conta propria.

---

## Resumo

Neste módulo, você aprendeu os conceitos fundamentais de Orientacao a Objetos em Python:

| Conceito | O Que E | Analogia |
|----------|---------|----------|
| Classe | Um molde/modelo para criar objetos | Receita de bolo |
| Objeto | Uma instância criada a partir de uma classe | O bolo pronto |
| Atributo | Um dado que o objeto carrega | Ingredientes da receita |
| Método | Uma ação que o objeto pode realizar | Modo de preparo |
| `__init__` | O construtor — inicializa os dados do objeto | Preencher a ficha de cadastro |
| `self` | Referência ao proprio objeto | Crachá de identificacao |

Pontos importantes para lembrar:

- Classes usam **CamelCase** no nome: `Product`, `Student`, `BankAccount`
- Métodos sempre recebem `self` como primeiro parametro
- Você **não** passa o `self` ao chamar um método — o Python faz isso automaticamente
- Atributos sao acessados com **ponto**: `objeto.atributo`
- Métodos sao chamados com **ponto e parenteses**: `objeto.metodo()`
- Cada objeto e **independente** — alterar um não afeta os outros

---

## Para Saber Mais

- [W3Schools — Classes e Objetos em Python](https://www.w3schools.com/python/python_classes.asp)
  _Aqui você encontra mais exemplos de como criar classes e objetos em Python, com explicacoes em ingles simples_
- [W3Schools — O Método __init__](https://www.w3schools.com/python/gloss_python_class_init.asp)
  _Explicacao detalhada do construtor __init__ com exemplos praticos_
- [W3Schools — O Parametro self](https://www.w3schools.com/python/gloss_python_self.asp)
  _Entenda melhor o papel do self nos métodos de uma classe_
- [Documentação Oficial Python — Classes](https://docs.python.org/pt-br/3/tutorial/classes.html)
  _Referencia completa sobre classes em Python, em portugues_

---

## Perguntas Frequentes (FAQ)

**P: O que e uma classe em Python?**
R: Uma classe e um molde ou modelo que define quais dados (atributos) e quais ações (métodos) um objeto vai ter. Pense em uma receita de bolo: a receita descreve os ingredientes e o modo de preparo, mas não e o bolo em si. A classe descreve a estrutura, e a partir dela você cria objetos concretos.

**P: O que e um objeto?**
R: Um objeto e uma instância criada a partir de uma classe. Se a classe e a receita, o objeto e o bolo pronto. Você pode criar quantos objetos quiser a partir da mesma classe, e cada um tera seus proprios dados independentes.

**P: O que significa "instância"?**
R: "Instância" e apenas uma palavra técnica que significa "um exemplar criado a partir de um molde". Quando dizemos "o objeto `rice` e uma instância da classe `Product`", estamos dizendo que `rice` foi criado usando o molde `Product`. Os termos "objeto" e "instância" significam a mesma coisa na prática.

**P: O que e o __init__ e por que ele tem underscores?**
R: O `__init__` e o construtor da classe — um método especial que o Python chama automaticamente quando você cria um novo objeto. Os dois underscores de cada lado indicam que e um método especial do Python (chamado de "dunder method" ou "magic method"). Você não precisa chamar o `__init__` diretamente — o Python faz isso por você.

**P: O que e o self e por que preciso dele?**
R: O `self` e uma referência ao proprio objeto. Ele permite que o método saiba de qual objeto estamos falando. Quando você tem vários objetos da mesma classe, o `self` garante que cada método acesse os dados do objeto correto. Pense no `self` como um crachá de identificacao que cada objeto carrega.

**P: Preciso sempre escrever self como primeiro parametro?**
R: Sim, todo método dentro de uma classe deve ter `self` como primeiro parametro. Essa e uma regra do Python. Porém, quando você chama o método, não precisa passar o `self` — o Python faz isso automaticamente. Você so declara, não passa.

**P: Posso usar outro nome em vez de self?**
R: Tecnicamente sim, o Python aceita qualquer nome. Porém, usar `self` e uma convencao fortissima na comunidade Python. Todos os programadores Python usam `self`, e usar outro nome vai confundir quem ler seu código. Sempre use `self`.

**P: Qual a diferença entre uma função e um método?**
R: A diferença principal e onde eles vivem. Uma função e definida fora de qualquer classe, de forma independente. Um método e uma função que pertence a uma classe e sempre recebe `self` como primeiro parametro. Na prática, métodos sao funções que "moram dentro" de uma classe e podem acessar os dados do objeto.

**P: O que e um atributo?**
R: Um atributo e um dado que pertence a um objeto. E como um campo em uma ficha cadastral. Por exemplo, um objeto `Product` pode ter os atributos `name` (nome), `price` (preco) e `quantity` (quantidade). Cada objeto tem seus proprios valores para esses atributos.

**P: Posso criar atributos fora do __init__?**
R: Tecnicamente sim, você pode adicionar atributos a um objeto a qualquer momento. Porém, a boa prática e definir todos os atributos dentro do `__init__`. Isso torna o código mais claro e previsivel, porque qualquer pessoa que ler a classe sabe exatamente quais dados um objeto vai ter.

**P: Por que usar classes se eu posso usar dicionários?**
R: Dicionários funcionam bem para dados simples, mas classes oferecem vantagens: (1) você pode definir métodos que operam sobre os dados, mantendo tudo organizado em um único lugar; (2) o código fica mais legivel e fácil de manter; (3) você pode criar multiplos objetos com a mesma estrutura de forma consistente. Para projetos pequenos, dicionários sao suficientes. Para projetos maiores, classes ajudam muito na organização.

**P: E normal achar Orientacao a Objetos difícil no inicio?**
R: Sim, completamente normal! Orientacao a Objetos e um dos conceitos que mais confunde iniciantes. A ideia de "moldes que criam coisas" e o `self` podem parecer estranhos no comeco. Não desanime — com prática, esses conceitos vao se tornando naturais. Muitos programadores experientes também acharam difícil quando estavam aprendendo.

**P: Preciso usar Orientacao a Objetos em todos os meus programas?**
R: Não! Orientacao a Objetos e uma ferramenta, não uma obrigacao. Para programas simples, funções e variáveis sao suficientes. Classes sao mais úteis quando você tem dados e ações que fazem sentido juntos, ou quando precisa criar vários objetos com a mesma estrutura. Use quando fizer sentido, não por obrigacao.

**P: O que significa CamelCase?**
R: CamelCase e uma convencao de nomenclatura onde cada palavra comeca com letra maiuscula, sem espacos ou underscores. Exemplos: `Product`, `BankAccount`, `StudentRecord`. O nome vem das "corcovas" formadas pelas letras maiusculas, que lembram um camelo. Em Python, usamos CamelCase para nomes de classes e snake_case para variáveis e funções.

**P: Posso ter uma classe dentro de outra classe?**
R: Sim, e possível, mas e um conceito avancado que esta fora do escopo deste curso. Para o que você precisa agora, classes simples e independentes sao suficientes. Quando você tiver mais experiência, pode explorar esse conceito.

**P: O que acontece se eu esquecer o self nos parametros de um método?**
R: O Python vai gerar um erro. Se você definir um método sem `self` e tentar chama-lo a partir de um objeto, vai receber um `TypeError` dizendo que o método recebeu mais argumentos do que esperava. Isso acontece porque o Python tenta passar o objeto como primeiro argumento, mas o método não tem parametro para recebe-lo.

**P: Posso criar um objeto sem o __init__?**
R: Sim, você pode criar uma classe sem `__init__` e criar objetos a partir dela. Porém, o objeto não tera atributos iniciais. Você pode adicionar atributos depois, mas isso não e recomendado. O `__init__` e a forma padrão e organizada de definir os dados iniciais de um objeto.

**P: O que e "orientacao a objetos"? Por que esse nome?**
R: "Orientacao a Objetos" (ou OOP, de Object-Oriented Programming) e uma forma de organizar o código onde tudo gira em torno de **objetos**. Em vez de ter dados soltos e funções separadas, você agrupa dados e ações em objetos. O nome vem da ideia de que o programa e "orientado" (organizado, direcionado) por objetos.

**P: Posso usar print() dentro de um método?**
R: Sim! Métodos sao funções, e você pode usar qualquer comando Python dentro deles, incluindo `print()`, `input()`, condicionais, loops e tudo mais que você ja aprendeu. A única diferença e que métodos tem acesso ao `self`, que permite acessar os dados do objeto.

**P: Como sei quando devo criar uma classe?**
R: Uma boa regra e: se você tem um conjunto de dados que sempre andam juntos e ações que operam sobre esses dados, uma classe pode ser útil. Por exemplo, se você sempre trabalha com nome, preco e quantidade de um produto, e tem funções para calcular total e atualizar preco, faz sentido juntar tudo em uma classe `Product`.

**P: O que e a diferença entre self.name e name dentro do __init__?**
R: Dentro do `__init__`, `name` (sem self) e o **parametro** que você recebe — e um valor temporário que existe so durante a execução do `__init__`. Ja `self.name` (com self) e o **atributo** do objeto — e um valor que fica guardado no objeto e pode ser acessado depois, de qualquer método. A linha `self.name = name` copia o valor do parametro para o atributo do objeto.

**P: Posso ter vários métodos em uma classe?**
R: Sim, você pode ter quantos métodos quiser! Uma classe pode ter 1, 5, 10 ou mais métodos. Cada método representa uma ação diferente que o objeto pode realizar. Não ha limite para a quantidade de métodos.

**P: Classes em Python sao parecidas com classes em outras linguagens?**
R: Sim, o conceito de classes existe em muitas linguagens como Java, C#, JavaScript e outras. Os principios básicos (classe como molde, objeto como instância, atributos e métodos) sao os mesmos. A sintaxe muda de linguagem para linguagem, mas a ideia central e universal. Aprender classes em Python vai facilitar muito se você precisar aprender outra linguagem no futuro.

---

## Exercícios de Fixacao

Pratique o que aprendeu com os exercícios do módulo:

[Exercícios do Módulo 22 — Classes e Objetos](22-classes-objetos-exercicios.md)

---

[<- Anterior: Manipulação JSON](21-manipulacao-json.md) | [Glossário](00-glossario.md) | [Próximo: Exercícios Integradores ->](23-exercicios-integradores.md)
