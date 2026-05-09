# 21 — Manipulação JSON: Leitura e Escrita com o Módulo json

[<- Anterior: Leitura e Escrita de Arquivos](20-leitura-escrita-arquivos.md) | [Glossário](00-glossário.md) | [Próximo: Classes e Objetos ->](22-classes-objetos.md)

---

## Introdução

No módulo anterior, você aprendeu a ler e escrever arquivos de texto e CSV. Agora, vamos aprender a trabalhar com um formato de dados muito especial: o **JSON**.

Imagine que você precisa enviar uma ficha cadastral de um produto para outra pessoa por e-mail. Você poderia escrever tudo em um papel, mas a outra pessoa precisaria entender a sua letra e saber onde comeca cada informação. Seria muito mais fácil se existisse um formato **padronizado** que qualquer pessoa (ou programa) conseguisse ler e entender.

O JSON e exatamente isso: um formato padronizado para organizar e trocar dados entre programas, sistemas e ate entre linguagens de programação diferentes. Ele e usado em praticamente todo lugar na programação moderna — desde aplicativos de celular ate grandes sistemas na internet.

Neste módulo, você vai aprender a:

- Entender **o que e JSON** e por que ele e tao importante
- Converter dados entre **JSON e Python** (e vice-versa)
- **Ler** dados JSON de arquivos
- **Escrever** dados Python em arquivos JSON
- **Formatar** JSON para ficar legivel
- **Tratar erros** quando o JSON esta inválido

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-21/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-21`
4. Execute: `python3 nome_do_arquivo.py`

> **Importante:** Alguns exemplos criam arquivos JSON no mesmo diretório onde você executa o programa. Verifique a pasta apos executar para ver os arquivos criados.

---

## O Que e JSON

JSON e a sigla para **JavaScript Object Notation** (Notação de Objetos JavaScript). Apesar de ter "JavaScript" no nome, o JSON e usado por **todas** as linguagens de programação modernas, incluindo Python.

Pense no JSON como uma **lingua universal** entre programas de computador. Assim como o ingles e usado como lingua comum entre pessoas de paises diferentes, o JSON e usado como formato comum para trocar dados entre programas diferentes.

### Por Que o JSON e Tao Usado?

O JSON e popular por vários motivos:

- **Simples de ler:** Tanto humanos quanto computadores conseguem entender facilmente
- **Leve:** Ocupa pouco espaco, o que e importante para enviar dados pela internet
- **Universal:** Funciona com qualquer linguagem de programação
- **Padronizado:** Todo mundo usa o mesmo formato, evitando confusao

### Onde o JSON e Usado no Dia a Dia da Programação?

- **APIs na internet:** Quando um aplicativo de celular busca dados de um servidor, os dados geralmente vem em JSON
- **Arquivos de configuração:** Muitos programas guardam suas configuracoes em arquivos `.json`
- **Troca de dados entre sistemas:** Quando dois programas diferentes precisam trocar informações
- **Bancos de dados:** Alguns bancos de dados armazenam dados diretamente em formato JSON

### Como e a Aparencia de um JSON?

Um JSON se parece muito com um dicionário do Python:

```
{
    "name": "Arroz Integral",
    "price": 8.99,
    "quantity": 50,
    "available": true,
    "categories": ["alimentos", "graos"]
}
```

> **Nota:** Esse exemplo acima e JSON puro, não e código Python. Repare que `true` esta em minusculo — no Python seria `True` com T maiusculo. Vamos ver todas as diferencas a seguir.

---

## Correspondencia JSON e Python

Uma das grandes vantagens de trabalhar com JSON em Python e que as estruturas sao muito parecidas. E como se JSON e Python falassem "dialetos" da mesma lingua — as ideias sao as mesmas, mas algumas palavras mudam.

### Tabela de Correspondencia JSON para Python

| JSON | Python | Exemplo JSON | Exemplo Python |
|------|--------|-------------|----------------|
| object (objeto) | dict (dicionário) | `{"name": "Ana"}` | `{"name": "Ana"}` |
| array (arranjo) | list (lista) | `[1, 2, 3]` | `[1, 2, 3]` |
| string (texto) | str (string) | `"hello"` | `"hello"` |
| number (inteiro) | int (inteiro) | `42` | `42` |
| number (decimal) | float (decimal) | `3.14` | `3.14` |
| true | True | `true` | `True` |
| false | False | `false` | `False` |
| null (nulo/vazio) | None (nenhum) | `null` | `None` |

### Diferencas Importantes

Preste atenção nestas diferencas entre JSON e Python:

1. **Booleanos:** No JSON e `true`/`false` (minusculo). No Python e `True`/`False` (maiusculo).
2. **Valor nulo:** No JSON e `null`. No Python e `None`.
3. **Strings:** No JSON, strings **devem** usar aspas duplas (`"`). No Python, você pode usar aspas simples (`'`) ou duplas (`"`).
4. **Chaves de dicionário:** No JSON, as chaves **devem** ser strings com aspas duplas. No Python, as chaves podem ser de vários tipos.

> **Boa noticia:** O módulo `json` do Python faz todas essas conversoes automaticamente! Você não precisa se preocupar em trocar `True` por `true` manualmente.

---

## O Módulo json do Python

O Python ja vem com um módulo chamado `json` na sua biblioteca padrão — você não precisa instalar nada. Basta importar e usar.

O módulo `json` tem 4 funções principais:

| Função | O que faz | Origem | Destino |
|--------|-----------|--------|---------|
| `json.loads()` | Converte string JSON para Python | String JSON | Objeto Python |
| `json.dumps()` | Converte Python para string JSON | Objeto Python | String JSON |
| `json.load()` | Le JSON de um arquivo | Arquivo JSON | Objeto Python |
| `json.dump()` | Escreve Python em um arquivo JSON | Objeto Python | Arquivo JSON |

> **Dica para lembrar:** As funções com **"s"** no final (`loads`, `dumps`) trabalham com **strings**. As funções sem "s" (`load`, `dump`) trabalham com **arquivos**. O "s" vem de "string".

---

## json.loads() — Converter String JSON para Python

A função `json.loads()` converte uma **string** que contem dados em formato JSON para estruturas do Python (dicionários, listas, etc.).

Pense assim: você recebeu uma **carta** (string JSON) e precisa **abrir o envelope e ler o conteúdo** (converter para Python). O `loads()` faz exatamente isso.

> **Lembrete:** O "s" em `loads` vem de "string" — essa função trabalha com strings.

```python
# Importamos o modulo json da biblioteca padrao
import json

