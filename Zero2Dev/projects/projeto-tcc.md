# Projeto Final — TCC

[← Voltar ao Capítulo 12](../capitulos/cap12-mod06-ia-no-desenvolvimento.md) · [Voltar ao Índice](../readme.md)

---

## Visao Geral

Este e o projeto final do curso. Você vai construir uma aplicação completa do zero — desde a definição do problema ate a entrega com documentação e apresentacao. O TCC consolida tudo que você aprendeu nos 11 capítulos anteriores.

Não existe um único projeto "certo". Você escolhe o problema, define o escopo e constroi a solução. O que importa e o processo e a qualidade da execução.

---

## Requisitos do Projeto

### Requisitos Obrigatórios

O projeto DEVE ter:

| Requisito | Capítulo de referência | Por que |
|-----------|----------------------|---------|
| Pelo menos 2 entidades relacionadas | Cap 8 — Modelagem | Exercita modelagem relacional |
| CRUD completo (Create, Read, Update, Delete) | Cap 8 — SQL | Operações básicas de dados |
| Persistência em banco de dados (SQLite) | Cap 8 — SQLite | Dados sobrevivem a reinicializacao |
| Pelo menos 3 regras de negocio | Cap 9 — OOP, Cap 10 — Servicos | Lógica além do CRUD básico |
| Arquitetura em camadas | Cap 10 — Arquitetura | Separacao de responsabilidades |
| Tratamento de erros consistente | Cap 5 — Erros, Cap 11 — APIs | Robustez e profissionalismo |
| Código versionado com Git | Cap 4 — Git | Histórico e controle de versão |
| README.md completo | Cap 12 — Documentação | Documentação do projeto |
| Código comentado | Cap 12 — Documentação | Legibilidade e manutenção |

### Requisitos Recomendados (Diferenciais)

| Requisito | Capítulo de referência | Impacto |
|-----------|----------------------|---------|
| API REST com FastAPI | Cap 11 — APIs | Demonstra integração de sistemas |
| Documentação Swagger | Cap 11 — FastAPI | Documentação interativa |
| Paginacao e filtros | Cap 11 — Projeto | Funcionalidades avancadas |
| Estatisticas e resumos | Cap 11 — Projeto | Consultas SQL avancadas |
| Testes automatizados | Cap 5 — Debugging | Qualidade de código |
| Docker | Cap 6 — Docker | Ambiente reproduzivel |

---

## Stacks Permitidas

### Opcao 1: Python + FastAPI + SQLite (Recomendada)

```
projeto/
├── main.py
├── database.py
├── models/
│   ├── __init__.py
│   └── [entidades].py
├── repositories/
│   ├── __init__.py
│   └── [entidades]_repository.py
├── services/
│   ├── __init__.py
│   └── [entidades]_service.py
├── routers/
│   ├── __init__.py
│   └── [entidades].py
├── README.md
└── projeto.db
```

### Opcao 2: Python CLI + SQLite

```
projeto/
├── main.py
├── database.py
├── models.py
├── repositories/
│   └── [entidades]_repository.py
├── services/
│   └── [entidades]_service.py
├── README.md
└── projeto.db
```

### Opcao 3: C# + .NET + SQLite

```
Projeto/
├── Program.cs
├── Domain/
│   └── [Entidades].cs
├── Interfaces/
│   └── I[Entidade]Repository.cs
├── Repositories/
│   └── [Entidade]Repository.cs
├── Services/
│   └── [Entidade]Service.cs
├── README.md
└── projeto.db
```

---

## Fases de Desenvolvimento

### Fase 1: Planejamento (Módulo 12.1)

**Entregavel:** README.md com documento de planejamento

- [ ] Problema definido (1-2 paragrafos)
- [ ] Escopo delimitado (dentro e fora do MVP)
- [ ] Entidades listadas com atributos e relacionamentos
- [ ] Funcionalidades priorizadas (essencial, importante, desejavel)
- [ ] Tecnologia escolhida
- [ ] Repositório Git criado

**Commit:** `docs: initial project planning`

### Fase 2: Modelagem e Arquitetura (Módulo 12.2)

**Entregavel:** Banco de dados criado, modelos definidos

- [ ] SQL de criação das tabelas escrito e testado
- [ ] Diagrama ER no README
- [ ] Modelos de dados (Pydantic/classes) criados
- [ ] Estrutura de pastas criada
- [ ] Diagrama de arquitetura no README
- [ ] Decisoes técnicas documentadas

