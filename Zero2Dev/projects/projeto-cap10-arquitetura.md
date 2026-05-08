# Projeto: Estruturando uma Aplicação em Camadas

## Visão Geral

Neste projeto, você vai pegar um sistema de cadastro de produtos que funciona perfeitamente — mas com todo o código misturado em um único arquivo — e reorganizá-lo em uma arquitetura de 3 camadas. O programa continuará fazendo exatamente a mesma coisa: cadastrar, listar, buscar, atualizar e remover produtos. A diferença é que o código ficará organizado em pastas e arquivos com responsabilidades claras.

Esse processo se chama **refatoração** — mudar a estrutura interna do código sem mudar o que ele faz. É uma das habilidades mais valorizadas no mercado de trabalho, porque a maioria dos projetos reais já existe e precisa ser mantida e evoluída, não criada do zero.

O projeto usa C# (.NET), a mesma linguagem dos capítulos 9 e 10. Você vai aplicar tudo que aprendeu: entidades de domínio, Repository Pattern, Services, Controllers, DTOs e injeção de dependência.

## Objetivo de Aprendizagem

Ao completar este projeto, você será capaz de:

- Analisar código existente e identificar responsabilidades misturadas
- Separar código em camadas (Models, Repositories, Services, Controllers, DTOs)
- Aplicar o Repository Pattern com interface e implementação
- Criar Services que encapsulam regras de negócio
- Criar Controllers magros que apenas delegam para Services
- Usar DTOs quando fazem sentido (e não usar quando não fazem)
- Configurar dependências no ponto de entrada (Composition Root)
- Refatorar incrementalmente sem quebrar funcionalidades
- Documentar a arquitetura de um projeto

## Requisitos

O sistema reorganizado deve:

1. Cadastrar produtos com nome, preço e estoque
2. Listar todos os produtos cadastrados
3. Buscar um produto por ID
4. Atualizar o preço de um produto
5. Adicionar estoque a um produto
6. Remover um produto (com confirmação)
7. Validar regras de negócio: nome não vazio, preço positivo, estoque não negativo, nome não duplicado
8. Manter dados em memória (sem banco de dados)
9. Ter cada camada em sua própria pasta
10. Ter o Program.cs apenas como Composition Root (configuração e inicialização)

## Especificação Técnica

- **Linguagem**: C# (.NET 8+)
- **Tipo de projeto**: Console Application
- **Armazenamento**: Em memória (List)
- **Padrões**: 3 camadas, Repository Pattern, Injeção de Dependência via construtor

### Estrutura Final do Projeto

```
ProdutosCamadas/
├── Program.cs                          # Composition Root
├── Models/
│   └── Product.cs                      # Entidade de dominio
├── Repositories/
│   ├── IProductRepository.cs           # Interface do repositorio
│   └── InMemoryProductRepository.cs    # Implementacao em memoria
├── Services/
│   └── ProductService.cs               # Logica de negocio
├── Controllers/
│   └── ProductController.cs            # Interface com o usuario (CLI)
├── DTOs/
│   ├── CreateProductRequest.cs         # Dados de entrada para cadastro
│   ├── UpdatePriceRequest.cs           # Dados de entrada para atualizacao
│   └── ProductResponse.cs             # Dados de saida
├── ProdutosCamadas.csproj
└── README.md                           # Documentacao da arquitetura
```

---

## Desenvolvimento Incremental

### Preparação: Criar o Projeto

Antes de começar as fases, crie o projeto base:

```bash
# Crie a pasta do projeto
mkdir -p ~/meus-projetos/curso/cap10/projeto
cd ~/meus-projetos/curso/cap10/projeto

# Crie o projeto .NET
dotnet new console -n ProdutosCamadas
cd ProdutosCamadas
```

Agora copie o código original (do módulo 10.9) para o `Program.cs`. Esse é o ponto de partida — tudo em um arquivo.

Execute para confirmar que funciona:

```bash
dotnet run
```

Você deve ver o menu do sistema de produtos. Teste cadastrar, listar e remover um produto. Tudo funcionando? Ótimo. Agora vamos reorganizar.

---

### Fase 1 — Analisar o Código e Mapear Responsabilidades

**Objetivo**: Entender o código existente antes de mover qualquer coisa.