# Uma string contendo dados em formato JSON
# "json_text" = texto em formato JSON
# Repare que e uma string Python normal, com aspas no inicio e no fim
json_text = '{"name": "Arroz Integral", "price": 8.99, "quantity": 50}'

# json.loads() converte a string JSON para um dicionario Python
# "loads" = load string = carregar de string
# "product" = produto
product = json.loads(json_text)

# Agora "product" e um dicionario Python normal!
# Podemos acessar os valores pelas chaves
print(type(product))
print(product)
print(product["name"])
print(product["price"])
```

Saida esperada:
```
<class 'dict'>
{'name': 'Arroz Integral', 'price': 8.99, 'quantity': 50}
Arroz Integral
8.99
```

### Convertendo JSON com Lista (Array)

```python
import json

# String JSON contendo um array (lista)
# "json_text" = texto JSON
json_text = '["Arroz", "Feijao", "Macarrao", "Leite"]'

# json.loads() converte o array JSON para uma lista Python
# "shopping_list" = lista de compras
shopping_list = json.loads(json_text)

# Agora e uma lista Python normal
print(type(shopping_list))
print(shopping_list)

# Podemos percorrer com for
for item in shopping_list:
    # "item" = item/elemento
    print(f"  - {item}")
```

Saida esperada:
```
<class 'list'>
['Arroz', 'Feijao', 'Macarrao', 'Leite']
  - Arroz
  - Feijao
  - Macarrao
  - Leite
```

### Conversão Automática de Tipos

O `json.loads()` converte automaticamente os tipos JSON para os tipos Python correspondentes:

```python
import json

# String JSON com varios tipos de dados
# "json_text" = texto JSON
json_text = '''
{
    "name": "Ana",
    "age": 25,
    "height": 1.65,
    "is_student": true,
    "address": null,
    "hobbies": ["leitura", "programacao", "cozinhar"]
}
'''

# json.loads() converte tudo automaticamente
# "person" = pessoa
person = json.loads(json_text)

# Verificamos o tipo de cada valor
# "key" = chave, "value" = valor
for key, value in person.items():
    # type() retorna o tipo do valor
    print(f"{key}: {value} (tipo: {type(value).__name__})")
```

Saida esperada:
```
name: Ana (tipo: str)
age: 25 (tipo: int)
height: 1.65 (tipo: float)
is_student: True (tipo: bool)
address: None (tipo: NoneType)
hobbies: ['leitura', 'programacao', 'cozinhar'] (tipo: list)
```

> **Observe:** O `true` do JSON virou `True` do Python, e o `null` virou `None`. A conversão e automática!

---

## json.dumps() — Converter Python para String JSON

A função `json.dumps()` faz o caminho inverso: converte estruturas Python (dicionários, listas, etc.) para uma **string** em formato JSON.

Pense assim: você tem informações organizadas (dicionário Python) e precisa **colocar em um envelope padronizado** (string JSON) para enviar para outro programa.

> **Lembrete:** O "s" em `dumps` vem de "string" — essa função produz uma string.

```python
import json

