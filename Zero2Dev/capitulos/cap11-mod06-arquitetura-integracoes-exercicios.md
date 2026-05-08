# 11.6 — Exercícios: Arquitetura de Integracoes em Microservicos

[← Voltar ao conteúdo](cap11-mod06-arquitetura-integracoes-conteudo.md)

---

## Sobre estes Exercícios

Estes exercícios cobrem os padrões arquiteturais de integração apresentados no módulo 11.6: API Gateway, Service Discovery, Circuit Breaker, Retry, Idempotencia, Saga, Event-Driven Architecture e Observabilidade. O foco e em análise, decisao e projeto — habilidades que diferenciam um desenvolvedor junior de um pleno.

---

## Exercício 1: Mapeando Padrões para Problemas

Para cada problema descrito, identifique o padrão arquitetural mais adequado e explique por que:

**a)** O servico de recomendacoes esta fora do ar, e a página inicial do site mostra erro 500 para todos os usuarios, mesmo que as recomendacoes sejam apenas um detalhe da página.

**Resposta esperada:** Circuit Breaker com Fallback. O circuit breaker detecta que o servico de recomendacoes esta falhando e para de enviar requisicoes. O fallback mostra "produtos mais vendidos" (dados em cache) em vez de recomendacoes personalizadas. O usuario ve a página normalmente, sem perceber que um servico esta fora do ar.

**b)** Quando um usuario cancela uma assinatura, o sistema precisa: parar a cobranca recorrente, revogar acesso ao conteúdo premium, enviar email de confirmacao, atualizar metricas de churn, e oferecer desconto de retencao.

**Resposta esperada:** Event-Driven Architecture. O servico de assinaturas pública o evento "assinatura_cancelada". Cada servico interessado (pagamentos, acesso, email, analytics, retencao) se inscreve e processa independentemente. Isso desacopla os servicos — o servico de assinaturas não precisa conhecer todos os outros.

**c)** Um sistema de transferencia bancaria precisa debitar R$ 500 da conta A e creditar R$ 500 na conta B. As contas estao em servicos diferentes. Se o credito falhar, o debito precisa ser revertido.

**Resposta esperada:** Saga (orquestracao). Um orquestrador coordena: primeiro debita da conta A, depois credita na conta B. Se o credito falhar, executa a compensacao: credita de volta na conta A. Orquestracao e melhor que coreografia aqui porque o fluxo e critico e precisa de controle rigoroso.

**d)** Seu sistema tem 40 microservicos rodando em containers Docker. Quando um container e recriado, ele recebe um novo endereco IP. Os outros servicos precisam saber o novo endereco.

**Resposta esperada:** Service Discovery. Cada servico se registra no service discovery quando sobe e se desregistra quando para. Outros servicos consultam o registro para encontrar enderecos atualizados. Em Kubernetes, o DNS interno ja faz isso automaticamente.

**e)** Uma requisicao de um usuario esta demorando 8 segundos para responder. O sistema tem 12 microservicos e você não sabe qual deles esta causando a lentidao.

**Resposta esperada:** Distributed Tracing (Observabilidade). Com um trace ID propagado entre todos os servicos, você pode ver exatamente quanto tempo cada servico levou para processar sua parte. O servico com maior latencia e o gargalo.

---

## Exercício 2: Projetando Circuit Breaker

O servico de CEP (consulta de endereco por CEP) do seu e-commerce esta instavel — funciona por 10 minutos, cai por 2 minutos, volta por 10 minutos, e assim por diante.

**a)** Configure o circuit breaker para esse cenário. Defina:
- Quantas falhas consecutivas para abrir o circuito
- Quanto tempo ficar aberto antes de testar
- Quantas requisicoes de teste no estado meio-aberto

**Resposta esperada:**
- Limite de falhas: 5 falhas consecutivas (o servico cai por periodos, então 5 falhas seguidas indica que esta fora)
- Tempo aberto: 30 segundos (o servico volta em ~2 minutos, então testar a cada 30s e razoavel)
- Requisicoes de teste: 1 (uma única requisicao para verificar se voltou)

**b)** Qual fallback você implementaria quando o circuit breaker estiver aberto?

**Resposta esperada:**
Cache local dos ultimos CEPs consultados. Quando o servico de CEP esta fora, buscar no cache. Se o CEP não estiver no cache, mostrar "endereco sera confirmado em breve" e processar quando o servico voltar. Outra opcao: usar um servico de CEP alternativo (backup).

**c)** Desenhe o diagrama de estados do circuit breaker com os valores que você definiu.

