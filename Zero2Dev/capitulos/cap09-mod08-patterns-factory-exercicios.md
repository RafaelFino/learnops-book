# 9.8 — Exercícios: Design Pattern Factory

[← Voltar ao conteúdo: Factory](cap09-mod08-patterns-factory-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios praticam o Factory Pattern: criação desacoplada de objetos, uso de interfaces com Factory, registro dinâmico e cenários reais de aplicação.

---

## Exercício 1 — Factory de Formas Geométricas

Crie uma interface `IShape` com `double CalculateArea()`, `double CalculatePerimeter()` e `string GetName()`. Implemente `Circle`, `Rectangle` e `Triangle`. Crie uma `ShapeFactory` que recebe o tipo como string e os parâmetros necessários. Demonstre criando 5 formas via Factory e calculando a área total.

---

## Exercício 2 — Factory de Exportação

Crie uma interface `IExporter` com `string Export(string title, List<string[]> rows)`. Implemente `CsvExporter` (gera CSV), `JsonExporter` (gera JSON simplificado) e `TextExporter` (gera texto formatado). Crie uma Factory e exporte os mesmos dados nos três formatos.

---

## Exercício 3 — Factory com Registro Dinâmico

Implemente uma versão do exercício 2 usando registro dinâmico (dicionário de `Func<IExporter>`). Adicione um quarto formato (Markdown) sem alterar a classe da Factory — apenas registrando.

---

## Exercício 4 — Factory de Calculadoras

Crie `ICalculator` com `double Calculate(double a, double b)` e `string GetSymbol()`. Implemente para +, -, *, /. Crie uma Factory que recebe o símbolo e retorna a calculadora. Faça um programa interativo que lê expressões do tipo "10 + 5" e calcula.

---

## Exercício 5 — Factory de Loggers

Crie `ILogger` com `void Log(string message)`. Implemente `ConsoleLogger`, `FileLogger` (simula arquivo) e `NullLogger` (não faz nada). Demonstre como trocar de logger muda o comportamento sem alterar o código da aplicação.

---

## Exercício 6 — Refatoração com Factory

Refatore o código abaixo para usar Factory:

```csharp
string tipo = "email";
if (tipo == "email") Console.WriteLine("Enviando email...");
else if (tipo == "sms") Console.WriteLine("Enviando SMS...");
else if (tipo == "push") Console.WriteLine("Enviando push...");
```

O código final deve ser: `var notifier = NotifierFactory.Create(tipo); notifier.Send("mensagem");`

---

## Exercício 7 — Factory + Composição

Crie `IPaymentProcessor` e `INotifier` com implementações variadas. Crie `OrderService` que recebe ambos via construtor. Use duas Factories para criar os componentes baseado em configuração. Demonstre que trocar implementações requer apenas mudar strings.

---

## Exercício 8 — Análise: Factory ou Over-engineering?

Para cada cenário, diga se Factory é necessário e justifique:
1. Sistema que sempre usa SQLite
2. Sistema com 5 formas de pagamento
3. Script de 50 linhas que imprime no console
4. API com múltiplos provedores de cloud
5. Jogo com 20 tipos de inimigos

---

## Exercício 9 — Factory e Testes

Explique como Factory facilita testes unitários usando o exemplo de banco de dados: como testar lógica sem banco real?

---

## Exercício 10 — Sistema de Relatórios Completo

Crie `IReportGenerator` com `GenerateHeader(title)`, `GenerateRow(data)`, `GenerateFooter()`. Implemente para HTML, Markdown e texto puro. Crie Factory e gere o mesmo relatório de vendas nos três formatos.


---

## Exercício 4 — Factory com Validação — Nível: Intermediário

### Enunciado

Crie uma `UserFactory` que cria objetos `User` com validação embutida. A factory deve:
- Gerar ID automaticamente (sequencial)
- Validar que o nome não está vazio
- Validar que o email contém "@"
- Definir a data de registro automaticamente como a data atual
- Lançar exceção com mensagem clara se os dados forem inválidos

### Dicas

1. Use um campo `static int _nextId` para gerar IDs sequenciais
2. Use `string.IsNullOrWhiteSpace()` para validar strings vazias
3. Use `email.Contains("@")` como validação simples de email
4. Use `DateTime.Now` para a data de registro
5. Lance `ArgumentException` com mensagem descritiva

### Proposta de Teste

- **Caso básico:** `UserFactory.Create("Maria", "maria@email.com")` → User com ID 1, nome "Maria", data de hoje
- **Caso de borda:** Nome vazio → `ArgumentException("Nome e obrigatorio")`
- **Caso de borda:** Email sem "@" → `ArgumentException("Email invalido")`

---

## Exercício 5 — Factory Method vs Simple Factory — Nível: Avançado

### Enunciado

Refatore o exercício 1 (VehicleFactory) para usar o padrão Factory Method em vez de Simple Factory:
- Crie uma classe abstrata `VehicleFactory` com método abstrato `CreateVehicle()`
- Crie `CarFactory`, `MotorcycleFactory` e `TruckFactory` que herdam de `VehicleFactory`
- Cada factory concreta cria seu tipo específico de veículo

Compare as duas abordagens: quando usar Simple Factory e quando usar Factory Method?

### Dicas

1. Simple Factory: uma classe com switch/if que decide qual objeto criar
2. Factory Method: cada tipo tem sua própria factory — sem switch/if
3. Factory Method é melhor quando novos tipos são adicionados frequentemente
4. Simple Factory é mais simples quando os tipos são fixos e poucos

### Proposta de Teste

- **Caso básico:** `new CarFactory().CreateVehicle()` → retorna objeto Car
- **Caso de comparação:** Adicionar um novo tipo (Bicycle) — quantas classes mudam em cada abordagem?

---

## Exercício 6 — Factory com Configuração — Nível: Avançado

### Enunciado

Crie uma `NotificationFactory` que cria diferentes tipos de notificação baseado em configuração:
- `EmailNotification` — envia por email (simula com `Console.WriteLine`)
- `SmsNotification` — envia por SMS
- `PushNotification` — envia push notification

A factory deve receber o tipo como string ("email", "sms", "push") e retornar a implementação correta. Todas devem implementar `INotification` com método `Send(string message, string recipient)`.

### Dicas

1. Defina `INotification` com `void Send(string message, string recipient)`
2. Cada implementação imprime uma mensagem diferente simulando o envio
3. A factory usa switch/match no tipo string para decidir qual criar
4. Considere o caso de tipo desconhecido — lance exceção

### Proposta de Teste

- **Caso básico:** `NotificationFactory.Create("email").Send("Ola", "user@mail.com")` → imprime "Enviando email para user@mail.com: Ola"
- **Caso de borda:** `NotificationFactory.Create("whatsapp")` → exceção "Tipo de notificacao desconhecido: whatsapp"


### Dicas Gerais para os Exercícios

- Comece pelo exercício mais simples e avance gradualmente
- Teste cada parte do código separadamente antes de juntar tudo
- Use `print()` para verificar valores intermediários quando algo não funcionar
- Releia o enunciado se o resultado não for o esperado — às vezes o problema está na interpretação
- Não tenha medo de errar — cada erro é uma oportunidade de aprender como Python funciona

### Tabela de Referência Rápida

| Conceito | Exemplo | Resultado |
|----------|---------|-----------|
| Criar variável | `x = 10` | x vale 10 |
| Ler entrada | `nome = input("Nome: ")` | Espera digitação |
| Converter para inteiro | `int("42")` | 42 |
| Converter para decimal | `float("3.14")` | 3.14 |
| Converter para texto | `str(42)` | "42" |
| Formatar com f-string | `f"Valor: {x}"` | "Valor: 10" |
| Formatar decimais | `f"{x:.2f}"` | "10.00" |


### Exercício Extra: Identificando Quando Usar Factory

Para cada cenário abaixo, responda: Factory é necessário ou é complexidade desnecessária?

| Cenário | Factory? | Justificativa |
|---------|----------|---------------|
| Criar um único tipo de relatório PDF | Não | Só existe um tipo, Factory não agrega valor |
| Criar notificações por email, SMS ou push | Sim | Múltiplos tipos com mesma interface, decisão em runtime |
| Criar conexão com banco de dados | Depende | Se só usa um banco, não. Se pode trocar (SQLite, PostgreSQL), sim |
| Criar objetos de teste vs produção | Sim | Factory permite trocar implementação sem mudar código |

### Sinais de que Você Precisa de Factory

- Código com muitos `if/else` ou `switch` para decidir qual classe instanciar
- Testes difíceis porque a criação de objetos está espalhada pelo código
- Necessidade de trocar implementação sem alterar quem usa o objeto
- Múltiplas classes que implementam a mesma interface

### Sinais de que Factory é Exagero

- Apenas um tipo de objeto é criado
- A criação é simples (`new Produto()`) sem lógica de decisão
- O código nunca vai precisar trocar a implementação

---

[← Voltar ao conteúdo: Factory](cap09-mod08-patterns-factory-conteudo.md)