# Um dicionario Python com dados de um produto
# "product" = produto
product = {
    "name": "Feijao Carioca",
    "price": 7.50,
    "quantity": 80,
    "available": True
}

# json.dumps() converte o dicionario para uma string JSON
# "dumps" = dump string = despejar em string
# "json_text" = texto JSON
json_text = json.dumps(product)

# O resultado e uma string
print(type(json_text))
print(json_text)
```

Saida esperada:
```
<class 'str'>
{"name": "Feijao Carioca", "price": 7.5, "quantity": 80, "available": true}
```

> **Observe:** O `True` do Python virou `true` no JSON (minusculo). A conversão e automática!

### Formatacao com indent — JSON Legivel

Por padrão, o `json.dumps()` gera tudo em uma única linha. Para tornar o JSON mais fácil de ler, usamos o parametro `indent` (indentacao):

```python
import json

# Dicionario com dados de um produto
# "product" = produto
product = {
    "name": "Macarrao Espaguete",
    "price": 3.25,
    "quantity": 150,
    "categories": ["alimentos", "massas"],
    "available": True
}

# indent=4 adiciona 4 espacos de indentacao em cada nivel
# Isso torna o JSON muito mais facil de ler
# "json_formatted" = JSON formatado
json_formatted = json.dumps(product, indent=4)

print(json_formatted)
```

Saida esperada:
```
{
    "name": "Macarrao Espaguete",
    "price": 3.25,
    "quantity": 150,
    "categories": [
        "alimentos",
        "massas"
    ],
    "available": true
}
```

> **Dica:** Use `indent=4` sempre que quiser visualizar ou salvar JSON de forma legivel. O número indica quantos espacos de indentacao usar em cada nível.

### Parametro ensure_ascii — Acentos no JSON

Por padrão, o `json.dumps()` converte caracteres especiais (como acentos) para códigos especiais. Para manter os acentos legiveis, use `ensure_ascii=False`:

```python
import json

# Dicionario com texto em portugues (com acentos)
# "message" = mensagem
message = {"greeting": "Ola, como voce esta?", "city": "Sao Paulo"}

# SEM ensure_ascii=False — acentos ficam codificados
# "json_default" = JSON padrao
json_default = json.dumps(message, indent=4)
print("Padrao (com codigos):")
print(json_default)

print()

# COM ensure_ascii=False — acentos ficam legiveis
# "json_readable" = JSON legivel
json_readable = json.dumps(message, indent=4, ensure_ascii=False)
print("Com ensure_ascii=False (legivel):")
print(json_readable)
```

Saida esperada:
```
Padrao (com codigos):
{
    "greeting": "Ola, como voce esta?",
    "city": "Sao Paulo"
}

Com ensure_ascii=False (legivel):
{
    "greeting": "Ola, como voce esta?",
    "city": "Sao Paulo"
}
```

> **Recomendacao:** Sempre use `ensure_ascii=False` quando seus dados contiverem texto em portugues. Isso torna o JSON muito mais fácil de ler.

---

## json.dump() — Escrever Python em Arquivo JSON

A função `json.dump()` (sem "s") escreve dados Python diretamente em um **arquivo** no formato JSON. E como pegar suas informações organizadas e **escrever em um caderno** para guardar.

> **Lembrete:** `dump` (sem "s") trabalha com **arquivos**. `dumps` (com "s") trabalha com **strings**.

```python
import json

# Dados de produtos para salvar em arquivo
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99, "quantity": 100},
    {"name": "Feijao", "price": 7.50, "quantity": 80},
    {"name": "Macarrao", "price": 3.25, "quantity": 150}
]

# Abrimos o arquivo para escrita
# "w" = write = escrita
with open("produtos.json", "w", encoding="utf-8") as file:
    # json.dump() escreve os dados Python no arquivo em formato JSON
    # indent=4 para ficar legivel
    # ensure_ascii=False para manter acentos
    json.dump(products, file, indent=4, ensure_ascii=False)

print("Arquivo 'produtos.json' criado com sucesso!")
```

Saida esperada:
```
Arquivo 'produtos.json' criado com sucesso!
```

Apos executar, o arquivo `produtos.json` tera o seguinte conteúdo:

```
[
    {
        "name": "Arroz",
        "price": 5.99,
        "quantity": 100
    },
    {
        "name": "Feijao",
        "price": 7.50,
        "quantity": 80
    },
    {
        "name": "Macarrao",
        "price": 3.25,
        "quantity": 150
    }
]
```

### Salvando Configuracoes em JSON

Um uso muito comum de arquivos JSON e salvar configuracoes de programas:

```python
import json