**Resposta esperada:**
```
FECHADO → (5 falhas consecutivas) → ABERTO
ABERTO → (30 segundos) → MEIO-ABERTO
MEIO-ABERTO → (teste OK) → FECHADO
MEIO-ABERTO → (teste falhou) → ABERTO
```

---

## Exercício 3: Desenhando uma Saga

Você esta projetando o fluxo de matricula em uma universidade online. Quando um aluno se matricula em um curso, os seguintes passos precisam acontecer:

1. Servico de Matriculas: registrar a matricula
2. Servico de Vagas: reservar uma vaga no curso (cursos tem limite)
3. Servico Financeiro: gerar boleto ou cobrar cartao
4. Servico de Acesso: liberar acesso ao conteúdo do curso
5. Servico de Email: enviar email de boas-vindas com instruções

**a)** Desenhe o fluxo normal (tudo funciona).

**Resposta esperada:**
```
Matriculas: registrar matricula → OK
Vagas: reservar vaga → OK
Financeiro: cobrar pagamento → OK
Acesso: liberar conteudo → OK
Email: enviar boas-vindas → OK
```

**b)** Desenhe o fluxo de compensacao quando o pagamento falha (passo 3).

**Resposta esperada:**
```
Matriculas: registrar matricula → OK
Vagas: reservar vaga → OK
Financeiro: cobrar pagamento → FALHOU
--- Compensacao ---
Vagas: liberar vaga reservada
Matriculas: cancelar matricula
(Email nao precisa de compensacao — nao foi executado)
```

**c)** O que acontece se o Servico de Email falhar no passo 5? Precisa desfazer tudo?

**Resposta esperada:**
Não. O email e uma operação não-critica. Se falhar, a matricula, vaga, pagamento e acesso ja estao corretos. O email pode ser reenviado depois (retry assincrono). Não faz sentido cancelar uma matricula válida porque o email de boas-vindas não foi enviado. Isso mostra que nem toda falha exige compensacao — depende da criticidade da operação.

**d)** Você usaria coreografia ou orquestracao para essa saga? Justifique.

**Resposta esperada:**
Orquestracao. O fluxo tem dependências claras (não pode cobrar sem reservar vaga, não pode liberar acesso sem cobrar) e a compensacao precisa ser coordenada na ordem inversa. Um orquestrador central facilita o controle do fluxo e das compensacoes. Coreografia seria mais complexa porque cada servico precisaria saber qual e o próximo passo e como compensar.

---

## Exercício 4: Retry e Idempotencia

**a)** Calcule os tempos de espera para 6 tentativas com backoff exponencial (base 2 segundos):

| Tentativa | Espera | Tempo acumulado |
|-----------|--------|-----------------|
| 1 | ? | ? |
| 2 | ? | ? |
| 3 | ? | ? |
| 4 | ? | ? |
| 5 | ? | ? |
| 6 | ? | ? |

**Resposta esperada:**

| Tentativa | Espera | Tempo acumulado |
|-----------|--------|-----------------|
| 1 | 0s (imediata) | 0s |
| 2 | 2s | 2s |
| 3 | 4s | 6s |
| 4 | 8s | 14s |
| 5 | 16s | 30s |
| 6 | 32s | 62s |

**b)** Para cada operação, diga se e idempotente e por que:

1. `GET /products/123`
2. `POST /orders` (criar novo pedido)
3. `PUT /users/123` (atualizar usuario com dados completos)
4. `DELETE /comments/456`
5. `POST /payments` (processar pagamento)
6. `PATCH /products/123` (incrementar estoque em +1)

**Resposta esperada:**
1. Sim — ler dados não muda nada
2. Não — cada chamada cria um novo pedido
3. Sim — substituir com os mesmos dados produz o mesmo resultado
4. Sim — deletar algo ja deletado não muda nada (retorna 404 ou 204)
5. Não — cada chamada pode processar um novo pagamento
6. Não — cada chamada incrementa +1, então chamar 3 vezes adiciona 3

**c)** Como você tornaria a operação `POST /payments` idempotente?

**Resposta esperada:**
Adicionar um header `Idempotency-Key` com um UUID gerado pelo cliente. O servidor verifica se ja existe um pagamento com essa chave. Se sim, retorna o resultado anterior sem processar novamente. Se não, processa o pagamento e armazena o resultado associado a chave. Exemplo:
```
POST /payments
Idempotency-Key: 550e8400-e29b-41d4-a716-446655440000
Body: { "valor": 100, "destino": "loja-xyz" }
```

---

## Exercício 5: Arquitetura Completa

Você esta projetando um sistema de delivery de comida (como iFood). Os servicos são:

- API Gateway
- Servico de Restaurantes (catalogo, cardapio)
- Servico de Pedidos (criar, acompanhar pedidos)
- Servico de Pagamentos (cobrar cliente)
- Servico de Entregadores (encontrar entregador disponível)
- Servico de Rastreamento (posição do entregador em tempo real)
- Servico de Avaliacoes (notas e comentários)
- Servico de Notificacoes (push, email, SMS)
- Servico de Promocoes (cupons, descontos)

Para cada par de comunicação listado, defina: tecnologia (REST, gRPC, WebSocket, filas, eventos), padrão de resiliencia (circuit breaker, retry, fallback), e justificativa.

1. App do cliente → API Gateway → Servico de Restaurantes (buscar cardapio)
2. Servico de Pedidos → Servico de Pagamentos (cobrar)
3. Servico de Pedidos → Servico de Entregadores (encontrar entregador)
4. Servico de Rastreamento → App do cliente (posição do entregador)
5. Pedido entregue → Servico de Avaliacoes, Notificacoes, Promocoes

**Respostas esperadas:**

1. REST via Gateway. O cliente busca o cardapio — operação sincrona simples. Circuit breaker no gateway para proteger o servico de restaurantes. Fallback: cache do cardapio (cardapios não mudam a cada segundo).

2. gRPC com circuit breaker e idempotencia. Comunicação interna critica entre microservicos. gRPC para performance. Circuit breaker para evitar cascata se pagamentos falhar. Idempotency-Key para evitar cobranca dupla em caso de retry.

3. gRPC com circuit breaker e fallback. Encontrar entregador e sincrono (o pedido precisa de um entregador). Circuit breaker para proteger. Fallback: colocar pedido em fila de espera se não houver entregador disponível.

4. WebSocket. Posição do entregador atualiza em tempo real no mapa do cliente. WebSocket mantem conexão aberta para atualizacoes continuas sem polling.

5. Event-driven (pub/sub). O evento "pedido_entregue" e publicado uma vez. Avaliacoes, Notificacoes e Promocoes se inscrevem e processam independentemente. Desacoplamento total — adicionar um novo consumer não exige alterar o servico de pedidos.

---

## Exercício 6: As Falacias na Prática

Para cada falacia da computacao distribuida, de um exemplo concreto de bug ou problema que aconteceria se você assumisse que ela e verdadeira:

1. "A rede e confiavel"
2. "A latencia e zero"
3. "A banda e infinita"
4. "A rede e segura"

**Respostas esperadas:**

1. Você não implementa retry nem circuit breaker. Quando a rede falha (e vai falhar), seu sistema trava esperando respostas que nunca chegam, e o usuario ve uma tela de loading infinita.

2. Você faz 20 chamadas sincronas encadeadas (A chama B que chama C que chama D...). Cada chamada tem 50ms de latencia. Total: 1 segundo. O usuario espera 1 segundo por algo que deveria ser instantaneo. Se tivesse considerado a latencia, teria paralelizado as chamadas ou usado cache.

3. Você retorna todos os campos de todos os registros em cada requisicao (sem paginacao, sem seleção de campos). Com 10.000 usuarios fazendo isso simultaneamente, a banda satura e o sistema fica lento para todos.

4. Você transmite dados sensiveis (senhas, tokens, dados pessoais) sem criptografia (HTTP em vez de HTTPS). Qualquer pessoa na mesma rede pode interceptar esses dados.

---

## Exercício 7: Reflexao — Simplicidade vs Robustez

Escreva um paragrafo (5-8 frases) respondendo:

"Um desenvolvedor junior argumenta que implementar circuit breaker, retry, idempotencia e saga e 'over-engineering' para um projeto com 3 microservicos. Você concorda ou discorda? Justifique."

**Resposta esperada (exemplo):**
Depende do contexto. Para 3 microservicos em um projeto interno com poucos usuarios, implementar todos os padrões de uma vez pode ser over-engineering — a complexidade adicionada pode ser maior que o beneficio. Porém, alguns padrões são quase obrigatórios independente do tamanho: retry com backoff e essencial em qualquer chamada de rede, e idempotencia e critica em operações financeiras. Circuit breaker faz sentido assim que você tem chamadas entre servicos que podem falhar. Saga so e necessária quando você tem transações que abrangem multiplos servicos. A abordagem correta e comecar com o mínimo (retry + idempotencia), monitorar o sistema, e adicionar padrões conforme os problemas aparecem. O erro não e implementar demais — e não implementar o básico e descobrir na produção que precisava.

---

[← Voltar ao conteúdo](cap11-mod06-arquitetura-integracoes-conteudo.md)
