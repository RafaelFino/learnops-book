# 8.5 — CREATE e INSERT: Criando Tabelas e Inserindo Dados

[← Anterior: SQLite e Ambiente](cap08-mod04-sqlite-ambiente-conteudo.md) · [Próximo: SELECT e Consultas →](cap08-mod06-sql-select-conteudo.md)

---

## Introdução

No módulo anterior, você instalou o SQLite, criou seu primeiro banco de dados e aprendeu a se conectar usando Python. Viu rapidamente como criar uma tabela e inserir dados, mas sem entrar em detalhes. Agora vamos aprofundar.

Neste módulo, você vai aprender dois dos comandos mais fundamentais do SQL: **CREATE TABLE** (criar tabela) e **INSERT INTO** (inserir dados). São os comandos que definem a estrutura do seu banco e o populam com informações. Sem eles, o banco é apenas um arquivo vazio.

CREATE TABLE é onde você traduz a modelagem que aprendeu no módulo 8.3 em código SQL real. Cada decisão de modelagem — tipos de dados, chaves primárias, chaves estrangeiras, restrições — se materializa aqui. INSERT INTO é onde os dados ganham vida — cada registro que você insere é uma linha nova na tabela.

Vamos trabalhar com o exemplo da lanchonete que modelamos no módulo 8.3, criando todas as tabelas e populando com dados de exemplo.

---

## Como Executar os Exemplos Deste Módulo

Todos os exemplos podem ser executados de duas formas:

**No shell SQLite:**

```bash
sqlite3 lanchonete.db
```

**Em Python:**

```bash
python3 nome_exemplo.py
```

Recomendo que você execute cada exemplo nas duas formas para se familiarizar com ambas.

---

## CREATE TABLE: Anatomia Completa

O comando CREATE TABLE define a estrutura de uma tabela. Vamos ver a sintaxe completa:

```sql
-- Sintaxe geral do CREATE TABLE
-- Cada linha dentro dos parenteses define uma coluna
CREATE TABLE nome_da_tabela (
    nome_coluna TIPO RESTRICOES,
    nome_coluna TIPO RESTRICOES,
    nome_coluna TIPO RESTRICOES
);
```

Vamos criar a tabela de categorias da lanchonete:

```sql
-- Cria a tabela de categorias
-- "categorias" = tabela que agrupa tipos de produtos
CREATE TABLE categorias (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- chave primaria com auto-incremento
    nome TEXT NOT NULL,                     -- nome da categoria, obrigatorio
    descricao TEXT                          -- descricao opcional (aceita NULL)
);
```

Saída esperada:

```
(nenhuma saida - tabela criada com sucesso)
```

Vamos analisar cada parte:

| Parte | Significado |
|-------|-------------|
| CREATE TABLE | Comando para criar uma nova tabela |
| categorias | Nome da tabela |
| id | Nome da primeira coluna |
| INTEGER | Tipo de dado: número inteiro |
| PRIMARY KEY | Esta coluna e a chave primaria |
| AUTOINCREMENT | O valor e gerado automaticamente (1, 2, 3...) |
| nome | Nome da segunda coluna |
| TEXT | Tipo de dado: texto |
| NOT NULL | Restrição: este campo e obrigatório |
| descrição | Nome da terceira coluna |
| TEXT | Tipo de dado: texto (sem NOT NULL, aceita NULL) |

---

## Tipos de Dados no SQLite

O SQLite tem um sistema de tipos simplificado comparado a outros bancos. Existem 5 tipos de armazenamento:

| Tipo | Descrição | Exemplos |
|------|-----------|----------|
| NULL | Ausência de valor | NULL |
| INTEGER | Número inteiro | 1, 42, -100, 0 |
| REAL | Número decimal (ponto flutuante) | 3.14, 22.90, -0.5 |
| TEXT | Texto (string) | 'Arroz', 'ana@email.com', '2024-03-15' |
| BLOB | Dados binarios | Imagens, arquivos (raramente usado) |

### Tipos Comuns e Suas Aplicações

Na prática, você vai usar principalmente INTEGER, REAL e TEXT:

| Dado | Tipo recomendado | Justificativa |
|------|-----------------|---------------|
| ID (chave primaria) | INTEGER | Eficiente, auto-incremento nativo |
| Nome, descrição | TEXT | Texto de tamanho variável |
| Email | TEXT | Texto com formato específico |
| Preco, valor monetario | REAL | Número com casas decimais |
| Quantidade, estoque | INTEGER | Número inteiro |
| Data | TEXT | Formato 'AAAA-MM-DD' (ISO 8601) |
| Hora | TEXT | Formato 'HH:MM:SS' |
| Data e hora | TEXT | Formato 'AAAA-MM-DD HH:MM:SS' |
| Sim ou Não (booleano) | INTEGER | 0 = não, 1 = sim |
| Status com opcoes | TEXT | 'pendente', 'ativo', 'cancelado' |

### Por que Datas São TEXT no SQLite?

O SQLite não tem um tipo DATE nativo como PostgreSQL ou MySQL. Datas são armazenadas como TEXT no formato ISO 8601: `'2024-03-15'`. Esse formato tem uma vantagem importante: ele é **ordenável naturalmente**. Se você ordenar textos no formato AAAA-MM-DD, a ordem alfabética coincide com a ordem cronológica.

```sql
-- Datas como TEXT no formato ISO
-- Ordenacao funciona corretamente
SELECT * FROM pedidos ORDER BY data_pedido;
-- 2024-01-15 vem antes de 2024-03-20 (ordem alfabetica = ordem cronologica)
```

Se usasse o formato brasileiro DD/MM/AAAA, a ordenação ficaria errada: '15/01/2024' viria depois de '01/03/2024' na ordem alfabética, mas cronologicamente é antes.

### Datatypes e Performance

A escolha do tipo de dado afeta a performance do banco. Alguns exemplos:

**CEP como INTEGER vs TEXT:**

```sql
-- CEP como INTEGER: 01310100 vira 1310100 (perde o zero a esquerda!)
-- CEP como TEXT: '01310100' mantem o formato correto
-- Conclusao: CEP deve ser TEXT
```

**Preço como INTEGER vs REAL:**

```sql
-- Preco como INTEGER (em centavos): 2290 = R$ 22.90
-- Preco como REAL: 22.90
-- INTEGER e mais preciso (sem problemas de ponto flutuante)
-- REAL e mais legivel e pratico para aprendizado
-- Em sistemas financeiros profissionais, usa-se INTEGER em centavos
```

**Booleano como INTEGER:**

```sql
-- SQLite nao tem tipo BOOLEAN nativo
-- Usa-se INTEGER: 0 = falso, 1 = verdadeiro
-- Exemplo: disponivel INTEGER DEFAULT 1
```

---

## Constraints (Restrições)

Constraints são regras que o banco impõe sobre os dados. Elas garantem integridade — se alguém tentar inserir dados que violam uma regra, o banco rejeita a operação.

### PRIMARY KEY

Identifica cada registro de forma única. Não aceita duplicatas nem NULL.

```sql
id INTEGER PRIMARY KEY AUTOINCREMENT
```

### NOT NULL

O campo é obrigatório — não aceita valor NULL.

```sql
nome TEXT NOT NULL  -- todo produto precisa de nome
```

### UNIQUE

O valor deve ser único na tabela — não pode haver duplicatas.

```sql
email TEXT UNIQUE NOT NULL  -- cada cliente tem email unico
```

### DEFAULT

Define um valor padrão quando nenhum valor é informado.

```sql
disponivel INTEGER DEFAULT 1     -- padrao: disponivel (1 = sim)
data_cadastro TEXT DEFAULT (date('now'))  -- padrao: data atual
```

### CHECK

Válida que o valor atende a uma condição.

```sql
preco REAL CHECK(preco > 0)           -- preco deve ser positivo
nota INTEGER CHECK(nota >= 1 AND nota <= 5)  -- nota entre 1 e 5
```

### FOREIGN KEY

Referência a chave primária de outra tabela. Garante integridade referencial.

```sql
categoria_id INTEGER REFERENCES categorias(id)
```

### Tabela Resumo de Constraints

