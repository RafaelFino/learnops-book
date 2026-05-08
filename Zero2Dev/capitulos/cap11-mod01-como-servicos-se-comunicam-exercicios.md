# 11.1 — Exercícios: Como Serviços se Comunicam

[← Voltar ao conteúdo](cap11-mod01-como-servicos-se-comunicam-conteudo.md)

---

## Sobre estes Exercícios

Estes exercícios são conceituais — não envolvem código. O objetivo é consolidar sua compreensão sobre por que serviços precisam se comunicar, quais são as formas de comunicação e quando usar cada uma. Nos módulos seguintes, quando entrarmos em HTTP, REST e FastAPI, os exercícios serão práticos com código.

---

## Exercício 1: Identificando Serviços em Sistemas Reais

### Parte A: Spotify

Imagine que você é um engenheiro de software no Spotify. Quando um usuário abre o app e dá play em uma música, vários serviços trabalham juntos.

Liste pelo menos 6 serviços que você imagina que existem e, para cada um, responda:

1. Qual é a responsabilidade desse serviço?
2. Com quais outros serviços ele precisa se comunicar?
3. A comunicação é síncrona ou assíncrona? Por quê?

**Dica**: pense no que acontece passo a passo quando você abre o Spotify, busca uma música, dá play, e depois a música aparece no seu histórico e influencia suas recomendações.

### Parte B: WhatsApp

Agora pense no WhatsApp. Quando você envia uma mensagem para um grupo com 50 pessoas:

1. Quais serviços você imagina que estão envolvidos?
2. A entrega da mensagem para cada membro do grupo é síncrona ou assíncrona?
3. O que acontece se um dos membros do grupo estiver offline?
4. Como o sistema sabe que a mensagem foi entregue (dois tiques azuis)?

---

## Exercício 2: Classificando Comunicações

Para cada cenário abaixo, classifique como:
- **(S)** Síncrono — precisa esperar a resposta
- **(A)** Assíncrono — pode continuar sem esperar
- **(B)** Batch — processamento periódico

Justifique cada resposta em uma frase.

| # | Cenário | Tipo | Justificativa |
|---|---------|------|---------------|
| 1 | Verificar se o CPF do cliente e válido antes de aprovar um cadastro | | |
| 2 | Enviar email de boas-vindas apos o cadastro | | |
| 3 | Gerar relatório de vendas do mes anterior | | |
| 4 | Consultar o saldo da conta antes de fazer uma transferencia | | |
| 5 | Notificar 1 milhao de usuarios sobre uma promocao | | |
| 6 | Atualizar o cache de precos dos produtos | | |
| 7 | Processar o pagamento de um pedido | | |
| 8 | Redimensionar uma foto de perfil apos o upload | | |
| 9 | Verificar se o usuario tem permissão para acessar uma página | | |
| 10 | Importar dados de vendas de um sistema legado via arquivo CSV | | |

---

## Exercício 3: Telefonema, Carta ou Jornal?

Usando as analogias do módulo, classifique cada situação como Telefonema (síncrono direto), Carta (fila assíncrona) ou Jornal (evento assíncrono). Explique por quê.

1. O serviço de autenticação verifica se o token JWT é válido
2. O serviço de pedidos pública que um pedido foi cancelado, e os serviços de estoque, pagamento e notificação precisam reagir
3. O serviço de relatórios pede ao serviço de vendas os dados do último trimestre
4. O serviço de upload coloca uma tarefa na fila para o serviço de processamento de imagens redimensionar a foto
5. O serviço de monitoramento detecta que um servidor está com CPU alta e pública um alerta
6. O serviço de checkout pergunta ao serviço de frete quanto custa enviar para o CEP 01001-000

---

## Exercício 4: Desenhando Arquiteturas

### Parte A: Sistema de Biblioteca Online

Desenhe o diagrama de comunicação entre serviços para uma biblioteca online (como o Kindle ou Google Books). O sistema precisa:

- Permitir que o usuário busque livros por título ou autor
- Mostrar detalhes do livro (capa, sinopse, avaliações)
- Permitir compra ou aluguel do livro
- Processar o pagamento
- Liberar o acesso ao livro digital
- Enviar email de confirmação
- Atualizar as recomendações do usuário

Para cada comunicação entre serviços, indique se é síncrona ou assíncrona.

Use o formato Mermaid `sequenceDiagram` ou `flowchart` — ou desenhe no papel se preferir.

### Parte B: Sistema de Estacionamento Inteligente

Desenhe o diagrama para um estacionamento que usa câmeras para ler placas de carros:

- Câmera detecta um carro entrando e lê a placa
- Sistema verifica se o carro tem mensalidade ativa
- Se não tem, registra a entrada com horário
- Quando o carro sai, calcula o valor a pagar
- Processa o pagamento (pode ser automático via app)
- Envia recibo por email
- Atualiza o painel de vagas disponíveis em tempo real

---

## Exercício 5: Analisando Falhas

Para cada cenário de falha abaixo, explique:
- O que acontece com o sistema?
- Como a forma de comunicação (síncrona vs assíncrona) afeta o impacto da falha?
- O que poderia ser feito para minimizar o problema?

