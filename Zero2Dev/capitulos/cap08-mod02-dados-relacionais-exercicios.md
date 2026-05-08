# 8.2 — Exercícios: Dados Relacionais

[← Voltar ao conteúdo: Dados Relacionais](cap08-mod02-dados-relacionais-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem os conceitos do módulo 8.2: tabelas, linhas, colunas, chaves primárias, chaves estrangeiras, tipos de relacionamento (1:1, 1:N, N:M), normalização, NULL e diagramas ER. São exercícios conceituais — você vai desenhar, analisar e raciocinar sobre estruturas de dados relacionais.

---

## Exercício 1: Identificando Relacionamentos

Para cada par de entidades abaixo, identifique o tipo de relacionamento (1:1, 1:N ou N:M) e justifique sua resposta. Indique também onde ficaria a chave estrangeira.

a) País e Cidades
b) Médico e Pacientes
c) Filme e Atores
d) Pessoa e Passaporte
e) Produto e Fornecedores
f) Post de blog e Comentários
g) Aluno e Notas
h) Receita de cozinha e Ingredientes
i) Motorista de Uber e Corridas
j) Playlist do Spotify e Músicas

**Dica**: para cada par, pergunte: "um X pode ter muitos Y?" e "um Y pode pertencer a muitos X?". Se ambas as respostas forem sim, é N:M.

---

## Exercício 2: Chaves Primárias e Estrangeiras

Análise as tabelas abaixo e responda:

**Tabela: departamentos**

| id | nome | andar |
|----|------|-------|
| 1 | Vendas | 3 |
| 2 | TI | 5 |
| 3 | RH | 2 |

**Tabela: funcionarios**

| id | nome | email | departamento_id | salario |
|----|------|-------|-----------------|---------|
| 1 | Ana | ana@empresa.com | 2 | 8500.00 |
| 2 | Bruno | bruno@empresa.com | 1 | 6200.00 |
| 3 | Carla | carla@empresa.com | 2 | 9100.00 |
| 4 | Diego | diego@empresa.com | 1 | 5800.00 |
| 5 | Eva | eva@empresa.com | 3 | 7300.00 |

a) Qual é a chave primária de cada tabela?
b) Qual é a chave estrangeira e para onde ela aponta?
c) Qual é o tipo de relacionamento entre departamentos e funcionários?
d) Quantos funcionários trabalham no departamento de TI?
e) O que aconteceria se tentássemos inserir um funcionário com `departamento_id = 99`?
f) O que aconteceria se tentássemos remover o departamento "Vendas" (id = 1)?
g) Podemos ter dois funcionários com o mesmo email? Por que sim ou por que não?

---

## Exercício 3: Normalizando uma Tabela

A tabela abaixo está desnormalizada. Identifique TODOS os problemas e proponha uma versão normalizada com tabelas separadas.

**Tabela: pedidos_completos (NAO normalizada)**

| pedido_id | cliente_nome | cliente_email | cliente_telefone | produto_nome | produto_preco | quantidade | data | forma_pagamento |
|-----------|-------------|---------------|------------------|-------------|---------------|------------|------|-----------------|
| 1 | Ana Silva | ana@email.com | 11-9999-0001 | Arroz 5kg | 22.90 | 2 | 2024-03-01 | Cartao |
| 1 | Ana Silva | ana@email.com | 11-9999-0001 | Feijao 1kg | 8.49 | 1 | 2024-03-01 | Cartao |
| 2 | Bruno Costa | bruno@email.com | 11-9999-0002 | Cafe 250g | 12.90 | 3 | 2024-03-02 | Pix |
| 3 | Ana Silva | ana@email.com | 11-9999-0001 | Cafe 250g | 12.90 | 1 | 2024-03-03 | Dinheiro |
| 3 | Ana Silva | ana@email.com | 11-9999-0001 | Leite 1L | 5.99 | 2 | 2024-03-03 | Dinheiro |

a) Liste todos os dados que estão repetidos (redundância).
b) O que acontece se Ana mudar de telefone? Quantas linhas precisam ser atualizadas?
c) Podemos cadastrar um novo produto sem que ele esteja em um pedido?
d) Se removermos o pedido 2, perdemos alguma informação sobre o Bruno?
e) Proponha um modelo normalizado com tabelas separadas. Desenhe as tabelas com colunas, chaves primárias e estrangeiras.
f) Desenhe o diagrama ER em Mermaid do seu modelo normalizado.

---

## Exercício 4: Desenhando um Diagrama ER

Desenhe (no papel ou usando Mermaid) o diagrama ER para um sistema de pizzaria com as seguintes necessidades:

