# 8.4 — Exercícios: SQLite e Ambiente

[← Voltar ao conteúdo: SQLite e Ambiente](cap08-mod04-sqlite-ambiente-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem a instalação e uso do SQLite, tanto pelo shell de linha de comando quanto pela biblioteca `sqlite3` do Python. A partir daqui, todos os exercícios envolvem código — execute cada um no seu computador.

---

## Como Executar

```bash
# Criar pasta para os exercicios
mkdir -p ~/meus-projetos/curso/cap08/exercicios

# Navegar ate a pasta
cd ~/meus-projetos/curso/cap08/exercicios

# Executar scripts Python
python3 nome_exercicio.py

# Abrir shell SQLite
sqlite3 nome_banco.db
```

---

## Exercício 1: Primeiros Passos no Shell SQLite

Abra o terminal e execute os comandos abaixo. Anote o resultado de cada um.

```bash
# Criar um banco de dados chamado escola.db
sqlite3 escola.db
```

Dentro do shell SQLite, execute:

```sql
-- Criar tabela de alunos
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE,
    idade INTEGER CHECK(idade > 0 AND idade < 150)
);

-- Inserir 5 alunos
INSERT INTO alunos (nome, email, idade) VALUES ('Ana Silva', 'ana@email.com', 20);
INSERT INTO alunos (nome, email, idade) VALUES ('Bruno Costa', 'bruno@email.com', 22);
INSERT INTO alunos (nome, email, idade) VALUES ('Carla Santos', 'carla@email.com', 19);
INSERT INTO alunos (nome, email, idade) VALUES ('Diego Lima', 'diego@email.com', 25);
INSERT INTO alunos (nome, email, idade) VALUES ('Eva Oliveira', 'eva@email.com', 21);

-- Listar todos os alunos
SELECT * FROM alunos;
```

Agora responda:

a) Execute `.tables` — o que aparece?
b) Execute `.schema alunos` — o que aparece?
c) Execute `SELECT COUNT(*) FROM alunos;` — qual o resultado?
d) Execute `SELECT * FROM alunos WHERE idade > 20;` — quais alunos aparecem?
e) Tente inserir um aluno com email repetido: `INSERT INTO alunos (nome, email, idade) VALUES ('Teste', 'ana@email.com', 18);` — o que acontece?
f) Tente inserir um aluno com idade negativa: `INSERT INTO alunos (nome, email, idade) VALUES ('Teste', 'teste@email.com', -5);` — o que acontece?
g) Execute `.headers on` e depois `.mode table` e repita o `SELECT * FROM alunos;` — qual a diferença na saída?

---

## Exercício 2: Python e SQLite — Criando e Populando

Crie o arquivo `ex02_escola.py` com o seguinte programa:

```python
# ex02_escola.py
# Programa que cria um banco de escola e insere alunos
# "school" = escola, "student" = aluno
import sqlite3

def create_database():
    """Cria o banco e a tabela de alunos"""
    # "connection" = conexao
    connection = sqlite3.connect("escola_python.db")
    cursor = connection.cursor()

    # Criar tabela (IF NOT EXISTS evita erro se ja existir)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            idade INTEGER,
            curso TEXT DEFAULT 'Indefinido'
        )
    """)

    connection.commit()
    print("Banco e tabela criados com sucesso!")
    return connection

def insert_students(connection):
    """Insere alunos usando executemany"""
    cursor = connection.cursor()

    # "students" = alunos
    students = [
        ("Ana Silva", "ana@escola.com", 20, "Engenharia"),
        ("Bruno Costa", "bruno@escola.com", 22, "Medicina"),
        ("Carla Santos", "carla@escola.com", 19, "Direito"),
        ("Diego Lima", "diego@escola.com", 25, "Computacao"),
        ("Eva Oliveira", "eva@escola.com", 21, "Arquitetura"),
    ]

    cursor.executemany(
        "INSERT OR IGNORE INTO alunos (nome, email, idade, curso) VALUES (?, ?, ?, ?)",
        students
    )

    connection.commit()
    print(f"{cursor.rowcount} alunos inseridos.")

def list_students(connection):
    """Lista todos os alunos"""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM alunos")
    rows = cursor.fetchall()

    print(f"\nTotal de alunos: {len(rows)}")
    print("-" * 60)
    for row in rows:
        # row = (id, nome, email, idade, curso)
        print(f"  {row[0]}. {row[1]} ({row[3]} anos) - {row[4]} - {row[2]}")

def search_by_age(connection, min_age):
    """Busca alunos com idade maior que min_age"""
    # "min_age" = idade minima
    cursor = connection.cursor()
    cursor.execute("SELECT nome, idade FROM alunos WHERE idade > ?", (min_age,))
    rows = cursor.fetchall()

    print(f"\nAlunos com mais de {min_age} anos: {len(rows)}")
    for row in rows:
        print(f"  {row[0]} - {row[1]} anos")

# Programa principal
connection = create_database()
insert_students(connection)
list_students(connection)
search_by_age(connection, 20)
connection.close()
```

