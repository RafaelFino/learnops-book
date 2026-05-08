# 9.9 — Exercícios: Design Pattern Repository

[← Voltar ao conteúdo: Repository](cap09-mod09-patterns-repository-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios praticam o Repository Pattern: abstração de acesso a dados, múltiplas implementações (memória e SQLite), uso com Factory e testabilidade.

---

## Exercício 1 — Repository de Contatos

Crie `IContactRepository` com: `Add(Contact)`, `GetById(int)`, `GetAll()`, `Update(Contact)`, `Delete(int)`, `SearchByName(string)`. Implemente `InMemoryContactRepository`. Crie um programa CRUD completo de contatos usando a interface.

---

## Exercício 2 — Duas Implementações

Para o exercício 1, crie uma segunda implementação: `FileContactRepository` que simula persistência em arquivo (pode usar Console.WriteLine para simular). Use Factory para alternar entre as duas implementações.

---

## Exercício 3 — Repository de Tarefas

Crie `ITaskRepository` para um sistema de tarefas (to-do). Implemente `InMemoryTaskRepository`. O sistema deve suportar: adicionar, listar todas, listar por status (pendente/concluída), marcar como concluída, remover. Compare com a versão procedural do módulo 9.1.

---

## Exercício 4 — Repository + Service

Crie uma camada de serviço `ProductService` que recebe `IProductRepository` no construtor. O serviço adiciona regras de negócio: validar nome não vazio, preço positivo, verificar duplicatas. O repository cuida apenas do armazenamento. Demonstre a separação de responsabilidades.

---

## Exercício 5 — Testabilidade

Crie `InMemoryProductRepository` e use-o para testar a lógica do `ProductService` do exercício 4. Demonstre que você pode verificar se os produtos foram salvos corretamente sem precisar de banco de dados.

---

## Exercício 6 — Repository Genérico

Crie uma interface genérica `IRepository<T>` com: `Add(T)`, `GetById(int)`, `GetAll()`, `Delete(int)`. Implemente `InMemoryRepository<T>`. Demonstre usando com `Product`, `Customer` e `Order`.

Dica: use `where T : class` para restringir o tipo genérico.

---

## Exercício 7 — Factory de Repositories

Crie uma `RepositoryFactory` que retorna `IProductRepository` baseado em configuração ("memory" ou "sqlite"). Demonstre que trocar de implementação requer apenas mudar a string de configuração.

---

## Exercício 8 — Análise do CRUD do Cap 8

Volte ao CRUD do capítulo 8 e análise:
1. Quantas funções acessam o banco diretamente?
2. Se quisesse trocar SQLite por PostgreSQL, quantas funções mudariam?
3. Como o Repository Pattern resolveria esses problemas?
4. Desenhe como ficaria a arquitetura com Repository.

---

## Exercício 9 — Comparação Antes e Depois

Escreva um parágrafo comparando o CRUD procedural do cap 8 com a versão usando Repository. O que mudou em termos de: organização, testabilidade, flexibilidade e manutenção?

---

## Exercício 10 — Sistema Completo

Crie um sistema de biblioteca simplificado com:
- `IBookRepository` com implementação em memória
- `BookService` com regras de negócio (não duplicar ISBN, validar dados)
- `BookFactory` para criar o repository
- Menu CLI para interação

Este exercício prepara o terreno para o projeto do módulo 9.11.


---

## Exercício 4 — Busca com Filtros — Nível: Intermediário

### Enunciado

Adicione ao `IProductRepository` um método `FindByPriceRange(double minPrice, double maxPrice)` que retorna todos os produtos dentro de uma faixa de preço. Implemente na versão InMemory.

### Dicas

1. O método deve retornar `List<Product>` — pode ser vazia se nenhum produto estiver na faixa
2. Use LINQ ou um loop com condição: `price >= minPrice && price <= maxPrice`
3. Considere o caso onde `minPrice > maxPrice` — o que fazer?

### Proposta de Teste

- **Caso básico:** Produtos com preços 50, 100, 150, 200. Buscar faixa 80-160 → retorna 100 e 150
- **Caso de borda:** Faixa 100-100 → retorna apenas produtos com preço exatamente 100
- **Caso vazio:** Faixa 500-600 sem produtos nessa faixa → retorna lista vazia

---

## Exercício 5 — Repository com Contagem e Estatísticas — Nível: Avançado

### Enunciado

Adicione ao `IProductRepository` os seguintes métodos:
- `Count()` — retorna o número total de produtos
- `GetTotalValue()` — retorna a soma de (preço x quantidade) de todos os produtos
- `GetMostExpensive()` — retorna o produto com maior preço

Implemente todos na versão InMemory.

### Dicas

1. `Count()` é simples — retorne o tamanho da lista
2. Para `GetTotalValue()`, percorra a lista somando `Price * Quantity`
3. Para `GetMostExpensive()`, percorra a lista mantendo referência ao maior
4. Considere o caso de lista vazia em todos os métodos

### Proposta de Teste

- **Caso básico:** 3 produtos com preços diferentes → `GetMostExpensive()` retorna o correto
- **Caso de borda:** Lista com 1 produto → todos os métodos funcionam
- **Caso vazio:** Lista vazia → `Count()` retorna 0, `GetTotalValue()` retorna 0, `GetMostExpensive()` retorna null

---

## Exercício 6 — Trocar Implementação sem Mudar o Service — Nível: Avançado

### Enunciado

Crie uma segunda implementação do `IProductRepository` chamada `FileProductRepository` que salva os produtos em um arquivo de texto (um produto por linha, campos separados por `;`). O `ProductService` deve funcionar sem nenhuma alteração — apenas troque a implementação injetada.

### Dicas

1. O formato do arquivo pode ser: `id;name;price;quantity` — uma linha por produto
2. `GetAll()` lê o arquivo e converte cada linha em um `Product`
3. `Create()` adiciona uma linha ao final do arquivo
4. `Delete()` reescreve o arquivo sem a linha do produto removido
5. O `ProductService` não deve saber se está usando InMemory ou File — ele só conhece a interface

### Proposta de Teste

- **Caso básico:** Criar 3 produtos, fechar o programa, reabrir — produtos devem estar lá
- **Caso de borda:** Arquivo não existe ainda → `GetAll()` retorna lista vazia (cria o arquivo)

Este exercício demonstra o poder real do Repository pattern: trocar a forma de armazenamento sem alterar a lógica de negócio.


### Dicas Gerais para os Exercícios

- Comece pelo exercício mais simples e avance gradualmente
- Teste cada parte do código separadamente antes de juntar tudo
- Use `print()` para verificar valores intermediários quando algo não funcionar
- Releia o enunciado se o resultado não for o esperado — às vezes o problema está na interpretação
- Não tenha medo de errar — cada erro é uma oportunidade de aprender como Python funciona

### Tabela de Referência Rápida

| Conceito | Exemplo | Resultado |
|----------|---------|-----------|
| Criar variável | `x = 10` | x vale 10 |
| Ler entrada | `nome = input("Nome: ")` | Espera digitação |
| Converter para inteiro | `int("42")` | 42 |
| Converter para decimal | `float("3.14")` | 3.14 |
| Converter para texto | `str(42)` | "42" |
| Formatar com f-string | `f"Valor: {x}"` | "Valor: 10" |
| Formatar decimais | `f"{x:.2f}"` | "10.00" |


### Exercício Extra: Repository com Múltiplas Implementações

Imagine que você tem a interface `IProductRepository` com os métodos:
- `Add(Product product)`
- `FindById(int id)`
- `FindAll()`
- `Delete(int id)`

Descreva como seriam duas implementações diferentes:

**1. InMemoryProductRepository** (para testes):
- Usa uma `List<Product>` interna
- `Add` adiciona à lista
- `FindById` percorre a lista com LINQ
- Dados somem quando o programa fecha

**2. SqliteProductRepository** (para produção):
- Usa conexão com banco SQLite
- `Add` executa `INSERT INTO`
- `FindById` executa `SELECT WHERE id = @id`
- Dados persistem no arquivo do banco

**Pergunta:** Qual é a vantagem de ter essas duas implementações?

**Resposta:** O código que usa o Repository (Service, Controller) não sabe qual implementação está rodando. Nos testes, usa InMemory (rápido, sem banco real). Em produção, usa SQLite (dados persistentes). Trocar é mudar uma linha na Factory ou na configuração.

### Checklist do Repository Pattern

| Critério | Correto | Incorreto |
|----------|---------|-----------|
| Interface define o contrato | `IProductRepository` | Classe concreta sem interface |
| Service depende da interface | `IProductRepository repo` | `SqliteRepository repo` |
| SQL fica no Repository | `SELECT * FROM products` no Repository | SQL no Service ou Controller |
| Lógica de negócio fora | Validações no Service | Validações no Repository |

---

[← Voltar ao conteúdo: Repository](cap09-mod09-patterns-repository-conteudo.md)