# Configuracoes do programa
# "settings" = configuracoes
settings = {
    "app_name": "Meu Programa",
    "version": "1.0",
    "language": "pt-BR",
    "max_items": 100,
    "debug_mode": False
}

# Salvamos as configuracoes em um arquivo JSON
with open("config.json", "w", encoding="utf-8") as file:
    # "file" = arquivo
    json.dump(settings, file, indent=4, ensure_ascii=False)

print("Configuracoes salvas em 'config.json'.")
```

Saida esperada:
```
Configuracoes salvas em 'config.json'.
```

---

## json.load() — Ler JSON de Arquivo

A função `json.load()` (sem "s") le dados de um **arquivo** JSON e converte para estruturas Python. E como **abrir o caderno** onde você guardou informações e ler o que esta escrito.

> **Lembrete:** `load` (sem "s") trabalha com **arquivos**. `loads` (com "s") trabalha com **strings**.

```python
import json

# Primeiro, vamos criar um arquivo JSON para o exemplo
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99, "quantity": 100},
    {"name": "Feijao", "price": 7.50, "quantity": 80}
]

# Salvamos os dados no arquivo
with open("produtos.json", "w", encoding="utf-8") as file:
    json.dump(products, file, indent=4, ensure_ascii=False)

# Agora vamos LER o arquivo JSON
# "r" = read = leitura
with open("produtos.json", "r", encoding="utf-8") as file:
    # json.load() le o arquivo e converte para Python
    # "loaded_products" = produtos carregados
    loaded_products = json.load(file)

# Agora "loaded_products" e uma lista de dicionarios Python
print(type(loaded_products))
print(f"Total de produtos: {len(loaded_products)}")

# Percorremos e exibimos cada produto
for product in loaded_products:
    # "product" = produto
    # "name" = nome, "price" = preco, "quantity" = quantidade
    print(f"  {product['name']} - R$ {product['price']} ({product['quantity']} unidades)")
```

Saida esperada:
```
<class 'list'>
Total de produtos: 2
  Arroz - R$ 5.99 (100 unidades)
  Feijao - R$ 7.50 (80 unidades)
```

### Lendo Configuracoes de um Arquivo JSON

```python
import json

