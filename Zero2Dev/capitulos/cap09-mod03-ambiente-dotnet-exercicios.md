# 9.3 — Exercícios: Ambiente .NET, Instalação e Primeiro Projeto

[← Voltar ao conteúdo: Ambiente .NET](cap09-mod03-ambiente-dotnet-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem tudo que você aprendeu no módulo 9.3: instalação do .NET SDK, uso do `dotnet` CLI, tipos básicos, entrada e saída, e a estrutura de um projeto C#. Cada exercício tem um nível de dificuldade indicado:

- ⭐ Básico — aplica diretamente o que foi ensinado
- ⭐⭐ Intermediário — combina conceitos ou exige adaptação
- ⭐⭐⭐ Desafio — exige pesquisa ou raciocínio extra

Para cada exercício, crie um projeto separado com `dotnet new console -n NomeDoExercicio`.

---

## Exercício 1 — Verificação do Ambiente ⭐

### Objetivo

Confirmar que o .NET SDK está instalado corretamente e que você consegue criar, compilar e executar um projeto.

### Instruções

1. Abra o terminal e execute:

```bash
# Verificar versao do SDK
dotnet --version

# Ver informacoes completas
dotnet --info

# Listar SDKs instalados
dotnet --list-sdks

# Listar runtimes instalados
dotnet --list-runtimes
```

2. Anote as seguintes informações:
   - Versão do SDK instalado
   - Sistema operacional detectado
   - Caminho de instalação do SDK

3. Crie um projeto de teste:

```bash
# Criar projeto
dotnet new console -n TesteAmbiente

# Entrar na pasta
cd TesteAmbiente

# Executar
dotnet run
```

4. Confirme que a saída é `Hello, World!`

5. Agora teste a compilação separada:

```bash
# Apenas compilar
dotnet build

# Verificar que a pasta bin/ foi criada
ls bin/Debug/net9.0/
```

### Resultado Esperado

Você deve ver a versão do SDK, conseguir criar e executar o projeto, e ver os arquivos compilados na pasta `bin/`.

### O que Entregar

Anote em um comentário no `Program.cs` a versão do SDK e o sistema operacional:

```csharp
// Ambiente verificado em: [data]
// SDK: [versao]
// SO: [sistema operacional]
// Tudo funcionando!
Console.WriteLine("Ambiente .NET configurado com sucesso!");
```

Saída esperada:
```
Ambiente .NET configurado com sucesso!
```

---

## Exercício 2 — Cartão de Apresentação ⭐

### Objetivo

Praticar `Console.ReadLine()`, `Console.WriteLine()`, interpolação de strings e conversão de tipos.

### Instruções

Crie um programa que peça ao usuário: nome, idade, cidade e profissão (ou "estudante"). Depois, exiba um cartão formatado.

```csharp
// Cartao de Apresentacao
// "name" = nome, "age" = idade, "city" = cidade, "job" = profissao

Console.WriteLine("=== Cadastro ===");

Console.Write("Nome: ");
string name = Console.ReadLine();

Console.Write("Idade: ");
int age = int.Parse(Console.ReadLine());

Console.Write("Cidade: ");
string city = Console.ReadLine();

Console.Write("Profissao (ou estudante): ");
string job = Console.ReadLine();

// Exibir o cartao
Console.WriteLine();
Console.WriteLine("╔══════════════════════════════╗");
Console.WriteLine($"  Nome: {name}");
Console.WriteLine($"  Idade: {age} anos");
Console.WriteLine($"  Cidade: {city}");
Console.WriteLine($"  Profissao: {job}");
Console.WriteLine("╚══════════════════════════════╝");
```

Saída esperada (com entradas "Maria", "25", "São Paulo", "Estudante"):
```
=== Cadastro ===
Nome: Maria
Idade: 25
Cidade: Sao Paulo
Profissao (ou estudante): Estudante

╔══════════════════════════════╗
  Nome: Maria
  Idade: 25 anos
  Cidade: Sao Paulo
  Profissao: Estudante
╚══════════════════════════════╝
```

### Desafio Extra

Adicione uma linha que diga "Menor de idade" ou "Maior de idade" baseado na idade informada. Use um `if/else`.

---

## Exercício 3 — Conversor de Temperaturas ⭐

### Objetivo

Praticar tipos numéricos (`double`), operações matemáticas e formatação de saída.

### Instruções

Crie um programa que leia uma temperatura em Celsius e converta para Fahrenheit e Kelvin.

Fórmulas:
- Fahrenheit = Celsius * 9.0 / 5.0 + 32.0
- Kelvin = Celsius + 273.15

```csharp
// Conversor de Temperaturas
// "celsius" = temperatura em Celsius
// "fahrenheit" = temperatura em Fahrenheit
// "kelvin" = temperatura em Kelvin

Console.WriteLine("=== Conversor de Temperaturas ===");
Console.Write("Digite a temperatura em Celsius: ");
double celsius = double.Parse(Console.ReadLine());

double fahrenheit = celsius * 9.0 / 5.0 + 32.0;
double kelvin = celsius + 273.15;

Console.WriteLine();
Console.WriteLine($"Celsius:    {celsius:F1} C");
Console.WriteLine($"Fahrenheit: {fahrenheit:F1} F");
Console.WriteLine($"Kelvin:     {kelvin:F1} K");
```

Saída esperada (com entrada "100"):
```
=== Conversor de Temperaturas ===
Digite a temperatura em Celsius: 100

Celsius:    100.0 C
Fahrenheit: 212.0 F
Kelvin:     373.1 K
```

### Desafio Extra

Adicione uma mensagem que diga o estado da água nessa temperatura:
- Abaixo de 0°C: "A agua esta congelada"
- Entre 0°C e 100°C: "A agua esta liquida"
- Acima de 100°C: "A agua esta em ebulicao"

---

## Exercício 4 — Explorador de Tipos ⭐⭐

### Objetivo

Entender na prática os diferentes tipos de C# e como eles se comportam.

### Instruções

Crie um programa que declare variáveis de cada tipo básico e mostre o tipo, o valor e o tamanho em bytes:

```csharp
// Explorador de Tipos em C#
// Mostra tipo, valor e tamanho de cada tipo basico

// "age" = idade
int age = 25;
// "distance" = distancia
long distance = 384400000;
// "price" = preco
double price = 49.90;
// "salary" = salario
decimal salary = 5432.10m;
// "weight" = peso
float weight = 72.5f;
// "letter" = letra
char letter = 'A';
// "isActive" = esta ativo
bool isActive = true;
// "name" = nome
string name = "Carlos";
// "level" = nivel
byte level = 200;
// "temperature" = temperatura
short temperature = -15;

Console.WriteLine("=== Explorador de Tipos C# ===");
Console.WriteLine();
Console.WriteLine($"{"Tipo",-12} {"Valor",-20} {"Tamanho",-10}");
Console.WriteLine(new string('-', 42));
Console.WriteLine($"{"int",-12} {age,-20} {sizeof(int)} bytes");
Console.WriteLine($"{"long",-12} {distance,-20} {sizeof(long)} bytes");
Console.WriteLine($"{"double",-12} {price,-20} {sizeof(double)} bytes");
Console.WriteLine($"{"decimal",-12} {salary,-20} {sizeof(decimal)} bytes");
Console.WriteLine($"{"float",-12} {weight,-20} {sizeof(float)} bytes");
Console.WriteLine($"{"char",-12} {letter,-20} {sizeof(char)} bytes");
Console.WriteLine($"{"bool",-12} {isActive,-20} {sizeof(bool)} bytes");
Console.WriteLine($"{"string",-12} {name,-20} {"variavel"}");
Console.WriteLine($"{"byte",-12} {level,-20} {sizeof(byte)} bytes");
Console.WriteLine($"{"short",-12} {temperature,-20} {sizeof(short)} bytes");
```

Saída esperada:
```
=== Explorador de Tipos C# ===

Tipo         Valor                Tamanho   
------------------------------------------
int          25                   4 bytes
long         384400000            8 bytes
double       49.9                 8 bytes
decimal      5432.10              16 bytes
float        72.5                 4 bytes
char         A                    2 bytes
bool         True                 1 bytes
string       Carlos               variavel
byte         200                  1 bytes
short        -15                  2 bytes
```

### Perguntas para Reflexão

1. Por que `string` não tem tamanho fixo como os outros tipos?
2. Por que `decimal` ocupa 16 bytes enquanto `double` ocupa apenas 8?
3. Se `byte` vai de 0 a 255, o que acontece se você tentar atribuir 256?

---

## Exercício 5 — Problema do Ponto Flutuante ⭐⭐

### Objetivo

Entender na prática a diferença entre `double` e `decimal` e por que `decimal` é importante para cálculos financeiros.

### Instruções

Crie um programa que simule uma compra com vários itens e compare o resultado usando `double` e `decimal`:

```csharp
// Comparacao: double vs decimal em calculos financeiros
// "item" = item, "price" = preco, "total" = total

Console.WriteLine("=== Simulacao de Compra ===");
Console.WriteLine();

// Usando double
Console.WriteLine("--- Calculo com double ---");
double totalDouble = 0.0;
// "coffee" = cafe
double coffeeDouble = 4.50;
// "bread" = pao
double breadDouble = 0.75;
// "milk" = leite
double milkDouble = 3.20;

// Simular 100 compras do mesmo carrinho
for (int i = 0; i < 100; i++)
{
    totalDouble += coffeeDouble + breadDouble + milkDouble;
}
Console.WriteLine($"Total (100 compras): R${totalDouble}");

// Usando decimal
Console.WriteLine();
Console.WriteLine("--- Calculo com decimal ---");
decimal totalDecimal = 0.0m;
decimal coffeeDecimal = 4.50m;
decimal breadDecimal = 0.75m;
decimal milkDecimal = 3.20m;

for (int i = 0; i < 100; i++)
{
    totalDecimal += coffeeDecimal + breadDecimal + milkDecimal;
}
Console.WriteLine($"Total (100 compras): R${totalDecimal}");

// Comparacao
Console.WriteLine();
Console.WriteLine($"Diferenca: R${(decimal)totalDouble - totalDecimal}");
```

Saída esperada:
```
=== Simulacao de Compra ===

--- Calculo com double ---
Total (100 compras): R$845.0000000000006

--- Calculo com decimal ---
Total (100 compras): R$845.00

Diferenca: R$0.0000000000006
```

### Perguntas para Reflexão

1. A diferença parece pequena (frações de centavo). Mas o que acontece se forem 1 milhão de transações por dia em um banco?
2. Por que não usar `decimal` para tudo, já que é mais preciso?
3. Em que situações o `double` é preferível ao `decimal`?

---

## Exercício 6 — Calculadora Interativa ⭐⭐

### Objetivo

Combinar entrada do usuário, tipos numéricos, condicionais e formatação em um programa mais completo.

### Instruções

Crie uma calculadora que leia dois números e uma operação, e mostre o resultado:

```csharp
// Calculadora Interativa
// "num1" = primeiro numero, "num2" = segundo numero
// "operation" = operacao, "result" = resultado

Console.WriteLine("=== Calculadora C# ===");
Console.WriteLine();

Console.Write("Primeiro numero: ");
double num1 = double.Parse(Console.ReadLine());

Console.Write("Segundo numero: ");
double num2 = double.Parse(Console.ReadLine());

Console.Write("Operacao (+, -, *, /): ");
string operation = Console.ReadLine();

double result = 0;
// "valid" = valido (se a operacao e reconhecida)
bool valid = true;

if (operation == "+")
{
    result = num1 + num2;
}
else if (operation == "-")
{
    result = num1 - num2;
}
else if (operation == "*")
{
    result = num1 * num2;
}
else if (operation == "/")
{
    if (num2 == 0)
    {
        Console.WriteLine("Erro: divisao por zero!");
        valid = false;
    }
    else
    {
        result = num1 / num2;
    }
}
else
{
    Console.WriteLine($"Operacao '{operation}' nao reconhecida!");
    valid = false;
}

if (valid)
{
    Console.WriteLine($"{num1} {operation} {num2} = {result:F2}");
}
```

Saída esperada (com entradas "10", "3", "/"):
```
=== Calculadora C# ===

Primeiro numero: 10
Segundo numero: 3
Operacao (+, -, *, /): /
10 / 3 = 3.33
```

### Desafio Extra

Adicione a operação `%` (módulo/resto da divisão) e `^` (potência). Para potência, use `Math.Pow(num1, num2)`.

---

## Exercício 7 — Conversor Python para C# ⭐⭐

### Objetivo

Praticar a conversão de código Python para C#, reforçando as diferenças de sintaxe.

### Instruções

Converta o seguinte programa Python para C#. Mantenha a mesma lógica e saída:

```python
# Programa em Python para converter para C#
# "name" = nome, "birth_year" = ano de nascimento
# "current_year" = ano atual, "age" = idade

name = input("Qual seu nome? ")
birth_year = int(input("Ano de nascimento: "))
current_year = 2025

age = current_year - birth_year

print(f"\nOla, {name}!")
print(f"Voce tem (ou tera) {age} anos em {current_year}")

if age >= 18:
    print("Voce e maior de idade")
    if age >= 65:
        print("Voce tem direito a meia-entrada por idade")
elif age >= 16:
    print("Voce pode votar, mas nao e obrigatorio")
else:
    print("Voce e menor de idade")
    years_left = 18 - age
    print(f"Faltam {years_left} anos para a maioridade")
```

Saída esperada (com entradas "Ana", "2000"):
```
Qual seu nome? Ana
Ano de nascimento: 2000

Ola, Ana!
Voce tem (ou tera) 25 anos em 2025
Voce e maior de idade
```

### Dicas

- `input()` em Python → `Console.ReadLine()` em C#
- `int()` em Python → `int.Parse()` em C#
- `f"..."` em Python → `$"..."` em C#
- `elif` em Python → `else if` em C#
- Não esqueça os `;` e `{ }`

### Solução

Tente fazer sozinho antes de olhar. Quando terminar, compare sua solução com esta:

```csharp
// Versao C# do programa Python
// "name" = nome, "birthYear" = ano de nascimento
// "currentYear" = ano atual, "age" = idade

Console.Write("Qual seu nome? ");
string name = Console.ReadLine();

Console.Write("Ano de nascimento: ");
int birthYear = int.Parse(Console.ReadLine());

int currentYear = 2025;
int age = currentYear - birthYear;

Console.WriteLine();
Console.WriteLine($"Ola, {name}!");
Console.WriteLine($"Voce tem (ou tera) {age} anos em {currentYear}");

if (age >= 18)
{
    Console.WriteLine("Voce e maior de idade");
    if (age >= 65)
    {
        Console.WriteLine("Voce tem direito a meia-entrada por idade");
    }
}
else if (age >= 16)
{
    Console.WriteLine("Voce pode votar, mas nao e obrigatorio");
}
else
{
    Console.WriteLine("Voce e menor de idade");
    // "yearsLeft" = anos restantes
    int yearsLeft = 18 - age;
    Console.WriteLine($"Faltam {yearsLeft} anos para a maioridade");
}
```

Saída esperada (com entradas "Ana", "2000"):
```
Qual seu nome? Ana
Ano de nascimento: 2000

Ola, Ana!
Voce tem (ou tera) 25 anos em 2025
Voce e maior de idade
```

---

## Exercício 8 — Tabela de Conversão de Tipos ⭐⭐⭐

### Objetivo

Explorar conversões entre tipos e entender quando funcionam e quando dão erro.

### Instruções

Crie um programa que teste diferentes conversões e mostre quais funcionam e quais falham:

```csharp
// Testando conversoes de tipo em C#
Console.WriteLine("=== Conversoes de Tipo ===");
Console.WriteLine();

// Conversao implicita (automatica) — de menor para maior
// "smallNumber" = numero pequeno
int smallNumber = 42;
long bigNumber = smallNumber;     // int -> long: OK (sem perda)
double decimalNumber = smallNumber; // int -> double: OK (sem perda)
Console.WriteLine($"int -> long: {smallNumber} -> {bigNumber}");
Console.WriteLine($"int -> double: {smallNumber} -> {decimalNumber}");

// Conversao explicita (cast) — de maior para menor
// "bigValue" = valor grande
double bigValue = 3.99;
int truncated = (int)bigValue;  // "truncated" = truncado (perde as casas decimais)
Console.WriteLine($"double -> int (cast): {bigValue} -> {truncated}");

// Conversao de string para numeros
// "text" = texto
string text = "123";
int fromString = int.Parse(text);
Console.WriteLine($"string -> int (Parse): \"{text}\" -> {fromString}");

// Conversao de numeros para string
int number = 456;
string toString = number.ToString();  // "toString" = para string
Console.WriteLine($"int -> string (ToString): {number} -> \"{toString}\"");

// Conversao com TryParse (segura)
// "invalidText" = texto invalido
string invalidText = "abc";
if (int.TryParse(invalidText, out int parsed))
{
    Console.WriteLine($"TryParse de \"{invalidText}\": {parsed}");
}
else
{
    Console.WriteLine($"TryParse de \"{invalidText}\": FALHOU (nao e numero)");
}
```

Saída esperada:
```
=== Conversoes de Tipo ===

int -> long: 42 -> 42
int -> double: 42 -> 42
double -> int (cast): 3.99 -> 3
string -> int (Parse): "123" -> 123
int -> string (ToString): 456 -> "456"
TryParse de "abc": FALHOU (nao e numero)
```

### Perguntas para Reflexão

1. Por que `(int)3.99` resulta em `3` e não em `4`? (Dica: é truncamento, não arredondamento)
2. Qual a diferença entre `Parse` e `TryParse`? Quando usar cada um?
3. Por que a conversão de `int` para `long` é automática, mas de `long` para `int` precisa de cast?

---

## Exercício 9 — Ficha de Personagem de RPG ⭐⭐⭐

### Objetivo

Criar um programa mais completo que combine todos os conceitos do módulo em um contexto divertido.

### Instruções

Crie um programa que gere uma ficha de personagem de RPG. O programa deve pedir o nome do personagem e a classe (guerreiro, mago ou arqueiro), e calcular os atributos base:

```csharp
// Ficha de Personagem de RPG
// "characterName" = nome do personagem
// "characterClass" = classe do personagem

Console.WriteLine("=== Criador de Personagem ===");
Console.WriteLine();

Console.Write("Nome do personagem: ");
string characterName = Console.ReadLine();

Console.WriteLine("Classes disponiveis: guerreiro, mago, arqueiro");
Console.Write("Escolha a classe: ");
string characterClass = Console.ReadLine().ToLower();

// Atributos base dependem da classe
// "strength" = forca, "intelligence" = inteligencia
// "agility" = agilidade, "health" = vida
int strength = 0;
int intelligence = 0;
int agility = 0;
int health = 0;
// "description" = descricao
string description = "";

if (characterClass == "guerreiro")
{
    strength = 18;
    intelligence = 8;
    agility = 12;
    health = 150;
    description = "Especialista em combate corpo a corpo";
}
else if (characterClass == "mago")
{
    strength = 6;
    intelligence = 20;
    agility = 10;
    health = 80;
    description = "Mestre das artes arcanas";
}
else if (characterClass == "arqueiro")
{
    strength = 10;
    intelligence = 12;
    agility = 18;
    health = 100;
    description = "Precisao mortal a distancia";
}
else
{
    Console.WriteLine($"Classe '{characterClass}' nao reconhecida!");
    Console.WriteLine("Use: guerreiro, mago ou arqueiro");
    return;
}

// Calcular nivel de poder total
// "powerLevel" = nivel de poder
int powerLevel = strength + intelligence + agility;

// Exibir a ficha
Console.WriteLine();
Console.WriteLine("╔════════════════════════════════════╗");
Console.WriteLine($"  FICHA DE PERSONAGEM");
Console.WriteLine("╠════════════════════════════════════╣");
Console.WriteLine($"  Nome:         {characterName}");
Console.WriteLine($"  Classe:       {characterClass.ToUpper()}");
Console.WriteLine($"  Descricao:    {description}");
Console.WriteLine("╠════════════════════════════════════╣");
Console.WriteLine($"  Forca:        {strength}");
Console.WriteLine($"  Inteligencia: {intelligence}");
Console.WriteLine($"  Agilidade:    {agility}");
Console.WriteLine($"  Vida:         {health} HP");
Console.WriteLine("╠════════════════════════════════════╣");
Console.WriteLine($"  Poder Total:  {powerLevel}");
Console.WriteLine("╚════════════════════════════════════╝");
```

Saída esperada (com entradas "Aragorn", "guerreiro"):
```
=== Criador de Personagem ===

Nome do personagem: Aragorn
Classes disponiveis: guerreiro, mago, arqueiro
Escolha a classe: guerreiro

╔════════════════════════════════════╗
  FICHA DE PERSONAGEM
╠════════════════════════════════════╣
  Nome:         Aragorn
  Classe:       GUERREIRO
  Descricao:    Especialista em combate corpo a corpo
╠════════════════════════════════════╣
  Forca:        18
  Inteligencia: 8
  Agilidade:    12
  Vida:         150 HP
╠════════════════════════════════════╣
  Poder Total:  38
╚════════════════════════════════════╝
```

### Desafio Extra

Adicione um sistema de "bônus de nome" — se o nome do personagem tiver mais de 10 caracteres, adicione +2 em todos os atributos (personagens com nomes épicos são mais fortes). Use `characterName.Length` para verificar o tamanho do nome.

---

## Exercício 10 — Comparação Lado a Lado ⭐

### Objetivo

Consolidar o mapeamento mental entre Python e C# escrevendo o mesmo programa nas duas linguagens.

### Instruções

Escreva o programa abaixo em Python E em C#. Execute ambos e confirme que a saída é idêntica:

O programa deve:
1. Pedir o nome de um produto
2. Pedir o preço
3. Pedir a quantidade em estoque
4. Calcular o valor total em estoque (preço * quantidade)
5. Mostrar um resumo formatado
6. Dizer se o estoque está "Baixo" (menos de 10), "Normal" (10-50) ou "Alto" (mais de 50)

Saída esperada (com entradas "Notebook", "3500.00", "25"):
```
=== Cadastro de Produto ===
Produto: Notebook
Preco: R$3500.00
Quantidade: 25
Valor total em estoque: R$87500.00
Status do estoque: Normal
```

Dica: faça primeiro em Python (que você já domina) e depois converta para C#. Compare as diferenças.

---

## Gabarito Rápido

Não olhe antes de tentar! Mas se ficar travado, aqui vão dicas:

| Exercício | Dica principal |
|-----------|---------------|
| 1 | Se `dotnet --version` não funciona, reinstale o SDK |
| 2 | Use `$"..."` para interpolacao e `int.Parse()` para converter idade |
| 3 | Cuidado com a divisao: use `9.0 / 5.0`, não `9 / 5` (divisao inteira!) |
| 4 | `sizeof()` funciona para tipos primitivos, não para `string` |
| 5 | O `for` em C# e igual ao de C: `for (int i = 0; i < 100; i++)` |
| 6 | Compare strings com `==` em C# (diferente de Java que usa `.equals()`) |
| 7 | `elif` vira `else if`, `f"..."` vira `$"..."` |
| 8 | Cast com `(tipo)` trunca, não arredonda |
| 9 | `.ToLower()` converte para minusculas, `.ToUpper()` para maiusculas |
| 10 | Faca em Python primeiro, depois converta sistematicamente |

---

[← Voltar ao conteúdo: Ambiente .NET](cap09-mod03-ambiente-dotnet-conteudo.md)