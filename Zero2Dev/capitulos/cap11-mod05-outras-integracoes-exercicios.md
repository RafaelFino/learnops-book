# 11.5 — Exercícios: Outras Formas de Integração

[← Voltar ao conteúdo](cap11-mod05-outras-integracoes-conteudo.md)

---

## Sobre estes Exercícios

Estes exercícios cobrem as tecnologias de integração apresentadas no módulo 11.5: gRPC, GraphQL, WebSocket, webhooks, TCP direto, integração por arquivos e MCP. Como este módulo e predominantemente conceitual, os exercícios focam em análise, comparação e tomada de decisao — habilidades essenciais para um desenvolvedor que precisa escolher a tecnologia certa para cada problema.

---

## Exercício 1: Identificando a Tecnologia pelo Comportamento

Para cada descrição abaixo, identifique qual tecnologia de integração esta sendo descrita. Justifique sua resposta com pelo menos uma caracteristica técnica.

1. "O cliente envia uma única requisicao descrevendo exatamente quais campos quer, e o servidor retorna apenas esses campos"
2. "Os dados são serializados em formato binário usando um arquivo .proto que define o contrato"
3. "Apos um handshake HTTP inicial, a conexão permanece aberta e ambos os lados podem enviar mensagens a qualquer momento"
4. "O sistema A gera um arquivo CSV toda noite e coloca em uma pasta compartilhada. O sistema B le o arquivo de manha e processa"
5. "Quando um pagamento e aprovado, o gateway faz um POST para uma URL que você registrou previamente"
6. "Um agente de IA se conecta a um servidor que expoe ferramentas como 'ler_arquivo' e 'executar_sql'"
7. "A comunicação usa bytes puros sobre TCP, sem headers HTTP, para minimizar latencia em um jogo multiplayer"
8. "O servidor envia dados continuamente para o cliente via HTTP, mas o cliente não pode enviar de volta pela mesma conexão"

**Respostas esperadas:**

1. GraphQL — o cliente define a estrutura da resposta via query
2. gRPC — usa Protocol Buffers (.proto) para serialização binaria
3. WebSocket — conexão bidirecional persistente apos handshake
4. Integração por arquivos — troca de dados via arquivos em local compartilhado
5. Webhook — callback HTTP acionado por evento
6. MCP (Model Context Protocol) — protocolo para conectar IA a ferramentas
7. TCP direto — comunicação sem camada HTTP para performance máxima
8. SSE (Server-Sent Events) — streaming unidirecional do servidor para o cliente

---

## Exercício 2: Tabela Comparativa Personalizada

Crie uma tabela comparando REST, gRPC e GraphQL nos seguintes critérios. Preencha com suas proprias palavras baseado no que aprendeu:

| Critério | REST | gRPC | GraphQL |
|----------|------|------|---------|
| Formato de dados | | | |
| Quem define o formato da resposta | | | |
| Número de endpoints | | | |
| Facilidade de debug | | | |
| Melhor cenário de uso | | | |
| Pior cenário de uso | | | |
| Suporte em navegadores | | | |
| Curva de aprendizado | | | |

**Resposta esperada:**

| Critério | REST | gRPC | GraphQL |
|----------|------|------|---------|
| Formato de dados | JSON (texto) | Protobuf (binário) | JSON (texto) |
| Quem define o formato da resposta | Servidor | Arquivo .proto (contrato) | Cliente (via query) |
| Número de endpoints | Multiplos (um por recurso) | Multiplos (um por função) | Um único (/graphql) |
| Facilidade de debug | Alta (curl, Postman, legivel) | Baixa (binário, ferramentas especificas) | Media (GraphiQL, mas queries complexas) |
| Melhor cenário de uso | APIs publicas, CRUD simples | Microservicos internos, alta performance | Frontends complexos, apps mobile |
| Pior cenário de uso | Frontends que precisam de dados variados | APIs publicas para terceiros | CRUD simples, APIs internas |
| Suporte em navegadores | Excelente (nativo) | Limitado (precisa de gRPC-Web) | Bom (via HTTP POST) |
| Curva de aprendizado | Baixa | Media | Media-Alta |

---

## Exercício 3: Cenários de Decisao

Para cada cenário, escolha a tecnologia mais adequada entre: REST, gRPC, GraphQL, WebSocket, Webhook, Filas, Arquivos, TCP direto, MCP. Justifique em 2-3 frases.

**Cenário A:** Uma startup de 3 pessoas esta criando um app de lista de tarefas. O app tem um frontend web e precisa de operações básicas: criar, listar, editar e deletar tarefas.

**Resposta esperada:** REST. E o cenário mais simples possível — CRUD básico com um único frontend. REST e a opcao mais simples, com mais tutoriais e ferramentas disponiveis. Não ha justificativa para a complexidade de gRPC ou GraphQL aqui.

**Cenário B:** Uma empresa de logistica tem 200 microservicos internos que processam 50.000 requisicoes por segundo entre si. A latencia precisa ser menor que 5ms.

**Resposta esperada:** gRPC. Comunicação interna entre microservicos com requisito de alta performance e baixa latencia. O formato binário (protobuf) e a multiplexacao do HTTP/2 reduzem significativamente o overhead comparado a REST com JSON.

