# 8.8 — Exercícios: SQL vs NoSQL

[← Voltar ao conteúdo: SQL vs NoSQL](cap08-mod08-sql-vs-nosql-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem a comparação entre bancos SQL e NoSQL: quando usar cada um, Teorema CAP, tipos de bancos NoSQL, e decisões de arquitetura. São exercícios conceituais e de análise — não há código para executar.

---

## Exercício 1: Escolhendo o Banco Certo

Para cada cenário abaixo, escolha o tipo de banco mais adequado (Relacional SQL, Documentos, Chave-Valor, Grafos ou Colunar). Justifique sua escolha explicando por que os outros tipos seriam piores.

a) **Sistema de RH de uma empresa** com 2.000 funcionários. Precisa gerenciar: dados pessoais, cargos, salários, férias, benefícios, avaliações de desempenho. Relatórios mensais de folha de pagamento.

b) **Catálogo de um marketplace** como o Mercado Livre. Milhões de produtos de categorias completamente diferentes: eletrônicos têm voltagem e garantia, roupas têm tamanho e cor, alimentos têm data de validade e peso. Cada categoria tem atributos únicos.

c) **Sistema de detecção de fraude** de um banco. Precisa analisar conexões entre contas: transferências entre contas, titulares em comum, endereços compartilhados, padrões de transação suspeitos.

d) **Cache de um portal de notícias** que recebe 50 milhões de pageviews por dia. As 100 notícias mais acessadas precisam ser servidas em menos de 5ms.

e) **Sistema de analytics** de um e-commerce. Precisa processar 2 TB de logs por dia para responder: "quantas vendas por hora?", "qual produto mais visto?", "qual a taxa de conversão por região?".

f) **Sistema de prontuário eletrônico** de um hospital. Dados de pacientes, consultas, exames, prescrições, internações. Regulamentação exige auditoria completa e integridade absoluta.

g) **Aplicativo de chat** como WhatsApp. Bilhões de mensagens por dia, cada mensagem com remetente, destinatário, texto, timestamp, status de entrega.

h) **Sistema de recomendação** do Spotify. Precisa responder: "usuários que ouviram X também ouviram Y", "artistas similares a Z", "playlists com músicas parecidas".

---

## Exercício 2: Representando Dados em Diferentes Modelos

Pegue o modelo da lanchonete (módulo 8.3) e represente os mesmos dados em formatos diferentes:

a) **Banco de documentos (JSON)**: escreva o documento JSON completo de um pedido, incluindo dados do cliente, itens com dados do produto e categoria. Tudo em um único documento.

```json
{
    "pedido_id": 1,
    "data": "2024-03-01",
    "status": "entregue",
    "cliente": {
        // TODO: dados do cliente embutidos
    },
    "itens": [
        {
            // TODO: dados de cada item com produto embutido
        }
    ],
    "valor_total": 43.80
}
```

b) **Banco chave-valor**: defina as chaves e valores para armazenar os mesmos dados. Que convenção de chaves você usaria?

```
cliente:1          → {"nome": "Joao Silva", "email": "joao@email.com"}
produto:1          → {"nome": "X-Burguer", "preco": 18.90, "categoria": "Lanches"}
pedido:1           → {"cliente_id": 1, "data": "2024-03-01", "valor_total": 43.80}
pedido:1:itens     → [{"produto_id": 1, "qtd": 1}, {"produto_id": 3, "qtd": 2}]
```

c) Compare detalhadamente as três representações (relacional, documento, chave-valor):

| Operação | SQL Relacional | Documento | Chave-Valor |
|----------|---------------|-----------|-------------|
| Buscar pedido completo | ? | ? | ? |
| Atualizar preço do produto | ? | ? | ? |
| Listar pedidos de um cliente | ? | ? | ? |
| Produto mais vendido | ? | ? | ? |
| Mudar email do cliente | ? | ? | ? |

Para cada célula, descreva a complexidade da operação (fácil, médio, difícil) e por quê.

---

## Exercício 3: Teorema CAP

O Teorema CAP diz que um sistema distribuído pode garantir no máximo 2 de 3 propriedades: Consistência (C), Disponibilidade (A) e Tolerância a Partição (P).

