# 8.5 — Exercícios: CREATE e INSERT

[← Voltar ao conteúdo: CREATE e INSERT](cap08-mod05-sql-criar-inserir-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem CREATE TABLE (tipos de dados, constraints, chaves primárias e estrangeiras) e INSERT INTO (inserção simples, em lote, com tratamento de erros). Execute todos no seu computador.

---

## Como Executar

```bash
cd ~/meus-projetos/curso/cap08/exercicios
python3 nome_exercicio.py
```

Ou no shell SQLite:

```bash
sqlite3 nome_banco.db
```

---

## Exercício 1: Criando Tabelas de uma Escola

Crie o arquivo `ex01_escola_completa.py` que cria um banco `escola_completa.db` com as seguintes tabelas:

**professores**: id (PK), nome (NOT NULL), email (UNIQUE), disciplina (NOT NULL)

**turmas**: id (PK), nome (NOT NULL, UNIQUE), professor_id (FK → professores), horario (TEXT), sala (TEXT)

**alunos**: id (PK), nome (NOT NULL), email (UNIQUE), data_nascimento (TEXT), turma_id (FK → turmas)

Requisitos:
- Ativar `PRAGMA foreign_keys = ON`
- Usar `IF NOT EXISTS` em todos os CREATE TABLE
- Inserir 3 professores, 4 turmas e 10 alunos usando `executemany()`
- Listar todas as tabelas e seus schemas ao final

```python
# ex01_escola_completa.py
# Cria banco de escola com 3 tabelas relacionadas
# "teacher" = professor, "class" = turma, "student" = aluno
import sqlite3

DATABASE = "escola_completa.db"

def create_tables(conn):
    """Cria todas as tabelas do banco"""
    conn.execute("PRAGMA foreign_keys = ON")

    # TODO: Criar tabela professores
    # TODO: Criar tabela turmas (com FK para professores)
    # TODO: Criar tabela alunos (com FK para turmas)

    conn.commit()
    print("Tabelas criadas com sucesso!")

def insert_data(conn):
    """Insere dados de exemplo"""
    # TODO: Inserir 3 professores
    # TODO: Inserir 4 turmas (cada uma com um professor)
    # TODO: Inserir 10 alunos (distribuidos entre as turmas)

    conn.commit()
    print("Dados inseridos com sucesso!")

def show_schema(conn):
    """Mostra o schema de todas as tabelas"""
    cursor = conn.execute(
        "SELECT name, sql FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    for name, sql in cursor.fetchall():
        print(f"\n--- {name} ---")
        print(sql)

def show_counts(conn):
    """Mostra contagem de registros por tabela"""
    for table in ["professores", "turmas", "alunos"]:
        cursor = conn.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table}: {count} registros")

# Programa principal
with sqlite3.connect(DATABASE) as conn:
    create_tables(conn)
    insert_data(conn)
    print("\n=== Schema do Banco ===")
    show_schema(conn)
    print("\n=== Contagem de Registros ===")
    show_counts(conn)
```

Complete os TODOs e execute o programa.

---

## Exercício 2: Testando Constraints

Crie o arquivo `ex02_constraints.py` que testa cada tipo de constraint:

```python
# ex02_constraints.py
# Testa todas as constraints do banco escola_completa.db
# "constraint" = restricao, "violation" = violacao
import sqlite3

DATABASE = "escola_completa.db"

def test_constraint(conn, description, sql, params=None):
    """Tenta executar uma operacao e mostra se deu erro"""
    try:
        if params:
            conn.execute(sql, params)
        else:
            conn.execute(sql)
        conn.commit()
        print(f"  OK: {description}")
    except sqlite3.IntegrityError as e:
        print(f"  BLOQUEADO: {description}")
        print(f"    Erro: {e}")
    except sqlite3.OperationalError as e:
        print(f"  ERRO SQL: {description}")
        print(f"    Erro: {e}")

with sqlite3.connect(DATABASE) as conn:
    conn.execute("PRAGMA foreign_keys = ON")

    print("=== Testando NOT NULL ===")
    test_constraint(conn,
        "Inserir professor sem nome",
        "INSERT INTO professores (nome, email, disciplina) VALUES (NULL, 'teste@email.com', 'Matematica')"
    )

    print("\n=== Testando UNIQUE ===")
    # TODO: Tentar inserir professor com email que ja existe

    print("\n=== Testando FOREIGN KEY ===")
    # TODO: Tentar inserir aluno com turma_id que nao existe (ex: 999)

    print("\n=== Testando PRIMARY KEY ===")
    # TODO: Tentar inserir professor com id que ja existe

    print("\n=== Testando CHECK (se houver) ===")
    # TODO: Adicionar uma constraint CHECK em alguma tabela e testar

    print("\n=== Testando DELETE com FK ===")
    # TODO: Tentar deletar um professor que tem turmas associadas
```

Complete os TODOs e verifique que cada constraint funciona corretamente.

---

## Exercício 3: INSERT com Dados Reais

Crie o arquivo `ex03_loja_completa.py` que cria um banco de loja com dados realistas:

```python
# ex03_loja_completa.py
# Cria banco de loja com categorias e produtos
# "store" = loja, "category" = categoria, "product" = produto
import sqlite3

DATABASE = "loja_exercicio.db"

def setup(conn):
    """Cria tabelas e insere dados"""
    conn.execute("PRAGMA foreign_keys = ON")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            descricao TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL CHECK(preco > 0),
            estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque >= 0),
            categoria_id INTEGER NOT NULL,
            ativo INTEGER NOT NULL DEFAULT 1,
            data_cadastro TEXT DEFAULT (date('now')),
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)

    # Inserir categorias
    categories = [
        ("Alimentos", "Produtos alimenticios em geral"),
        ("Bebidas", "Bebidas quentes e frias"),
        ("Limpeza", "Produtos de limpeza domestica"),
        ("Higiene", "Produtos de higiene pessoal"),
        ("Papelaria", "Material escolar e escritorio"),
    ]
    conn.executemany(
        "INSERT OR IGNORE INTO categorias (nome, descricao) VALUES (?, ?)",
        categories
    )

    # TODO: Inserir pelo menos 20 produtos distribuidos entre as categorias
    # Use dados realistas com precos e estoques variados
    # Inclua pelo menos 2 produtos inativos (ativo = 0)
    products = [
        # ("nome", "descricao", preco, estoque, categoria_id, ativo),
        # Seu codigo aqui...
    ]

    conn.executemany(
        "INSERT OR IGNORE INTO produtos (nome, descricao, preco, estoque, categoria_id, ativo) VALUES (?, ?, ?, ?, ?, ?)",
        products
    )

    conn.commit()

# TODO: Implemente funcoes para:
# 1. Listar todos os produtos ativos com nome da categoria
# 2. Mostrar total de produtos por categoria
# 3. Mostrar valor total do estoque (preco * estoque de cada produto)
# 4. Listar produtos com estoque baixo (menos de 10 unidades)
# 5. Listar produtos inativos
```

Complete os TODOs com pelo menos 20 produtos e implemente as 5 funções de consulta.

---

## Exercício 4: Tipos de Dados na Prática

Crie o arquivo `ex04_tipos_dados.py` que demonstra o comportamento dos tipos de dados no SQLite:

```python
# ex04_tipos_dados.py
# Demonstra como o SQLite lida com tipos de dados
# "type" = tipo, "affinity" = afinidade
import sqlite3

with sqlite3.connect(":memory:") as conn:
    # Banco em memoria (nao cria arquivo)
    conn.execute("""
        CREATE TABLE teste_tipos (
            id INTEGER PRIMARY KEY,
            campo_integer INTEGER,
            campo_real REAL,
            campo_text TEXT,
            campo_blob BLOB
        )
    """)

    # TODO: Insira valores de diferentes tipos em cada campo e observe o comportamento
    # Teste: o que acontece se inserir texto em campo INTEGER?
    # Teste: o que acontece se inserir numero em campo TEXT?
    # Teste: o que acontece se inserir float em campo INTEGER?
    # Teste: o que acontece se inserir None (NULL) em cada campo?

    # Para cada teste, insira o valor e depois leia de volta com typeof()
    # Exemplo:
    conn.execute("INSERT INTO teste_tipos (id, campo_integer) VALUES (1, 42)")
    conn.execute("INSERT INTO teste_tipos (id, campo_integer) VALUES (2, 'texto')")
    conn.execute("INSERT INTO teste_tipos (id, campo_integer) VALUES (3, 3.14)")
    conn.execute("INSERT INTO teste_tipos (id, campo_integer) VALUES (4, NULL)")

    cursor = conn.execute(
        "SELECT id, campo_integer, typeof(campo_integer) FROM teste_tipos"
    )
    print("=== Tipo real armazenado em campo INTEGER ===")
    for row in cursor.fetchall():
        print(f"  id={row[0]}, valor={row[1]}, tipo={row[2]}")
```

Execute e responda:
a) O SQLite rejeita tipos incompatíveis ou aceita tudo?
b) O que a função `typeof()` retorna para cada valor?
c) Por que isso é diferente de bancos como PostgreSQL (que são mais rígidos com tipos)?
d) Quais problemas isso pode causar em um sistema real?