**Cenário C:** Um banco precisa enviar o extrato mensal de 2 milhoes de clientes para o sistema de auditoria do Banco Central.

**Resposta esperada:** Integração por arquivos. Volume massivo de dados (milhoes de registros), processamento em batch (mensal), e o receptor e um sistema externo com requisitos proprios. Gerar um arquivo (CSV ou Parquet) e transferir e mais eficiente e confiavel do que 2 milhoes de chamadas de API.

**Cenário D:** Um app de esportes precisa mostrar o placar de jogos atualizando em tempo real para 500.000 usuarios simultaneos.

**Resposta esperada:** WebSocket (ou SSE, ja que e unidirecional). Os usuarios precisam receber atualizacoes instantaneas sem fazer requisicoes. WebSocket mantem a conexão aberta e o servidor envia o placar assim que muda. SSE também funcionaria porque a comunicação e so do servidor para o cliente.

**Cenário E:** Uma plataforma de e-commerce quer que quando um pedido for enviado, o sistema de email envie confirmacao, o sistema de estoque atualize quantidades, e o sistema de analytics registre a venda.

**Resposta esperada:** Filas com padrão pub/sub. Um único evento (pedido enviado) precisa ser processado por multiplos consumers independentes. Pub/sub permite que cada sistema receba o evento e processe no seu ritmo, sem acoplamento entre eles.

**Cenário F:** Uma empresa de midia tem um app mobile, um site web e um app para smart TV. Cada plataforma precisa de dados diferentes do mesmo backend — o mobile precisa de dados compactos, o site precisa de dados completos, a TV precisa de dados otimizados para tela grande.

**Resposta esperada:** GraphQL. Multiplos clientes com necessidades diferentes de dados e o cenário classico do GraphQL. Cada cliente envia a query pedindo exatamente o que precisa, sem over-fetching. A alternativa seria criar um BFF (Backend for Frontend) para cada plataforma, mas GraphQL resolve com menos código.

---

## Exercício 4: Analisando um Sistema Real

Considere o sistema do Spotify. Pesquise (ou imagine baseado no que aprendeu) e responda:

1. Quando você abre o app e ve a tela inicial com playlists recomendadas, albuns novos e podcasts sugeridos — qual tecnologia provavelmente e usada entre o app e o backend? Por que?

2. Quando você da play em uma musica e o streaming comeca — a entrega do audio usa HTTP normal ou algum protocolo especial? Por que?

3. Quando você esta ouvindo musica e um amigo comeca a ouvir a mesma musica, e o app mostra "Fulano também esta ouvindo" — qual tecnologia permite essa atualização em tempo real?

4. Quando o Spotify calcula suas recomendacoes personalizadas (Discover Weekly), isso acontece em tempo real ou em batch? Qual forma de integração faz mais sentido para processar dados de 500 milhoes de usuarios?

5. Quando um artista lanca um album novo e o Spotify precisa atualizar o catalogo, indexar para busca, gerar thumbnails e notificar seguidores — qual padrão de comunicação e mais adequado?

**Respostas esperadas:**

1. Provavelmente GraphQL ou REST otimizado. A tela inicial precisa de dados de multiplas fontes (playlists, albuns, podcasts) e cada plataforma (mobile, desktop, web) pode precisar de dados diferentes. GraphQL permite buscar tudo em uma query.

2. O streaming de audio geralmente usa HTTP com streaming progressivo (HTTP Live Streaming ou similar). Não e REST tradicional — e um download progressivo onde o audio e entregue em chunks enquanto você ouve. Protocolos como HLS (HTTP Live Streaming) são comuns.

3. WebSocket ou SSE. Atualizacoes de atividade social em tempo real exigem que o servidor envie dados sem o cliente pedir. WebSocket mantem a conexão aberta para essas notificacoes.

4. Batch (processamento em lote). Calcular recomendacoes para 500 milhoes de usuarios em tempo real seria inviavel. O Spotify processa dados de escuta em batch (provavelmente com Kafka e pipelines de dados), gerando recomendacoes que são armazenadas e servidas quando o usuario abre o app.

5. Filas com pub/sub. Um único evento (album lancado) precisa acionar multiplos sistemas independentes. Pub/sub permite que cada sistema (catalogo, busca, thumbnails, notificacoes) processe o evento no seu ritmo.

---

## Exercício 5: Escrevendo uma Query GraphQL

Dado o seguinte schema GraphQL de uma loja online:

```graphql
type Product {
  id: ID!
  name: String!
  price: Float!
  description: String
  category: Category!
  reviews: [Review!]!
  stock: Int!
  images: [String!]!
}

type Category {
  id: ID!
  name: String!
  products: [Product!]!
}

type Review {
  id: ID!
  author: User!
  rating: Int!
  comment: String
  createdAt: String!
}

type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
}

type Order {
  id: ID!
  products: [Product!]!
  total: Float!
  status: String!
}

type Query {
  product(id: ID!): Product
  products(category: String, limit: Int): [Product!]!
  user(id: ID!): User
  categories: [Category!]!
}
```