a) Explique com suas palavras o que cada propriedade significa:
   - **Consistência**: todos os nós veem os mesmos dados ao mesmo tempo
   - **Disponibilidade**: toda requisição recebe uma resposta (mesmo que não seja a mais atualizada)
   - **Tolerância a Partição**: o sistema continua funcionando mesmo se a comunicação entre nós falhar

b) Para cada combinação, dê um exemplo de banco de dados real e um cenário onde essa combinação faz sentido:
   - **CP** (Consistência + Partição, sacrifica Disponibilidade): ?
   - **AP** (Disponibilidade + Partição, sacrifica Consistência): ?
   - **CA** (Consistência + Disponibilidade, sacrifica Partição): ?

c) Por que "CA" é considerado impraticável em sistemas distribuídos?

d) Um banco de dados relacional tradicional (PostgreSQL rodando em um único servidor) se encaixa em qual combinação? Por quê?

---

## Exercício 4: Análise SWOT — SQL vs NoSQL

Faça uma análise SWOT (Forças, Fraquezas, Oportunidades, Ameaças) para cada tipo:

**SQL (Relacional)**

| | Positivo | Negativo |
|---|---------|----------|
| Interno | Forças: ? | Fraquezas: ? |
| Externo | Oportunidades: ? | Ameaças: ? |

**NoSQL (Documentos — ex: MongoDB)**

| | Positivo | Negativo |
|---|---------|----------|
| Interno | Forças: ? | Fraquezas: ? |
| Externo | Oportunidades: ? | Ameaças: ? |

Para cada quadrante, liste pelo menos 3 itens com justificativa.

---

## Exercício 5: Debate — MongoDB vs PostgreSQL

Imagine que você está em uma reunião de equipe decidindo o banco de dados para um novo projeto: um sistema de gestão escolar (alunos, professores, turmas, notas, frequência, boletins).

Um colega argumenta: "Vamos usar MongoDB porque é mais moderno, mais flexível e mais fácil de escalar."

a) Escreva 5 argumentos a favor de PostgreSQL para este caso específico.

b) Escreva 3 argumentos a favor de MongoDB para este caso (tente ser justo).

c) Qual seria sua recomendação final? Justifique considerando: volume de dados esperado, tipo de consultas, necessidade de integridade, equipe disponível, prazo do projeto.

d) Existe um cenário onde usar AMBOS faria sentido neste projeto? Qual parte usaria SQL e qual usaria NoSQL?

---

## Exercício 6: Pesquisa — Bancos de Dados no Mercado

Pesquise e escreva um parágrafo (5-8 linhas) sobre cada tema:

a) **DB-Engines Ranking**: acesse db-engines.com e veja o ranking atual. Quais são os 10 bancos mais populares? Quantos são SQL e quantos são NoSQL? A posição mudou nos últimos 5 anos?

b) **PostgreSQL JSONB**: o PostgreSQL tem suporte a dados JSON nativamente. Pesquise o que é JSONB e como ele permite usar PostgreSQL como banco de documentos. Isso torna o MongoDB desnecessário?

c) **Google Bigtable e Spanner**: o Google criou o Bigtable (NoSQL) em 2004 e o Spanner (SQL distribuído) em 2012. Por que o Google "voltou" para SQL? O que o Spanner resolve que o Bigtable não resolvia?

d) **Mercado brasileiro**: quais bancos de dados são mais usados em empresas brasileiras? Pesquise vagas de emprego em sites como LinkedIn e Gupy — quais bancos aparecem mais nos requisitos?

---

## Exercício 7: Modelagem Comparada

Modele o mesmo sistema em SQL e NoSQL (documentos):

**Sistema**: plataforma de streaming de vídeo (tipo Netflix simplificado)

Entidades: filmes, séries (com temporadas e episódios), usuários, perfis (cada conta tem até 5 perfis), lista "Minha Lista", histórico de visualização, avaliações.

a) **Modelo SQL**: crie o diagrama ER com todas as tabelas, chaves e relacionamentos.

b) **Modelo NoSQL (documentos)**: crie os documentos JSON que representariam os mesmos dados. Decida o que embutir e o que referenciar.

c) Compare os dois modelos:
   - Qual é mais fácil de entender?
   - Qual é mais fácil de consultar para "mostrar a página inicial de um perfil" (filmes recomendados, continuar assistindo, minha lista)?
   - Qual é mais fácil de atualizar quando um filme muda de título?
   - Qual garante melhor integridade dos dados?