### Cenário A
O serviço de email está fora do ar. O serviço de pedidos acabou de confirmar uma compra e precisa enviar o email de confirmação.

- Se a comunicação for síncrona, o que acontece?
- Se a comunicação for assíncrona (via fila), o que acontece?
- Qual abordagem é melhor neste caso?

### Cenário B
O serviço de estoque está respondendo muito lentamente (5 segundos por requisição em vez dos habituais 100ms). O serviço de checkout precisa verificar o estoque antes de processar o pagamento.

- O que acontece com a experiência do usuário?
- O que acontece se muitos usuários tentarem comprar ao mesmo tempo?
- Que estratégias poderiam minimizar o impacto?

### Cenário C
O serviço de recomendação caiu completamente. O serviço de feed precisa montar a página inicial do usuário.

- O feed inteiro deve ficar indisponível porque as recomendações não funcionam?
- Como o sistema poderia continuar funcionando parcialmente?
- Qual a diferença entre um serviço "crítico" e um serviço "não-crítico"?

---

## Exercício 6: Comparando Abordagens

Uma empresa de e-commerce precisa implementar o envio de notificações para os clientes. Existem três opções:

**Opção A**: O serviço de pedidos chama o serviço de notificação de forma síncrona (HTTP direto) toda vez que um pedido muda de status.

**Opção B**: O serviço de pedidos coloca uma mensagem em uma fila toda vez que um pedido muda de status. O serviço de notificação consome as mensagens da fila.

**Opção C**: O serviço de pedidos pública um evento "status do pedido mudou". O serviço de notificação (e qualquer outro serviço interessado) se inscreve para receber esse evento.

Para cada opção, análise:

1. O que acontece se o serviço de notificação estiver fora do ar?
2. O que acontece se amanhã a empresa quiser que o serviço de analytics também saiba quando um pedido muda de status?
3. Qual é a mais simples de implementar?
4. Qual é a mais flexível para o futuro?
5. Qual você recomendaria e por quê?

---

## Exercício 7: Reflexão — Monolito vs Distribuído

Releia a seção "Quando Uma Aplicação Não é Suficiente" do módulo e responda:

1. O CRUD de produtos que você construiu no capítulo 8 precisaria ser dividido em microserviços? Por quê?
2. A partir de que ponto faria sentido dividir? Que sinais indicariam que é hora de separar?
3. Se você fosse dividir o CRUD em serviços separados, quais serviços criaria?
4. Quais problemas novos surgiriam com essa divisão que não existiam no monolito?

---

## Gabarito Comentado

### Exercício 2 — Respostas

| # | Tipo | Justificativa |
|---|------|---------------|
| 1 | (S) | O cadastro so pode ser aprovado se o CPF for válido - precisa da resposta |
| 2 | (A) | O usuario ja esta cadastrado, o email pode ser enviado em background |
| 3 | (B) | Relatório mensal não precisa ser em tempo real, pode ser processado periodicamente |
| 4 | (S) | A transferencia so pode acontecer se houver saldo - precisa da resposta |
| 5 | (A) | Notificar 1 milhao de pessoas não pode ser sincrono - levaria horas |
| 6 | (A) ou (B) | Cache pode ser atualizado periodicamente ou via evento quando precos mudam |
| 7 | (S) | O usuario esta esperando saber se o pagamento foi aprovado |
| 8 | (A) | O usuario não precisa esperar o redimensionamento - pode continuar usando o app |
| 9 | (S) | A página so pode ser exibida se o usuario tiver permissão - precisa da resposta |
| 10 | (B) | Importacao de arquivo e processamento periodico por definição |

### Exercício 3 — Respostas

1. **Telefonema** — verificação de token precisa de resposta imediata para liberar ou bloquear o acesso
2. **Jornal** — o serviço de pedidos pública o evento e múltiplos serviços reagem independentemente
3. **Telefonema** — o serviço de relatórios precisa dos dados para continuar gerando o relatório
4. **Carta** — a tarefa é enviada para uma fila específica, o processador de imagens pega quando puder
5. **Jornal** — o alerta é publicado e qualquer serviço interessado (dashboard, email, pager) pode reagir
6. **Telefonema** — o checkout precisa do valor do frete para mostrar o total ao usuário

### Exercício 5A — Resposta Comentada

Se a comunicação for síncrona: o serviço de pedidos tenta chamar o serviço de email, não consegue, e a confirmação do pedido falha — mesmo que o pagamento já tenha sido processado. O usuário vê um erro, fica preocupado, e pode tentar comprar de novo (gerando cobrança duplicada).

Se a comunicação for assíncrona: o serviço de pedidos coloca a mensagem "enviar email de confirmação" na fila e confirma o pedido normalmente. O usuário vê "pedido confirmado". Quando o serviço de email voltar, processa as mensagens pendentes e envia todos os emails atrasados.

A abordagem assíncrona é claramente melhor neste caso. O envio de email não é crítico para a operação de compra — o pedido existe independentemente do email. Usar comunicação síncrona para algo não-crítico é um erro de design comum.

---

[← Voltar ao conteúdo](cap11-mod01-como-servicos-se-comunicam-conteudo.md)
