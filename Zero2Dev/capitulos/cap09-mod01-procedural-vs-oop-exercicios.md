# 9.1 — Exercícios: Procedural vs OOP

[← Voltar ao conteúdo: Procedural vs OOP](cap09-mod01-procedural-vs-oop-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem os conceitos do módulo 9.1: programação procedural, seus limites, e a introdução à Programação Orientada a Objetos. A maioria é conceitual e de reflexão — o código em C# começa no módulo 9.3. Use Python para os exercícios que pedem código.

---

## Exercício 1 — Identificando o Estilo Procedural

Olhe para o código abaixo e identifique as 5 características da programação procedural que estudamos:

```python
# "students" = alunos
students = []

# "add_student" = adicionar aluno
def add_student(students, name, age, grade):
    student = {"name": name, "age": age, "grade": grade}
    students.append(student)

# "calculate_average" = calcular media
def calculate_average(students):
    if not students:
        return 0
    total = sum(s["grade"] for s in students)
    return total / len(students)

# "find_best_student" = encontrar melhor aluno
def find_best_student(students):
    if not students:
        return None
    best = students[0]
    for s in students[1:]:
        if s["grade"] > best["grade"]:
            best = s
    return best

add_student(students, "Ana", 20, 8.5)
add_student(students, "Bruno", 22, 9.0)
add_student(students, "Carla", 21, 7.5)
print(f"Média: {calculate_average(students):.1f}")
best = find_best_student(students)
print(f"Melhor aluno: {best['name']} ({best['grade']})")
```

Saída esperada:
```
Média: 8.3
Melhor aluno: Bruno (9.0)
```

Para cada característica, aponte onde ela aparece no código:
1. Dados e funções separados
2. Execução sequencial
3. Funções como unidade de organização
4. Estado passado por parâmetro
5. Sem agrupamento formal entre dados e funções

---

## Exercício 2 — Contando os Problemas

Análise o código procedural abaixo de um sistema de biblioteca simplificado:

```python
# "books" = livros, "members" = membros, "loans" = emprestimos
books = []
members = []
loans = []

# "add_book" = adicionar livro
def add_book(books, title, author, isbn):
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "isbn": isbn,
        "available": True
    }
    books.append(book)
    return book

# "add_member" = adicionar membro
def add_member(members, name, email, phone):
    member = {
        "id": len(members) + 1,
        "name": name,
        "email": email,
        "phone": phone
    }
    members.append(member)
    return member

# "borrow_book" = emprestar livro
def borrow_book(books, members, loans, member_id, book_id):
    book = None
    for b in books:
        if b["id"] == book_id:
            book = b
            break

    member = None
    for m in members:
        if m["id"] == member_id:
            member = m
            break

    if not book:
        print("Livro não encontrado!")
        return None
    if not member:
        print("Membro não encontrado!")
        return None
    if not book["available"]:
        print("Livro não disponível!")
        return None

    # Verifica limite de empréstimos
    member_loans = [l for l in loans if l["member_id"] == member_id and not l["returned"]]
    if len(member_loans) >= 3:
        print("Limite de empréstimos atingido!")
        return None

    book["available"] = False
    loan = {
        "id": len(loans) + 1,
        "member_id": member_id,
        "book_id": book_id,
        "returned": False
    }
    loans.append(loan)
    return loan

# "return_book" = devolver livro
def return_book(books, loans, loan_id):
    loan = None
    for l in loans:
        if l["id"] == loan_id:
            loan = l
            break

    if not loan:
        print("Empréstimo não encontrado!")
        return False

    loan["returned"] = True
    for b in books:
        if b["id"] == loan["book_id"]:
            b["available"] = True
            break
    return True
```

Responda:
1. Quantos parâmetros a função `borrow_book` recebe? Isso é um problema?
2. Se você mudar o nome do campo `"available"` para `"is_available"`, quantas funções precisam ser alteradas?
3. Se você quiser adicionar a entidade "Funcionário" com operações similares, quanto código novo precisa escrever?
4. A função `borrow_book` faz quantas coisas diferentes? Liste cada responsabilidade.
5. Se você quiser testar apenas a lógica de "verificar limite de empréstimos", consegue fazer isso isoladamente?

---

## Exercício 3 — Pensando em Objetos

Para cada entidade abaixo, liste pelo menos 3 atributos e 3 métodos que fariam sentido se ela fosse um objeto:

1. **Conta Bancária**
   - Atributos: ...
   - Métodos: ...

2. **Carro em uma locadora**
   - Atributos: ...
   - Métodos: ...

3. **Filme em um serviço de streaming**
   - Atributos: ...
   - Métodos: ...

4. **Pedido em um restaurante**
   - Atributos: ...
   - Métodos: ...

5. **Aluno em uma escola**
   - Atributos: ...
   - Métodos: ...

Dica: atributos descrevem O QUE o objeto É (características). Métodos descrevem O QUE o objeto FAZ (comportamentos). Pense: "o que esse objeto precisa saber sobre si mesmo?" e "o que esse objeto precisa saber fazer?"

---

## Exercício 4 — Refatoração Mental

Olhe para o Exercício 2 (sistema de biblioteca procedural) e responda:

1. Se `borrow_book` fosse um método do objeto `Library`, quantos parâmetros ele precisaria receber? (Dica: a biblioteca já "conhece" seus livros, membros e empréstimos)
2. Se `Book` fosse uma classe, qual método faria mais sentido: uma função externa `check_availability(book)` ou um método `book.is_available()`? Por quê?
3. Se `Member` fosse uma classe com um método `can_borrow()`, como isso simplificaria a função `borrow_book`?
4. Desenhe (em papel ou texto) como você organizaria as classes: quais classes existiriam, quais atributos e métodos cada uma teria, e como elas se relacionariam.

---

## Exercício 5 — Procedural na Prática

Escreva em Python um sistema procedural de gerenciamento de tarefas (to-do list) com as seguintes funcionalidades:

- Adicionar tarefa (com título, descrição e prioridade: alta, média, baixa)
- Listar todas as tarefas
- Marcar tarefa como concluída
- Listar apenas tarefas pendentes
- Listar tarefas por prioridade

Depois de implementar, responda:
1. Quantas funções você criou?
2. Todas recebem a lista de tarefas como parâmetro?
3. Se você quisesse adicionar "categorias" às tarefas, quantos lugares do código precisaria alterar?
4. Se você quisesse adicionar "projetos" (cada projeto tem várias tarefas), como ficaria a complexidade?

---

## Exercício 6 — Comparação de Paradigmas

Complete a tabela comparando como cada conceito funciona em programação procedural vs OOP:

| Conceito | Procedural | OOP |
|----------|-----------|-----|
| Onde ficam os dados? | Em variáveis e estruturas separadas | ... |
| Onde ficam os comportamentos? | ... | Em métodos dentro das classes |
| Como dados e comportamentos se conectam? | ... | ... |
| Como se adiciona uma entidade nova? | ... | ... |
| Como se muda a estrutura de um dado? | ... | ... |
| Como se testa uma parte isolada? | ... | ... |

---

## Exercício 7 — Análise do Seu CRUD

Volte ao projeto CRUD do capítulo 8 (produtos com SQLite) e faça uma análise crítica:

1. Liste todas as funções do seu CRUD
2. Para cada função, identifique: quais dados ela acessa? Quais outras funções ela chama?
3. Desenhe um diagrama (pode ser em texto) mostrando as dependências entre funções
4. Identifique: se você quisesse trocar SQLite por PostgreSQL, quais funções precisariam mudar?
5. Identifique: se você quisesse adicionar "categorias de produtos", quais funções precisariam mudar?

Este exercício prepara o terreno para o módulo 9.9 (Repository Pattern), onde vamos ver como OOP resolve exatamente esses problemas.

---

## Exercício 8 — Reflexão: Quando Procedural é Melhor

Nem tudo precisa ser OOP. Para cada cenário abaixo, diga se você usaria procedural ou OOP, e justifique:

1. Um script que renomeia 500 arquivos em uma pasta
2. Um sistema de e-commerce com produtos, clientes, pedidos e pagamentos
3. Um programa que converte temperaturas de Celsius para Fahrenheit
4. Um jogo com personagens, inimigos, itens e cenários
5. Um script que faz backup de um banco de dados
6. Um sistema de gestão hospitalar com pacientes, médicos, consultas e prontuários
7. Uma calculadora de linha de comando
8. Um aplicativo de banco com contas, transferências e investimentos

---

## Exercício 9 — Linha do Tempo

Sem consultar o módulo, tente preencher a linha do tempo da evolução da OOP:

1. 1967 — Qual linguagem introduziu os primeiros conceitos de OOP? Quem criou?
2. 1972 — Qual linguagem cunhou o termo "Programação Orientada a Objetos"? Quem criou?
3. 1983 — Qual linguagem adicionou OOP à linguagem C? Quem criou?
4. 1995 — Qual linguagem trouxe OOP para o mainstream com "Write Once, Run Anywhere"?
5. 2000 — Qual linguagem a Microsoft criou para competir com Java?

---

## Exercício 10 — Os Quatro Pilares

Para cada pilar da OOP, escreva com suas palavras:
1. O que é
2. Uma analogia do dia a dia
3. Qual problema do código procedural ele resolve

Pilares:
- Encapsulamento
- Herança
- Polimorfismo
- Abstração

---

[← Voltar ao conteúdo: Procedural vs OOP](cap09-mod01-procedural-vs-oop-conteudo.md)