---

## Exercício 8: Cenário Real — Migrando de SQL para NoSQL

Uma startup começou com PostgreSQL e agora tem 50 milhões de usuários. O banco está lento para certas operações. A equipe está considerando migrar parte dos dados para MongoDB.

a) Quais dados fariam sentido migrar para MongoDB? (Pense em dados com schema flexível ou que são acessados como documentos completos.)

b) Quais dados DEVEM permanecer em PostgreSQL? (Pense em dados que precisam de integridade referencial, transações ACID, relatórios com JOINs.)

c) Como os dois bancos se comunicariam? (A aplicação acessa ambos? Existe sincronização?)

d) Quais riscos essa migração traz? Liste pelo menos 5 riscos técnicos e organizacionais.

e) Existe uma alternativa a migrar para NoSQL? (Dica: PostgreSQL tem recursos como JSONB, particionamento, réplicas de leitura.)

---

## Gabarito Comentado

### Exercício 1 — Escolhendo o Banco Certo

a) **SQL Relacional** — dados altamente estruturados com relacionamentos claros (funcionário → cargo → departamento), necessidade de integridade absoluta (folha de pagamento não pode ter erros), relatórios complexos com JOINs e agregações. Volume pequeno (2.000 registros) — qualquer banco dá conta.

b) **Documentos (MongoDB)** — cada categoria de produto tem atributos completamente diferentes. Em SQL, precisaria de uma tabela genérica com campos opcionais ou uma tabela por categoria (dezenas de tabelas). Em documentos, cada produto é um JSON com os campos que precisa — flexibilidade natural.

c) **Grafos (Neo4j)** — o problema é essencialmente sobre conexões e caminhos entre entidades. "Encontre todas as contas conectadas a esta conta suspeita em até 3 graus de separação" é uma query natural em grafos mas extremamente complexa em SQL (JOINs recursivos).

d) **Chave-Valor (Redis)** — acesso por chave (URL da notícia), latência ultra-baixa (<5ms), dados temporários (cache expira). Não precisa de consultas complexas — apenas "dada esta URL, retorne o HTML".

e) **Colunar (ClickHouse)** — consultas analíticas em grandes volumes, lendo apenas colunas necessárias de bilhões de registros. "Soma de vendas por hora" lê apenas as colunas timestamp e valor, ignorando todas as outras.

f) **SQL Relacional** — regulamentação exige integridade absoluta e auditoria. Transações ACID são obrigatórias (não pode perder dados de paciente). Relacionamentos claros entre entidades. Compliance é mais importante que performance.

g) **Documentos ou Chave-Valor** — volume massivo (bilhões/dia), cada mensagem é independente, não precisa de JOINs complexos. Chave-valor para mensagens recentes (acesso rápido), documentos para histórico.

h) **Grafos** — "usuários que ouviram X também ouviram Y" é uma travessia de grafo. "Artistas similares" são nós próximos no grafo de relações. Recomendação é o caso de uso clássico de grafos.

### Exercício 3 — Teorema CAP

b) **CP**: MongoDB (com write concern majority) — garante que todos os nós têm os mesmos dados, mas pode ficar indisponível durante partições de rede. Cenário: sistema bancário onde consistência é mais importante que disponibilidade.

**AP**: Cassandra — sempre responde requisições, mas diferentes nós podem retornar dados ligeiramente diferentes durante partições. Cenário: feed de rede social onde ver um post com 1 segundo de atraso é aceitável.

**CA**: PostgreSQL em servidor único — consistente e disponível, mas não tolera partição (se o servidor cair, tudo para). Cenário: sistema interno de uma empresa com um único servidor.

c) Em sistemas distribuídos, partições de rede SEMPRE podem acontecer (cabos cortados, switches com defeito, latência extrema). Não é uma escolha — é uma realidade. Portanto, P é obrigatório, e a escolha real é entre C e A.

d) PostgreSQL em servidor único é CA — consistente e disponível, mas se o servidor cair, o sistema para (não tolera partição). Com réplicas, PostgreSQL pode ser configurado como CP (prioriza consistência) ou AP (prioriza disponibilidade com réplicas de leitura).

---

[← Voltar ao conteúdo: SQL vs NoSQL](cap08-mod08-sql-vs-nosql-conteudo.md)