---

## Exercício 5: Datas no SQLite

O SQLite não tem tipo DATE nativo — datas são armazenadas como TEXT. Crie o arquivo `ex05_datas.py`:

```python
# ex05_datas.py
# Trabalhando com datas no SQLite
# "date" = data, "event" = evento
import sqlite3

DATABASE = ":memory:"

with sqlite3.connect(DATABASE) as conn:
    conn.execute("""
        CREATE TABLE eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_evento TEXT NOT NULL,
            data_criacao TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)

    # Inserir eventos com datas no formato ISO
    events = [
        ("Ano Novo", "2025-01-01"),
        ("Carnaval", "2025-03-04"),
        ("Natal", "2025-12-25"),
        ("Dia das Maes", "2025-05-11"),
        ("Dia dos Pais", "2025-08-10"),
        ("Independencia", "2025-09-07"),
    ]
    conn.executemany(
        "INSERT INTO eventos (nome, data_evento) VALUES (?, ?)",
        events
    )

    # TODO: Escreva queries para:
    # 1. Listar eventos ordenados por data
    # 2. Listar eventos do primeiro semestre (janeiro a junho)
    # 3. Listar eventos que ainda nao aconteceram (data > hoje)
    # 4. Calcular quantos dias faltam para cada evento futuro
    # 5. Agrupar eventos por mes

    # Dica: use as funcoes date(), strftime() do SQLite
    # strftime('%m', data_evento) extrai o mes
    # julianday(data1) - julianday(data2) calcula diferenca em dias
```