| Constraint | O que faz | Exemplo |
|------------|-----------|---------|
| PRIMARY KEY | Identifica registro unicamente | id INTEGER PRIMARY KEY |
| NOT NULL | Campo obrigatório | nome TEXT NOT NULL |
| UNIQUE | Valor único na tabela | email TEXT UNIQUE |
| DEFAULT | Valor padrão | status TEXT DEFAULT 'ativo' |
| CHECK | Válida condição | preco REAL CHECK(preco > 0) |
| FOREIGN KEY | Referência outra tabela | REFERENCES categorias(id) |

---

## Criando as Tabelas da Lanchonete

Agora vamos criar todas as tabelas do modelo que projetamos no módulo 8.3:

```python
# criar_tabelas_lanchonete.py
# Cria todas as tabelas do sistema da lanchonete
import sqlite3

with sqlite3.connect("lanchonete.db") as conn:
    cursor = conn.cursor()
    
    # Habilita suporte a chaves estrangeiras
    # Por padrao, SQLite nao verifica FKs - precisamos ativar
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # 1. Tabela de categorias (nao depende de nenhuma outra)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT
        )
    """)
    print("Tabela 'categorias' criada!")
    
    # 2. Tabela de produtos (depende de categorias)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL CHECK(preco > 0),
            categoria_id INTEGER NOT NULL,
            disponivel INTEGER DEFAULT 1,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)
    print("Tabela 'produtos' criada!")
    
    # 3. Tabela de clientes (nao depende de nenhuma outra)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT UNIQUE,
            data_cadastro TEXT DEFAULT (date('now'))
        )
    """)
    print("Tabela 'clientes' criada!")
    
    # 4. Tabela de pedidos (depende de clientes)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            data_pedido TEXT DEFAULT (datetime('now')),
            valor_total REAL DEFAULT 0,
            status TEXT DEFAULT 'pendente' CHECK(
                status IN ('pendente', 'preparando', 'pronto', 'entregue', 'cancelado')
            ),
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)
    print("Tabela 'pedidos' criada!")
    
    # 5. Tabela de itens do pedido (depende de pedidos e produtos)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS itens_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            produto_id INTEGER NOT NULL,
            quantidade INTEGER NOT NULL CHECK(quantidade > 0),
            preco_unitario REAL NOT NULL CHECK(preco_unitario > 0),
            FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
    """)
    print("Tabela 'itens_pedido' criada!")
    
    conn.commit()
    
    # Verifica as tabelas criadas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")
    tables = cursor.fetchall()
    print(f"\nTabelas no banco: {[t[0] for t in tables]}")
```

Saída esperada:

```
Tabela 'categorias' criada!
Tabela 'produtos' criada!
Tabela 'clientes' criada!
Tabela 'pedidos' criada!
Tabela 'itens_pedido' criada!

Tabelas no banco: ['categorias', 'clientes', 'itens_pedido', 'pedidos', 'produtos']
```

### Detalhes Importantes

**PRAGMA foreign_keys = ON**: por padrão, o SQLite não verifica chaves estrangeiras. Precisamos ativar explicitamente com esse comando. Sem ele, você poderia inserir um produto com `categoria_id = 999` mesmo que a categoria 999 não exista.

**Ordem de criação**: tabelas que são referenciadas por outras devem ser criadas primeiro. `categorias` antes de `produtos`, `clientes` antes de `pedidos`.

**IF NOT EXISTS**: evita erro se a tabela já existir. Sem isso, executar o script duas vezes daria erro.

**CHECK com IN**: a constraint `CHECK(status IN ('pendente', 'preparando', ...))` garante que o status só pode ter um dos valores listados.

---

## INSERT INTO: Inserindo Dados

Com as tabelas criadas, vamos populá-las com dados. O comando INSERT INTO adiciona novas linhas a uma tabela.

### Sintaxe Básica

```sql
-- Sintaxe: INSERT INTO tabela (colunas) VALUES (valores)
INSERT INTO categorias (nome, descricao) VALUES ('Lanches', 'Sanduiches e hamburgueres');
```

Observe que não informamos o `id` — ele é gerado automaticamente pelo AUTOINCREMENT.

### Inserindo Dados na Lanchonete

