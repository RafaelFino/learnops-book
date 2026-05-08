# 11.4 — Exercícios: Filas e Mensageria

[← Voltar ao conteúdo: Filas e Mensageria](cap11-mod04-filas-mensageria-conteudo.md)

---

## Sobre os Exercícios

Estes exercícios são conceituais — não há código para executar. O objetivo é que você pratique o raciocínio sobre quando e como usar filas de mensagens, identifique padrões e projete soluções para problemas reais.

Para cada exercício, escreva sua resposta em um arquivo de texto ou no caderno. Depois, compare com as respostas comentadas no final.

---

## Exercício 1: Classificando Operações — Síncrono ou Fila?

Um aplicativo de delivery de comida (como iFood) precisa executar as seguintes operações quando um cliente faz um pedido. Para cada operação, classifique como **síncrona** (o cliente precisa esperar) ou **assíncrona via fila** (pode acontecer em background). Justifique cada escolha.

1. Verificar se o restaurante está aberto e aceita pedidos
2. Calcular o valor total do pedido (itens + taxa de entrega)
3. Processar o pagamento no cartão de crédito
4. Enviar notificação push para o restaurante
5. Enviar email de confirmação para o cliente
6. Encontrar um entregador disponível na região
7. Atualizar as estatísticas de vendas do restaurante
8. Verificar se o cliente tem cupom de desconto válido
9. Registrar o pedido no sistema de analytics
10. Enviar SMS para o cliente com o código de acompanhamento

---

## Exercício 2: Projetando Mensagens

Para cada cenário abaixo, projete a mensagem que seria enviada para a fila. Defina os headers e o body com campos relevantes. Use o formato JSON.

### Cenário A: Redimensionar Foto de Perfil

Um usuário fez upload de uma nova foto de perfil. A foto precisa ser redimensionada para 3 tamanhos: 32x32 (ícone), 128x128 (thumbnail) e 512x512 (perfil).

### Cenário B: Enviar Notificação de Promoção

Uma loja está fazendo uma promoção relâmpago de 2 horas. Precisa notificar todos os clientes que favoritaram produtos da categoria em promoção.

### Cenário C: Gerar Relatório Mensal

O gerente financeiro solicitou o relatório de vendas do mês de março de 2024, agrupado por região e categoria de produto.

---

## Exercício 3: Identificando Problemas

Análise cada situação e identifique o problema. Depois, proponha uma solução usando conceitos de mensageria.

### Situação A

Um e-commerce envia emails de confirmação de forma síncrona. Na Black Friday, o serviço de email ficou sobrecarregado e começou a responder em 10 segundos. Resultado: todos os pedidos passaram a demorar 10 segundos a mais para confirmar, e muitos clientes desistiram.

**Perguntas**: Qual é o problema fundamental? Como filas resolveriam? O que aconteceria na Black Friday com filas?

### Situação B

Um sistema de processamento de pagamentos usa uma fila, mas o consumer não verifica o `message_id`. Durante uma instabilidade de rede, o broker reenviou algumas mensagens. Resultado: 47 clientes foram cobrados duas vezes.

**Perguntas**: Qual conceito de mensageria foi ignorado? Como o consumer deveria funcionar? Qual garantia de entrega estava configurada?

### Situação C

Uma startup usa uma fila para processar uploads de vídeo. Um usuário enviou um arquivo corrompido que faz o consumer crashar toda vez que tenta processar. O consumer reinicia, pega a mesma mensagem, crasha de novo. Isso se repete indefinidamente, e nenhum outro vídeo é processado.

**Perguntas**: Como se chama esse tipo de mensagem? Qual mecanismo deveria estar configurado? Descreva o fluxo correto.

---

## Exercício 4: Point-to-Point vs Pub/Sub

Para cada cenário, decida se o padrão mais adequado é Point-to-Point ou Pub/Sub. Justifique e desenhe o diagrama de fluxo (pode ser em texto).

1. Um sistema bancário precisa processar transferências PIX. Cada transferência deve ser processada exatamente uma vez.

2. Quando um novo funcionário é cadastrado no sistema de RH, os seguintes sistemas precisam ser atualizados: folha de pagamento, controle de acesso (crachá), email corporativo, plano de saúde e sistema de ponto.

3. Uma plataforma de e-learning precisa gerar certificados em PDF para alunos que concluíram um curso. São 5.000 certificados para gerar.

4. Quando um sensor IoT detecta temperatura acima de 40 graus em um data center, os seguintes sistemas precisam reagir: sistema de refrigeração, painel de monitoramento, sistema de alertas (email + SMS) e sistema de log.

5. Um sistema de impressão recebe documentos para imprimir. Há 3 impressoras disponíveis que devem dividir o trabalho.