---

## Exercício 6: INSERT com Validação em Python

Crie o arquivo `ex06_validacao.py` que válida dados antes de inserir no banco:

```python
# ex06_validacao.py
# Valida dados antes de inserir no banco
# "validate" = validar, "input" = entrada
import sqlite3
import re  # "re" = regular expressions (expressoes regulares)

DATABASE = "clientes_validados.db"

def validate_email(email):
    """Verifica se o email tem formato valido"""
    # Regex simples para email
    # "pattern" = padrao, "match" = corresponder
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Verifica se o telefone tem formato valido (XX-XXXXX-XXXX)"""
    pattern = r'^\d{2}-\d{4,5}-\d{4}$'
    return re.match(pattern, phone) is not None

def validate_name(name):
    """Verifica se o nome tem pelo menos 2 caracteres"""
    return len(name.strip()) >= 2

def add_client(conn, name, email, phone):
    """Adiciona cliente com validacao completa"""
    # "errors" = erros
    errors = []

    if not validate_name(name):
        errors.append("Nome deve ter pelo menos 2 caracteres")
    if not validate_email(email):
        errors.append(f"Email invalido: {email}")
    if phone and not validate_phone(phone):
        errors.append(f"Telefone invalido: {phone} (formato: XX-XXXXX-XXXX)")

    if errors:
        print(f"  Erros de validacao para '{name}':")
        for error in errors:
            print(f"    - {error}")
        return False

    try:
        conn.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (name.strip(), email.strip().lower(), phone)
        )
        conn.commit()
        print(f"  Cliente '{name}' cadastrado com sucesso!")
        return True
    except sqlite3.IntegrityError as e:
        print(f"  Erro de integridade para '{name}': {e}")
        return False

# TODO: Crie a tabela clientes e teste com dados validos e invalidos
# Teste: nome vazio, email sem @, telefone com formato errado, email duplicado
```

Complete o programa e teste com pelo menos 8 tentativas de inserção (4 válidas e 4 inválidas).

---

## Exercício 7: Criando um Banco Completo — Videolocadora

Crie o arquivo `ex07_videolocadora.py` que modela e cria um banco para uma videolocadora:

Tabelas necessárias:
- **generos**: id, nome (UNIQUE)
- **filmes**: id, título, ano, duracao_minutos, genero_id (FK), classificação (L, 10, 12, 14, 16, 18)
- **clientes**: id, nome, cpf (UNIQUE), telefone, data_cadastro
- **locacoes**: id, cliente_id (FK), filme_id (FK), data_locacao, data_prevista_devolucao, data_devolucao, valor