# Primeiro criamos o arquivo de configuracao
# "settings" = configuracoes
settings = {
    "app_name": "Meu Programa",
    "version": "1.0",
    "language": "pt-BR",
    "max_items": 100,
    "debug_mode": False
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(settings, file, indent=4, ensure_ascii=False)

# Agora lemos as configuracoes do arquivo
with open("config.json", "r", encoding="utf-8") as file:
    # "loaded_settings" = configuracoes carregadas
    loaded_settings = json.load(file)

# Acessamos as configuracoes como um dicionario normal
print(f"Nome do app: {loaded_settings['app_name']}")
print(f"Versao: {loaded_settings['version']}")
print(f"Idioma: {loaded_settings['language']}")
print(f"Maximo de itens: {loaded_settings['max_items']}")
print(f"Modo debug: {loaded_settings['debug_mode']}")
```

Saida esperada:
```
Nome do app: Meu Programa
Versao: 1.0
Idioma: pt-BR
Maximo de itens: 100
Modo debug: False
```

---

## Tratamento de Erros — json.JSONDecodeError

Quando você tenta converter uma string que **não e um JSON válido**, o Python gera um erro chamado `json.JSONDecodeError`. E como tentar ler uma carta escrita em uma lingua que você não entende — o Python não consegue interpretar o conteúdo.

### Exemplos de JSON Inválido

```python
import json

# Exemplo 1: falta uma virgula entre os campos
# "invalid_json" = JSON invalido
invalid_json = '{"name": "Arroz" "price": 5.99}'

try:
    # Tentamos converter o JSON invalido
    # "data" = dados
    data = json.loads(invalid_json)
    print(data)
except json.JSONDecodeError as error:
    # "error" = erro
    # O erro nos diz exatamente o que esta errado e onde
    print(f"Erro ao ler JSON: {error}")
```

Saida esperada:
```
Erro ao ler JSON: Expecting ',' delimiter: line 1 column 18 (char 17)
```

### Tratamento Completo com Mensagem Amigavel

```python
import json

def parse_json_safely(json_text):
    """
    Funcao que tenta converter JSON de forma segura.
    "parse" = analisar/interpretar
    "safely" = de forma segura
    "json_text" = texto JSON
    """
    try:
        # Tentamos converter a string JSON
        # "data" = dados
        data = json.loads(json_text)
        # Se deu certo, retornamos os dados
        return data
    except json.JSONDecodeError as error:
        # Se o JSON e invalido, exibimos uma mensagem amigavel
        # "error" = erro
        print(f"O texto fornecido nao e um JSON valido.")
        print(f"Detalhe do erro: {error}")
        # Retornamos None para indicar que falhou
        return None

# Testando com JSON valido
# "valid" = valido
print("Teste 1 — JSON valido:")
valid = '{"name": "Arroz", "price": 5.99}'
# "result" = resultado
result = parse_json_safely(valid)
print(f"Resultado: {result}")

print()

# Testando com JSON invalido (aspas simples em vez de duplas)
# "invalid" = invalido
print("Teste 2 — JSON invalido:")
invalid = "{'name': 'Arroz', 'price': 5.99}"
result = parse_json_safely(invalid)
print(f"Resultado: {result}")
```

Saida esperada:
```
Teste 1 — JSON valido:
Resultado: {'name': 'Arroz', 'price': 5.99}

Teste 2 — JSON invalido:
O texto fornecido nao e um JSON valido.
Detalhe do erro: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
Resultado: None
```

> **Erros comuns que geram JSONDecodeError:**
> - Usar aspas simples em vez de aspas duplas
> - Esquecer virgulas entre campos
> - Ter uma virgula sobrando no final (trailing comma)
> - Texto que não e JSON (como uma frase normal)

### Lendo Arquivo JSON com Tratamento de Erros

Na prática, e importante combinar o tratamento de `json.JSONDecodeError` com `FileNotFoundError`:

```python
import json

def load_json_file(file_path):
    """
    Funcao que le um arquivo JSON de forma segura.
    "load_json_file" = carregar arquivo JSON
    "file_path" = caminho do arquivo
    """
    try:
        # Tentamos abrir e ler o arquivo
        with open(file_path, "r", encoding="utf-8") as file:
            # json.load() le e converte o conteudo
            # "data" = dados
            data = json.load(file)
            return data
    except FileNotFoundError:
        # O arquivo nao foi encontrado
        print(f"Erro: arquivo '{file_path}' nao encontrado.")
        return None
    except json.JSONDecodeError as error:
        # O arquivo existe mas o conteudo nao e JSON valido
        # "error" = erro
        print(f"Erro: o arquivo '{file_path}' nao contem JSON valido.")
        print(f"Detalhe: {error}")
        return None

# Testando com arquivo que nao existe
print("Teste 1 — Arquivo inexistente:")
# "result" = resultado
result = load_json_file("nao_existe.json")
print(f"Resultado: {result}")

print()

# Testando com arquivo valido (vamos criar um primeiro)
with open("teste.json", "w", encoding="utf-8") as file:
    json.dump({"status": "ok"}, file)

print("Teste 2 — Arquivo valido:")
result = load_json_file("teste.json")
print(f"Resultado: {result}")
```

Saida esperada:
```
Teste 1 — Arquivo inexistente:
Erro: arquivo 'nao_existe.json' nao encontrado.
Resultado: None

Teste 2 — Arquivo valido:
Resultado: {'status': 'ok'}
```

---

## JSON Aninhado — Dados Dentro de Dados

Assim como dicionários podem conter outros dicionários (e listas podem conter outras listas), o JSON também pode ter **dados dentro de dados**. Isso e chamado de JSON aninhado (nested JSON).

Pense em uma pasta de arquivos: dentro da pasta principal, você pode ter subpastas, e dentro das subpastas, mais arquivos. O JSON funciona da mesma forma.

```python
import json

# JSON aninhado — um cadastro de loja com produtos organizados por categoria
# "store" = loja
store = {
    "store_name": "Mercado Central",
    "address": {
        "street": "Rua das Flores",
        "number": 123,
        "city": "Sao Paulo"
    },
    "products": [
        {"name": "Arroz", "price": 5.99, "category": "alimentos"},
        {"name": "Sabonete", "price": 2.50, "category": "higiene"},
        {"name": "Caderno", "price": 12.00, "category": "papelaria"}
    ]
}

# Convertemos para JSON formatado
# "json_text" = texto JSON
json_text = json.dumps(store, indent=4, ensure_ascii=False)
print(json_text)
```

Saida esperada:
```
{
    "store_name": "Mercado Central",
    "address": {
        "street": "Rua das Flores",
        "number": 123,
        "city": "Sao Paulo"
    },
    "products": [
        {
            "name": "Arroz",
            "price": 5.99,
            "category": "alimentos"
        },
        {
            "name": "Sabonete",
            "price": 2.50,
            "category": "higiene"
        },
        {
            "name": "Caderno",
            "price": 12.00,
            "category": "papelaria"
        }
    ]
}
```

### Acessando Dados em JSON Aninhado

```python
import json

# JSON aninhado como string
# "json_text" = texto JSON
json_text = '''
{
    "store_name": "Mercado Central",
    "address": {
        "street": "Rua das Flores",
        "number": 123,
        "city": "Sao Paulo"
    },
    "products": [
        {"name": "Arroz", "price": 5.99},
        {"name": "Feijao", "price": 7.50}
    ]
}
'''

# Convertemos para Python
# "store" = loja
store = json.loads(json_text)

# Acessando dados simples
# "store_name" = nome da loja
print(f"Loja: {store['store_name']}")

# Acessando dados aninhados (dicionario dentro de dicionario)
# "address" = endereco, "street" = rua, "city" = cidade
print(f"Rua: {store['address']['street']}")
print(f"Cidade: {store['address']['city']}")

# Acessando dados em lista aninhada
# "products" = produtos
print(f"Primeiro produto: {store['products'][0]['name']}")
print(f"Preco do segundo produto: R$ {store['products'][1]['price']}")

# Percorrendo a lista de produtos
print("\nTodos os produtos:")
for product in store["products"]:
    # "product" = produto
    print(f"  {product['name']} - R$ {product['price']}")
```

Saida esperada:
```
Loja: Mercado Central
Rua: Rua das Flores
Cidade: Sao Paulo
Primeiro produto: Arroz
Preco do segundo produto: R$ 7.5

Todos os produtos:
  Arroz - R$ 5.99
  Feijao - R$ 7.5
```

---

## Exemplo Prático Completo — Cadastro de Produtos em JSON

Vamos juntar tudo em um exemplo prático: um programa que gerência um cadastro de produtos usando um arquivo JSON para guardar os dados.

```python
import json

def load_products(file_path):
    """
    Carrega a lista de produtos de um arquivo JSON.
    "load_products" = carregar produtos
    "file_path" = caminho do arquivo
    """
    try:
        # Tentamos abrir e ler o arquivo
        with open(file_path, "r", encoding="utf-8") as file:
            # json.load() le o arquivo e converte para Python
            # "products" = produtos
            products = json.load(file)
            return products
    except FileNotFoundError:
        # Se o arquivo nao existe, retornamos lista vazia
        print("Arquivo nao encontrado. Iniciando lista vazia.")
        return []
    except json.JSONDecodeError:
        # Se o arquivo tem conteudo invalido
        print("Erro no formato do arquivo. Iniciando lista vazia.")
        return []


def save_products(products, file_path):
    """
    Salva a lista de produtos em um arquivo JSON.
    "save_products" = salvar produtos
    "products" = produtos, "file_path" = caminho do arquivo
    """
    # Abrimos o arquivo para escrita
    with open(file_path, "w", encoding="utf-8") as file:
        # json.dump() escreve os dados no arquivo
        # indent=4 para ficar legivel
        # ensure_ascii=False para manter acentos
        json.dump(products, file, indent=4, ensure_ascii=False)


def show_products(products):
    """
    Exibe todos os produtos na tela.
    "show_products" = mostrar produtos
    """
    # Verificamos se a lista esta vazia
    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return

    # Percorremos e exibimos cada produto
    print("\n--- Lista de Produtos ---")
    for product in products:
        # "product" = produto
        # "name" = nome, "price" = preco, "quantity" = quantidade
        print(f"  ID: {product['id']} | {product['name']} | "
              f"R$ {product['price']:.2f} | Qtd: {product['quantity']}")
    print("-------------------------")


# --- Programa principal ---

# Caminho do arquivo JSON
# "file_path" = caminho do arquivo
file_path = "produtos_cadastro.json"

# Carregamos os produtos existentes (ou lista vazia)
# "products" = produtos
products = load_products(file_path)

# Adicionamos alguns produtos
# "new_product" = novo produto
new_product_1 = {"id": 1, "name": "Arroz", "price": 5.99, "quantity": 100}
new_product_2 = {"id": 2, "name": "Feijao", "price": 7.50, "quantity": 80}
new_product_3 = {"id": 3, "name": "Macarrao", "price": 3.25, "quantity": 150}

# append() adiciona cada produto a lista
products.append(new_product_1)
products.append(new_product_2)
products.append(new_product_3)

# Salvamos no arquivo JSON
save_products(products, file_path)
print(f"{len(products)} produto(s) salvo(s) em '{file_path}'.")

# Exibimos os produtos
show_products(products)

# Carregamos novamente do arquivo para confirmar que salvou
# "loaded" = carregados
loaded = load_products(file_path)
print(f"\nProdutos carregados do arquivo: {len(loaded)}")
```

Saida esperada:
```
Arquivo nao encontrado. Iniciando lista vazia.
3 produto(s) salvo(s) em 'produtos_cadastro.json'.

--- Lista de Produtos ---
  ID: 1 | Arroz | R$ 5.99 | Qtd: 100
  ID: 2 | Feijao | R$ 7.50 | Qtd: 80
  ID: 3 | Macarrao | R$ 3.25 | Qtd: 150
-------------------------

Produtos carregados do arquivo: 3
```

---

## Resumo dos Principais Comandos

| Comando | O que faz | Exemplo |
|---------|-----------|---------|
| `import json` | Importa o módulo JSON | `import json` |
| `json.loads(string)` | String JSON para Python | `data = json.loads('{"a": 1}')` |
| `json.dumps(objeto)` | Python para string JSON | `text = json.dumps({"a": 1})` |
| `json.dumps(obj, indent=4)` | JSON formatado (legivel) | `text = json.dumps(data, indent=4)` |
| `json.dumps(obj, ensure_ascii=False)` | Manter acentos no JSON | `text = json.dumps(data, ensure_ascii=False)` |
| `json.load(arquivo)` | Ler JSON de arquivo | `data = json.load(file)` |
| `json.dump(objeto, arquivo)` | Escrever JSON em arquivo | `json.dump(data, file, indent=4)` |

---

## Para Saber Mais

- [W3Schools — Python JSON](https://www.w3schools.com/python/python_json.asp)
  _Aqui você encontra exemplos interativos de como trabalhar com JSON em Python_

- [W3Schools — JSON Introduction](https://www.w3schools.com/js/js_json_intro.asp)
  _Introducao ao formato JSON com exemplos visuais e explicacoes simples_

- [Documentação Oficial Python — Módulo json](https://docs.python.org/pt-br/3/library/json.html)
  _Referencia completa sobre todas as funções do módulo json em Python_

- [W3Schools — JSON Syntax](https://www.w3schools.com/js/js_json_syntax.asp)
  _Explicacao detalhada das regras de sintaxe do formato JSON_

- [Documentação Oficial Python — Tutorial de Entrada e Saida](https://docs.python.org/pt-br/3/tutorial/inputoutput.html)
  _Referencia sobre leitura e escrita de dados, incluindo JSON_

---

## Perguntas Frequentes (FAQ)

**P: O que e JSON?**
R: JSON e a sigla para JavaScript Object Notation (Notação de Objetos JavaScript). E um formato de texto leve e padronizado para organizar e trocar dados entre programas. Apesar de ter "JavaScript" no nome, ele e usado por praticamente todas as linguagens de programação, incluindo Python.

**P: Por que o JSON tem "JavaScript" no nome se funciona com Python?**
R: O JSON foi criado originalmente como parte da linguagem JavaScript, mas rapidamente se tornou um padrão universal. Hoje, ele e independente de qualquer linguagem. E como o sistema metrico — foi criado na Franca, mas e usado no mundo inteiro.

**P: Qual a diferença entre JSON e um dicionário Python?**
R: Eles sao muito parecidos, mas tem diferencas importantes. No JSON: strings devem usar aspas duplas, booleanos sao `true`/`false` (minusculo), e o valor nulo e `null`. No Python: strings podem usar aspas simples ou duplas, booleanos sao `True`/`False` (maiusculo), e o valor nulo e `None`. O módulo `json` faz essas conversoes automaticamente.

**P: Qual a diferença entre json.loads() e json.load()?**
R: A diferença e o "s" no final. `json.loads()` (com "s" de "string") converte uma **string** JSON para Python. `json.load()` (sem "s") le dados de um **arquivo** JSON. Use `loads` quando você ja tem o texto JSON em uma variável, e `load` quando quer ler de um arquivo.

**P: Qual a diferença entre json.dumps() e json.dump()?**
R: Mesma lógica: `json.dumps()` (com "s") converte Python para uma **string** JSON. `json.dump()` (sem "s") escreve dados Python diretamente em um **arquivo** JSON. Use `dumps` quando quer o texto JSON em uma variável, e `dump` quando quer salvar em arquivo.

**P: O que e o parametro indent?**
R: O `indent` (indentacao) controla a formatacao do JSON gerado. Sem `indent`, o JSON fica tudo em uma linha so. Com `indent=4`, cada nível de dados recebe 4 espacos de indentacao, tornando o JSON muito mais fácil de ler. Use `indent=4` sempre que quiser visualizar ou salvar JSON de forma legivel.

**P: O que e ensure_ascii=False?**
R: Por padrão, o `json.dumps()` converte caracteres especiais (como acentos) para códigos especiais. Quando você usa `ensure_ascii=False`, os acentos e caracteres especiais ficam legiveis no JSON. Sempre use esse parametro quando seus dados contiverem texto em portugues.

**P: O que e json.JSONDecodeError?**
R: E o erro que o Python gera quando você tenta converter uma string que não e um JSON válido. Pode acontecer por vários motivos: aspas simples em vez de duplas, virgulas faltando, texto que não e JSON, entre outros. Use `try/except` para tratar esse erro de forma amigavel.

**P: Posso usar aspas simples no JSON?**
R: Não! O JSON exige aspas **duplas** para strings e chaves. Aspas simples não sao validas em JSON. Essa e uma das diferencas entre JSON e dicionários Python, onde você pode usar aspas simples. Se você tentar usar aspas simples, o `json.loads()` vai gerar um `JSONDecodeError`.

**P: O que acontece se eu tentar converter um tipo que o JSON não suporta?**
R: O Python gera um erro `TypeError`. Por exemplo, se você tentar converter um `set` (conjunto) ou um objeto de uma classe personalizada, o `json.dumps()` não vai conseguir. O JSON so suporta: dicionários, listas, strings, números, booleanos e `None`.

**P: JSON e a mesma coisa que um arquivo .json?**
R: Não exatamente. JSON e o **formato** (as regras de como os dados sao organizados). Um arquivo `.json` e um **arquivo de texto** que contem dados nesse formato. Você pode ter dados JSON dentro de uma string Python sem precisar de um arquivo.

**P: Posso ter comentários dentro de um arquivo JSON?**
R: Não! O formato JSON não suporta comentários. Diferente do Python (que usa `#`), o JSON e puramente dados, sem espaco para anotacoes. Se você precisar documentar algo, faca isso fora do arquivo JSON ou adicione um campo como `"_comment": "explicacao aqui"`.

**P: O que e JSON aninhado?**
R: E quando você tem dados dentro de dados — por exemplo, um dicionário que contem outro dicionário, ou uma lista que contem dicionários. E como uma pasta de arquivos que contem subpastas. Para acessar dados aninhados, você encadeia as chaves: `dados["endereco"]["cidade"]`.

**P: Como sei se meu JSON e válido?**
R: Você pode tentar converter com `json.loads()` dentro de um `try/except`. Se não gerar erro, o JSON e válido. Também existem sites na internet como o JSONLint (jsonlint.com) onde você pode colar seu JSON e verificar se esta correto.

**P: Preciso sempre usar encoding="utf-8" ao trabalhar com JSON?**
R: E altamente recomendado, especialmente quando seus dados contiverem texto em portugues com acentos. O `encoding="utf-8"` garante que os caracteres especiais sejam lidos e escritos corretamente.

**P: Qual a diferença entre JSON e CSV?**
R: CSV (Comma-Separated Values) e um formato tabular simples — como uma planilha com linhas e colunas. JSON e mais flexível: permite dados aninhados (dados dentro de dados), tipos variados e estruturas complexas. Use CSV para dados simples em formato de tabela, e JSON para dados mais complexos ou estruturados.

**P: O json.dump() apaga o conteúdo anterior do arquivo?**
R: Depende do modo de abertura. Se você abrir com `"w"` (write), sim, o conteúdo anterior e apagado. Para atualizar dados em um arquivo JSON, o padrão e: ler o arquivo inteiro, modificar os dados em Python, e salvar tudo de volta. Não existe um modo "append" para JSON como existe para arquivos de texto.

**P: Posso salvar uma lista diretamente em JSON?**
R: Sim! O JSON aceita tanto objetos (dicionários) quanto arrays (listas) como elemento principal. Você pode salvar `[1, 2, 3]` ou `[{"name": "Ana"}, {"name": "Bruno"}]` diretamente em um arquivo JSON.

**P: E normal ter dificuldade com JSON no inicio?**
R: Sim, completamente normal! JSON e um conceito novo que envolve entender um formato de dados e como converter entre formatos. Com prática, trabalhar com JSON se torna tao natural quanto trabalhar com dicionários. Não desanime — cada erro e uma oportunidade de aprender.

**P: Por que o JSON e importante para o projeto CRUD?**
R: No projeto CRUD que você vai construir nos proximos módulos, o JSON sera fundamental. Quando você criar uma API com FastAPI, os dados serao enviados e recebidos em formato JSON. Entender JSON agora vai facilitar muito o trabalho com APIs mais adiante.

**P: Posso usar json.dumps() para exibir dicionários de forma bonita no terminal?**
R: Sim! Essa e uma otima dica. Em vez de usar `print(dicionario)`, você pode usar `print(json.dumps(dicionario, indent=4, ensure_ascii=False))` para ver o dicionário formatado de forma muito mais legivel. Muitos programadores usam essa técnica no dia a dia.

---

## Exercícios de Fixacao

Pratique o que aprendeu com os exercícios do módulo:

[Exercícios do Módulo 21 — Manipulação JSON](21-manipulação-json-exercícios.md)

---

[<- Anterior: Leitura e Escrita de Arquivos](20-leitura-escrita-arquivos.md) | [Glossário](00-glossário.md) | [Próximo: Classes e Objetos ->](22-classes-objetos.md)
