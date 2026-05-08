# Exercícios — Módulo 10.8: Arquiteturas Alternativas: Hexagonal e Clean Architecture

[← Voltar ao Módulo 10.8](cap10-mod08-arquiteturas-alternativas-conteudo.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção — cada cenário tem detalhes importantes
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho, escrevendo sua resposta em um arquivo de texto
> 4. Use a Proposta de Teste para verificar se sua resposta está completa
> 5. Só depois consulte a Resposta Comentada

> **Importante:** Estes exercícios são conceituais — não há código para executar. O objetivo é desenvolver seu pensamento crítico sobre decisões de arquitetura. Escreva suas respostas como se estivesse explicando para um colega de trabalho.

---

## Exercício 1 — Identificando a Arquitetura — Nível: Básico

### Enunciado

Análise as três estruturas de pastas abaixo e identifique qual arquitetura cada uma representa (3 camadas, hexagonal ou clean architecture). Justifique sua resposta apontando os elementos que te levaram à conclusão.

**Estrutura A:**

```
MeuApp/
    Controllers/
        OrderController.cs
    Services/
        OrderService.cs
    Repositories/
        OrderRepository.cs
    Models/
        Order.cs
    Program.cs
```

**Estrutura B:**

```
MeuApp/
    Domain/
        Models/
            Order.cs
        Ports/
            Inbound/
                IOrderService.cs
            Outbound/
                IOrderRepository.cs
                INotificationSender.cs
        Services/
            OrderService.cs
    Infrastructure/
        Adapters/
            Inbound/
                OrderHttpController.cs
                OrderQueueHandler.cs
            Outbound/
                PostgresOrderRepository.cs
                SmtpNotificationSender.cs
    Program.cs
```

**Estrutura C:**

```
MeuApp/
    Entities/
        Order.cs
    UseCases/
        CreateOrder.cs
        ListOrders.cs
        Interfaces/
            IOrderGateway.cs
    InterfaceAdapters/
        Controllers/
            OrderController.cs
        Gateways/
            SqlOrderGateway.cs
        Presenters/
            OrderPresenter.cs
    FrameworksAndDrivers/
        Web/
            WebServer.cs
        Database/
            DbConnection.cs
    Program.cs
```

### Dicas

- Observe os nomes das pastas — eles revelam a nomenclatura da arquitetura
- Conte a quantidade de arquivos e níveis de pasta — arquiteturas mais complexas têm mais
- Procure por "Ports", "Adapters", "UseCases", "Entities" — são palavras-chave
- Verifique onde as interfaces estão definidas — isso indica a direção das dependências

### Proposta de Teste

- Cada estrutura deve ser corretamente identificada
- A justificativa deve citar pelo menos 2 elementos específicos da estrutura
- Deve explicar a diferença entre as três de forma clara

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Estrutura A: 3 Camadas.** Elementos que indicam: (1) pastas nomeadas por camada — Controllers, Services, Repositories — que é a nomenclatura clássica de 3 camadas. (2) Estrutura simples e direta com poucos arquivos. (3) Não há separação entre domínio e infraestrutura — tudo está no mesmo nível.

**Estrutura B: Hexagonal (Ports and Adapters).** Elementos que indicam: (1) pasta `Domain/Ports/` com subpastas `Inbound` e `Outbound` — nomenclatura clássica de portas. (2) pasta `Infrastructure/Adapters/` com subpastas `Inbound` e `Outbound` — nomenclatura clássica de adaptadores. (3) Separação clara entre `Domain/` (centro) e `Infrastructure/` (borda). (4) Interfaces definidas dentro do domínio, não na infraestrutura. (5) Múltiplos adaptadores de entrada (HTTP e Queue) e saída (Postgres e SMTP).

**Estrutura C: Clean Architecture.** Elementos que indicam: (1) pastas nomeadas com a nomenclatura de Uncle Bob — `Entities`, `UseCases`, `InterfaceAdapters`, `FrameworksAndDrivers`. (2) Separação em 4 camadas concêntricas. (3) Use cases como classes individuais (`CreateOrder`, `ListOrders`) em vez de um service com múltiplos métodos. (4) Presença de `Presenters` — conceito específico da Clean Architecture.

---

## Exercício 2 — Análise de Cenário: Qual Arquitetura Usar — Nível: Básico

### Enunciado

Para cada cenário abaixo, recomende uma arquitetura (3 camadas, 3 camadas com interfaces, ou hexagonal) e justifique com pelo menos 3 argumentos.

**Cenário A:** Um desenvolvedor freelancer está construindo um sistema de agendamento de horários para um salão de beleza. O sistema tem 4 entidades (Cliente, Profissional, Serviço, Agendamento), regras simples e será usado por 1 salão com 5 profissionais.

**Cenário B:** Uma empresa de logística com 25 desenvolvedores está construindo um sistema de rastreamento de entregas. O sistema se integra com 8 transportadoras diferentes (cada uma com sua própria API), precisa ser acessado por API REST, aplicativo móvel e painel web, e tem regras complexas de cálculo de prazo e custo de frete que mudam frequentemente por causa de regulamentações.

**Cenário C:** Uma startup com 6 desenvolvedores está construindo um marketplace de serviços domésticos (como um "iFood de serviços"). O sistema tem 12 entidades, regras de negócio moderadas (matching de profissionais, cálculo de preço, avaliações) e precisa crescer rápido para validar o modelo de negócio.

### Dicas

- Considere: tamanho do time, complexidade do domínio, número de integrações, necessidade de trocar tecnologias
- Lembre da regra prática: "comece simples, evolua quando necessário"
- Pense no custo-benefício: a complexidade adicional se paga?
- Não existe resposta "errada" — o importante é a justificativa

### Proposta de Teste

- Cada cenário deve ter uma recomendação clara
- Cada recomendação deve ter pelo menos 3 argumentos conectados ao cenário
- Os argumentos devem ser específicos, não genéricos

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Cenário A: 3 Camadas.** (1) Um desenvolvedor sozinho — não há necessidade de isolamento rigoroso nem de facilitar trabalho em paralelo. (2) 4 entidades com regras simples — o domínio não justifica a complexidade de hexagonal. (3) Um único ponto de entrada (provavelmente web) — não há múltiplos canais que justifiquem adaptadores. (4) Velocidade de entrega é prioridade — o freelancer precisa entregar rápido, e 3 camadas é a forma mais rápida de organizar o código.

**Cenário B: Hexagonal.** (1) 8 integrações com transportadoras que podem mudar — adaptadores de saída facilitam trocar ou adicionar transportadoras sem mexer no domínio. (2) 3 canais de entrada (API REST, app móvel, painel web) — adaptadores de entrada permitem que todos usem as mesmas regras. (3) Regras complexas de frete que mudam frequentemente — domínio isolado facilita testar e modificar regras sem risco de quebrar integrações. (4) Time de 25 desenvolvedores — a curva de aprendizado da hexagonal é absorvível por um time desse tamanho.

**Cenário C: 3 Camadas com interfaces.** (1) Startup precisa validar rápido — hexagonal adicionaria complexidade que desacelera o desenvolvimento inicial. (2) Regras moderadas — não são simples o suficiente para ignorar interfaces, mas não são complexas o suficiente para justificar hexagonal completa. (3) 6 desenvolvedores — time pequeno que se beneficia de simplicidade. (4) Interfaces nos repositórios preparam para uma eventual migração para hexagonal se o domínio crescer em complexidade.

---

## Exercício 3 — Mapeando Ports e Adapters — Nível: Intermediário

### Enunciado

Você está projetando um sistema de reservas de hotel usando arquitetura hexagonal. O sistema precisa:

- Receber reservas via API REST e via integração com Booking.com
- Verificar disponibilidade de quartos
- Calcular preço (com regras de temporada, antecedência e tipo de quarto)
- Salvar reservas no banco de dados
- Enviar confirmação por email ao hóspede
- Notificar o sistema de limpeza quando uma reserva é confirmada

Para cada item, classifique como: porta de entrada, porta de saída, adaptador de entrada ou adaptador de saída. Depois, desenhe a estrutura de pastas completa do projeto.

### Dicas

- Portas são interfaces definidas pelo domínio
- Adaptadores são implementações concretas
- Pergunte: "quem inicia a ação?" — se é o mundo externo, é entrada. Se é o domínio que precisa de algo, é saída
- O domínio contém a lógica de verificar disponibilidade e calcular preço

### Proposta de Teste

- Cada item deve ser corretamente classificado
- A estrutura de pastas deve refletir a separação domínio/infraestrutura
- Deve haver pelo menos 2 adaptadores de entrada e 3 adaptadores de saída

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Classificação:**

| Item | Tipo | Justificativa |
|------|------|---------------|
| Receber reservas via API REST | Adaptador de entrada | Implementação concreta de como o mundo externo acessa o dominio |
| Receber reservas via Booking.com | Adaptador de entrada | Outra forma concreta de acessar o dominio |
| Interface para criar reserva | Porta de entrada | Interface que o dominio define e os adaptadores de entrada usam |
| Verificar disponibilidade | Lógica de dominio | Regra de negocio pura, fica dentro do dominio |
| Calcular preco | Lógica de dominio | Regra de negocio pura com regras de temporada e antecedencia |
| Interface para salvar reserva | Porta de saida | Interface que o dominio define para persistir dados |
| Salvar no banco de dados | Adaptador de saida | Implementação concreta da porta de saida usando banco |
| Interface para enviar notificacao | Porta de saida | Interface que o dominio define para enviar mensagens |
| Enviar email ao hospede | Adaptador de saida | Implementação concreta da porta de notificacao via email |
| Notificar sistema de limpeza | Adaptador de saida | Implementação concreta da porta de notificacao via integração |

**Estrutura de pastas:**

```
HotelReservation/
    Domain/
        Models/
            Reservation.cs
            Room.cs
            PriceCalculation.cs
        Ports/
            Inbound/
                IReservationService.cs
            Outbound/
                IReservationRepository.cs
                INotificationSender.cs
        Services/
            ReservationService.cs
            PriceCalculator.cs
            AvailabilityChecker.cs
    Infrastructure/
        Adapters/
            Inbound/
                RestReservationController.cs
                BookingComIntegration.cs
            Outbound/
                PostgresReservationRepository.cs
                SmtpEmailSender.cs
                CleaningSystemNotifier.cs
        Config/
            DependencyInjection.cs
    Program.cs
```

---

## Exercício 4 — Argumentando Contra o Hype — Nível: Intermediário

### Enunciado

Seu colega de trabalho leu o livro "Clean Architecture" e está empolgado. Ele quer refatorar o projeto atual — um sistema de controle de estoque com 6 entidades, regras simples e um time de 4 desenvolvedores — para usar Clean Architecture completa. Ele argumenta:

1. "Clean Architecture é o padrão da indústria, todo projeto sério usa"
2. "Se a gente precisar trocar o banco de dados no futuro, vai ser fácil"
3. "O código vai ficar mais organizado e profissional"
4. "Uncle Bob recomenda, então deve ser o certo"

Escreva uma resposta educada mas firme para cada argumento, explicando por que Clean Architecture pode não ser a melhor escolha para esse projeto específico. Use dados e argumentos do módulo.

### Dicas

- Seja respeitoso — o colega está tentando melhorar o projeto
- Use argumentos específicos do contexto (6 entidades, 4 devs, regras simples)
- Não diga que Clean Architecture é ruim — diga que não é a melhor escolha para esse contexto
- Proponha uma alternativa concreta

### Proposta de Teste

- Cada contra-argumento deve ser específico e respeitoso
- Deve referenciar o contexto do projeto (tamanho, complexidade, time)
- Deve propor uma alternativa concreta ao final
- Não deve ser dogmático ("Clean Architecture é ruim") — deve ser pragmático

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Contra-argumento 1:** "Clean Architecture é usada em alguns projetos enterprise, mas não é 'o padrão da indústria'. A maioria dos projetos profissionais usa 3 camadas — incluindo empresas como Shopify e Basecamp. O padrão da indústria é usar a arquitetura adequada ao problema. Para nosso sistema com 6 entidades e 4 devs, 3 camadas é o padrão adequado."

**Contra-argumento 2:** "Com que frequência trocamos de banco de dados? Nos últimos 3 anos, nunca. Se usarmos interfaces nos repositórios (como já fazemos), trocar o banco já é possível sem Clean Architecture. Construir toda uma arquitetura para facilitar algo que provavelmente nunca vai acontecer é investir tempo em flexibilidade que não vamos usar."

**Contra-argumento 3:** "Organização e profissionalismo não dependem da arquitetura — dependem de disciplina. Um projeto com 3 camadas bem organizadas, com nomes claros e responsabilidades definidas, é tão profissional quanto um com Clean Architecture. E é mais fácil de entender: qualquer dev novo entende 3 camadas em minutos. Clean Architecture pode levar dias."

**Contra-argumento 4:** "Uncle Bob criou Clean Architecture para resolver problemas de sistemas enterprise complexos. No próprio livro, ele fala sobre contexto e trade-offs. Aplicar a solução dele em um sistema simples é como usar um caminhão para ir ao supermercado — funciona, mas não é a ferramenta certa. O próprio Uncle Bob provavelmente recomendaria simplicidade para nosso caso."

**Alternativa proposta:** "Que tal a gente manter 3 camadas, garantir que todos os repositórios usam interfaces, e organizar bem as pastas? Se no futuro o domínio ficar mais complexo, a gente migra gradualmente para hexagonal — módulo por módulo. Assim a gente tem o benefício da simplicidade agora e a opção de evoluir depois."

---

## Exercício 5 — Comparando o Mesmo Fluxo — Nível: Avançado

### Enunciado

Considere a operação "cadastrar um novo cliente" com as seguintes regras de negócio:
- Nome é obrigatório e deve ter entre 3 e 100 caracteres
- Email é obrigatório e deve ser único no sistema
- Após cadastrar, enviar email de boas-vindas

Descreva o fluxo completo dessa operação em cada arquitetura, listando:
1. Quais classes/interfaces são envolvidas
2. A ordem das chamadas
3. Onde cada regra de negócio é verificada
4. Onde o email de boas-vindas é disparado

Faça para: (a) 3 camadas, (b) hexagonal.

Depois, conte o número total de classes/interfaces em cada abordagem e comente sobre o trade-off.

### Dicas

- Em 3 camadas: Controller → Service → Repository + EmailService
- Em hexagonal: Adapter HTTP → Port In → Domain Service → Port Out (Repository) + Port Out (Email) → Adapters
- As regras de negócio ficam no mesmo lugar em ambas — no Service/Domain
- A diferença está na organização e nas dependências

### Proposta de Teste

- Cada arquitetura deve ter o fluxo completo descrito
- Deve listar todas as classes e interfaces envolvidas
- Deve indicar onde cada regra é verificada
- A contagem de classes deve estar correta
- O comentário sobre trade-off deve ser equilibrado

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**(a) 3 Camadas:**

Classes/interfaces: `CustomerController`, `CustomerService`, `ICustomerRepository`, `SqlCustomerRepository`, `IEmailService`, `SmtpEmailService`, `Customer` — total: 7 (5 classes + 2 interfaces).

Fluxo:
1. `CustomerController` recebe nome e email do usuário
2. `CustomerController` chama `CustomerService.Register(name, email)`
3. `CustomerService` válida nome (3-100 caracteres) — regra de negócio
4. `CustomerService` chama `_repository.ExistsByEmail(email)` para verificar unicidade — regra de negócio
5. `CustomerService` cria objeto `Customer` e chama `_repository.Save(customer)`
6. `CustomerService` chama `_emailService.SendWelcome(email)` — disparo do email
7. `CustomerService` retorna resultado para `CustomerController`
8. `CustomerController` exibe resultado ao usuário

**(b) Hexagonal:**

Classes/interfaces: `CustomerHttpController` (adapter in), `ICustomerService` (port in), `CustomerService` (domain), `ICustomerRepository` (port out), `INotificationSender` (port out), `PostgresCustomerRepository` (adapter out), `SmtpNotificationSender` (adapter out), `Customer` (entity) — total: 8 (5 classes + 3 interfaces).

Fluxo:
1. `CustomerHttpController` (adapter de entrada) recebe nome e email
2. `CustomerHttpController` chama `ICustomerService.Register(name, email)` (porta de entrada)
3. `CustomerService` (domínio) válida nome (3-100 caracteres) — regra de negócio
4. `CustomerService` chama `ICustomerRepository.ExistsByEmail(email)` (porta de saída) — regra de negócio
5. `PostgresCustomerRepository` (adapter de saída) executa a query
6. `CustomerService` cria `Customer` e chama `ICustomerRepository.Save(customer)` (porta de saída)
7. `CustomerService` chama `INotificationSender.SendWelcome(email)` (porta de saída) — disparo do email
8. `SmtpNotificationSender` (adapter de saída) envia o email
9. Resultado volta pelo mesmo caminho até o `CustomerHttpController`

**Trade-off:** A hexagonal tem 1 classe e 1 interface a mais (8 vs 7). A diferença parece pequena, mas multiplique por 10 entidades e a hexagonal terá 10 classes e 10 interfaces a mais. A vantagem: na hexagonal, o domínio (`CustomerService`) não conhece PostgreSQL nem SMTP — ele só conhece interfaces. Se amanhã o email mudar de SMTP para SendGrid, só o adapter muda. Na 3 camadas, o Service já usa interface para o repository, mas o `IEmailService` pode estar definido fora do domínio, criando uma dependência sutil. Para este caso simples, a diferença prática é mínima. Para um sistema com 15 integrações externas, a diferença se torna significativa.

---

## Exercício 6 — Migração Gradual — Nível: Avançado

### Enunciado

Você tem um projeto em 3 camadas com a seguinte estrutura:

```
MeuProjeto/
    Controllers/
        ProductController.cs
        OrderController.cs
    Services/
        ProductService.cs
        OrderService.cs
    Repositories/
        IProductRepository.cs
        SqlProductRepository.cs
        IOrderRepository.cs
        SqlOrderRepository.cs
    Models/
        Product.cs
        Order.cs
    Program.cs
```

O módulo de pedidos (Order) ficou complexo: tem 15 regras de negócio, se integra com 3 serviços externos (pagamento, estoque, notificação) e precisa ser acessado por API REST e por uma fila de mensagens. O módulo de produtos (Product) continua simples.

Descreva passo a passo como você migraria **apenas o módulo de pedidos** para hexagonal, mantendo o módulo de produtos em 3 camadas. Mostre a estrutura de pastas final.

### Dicas

- Migre apenas o que precisa — o módulo de produtos fica como está
- Siga os passos descritos no módulo: mover interfaces, criar portas, reorganizar
- Pense em como os dois módulos coexistem na mesma aplicação
- A migração deve ser gradual — não reescreva tudo de uma vez

### Proposta de Teste

- Os passos devem ser claros e sequenciais
- A estrutura final deve mostrar Product em 3 camadas e Order em hexagonal
- Deve explicar como os dois módulos coexistem
- Deve ser uma migração realista (não reescrever do zero)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

**Passo 1: Criar a estrutura de domínio para Order.**
Criar pasta `Domain/Order/` com subpastas `Models/`, `Ports/Inbound/`, `Ports/Outbound/`, `Services/`.

**Passo 2: Mover o modelo Order.**
Mover `Models/Order.cs` para `Domain/Order/Models/Order.cs`.

**Passo 3: Mover e renomear interfaces de repositório.**
Mover `Repositories/IOrderRepository.cs` para `Domain/Order/Ports/Outbound/IOrderRepository.cs`.

**Passo 4: Criar portas de saída para integrações.**
Criar `Domain/Order/Ports/Outbound/IPaymentGateway.cs`, `IStockService.cs`, `INotificationSender.cs`.

**Passo 5: Criar porta de entrada.**
Criar `Domain/Order/Ports/Inbound/IOrderService.cs` extraindo a interface do `OrderService`.

**Passo 6: Mover o service para o domínio.**
Mover `Services/OrderService.cs` para `Domain/Order/Services/OrderService.cs`. Ajustar para implementar `IOrderService` e usar apenas as portas de saída.

**Passo 7: Criar adaptadores.**
Mover `Repositories/SqlOrderRepository.cs` para `Infrastructure/Adapters/Outbound/SqlOrderRepository.cs`. Mover `Controllers/OrderController.cs` para `Infrastructure/Adapters/Inbound/OrderHttpController.cs`. Criar `Infrastructure/Adapters/Inbound/OrderQueueHandler.cs` para a fila.

**Estrutura final:**

```
MeuProjeto/
    Controllers/
        ProductController.cs              # Product continua em 3 camadas
    Services/
        ProductService.cs                 # Product continua em 3 camadas
    Repositories/
        IProductRepository.cs             # Product continua em 3 camadas
        SqlProductRepository.cs           # Product continua em 3 camadas
    Models/
        Product.cs                        # Product continua em 3 camadas
    Domain/
        Order/
            Models/
                Order.cs                  # Entidade de dominio
            Ports/
                Inbound/
                    IOrderService.cs      # Porta de entrada
                Outbound/
                    IOrderRepository.cs   # Porta de saida
                    IPaymentGateway.cs    # Porta de saida
                    IStockService.cs      # Porta de saida
                    INotificationSender.cs # Porta de saida
            Services/
                OrderService.cs           # Logica de negocio
    Infrastructure/
        Adapters/
            Inbound/
                OrderHttpController.cs    # Adapter REST
                OrderQueueHandler.cs      # Adapter fila
            Outbound/
                SqlOrderRepository.cs     # Adapter banco
                StripePaymentGateway.cs   # Adapter pagamento
                HttpStockService.cs       # Adapter estoque
                SmtpNotificationSender.cs # Adapter notificacao
    Program.cs
```

Os dois módulos coexistem: Product usa a estrutura simples de 3 camadas, Order usa hexagonal. O `Program.cs` monta as dependências de ambos. Isso é perfeitamente válido e é a abordagem mais pragmática — complexidade apenas onde se justifica.

---

[← Voltar ao Módulo 10.8](cap10-mod08-arquiteturas-alternativas-conteudo.md)