**Commit:** `feat(database): add data model and database setup`

### Fase 3: CRUD Básico (Módulo 12.3)

**Entregavel:** Operações básicas funcionando

- [ ] Repositórios implementados (create, get_all, get_by_id, update, delete)
- [ ] Servicos implementados (repassam para repositórios)
- [ ] Controllers/routers implementados (endpoints ou menu CLI)
- [ ] Todas as operações testadas manualmente

**Commit:** `feat(crud): add basic CRUD operations`

### Fase 4: Regras de Negocio (Módulo 12.3)

**Entregavel:** Sistema robusto com validacoes

- [ ] Pelo menos 3 regras de negocio implementadas no servico
- [ ] Tratamento de erros consistente (400, 404, 409, 422)
- [ ] Cenários de erro testados
- [ ] Mensagens de erro claras e informativas

**Commit:** `feat(validation): add business rules and error handling`

### Fase 5: Funcionalidades Extras (Módulo 12.3)

**Entregavel:** Sistema completo e útil

- [ ] Paginacao (se API)
- [ ] Filtros relevantes para o dominio
- [ ] Busca por texto (se aplicavel)
- [ ] Estatisticas ou resumos
- [ ] Pelo menos 1 funcionalidade "importante" além do CRUD

**Commit:** `feat(features): add filters, pagination and statistics`

### Fase 6: Documentação e Entrega (Módulo 12.4)

**Entregavel:** Projeto pronto para avaliacao

- [ ] README.md completo (instalacao, uso, endpoints, modelo, arquitetura)
- [ ] Código comentado (cabecalhos, docstrings, inline)
- [ ] Swagger customizado (se FastAPI)
- [ ] Histórico de commits limpo e descritivo
- [ ] Tag de versão: `git tag -a v1.0.0 -m "TCC v1.0.0"`

**Commit:** `docs: complete project documentation`

---

## Ideias de Projeto

Se você não tem uma ideia propria, escolha uma destas:

### 1. FinControl — Controle Financeiro Pessoal

**Problema:** Não saber quanto gasta por mes nem em que categorias.

**Entidades:** Transaction, Category

**Funcionalidades:**
- Registrar receitas e despesas com categoria e data
- Listar transações com filtros (data, categoria, tipo)
- Consultar saldo (receitas - despesas)
- Resumo por categoria
- Gerenciar categorias

**Regras de negocio:**
- Valor deve ser positivo
- Tipo so pode ser "income" ou "expense"
- Categoria deve existir ao criar transação
- Não remover categoria com transações

---

### 2. BookShelf — Gerenciador de Biblioteca Pessoal

**Problema:** Não lembrar quais livros tem, quais ja leu e quais quer ler.

**Entidades:** Book, Category, ReadingLog

**Funcionalidades:**
- Cadastrar livros com título, autor, categoria e status
- Registrar leituras (data inicio, data fim, avaliacao)
- Listar livros por status (quero ler, lendo, lido)
- Buscar por título ou autor
- Estatisticas (livros lidos por mes, autores mais lidos)

**Regras de negocio:**
- ISBN deve ser único
- Avaliacao de 1 a 5
- Não pode registrar leitura de livro com status "quero ler" sem mudar para "lendo"
- Data fim deve ser posterior a data inicio

---

### 3. FitTracker — Registro de Treinos

**Problema:** Não lembrar quais exercícios fez, com qual carga e quando.

**Entidades:** Exercise, Workout, WorkoutExercise

**Funcionalidades:**
- Cadastrar exercícios (nome, grupo muscular)
- Registrar treinos com data e exercícios realizados
- Para cada exercício no treino: series, repeticoes, carga
- Listar treinos por data
- Histórico de evolução de carga por exercício

**Regras de negocio:**
- Carga e repeticoes devem ser positivos
- Exercício deve existir ao adicionar no treino
- Não pode ter dois treinos na mesma data (ou pode, dependendo da regra)
- Grupo muscular deve ser de uma lista válida

---

### 4. TaskFlow — Gerenciador de Tarefas

**Problema:** Não conseguir organizar tarefas e prioridades.

**Entidades:** Task, Project, Tag