---

## Exercício 5: Garantias de Entrega

Para cada cenário, identifique qual garantia de entrega é mais adequada (At Most Once, At Least Once ou Exactly Once) e justifique.

1. Enviar métricas de uso de CPU para um dashboard de monitoramento (a cada 5 segundos)
2. Processar uma transferência bancária de R$ 10.000
3. Enviar notificação push informando que um amigo postou uma foto
4. Debitar pontos de fidelidade do cliente após uma compra
5. Registrar um clique em um anúncio para fins de cobrança do anunciante
6. Enviar um lembrete de consulta médica por SMS
7. Atualizar o cache de preços de produtos

---

## Exercício 6: Projetando um Sistema Completo

Uma universidade está criando um sistema de matrícula online. O sistema precisa lidar com o período de matrícula, quando milhares de alunos tentam se matricular ao mesmo tempo.

O fluxo de matrícula envolve:
1. Aluno seleciona as disciplinas desejadas
2. Sistema verifica se há vagas nas disciplinas
3. Sistema verifica se o aluno tem os pré-requisitos
4. Sistema verifica se não há conflito de horário
5. Sistema reserva a vaga na disciplina
6. Sistema gera o comprovante de matrícula em PDF
7. Sistema envia o comprovante por email
8. Sistema atualiza o quadro de vagas disponíveis
9. Sistema notifica o coordenador do curso
10. Sistema atualiza as estatísticas de matrícula

Projete a solução respondendo:

a) Quais operações são síncronas e quais vão para filas? Justifique cada uma.

b) Quais filas você criaria? Para cada fila, defina: nome, producer, consumer e conteúdo da mensagem.

c) O que acontece se 500 alunos tentarem se matricular na mesma disciplina que tem 30 vagas? Como o sistema garante que não matricula mais alunos do que vagas?

d) O que acontece se o serviço de email estiver fora do ar durante o período de matrícula?

e) Qual padrão de mensageria você usaria para a operação 8 (atualizar quadro de vagas)? E para a operação 9 (notificar coordenador)?

---

## Exercício 7: Análise de Trade-offs

Uma fintech está decidindo entre duas arquiteturas para seu sistema de processamento de boletos:

**Opção A — Tudo Síncrono**: quando um boleto é pago, o sistema processa o pagamento, atualiza o saldo do recebedor, envia notificação ao recebedor, gera comprovante e registra no extrato — tudo na mesma requisição. Tempo médio: 3 segundos.

**Opção B — Síncrono + Filas**: quando um boleto é pago, o sistema processa o pagamento e atualiza o saldo (síncrono, 500ms). Notificação, comprovante e extrato vão para filas e são processados em background.

Análise os trade-offs:

1. O que acontece com cada opção quando o serviço de notificação fica lento (5 segundos por notificação)?
2. O que acontece com cada opção quando o volume de boletos triplica em dia de vencimento?
3. Qual opção é mais simples de implementar e manter?
4. Qual opção oferece melhor experiência para o usuário?
5. Em qual opção é mais fácil adicionar um novo serviço (por exemplo, enviar SMS além de email)?

---

## Respostas Comentadas

### Exercício 1

1. **Síncrona** — o cliente precisa saber se o restaurante está aberto antes de fazer o pedido. Sem essa informação, o pedido não faz sentido.

2. **Síncrona** — o cliente precisa ver o valor total antes de confirmar. É informação essencial para a decisão de compra.

3. **Síncrona** — o cliente precisa saber se o pagamento foi aprovado. Se não foi, precisa tentar outro cartão ou forma de pagamento.

4. **Fila** — o restaurante será notificado de qualquer forma. Se a notificação demorar 5 segundos a mais, não afeta a experiência do cliente. Se o serviço de notificação estiver fora do ar, a mensagem fica na fila.

5. **Fila** — o email de confirmação pode chegar 30 segundos depois. O cliente já viu a confirmação na tela. Se o serviço de email cair, os emails são enviados quando voltar.

6. **Depende** — pode ser síncrona (o cliente espera ver "entregador a caminho") ou assíncrona (o cliente vê "buscando entregador" e recebe notificação quando encontrar). A maioria dos apps usa uma abordagem híbrida: responde rápido com "pedido confirmado" e busca o entregador em background.

7. **Fila** — estatísticas não são urgentes. Podem ser atualizadas minutos depois sem nenhum impacto.

8. **Síncrona** — o desconto precisa ser aplicado antes de calcular o total. O cliente precisa ver o preço com desconto antes de confirmar.

9. **Fila** — analytics é processamento em background por definição. Não afeta a experiência do cliente.