**O que fazer**: Leia o código original e classifique cada parte:

| Trecho | Camada destino | Arquivo destino |
|--------|---------------|-----------------|
| Classe `Product` | Models | Models/Product.cs |
| `List<Product> products`, `nextId` | Repository | Repositories/InMemoryProductRepository.cs |
| `GetAllProducts`, `GetProductById` | Repository | Repositories/InMemoryProductRepository.cs |
| `AddProduct`, `UpdateProduct`, `DeleteProduct` | Repository | Repositories/InMemoryProductRepository.cs |
| `ProductExists` | Repository | Repositories/InMemoryProductRepository.cs |
| Validacoes de negocio (nome vazio, preco positivo) | Service | Services/ProductService.cs |
| `Console.Write`, `Console.ReadLine`, menu | Controller | Controllers/ProductController.cs |
| Parsing (TryParse) | Controller | Controllers/ProductController.cs |
| Mensagens de erro e sucesso | Controller | Controllers/ProductController.cs |

**Checkpoint**: Você consegue explicar para onde cada parte do código vai e por quê? Se sim, siga para a Fase 2.

---

### Fase 2 — Criar a Estrutura de Pastas

**Objetivo**: Criar as pastas que vão receber o código reorganizado.

**O que fazer**:

```bash
# Na pasta ProdutosCamadas/
mkdir Models
mkdir Repositories
mkdir Services
mkdir Controllers
mkdir DTOs
```

**Checkpoint**: Execute `dotnet run` — o programa deve continuar funcionando normalmente. Criamos apenas pastas vazias, nada mudou no código.

---

### Fase 3 — Extrair Models e Repositories

**Objetivo**: Mover a entidade Product e as funções de acesso a dados para seus próprios arquivos.

#### Passo 3.1: Criar Models/Product.cs

Crie o arquivo `Models/Product.cs` com a classe Product:

```csharp
// Models/Product.cs
// "Product" = Produto — entidade de dominio
// Representa um produto no sistema de cadastro

namespace ProdutosCamadas.Models;

public class Product
{
    public int Id { get; set; }              // "Id" = identificador unico
    public string Name { get; set; }         // "Name" = nome do produto
    public decimal Price { get; set; }       // "Price" = preco
    public int Stock { get; set; }           // "Stock" = estoque disponivel
    public DateTime CreatedAt { get; set; }  // "CreatedAt" = data de criacao

    // Construtor — recebe os dados obrigatorios
    public Product(string name, decimal price, int stock)
    {
        Name = name;
        Price = price;
        Stock = stock;
        CreatedAt = DateTime.Now; // data e hora atuais
    }

    // Representacao em texto do produto
    public override string ToString()
    {
        return $"[{Id}] {Name} — R${Price:F2} (Estoque: {Stock})";
    }
}
```

#### Passo 3.2: Criar Repositories/IProductRepository.cs

Crie a interface que define o contrato do repositório:

```csharp
// Repositories/IProductRepository.cs
// "IProductRepository" = interface do repositorio de produtos
// Define QUAIS operacoes existem, sem dizer COMO sao feitas

using ProdutosCamadas.Models;

namespace ProdutosCamadas.Repositories;

public interface IProductRepository
{
    List<Product> GetAll();           // "GetAll" = obter todos os produtos
    Product? GetById(int id);         // "GetById" = obter por ID (pode retornar null)
    void Add(Product product);        // "Add" = adicionar um produto
    void Update(Product product);     // "Update" = atualizar um produto existente
    void Delete(int id);              // "Delete" = remover um produto pelo ID
    bool Exists(string name);         // "Exists" = verificar se um nome ja existe
}
```

#### Passo 3.3: Criar Repositories/InMemoryProductRepository.cs

Crie a implementação que guarda dados em memória:

```csharp
// Repositories/InMemoryProductRepository.cs
// "InMemoryProductRepository" = repositorio em memoria
// Implementa IProductRepository usando uma lista interna

using ProdutosCamadas.Models;

namespace ProdutosCamadas.Repositories;

public class InMemoryProductRepository : IProductRepository
{
    // Lista interna que simula o banco de dados
    private readonly List<Product> _products = new List<Product>();
    private int _nextId = 1; // "nextId" = proximo ID a ser atribuido

    public List<Product> GetAll()
    {
        // Retorna copia da lista para proteger os dados internos
        return new List<Product>(_products);
    }

    public Product? GetById(int id)
    {
        // Procura o produto pelo ID — retorna null se nao encontrar
        return _products.FirstOrDefault(p => p.Id == id);
    }

    public void Add(Product product)
    {
        // Atribui ID automatico e adiciona a lista
        product.Id = _nextId++;
        _products.Add(product);
    }

    public void Update(Product product)
    {
        // Encontra o produto pelo ID e substitui
        var index = _products.FindIndex(p => p.Id == product.Id);
        if (index >= 0)
        {
            _products[index] = product;
        }
    }

    public void Delete(int id)
    {
        // Remove o produto com o ID informado
        _products.RemoveAll(p => p.Id == id);
    }

    public bool Exists(string name)
    {
        // Verifica se ja existe um produto com esse nome (ignora maiusculas)
        return _products.Any(
            p => p.Name.Equals(name, StringComparison.OrdinalIgnoreCase)
        );
    }
}
```

#### Passo 3.4: Atualizar o Program.cs

Remova do `Program.cs` a classe `Product`, a lista `products`, o `nextId` e todas as funções de acesso a dados (`GetAllProducts`, `GetProductById`, `AddProduct`, `UpdateProduct`, `DeleteProduct`, `ProductExists`).

No lugar, crie uma instância do repositório e atualize as funções restantes para usá-lo:

```csharp
// Program.cs — apos Fase 3
// Removemos: classe Product, lista products, funcoes de dados
// Adicionamos: instancia do repositorio

using ProdutosCamadas.Models;
using ProdutosCamadas.Repositories;

// Cria o repositorio
var repository = new InMemoryProductRepository();

// As funcoes de operacao agora usam o repositorio
// (ainda misturadas com Console — vamos separar nas proximas fases)
```

Atualize cada função para usar `repository` em vez das funções estáticas. Por exemplo, `GetAllProducts()` vira `repository.GetAll()`, `AddProduct(product)` vira `repository.Add(product)`, etc.

**Checkpoint**: Execute `dotnet run`. O programa deve funcionar exatamente como antes — mesmas opções, mesmas validações, mesmas mensagens. Se funcionar, a Fase 3 está completa.

---

### Fase 4 — Criar a Camada de Services

**Objetivo**: Extrair toda a lógica de negócio para o ProductService.

#### Passo 4.1: Criar Services/ProductService.cs

O Service recebe o repositório pelo construtor e expõe métodos com regras de negócio:

```csharp
// Services/ProductService.cs
// "ProductService" = servico de produtos
// Contem TODA a logica de negocio: validacoes, regras, orquestracao

using ProdutosCamadas.Models;
using ProdutosCamadas.Repositories;

namespace ProdutosCamadas.Services;

public class ProductService
{
    private readonly IProductRepository _repository;

    // Recebe o repositorio pelo construtor (injecao de dependencia)
    public ProductService(IProductRepository repository)
    {
        _repository = repository;
    }

    // Cadastrar novo produto — com todas as regras de negocio
    // "Register" = registrar
    public string Register(string name, decimal price, int stock)
    {
        // Regra 1: nome nao pode ser vazio
        if (string.IsNullOrWhiteSpace(name))
        {
            return "Erro: nome do produto nao pode ser vazio.";
        }

        // Regra 2: preco deve ser positivo
        if (price <= 0)
        {
            return "Erro: preco deve ser maior que zero.";
        }

        // Regra 3: estoque nao pode ser negativo
        if (stock < 0)
        {
            return "Erro: estoque nao pode ser negativo.";
        }

        // Regra 4: nome nao pode ser duplicado
        if (_repository.Exists(name))
        {
            return $"Erro: ja existe um produto com o nome '{name}'.";
        }

        // Tudo valido — cria e salva
        var product = new Product(name, price, stock);
        _repository.Add(product);

        return $"Produto '{name}' cadastrado com sucesso! ID: {product.Id}";
    }

    // Listar todos os produtos
    // "ListAll" = listar todos
    public List<Product> ListAll()
    {
        return _repository.GetAll();
    }

    // Buscar produto por ID
    // "FindById" = encontrar por ID
    public Product? FindById(int id)
    {
        return _repository.GetById(id);
    }

    // Atualizar preco — com regra de negocio
    // "UpdatePrice" = atualizar preco
    public string UpdatePrice(int id, decimal newPrice)
    {
        // Regra: preco deve ser positivo
        if (newPrice <= 0)
        {
            return "Erro: preco deve ser maior que zero.";
        }

        var product = _repository.GetById(id);
        if (product == null)
        {
            return $"Erro: produto com ID {id} nao encontrado.";
        }

        product.Price = newPrice;
        _repository.Update(product);

        return $"Preco de '{product.Name}' atualizado para R${newPrice:F2}.";
    }

    // Adicionar estoque
    // "AddStock" = adicionar estoque
    public string AddStock(int id, int quantity)
    {
        // Regra: quantidade deve ser positiva
        if (quantity <= 0)
        {
            return "Erro: quantidade deve ser maior que zero.";
        }

        var product = _repository.GetById(id);
        if (product == null)
        {
            return $"Erro: produto com ID {id} nao encontrado.";
        }

        product.Stock += quantity;
        _repository.Update(product);

        return $"Estoque de '{product.Name}' atualizado para {product.Stock} unidades.";
    }

    // Remover produto
    // "Remove" = remover
    public string Remove(int id)
    {
        var product = _repository.GetById(id);
        if (product == null)
        {
            return $"Erro: produto com ID {id} nao encontrado.";
        }

        _repository.Delete(id);
        return $"Produto '{product.Name}' removido com sucesso.";
    }
}
```

