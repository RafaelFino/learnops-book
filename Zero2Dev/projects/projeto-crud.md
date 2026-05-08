```python
    print(f"\n{'ID':<4} {'Produto':<25} {'Categoria':<12} {'Preco':>9} {'Estoque':>8}")
        print("-" * 62)
        for row in rows:
            print(f"{row['id']:<4} {row['nome']:<25} {row['categoria']:<12} R$ {row['preco']:>6.2f} {row['estoque']:>6}")
        print(f"\nTotal: {len(rows)} produtos")

def search_products(search_term):
    """Busca produtos por nome (busca parcial)"""
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT p.id, p.nome, p.preco, p.estoque, c.nome AS categoria
            FROM produtos p
            JOIN categorias c ON p.categoria_id = c.id
            WHERE p.ativo = 1 AND p.nome LIKE ?
            ORDER BY p.nome
        """, (f"%{search_term}%",))
        rows = cursor.fetchall()

        if not rows:
            print(f"\nNenhum produto encontrado com '{search_term}'.")
            return

        print(f"\nResultados para '{search_term}':")
        print(f"{'ID':<4} {'Produto':<25} {'Categoria':<12} {'Preco':>9}")
        print("-" * 54)
        for row in rows:
            print(f"{row['id']:<4} {row['nome']:<25} {row['categoria']:<12} R$ {row['preco']:>6.2f}")

def list_categories():
    """Lista todas as categorias com contagem de produtos"""
    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT c.id, c.nome, c.descrição,
                   COUNT(p.id) AS total_produtos
            FROM categorias c
            LEFT JOIN produtos p ON c.id = p.categoria_id AND p.ativo = 1
            GROUP BY c.id
            ORDER BY c.nome
        """)
        rows = cursor.fetchall()

        print(f"\n{'ID':<4} {'Categoria':<15} {'Produtos':>9} {'Descrição'}")
        print("-" * 60)
        for row in rows:
            desc = row['descrição'] or ""
            print(f"{row['id']:<4} {row['nome']:<15} {row['total_produtos']:>7}   {desc}")
```

**Checkpoint da Fase 2**: teste `list_products()` (deve mostrar "Nenhum produto cadastrado"), `list_categories()` (deve mostrar as 5 categorias padrão) e `search_products("arroz")` (nenhum resultado).

---

### Fase 3: Funções de Escrita (INSERT, UPDATE, DELETE)

Implemente as funções que modificam dados:

```python
def add_product():
    """Cadastra um novo produto"""
    print("\n=== CADASTRAR PRODUTO ===")

    # Mostrar categorias disponiveis
    list_categories()

    # Coletar dados do usuario
    name = input("\nNome do produto: ").strip()
    if not name:
        print("Nome não pode ser vazio.")
        return

    description = input("Descrição (opcional, Enter para pular): ").strip() or None

    # Validar preco
    try:
        price = float(input("Preco (R$): ").strip())
        if price <= 0:
            print("Preco deve ser maior que zero.")
            return
    except ValueError:
        print("Preco inválido. Use números (ex: 12.90).")
        return

    # Validar estoque
    try:
        stock = int(input("Estoque inicial: ").strip())
        if stock < 0:
            print("Estoque não pode ser negativo.")
            return
    except ValueError:
        print("Estoque inválido. Use números inteiros.")
        return

    # Validar categoria
    try:
        category_id = int(input("ID da categoria: ").strip())
    except ValueError:
        print("ID de categoria inválido.")
        return

    # Inserir no banco
    try:
        with get_connection() as conn:
            conn.execute(
                """INSERT INTO produtos (nome, descrição, preco, estoque, categoria_id)
                   VALUES (?, ?, ?, ?, ?)""",
                (name, description, price, stock, category_id)
            )
        print(f"\nProduto '{name}' cadastrado com sucesso!")
    except sqlite3.IntegrityError as e:
        if "FOREIGN KEY" in str(e):
            print(f"Categoria {category_id} não existe. Use uma categoria válida.")
        else:
            print(f"Erro ao cadastrar: {e}")

def update_price():
    """Atualiza o preco de um produto"""
    print("\n=== ATUALIZAR PRECO ===")

    # Mostrar produtos para o usuario escolher
    list_products()

    try:
        product_id = int(input("\nID do produto: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    # Verificar se o produto existe
    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT id, nome, preco FROM produtos WHERE id = ? AND ativo = 1",
            (product_id,)
        )
        product = cursor.fetchone()

        if not product:
            print(f"Produto {product_id} não encontrado.")
            return

        print(f"\nProduto: {product['nome']}")
        print(f"Preco atual: R$ {product['preco']:.2f}")

        try:
            new_price = float(input("Novo preco (R$): ").strip())
            if new_price <= 0:
                print("Preco deve ser maior que zero.")
                return
        except ValueError:
            print("Preco inválido.")
            return

        conn.execute(
            "UPDATE produtos SET preco = ? WHERE id = ?",
            (new_price, product_id)
        )
        print(f"Preco atualizado: R$ {product['preco']:.2f} -> R$ {new_price:.2f}")

def remove_product():
    """Remove um produto (soft delete — marca como inativo)"""
    print("\n=== REMOVER PRODUTO ===")

    list_products()

    try:
        product_id = int(input("\nID do produto para remover: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    with get_connection() as conn:
        cursor = conn.execute(
            "SELECT id, nome, preco FROM produtos WHERE id = ? AND ativo = 1",
            (product_id,)
        )
        product = cursor.fetchone()

        if not product:
            print(f"Produto {product_id} não encontrado.")
            return

        print(f"\nVoce quer remover: {product['nome']} (R$ {product['preco']:.2f})?")
        confirm = input("Confirmar? (s/n): ").strip().lower()

        if confirm == "s":
            # Soft delete: marca como inativo em vez de deletar
            conn.execute(
                "UPDATE produtos SET ativo = 0 WHERE id = ?",
                (product_id,)
            )
            print(f"Produto '{product['nome']}' removido com sucesso.")
        else:
            print("Operação cancelada.")
```

