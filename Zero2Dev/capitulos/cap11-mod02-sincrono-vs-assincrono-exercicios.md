# 11.2 — Exercícios: Síncrono vs Assíncrono

[← Voltar ao conteúdo](cap11-mod02-sincrono-vs-assincrono-conteudo.md)

---

## Sobre estes Exercícios

Estes exercícios consolidam a compreensão sobre comunicação síncrona e assíncrona. São conceituais — envolvem análise de cenários, classificação de operações e design de fluxos. A habilidade de decidir "síncrono ou assíncrono?" é uma das mais importantes na arquitetura de sistemas.

---

## Exercício 1: Classificação Rápida

Para cada operação abaixo, marque (S) para síncrono ou (A) para assíncrono. Justifique em uma frase.

1. Validar o CEP digitado pelo usuário no formulário de endereço
2. Enviar notificação push quando um amigo curtir sua foto
3. Verificar se o cupom de desconto é válido antes de aplicar
4. Gerar o PDF de um boleto bancário
5. Atualizar o ranking de vendedores após uma nova venda
6. Buscar os comentários de um post quando o usuário clica para ver
7. Processar a devolução de um produto comprado
8. Enviar SMS com código de verificação para login
9. Calcular o imposto sobre um produto no carrinho
10. Indexar um novo artigo para que apareça nas buscas
11. Verificar a idade do usuário antes de exibir conteúdo restrito
12. Sincronizar o catálogo de produtos com um marketplace externo

---

## Exercício 2: Redesenhando Fluxos

### Parte A: Sistema de Matrícula Universitária

O sistema atual é 100% síncrono:

1. Aluno seleciona disciplinas
2. Sistema verifica pré-requisitos de cada disciplina
3. Sistema verifica se há vagas em cada disciplina
4. Sistema calcula o valor da mensalidade
5. Sistema gera boleto de pagamento
6. Sistema envia email com o boleto
7. Sistema atualiza o quadro de horários do aluno
8. Sistema notifica os professores sobre novos alunos
9. Sistema atualiza as estatísticas de ocupação das turmas
10. Sistema responde ao aluno "matrícula confirmada"

Problema: no período de matrícula, milhares de alunos tentam se matricular ao mesmo tempo. O sistema fica extremamente lento porque cada matrícula executa todos os 10 passos sincronamente.

Sua tarefa:
- Identifique quais passos PRECISAM ser síncronos (o aluno está esperando)
- Identifique quais passos PODEM ser assíncronos
- Redesenhe o fluxo usando o padrão "síncrono na frente, assíncrono nos bastidores"
- Desenhe o diagrama de sequência do novo fluxo

### Parte B: Sistema de Streaming de Música

Quando o usuário dá play em uma música no app:

1. Verificar se o usuário tem assinatura ativa
2. Buscar os metadados da música (título, artista, capa)
3. Iniciar o streaming do áudio
4. Registrar no histórico de reprodução
5. Atualizar as recomendações baseado no gosto do usuário
6. Incrementar o contador de reproduções da música
7. Calcular royalties para o artista
8. Atualizar a playlist "Tocadas Recentemente"

Classifique cada passo e redesenhe o fluxo.

---

## Exercício 3: Análise de Falhas

Para cada cenário de falha, análise o impacto considerando comunicação síncrona vs assíncrona:

### Cenário A: Black Friday

Uma loja online está com promoção de Black Friday. O tráfego é 10x maior que o normal. O serviço de recomendações não aguenta a carga e começa a responder com timeout.

1. Se o serviço de recomendações é chamado sincronamente pela página de produtos, o que acontece?
2. Se o serviço de recomendações recebe eventos assíncronos, o que acontece?
3. Qual abordagem permite que a loja continue vendendo mesmo sem recomendações?

### Cenário B: Serviço de Email Instável

O serviço de email de uma empresa está com problemas intermitentes — funciona por 5 minutos, cai por 2 minutos, volta por 5 minutos.

1. Se os emails são enviados sincronamente (o serviço de pedidos chama o serviço de email e espera), o que acontece com os pedidos durante os 2 minutos de queda?
2. Se os emails são enviados via fila, o que acontece?
3. Qual abordagem garante que nenhum email se perde?

### Cenário C: Pico de Cadastros

Um app de delivery lançou uma promoção "primeira entrega grátis" e recebeu 50.000 cadastros em 1 hora (normalmente recebe 500/hora).

1. O serviço de cadastro precisa: validar dados, criar conta, enviar email de verificação, criar perfil, notificar equipe de marketing. Se tudo for síncrono, o que acontece?
2. Redesenhe o fluxo para suportar o pico sem degradar a experiência do usuário.

---

## Exercício 4: Fluxograma de Decisão

Crie seu próprio fluxograma de decisão para escolher entre síncrono e assíncrono. Use pelo menos 5 perguntas de decisão. Teste seu fluxograma com os seguintes cenários:

1. Verificar se um produto está em estoque
2. Enviar relatório mensal por email
3. Processar pagamento com cartão de crédito
4. Atualizar o feed de notícias de um usuário
5. Gerar thumbnail de uma imagem uploadada
6. Validar CPF em um formulário de cadastro

---

## Exercício 5: Consistência Eventual na Prática