```python
# inserir_dados_lanchonete.py
# Popula o banco da lanchonete com dados de exemplo
import sqlite3

with sqlite3.connect("lanchonete.db") as conn:
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # --- Inserir categorias ---
    categorias = [
        ("Lanches", "Sanduiches e hamburgueres"),
        ("Bebidas", "Refrigerantes, sucos e agua"),
        ("Sobremesas", "Doces e sorvetes"),
        ("Porcoes", "Acompanhamentos e porcoes"),
    ]
    
    cursor.executemany(
        "INSERT INTO categorias (nome, descricao) VALUES (?, ?)",
        categorias
    )
    print(f"{len(categorias)} categorias inseridas!")
    
    # --- Inserir produtos ---
    produtos = [
        ("X-Burguer", "Hamburguer com queijo", 18.90, 1, 1),
        ("X-Salada", "Hamburguer com salada e queijo", 21.90, 1, 1),
        ("X-Bacon", "Hamburguer com bacon e queijo", 24.90, 1, 1),
        ("X-Tudo", "Hamburguer completo", 28.90, 1, 1),
        ("Coca-Cola 350ml", "Refrigerante lata", 6.00, 2, 1),
        ("Guarana 350ml", "Refrigerante lata", 5.50, 2, 1),
        ("Suco Natural", "Suco de laranja natural", 8.00, 2, 0),
        ("Agua 500ml", "Agua mineral sem gas", 3.00, 2, 1),
        ("Pudim", "Pudim de leite condensado", 10.00, 3, 1),
        ("Sorvete", "Sorvete 2 bolas", 12.00, 3, 1),
        ("Batata Frita", "Porcao de batata frita", 15.00, 4, 1),
        ("Onion Rings", "Aneis de cebola empanados", 18.00, 4, 1),
    ]
    
    cursor.executemany(
        "INSERT INTO produtos (nome, descricao, preco, categoria_id, disponivel) VALUES (?, ?, ?, ?, ?)",
        produtos
    )
    print(f"{len(produtos)} produtos inseridos!")
    
    # --- Inserir clientes ---
    clientes = [
        ("Joao Silva", "11-99999-0001", "joao@email.com"),
        ("Maria Santos", "11-99999-0002", "maria@email.com"),
        ("Pedro Lima", "11-99999-0003", "pedro@email.com"),
        ("Ana Costa", "11-99999-0004", "ana@email.com"),
        ("Carlos Oliveira", None, "carlos@email.com"),
    ]
    
    cursor.executemany(
        "INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
        clientes
    )
    print(f"{len(clientes)} clientes inseridos!")
    
    # --- Inserir pedidos ---
    # Pedido 1: Joao pediu X-Burguer + Coca + Pudim
    cursor.execute(
        "INSERT INTO pedidos (cliente_id, data_pedido, valor_total, status) VALUES (?, ?, ?, ?)",
        (1, "2024-03-01 12:30:00", 34.90, "entregue")
    )
    pedido1_id = cursor.lastrowid  # pega o id do ultimo registro inserido
    
    # Pedido 2: Maria pediu X-Salada + Guarana
    cursor.execute(
        "INSERT INTO pedidos (cliente_id, data_pedido, valor_total, status) VALUES (?, ?, ?, ?)",
        (2, "2024-03-01 13:15:00", 27.40, "entregue")
    )
    pedido2_id = cursor.lastrowid
    
    # Pedido 3: Pedro pediu X-Tudo + Batata + Coca
    cursor.execute(
        "INSERT INTO pedidos (cliente_id, data_pedido, valor_total, status) VALUES (?, ?, ?, ?)",
        (3, "2024-03-02 19:00:00", 49.90, "pronto")
    )
    pedido3_id = cursor.lastrowid
    
    print("3 pedidos inseridos!")
    
    # --- Inserir itens dos pedidos ---
    itens = [
        # Pedido 1: X-Burguer + Coca + Pudim
        (pedido1_id, 1, 1, 18.90),   # 1 X-Burguer
        (pedido1_id, 5, 1, 6.00),    # 1 Coca-Cola
        (pedido1_id, 9, 1, 10.00),   # 1 Pudim
        # Pedido 2: X-Salada + Guarana
        (pedido2_id, 2, 1, 21.90),   # 1 X-Salada
        (pedido2_id, 6, 1, 5.50),    # 1 Guarana
        # Pedido 3: X-Tudo + Batata + Coca
        (pedido3_id, 4, 1, 28.90),   # 1 X-Tudo
        (pedido3_id, 11, 1, 15.00),  # 1 Batata Frita
        (pedido3_id, 5, 1, 6.00),    # 1 Coca-Cola
    ]
    
    cursor.executemany(
        "INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
        itens
    )
    print(f"{len(itens)} itens de pedido inseridos!")
    
    conn.commit()
    
    # --- Resumo ---
    print("\n--- Resumo do banco ---")
    for table in ["categorias", "produtos", "clientes", "pedidos", "itens_pedido"]:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table}: {count} registros")
```