Observe: o Service **não tem nenhum** `Console.Write` ou `Console.ReadLine`. Ele recebe dados puros (string, decimal, int), aplica regras e retorna resultados como string. Não sabe e não precisa saber de onde os dados vieram.

**Checkpoint**: O arquivo compila sem erros. O Service não referência `System.Console` em nenhum lugar.

---

### Fase 5 — Extrair Controllers

**Objetivo**: Mover toda a interface com o usuário para o ProductController.

#### Passo 5.1: Criar Controllers/ProductController.cs

O Controller recebe o Service pelo construtor e cuida de toda a interação com o Console:

```csharp
// Controllers/ProductController.cs
// "ProductController" = controlador de produtos
// Responsavel por: menu, leitura de entrada, exibicao de resultados
// NAO tem logica de negocio — apenas delega para o Service

using ProdutosCamadas.Services;

namespace ProdutosCamadas.Controllers;

public class ProductController
{
    private readonly ProductService _service;

    // Recebe o servico pelo construtor
    public ProductController(ProductService service)
    {
        _service = service;
    }

    // Inicia o menu principal
    // "Run" = executar
    public void Run()
    {
        while (true)
        {
            Console.WriteLine("\n========================================");
            Console.WriteLine("       SISTEMA DE PRODUTOS");
            Console.WriteLine("========================================");
            Console.WriteLine("  1. Cadastrar produto");
            Console.WriteLine("  2. Listar produtos");
            Console.WriteLine("  3. Buscar produto por ID");
            Console.WriteLine("  4. Atualizar preco");
            Console.WriteLine("  5. Adicionar estoque");
            Console.WriteLine("  6. Remover produto");
            Console.WriteLine("  0. Sair");
            Console.WriteLine("========================================");
            Console.Write("Escolha uma opcao: ");

            switch (Console.ReadLine())
            {
                case "1": RegisterProduct(); break;
                case "2": ListProducts(); break;
                case "3": FindProduct(); break;
                case "4": UpdatePrice(); break;
                case "5": AddStock(); break;
                case "6": RemoveProduct(); break;
                case "0":
                    Console.WriteLine("Ate logo!");
                    return;
                default:
                    Console.WriteLine("Opcao invalida!");
                    break;
            }
        }
    }

    // Cadastrar produto — le dados e delega para o Service
    private void RegisterProduct()
    {
        Console.Write("Nome do produto: ");
        var name = Console.ReadLine() ?? "";

        Console.Write("Preco: ");
        if (!decimal.TryParse(Console.ReadLine(), out decimal price))
        {
            Console.WriteLine("Preco invalido. Use numeros (ex: 29.90).");
            return;
        }

        Console.Write("Estoque inicial: ");
        if (!int.TryParse(Console.ReadLine(), out int stock))
        {
            Console.WriteLine("Estoque invalido. Use numeros inteiros.");
            return;
        }

        // Delega para o Service — ele valida as regras de negocio
        var result = _service.Register(name, price, stock);
        Console.WriteLine(result);
    }

    // Listar todos os produtos
    private void ListProducts()
    {
        var products = _service.ListAll();

        if (products.Count == 0)
        {
            Console.WriteLine("Nenhum produto cadastrado.");
            return;
        }

        Console.WriteLine("\n--- Lista de Produtos ---");
        foreach (var p in products)
        {
            Console.WriteLine($"  {p}");
        }
        Console.WriteLine($"Total: {products.Count} produtos");
    }

    // Buscar produto por ID
    private void FindProduct()
    {
        Console.Write("ID do produto: ");
        if (!int.TryParse(Console.ReadLine(), out int id))
        {
            Console.WriteLine("ID invalido.");
            return;
        }

        var product = _service.FindById(id);
        if (product == null)
        {
            Console.WriteLine($"Produto com ID {id} nao encontrado.");
            return;
        }

        Console.WriteLine($"\n  {product}");
        Console.WriteLine($"  Criado em: {product.CreatedAt:dd/MM/yyyy HH:mm}");
    }

    // Atualizar preco
    private void UpdatePrice()
    {
        Console.Write("ID do produto: ");
        if (!int.TryParse(Console.ReadLine(), out int id))
        {
            Console.WriteLine("ID invalido.");
            return;
        }

        // Busca o produto para mostrar informacoes atuais
        var product = _service.FindById(id);
        if (product == null)
        {
            Console.WriteLine($"Produto com ID {id} nao encontrado.");
            return;
        }

        Console.WriteLine($"Produto: {product.Name} — Preco atual: R${product.Price:F2}");
        Console.Write("Novo preco: ");
        if (!decimal.TryParse(Console.ReadLine(), out decimal newPrice))
        {
            Console.WriteLine("Preco invalido.");
            return;
        }

        // Delega para o Service
        var result = _service.UpdatePrice(id, newPrice);
        Console.WriteLine(result);
    }

    // Adicionar estoque
    private void AddStock()
    {
        Console.Write("ID do produto: ");
        if (!int.TryParse(Console.ReadLine(), out int id))
        {
            Console.WriteLine("ID invalido.");
            return;
        }

        var product = _service.FindById(id);
        if (product == null)
        {
            Console.WriteLine($"Produto com ID {id} nao encontrado.");
            return;
        }

        Console.WriteLine($"Produto: {product.Name} — Estoque atual: {product.Stock}");
        Console.Write("Quantidade a adicionar: ");
        if (!int.TryParse(Console.ReadLine(), out int qty))
        {
            Console.WriteLine("Quantidade invalida.");
            return;
        }

        var result = _service.AddStock(id, qty);
        Console.WriteLine(result);
    }

    // Remover produto
    private void RemoveProduct()
    {
        Console.Write("ID do produto para remover: ");
        if (!int.TryParse(Console.ReadLine(), out int id))
        {
            Console.WriteLine("ID invalido.");
            return;
        }

        var product = _service.FindById(id);
        if (product == null)
        {
            Console.WriteLine($"Produto com ID {id} nao encontrado.");
            return;
        }

        Console.Write($"Remover '{product.Name}'? (s/n): ");
        if (Console.ReadLine()?.ToLower() == "s")
        {
            var result = _service.Remove(id);
            Console.WriteLine(result);
        }
        else
        {
            Console.WriteLine("Operacao cancelada.");
        }
    }
}
```

