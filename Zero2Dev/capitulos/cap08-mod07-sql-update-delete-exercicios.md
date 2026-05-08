# 8.7 — Exercícios: UPDATE e DELETE

[← Voltar ao conteúdo: UPDATE e DELETE](cap08-mod07-sql-update-delete-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem UPDATE, DELETE, transações, ROLLBACK e boas práticas de segurança ao modificar dados. UPDATE e DELETE são operações destrutivas — sempre teste com SELECT antes.

**Regra de ouro**: antes de qualquer UPDATE ou DELETE, execute um SELECT com a mesma condição WHERE para verificar quais registros serão afetados.

---

## Como Executar

```bash
cd ~/meus-projetos/curso/cap08/exercicios

# IMPORTANTE: faca backup do banco antes de exercicios destrutivos
cp lanchonete.db lanchonete_backup.db

# Shell SQLite
sqlite3 lanchonete.db

# Python
python3 nome_exercicio.py
```

---

## Exercício 1: UPDATE Básico

Usando o banco `lanchonete.db`, execute cada operação. Para cada uma, primeiro execute o SELECT correspondente para verificar quais registros serão afetados:

a) Atualize o preço do "X-Burguer" para R$ 21.90.

```sql
-- Primeiro: verificar
SELECT id, nome, preco FROM produtos WHERE nome = 'X-Burguer';

-- Depois: atualizar
UPDATE produtos SET preco = 21.90 WHERE nome = 'X-Burguer';

-- Confirmar: verificar de novo
SELECT id, nome, preco FROM produtos WHERE nome = 'X-Burguer';
```

b) Aumente em 10% o preço de todos os produtos da categoria "Bebidas" (categoria_id = 2).

c) Marque todos os produtos com preço acima de R$ 25 como indisponíveis (disponível = 0).

d) Atualize o email do cliente "Joao Silva" para "joao.silva@novoemail.com".

e) Atualize o status de todos os pedidos com status "pendente" para "preparando".

f) **CUIDADO**: o que acontece se você executar `UPDATE produtos SET preco = 0;` sem WHERE? Teste em uma cópia do banco.

---

## Exercício 2: DELETE com Segurança

Execute cada operação com a verificação prévia:

a) Remova o produto com id = 99 (que provavelmente não existe). O que acontece?

b) Remova todos os produtos indisponíveis (disponível = 0). Primeiro conte quantos são.

c) Tente remover uma categoria que tem produtos associados. O que acontece com PRAGMA foreign_keys = ON?

d) Remova todos os itens do pedido #1. Depois remova o pedido #1. A ordem importa? Por quê?

e) **CUIDADO**: o que acontece se você executar `DELETE FROM produtos;` sem WHERE? Teste em uma cópia do banco.

---

## Exercício 3: Transações em Python

Crie o arquivo `ex03_transacoes.py` que demonstra transações:

```python
# ex03_transacoes.py
# Demonstra transacoes com commit e rollback
# "transaction" = transacao, "rollback" = reverter
import sqlite3

DATABASE = "lanchonete.db"

def create_order_with_transaction(conn, client_id, items):
    """
    Cria um pedido completo usando transacao.
    Se qualquer parte falhar, tudo e revertido.

    items = [(produto_id, quantidade), ...]
    """
    try:
        cursor = conn.cursor()

        # 1. Verificar se o cliente existe
        cursor.execute("SELECT id, nome FROM clientes WHERE id = ?", (client_id,))
        client = cursor.fetchone()
        if not client:
            raise ValueError(f"Cliente {client_id} nao encontrado")
        print(f"Cliente: {client[1]}")

        # 2. Criar o pedido (valor_total sera atualizado depois)
        cursor.execute(
            "INSERT INTO pedidos (cliente_id, data_pedido, valor_total, status) VALUES (?, date('now'), 0, 'pendente')",
            (client_id,)
        )
        order_id = cursor.lastrowid
        print(f"Pedido #{order_id} criado")

        # 3. Adicionar cada item
        total = 0
        for product_id, quantity in items:
            # Buscar preco do produto
            cursor.execute(
                "SELECT id, nome, preco, disponivel FROM produtos WHERE id = ?",
                (product_id,)
            )
            product = cursor.fetchone()
            if not product:
                raise ValueError(f"Produto {product_id} nao encontrado")
            if not product[3]:  # disponivel = 0
                raise ValueError(f"Produto '{product[1]}' indisponivel")

            # Inserir item do pedido
            price = product[2]
            cursor.execute(
                "INSERT INTO itens_pedido (pedido_id, produto_id, quantidade, preco_unitario) VALUES (?, ?, ?, ?)",
                (order_id, product_id, quantity, price)
            )
            subtotal = price * quantity
            total += subtotal
            print(f"  + {product[1]} x{quantity} = R$ {subtotal:.2f}")

        # 4. Atualizar valor total do pedido
        cursor.execute(
            "UPDATE pedidos SET valor_total = ? WHERE id = ?",
            (total, order_id)
        )

        # 5. Confirmar tudo
        conn.commit()
        print(f"Pedido #{order_id} confirmado! Total: R$ {total:.2f}")
        return order_id

    except (ValueError, sqlite3.Error) as e:
        # Se qualquer coisa falhar, desfaz tudo
        conn.rollback()
        print(f"ERRO: {e}")
        print("Transacao revertida — nenhuma alteracao foi salva.")
        return None

# Teste 1: Pedido valido
print("=== Teste 1: Pedido valido ===")
with sqlite3.connect(DATABASE) as conn:
    conn.execute("PRAGMA foreign_keys = ON")
    create_order_with_transaction(conn, 1, [(1, 2), (3, 1)])

# Teste 2: Pedido com produto inexistente (deve falhar e reverter)
print("\n=== Teste 2: Produto inexistente ===")
with sqlite3.connect(DATABASE) as conn:
    conn.execute("PRAGMA foreign_keys = ON")
    create_order_with_transaction(conn, 1, [(1, 1), (999, 2)])

# TODO: Adicione mais testes:
# Teste 3: Pedido com cliente inexistente
# Teste 4: Pedido com produto indisponivel
# Teste 5: Pedido valido com 5 itens diferentes
```

Execute e verifique que:
- No teste 1, o pedido é criado com sucesso
- No teste 2, nenhum dado é salvo (nem o pedido parcial, nem o primeiro item)

---

## Exercício 4: UPDATE com Subquery

Escreva queries UPDATE que usam subqueries:

a) Aumente em 15% o preço de todos os produtos da categoria "Lanches" (use subquery para encontrar o id da categoria pelo nome):

```sql
UPDATE produtos
SET preco = preco * 1.15
WHERE categoria_id = (SELECT id FROM categorias WHERE nome = 'Lanches');
```

b) Marque como indisponíveis todos os produtos que nunca foram vendidos (não aparecem em itens_pedido).

c) Atualize o valor_total de todos os pedidos recalculando a partir dos itens (soma de quantidade * preco_unitario).

d) Atualize o status para "entregue" de todos os pedidos com mais de 7 dias.

---

## Exercício 5: CRUD Completo com Menu

Crie o arquivo `ex05_crud_menu.py` com um menu interativo completo:

```python
# ex05_crud_menu.py
# CRUD completo de produtos com menu interativo
# "crud" = Create, Read, Update, Delete
import sqlite3

DATABASE = "lanchonete.db"

def show_menu():
    """Mostra o menu principal"""
    print("\n=== GERENCIADOR DE PRODUTOS ===")
    print("[1] Listar todos os produtos")
    print("[2] Buscar produto por nome")
    print("[3] Adicionar novo produto")
    print("[4] Atualizar preco de produto")
    print("[5] Remover produto")
    print("[6] Alternar disponibilidade")
    print("[0] Sair")
    return input("Opcao: ").strip()

def list_products(conn):
    """Lista todos os produtos com categoria"""
    cursor = conn.execute("""
        SELECT p.id, p.nome, c.nome, p.preco, p.disponivel
        FROM produtos p
        JOIN categorias c ON p.categoria_id = c.id
        ORDER BY c.nome, p.nome
    """)
    rows = cursor.fetchall()
    print(f"\n{'ID':<4} {'Produto':<25} {'Categoria':<15} {'Preco':>8} {'Status':<12}")
    print("-" * 68)
    for row in rows:
        status = "Disponivel" if row[4] else "Indisponivel"
        print(f"{row[0]:<4} {row[1]:<25} {row[2]:<15} R$ {row[3]:>6.2f} {status}")
    print(f"\nTotal: {len(rows)} produtos")

# TODO: Implemente as funcoes restantes:
# search_product(conn) — busca por nome com LIKE
# add_product(conn) — pede dados ao usuario e insere
# update_price(conn) — pede id e novo preco, atualiza
# remove_product(conn) — pede id, mostra dados, pede confirmacao, remove
# toggle_availability(conn) — alterna disponivel entre 0 e 1

def main():
    """Loop principal"""
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        while True:
            option = show_menu()
            if option == "0":
                print("Ate logo!")
                break
            elif option == "1":
                list_products(conn)
            # TODO: Adicionar as outras opcoes

main()
```