Saída esperada:

```
4 categorias inseridas!
12 produtos inseridos!
5 clientes inseridos!
3 pedidos inseridos!
8 itens de pedido inseridos!

--- Resumo do banco ---
  categorias: 4 registros
  produtos: 12 registros
  clientes: 5 registros
  pedidos: 3 registros
  itens_pedido: 8 registros
```

### lastrowid: Pegando o ID do Registro Inserido

Observe o uso de `cursor.lastrowid` — ele retorna o id do último registro inserido. Isso é essencial quando você precisa do id para inserir registros relacionados (como itens de um pedido que precisa do id do pedido).

---

## INSERT OR IGNORE e INSERT OR REPLACE

Às vezes você quer inserir um registro, mas ele pode já existir (por exemplo, um email que é UNIQUE). O SQLite oferece variações do INSERT para lidar com isso:

### INSERT OR IGNORE

Se o registro violar uma constraint (como UNIQUE), a operação é silenciosamente ignorada:

```sql
-- Se o email ja existir, nao faz nada (sem erro)
INSERT OR IGNORE INTO clientes (nome, email) VALUES ('Ana Costa', 'ana@email.com');
```

### INSERT OR REPLACE

Se o registro violar uma constraint, o registro existente é substituído pelo novo:

```sql
-- Se o email ja existir, substitui o registro inteiro
INSERT OR REPLACE INTO clientes (nome, email) VALUES ('Ana Costa Nova', 'ana@email.com');
```

| Variacao | Comportamento com conflito |
|----------|---------------------------|
| INSERT | Erro - operação falha |
| INSERT OR IGNORE | Ignora silenciosamente |
| INSERT OR REPLACE | Substitui o registro existente |

---

## Verificando Constraints na Prática

Vamos ver o que acontece quando tentamos violar constraints:

```python
# testar_constraints.py
# Demonstra o comportamento das constraints
import sqlite3

with sqlite3.connect("lanchonete.db") as conn:
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    
    # Teste 1: NOT NULL - tentar inserir categoria sem nome
    print("Teste 1: Inserir categoria sem nome (NOT NULL)")
    try:
        cursor.execute("INSERT INTO categorias (nome) VALUES (NULL)")
        print("  Resultado: Inserido (nao deveria!)")
    except sqlite3.IntegrityError as e:
        print(f"  Resultado: ERRO - {e}")
    
    # Teste 2: UNIQUE - tentar inserir email duplicado
    print("\nTeste 2: Inserir email duplicado (UNIQUE)")
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            ("Outro Joao", "joao@email.com")
        )
        print("  Resultado: Inserido (nao deveria!)")
    except sqlite3.IntegrityError as e:
        print(f"  Resultado: ERRO - {e}")
    
    # Teste 3: CHECK - tentar inserir preco negativo
    print("\nTeste 3: Inserir preco negativo (CHECK)")
    try:
        cursor.execute(
            "INSERT INTO produtos (nome, preco, categoria_id) VALUES (?, ?, ?)",
            ("Produto Invalido", -5.00, 1)
        )
        print("  Resultado: Inserido (nao deveria!)")
    except sqlite3.IntegrityError as e:
        print(f"  Resultado: ERRO - {e}")
    
    # Teste 4: FOREIGN KEY - tentar inserir produto com categoria inexistente
    print("\nTeste 4: Inserir produto com categoria inexistente (FK)")
    try:
        cursor.execute(
            "INSERT INTO produtos (nome, preco, categoria_id) VALUES (?, ?, ?)",
            ("Produto Orfao", 10.00, 999)
        )
        print("  Resultado: Inserido (nao deveria!)")
    except sqlite3.IntegrityError as e:
        print(f"  Resultado: ERRO - {e}")
    
    # Teste 5: CHECK com IN - tentar inserir status invalido
    print("\nTeste 5: Inserir status invalido (CHECK IN)")
    try:
        cursor.execute(
            "INSERT INTO pedidos (cliente_id, status) VALUES (?, ?)",
            (1, "invalido")
        )
        print("  Resultado: Inserido (nao deveria!)")
    except sqlite3.IntegrityError as e:
        print(f"  Resultado: ERRO - {e}")
    
    print("\nTodos os testes concluidos!")
    print("As constraints protegeram o banco contra dados invalidos.")
```