Observe: o Controller faz apenas 3 coisas — lê entrada, delega para o Service e exibe o resultado. Toda validação de negócio (preço positivo, nome duplicado) está no Service. O Controller só faz validação de **formato** (TryParse para converter string em número).

**Checkpoint**: Execute `dotnet run`. O programa deve funcionar exatamente como antes. Teste todas as opções: cadastrar, listar, buscar, atualizar preço, adicionar estoque e remover.

---

### Fase 6 — Adicionar DTOs

**Objetivo**: Criar objetos de transferência de dados para separar os dados de entrada/saída da entidade de domínio.

#### Passo 6.1: Criar DTOs/CreateProductRequest.cs

```csharp
// DTOs/CreateProductRequest.cs
// "CreateProductRequest" = requisicao de criacao de produto
// Contem apenas os dados que o usuario envia para cadastrar
// NAO tem Id nem CreatedAt — esses sao gerados pelo sistema

namespace ProdutosCamadas.DTOs;

public class CreateProductRequest
{
    public string Name { get; set; } = "";    // "Name" = nome do produto
    public decimal Price { get; set; }        // "Price" = preco
    public int Stock { get; set; }            // "Stock" = estoque inicial
}
```

#### Passo 6.2: Criar DTOs/UpdatePriceRequest.cs

