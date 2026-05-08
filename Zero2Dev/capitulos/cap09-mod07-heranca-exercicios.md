# 9.7 — Exercícios: Herança e Polimorfismo

[← Voltar ao conteúdo: Herança e Polimorfismo](cap09-mod07-heranca-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios praticam herança, classes abstratas, override, polimorfismo e a decisão entre herança e composição em C#.

---

## Exercício 1 — Hierarquia de Veículos

Crie uma classe abstrata `Vehicle` com: Brand, Model, Year, CurrentSpeed. Métodos: `Accelerate(int amount)` (não pode ultrapassar velocidade máxima), `Brake(int amount)` (não pode ficar negativo), `abstract int GetMaxSpeed()`, `Display()`.

Derive:
- `Car` — velocidade máxima 200 km/h
- `Motorcycle` — velocidade máxima 250 km/h
- `Truck` — velocidade máxima 120 km/h

Crie uma lista polimórfica com 5 veículos, acelere todos em 100 km/h e exiba os resultados.

---

## Exercício 2 — Sistema de Funcionários

Crie uma classe abstrata `Employee` com: Name, BaseSalary. Método abstrato `decimal CalculateTotalSalary()`.

Derive:
- `FullTimeEmployee` — salário total = base + 30% de benefícios
- `PartTimeEmployee` — salário total = valor por hora x horas trabalhadas
- `Intern` — salário total = bolsa fixa (sem cálculo)

Crie 6 funcionários de tipos variados e calcule a folha de pagamento total.

---

## Exercício 3 — Formas Geométricas Expandidas

Expanda o exemplo de formas do módulo adicionando:
- `Square` que herda de `Rectangle` (largura == altura)
- `Ellipse` com semi-eixo maior e menor (área = PI * a * b)

Adicione todas as formas em uma lista e encontre a de maior e menor área.

---

## Exercício 4 — Animais com Comportamentos

Expanda a hierarquia de animais:
- Adicione `Bird` com método `Fly()`
- Adicione `Fish` com método `Swim()`
- Cada animal tem um som diferente (override de MakeSound)

Crie uma lista polimórfica e use o operador `is` para chamar métodos específicos de cada tipo.

---

## Exercício 5 — Contas Bancárias Expandidas

Adicione ao exemplo de contas bancárias:
- `InvestmentAccount` com taxa de rendimento mensal e método `ApplyMonthlyReturn()`
- Taxa mensal: R$30 se saldo < R$10.000, R$0 se >= R$10.000

Adicione à lista polimórfica e calcule o total de taxas.

---

## Exercício 6 — Media Player

Crie uma classe abstrata `MediaPlayer` com:
- `abstract void Play()`
- `void Stop()` (concreto — imprime "Parado")

Derive: `MusicPlayer`, `VideoPlayer`, `PodcastPlayer`. Cada um imprime uma mensagem diferente no `Play()`. Crie uma playlist polimórfica.

---

## Exercício 7 — Logger com Override

Crie `Logger` com método virtual `Log(string message)`. Derive:
- `TimestampLogger` — adiciona data/hora antes da mensagem (usa `base.Log()`)
- `ColorLogger` — adiciona "[INFO]", "[WARN]" ou "[ERROR]" antes da mensagem

Demonstre os três tipos.

---

## Exercício 8 — Composição vs Herança

Para cada cenário, diga se usaria herança ou composição e justifique:
1. `Smartphone` e `Tablet` compartilham funcionalidades de `Device`
2. `Car` tem um `Engine`
3. `ElectricCar` é um tipo especial de `Car`
4. `Order` tem uma lista de `OrderItem`
5. `Bird` e `Airplane` podem voar
6. `Student` e `Teacher` compartilham dados de `Person`

---

## Exercício 9 — Classe Abstrata vs Interface

Para cada cenário, diga se usaria classe abstrata ou interface:
1. Diferentes formas de pagamento (cartão, pix, boleto)
2. Diferentes tipos de conta bancária com código compartilhado
3. Objetos que podem ser serializados para JSON
4. Diferentes tipos de relatório com formatação base comum
5. Objetos que podem ser comparados entre si

---

## Exercício 10 — Projeto Mini: Sistema de Transporte

Crie um sistema com:
- Classe abstrata `Vehicle` (marca, modelo, capacidade de passageiros)
- Classes derivadas: `Bus`, `Taxi`, `Subway`
- Cada tipo calcula tarifa de forma diferente
- Classe `TransportSystem` que gerência uma frota de veículos
- Método que calcula a receita total da frota

Este exercício integra herança, polimorfismo, composição e encapsulamento.



---

## Exercicio 5 — Hierarquia de Formas Geometricas — Nivel: Intermediario

### Enunciado

Crie uma classe base `Shape` com metodo abstrato `CalculateArea()`. Implemente `Circle` (raio), `Rectangle` (largura, altura) e `Triangle` (base, altura). Crie uma lista de formas e calcule a area total.

### Dicas

1. `Shape` deve ser abstrata com `abstract double CalculateArea()`
2. Circulo: area = PI * raio * raio
3. Retangulo: area = largura * altura
4. Triangulo: area = base * altura / 2
5. Use `List<Shape>` para armazenar formas diferentes

### Proposta de Teste

- **Caso basico:** Circulo(5) + Retangulo(4,6) + Triangulo(3,8) -> area total correta
- **Caso de borda:** Formas com dimensao zero -> area = 0

---

## Exercicio 6 — Override de ToString — Nivel: Basico

### Enunciado

Adicione o metodo `override string ToString()` a cada forma do exercicio anterior. O ToString deve retornar uma descricao legivel, ex: "Circulo (raio=5, area=78.5)". Use `Console.WriteLine(forma)` para testar — o C# chama ToString automaticamente.

### Dicas

1. `override` indica que esta substituindo o metodo da classe base
2. Use interpolacao: `$"Circulo (raio={Radius}, area={CalculateArea():F1})"`
3. Teste com `Console.WriteLine(circle)` — deve imprimir a descricao

### Proposta de Teste

- **Caso basico:** `Console.WriteLine(new Circle(5))` -> "Circulo (raio=5, area=78.5)"


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


### Exercício Extra: Quando Herança NÃO é a Melhor Opção

Analise o cenário abaixo e explique por que herança seria problemática:

**Cenário:** Você tem `Pato` que voa e nada, `Pinguim` que nada mas não voa, e `Aviao` que voa mas não nada.

Se criar uma classe base `Voador` com método `Voar()`:
- `Pato` herda de `Voador` — OK
- `Pinguim` — não pode herdar de `Voador` (não voa)
- `Aviao` — herda de `Voador`, mas não é um animal

**Pergunta:** Como interfaces resolveriam esse problema melhor que herança?

**Resposta esperada:** Criar interfaces `IVoador` e `INadador`. `Pato` implementa ambas, `Pinguim` implementa apenas `INadador`, `Aviao` implementa apenas `IVoador`. Cada classe implementa apenas os comportamentos que realmente possui, sem herdar métodos que não fazem sentido.

### Erros Comuns com Herança

| Erro | Causa | Solução |
|------|-------|---------|
| Herança profunda demais | Mais de 3 níveis | Preferir composição ou interfaces |
| Classe base com lógica específica | Base sabe detalhes da filha | Mover para a classe filha |
| Override esquecido | Método da base executa em vez do esperado | Usar `override` explicitamente |
| Herança para reutilizar código | Herança é sobre "é um", não "tem um" | Usar composição para reutilização |

---

[← Voltar ao conteúdo: Herança e Polimorfismo](cap09-mod07-heranca-conteudo.md)