Saída esperada:

```
Teste 1: Inserir categoria sem nome (NOT NULL)
  Resultado: ERRO - NOT NULL constraint failed: categorias.nome

Teste 2: Inserir email duplicado (UNIQUE)
  Resultado: ERRO - UNIQUE constraint failed: clientes.email

Teste 3: Inserir preco negativo (CHECK)
  Resultado: ERRO - CHECK constraint failed: produtos

Teste 4: Inserir produto com categoria inexistente (FK)
  Resultado: ERRO - FOREIGN KEY constraint failed

Teste 5: Inserir status invalido (CHECK IN)
  Resultado: ERRO - CHECK constraint failed: pedidos

Todos os testes concluidos!
As constraints protegeram o banco contra dados invalidos.
```

Cada constraint fez seu trabalho — rejeitou dados inválidos e protegeu a integridade do banco. Isso é muito mais seguro do que validar apenas no código Python, porque as regras valem para qualquer programa que acesse o banco.

---

## ALTER TABLE e DROP TABLE

Depois de criar uma tabela, você pode modificá-la ou removê-la:

### ALTER TABLE — Modificar Tabela

```sql
-- Adicionar uma coluna
ALTER TABLE produtos ADD COLUMN peso REAL;

-- Renomear uma tabela
ALTER TABLE categorias RENAME TO tipos;

-- Renomear uma coluna (SQLite 3.25+)
ALTER TABLE produtos RENAME COLUMN peso TO peso_kg;
```

Limitações do ALTER TABLE no SQLite:
- Não pode remover colunas (em versões antigas, antes da 3.35)
- Não pode alterar o tipo de uma coluna
- Não pode adicionar constraints a colunas existentes

Para mudanças mais complexas, a estratégia é: criar tabela nova → copiar dados → remover tabela antiga → renomear tabela nova.

### DROP TABLE — Remover Tabela

```sql
-- Remove a tabela completamente (dados e estrutura)
-- CUIDADO: nao tem como desfazer!
DROP TABLE IF EXISTS nome_tabela;
```

`DROP TABLE` é destrutivo — remove a tabela e todos os seus dados permanentemente. Use com muito cuidado.

---

## Como a IA pode te ajudar aqui
**Prompt 1 — Pedir ajuda prática:**
> "Preciso criar uma tabela de funcionários com nome, cargo, salário, data de admissão e departamento. Me ajude a escrever o CREATE TABLE com os tipos e constraints corretos."

**Prompt 2 — Entender erros comuns:**
> "Estou recebendo 'FOREIGN KEY constraint failed' ao inserir um produto. O que está acontecendo?"

**Prompt 3 — Converter e transformar:**
> "Tenho este diagrama ER [cole o diagrama]. Me ajude a converter em comandos CREATE TABLE para SQLite."

---

## Casos de Uso no Mundo Real

### Caso 1: Migrações em Startups

Quando uma startup cresce, a estrutura do banco precisa evoluir. Novos campos são adicionados (ALTER TABLE), novas tabelas são criadas (CREATE TABLE), dados são migrados. Ferramentas como Alembic (Python) e Flyway (Java) automatizam esse processo, mas por baixo executam os mesmos comandos CREATE e ALTER que você aprendeu aqui.

### Caso 2: Seed Data em Desenvolvimento

Quando desenvolvedores começam a trabalhar em um projeto, precisam de dados de teste no banco. Scripts de "seed" (semente) usam INSERT para popular o banco com dados fictícios — exatamente como fizemos com a lanchonete. Empresas mantêm scripts de seed atualizados para que qualquer desenvolvedor possa ter um banco funcional em minutos.