```csharp
// DTOs/UpdatePriceRequest.cs
// "UpdatePriceRequest" = requisicao de atualizacao de preco
// Contem o ID do produto e o novo preco

namespace ProdutosCamadas.DTOs;

public class UpdatePriceRequest
{
    public int ProductId { get; set; }     // "ProductId" = ID do produto
    public decimal NewPrice { get; set; }  // "NewPrice" = novo preco
}
```

#### Passo 6.3: Criar DTOs/ProductResponse.cs

```csharp
// DTOs/ProductResponse.cs
// "ProductResponse" = resposta com dados do produto
// Contem os dados que o usuario precisa ver
// Pode ser diferente da entidade (ex: formatar preco, omitir campos internos)

namespace ProdutosCamadas.DTOs;

public class ProductResponse
{
    public int Id { get; set; }
    public string Name { get; set; } = "";
    public string FormattedPrice { get; set; } = "";  // "FormattedPrice" = preco formatado
    public int Stock { get; set; }
    public string CreatedAt { get; set; } = "";        // Data como string formatada

    // Metodo estatico para converter de Product para ProductResponse
    // "FromProduct" = a partir de um produto
    public static ProductResponse FromProduct(Models.Product product)
    {
        return new ProductResponse
        {
            Id = product.Id,
            Name = product.Name,
            FormattedPrice = $"R${product.Price:F2}",
            Stock = product.Stock,
            CreatedAt = product.CreatedAt.ToString("dd/MM/yyyy HH:mm")
        };
    }

    // Representacao em texto
    public override string ToString()
    {
        return $"[{Id}] {Name} — {FormattedPrice} (Estoque: {Stock})";
    }
}
```

#### Passo 6.4: Atualizar o Service para usar DTOs (opcional)

Você pode atualizar o método `Register` do Service para receber um `CreateProductRequest` em vez de parâmetros separados:

```csharp
// No ProductService — versao com DTO
// "Register" = registrar produto usando DTO de entrada
public string Register(CreateProductRequest request)
{
    if (string.IsNullOrWhiteSpace(request.Name))
    {
        return "Erro: nome do produto nao pode ser vazio.";
    }

    if (request.Price <= 0)
    {
        return "Erro: preco deve ser maior que zero.";
    }

    if (request.Stock < 0)
    {
        return "Erro: estoque nao pode ser negativo.";
    }

    if (_repository.Exists(request.Name))
    {
        return $"Erro: ja existe um produto com o nome '{request.Name}'.";
    }

    var product = new Product(request.Name, request.Price, request.Stock);
    _repository.Add(product);

    return $"Produto '{request.Name}' cadastrado com sucesso! ID: {product.Id}";
}
```

E atualizar o Controller para criar o DTO:

```csharp
// No ProductController — versao com DTO
private void RegisterProduct()
{
    Console.Write("Nome do produto: ");
    var name = Console.ReadLine() ?? "";

    Console.Write("Preco: ");
    if (!decimal.TryParse(Console.ReadLine(), out decimal price))
    {
        Console.WriteLine("Preco invalido. Use numeros (ex: 29.90).");
        return;
    }

    Console.Write("Estoque inicial: ");
    if (!int.TryParse(Console.ReadLine(), out int stock))
    {
        Console.WriteLine("Estoque invalido. Use numeros inteiros.");
        return;
    }

    // Cria o DTO e delega para o Service
    var request = new CreateProductRequest
    {
        Name = name,
        Price = price,
        Stock = stock
    };

    var result = _service.Register(request);
    Console.WriteLine(result);
}
```