**Checkpoint da Fase 3**: cadastre 5 produtos, liste-os, atualize o preço de um, remova outro. Feche o programa, abra novamente e verifique que os dados persistiram.

---

### Fase 4: Relatório e Menu Principal

Implemente o relatório e o menu:

```python
def show_report():
    """Mostra relatório resumido"""
    with get_connection() as conn:
        # Total de produtos ativos
        total = conn.execute(
            "SELECT COUNT(*) FROM produtos WHERE ativo = 1"
        ).fetchone()[0]

        # Valor total do estoque
        stock_value = conn.execute(
            "SELECT COALESCE(SUM(preco * estoque), 0) FROM produtos WHERE ativo = 1"
        ).fetchone()[0]

        # Produto mais caro
        expensive = conn.execute(
            "SELECT nome, preco FROM produtos WHERE ativo = 1 ORDER BY preco DESC LIMIT 1"
        ).fetchone()

        # Produto mais barato
        cheapest = conn.execute(
            "SELECT nome, preco FROM produtos WHERE ativo = 1 ORDER BY preco ASC LIMIT 1"
        ).fetchone()

        # Preco medio
        avg_price = conn.execute(
            "SELECT COALESCE(AVG(preco), 0) FROM produtos WHERE ativo = 1"
        ).fetchone()[0]

        # Produtos por categoria
        by_category = conn.execute("""
            SELECT c.nome, COUNT(p.id) AS total
            FROM categorias c
            LEFT JOIN produtos p ON c.id = p.categoria_id AND p.ativo = 1
            GROUP BY c.nome
            HAVING total > 0
            ORDER BY total DESC
        """).fetchall()

        print("\n" + "=" * 45)
        print("         RELATORIO RESUMIDO")
        print("=" * 45)
        print(f"  Total de produtos ativos: {total}")
        print(f"  Valor total do estoque:   R$ {stock_value:,.2f}")
        print(f"  Preco medio:              R$ {avg_price:.2f}")
        if expensive:
            print(f"  Mais caro:  {expensive['nome']} (R$ {expensive['preco']:.2f})")
        if cheapest:
            print(f"  Mais barato: {cheapest['nome']} (R$ {cheapest['preco']:.2f})")
        if by_category:
            print(f"\n  Produtos por categoria:")
            for row in by_category:
                print(f"    {row['nome']:<15} {row['total']} produtos")
        print("=" * 45)

def show_menu():
    """Mostra o menu principal"""
    print("\n============================================")
    print("   SISTEMA DE CADASTRO DE PRODUTOS")
    print("============================================")
    print("[1] Listar todos os produtos")
    print("[2] Buscar produto por nome")
    print("[3] Cadastrar novo produto")
    print("[4] Atualizar preco de produto")
    print("[5] Remover produto")
    print("[6] Listar categorias")
    print("[7] Relatório resumido")
    print("[0] Sair")
    print("============================================")
    return input("Escolha uma opcao: ").strip()

def main():
    """Loop principal do programa"""
    init_database()

    while True:
        option = show_menu()

        if option == "1":
            list_products()
        elif option == "2":
            term = input("\nDigite o nome para buscar: ").strip()
            if term:
                search_products(term)
            else:
                print("Digite algo para buscar.")
        elif option == "3":
            add_product()
        elif option == "4":
            update_price()
        elif option == "5":
            remove_product()
        elif option == "6":
            list_categories()
        elif option == "7":
            show_report()
        elif option == "0":
            print("\nAte logo! Seus dados estao salvos no banco.")
            break
        else:
            print("Opcao inválida. Tente novamente.")

if __name__ == "__main__":
    main()
```