### Caso 3: Importação de Dados em Massa

Empresas frequentemente precisam importar dados de planilhas, CSVs ou outros sistemas para o banco. Isso envolve ler o arquivo, validar os dados e executar milhares de INSERTs. O `executemany()` que aprendemos é a base dessa operação — inserir muitos registros de forma eficiente.

---

## Resumo do Módulo

| Conceito | Definição |
|----------|-----------|
| CREATE TABLE | Comando SQL para criar uma nova tabela |
| INSERT INTO | Comando SQL para inserir dados em uma tabela |
| INTEGER, REAL, TEXT | Tipos de dados principais do SQLite |
| PRIMARY KEY | Constraint que identifica registros unicamente |
| NOT NULL | Constraint que torna um campo obrigatório |
| UNIQUE | Constraint que impede valores duplicados |
| DEFAULT | Define valor padrão para uma coluna |
| CHECK | Constraint que válida uma condição |
| FOREIGN KEY | Constraint que referência outra tabela |
| AUTOINCREMENT | Gera valores sequenciais automaticamente |
| ALTER TABLE | Comando para modificar estrutura de tabela existente |
| DROP TABLE | Comando para remover uma tabela completamente |

---

## Glossário do Módulo

| Termo | Definição |
|-------|-----------|
| ALTER TABLE | Comando SQL para modificar a estrutura de uma tabela existente |
| AUTOINCREMENT | Mecanismo que gera valores inteiros sequenciais automaticamente |
| BLOB (Binary Large Object) | Tipo de dado para armazenar dados binarios |
| CHECK | Constraint que válida uma condição lógica sobre os dados |
| Constraint (restrição) | Regra imposta pelo banco sobre os valores de uma coluna |
| CREATE TABLE | Comando SQL para definir e criar uma nova tabela |
| DEFAULT | Valor atribuido automaticamente quando nenhum valor e informado |
| DROP TABLE | Comando SQL para remover uma tabela e todos os seus dados |
| executemany | Método Python para executar o mesmo SQL com multiplos conjuntos de dados |
| FOREIGN KEY (chave estrangeira) | Constraint que garante que um valor referência um registro válido em outra tabela |
| IF NOT EXISTS | Clausula que evita erro ao criar tabela que ja existe |
| INSERT INTO | Comando SQL para adicionar novos registros a uma tabela |
| INSERT OR IGNORE | Variacao que ignora silenciosamente conflitos de constraint |
| INSERT OR REPLACE | Variacao que substitui registros em caso de conflito |
| IntegrityError | Exceção Python lancada quando uma constraint e violada |
| ISO 8601 | Padrão internacional para formato de datas (AAAA-MM-DD) |
| lastrowid | Propriedade do cursor que retorna o id do último registro inserido |
| NOT NULL | Constraint que impede valores nulos em uma coluna |
| PRAGMA | Comando especial do SQLite para configurar comportamentos |
| PRIMARY KEY (chave primaria) | Constraint que identifica cada registro de forma única |
| Seed data | Dados iniciais inseridos no banco para desenvolvimento e testes |
| UNIQUE | Constraint que garante valores unicos em uma coluna |

---

## Na Cultura Popular

- **The Social Network** (filme, 2010) — na cena em que Mark Zuckerberg cria o FaceMash em uma noite, ele precisa criar tabelas para armazenar fotos e votos dos estudantes. Embora o filme não mostre SQL, a lógica é exatamente o que fizemos: CREATE TABLE para definir a estrutura, INSERT para popular com dados. A velocidade com que ele constrói o sistema mostra como SQL é direto e eficiente.

---

## Para Saber Mais