**Nota**: usar DTOs neste projeto é opcional e pedagógico. O sistema funciona perfeitamente com parâmetros simples. A versão com DTOs mostra como projetos maiores organizam os dados de entrada e saída.

**Checkpoint**: Execute `dotnet run`. O programa deve funcionar exatamente como antes. Os DTOs não mudam o comportamento — apenas organizam como os dados são transportados entre camadas.

---

### Fase 7 — Documentar a Arquitetura

**Objetivo**: Criar um README que explica a organização do projeto.

#### Passo 7.1: Criar o README.md do projeto

Crie o arquivo `README.md` na raiz do projeto `ProdutosCamadas/`:

```markdown
# Sistema de Cadastro de Produtos — Arquitetura em Camadas

Sistema de cadastro de produtos com CRUD completo, organizado em
arquitetura de 3 camadas.

## Arquitetura

O projeto segue o padrao de 3 camadas:

- **Controllers/** — Interface com o usuario (menu CLI)
- **Services/** — Logica de negocio (validacoes, regras)
- **Repositories/** — Acesso a dados (armazenamento em memoria)
- **Models/** — Entidades de dominio
- **DTOs/** — Objetos de transferencia de dados

### Fluxo de uma operacao

1. O usuario interage com o Controller (menu no terminal)
2. O Controller le a entrada, faz parsing e chama o Service
3. O Service aplica regras de negocio e chama o Repository
4. O Repository executa a operacao de dados
5. O resultado volta pelo mesmo caminho: Repository -> Service -> Controller -> Usuario

### Regra fundamental

Cada camada so conversa com a camada adjacente:
- Controller chama Service (nunca Repository)
- Service chama Repository (nunca Controller)
- Repository nao chama ninguem — apenas responde

## Como executar

```bash
dotnet run
```

## Estrutura de pastas

```
ProdutosCamadas/
├── Program.cs              # Composition Root (configuração)
├── Models/
│   └── Product.cs          # Entidade de dominio
├── Repositories/
│   ├── IProductRepository.cs       # Interface
│   └── InMemoryProductRepository.cs # Implementação
├── Services/
│   └── ProductService.cs   # Lógica de negocio
├── Controllers/
│   └── ProductController.cs # Interface CLI
└── DTOs/
    ├── CreateProductRequest.cs
    ├── UpdatePriceRequest.cs
    └── ProductResponse.cs
```

## Decisoes de arquitetura

1. **Interface no Repository**: permite trocar de memoria para SQLite
   sem mudar o Service
2. **Service retorna strings**: simplicidade para projeto CLI.
   Em uma API, retornaria objetos tipados
3. **DTOs opcionais**: adicionados para praticar o conceito.
   Para este tamanho de projeto, parametros simples bastam
4. **Composition Root no Program.cs**: todas as dependencias sao
   montadas em um unico lugar
```

#### Passo 7.2: Atualizar o Program.cs final

O `Program.cs` final deve ter apenas a configuração:

```csharp
// Program.cs — Composition Root
// Responsabilidade unica: criar dependencias e iniciar a aplicacao

using ProdutosCamadas.Repositories;
using ProdutosCamadas.Services;
using ProdutosCamadas.Controllers;

// Camada de dados: cria o repositorio em memoria
var repository = new InMemoryProductRepository();

// Camada de negocio: cria o servico com o repositorio
var service = new ProductService(repository);

// Camada de entrada: cria o controller com o servico
var controller = new ProductController(service);

// Inicia a aplicacao
controller.Run();
```

**Checkpoint final**: Execute `dotnet run` e teste TODAS as funcionalidades:

1. Cadastre 3 produtos (Notebook R$3500, Mouse R$89.90, Teclado R$199)
2. Liste todos — deve mostrar os 3 produtos
3. Busque o produto com ID 1 — deve mostrar o Notebook
4. Atualize o preço do Mouse para R$99.90
5. Adicione 5 unidades ao estoque do Teclado
6. Remova o Notebook (confirme com "s")
7. Liste novamente — deve mostrar apenas Mouse e Teclado
8. Tente cadastrar com nome vazio — deve dar erro
9. Tente cadastrar com preço negativo — deve dar erro
10. Tente cadastrar com nome duplicado — deve dar erro

Se tudo funcionar, o projeto está completo.

---

## Critérios de Conclusão

Seu projeto está pronto quando:

- [ ] O código original foi reorganizado em 5 pastas (Models, Repositories, Services, Controllers, DTOs)
- [ ] Cada arquivo tem uma única responsabilidade
- [ ] O Program.cs tem apenas configuração (Composition Root) — menos de 15 linhas
- [ ] O Controller não tem regras de negócio (nenhuma validação de preço, nome duplicado, etc.)
- [ ] O Service não tem `Console.Write` ou `Console.ReadLine`
- [ ] O Repository não tem regras de negócio
- [ ] O Repository implementa uma interface (`IProductRepository`)
- [ ] Todas as 6 operações funcionam: cadastrar, listar, buscar, atualizar preço, adicionar estoque, remover
- [ ] As validações funcionam: nome vazio, preço negativo, nome duplicado, estoque negativo
- [ ] O README documenta a arquitetura com estrutura de pastas e decisões
- [ ] O programa compila e executa sem erros (`dotnet run`)

---

## Dicas de Implementação

1. **Faça uma fase por vez**. Não tente reorganizar tudo de uma vez. Mova uma camada, teste, confirme que funciona, e siga para a próxima.

2. **Use `dotnet build` frequentemente**. Depois de cada mudança, compile para verificar se não tem erros de referência (classe não encontrada, namespace errado).

3. **Não esqueça dos `using`**. Quando mover uma classe para outro namespace, os arquivos que a usam precisam de `using ProdutosCamadas.Models;`, `using ProdutosCamadas.Repositories;`, etc.

4. **Comece pelo mais fácil**. Models e Repositories são os mais independentes — comece por eles. Controllers e Services dependem dos anteriores — faça depois.

5. **Se algo quebrar, volte atrás**. Se depois de mover algo o programa não compila, desfaça a última mudança e tente de novo com mais cuidado. Refatoração incremental permite voltar atrás facilmente.

6. **Compare com o módulo 10.2**. O exemplo completo de 3 camadas do módulo 10.2 é uma referência. Se tiver dúvida sobre onde algo vai, consulte aquele exemplo.

7. **Não crie complexidade desnecessária**. Se algo funciona com parâmetros simples, não crie um DTO "por precaução". Adicione complexidade apenas quando houver benefício real.

---

## Extensões Opcionais (Para Quem Quer Ir Além)

Se você completou o projeto e quer praticar mais:

1. **Implementar SqliteProductRepository**: crie uma segunda implementação de `IProductRepository` que salva dados em SQLite (como no capítulo 8). Troque a implementação no `Program.cs` mudando apenas uma linha.

2. **Adicionar campo Categoria**: adicione uma propriedade `Category` ao `Product`. Atualize o Repository, Service e Controller. Observe como a mudança se propaga pelas camadas.

3. **Criar um segundo Controller**: crie um `BatchController` que lê produtos de um arquivo CSV e cadastra todos de uma vez, usando o mesmo `ProductService`. Isso demonstra que dois Controllers diferentes podem usar o mesmo Service.

4. **Adicionar relatório**: crie um método `GenerateReport()` no Service que retorna estatísticas (total de produtos, preço médio, produto mais caro). Adicione uma opção no menu do Controller para exibir o relatório.

5. **Adicionar log**: crie um `LoggingProductService` que envolve o `ProductService` original e registra cada operação em um arquivo de log. Isso demonstra o padrão Decorator.

---

## Conexão com o Mundo Real

Este projeto simula o que acontece em empresas reais quando um sistema precisa ser reorganizado. No Mercado Livre, por exemplo, a migração de monolito para microserviços começou exatamente assim: primeiro organizaram o código em camadas dentro do monolito, depois extraíram cada camada para um serviço independente.

No seu primeiro emprego, é muito provável que você encontre código misturado que precisa ser reorganizado. Saber fazer isso de forma incremental — sem quebrar funcionalidades — é uma das habilidades mais valorizadas no mercado. Este projeto te deu essa experiência prática.

No capítulo 11, você vai dar o próximo passo: transformar um sistema organizado em camadas em uma API REST acessível pela web. A arquitetura será a mesma — Controller, Service, Repository — mas o Controller será HTTP em vez de CLI.

---

[← Voltar ao Módulo 10.9](../capitulos/cap10-mod09-projeto-estrutura-conteudo.md)