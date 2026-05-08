# 8.6 — Exercícios: SELECT e Consultas

[← Voltar ao conteúdo: SELECT e Consultas](cap08-mod06-sql-select-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem SELECT em profundidade: filtros com WHERE, ordenação, funções de agregação (COUNT, SUM, AVG, MIN, MAX), GROUP BY, HAVING, LIKE, JOINs e subqueries. Use o banco `lanchonete.db` dos módulos anteriores.

---

## Como Executar

```bash
# No shell SQLite (recomendado para queries rapidas)
sqlite3 lanchonete.db
sqlite> .headers on
sqlite> .mode column

# Em Python (para exercicios com codigo)
cd ~/meus-projetos/curso/cap08/exercicios
python3 nome_exercicio.py
```

Se você não tem o banco `lanchonete.db`, crie-o executando os scripts do módulo 8.5.

---

## Exercício 1: Consultas Básicas com WHERE

Escreva queries SQL para cada item. Execute no shell SQLite e anote o resultado:

a) Listar todos os produtos disponíveis (disponível = 1) com preço menor que R$ 15.

b) Listar todos os produtos cujo nome contém a palavra "Burguer" (use LIKE).

c) Listar todos os clientes cadastrados em 2024 (data_cadastro começa com '2024').

d) Listar produtos com preço entre R$ 5 e R$ 20 (use BETWEEN).

e) Listar produtos que NÃO são da categoria 1 (use != ou NOT).

f) Listar os 3 produtos mais caros (use ORDER BY e LIMIT).

g) Listar produtos ordenados por categoria e, dentro de cada categoria, por preço decrescente.

h) Contar quantos produtos estão indisponíveis.

---

## Exercício 2: Funções de Agregação

Escreva queries usando funções de agregação:

a) Quantos produtos existem no total?

b) Qual o preço médio dos produtos?

c) Qual o produto mais caro e o mais barato? (mostre nome e preço)

d) Qual o valor total se comprássemos 1 unidade de cada produto disponível?

e) Quantos clientes estão cadastrados?

f) Qual a data do pedido mais antigo e do mais recente?

g) Qual o valor médio dos pedidos?

h) Quantos pedidos têm valor total acima de R$ 30?

---

## Exercício 3: GROUP BY e HAVING

Escreva queries com agrupamento:

a) Quantos produtos existem em cada categoria? (mostre o nome da categoria, não o id)

b) Qual o preço médio dos produtos por categoria?

c) Quais categorias têm mais de 3 produtos?

d) Quantos pedidos cada cliente fez? (mostre nome do cliente e quantidade)

e) Qual o valor total gasto por cada cliente?

f) Quais clientes gastaram mais de R$ 50 no total?

g) Quantos itens cada pedido tem? (conte os itens_pedido por pedido_id)

h) Qual o produto mais vendido? (conte quantas vezes aparece em itens_pedido)

---

## Exercício 4: JOINs

Escreva queries usando JOIN:

a) Liste todos os produtos com o nome da categoria (INNER JOIN entre produtos e categorias).

b) Liste todos os pedidos com o nome do cliente (INNER JOIN entre pedidos e clientes).

c) Liste os itens do pedido #1 com: nome do produto, quantidade, preço unitário e subtotal (quantidade * preço unitário).

d) Liste todos os clientes e quantos pedidos cada um fez, incluindo clientes sem pedidos (LEFT JOIN).

e) Liste todas as categorias e quantos produtos cada uma tem, incluindo categorias sem produtos (LEFT JOIN).

f) Crie uma "nota fiscal" do pedido #1: nome do cliente, data, cada item com nome do produto, quantidade, preço unitário, subtotal, e o valor total do pedido.

---

## Exercício 5: Relatório Completo em Python

Crie o arquivo `ex05_relatorio.py` que gera um relatório completo da lanchonete:

```python
# ex05_relatorio.py
# Gera relatorio completo da lanchonete
# "report" = relatorio, "summary" = resumo
import sqlite3

DATABASE = "lanchonete.db"

def print_section(title):
    """Imprime cabecalho de secao"""
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")

def general_stats(conn):
    """Estatisticas gerais"""
    print_section("ESTATISTICAS GERAIS")
    # TODO: Total de produtos, categorias, clientes, pedidos
    pass

def products_by_category(conn):
    """Produtos agrupados por categoria"""
    print_section("PRODUTOS POR CATEGORIA")
    # TODO: Para cada categoria, listar produtos com preco
    # Use JOIN entre produtos e categorias
    pass

def top_products(conn):
    """Produtos mais vendidos"""
    print_section("TOP 5 PRODUTOS MAIS VENDIDOS")
    # TODO: Contar quantas vezes cada produto aparece em itens_pedido
    # Ordenar por quantidade vendida decrescente, LIMIT 5
    pass

def revenue_by_client(conn):
    """Faturamento por cliente"""
    print_section("FATURAMENTO POR CLIENTE")
    # TODO: Valor total gasto por cada cliente
    # Use JOIN entre pedidos e clientes, GROUP BY cliente
    pass

def monthly_revenue(conn):
    """Faturamento por mes"""
    print_section("FATURAMENTO MENSAL")
    # TODO: Valor total de pedidos agrupado por mes
    # Use strftime('%Y-%m', data_pedido) para agrupar
    pass

def low_stock_alert(conn):
    """Alerta de estoque baixo"""
    print_section("ALERTA: PRODUTOS INDISPONIVEIS")
    # TODO: Listar produtos com disponivel = 0
    pass

# Programa principal
with sqlite3.connect(DATABASE) as conn:
    conn.row_factory = sqlite3.Row
    general_stats(conn)
    products_by_category(conn)
    top_products(conn)
    revenue_by_client(conn)
    monthly_revenue(conn)
    low_stock_alert(conn)
    print(f"\n{'=' * 50}")
    print("  Relatorio gerado com sucesso!")
    print(f"{'=' * 50}")
```

Implemente todas as funções. O relatório deve ser legível e bem formatado.

---

## Exercício 6: Subqueries

Subqueries são queries dentro de queries. Escreva:

a) Liste os produtos com preço acima da média:

```sql
SELECT nome, preco
FROM produtos
WHERE preco > (SELECT AVG(preco) FROM produtos);
```

b) Liste os clientes que fizeram pelo menos 2 pedidos (use subquery com COUNT).

c) Liste os produtos que nunca foram vendidos (não aparecem em itens_pedido):

```sql
-- Dica: use NOT IN ou NOT EXISTS
SELECT nome FROM produtos
WHERE id NOT IN (SELECT DISTINCT produto_id FROM itens_pedido);
```

d) Para cada produto, mostre o preço e a diferença em relação à média:

```sql
SELECT nome, preco,
       preco - (SELECT AVG(preco) FROM produtos) AS diferenca_media
FROM produtos
ORDER BY diferenca_media DESC;
```

e) Liste o pedido com maior valor total (use subquery com MAX).

f) Liste os produtos da mesma categoria do produto mais caro.

---

## Exercício 7: Queries do Mundo Real

Imagine que você é o gerente da lanchonete e precisa de informações para tomar decisões. Escreva a query para cada pergunta:

a) "Quais produtos devo reabastecer?" (produtos disponíveis com poucas vendas — menos de 3 vezes vendidos)

b) "Qual horário do dia tem mais pedidos?" (agrupe por hora da data_pedido, se disponível)

c) "Qual é o ticket médio?" (valor médio por pedido)

d) "Quais clientes não compram há mais de 30 dias?" (último pedido há mais de 30 dias)

e) "Se eu aumentar todos os preços em 10%, qual seria o novo faturamento estimado?" (recalcule com preços ajustados)

f) "Quais combinações de produtos são mais comuns nos pedidos?" (produtos que aparecem juntos no mesmo pedido)

---

## Exercício 8: Desafio — Dashboard em Python

Crie o arquivo `ex08_dashboard.py` que mostra um dashboard interativo:

```python
# ex08_dashboard.py
# Dashboard interativo da lanchonete
# "dashboard" = painel de controle
import sqlite3

DATABASE = "lanchonete.db"

def show_menu():
    """Mostra menu do dashboard"""
    print("\n=== DASHBOARD DA LANCHONETE ===")
    print("[1] Resumo geral")
    print("[2] Produtos por categoria")
    print("[3] Top 5 mais vendidos")
    print("[4] Faturamento por cliente")
    print("[5] Buscar produto por nome")
    print("[6] Pedidos de um cliente")
    print("[7] Detalhes de um pedido")
    print("[0] Sair")
    return input("Opcao: ").strip()

# TODO: Implemente cada opcao do menu
# Opcao 5: pedir nome ao usuario e buscar com LIKE
# Opcao 6: pedir nome do cliente e mostrar todos os pedidos dele
# Opcao 7: pedir numero do pedido e mostrar todos os itens com subtotais

def main():
    """Loop principal do dashboard"""
    while True:
        option = show_menu()
        if option == "0":
            print("Ate logo!")
            break
        # TODO: Chamar a funcao correspondente a cada opcao

main()
```

Implemente todas as opções do menu. Este exercício é uma preparação direta para o projeto CRUD do módulo 8.9.

---

## Gabarito Comentado

### Exercício 1 — Consultas Básicas

```sql
-- a) Produtos disponiveis com preco < 15
SELECT * FROM produtos WHERE disponivel = 1 AND preco < 15;

-- b) Produtos com "Burguer" no nome
SELECT * FROM produtos WHERE nome LIKE '%Burguer%';

-- c) Clientes cadastrados em 2024
SELECT * FROM clientes WHERE data_cadastro LIKE '2024%';

-- d) Produtos com preco entre 5 e 20
SELECT * FROM produtos WHERE preco BETWEEN 5 AND 20;

-- e) Produtos que NAO sao da categoria 1
SELECT * FROM produtos WHERE categoria_id != 1;

-- f) 3 produtos mais caros
SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 3;

-- g) Ordenados por categoria e preco
SELECT * FROM produtos ORDER BY categoria_id, preco DESC;

-- h) Produtos indisponiveis
SELECT COUNT(*) FROM produtos WHERE disponivel = 0;
```

### Exercício 3 — GROUP BY e HAVING

```sql
-- a) Produtos por categoria (com nome)
SELECT c.nome, COUNT(*) AS total
FROM produtos p
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nome;

-- b) Preco medio por categoria
SELECT c.nome, ROUND(AVG(p.preco), 2) AS preco_medio
FROM produtos p
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nome;

-- c) Categorias com mais de 3 produtos
SELECT c.nome, COUNT(*) AS total
FROM produtos p
JOIN categorias c ON p.categoria_id = c.id
GROUP BY c.nome
HAVING total > 3;

-- d) Pedidos por cliente
SELECT cl.nome, COUNT(*) AS total_pedidos
FROM pedidos p
JOIN clientes cl ON p.cliente_id = cl.id
GROUP BY cl.nome;

-- e) Valor total por cliente
SELECT cl.nome, SUM(p.valor_total) AS total_gasto
FROM pedidos p
JOIN clientes cl ON p.cliente_id = cl.id
GROUP BY cl.nome
ORDER BY total_gasto DESC;

-- h) Produto mais vendido
SELECT p.nome, SUM(ip.quantidade) AS total_vendido
FROM itens_pedido ip
JOIN produtos p ON ip.produto_id = p.id
GROUP BY p.nome
ORDER BY total_vendido DESC
LIMIT 1;
```

### Exercício 4 — JOINs

```sql
-- f) Nota fiscal do pedido #1
SELECT
    cl.nome AS cliente,
    ped.data_pedido,
    prod.nome AS produto,
    ip.quantidade,
    ip.preco_unitario,
    (ip.quantidade * ip.preco_unitario) AS subtotal
FROM itens_pedido ip
JOIN pedidos ped ON ip.pedido_id = ped.id
JOIN clientes cl ON ped.cliente_id = cl.id
JOIN produtos prod ON ip.produto_id = prod.id
WHERE ped.id = 1;
```

---

[← Voltar ao conteúdo: SELECT e Consultas](cap08-mod06-sql-select-conteudo.md)