- Cadastrar pizzas com nome, descrição e tamanhos disponíveis (broto, média, grande) com preços diferentes por tamanho
- Cadastrar ingredientes com nome e tipo (queijo, carne, vegetal, molho)
- Saber quais ingredientes cada pizza leva
- Cadastrar clientes com nome, telefone e endereço de entrega
- Registrar pedidos com data, valor total, status (pendente, preparando, saiu para entrega, entregue) e forma de pagamento
- Saber quais pizzas cada pedido contém, com tamanho e quantidade

**Dica**: pense com cuidado na relação entre pizza e tamanho. Se cada tamanho tem preço diferente, "tamanho" não é apenas um atributo — pode ser uma entidade ou uma tabela de variações (como o SKU que vimos no módulo 8.3).

Entregue:
1. Lista de entidades identificadas
2. Atributos de cada entidade com tipos
3. Relacionamentos com cardinalidade (1:1, 1:N, N:M)
4. Diagrama ER em Mermaid
5. Exemplo de dados preenchidos (2-3 registros por tabela)

---

## Exercício 5: NULL — O Valor que Não Existe

Análise a tabela abaixo e responda:

**Tabela: clientes**

| id | nome | email | telefone | data_nascimento |
|----|------|-------|----------|-----------------|
| 1 | Ana | ana@email.com | 11-9999-0001 | 1990-05-15 |
| 2 | Bruno | bruno@email.com | NULL | 1985-11-20 |
| 3 | Carla | NULL | 11-9999-0003 | NULL |
| 4 | Diego | diego@email.com | 11-9999-0004 | 1992-08-10 |

a) Quais campos do Bruno são NULL? O que isso significa na prática?
b) Carla tem dois campos NULL. Isso é um problema? Quando faz sentido ter campos NULL?
c) Se fizermos a consulta "clientes com telefone = NULL", o resultado seria Bruno. Mas se fizermos "clientes com telefone = ''" (string vazia), o resultado seria diferente. Explique a diferença entre NULL e string vazia.
d) Se fizermos a consulta "clientes com data_nascimento > '1990-01-01'", Carla apareceria no resultado? Por quê?
e) Quais colunas desta tabela deveriam ser NOT NULL (obrigatórias)? Justifique cada decisão.

---

## Exercício 6: Tabelas Intermediárias (N:M)

Um sistema de cinema precisa gerenciar filmes e atores. Um filme tem muitos atores, e um ator participa de muitos filmes.

a) Crie as tabelas `filmes`, `atores` e a tabela intermediária `elenco` com todos os campos necessários.

b) Preencha as tabelas com os seguintes dados:
   - Filmes: "Matrix" (1999), "John Wick" (2014), "O Poderoso Chefao" (1972)
   - Atores: Keanu Reeves, Al Pacino, Laurence Fishburne
   - Elenco: Keanu Reeves em Matrix e John Wick, Al Pacino em O Poderoso Chefão, Laurence Fishburne em Matrix

c) A tabela intermediária `elenco` poderia ter campos adicionais além das chaves estrangeiras? Dê 3 exemplos de campos úteis e explique por que fariam sentido.

d) Se quisermos adicionar o campo "personagem" (qual personagem o ator interpreta no filme), onde ele ficaria? Na tabela de filmes, de atores ou de elenco? Justifique.

e) Desenhe o diagrama ER completo em Mermaid.

---

## Exercício 7: Comparando com Python

No capítulo 5, você usou listas de dicionários para representar dados. Compare as duas abordagens:

**Em Python (lista de dicionários):**

```python
# "categories" = categorias
categories = [
    {"id": 1, "name": "Alimentos"},
    {"id": 2, "name": "Bebidas"},
]

# "products" = produtos
products = [
    {"id": 1, "name": "Arroz", "category_id": 1, "price": 22.90},
    {"id": 2, "name": "Cafe", "category_id": 2, "price": 12.90},
    {"id": 3, "name": "Feijao", "category_id": 1, "price": 8.49},
]
```

**Em banco de dados (tabelas):**

| id | name | (tabela: categories) |
|----|------|-----|
| 1 | Alimentos | |
| 2 | Bebidas | |

| id | name | category_id | price | (tabela: products) |
|----|------|-------------|-------|-----|
| 1 | Arroz | 1 | 22.90 | |
| 2 | Cafe | 2 | 12.90 | |
| 3 | Feijao | 1 | 8.49 | |

a) Em Python, o que impede você de inserir um produto com `category_id: 99` (que não existe)? E no banco de dados?

b) Em Python, o que impede você de inserir dois produtos com o mesmo `id`? E no banco?

c) Em Python, o que impede você de inserir um produto sem `name` (campo obrigatório)? E no banco?

d) Se você quiser encontrar "todos os produtos da categoria Alimentos", como faria em Python (escreva o código) e como faria em SQL (escreva a query)?

e) Qual abordagem é mais segura para dados críticos (financeiros, médicos)? Por quê?

---