Requisitos:
- Usar parâmetros seguros (?) em todas as queries
- Validar entrada do usuário (preço deve ser número positivo, id deve existir)
- Pedir confirmação antes de remover
- Mostrar mensagens claras de sucesso e erro
- Tratar exceções com try/except

---

## Exercício 6: Backup e Restauração

Crie o arquivo `ex06_backup.py` que implementa backup e restauração do banco:

```python
# ex06_backup.py
# Backup e restauracao do banco SQLite
# "backup" = copia de seguranca, "restore" = restaurar
import sqlite3
import shutil  # "shutil" = shell utilities (utilitarios de shell)
import os
from datetime import datetime

DATABASE = "lanchonete.db"
BACKUP_DIR = "backups"

def create_backup():
    """Cria backup do banco com timestamp no nome"""
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{BACKUP_DIR}/lanchonete_{timestamp}.db"
    shutil.copy2(DATABASE, backup_name)
    print(f"Backup criado: {backup_name}")
    return backup_name

def list_backups():
    """Lista todos os backups disponiveis"""
    if not os.path.exists(BACKUP_DIR):
        print("Nenhum backup encontrado.")
        return []
    # "backups" = copias de seguranca
    backups = sorted(os.listdir(BACKUP_DIR))
    if not backups:
        print("Nenhum backup encontrado.")
        return []
    print("\nBackups disponiveis:")
    for i, name in enumerate(backups, 1):
        # Mostrar tamanho do arquivo
        size = os.path.getsize(f"{BACKUP_DIR}/{name}")
        print(f"  {i}. {name} ({size} bytes)")
    return backups

def restore_backup(backup_name):
    """Restaura banco a partir de um backup"""
    backup_path = f"{BACKUP_DIR}/{backup_name}"
    if not os.path.exists(backup_path):
        print(f"Backup nao encontrado: {backup_path}")
        return False
    # Criar backup do estado atual antes de restaurar
    create_backup()
    shutil.copy2(backup_path, DATABASE)
    print(f"Banco restaurado a partir de: {backup_name}")
    return True

# TODO: Crie um menu interativo que permita:
# [1] Criar backup
# [2] Listar backups
# [3] Restaurar backup (escolher da lista)
# [4] Mostrar estado atual do banco (contagem de registros)
# [0] Sair
```

---

## Exercício 7: Operações em Lote

Crie o arquivo `ex07_lote.py` que demonstra a diferença de performance entre operações individuais e em lote:

```python
# ex07_lote.py
# Compara performance de operacoes individuais vs lote
# "batch" = lote, "performance" = desempenho
import sqlite3
import time
import random

DATABASE = ":memory:"  # banco em memoria para teste

def setup(conn):
    """Cria tabela de teste"""
    conn.execute("""
        CREATE TABLE produtos_teste (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL
        )
    """)

def insert_one_by_one(conn, count):
    """Insere registros um por um (lento)"""
    # "start" = inicio
    start = time.time()
    for i in range(count):
        conn.execute(
            "INSERT INTO produtos_teste (nome, preco) VALUES (?, ?)",
            (f"Produto {i}", round(random.uniform(1, 100), 2))
        )
        conn.commit()  # commit a cada insercao
    elapsed = time.time() - start
    print(f"  Um por um ({count} registros): {elapsed:.3f} segundos")

def insert_batch(conn, count):
    """Insere registros em lote (rapido)"""
    start = time.time()
    data = [
        (f"Produto {i}", round(random.uniform(1, 100), 2))
        for i in range(count)
    ]
    conn.executemany(
        "INSERT INTO produtos_teste (nome, preco) VALUES (?, ?)",
        data
    )
    conn.commit()  # commit unico no final
    elapsed = time.time() - start
    print(f"  Em lote ({count} registros): {elapsed:.3f} segundos")

def insert_transaction(conn, count):
    """Insere registros em transacao unica (rapido)"""
    start = time.time()
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION")
    for i in range(count):
        cursor.execute(
            "INSERT INTO produtos_teste (nome, preco) VALUES (?, ?)",
            (f"Produto {i}", round(random.uniform(1, 100), 2))
        )
    cursor.execute("COMMIT")
    elapsed = time.time() - start
    print(f"  Transacao unica ({count} registros): {elapsed:.3f} segundos")

# Testar com diferentes quantidades
for count in [100, 1000, 5000]:
    print(f"\n=== {count} registros ===")

    conn1 = sqlite3.connect(DATABASE)
    setup(conn1)
    insert_one_by_one(conn1, count)
    conn1.close()

    conn2 = sqlite3.connect(DATABASE)
    setup(conn2)
    insert_batch(conn2, count)
    conn2.close()

    conn3 = sqlite3.connect(DATABASE)
    setup(conn3)
    insert_transaction(conn3, count)
    conn3.close()
```

Execute e responda:
a) Qual método é mais rápido? Por quê?
b) Qual a diferença entre `executemany` e transação explícita?
c) Por que commit a cada inserção é tão lento?

---

## Exercício 8: Desafio — Sistema de Pedidos Completo

Crie o arquivo `ex08_pedidos.py` que implementa um sistema completo de pedidos:

```
=== SISTEMA DE PEDIDOS ===
[1] Novo pedido
[2] Listar pedidos
[3] Detalhes de um pedido
[4] Cancelar pedido
[5] Atualizar status
[6] Relatorio do dia
[0] Sair
```

Requisitos:
- "Novo pedido": selecionar cliente, adicionar produtos um a um (com quantidade), calcular total, confirmar — tudo em uma transação
- "Cancelar pedido": remover itens e pedido em uma transação (só se status for "pendente")
- "Atualizar status": permitir transição pendente → preparando → pronto → entregue (não permitir pular etapas nem voltar)
- "Relatório do dia": total de pedidos, faturamento, produto mais vendido, ticket médio
- Usar transações para todas as operações de escrita
- Tratar todos os erros possíveis

---

## Gabarito Comentado

### Exercício 1 — UPDATE Básico

f) `UPDATE produtos SET preco = 0;` sem WHERE atualiza TODOS os produtos para preço 0. Todos os preços são perdidos. Isso é irreversível sem backup. Por isso a regra: SEMPRE use WHERE em UPDATE e DELETE.

### Exercício 2 — DELETE com Segurança

c) Com `PRAGMA foreign_keys = ON`, o banco rejeita a remoção da categoria porque existem produtos que referenciam ela (integridade referencial). Sem o PRAGMA, a remoção acontece e os produtos ficam "órfãos" — com categoria_id apontando para um registro que não existe mais.

d) A ordem importa. Primeiro remova os itens do pedido, depois o pedido. Se tentar remover o pedido primeiro com foreign_keys ON, o banco rejeita porque existem itens referenciando o pedido.

### Exercício 7 — Operações em Lote

a) `executemany` e transação explícita são muito mais rápidos (10-100x). A diferença é dramática com volumes maiores.

b) Na prática, são similares em performance. `executemany` é mais limpo sintaticamente. Transação explícita dá mais controle (pode fazer rollback parcial).

c) Cada commit força uma escrita no disco (fsync). Com 1000 inserções e commit individual, são 1000 escritas no disco. Com commit único no final, é 1 escrita. Disco é ordens de magnitude mais lento que memória.

---

[← Voltar ao conteúdo: UPDATE e DELETE](cap08-mod07-sql-update-delete-conteudo.md)