- [SQLBolt — Lições sobre CREATE e INSERT](https://sqlbolt.com/lesson/creating_tables) — *Tutorial interativo para praticar criação de tabelas e inserção de dados.*

- [SQLite Documentation — CREATE TABLE](https://www.sqlite.org/lang_createtable.html) — *Referência oficial completa do comando CREATE TABLE no SQLite.*

- [SQL Murder Mystery](https://mystery.knightlab.com/) — *Jogo de detetive que usa SELECT para resolver um crime. Ótimo para praticar consultas no próximo módulo.*

- [Curso em Vídeo — MySQL](https://www.youtube.com/playlist?list=PLHz_AreHm4dkBs-795Dsgvau_ekxg8g1r) — *As aulas sobre CREATE TABLE e INSERT complementam este módulo com exemplos visuais.*

---

## Perguntas Frequentes (FAQ)

**P: Preciso sempre especificar as colunas no INSERT?**
R: Tecnicamente não — `INSERT INTO produtos VALUES (NULL, 'Arroz', ...)` funciona se você informar todos os valores na ordem. Mas é fortemente recomendado especificar as colunas: é mais legível, mais seguro e não quebra se a ordem das colunas mudar.

**P: O que acontece se eu inserir um registro e o programa travar antes do commit?**
R: O registro é perdido. Sem commit, as alterações existem apenas na memória. Por isso é importante fazer commit após cada operação ou grupo de operações relacionadas.

**P: Posso inserir dados em uma tabela que tem FOREIGN KEY sem que a tabela referenciada exista?**
R: Se PRAGMA foreign_keys está ON, não — o banco rejeita. Se está OFF (padrão do SQLite), sim — mas os dados ficam inconsistentes. Sempre ative foreign_keys.

**P: AUTOINCREMENT é obrigatório para chaves primárias?**
R: Não. Sem AUTOINCREMENT, o SQLite ainda gera IDs automaticamente para colunas INTEGER PRIMARY KEY, mas pode reutilizar IDs de registros deletados. Com AUTOINCREMENT, IDs nunca são reutilizados. Para a maioria dos casos, a diferença não importa.

**P: Posso ter mais de uma coluna UNIQUE na mesma tabela?**
R: Sim. Cada coluna UNIQUE é verificada independentemente. Exemplo: email UNIQUE e cpf UNIQUE — ambos devem ser únicos, mas são verificados separadamente.

**P: Como faço para inserir a data e hora atual?**
R: Use as funções do SQLite: `date('now')` para data, `time('now')` para hora, `datetime('now')` para data e hora. Podem ser usadas como DEFAULT ou em INSERT.

**P: O que é PRAGMA no SQLite?**
R: PRAGMA são comandos especiais do SQLite para configurar comportamentos do banco. `PRAGMA foreign_keys = ON` ativa verificação de chaves estrangeiras. `PRAGMA table_info(tabela)` mostra informações sobre colunas. São específicos do SQLite — não existem em outros bancos.

**P: Posso desfazer um DROP TABLE?**
R: Não. DROP TABLE é permanente e irreversível. Sempre faça backup antes de executar DROP TABLE em um banco com dados importantes.

**P: Qual a diferença entre TEXT e VARCHAR no SQLite?**
R: No SQLite, não há diferença prática. O SQLite aceita VARCHAR(100) na definição, mas internamente trata como TEXT sem limite de tamanho. Em outros bancos como PostgreSQL e MySQL, VARCHAR(100) limita o texto a 100 caracteres. No SQLite, use TEXT — é mais simples e honesto.

**P: Como sei quais tabelas existem no meu banco?**
R: No shell SQLite, use `.tables`. Em Python, execute `SELECT name FROM sqlite_master WHERE type='table'`. Ambos listam todas as tabelas do banco.


---

## Exercícios Práticos

### Exercício 1: Criando Tabelas de uma Escola

Crie um banco `escola.db` com as tabelas: `professores` (id, nome, email UNIQUE, disciplina), `turmas` (id, nome, professor_id FK, horario), `alunos` (id, nome, email UNIQUE, data_nascimento). Use constraints apropriadas.

### Exercício 2: Populando com Dados

Usando o banco `escola.db`, insira: 3 professores, 4 turmas (cada uma com um professor) e 10 alunos. Use `executemany()` para inserções em lote.

### Exercício 3: Testando Constraints

Escreva um programa que tenta violar cada constraint do banco `escola.db` e capture os erros com try/except. Teste: NOT NULL, UNIQUE, FOREIGN KEY e CHECK (se tiver).

---

[← Anterior: SQLite e Ambiente](cap08-mod04-sqlite-ambiente-conteudo.md) · [Próximo: SELECT e Consultas →](cap08-mod06-sql-select-conteudo.md)