Um sistema de e-commerce usa comunicação assíncrona para atualizar o estoque. Quando uma venda é feita, uma mensagem é enviada para a fila e o serviço de estoque processa quando puder.

Análise os seguintes cenários de consistência eventual:

1. O produto tem 1 unidade em estoque. Dois clientes tentam comprar ao mesmo tempo. O que pode acontecer com consistência eventual? Como resolver?

2. O cliente comprou um produto, mas o estoque ainda não foi atualizado (mensagem na fila). Outro cliente vê o produto como "disponível" e tenta comprar. O que acontece?

3. Quais operações deste e-commerce PRECISAM de consistência imediata e quais podem ter consistência eventual?

---

## Exercício 6: Projeto de Comunicação

Você está projetando o backend de um aplicativo de delivery de comida (similar ao iFood). O sistema tem os seguintes serviços:

- Serviço de Restaurantes (cardápio, horários, disponibilidade)
- Serviço de Pedidos (criar, acompanhar, cancelar pedidos)
- Serviço de Pagamento (processar pagamentos)
- Serviço de Entregadores (localização, disponibilidade, atribuição)
- Serviço de Notificações (push, SMS, email)
- Serviço de Avaliações (notas e comentários)
- Serviço de Promoções (cupons, descontos)

Para o fluxo "cliente faz um pedido":

1. Liste todas as comunicações necessárias entre serviços
2. Classifique cada uma como síncrona ou assíncrona
3. Desenhe o diagrama de sequência completo
4. Identifique os pontos de falha mais críticos
5. Proponha como o sistema deve se comportar se o serviço de notificações cair

---

## Gabarito Comentado

### Exercício 1 — Respostas

| # | Tipo | Justificativa |
|---|------|---------------|
| 1 | (S) | O usuario esta esperando a validação para continuar preenchendo o formulário |
| 2 | (A) | A notificacao pode chegar segundos depois, o usuario que curtiu não espera |
| 3 | (S) | O usuario precisa ver o desconto aplicado antes de confirmar a compra |
| 4 | (A) | O PDF pode ser gerado em background e enviado por email quando pronto |
| 5 | (A) | O ranking pode ser atualizado periodicamente, não precisa ser instantaneo |
| 6 | (S) | O usuario clicou e esta esperando ver os comentários na tela |
| 7 | (A) | A devolucao envolve multiplos passos que podem ser processados em background |
| 8 | (S) | O usuario esta na tela de login esperando o SMS para digitar o código |
| 9 | (S) | O usuario precisa ver o valor total com imposto antes de comprar |
| 10 | (A) | A indexacao pode levar minutos, o artigo ja foi publicado |
| 11 | (S) | A verificacao precisa acontecer antes de exibir o conteúdo |
| 12 | (A) | A sincronizacao pode acontecer periodicamente em background |

### Exercício 2A — Resposta Comentada

Passos que PRECISAM ser síncronos (o aluno está esperando):
- Verificar pré-requisitos (passos 2)
- Verificar vagas (passo 3)
- Calcular mensalidade (passo 4)

Passos que PODEM ser assíncronos:
- Gerar boleto (passo 5) — pode ser gerado em background e enviado por email
- Enviar email (passo 6) — claramente assíncrono
- Atualizar quadro de horários (passo 7) — pode ser atualizado em segundos via fila
- Notificar professores (passo 8) — assíncrono
- Atualizar estatísticas (passo 9) — assíncrono

Fluxo redesenhado: o aluno recebe "matrícula confirmada" após os passos 2, 3 e 4. Os passos 5-9 são disparados como mensagens assíncronas. Resultado: a matrícula que levava 10 segundos agora leva 2 segundos para o aluno, e o resto acontece em background.

### Exercício 3A — Resposta Comentada

1. Se as recomendações são chamadas sincronamente, a página de produtos fica lenta ou falha. O usuário vê erro ou espera 30 segundos para ver os produtos — mesmo que os produtos em si estejam disponíveis. A loja perde vendas porque o serviço de recomendações (que não é crítico para a compra) está derrubando a experiência.

2. Se as recomendações recebem eventos assíncronos, o serviço de recomendações fica com backlog na fila, mas a página de produtos funciona normalmente. O usuário vê os produtos sem recomendações personalizadas (pode mostrar "mais vendidos" como fallback).

3. A abordagem assíncrona permite que a loja continue vendendo. A regra é: serviços não-críticos nunca devem derrubar o caminho crítico. Recomendações são um "nice to have" — a compra funciona sem elas.

### Exercício 5.1 — Resposta Comentada

Com consistência eventual, ambos os clientes podem ver "1 unidade disponível" e ambos tentam comprar. Se a verificação de estoque for assíncrona, ambas as compras podem ser aceitas — resultando em venda de um produto que não existe (overselling).

Solução: a verificação de estoque PRECISA ser síncrona e atômica. Use uma operação que verifica e reserva ao mesmo tempo (check-and-reserve). Se o primeiro cliente reservou, o segundo recebe "indisponível". Essa é uma operação que exige consistência imediata — consistência eventual não é aceitável aqui.

---

[← Voltar ao conteúdo](cap11-mod02-sincrono-vs-assincrono-conteudo.md)