## Exercício 8: Modelagem Livre — Sistema de Sua Escolha

Escolha UM dos sistemas abaixo e faça a modelagem completa:

**Opção A**: Sistema de uma academia de ginástica
- Alunos, planos (mensal, trimestral, anual), matrículas, aulas (yoga, musculação, spinning), instrutores, agendamentos

**Opção B**: Sistema de uma locadora de veículos
- Veículos (carro, moto, van), categorias, clientes, reservas, locações, devoluções, multas

**Opção C**: Sistema de um hospital veterinário
- Animais, donos, veterinários, consultas, exames, medicamentos, internações

Para o sistema escolhido, entregue:

1. Lista de entidades com justificativa (por que cada uma é uma entidade e não um atributo)
2. Atributos de cada entidade com tipos de dados
3. Chaves primárias e estrangeiras
4. Tipos de relacionamento (1:1, 1:N, N:M) com justificativa
5. Tabelas intermediárias necessárias
6. Diagrama ER em Mermaid
7. Dados de exemplo (3-5 registros por tabela)
8. 3 perguntas que o sistema precisa responder e como o modelo permite respondê-las

---

## Gabarito Comentado

### Exercício 1 — Identificando Relacionamentos

a) **1:N** — Um país tem muitas cidades, mas cada cidade pertence a um país. FK: `pais_id` na tabela cidades.

b) **N:M** — Um médico atende muitos pacientes, e um paciente pode ser atendido por muitos médicos. Tabela intermediária: `consultas` com `medico_id` e `paciente_id`.

c) **N:M** — Um filme tem muitos atores, e um ator participa de muitos filmes. Tabela intermediária: `elenco`.

d) **1:1** — Cada pessoa tem um passaporte, e cada passaporte pertence a uma pessoa. FK: `pessoa_id` na tabela passaportes (ou `passaporte_id` na tabela pessoas).

e) **N:M** — Um produto pode ser vendido por muitos fornecedores, e um fornecedor vende muitos produtos. Tabela intermediária: `produtos_fornecedores`.

f) **1:N** — Um post tem muitos comentários, mas cada comentário pertence a um post. FK: `post_id` na tabela comentários.

g) **1:N** — Um aluno tem muitas notas (uma por disciplina/avaliação), mas cada nota pertence a um aluno. FK: `aluno_id` na tabela notas.

h) **N:M** — Uma receita usa muitos ingredientes, e um ingrediente aparece em muitas receitas. Tabela intermediária: `receitas_ingredientes` (com campo `quantidade`).

i) **1:N** — Um motorista faz muitas corridas, mas cada corrida tem um motorista. FK: `motorista_id` na tabela corridas. (Nota: se considerarmos que uma corrida pode ter motorista e passageiro, o passageiro também é 1:N.)

j) **N:M** — Uma playlist tem muitas músicas, e uma música pode estar em muitas playlists. Tabela intermediária: `playlist_musicas` (com campo `posição` para a ordem).

### Exercício 2 — Chaves Primárias e Estrangeiras

a) `id` em ambas as tabelas.
b) `departamento_id` na tabela funcionários, aponta para `id` na tabela departamentos.
c) 1:N — um departamento tem muitos funcionários.
d) 2 funcionários (Ana e Carla, ambas com departamento_id = 2).
e) O banco rejeitaria a inserção com erro de integridade referencial (violação de FK).
f) O banco rejeitaria a remoção porque existem funcionários (Bruno e Diego) referenciando esse departamento.
g) Depende se `email` tem constraint UNIQUE. Se tiver, não. Se não tiver, sim — mas seria um problema de modelagem.

### Exercício 5 — NULL

a) O campo `telefone` é NULL. Significa que Bruno não informou seu telefone — não sabemos qual é.
b) Não é necessariamente um problema. Faz sentido quando a informação é opcional (nem todo cliente quer informar email ou data de nascimento). O importante é que campos essenciais (como `nome` e `id`) não sejam NULL.
c) NULL significa "não sabemos o valor" — a informação não foi fornecida. String vazia ("") significa "o valor foi fornecido e é vazio" — o campo foi preenchido, mas sem conteúdo. São conceitos diferentes: NULL = ausência de informação, "" = informação presente mas vazia.
d) Não. Comparações com NULL resultam em NULL (nem verdadeiro nem falso). Carla seria excluída do resultado porque sua data_nascimento é NULL, e `NULL > '1990-01-01'` não é verdadeiro.
e) `id` (obrigatório — é a chave primária), `nome` (obrigatório — todo cliente precisa de nome). `email` e `telefone` podem ser NULL (opcionais). `data_nascimento` pode ser NULL (opcional, mas útil para marketing).

---

[← Voltar ao conteúdo: Dados Relacionais](cap08-mod02-dados-relacionais-conteudo.md)