10. **Fila** — o SMS pode chegar alguns segundos depois. O cliente já tem a confirmação na tela do app.

### Exercício 2

#### Cenário A — Redimensionar Foto

```json
{
  "headers": {
    "message_id": "msg-img-2024-001",
    "timestamp": "2024-03-15T10:30:00Z",
    "source": "user-service",
    "type": "resize_profile_photo",
    "priority": "normal",
    "retry_count": 0
  },
  "body": {
    "user_id": "USR-12345",
    "original_path": "/uploads/profiles/USR-12345/original.jpg",
    "sizes": [
      {"name": "icon", "width": 32, "height": 32},
      {"name": "thumbnail", "width": 128, "height": 128},
      {"name": "profile", "width": 512, "height": 512}
    ],
    "output_path": "/uploads/profiles/USR-12345/"
  }
}
```

#### Cenário B — Notificação de Promoção

```json
{
  "headers": {
    "message_id": "msg-promo-2024-bf-001",
    "timestamp": "2024-11-29T08:00:00Z",
    "source": "marketing-service",
    "type": "send_promotion_notification",
    "priority": "high",
    "retry_count": 0
  },
  "body": {
    "promotion_id": "PROMO-BF-2024",
    "category": "eletronicos",
    "discount_percent": 30,
    "expires_at": "2024-11-29T10:00:00Z",
    "target_customers": "favorited_category_eletronicos",
    "notification_channels": ["push", "email"],
    "message_template": "flash_sale"
  }
}
```

#### Cenário C — Relatório Mensal

```json
{
  "headers": {
    "message_id": "msg-report-2024-mar-001",
    "timestamp": "2024-04-01T09:15:00Z",
    "source": "finance-dashboard",
    "type": "generate_monthly_report",
    "priority": "normal",
    "retry_count": 0
  },
  "body": {
    "report_type": "monthly_sales",
    "period": {"month": 3, "year": 2024},
    "group_by": ["region", "product_category"],
    "format": "pdf",
    "requested_by": "gerente-financeiro",
    "delivery_email": "[email]"
  }
}
```

### Exercício 3

#### Situação A

**Problema fundamental**: operação não-crítica (email) no caminho crítico (confirmação do pedido). O serviço de email sendo síncrono significa que sua lentidão afeta diretamente a experiência de compra.

**Solução com filas**: o serviço de pedidos coloca a mensagem "enviar email de confirmação" na fila e responde ao cliente imediatamente. O serviço de email processa as mensagens no seu ritmo.

**Na Black Friday com filas**: os pedidos continuam sendo confirmados em milissegundos. A fila de emails cresce (pode acumular milhares de mensagens), mas os emails são enviados conforme o serviço consegue processar. O cliente recebe o email alguns minutos depois em vez de instantaneamente — mas o pedido foi confirmado sem atraso.

#### Situação B

**Conceito ignorado**: idempotência. O consumer deveria verificar o `message_id` antes de processar para evitar cobranças duplicadas.

**Consumer correto**: antes de processar o pagamento, verificar em um banco de dados se já existe um registro com aquele `message_id`. Se existir, ignorar a mensagem (já foi processada). Se não existir, processar e registrar o `message_id`.

**Garantia de entrega**: At Least Once — mensagens podem ser entregues mais de uma vez, mas não se perdem. O problema não é a garantia em si, mas a falta de idempotência no consumer.

#### Situação C

**Tipo de mensagem**: Poison Message (mensagem envenenada) — uma mensagem com dados inválidos que causa falha em qualquer consumer que tente processá-la.

**Mecanismo necessário**: Dead Letter Queue (DLQ) com limite de retries. Após N tentativas (por exemplo, 3), a mensagem é movida para a DLQ e para de bloquear a fila principal.

**Fluxo correto**: Consumer tenta processar → falha → mensagem volta para a fila (retry_count = 1) → consumer tenta de novo → falha (retry_count = 2) → tenta de novo → falha (retry_count = 3) → limite excedido → mensagem vai para a DLQ → desenvolvedor investiga → outros vídeos voltam a ser processados normalmente.

### Exercício 4

1. **Point-to-Point** — cada transferência PIX deve ser processada exatamente uma vez por um worker. Múltiplos workers podem dividir o trabalho, mas cada transferência vai para apenas um.

2. **Pub/Sub** — o evento "funcionário cadastrado" precisa ser recebido por 5 sistemas diferentes. Cada um reage de forma independente. Se amanhã adicionar um sexto sistema (por exemplo, sistema de treinamento), basta inscrevê-lo no tópico.

3. **Point-to-Point** — cada certificado é uma tarefa independente que precisa ser executada uma vez. Múltiplos workers podem gerar certificados em paralelo, cada um pegando da fila.