Saída esperada:

```
Banco e tabela criados com sucesso!
5 alunos inseridos.

Total de alunos: 5
------------------------------------------------------------
  1. Ana Silva (20 anos) - Engenharia - ana@escola.com
  2. Bruno Costa (22 anos) - Medicina - bruno@escola.com
  3. Carla Santos (19 anos) - Direito - carla@escola.com
  4. Diego Lima (25 anos) - Computacao - diego@escola.com
  5. Eva Oliveira (21 anos) - Arquitetura - eva@escola.com

Alunos com mais de 20 anos: 3
  Bruno Costa - 22 anos
  Diego Lima - 25 anos
  Eva Oliveira - 21 anos
```

Agora modifique o programa para:

a) Adicionar uma função `search_by_course(connection, course)` que busca alunos por curso.
b) Adicionar uma função `count_by_course(connection)` que mostra quantos alunos tem em cada curso.
c) Executar o programa duas vezes seguidas. O que acontece com os dados? Por que o `INSERT OR IGNORE` é importante aqui?

---

## Exercício 3: Explorando Comandos do Shell

Usando o banco `escola_python.db` criado no exercício anterior, abra o shell SQLite e execute cada comando abaixo. Anote o que cada um faz:

```bash
sqlite3 escola_python.db
```

```sql
-- Comandos de informacao
.tables
.schema alunos
.headers on
.mode column

-- Consultas
SELECT * FROM alunos;
SELECT nome, curso FROM alunos ORDER BY nome;
SELECT curso, COUNT(*) FROM alunos GROUP BY curso;
SELECT AVG(idade) FROM alunos;
SELECT MIN(idade), MAX(idade) FROM alunos;

-- Exportar dados
.mode csv
SELECT * FROM alunos;
.mode table
```

Responda:
a) Qual a diferença entre `.mode column`, `.mode table` e `.mode csv`?
b) O que o comando `.schema` mostra que `.tables` não mostra?
c) Como você exportaria os dados para um arquivo CSV usando o shell?

---

## Exercício 4: Tratamento de Erros

Crie o arquivo `ex04_erros.py` que testa diferentes tipos de erro:

```python
# ex04_erros.py
# Programa que testa tratamento de erros com SQLite
# "error" = erro, "handle" = tratar
import sqlite3

def test_errors():
    """Testa diferentes tipos de erro"""
    connection = sqlite3.connect("teste_erros.db")
    cursor = connection.cursor()

    # Criar tabela de teste
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL CHECK(preco > 0),
            codigo TEXT UNIQUE
        )
    """)
    # Ativar verificacao de chaves estrangeiras
    cursor.execute("PRAGMA foreign_keys = ON")
    connection.commit()

    # Inserir um produto valido primeiro
    try:
        cursor.execute(
            "INSERT INTO produtos (nome, preco, codigo) VALUES (?, ?, ?)",
            ("Arroz", 22.90, "ARR001")
        )
        connection.commit()
        print("1. Produto inserido com sucesso")
    except sqlite3.Error as e:
        print(f"1. Erro: {e}")

    # TODO: Complete os testes abaixo

    # Teste 2: Inserir produto com nome NULL (viola NOT NULL)
    # Seu codigo aqui...

    # Teste 3: Inserir produto com preco negativo (viola CHECK)
    # Seu codigo aqui...

    # Teste 4: Inserir produto com codigo duplicado (viola UNIQUE)
    # Seu codigo aqui...

    # Teste 5: Inserir produto sem preco (campo opcional? ou obrigatorio?)
    # Seu codigo aqui...

    connection.close()

test_errors()
```

Complete os testes 2 a 5. Para cada teste:
a) Escreva o código que tenta a operação inválida
b) Capture o erro com `try/except sqlite3.Error`
c) Imprima uma mensagem descritiva do erro
d) Verifique se o banco continua funcionando após o erro

---

## Exercício 5: Context Manager e Boas Práticas

Reescreva o exercício 2 usando context manager (`with`) em vez de `connection.close()` manual:

```python
# ex05_context_manager.py
# Programa que usa context manager para gerenciar conexao
# "context" = contexto, "manager" = gerenciador
import sqlite3

DATABASE = "escola_context.db"

def setup_database():
    """Cria o banco e a tabela"""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE,
                idade INTEGER
            )
        """)
        # commit automatico ao sair do with (se nao houver erro)
    print("Banco configurado!")

# TODO: Implemente as funcoes abaixo usando context manager

def add_student(name, email, age):
    """Adiciona um aluno usando context manager"""
    # Seu codigo aqui...
    pass

def list_all_students():
    """Lista todos os alunos usando context manager"""
    # Seu codigo aqui...
    pass

def find_student(name):
    """Busca aluno por nome (busca parcial com LIKE)"""
    # Seu codigo aqui...
    pass

# Programa principal
setup_database()
add_student("Ana Silva", "ana@escola.com", 20)
add_student("Bruno Costa", "bruno@escola.com", 22)
add_student("Carla Santos", "carla@escola.com", 19)
list_all_students()
find_student("Ana")
```

Implemente as três funções usando `with sqlite3.connect(DATABASE) as conn:` e responda:

a) Qual a vantagem de usar `with` em vez de `connection.close()`?
b) O que acontece se ocorrer um erro dentro do bloco `with`? O commit é feito ou não?
c) Quando você precisa chamar `conn.commit()` explicitamente dentro do `with`?

---

## Exercício 6: Row Factory — Resultados como Dicionários

Por padrão, o `sqlite3` retorna resultados como tuplas: `(1, 'Ana', 'ana@email.com', 20)`. Isso é difícil de ler — você precisa lembrar que o índice 0 é id, 1 é nome, etc.

Crie o arquivo `ex06_row_factory.py` que usa `row_factory` para retornar dicionários:

```python
# ex06_row_factory.py
# Programa que usa row_factory para resultados mais legíveis
# "row" = linha, "factory" = fabrica
import sqlite3

DATABASE = "escola_factory.db"

def setup():
    """Cria banco e insere dados"""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE,
                idade INTEGER,
                curso TEXT
            )
        """)
        conn.executemany(
            "INSERT OR IGNORE INTO alunos (nome, email, idade, curso) VALUES (?, ?, ?, ?)",
            [
                ("Ana Silva", "ana@escola.com", 20, "Engenharia"),
                ("Bruno Costa", "bruno@escola.com", 22, "Medicina"),
                ("Carla Santos", "carla@escola.com", 19, "Direito"),
            ]
        )

def list_as_tuples():
    """Lista alunos como tuplas (padrao)"""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute("SELECT * FROM alunos")
        rows = cursor.fetchall()
        print("Como tuplas:")
        for row in rows:
            # Precisa lembrar os indices: 0=id, 1=nome, 2=email...
            print(f"  {row[0]}. {row[1]} - {row[2]}")

def list_as_dicts():
    """Lista alunos como dicionarios"""
    with sqlite3.connect(DATABASE) as conn:
        # row_factory transforma cada linha em um objeto Row
        conn.row_factory = sqlite3.Row
        cursor = conn.execute("SELECT * FROM alunos")
        rows = cursor.fetchall()
        print("\nComo dicionarios (sqlite3.Row):")
        for row in rows:
            # Agora pode acessar por nome da coluna!
            print(f"  {row['id']}. {row['nome']} - {row['email']}")

setup()
list_as_tuples()
list_as_dicts()
```

Saída esperada:

```
Como tuplas:
  1. Ana Silva - ana@escola.com
  2. Bruno Costa - bruno@escola.com
  3. Carla Santos - carla@escola.com

Como dicionarios (sqlite3.Row):
  1. Ana Silva - ana@escola.com
  2. Bruno Costa - bruno@escola.com
  3. Carla Santos - carla@escola.com
```

Agora adicione:

a) Uma função `student_to_dict(row)` que converte um `sqlite3.Row` em um dicionário Python puro (`dict`). Use `dict(row)`.

b) Uma função `list_as_json()` que lista os alunos em formato JSON usando `json.dumps()`.

c) Explique: por que acessar `row['nome']` é melhor que `row[1]` em código de produção?

---

## Exercício 7: Múltiplas Tabelas

Crie o arquivo `ex07_multiplas_tabelas.py` que cria um banco com duas tabelas relacionadas:

```python
# ex07_multiplas_tabelas.py
# Programa que cria tabelas com relacionamento
# "department" = departamento, "employee" = funcionario
import sqlite3

DATABASE = "empresa.db"

def setup():
    """Cria banco com departamentos e funcionarios"""
    with sqlite3.connect(DATABASE) as conn:
        # Ativar chaves estrangeiras
        conn.execute("PRAGMA foreign_keys = ON")

        conn.execute("""
            CREATE TABLE IF NOT EXISTS departamentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                andar INTEGER
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE,
                salario REAL CHECK(salario > 0),
                departamento_id INTEGER,
                FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
            )
        """)

        # Inserir departamentos
        conn.executemany(
            "INSERT OR IGNORE INTO departamentos (nome, andar) VALUES (?, ?)",
            [("Vendas", 3), ("TI", 5), ("RH", 2), ("Financeiro", 4)]
        )

        # TODO: Inserir 8 funcionarios distribuidos entre os departamentos
        # Seu codigo aqui...

setup()

# TODO: Implemente as funcoes abaixo

def list_employees_by_department():
    """Lista funcionarios agrupados por departamento"""
    # Use JOIN para mostrar o nome do departamento
    pass

def department_stats():
    """Mostra estatisticas por departamento"""
    # Quantidade de funcionarios, salario medio, maior e menor salario
    pass

def add_employee(name, email, salary, department_name):
    """Adiciona funcionario buscando o departamento pelo nome"""
    # Primeiro busca o id do departamento, depois insere o funcionario
    pass

def transfer_employee(employee_id, new_department_name):
    """Transfere funcionario para outro departamento"""
    # Atualiza o departamento_id do funcionario
    pass
```

Implemente todas as funções marcadas com TODO e teste cada uma.

---

## Exercício 8: Desafio — Agenda de Contatos

Crie um programa completo `ex08_agenda.py` que funciona como uma agenda de contatos com menu interativo:

```
=== AGENDA DE CONTATOS ===
[1] Listar contatos
[2] Buscar contato
[3] Adicionar contato
[4] Editar contato
[5] Remover contato
[0] Sair
```

Requisitos:
- Tabela `contatos` com: id, nome (NOT NULL), telefone, email (UNIQUE), categoria (amigo, familia, trabalho, outro)
- Busca por nome deve ser parcial (LIKE) e case-insensitive
- Ao remover, pedir confirmação mostrando os dados do contato
- Ao editar, mostrar os dados atuais e perguntar qual campo alterar
- Usar parâmetros seguros (?) em todas as queries
- Usar context manager (`with`) para todas as conexões
- Tratar erros (email duplicado, contato não encontrado, etc.)

Este exercício é uma preparação para o projeto CRUD do módulo 8.9.

---

## Gabarito Comentado

### Exercício 1 — Primeiros Passos

a) `.tables` mostra: `alunos` — a única tabela do banco.

b) `.schema alunos` mostra o comando CREATE TABLE completo, incluindo todas as constraints.

c) `SELECT COUNT(*) FROM alunos;` retorna `5`.

d) Aparecem Bruno (22), Diego (25) e Eva (21) — os três com idade maior que 20.

e) Erro: `UNIQUE constraint failed: alunos.email` — o banco rejeita porque `ana@email.com` já existe.

f) Erro: `CHECK constraint failed: alunos` — o banco rejeita porque a idade -5 viola a constraint `CHECK(idade > 0 AND idade < 150)`.

g) Com `.headers on` e `.mode table`, a saída fica formatada como tabela com bordas e cabeçalhos, muito mais legível.

### Exercício 5 — Context Manager

a) Com `with`, a conexão é fechada automaticamente ao sair do bloco, mesmo se ocorrer um erro. Com `close()` manual, se um erro acontecer antes do `close()`, a conexão fica aberta (vazamento de recurso).

b) Se ocorrer um erro dentro do `with`, o commit NÃO é feito — as alterações são revertidas automaticamente (rollback implícito). Isso é uma proteção contra dados parciais.

c) Para operações de escrita (INSERT, UPDATE, DELETE), o `with` faz commit automático se não houver erro. Mas se você quiser controle explícito (por exemplo, fazer rollback manual em certas condições), pode chamar `conn.commit()` ou `conn.rollback()` dentro do bloco.

### Exercício 6 — Row Factory

c) Acessar por nome (`row['nome']`) é melhor porque: (1) o código é auto-documentado — qualquer pessoa entende o que está sendo acessado; (2) não quebra se a ordem das colunas mudar no SELECT; (3) facilita manutenção — se adicionar uma coluna nova, os índices numéricos mudam mas os nomes não.

---

[← Voltar ao conteúdo: SQLite e Ambiente](cap08-mod04-sqlite-ambiente-conteudo.md)
