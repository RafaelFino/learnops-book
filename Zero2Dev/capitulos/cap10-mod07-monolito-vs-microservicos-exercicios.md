# Exercícios — Módulo 10.7: Monolito vs Microserviços

[← Voltar ao Módulo 10.7](cap10-mod07-monolito-vs-microservicos-conteudo.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção — cada cenário tem detalhes importantes
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho, escrevendo sua resposta em um arquivo de texto
> 4. Use a Proposta de Teste para verificar se sua resposta está completa
> 5. Só depois consulte a Resposta Comentada

> **Importante:** Estes exercícios são conceituais — não há código para executar. O objetivo é desenvolver seu pensamento crítico sobre decisões de arquitetura. Escreva suas respostas como se estivesse explicando para um colega de trabalho.

---

## Exercício 1 — Análise de Cenário: Escolhendo a Arquitetura — Nível: Básico

### Enunciado

Para cada cenário abaixo, decida se a melhor escolha é monolito, microserviços ou monolito modular. Justifique sua decisão com pelo menos 3 argumentos.

**Cenário A:** Uma ONG precisa de um sistema para gerenciar doações, voluntários e eventos. O time tem 2 desenvolvedores voluntários que trabalham nos fins de semana. O sistema vai atender cerca de 200 usuários.

**Cenário B:** Uma fintech com 80 desenvolvedores divididos em 12 times precisa construir uma plataforma de investimentos. O sistema precisa processar milhares de transações por segundo, com requisitos rigorosos de segurança e compliance. Diferentes partes do sistema têm requisitos técnicos muito diferentes (processamento financeiro, analytics, notificações).

**Cenário C:** Uma empresa de médio porte com 12 desenvolvedores está construindo um ERP (sistema de gestão empresarial) com módulos de vendas, estoque, financeiro e RH. O sistema vai atender 500 usuários internos.

### Dicas

- Considere o tamanho do time, o orçamento, a complexidade do domínio e os requisitos de escala
- Lembre da regra prática: "comece com monolito, migre quando o problema exigir"
- Pense no custo operacional de cada abordagem para o contexto específico
- Não existe resposta "certa" absoluta — o importante é a justificativa

### Proposta de Teste

- Cada cenário deve ter uma escolha clara (monolito, microserviços ou monolito modular)
- Cada escolha deve ter pelo menos 3 argumentos que se conectam com o cenário específico
- Os argumentos não devem ser genéricos ("microserviços são melhores") — devem referenciar detalhes do cenário

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Cenário A: Monolito.** (1) O time tem apenas 2 desenvolvedores voluntários — não há necessidade de autonomia de times nem capacidade de manter infraestrutura complexa. (2) O sistema atende 200 usuários — escala independente é desnecessária. (3) O orçamento é limitado (ONG com voluntários) — o custo de infraestrutura de microserviços não se justifica. (4) A simplicidade do monolito permite que os 2 desenvolvedores sejam produtivos rapidamente.

**Cenário B: Microserviços.** (1) 80 desenvolvedores em 12 times precisam de autonomia — deploy coordenado entre 12 times seria um gargalo enorme. (2) Requisitos técnicos muito diferentes (processamento financeiro vs analytics vs notificações) se beneficiam de stacks diferentes. (3) Milhares de transações por segundo exigem escala independente — o módulo de processamento precisa de muito mais recursos que o de notificações. (4) Isolamento de falhas é crítico em uma fintech — uma falha no analytics não pode afetar transações financeiras.

**Cenário C: Monolito modular.** (1) 12 desenvolvedores é um time médio — grande demais para um monolito desorganizado, mas pequeno demais para justificar microserviços. (2) Os módulos (vendas, estoque, financeiro, RH) têm fronteiras claras de negócio — perfeito para modularização interna. (3) 500 usuários internos não exigem escala independente. (4) Se o sistema crescer no futuro, os módulos já estarão preparados para extração como microserviços.

---

## Exercício 2 — Análise SWOT Aplicada — Nível: Intermediário

### Enunciado

Uma startup de delivery de medicamentos está crescendo rápido. Hoje tem 8 desenvolvedores e um monolito em Python. O sistema gerência: catálogo de medicamentos, pedidos, entregas (com rastreamento GPS), pagamentos e notificações. O tráfego triplicou nos últimos 6 meses e o módulo de rastreamento de entregas consome 70% dos recursos do servidor.

Faça uma análise SWOT para duas opções:
1. Manter o monolito e investir em otimização
2. Extrair o módulo de rastreamento como microserviço

Para cada opção, liste pelo menos 2 itens em cada quadrante (Forças, Fraquezas, Oportunidades, Ameaças).

### Dicas

- Pense no contexto específico: 8 desenvolvedores, crescimento rápido, um módulo consumindo 70% dos recursos
- Forças e fraquezas são internas (características da abordagem)
- Oportunidades e ameaças são externas (dependem do contexto e do mercado)
- Considere o custo de cada opção vs o benefício

### Proposta de Teste

- Cada opção deve ter uma tabela SWOT completa (4 quadrantes)
- Cada quadrante deve ter pelo menos 2 itens
- Os itens devem ser específicos para o cenário (não genéricos)
- Ao final, indique qual opção você recomendaria e por quê

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Opção 1: Manter o monolito e otimizar**

| Quadrante | Itens |
|-----------|-------|
| Forcas | Time ja conhece o código. Sem custo de aprendizado de novas ferramentas. Deploy continua simples |
| Fraquezas | Otimização tem limite — se o trafego continuar triplicando, vai precisar escalar tudo junto. O módulo de rastreamento continua acoplado ao resto |
| Oportunidades | Pode investir em cache e otimização de queries para ganhar tempo. Pode modularizar internamente enquanto otimiza |
| Ameacas | Se o crescimento continuar, a otimização pode não ser suficiente. Risco de o sistema inteiro ficar lento por causa do rastreamento |

**Opção 2: Extrair rastreamento como microserviço**

| Quadrante | Itens |
|-----------|-------|
| Forcas | Rastreamento escala independentemente — resolve o problema dos 70% de recursos. Falha no rastreamento não derruba pedidos e pagamentos |
| Fraquezas | Time de 8 precisa aprender a lidar com comunicação entre servicos. Custo de infraestrutura aumenta. Complexidade de deploy aumenta |
| Oportunidades | Rastreamento pode usar tecnologia otimizada para GPS e tempo real. Abre caminho para extrair outros módulos no futuro se necessário |
| Ameacas | Se a extracao for mal feita, pode criar um monolito distribuido. Time pode perder produtividade durante a migração |

**Recomendação:** Extrair o rastreamento como microserviço. O módulo consome 70% dos recursos e o tráfego está triplicando — otimização sozinha não vai resolver. A extração de um único serviço é gerenciável para um time de 8 pessoas e resolve o problema mais urgente. O resto do sistema pode continuar como monolito.

---

## Exercício 3 — Identificando o Monolito Distribuído — Nível: Intermediário

### Enunciado

Uma empresa dividiu seu sistema em 5 microserviços. Análise a descrição abaixo e identifique os sinais de que isso é, na verdade, um monolito distribuído. Para cada sinal, explique por que é um problema e sugira como corrigir.

Descrição do sistema:
- Os 5 serviços compartilham o mesmo banco de dados PostgreSQL
- O serviço de Pedidos chama o serviço de Produtos de forma síncrona para verificar estoque, que por sua vez chama o serviço de Preços para obter o preço atualizado
- Quando o time de Clientes faz deploy, precisa avisar o time de Pedidos porque o formato do DTO de cliente mudou
- Os 5 serviços usam uma biblioteca compartilhada com 200 classes, incluindo entidades de domínio, DTOs e utilitários
- O deploy dos 5 serviços é feito junto, toda sexta-feira, em uma janela de 2 horas

### Dicas

- Releia a seção sobre monolito distribuído no módulo
- Para cada item da descrição, pergunte: "isso aconteceria em microserviços bem projetados?"
- Pense em como cada problema viola o princípio de independência dos microserviços

### Proposta de Teste

- Identifique pelo menos 4 sinais de monolito distribuído
- Para cada sinal, explique o problema em 2-3 frases
- Para cada sinal, sugira uma correção concreta

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Sinal 1: Banco de dados compartilhado.** Microserviços devem ter bancos independentes. Compartilhar o banco cria acoplamento — uma mudança no schema de um serviço pode quebrar outro. Correção: cada serviço deve ter seu próprio banco (ou pelo menos seu próprio schema isolado).

**Sinal 2: Cadeia de chamadas síncronas.** Pedidos chama Produtos que chama Preços — são 3 serviços em cadeia. Se Preços cair, Produtos falha, e Pedidos falha. Isso é acoplamento temporal. Correção: o serviço de Pedidos deveria ter os dados que precisa localmente (cache ou réplica), ou usar comunicação assíncrona.

**Sinal 3: Deploy coordenado.** Se o time de Clientes precisa avisar o time de Pedidos antes do deploy, os serviços não são independentes. Correção: usar versionamento de API (v1, v2) para que mudanças no formato sejam retrocompatíveis. O serviço antigo continua funcionando enquanto os consumidores migram.

**Sinal 4: Biblioteca compartilhada com entidades de domínio.** Uma biblioteca com 200 classes compartilhadas cria acoplamento forte. Se a entidade Product muda na biblioteca, todos os 5 serviços precisam atualizar. Correção: cada serviço deve ter suas próprias entidades. Compartilhar apenas utilitários genéricos (logging, HTTP client), nunca entidades de domínio.

**Sinal 5: Deploy conjunto em janela fixa.** Deploy de todos os serviços juntos, toda sexta, é exatamente o que acontece em um monolito. Correção: cada serviço deve ter seu próprio pipeline de CI/CD e fazer deploy independentemente, quando estiver pronto.

**Conclusão:** Este sistema tem toda a complexidade de microserviços (rede, múltiplos deploys, múltiplos repositórios) sem nenhuma das vantagens (independência, escala, isolamento). Seria mais produtivo consolidar tudo em um monolito modular até que os problemas reais de escala e autonomia justifiquem a separação.

---

## Exercício 4 — Planejando uma Migração — Nível: Avançado

### Enunciado

Você trabalha em uma empresa de e-commerce com um monolito que tem os seguintes módulos: Catálogo, Busca, Carrinho, Pagamentos, Logística e Relatórios. O sistema atende 100 mil usuários por dia. O time cresceu para 30 desenvolvedores.

Os problemas atuais são:
- O módulo de Busca recebe 80% do tráfego mas não pode escalar independentemente
- O time de Pagamentos precisa fazer deploy urgente de uma correção de segurança, mas precisa esperar o deploy geral de sexta-feira
- O módulo de Relatórios roda queries pesadas que deixam o banco lento para todos os outros módulos

Proponha um plano de migração gradual. Defina:
1. Qual módulo extrair primeiro e por quê
2. Qual módulo extrair segundo e por quê
3. Quais módulos manter no monolito e por quê
4. Como os serviços extraídos vão se comunicar com o monolito

### Dicas

- Priorize pela dor: qual problema é mais urgente?
- Pense na independência de dados: qual módulo tem dados mais isolados?
- Considere o risco: qual extração é mais segura de fazer primeiro?
- Lembre que migração gradual significa extrair um serviço de cada vez

### Proposta de Teste

- O plano deve ter uma ordem clara de prioridade com justificativa
- Cada decisão deve referenciar os problemas listados no enunciado
- A comunicação entre serviços e monolito deve ser descrita (síncrona ou assíncrona)
- Deve explicar por que alguns módulos ficam no monolito

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**1. Extrair primeiro: Relatórios.** É a extração mais segura e resolve um problema crítico. Relatórios é um módulo de leitura que não afeta o fluxo principal de compra. Ao extraí-lo com seu próprio banco (réplica de leitura), as queries pesadas param de afetar o banco principal. Comunicação: o serviço de Relatórios lê de uma réplica do banco principal (comunicação assíncrona via replicação de dados).

**2. Extrair segundo: Busca.** Recebe 80% do tráfego e precisa escalar independentemente. A Busca pode usar tecnologia especializada (como Elasticsearch) que é mais eficiente para buscas do que o banco relacional do monolito. Comunicação: o monolito pública eventos quando produtos são criados ou atualizados (assíncrono), e o serviço de Busca indexa esses dados. As requisições de busca vão direto para o serviço de Busca (síncrono via API).

**3. Manter no monolito: Catálogo, Carrinho, Pagamentos e Logística.** Esses módulos estão fortemente interligados no fluxo de compra (catálogo → carrinho → pagamento → logística). Separá-los criaria muitas chamadas de rede no caminho crítico. O problema de deploy do time de Pagamentos pode ser resolvido com feature flags ou com modularização interna, sem precisar extrair como microserviço. Se no futuro o time crescer mais e a dor de deploy persistir, Pagamentos seria o próximo candidato a extração.

**4. Comunicação:** Relatórios usa réplica de banco (assíncrono). Busca recebe eventos do monolito via fila de mensagens (assíncrono) e responde buscas via API HTTP (síncrono). O monolito continua com comunicação interna por chamada de método.

---

## Exercício 5 — Debate: Defenda uma Posição — Nível: Avançado

### Enunciado

Escolha UMA das posições abaixo e escreva um texto de 10-15 linhas defendendo-a. Use argumentos técnicos, exemplos de empresas reais e dados concretos do módulo.

**Posição A:** "Para a maioria dos projetos de software, monolito é a melhor escolha e microserviços são over-engineering."

**Posição B:** "Microserviços são o futuro da engenharia de software e todo sistema deveria ser projetado para eventualmente migrar para microserviços."

Depois de escrever sua defesa, escreva 3-5 linhas com os **contra-argumentos** mais fortes contra a posição que você escolheu.

### Dicas

- Use exemplos reais: Shopify, Basecamp, Netflix, Amazon, iFood
- Cite dados concretos: tamanho de times, número de usuários, custos
- Não seja genérico — argumente com fatos
- Os contra-argumentos mostram que você entende os dois lados

### Proposta de Teste

- O texto de defesa deve ter 10-15 linhas com argumentos técnicos
- Deve citar pelo menos 2 exemplos de empresas reais
- Os contra-argumentos devem ser genuínos (não espantalhos fáceis de derrubar)
- O exercício demonstra pensamento crítico, não dogmatismo

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Não existe resposta "certa" — o importante é a qualidade da argumentação.

**Exemplo de defesa da Posição A:**

A maioria dos projetos de software não é a Netflix nem a Amazon. São sistemas internos, MVPs, aplicações de médio porte com times de 3 a 15 pessoas. Para esses projetos, monolito é objetivamente mais produtivo: menos infraestrutura, deploy mais simples, debug direto, transações ACID nativas. A Shopify atende milhões de lojas com um monolito modular em Rails. O Basecamp serve milhões de usuários com menos de 20 desenvolvedores e um monolito. O Stack Overflow, um dos sites mais acessados do mundo, roda em um monolito .NET com poucos servidores. Microserviços adicionam complexidade de rede, consistência eventual, distributed tracing, Kubernetes — ferramentas que custam dinheiro e exigem expertise que a maioria dos times não tem. Martin Fowler, que ajudou a definir microserviços, recomenda explicitamente "monolith first". O custo de over-engineering é real: times gastam mais tempo cuidando de infraestrutura do que escrevendo código de negócio.

**Contra-argumentos:** Quando o sistema cresce além de certo ponto (50+ desenvolvedores, milhões de requisições), o monolito se torna um gargalo real. Deploy coordenado entre muitos times desacelera todo mundo. E a impossibilidade de escalar partes independentemente desperdiça recursos e dinheiro em escala grande.

---

## Exercício 6 — Mapeando Fronteiras de Serviço — Nível: Avançado

### Enunciado

Você está projetando um sistema de gestão escolar com as seguintes funcionalidades:
- Cadastro de alunos e professores
- Matrícula em turmas
- Lançamento de notas e frequência
- Geração de boletins
- Comunicação com pais (mensagens e notificações)
- Biblioteca (empréstimo de livros)
- Financeiro (mensalidades e boletos)

Se esse sistema fosse dividido em microserviços, como você definiria as fronteiras? Agrupe as funcionalidades em serviços coesos. Para cada serviço proposto, defina: nome, funcionalidades que inclui, dados que possui e como se comunica com os outros serviços.

Depois, responda: esse sistema realmente precisa de microserviços? Justifique.

### Dicas

- Agrupe por capacidade de negócio, não por entidade de banco
- Pense em quais funcionalidades mudam juntas e quais mudam independentemente
- Considere quais partes têm requisitos de escala diferentes
- Lembre que menos serviços é geralmente melhor que mais serviços

### Proposta de Teste

- Defina entre 3 e 5 serviços (não mais — lembre do princípio de simplicidade)
- Cada serviço deve ter nome, funcionalidades, dados e comunicação definidos
- A resposta final sobre necessidade de microserviços deve ser justificada com argumentos do cenário

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Proposta de serviços:**

**1. Serviço Acadêmico** — Cadastro de alunos e professores, matrícula em turmas, lançamento de notas e frequência, geração de boletins. Dados: alunos, professores, turmas, notas, frequência. É o núcleo do sistema — tudo está fortemente relacionado.

**2. Serviço de Comunicação** — Mensagens para pais, notificações push, emails. Dados: mensagens, templates, preferências de notificação. Comunica-se com o Acadêmico para obter dados de alunos e eventos (nota lançada, falta registrada). Comunicação assíncrona via fila de mensagens.

**3. Serviço de Biblioteca** — Empréstimo de livros, catálogo, multas por atraso. Dados: livros, empréstimos, reservas. Comunica-se com o Acadêmico apenas para validar que o aluno existe. Comunicação síncrona via API.

**4. Serviço Financeiro** — Mensalidades, boletos, pagamentos, inadimplência. Dados: cobranças, pagamentos, planos. Comunica-se com o Acadêmico para saber quais alunos estão matriculados. Comunicação síncrona via API.

**Esse sistema precisa de microserviços?** Provavelmente não. Uma escola típica tem centenas ou poucos milhares de alunos. O time de desenvolvimento provavelmente é pequeno (3-8 pessoas). Não há requisitos de escala massiva. Um monolito modular com esses 4 módulos internos seria mais simples, mais barato e igualmente eficaz. Microserviços só fariam sentido se fosse uma plataforma SaaS atendendo milhares de escolas simultaneamente.

---

[← Voltar ao Módulo 10.7](cap10-mod07-monolito-vs-microservicos-conteudo.md)
