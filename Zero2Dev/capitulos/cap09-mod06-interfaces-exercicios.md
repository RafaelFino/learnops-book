# 9.6 — Exercícios: Interfaces

[← Voltar ao conteúdo: Interfaces](cap09-mod06-interfaces-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios praticam a criação e uso de interfaces em C#: definição de contratos, múltiplas implementações, polimorfismo via interface e desacoplamento. Execute cada exercício em um projeto C#.

---

## Exercício 1 — Interface de Notificação

Crie uma interface `INotifier` com o método `void Send(string recipient, string message)`.

Implemente três classes:
- `EmailNotifier` — imprime "Enviando email para {recipient}: {message}"
- `SmsNotifier` — imprime "Enviando SMS para {recipient}: {message}"
- `PushNotifier` — imprime "Enviando push para {recipient}: {message}"

Crie uma lista de `INotifier` com as três implementações e envie a mesma mensagem usando todas:

```csharp
List<INotifier> notifiers = new List<INotifier>
{
    new EmailNotifier(),
    new SmsNotifier(),
    new PushNotifier()
};

foreach (var n in notifiers)
{
    n.Send("maria@email.com", "Seu pedido foi enviado!");
}
```

Saída esperada:
```
Enviando email para maria@email.com: Seu pedido foi enviado!
Enviando SMS para maria@email.com: Seu pedido foi enviado!
Enviando push para maria@email.com: Seu pedido foi enviado!
```

---

## Exercício 2 — Interface de Forma Geométrica

Crie uma interface `IShape` com:
- `double CalculateArea()`
- `double CalculatePerimeter()`
- `string GetName()`

Implemente: `Circle` (raio), `Rectangle` (largura, altura), `Triangle` (base, altura, lado1, lado2, lado3).

Crie uma lista de `IShape`, calcule a área e perímetro de cada forma, e encontre a forma com maior área.

---

## Exercício 3 — Interface de Repositório

Crie uma interface `IProductRepository` com:
- `void Add(Product product)`
- `Product? GetById(int id)`
- `List<Product> GetAll()`
- `void Remove(int id)`

Implemente `InMemoryProductRepository` que armazena produtos em uma `List<Product>`.

Crie um programa que usa a interface (não a implementação concreta) para adicionar 5 produtos, listar todos, buscar por ID e remover um.

```csharp
// O programa usa a INTERFACE, não a classe concreta
IProductRepository repo = new InMemoryProductRepository();
repo.Add(new Product(1, "Notebook", 3500));
// ...
```

Este exercício prepara o terreno para o módulo 9.9 (Repository Pattern).

---

## Exercício 4 — Interface de Pagamento

Crie uma interface `IPaymentProcessor` com:
- `bool ProcessPayment(decimal amount)`
- `string GetPaymentMethod()`
- `decimal GetFee(decimal amount)` — taxa cobrada

Implemente:
- `CreditCardProcessor` — taxa de 2.5%, sempre aprova
- `PixProcessor` — taxa de 0%, sempre aprova
- `BoletoProcessor` — taxa de R$3.50 fixo, aprova se valor >= 10

Crie um programa que processa o mesmo pagamento com os três métodos e mostra a taxa de cada um.

---

## Exercício 5 — Múltiplas Interfaces

Crie duas interfaces:
- `IPrintable` com `void Print()`
- `IExportable` com `string ExportToText()`

Crie uma classe `Report` que implementa AMBAS as interfaces. O relatório tem título, data e conteúdo. `Print()` exibe no console, `ExportToText()` retorna uma string formatada.

Demonstre que o mesmo objeto pode ser tratado como `IPrintable` OU como `IExportable`:

```csharp
var report = new Report("Vendas Mensais", "Total: R$50.000");

IPrintable printable = report;
printable.Print();

IExportable exportable = report;
string text = exportable.ExportToText();
Console.WriteLine(text);
```

---

## Exercício 6 — Calculadora de Impostos

Crie uma interface `ITaxCalculator` com:
- `double CalculateTax(double value)`
- `string GetTaxName()`

Implemente:
- `IcmsCalculator` — 18% do valor
- `IssCalculator` — 5% do valor
- `IpiCalculator` — 12% do valor

Crie um método que recebe um valor e uma lista de `ITaxCalculator`, calcula cada imposto e mostra o total:

```csharp
// Saída esperada para valor = 1000:
// ICMS: R$180.00
// ISS: R$50.00
// IPI: R$120.00
// Total de impostos: R$350.00
// Valor final: R$1350.00
```

---

## Exercício 7 — Interface vs Classe Concreta

Explique com suas palavras:
1. Por que é melhor declarar variáveis como `IProductRepository repo` em vez de `InMemoryProductRepository repo`?
2. O que acontece se você precisar trocar de `InMemoryProductRepository` para `SqliteProductRepository`? Quantas linhas mudam em cada caso?
3. Como interfaces facilitam testes unitários?

---

## Exercício 8 — Comparação Python vs C#

Em Python, interfaces não existem formalmente — usamos "duck typing" (se anda como pato e faz quack como pato, é um pato). Em C#, interfaces são contratos explícitos.

Escreva um parágrafo comparando as duas abordagens. Qual é mais segura? Qual é mais flexível? Em qual cenário cada uma é melhor?

---

## Exercício 9 — Modelagem com Interfaces

Para um sistema de e-commerce, defina (apenas as assinaturas, sem implementar) as seguintes interfaces:
- `IOrderRepository` — operações de pedidos
- `IPaymentGateway` — processamento de pagamentos
- `IShippingService` — cálculo e rastreamento de frete
- `INotificationService` — envio de notificações

Para cada interface, defina 3-5 métodos que fariam sentido. Pense: quais operações cada serviço precisa oferecer?

---

## Exercício 10 — Reflexão

Responda: "Por que interfaces são consideradas o conceito mais importante da OOP para projetos grandes?" Use exemplos do módulo para justificar. Considere: desacoplamento, testabilidade, extensibilidade e trabalho em equipe.


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


---

[← Voltar ao conteúdo: Interfaces](cap09-mod06-interfaces-conteudo.md)