Escreva queries GraphQL para cada cenário:

**a)** A página de um produto precisa mostrar: nome, preco, descrição, nome da categoria, e as 3 reviews mais recentes (com nome do autor e nota).

**Resposta esperada:**
```graphql
query {
  product(id: "123") {
    name
    price
    description
    category {
      name
    }
    reviews {
      author {
        name
      }
      rating
    }
  }
}
```

**b)** A página inicial precisa mostrar: todas as categorias com nome, e os 5 primeiros produtos de cada categoria (so nome e preco).

**Resposta esperada:**
```graphql
query {
  categories {
    name
    products {
      name
      price
    }
  }
}
```

**c)** A página de perfil do usuario precisa mostrar: nome, email, e os ultimos pedidos com status e valor total.

**Resposta esperada:**
```graphql
query {
  user(id: "456") {
    name
    email
    orders {
      status
      total
    }
  }
}
```

**d)** Agora pense: quantas requisicoes REST você precisaria para obter os mesmos dados do item (a)? Liste os endpoints.

**Resposta esperada:**
Com REST, você precisaria de pelo menos 3 requisicoes:
1. `GET /products/123` — dados do produto (retornaria TODOS os campos, incluindo stock, images que não precisamos)
2. `GET /categories/{category_id}` — nome da categoria (o produto so teria o ID da categoria)
3. `GET /products/123/reviews?limit=3` — reviews com dados do autor (ou mais uma requisicao por autor)

Com GraphQL, tudo veio em uma única requisicao, com exatamente os campos necessários.

---

## Exercício 6: Projetando Webhooks

Você esta construindo uma plataforma de cursos online. Quando um aluno conclui um curso, os seguintes sistemas precisam ser notificados:

- Sistema de certificados (gerar PDF do certificado)
- Sistema de email (enviar email de parabens)
- Sistema de gamificacao (adicionar pontos e badges)
- Sistema de analytics (registrar conclusão)
- Sistema de recomendacoes (sugerir próximo curso)

**a)** Desenhe o fluxo usando webhooks internos. Quem envia o webhook? Quais URLs cada sistema registra?

**Resposta esperada:**
O sistema de cursos (que detecta a conclusão) envia webhooks para cada sistema:
- POST https://certificados.interno/webhook/conclusão
- POST https://email.interno/webhook/conclusão
- POST https://gamificacao.interno/webhook/conclusão
- POST https://analytics.interno/webhook/conclusão
- POST https://recomendacoes.interno/webhook/conclusão

**b)** Quais problemas podem acontecer com essa abordagem? Liste pelo menos 3.

**Resposta esperada:**
1. Se o sistema de certificados estiver fora do ar, o webhook se perde (a menos que haja retry)
2. Se o webhook for enviado duas vezes (retry apos timeout), o aluno pode receber dois certificados
3. O sistema de cursos precisa conhecer todos os sistemas que querem ser notificados — acoplamento
4. Se um novo sistema precisar ser notificado, o sistema de cursos precisa ser alterado
5. Não ha garantia de ordem — o email pode chegar antes do certificado ser gerado

**c)** Qual alternativa seria melhor que webhooks para esse cenário? Por que?

**Resposta esperada:**
Filas com pub/sub. O sistema de cursos pública um evento "aluno_concluiu_curso" em um tópico. Cada sistema se inscreve no tópico e processa no seu ritmo. Vantagens: desacoplamento (o sistema de cursos não precisa conhecer os consumers), garantia de entrega (o broker guarda as mensagens), e facilidade de adicionar novos consumers sem alterar o producer.

---

## Exercício 7: Reflexao — A Tecnologia Certa para o Momento Certo

Escreva um paragrafo (5-8 frases) respondendo a seguinte pergunta:

"Por que não existe uma única tecnologia de integração que resolva todos os problemas?"

Considere em sua resposta:
- Os diferentes requisitos (performance, simplicidade, tempo real, volume de dados)
- Os diferentes contextos (comunicação interna vs externa, poucos vs muitos clientes)
- O trade-off entre complexidade e capacidade
- A evolução historica (por que novas tecnologias continuam surgindo)

**Resposta esperada (exemplo):**
Não existe uma tecnologia universal porque cada cenário tem requisitos diferentes e muitas vezes conflitantes. REST e simples e universal, mas não serve para tempo real. WebSocket e ótimo para tempo real, mas desperdicaria recursos em um CRUD simples. gRPC e rápido, mas difícil de debugar e inacessivel para navegadores. GraphQL e flexível, mas adiciona complexidade desnecessaria para APIs simples. Cada tecnologia faz trade-offs — ganha em um aspecto e perde em outro. Além disso, novos problemas surgem conforme a tecnologia evolui: quando apps mobile se popularizaram, o over-fetching do REST virou problema e GraphQL surgiu. Quando IA generativa apareceu, a necessidade de conectar agentes a ferramentas criou o MCP. A diversidade de tecnologias reflete a diversidade de problemas reais que precisam ser resolvidos.

---

[← Voltar ao conteúdo](cap11-mod05-outras-integracoes-conteudo.md)