**Checkpoint da Fase 4**: teste o programa completo. Cadastre produtos, busque, atualize preços, remova, veja o relatório. Feche e reabra — tudo deve persistir.

---

### Fase 5: Melhorias e Polimento

Adicione estas melhorias ao programa:

a) **Atualizar estoque**: adicione opção [8] para atualizar a quantidade em estoque de um produto.

b) **Dados iniciais**: se o banco estiver vazio (nenhum produto), insira 5-10 produtos de exemplo automaticamente para que o programa não comece vazio.

c) **Validação de categoria**: na função `add_product()`, verifique se a categoria existe antes de tentar inserir (em vez de depender do erro de FK).

d) **Formatação de moeda**: garanta que todos os preços são exibidos com 2 casas decimais e o prefixo "R$".

e) **Contagem no menu**: mostre a contagem de produtos no cabeçalho do menu: "SISTEMA DE CADASTRO DE PRODUTOS (12 produtos)".

---

## Critérios de Conclusão

Seu projeto está pronto quando:

- [ ] O banco é criado automaticamente na primeira execução
- [ ] Categorias padrão são inseridas automaticamente
- [ ] Todas as 7 opções do menu funcionam corretamente
- [ ] Dados persistem entre execuções (fechar e reabrir mantém os dados)
- [ ] Busca por nome funciona com busca parcial (LIKE)
- [ ] Remoção usa soft delete (marca como inativo, não apaga)
- [ ] Preços são validados (não aceita zero ou negativo)
- [ ] Erros são tratados com mensagens claras (não mostra traceback)
- [ ] Parâmetros seguros (?) são usados em todas as queries
- [ ] O relatório mostra estatísticas corretas

---

## Conexão com o Mundo Real

Este projeto é uma versão simplificada do que sistemas reais fazem. Quando você usa um aplicativo de delivery e vê o cardápio, por trás existe um CRUD parecido com o que você construiu — com tabelas de produtos, categorias, preços e estoque. A diferença é que sistemas reais têm mais tabelas, mais validações, interface gráfica e múltiplos usuários simultâneos. Mas a base é a mesma: SQL, tabelas relacionadas e operações CRUD.

No capítulo 9, você vai aprender Orientação a Objetos e vai poder organizar esse código de forma muito mais estruturada. No capítulo 11, vai transformar esse CRUD em uma API REST acessível pela web. Cada capítulo constrói sobre o anterior.

---

## Extensões Opcionais (Para Quem Quer Ir Além)

Se você terminou o projeto e quer praticar mais:

1. **Histórico de preços**: crie uma tabela `historico_precos` que registra toda mudança de preço (produto_id, preco_antigo, preco_novo, data_alteracao). Atualize a função `update_price()` para registrar no histórico.

2. **Exportar para CSV**: adicione opção para exportar todos os produtos para um arquivo CSV.

3. **Importar de CSV**: adicione opção para importar produtos de um arquivo CSV.

4. **Paginação**: se houver muitos produtos, mostre 10 por vez com opção de "próxima página".

5. **Múltiplos critérios de busca**: permita buscar por categoria, faixa de preço ou estoque baixo.

---

[← Voltar ao Capítulo 8](../capitulos/cap08-mod09-projeto-crud-conteudo.md)