4. **Pub/Sub** — o evento "temperatura crítica" precisa ser recebido por 4 sistemas diferentes que reagem de formas independentes. Todos precisam saber, não apenas um.

5. **Point-to-Point** — cada documento é uma tarefa que vai para uma impressora. As 3 impressoras são consumers que dividem o trabalho da fila.

### Exercício 5

1. **At Most Once** — métricas de CPU chegam a cada 5 segundos. Se uma se perder, a próxima chega em 5 segundos. Duplicar métricas pode distorcer gráficos.

2. **Exactly Once** — transferência bancária não pode se perder (cliente perde dinheiro) nem duplicar (banco perde dinheiro). Requer o nível mais alto de garantia.

3. **At Most Once** — se a notificação se perder, o usuário não vê. Chato, mas não catastrófico. Duplicar notificações é mais irritante que perder uma.

4. **At Least Once com idempotência** — debitar pontos não pode se perder (cliente reclama), mas duplicar seria ruim (cliente perde pontos extras). At Least Once garante que não perde, e idempotência evita duplicação.

5. **Exactly Once** — cliques em anúncios geram cobrança. Perder um clique = anunciante não paga. Duplicar = anunciante paga a mais. Ambos são problemas financeiros.

6. **At Least Once** — o lembrete não pode se perder (paciente perde a consulta). Se enviar dois SMS, é redundante mas não prejudicial.

7. **At Most Once** — cache de preços é atualizado frequentemente. Se uma atualização se perder, a próxima corrige. Duplicar não causa problema (atualiza com o mesmo valor).

### Exercício 6

a) **Síncronas**: operações 1-5 (registrar, verificar vagas, verificar pré-requisitos, verificar conflito, reservar vaga). O aluno precisa saber imediatamente se conseguiu a matrícula.

**Filas**: operações 6-10 (gerar PDF, enviar email, atualizar quadro, notificar coordenador, atualizar estatísticas). Nenhuma dessas é necessária para confirmar a matrícula ao aluno.

b) Filas sugeridas:
- `enrollment_pdf_queue`: producer = serviço de matrícula, consumer = serviço de documentos, conteúdo = dados do aluno + disciplinas matriculadas
- `enrollment_email_queue`: producer = serviço de matrícula, consumer = serviço de email, conteúdo = email do aluno + link para comprovante
- `enrollment_events` (tópico pub/sub): producer = serviço de matrícula, consumers = serviço de quadro de vagas + serviço de notificação do coordenador + serviço de analytics

c) A verificação de vagas (operação 2) e a reserva (operação 5) devem ser atômicas — verificar e reservar na mesma transação do banco de dados. Isso garante que se dois alunos tentarem a última vaga ao mesmo tempo, apenas um consegue. O outro recebe "sem vagas" imediatamente.

d) As matrículas continuam funcionando normalmente. Os emails de comprovante ficam na fila. Quando o serviço de email voltar, todos os comprovantes são enviados. O aluno vê a confirmação na tela e recebe o email depois.

e) Operação 8 (atualizar quadro): **Pub/Sub** — o evento "matrícula realizada" é publicado e o serviço de quadro de vagas se inscreve para atualizar em tempo real. Operação 9 (notificar coordenador): **Pub/Sub** — o mesmo evento pode ser consumido pelo serviço de notificação do coordenador. Ambos reagem ao mesmo evento de forma independente.

### Exercício 7

1. **Opção A**: todos os pagamentos ficam lentos (3s + 5s = 8s por boleto). Fila de espera cresce. **Opção B**: pagamentos continuam em 500ms. Notificações acumulam na fila e são enviadas quando o serviço normalizar.

2. **Opção A**: tempo de processamento se mantém em 3s por boleto, mas o volume triplica. Se o sistema não escalar, forma fila de espera. **Opção B**: o caminho crítico (500ms) escala mais facilmente. As filas absorvem o pico de notificações e comprovantes.

3. **Opção A** é mais simples — um único fluxo sequencial, sem filas para configurar e monitorar. **Opção B** requer configurar broker, filas, consumers, monitoramento, DLQ. Mais complexa, mas mais robusta.

4. **Opção B** — o usuário vê "boleto pago" em 500ms em vez de 3 segundos. A experiência é significativamente melhor, especialmente em dispositivos móveis com conexão lenta.

5. **Opção B** — basta criar um novo consumer que se inscreve na fila de notificações (ou no tópico, se usar pub/sub). **Opção A** requer alterar o código do fluxo principal para adicionar a chamada ao serviço de SMS, aumentando o tempo de resposta.

---

[← Voltar ao conteúdo: Filas e Mensageria](cap11-mod04-filas-mensageria-conteudo.md)