Requisitos:
a) Criar todas as tabelas com constraints apropriadas
b) Inserir pelo menos 5 gêneros, 15 filmes, 5 clientes e 10 locações
c) Algumas locações devem ter `data_devolucao = NULL` (ainda não devolvidas)
d) Implementar função que lista filmes disponíveis (não emprestados atualmente)
e) Implementar função que lista clientes com locações em atraso
f) Implementar função que mostra o gênero mais popular (mais locações)

---

## Exercício 8: Desafio — Gerador de Dados

Crie o arquivo `ex08_gerador.py` que gera dados aleatórios para popular um banco:

```python
# ex08_gerador.py
# Gera dados aleatorios para popular um banco de teste
# "generate" = gerar, "random" = aleatorio, "fake" = falso
import sqlite3
import random
import string

# Listas de dados para gerar nomes e valores aleatorios
FIRST_NAMES = ["Ana", "Bruno", "Carla", "Diego", "Eva", "Felipe",
               "Gabriela", "Hugo", "Isabela", "Joao", "Karen", "Lucas",
               "Maria", "Nicolas", "Olivia", "Pedro", "Raquel", "Samuel"]

LAST_NAMES = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Costa",
              "Ferreira", "Pereira", "Almeida", "Nascimento", "Carvalho"]

PRODUCT_NAMES = ["Arroz", "Feijao", "Macarrao", "Cafe", "Acucar", "Sal",
                 "Oleo", "Leite", "Manteiga", "Queijo", "Presunto", "Pao",
                 "Biscoito", "Suco", "Refrigerante", "Agua", "Cerveja",
                 "Sabao", "Detergente", "Esponja"]

def random_name():
    """Gera um nome aleatorio"""
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_email(name):
    """Gera email a partir do nome"""
    # "clean" = limpo
    clean = name.lower().replace(" ", ".").replace("á", "a").replace("ã", "a")
    number = random.randint(1, 999)
    return f"{clean}{number}@email.com"

def random_price():
    """Gera preco aleatorio entre 1.00 e 100.00"""
    return round(random.uniform(1.0, 100.0), 2)

# TODO: Crie um banco com tabelas de clientes e produtos
# TODO: Gere e insira 100 clientes com dados aleatorios
# TODO: Gere e insira 50 produtos com dados aleatorios
# TODO: Gere e insira 200 pedidos com itens aleatorios
# TODO: Mostre estatisticas do banco gerado (contagens, medias, etc.)
```

Este exercício prática inserção em lote e prepara você para trabalhar com volumes maiores de dados.

---

## Gabarito Comentado

### Exercício 4 — Tipos de Dados

a) O SQLite aceita quase tudo — ele usa "type affinity" (afinidade de tipo) em vez de tipos rígidos. Um campo INTEGER pode receber texto, e o SQLite armazena como texto. Isso é uma característica única do SQLite.

b) `typeof()` retorna o tipo real do valor armazenado: `integer`, `real`, `text`, `blob` ou `null`. Pode ser diferente do tipo declarado na coluna.

c) PostgreSQL e MySQL são "strongly typed" — rejeitam valores incompatíveis com o tipo da coluna. SQLite é "weakly typed" — aceita qualquer valor em qualquer coluna (exceto INTEGER PRIMARY KEY). Isso torna o SQLite mais flexível mas menos seguro.

d) Problemas: dados inconsistentes (texto onde deveria ser número), erros silenciosos (o banco aceita o dado errado sem avisar), dificuldade de migração para bancos mais rígidos. Por isso é importante validar dados no código Python antes de inserir.

### Exercício 5 — Datas

Queries de exemplo:

```sql
-- 1. Eventos ordenados por data
SELECT * FROM eventos ORDER BY data_evento;

-- 2. Primeiro semestre
SELECT * FROM eventos WHERE strftime('%m', data_evento) <= '06';

-- 3. Eventos futuros
SELECT * FROM eventos WHERE data_evento > date('now');

-- 4. Dias faltando
SELECT nome, data_evento,
       CAST(julianday(data_evento) - julianday('now') AS INTEGER) AS dias_faltando
FROM eventos
WHERE data_evento > date('now')
ORDER BY data_evento;

-- 5. Agrupados por mes
SELECT strftime('%m', data_evento) AS mes, GROUP_CONCAT(nome) AS eventos
FROM eventos
GROUP BY mes
ORDER BY mes;
```

---

[← Voltar ao conteúdo: CREATE e INSERT](cap08-mod05-sql-criar-inserir-conteudo.md)
