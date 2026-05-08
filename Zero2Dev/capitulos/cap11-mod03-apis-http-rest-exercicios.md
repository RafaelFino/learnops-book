# 11.3 — Exercícios: APIs HTTP e REST

[← Voltar ao conteúdo](cap11-mod03-apis-http-rest-conteudo.md)

---

## Sobre estes Exercícios

Estes exercícios combinam prática com `curl` (testando APIs reais) e design de APIs REST (projetando endpoints). A habilidade de projetar APIs bem estruturadas é uma das mais valorizadas no mercado — e começa com a prática.

---

## Exercício 1: Praticando com curl

Use a API pública JSONPlaceholder (https://jsonplaceholder.typicode.com) para executar cada comando abaixo no terminal. Anote o status code e observe a estrutura da resposta.

### Parte A: Operações GET

```bash
# 1. Buscar todos os usuarios
curl https://jsonplaceholder.typicode.com/users

# 2. Buscar o usuario de ID 3
curl https://jsonplaceholder.typicode.com/users/3

# 3. Buscar os posts do usuario 1
curl https://jsonplaceholder.typicode.com/users/1/posts

# 4. Buscar todos os comentarios
curl https://jsonplaceholder.typicode.com/comments

# 5. Buscar comentarios do post 1
curl https://jsonplaceholder.typicode.com/posts/1/comments
```

Para cada requisição, responda:
- Quantos itens foram retornados?
- Quais campos cada item tem?
- A URL segue as convenções REST?

### Parte B: Operações de Escrita

```bash
# 6. Criar um novo post
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Meu primeiro post via API", "body": "Estou aprendendo REST!", "userId": 1}'

# 7. Atualizar o post 1 completamente (PUT)
curl -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "title": "Post atualizado", "body": "Novo conteudo completo", "userId": 1}'

# 8. Atualizar parcialmente o post 1 (PATCH)
curl -X PATCH https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Apenas o titulo mudou"}'

# 9. Deletar o post 1
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

Para cada requisição, responda:
- Qual status code foi retornado?
- O que veio no body da resposta?
- Qual a diferença entre a resposta do PUT e do PATCH?

### Parte C: Verificando Status Codes

```bash
# 10. Buscar um recurso que nao existe
curl -s -o /dev/null -w "Status: %{http_code}\n" https://jsonplaceholder.typicode.com/posts/9999

# 11. Buscar a lista de posts (deve retornar 200)
curl -s -o /dev/null -w "Status: %{http_code}\n" https://jsonplaceholder.typicode.com/posts

# 12. Criar um post (deve retornar 201)
curl -s -o /dev/null -w "Status: %{http_code}\n" -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Teste", "body": "Teste", "userId": 1}'
```

Nota: a JSONPlaceholder é uma API de teste — ela simula as operações mas não persiste os dados. Os POST, PUT e DELETE retornam respostas simuladas.

---

## Exercício 2: Projetando APIs REST

### Parte A: Sistema de Biblioteca

Projete a API REST para um sistema de biblioteca que gerência livros e empréstimos. O sistema tem:

- Livros: título, autor, ISBN, ano de publicação, disponível (sim/não)
- Empréstimos: livro, usuário, data de empréstimo, data de devolução prevista, devolvido (sim/não)

Para cada operação, defina verbo, URL, body (quando aplicável), status codes e exemplo de resposta JSON:

1. Listar todos os livros
2. Buscar um livro por ID
3. Cadastrar um novo livro
4. Atualizar informações de um livro
5. Remover um livro
6. Listar livros disponíveis (filtro)
7. Registrar um empréstimo
8. Registrar a devolução de um livro
9. Listar empréstimos de um usuário específico

### Parte B: Sistema de Notas Escolares

Projete a API REST para um sistema de notas com:

- Alunos: nome, matrícula, turma
- Disciplinas: nome, professor, carga horária
- Notas: aluno, disciplina, valor, bimestre

Defina pelo menos 8 endpoints cobrindo CRUD de alunos, disciplinas e notas, incluindo consultas como "notas de um aluno em uma disciplina" e "média da turma em uma disciplina".

---

## Exercício 3: Corrigindo APIs Mal Projetadas

Cada API abaixo viola convenções REST. Identifique o problema e proponha a correção.

| # | URL Original | Problema | URL Corrigida |
|---|-------------|----------|---------------|
| 1 | `GET /getAllUsers` | | |
| 2 | `POST /user/new` | | |
| 3 | `GET /Product/42` | | |
| 4 | `DELETE /users/remove/42` | | |
| 5 | `PUT /updateUser` | | |
| 6 | `GET /users/42/getOrders` | | |
| 7 | `POST /products/42/delete` | | |
| 8 | `GET /searchProducts?name=mouse` | | |

---

## Exercício 4: Status Codes Corretos

Para cada cenário, indique qual status code a API deveria retornar:

| # | Cenário | Status Code |
|---|---------|-------------|
| 1 | GET /products — lista retornada com sucesso | |
| 2 | GET /products/999 — produto não existe | |
| 3 | POST /products — produto criado com sucesso | |
| 4 | POST /products — JSON mal formatado no body | |
| 5 | POST /products — preco negativo enviado | |
| 6 | DELETE /products/42 — produto removido com sucesso | |
| 7 | PUT /products/42 — produto atualizado com sucesso | |
| 8 | GET /admin/dashboard — usuario não enviou token | |
| 9 | GET /admin/dashboard — usuario enviou token mas não e admin | |
| 10 | POST /users — email ja cadastrado | |
| 11 | GET /products — erro interno no banco de dados | |
| 12 | POST /products — campo "name" obrigatório não enviado | |

---

## Exercício 5: De CRUD para API

Pegue o CRUD de produtos que você construiu no capítulo 8 (Python + SQLite). Para cada função do CRUD, defina o endpoint REST equivalente:

| Função Python | Verbo | URL | Body | Status Sucesso |
|---------------|-------|-----|------|---------------|
| `create_product(name, price, stock)` | | | | |
| `list_products()` | | | | |
| `get_product(id)` | | | | |
| `update_product(id, name, price, stock)` | | | | |
| `delete_product(id)` | | | | |
| `search_products(name)` | | | | |

---

## Exercício 6: Analisando uma API Real

Acesse a documentação da API do GitHub (https://docs.github.com/en/rest) e responda:

1. Qual é a URL base da API?
2. Como buscar informações de um usuário específico?
3. Como listar os repositórios de um usuário?
4. A API usa versionamento? Como?
5. Quais headers de autenticação são necessários?
6. A API segue as convenções REST que aprendemos?

Dica: você pode testar com curl:
```bash
curl https://api.github.com/users/torvalds
curl https://api.github.com/users/torvalds/repos
```

---

## Gabarito Comentado

### Exercício 3 — Respostas

| # | URL Original | Problema | URL Corrigida |
|---|-------------|----------|---------------|
| 1 | `GET /getAllUsers` | Verbo na URL - GET ja indica busca | `GET /users` |
| 2 | `POST /user/new` | Verbo na URL e singular | `POST /users` |
| 3 | `GET /Product/42` | Maiuscula e singular | `GET /products/42` |
| 4 | `DELETE /users/remove/42` | Verbo na URL - DELETE ja indica remoção | `DELETE /users/42` |
| 5 | `PUT /updateUser` | Verbo na URL e sem ID do recurso | `PUT /users/42` |
| 6 | `GET /users/42/getOrders` | Verbo na URL | `GET /users/42/orders` |
| 7 | `POST /products/42/delete` | Usando POST para deletar com verbo na URL | `DELETE /products/42` |
| 8 | `GET /searchProducts?name=mouse` | Verbo na URL | `GET /products?name=mouse` |

### Exercício 4 — Respostas

| # | Status Code | Justificativa |
|---|-------------|---------------|
| 1 | 200 OK | Busca com sucesso |
| 2 | 404 Not Found | Recurso não existe |
| 3 | 201 Created | Recurso criado |
| 4 | 400 Bad Request | Dados mal formatados |
| 5 | 422 Unprocessable Entity | Dados validos mas conteúdo inválido |
| 6 | 204 No Content | Removido com sucesso, sem body |
| 7 | 200 OK | Atualizado com sucesso |
| 8 | 401 Unauthorized | Sem autenticação |
| 9 | 403 Forbidden | Autenticado mas sem permissão |
| 10 | 409 Conflict | Conflito com recurso existente |
| 11 | 500 Internal Server Error | Erro no servidor |
| 12 | 422 Unprocessable Entity | Campo obrigatório ausente |

### Exercício 5 — Respostas

| Função Python | Verbo | URL | Body | Status |
|---------------|-------|-----|------|--------|
| `create_product(...)` | POST | /products | `{"name": "...", "price": ..., "stock": ...}` | 201 |
| `list_products()` | GET | /products | - | 200 |
| `get_product(id)` | GET | /products/{id} | - | 200 |
| `update_product(...)` | PUT | /products/{id} | `{"name": "...", "price": ..., "stock": ...}` | 200 |
| `delete_product(id)` | DELETE | /products/{id} | - | 204 |
| `search_products(name)` | GET | /products?name={name} | - | 200 |

---

[← Voltar ao conteúdo](cap11-mod03-apis-http-rest-conteudo.md)