**Funcionalidades:**
- Criar tarefas com título, descrição, prioridade e prazo
- Organizar tarefas em projetos
- Marcar tarefas como concluidas
- Filtrar por projeto, prioridade, status
- Listar tarefas atrasadas

**Regras de negocio:**
- Prioridade: low, medium, high
- Status: pending, in_progress, done
- Não pode marcar como "done" sem ter passado por "in_progress"
- Prazo deve ser data futura ao criar

---

### 5. MenuMaster — Cardapio Digital

**Problema:** Restaurante pequeno que precisa gerenciar cardapio e precos.

**Entidades:** Dish, Category, Ingredient

**Funcionalidades:**
- Cadastrar pratos com nome, descrição, preco e categoria
- Gerenciar categorias (entrada, prato principal, sobremesa, bebida)
- Listar cardapio por categoria
- Buscar pratos por nome ou ingrediente
- Marcar pratos como disponiveis/indisponiveis

**Regras de negocio:**
- Preco deve ser positivo
- Nome do prato deve ser único
- Categoria deve existir
- Não remover categoria com pratos

---

## Critérios de Avaliacao

| Critério | Peso | O que e avaliado |
|----------|------|-----------------|
| Funcionalidade | 30% | O sistema funciona? CRUD completo? Regras de negocio? |
| Arquitetura | 20% | Código organizado em camadas? Responsabilidades claras? |
| Documentação | 20% | README completo? Código comentado? Swagger? |
| Modelagem | 15% | Modelo de dados correto? Relacionamentos? Indices? |
| Apresentacao | 15% | Clareza na explicacao? Demonstracao funcional? Respostas? |

### Nota Máxima

Para nota máxima, o projeto deve:
- Ter todas as fases completas (1-6)
- Funcionar sem erros
- Ter documentação que permite rodar sem ajuda
- Demonstrar dominio dos conceitos do curso
- Ter histórico de commits limpo e descritivo
- Apresentacao clara e dentro do tempo

### Nota Mínima para Aprovacao

Para aprovacao, o projeto deve ter no mínimo:
- Fases 1-4 completas (planejamento, modelagem, CRUD, regras)
- Sistema funcional com CRUD básico
- README com instruções de instalacao e uso
- Repositório Git com histórico de commits
- Apresentacao realizada

---

## Cronograma Sugerido

| Fase | Atividade | Duracao sugerida |
|------|-----------|-----------------|
| 1 | Planejamento | 3-4 horas |
| 2 | Modelagem e arquitetura | 3-4 horas |
| 3 | CRUD básico | 6-8 horas |
| 4 | Regras de negocio | 5-6 horas |
| 5 | Funcionalidades extras | 6-8 horas |
| 6 | Documentação e polimento | 3-4 horas |
| — | Preparacao da apresentacao | 2-3 horas |
| **Total** | | **28-37 horas** |

Distribua ao longo de 2-4 semanas, trabalhando algumas horas por dia.

---

## Entrega Final

O projeto e entregue como um repositório Git (preferencialmente no GitHub) contendo:

```
projeto/
├── README.md              # Documentacao completa
├── main.py                # Ponto de entrada
├── database.py            # Configuracao do banco
├── models/                # Modelos de dados
├── repositories/          # Acesso ao banco
├── services/              # Logica de negocio
├── routers/               # Endpoints (se API)
├── projeto.db             # Banco SQLite (criado automaticamente)
└── .gitignore             # Arquivos ignorados pelo Git
```

### .gitignore Recomendado

```
# Python
__pycache__/
*.pyc
*.pyo
.env

# Banco de dados (recriado automaticamente)
*.db

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

---

## Seu Projeto Esta Pronto Quando...

- [ ] Você consegue clonar o repositório em uma máquina limpa e rodar seguindo o README
- [ ] Todas as operações CRUD funcionam sem erros
- [ ] Dados persistem apos reiniciar o servidor
- [ ] Dados invalidos são rejeitados com mensagens claras
- [ ] O código esta organizado em camadas com responsabilidades definidas
- [ ] Cada arquivo tem comentários explicando o que faz
- [ ] O histórico de commits conta a história do desenvolvimento
- [ ] Você consegue explicar qualquer parte do código para outra pessoa
- [ ] Você se orgulha do que construiu

---

**Boa sorte. Você esta pronto.**

[← Voltar ao Capítulo 12](../capitulos/cap12-mod06-ia-no-desenvolvimento.md) · [Voltar ao Índice](../readme.md)
