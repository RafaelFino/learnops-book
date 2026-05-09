# Exercícios — Módulo 21: Manipulação JSON

[<- Voltar ao Módulo 21](21-manipulacao-json.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-21/` e execute com `python3 nome_do_arquivo.py`. Verifique os arquivos JSON criados na pasta apos a execução.

---

## Exercício 1 — Converter String JSON para Dicionário — Nível: Básico
**Conceitos:** json.loads, dicionário, acesso por chave

### Enunciado
Crie um programa que tenha uma string JSON representando um livro (com título, autor e ano) e converta para um dicionário Python. Exiba cada informação separadamente.

### Dicas
- Use `json.loads()` para converter a string JSON
- Lembre-se de importar o módulo `json`
- Acesse os valores usando as chaves do dicionário

### Proposta de Teste
- String JSON: `{"title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}`
- Saida esperada:
  ```
  Título: Dom Casmurro
  Autor: Machado de Assis
  Ano: 1899
  ```
- Caso de borda: tente com um livro sem o campo "year" — o programa deve funcionar para os campos existentes

### Resposta Comentada
```python
# Importamos o modulo json da biblioteca padrao
import json

# String contendo dados de um livro em formato JSON
# "json_text" = texto JSON
# "title" = titulo, "author" = autor, "year" = ano
json_text = '{"title": "Dom Casmurro", "author": "Machado de Assis", "year": 1899}'

# json.loads() converte a string JSON para um dicionario Python
# "loads" = load string = carregar de string
# "book" = livro
book = json.loads(json_text)

# Exibimos cada informacao acessando pelas chaves
# "title" = titulo
print(f"Titulo: {book['title']}")
# "author" = autor
print(f"Autor: {book['author']}")
# "year" = ano
print(f"Ano: {book['year']}")
```

---

## Exercício 2 — Converter Dicionário Python para JSON Formatado — Nível: Básico
**Conceitos:** json.dumps, indent, ensure_ascii

### Enunciado
Crie um dicionário Python com dados de um aluno (nome, idade, cidade e se esta matriculado). Converta para uma string JSON formatada com indentacao e exiba no terminal.

### Dicas
- Use `json.dumps()` com `indent=4` para formatar
- Use `ensure_ascii=False` para manter acentos legiveis
- O valor booleano `True` do Python sera convertido para `true` no JSON

### Proposta de Teste
- Dicionário: `{"name": "Carlos", "age": 20, "city": "Belo Horizonte", "enrolled": True}`
- Saida esperada (JSON formatado com 4 espacos de indentacao):
  ```
  {
      "name": "Carlos",
      "age": 20,
      "city": "Belo Horizonte",
      "enrolled": true
  }
  ```
- Caso de borda: use `enrolled: False` — deve aparecer `false` no JSON

### Resposta Comentada
```python
# Importamos o modulo json
import json

# Criamos um dicionario com dados de um aluno
# "student" = estudante/aluno
# "name" = nome, "age" = idade, "city" = cidade, "enrolled" = matriculado
student = {
    "name": "Carlos",
    "age": 20,
    "city": "Belo Horizonte",
    "enrolled": True
}

# json.dumps() converte o dicionario para string JSON
# "dumps" = dump string = despejar em string
# indent=4 formata com 4 espacos de indentacao
# ensure_ascii=False mantem acentos legiveis
# "json_text" = texto JSON
json_text = json.dumps(student, indent=4, ensure_ascii=False)

# Exibimos o JSON formatado
print(json_text)
```

---

## Exercício 3 — Salvar Lista de Produtos em Arquivo JSON — Nível: Básico
**Conceitos:** json.dump, open, write, lista de dicionários

### Enunciado
Crie uma lista com 3 produtos (cada um com nome, preco e quantidade). Salve essa lista em um arquivo chamado `produtos.json` com formatacao legivel.

### Dicas
- Use `open()` com modo `"w"` e `encoding="utf-8"`
- Use `json.dump()` (sem "s") para escrever no arquivo
- Use `indent=4` e `ensure_ascii=False`

### Proposta de Teste
- Apos executar, o arquivo `produtos.json` deve existir na pasta
- Abra o arquivo no VSCode — deve conter os 3 produtos formatados
- Caso de borda: execute o programa duas vezes — o arquivo deve conter apenas os 3 produtos (modo "w" sobrescreve)

### Resposta Comentada
```python
# Importamos o modulo json
import json

# Criamos uma lista de dicionarios com dados de produtos
# "products" = produtos
# "name" = nome, "price" = preco, "quantity" = quantidade
products = [
    {"name": "Arroz", "price": 5.99, "quantity": 100},
    {"name": "Feijao", "price": 7.50, "quantity": 80},
    {"name": "Macarrao", "price": 3.25, "quantity": 150}
]

# Abrimos o arquivo para escrita
# "w" = write = escrita
with open("produtos.json", "w", encoding="utf-8") as file:
    # json.dump() escreve os dados Python no arquivo em formato JSON
    # "file" = arquivo
    # indent=4 para ficar legivel
    # ensure_ascii=False para manter acentos
    json.dump(products, file, indent=4, ensure_ascii=False)

# Confirmamos que o arquivo foi criado
print("Arquivo 'produtos.json' criado com sucesso!")
```

---

## Exercício 4 — Ler Arquivo JSON e Exibir Dados — Nível: Básico
**Conceitos:** json.load, open, read, for

### Enunciado
Crie um programa que primeiro salve uma lista de 3 frutas com nome e preco em um arquivo `frutas.json`. Depois, leia o arquivo e exiba cada fruta com seu preco formatado.

### Dicas
- Use `json.dump()` para salvar e `json.load()` para ler
- Abra o arquivo duas vezes: uma para escrever e outra para ler
- Use f-string com `:.2f` para formatar o preco com 2 casas decimais

### Proposta de Teste
- Frutas: Maca (R$ 4.50), Banana (R$ 2.99), Laranja (R$ 3.75)
- Saida esperada:
  ```
  Maca - R$ 4.50
  Banana - R$ 2.99
  Laranja - R$ 3.75
  ```
- Caso de borda: adicione uma fruta com preco 0.00 — deve exibir `R$ 0.00`

### Resposta Comentada
```python
# Importamos o modulo json
import json

# Criamos uma lista de frutas com nome e preco
# "fruits" = frutas
# "name" = nome, "price" = preco
fruits = [
    {"name": "Maca", "price": 4.50},
    {"name": "Banana", "price": 2.99},
    {"name": "Laranja", "price": 3.75}
]

# Salvamos a lista no arquivo JSON
# "w" = write = escrita
with open("frutas.json", "w", encoding="utf-8") as file:
    # json.dump() escreve os dados no arquivo
    # "file" = arquivo
    json.dump(fruits, file, indent=4, ensure_ascii=False)

# Lemos o arquivo JSON
# "r" = read = leitura
with open("frutas.json", "r", encoding="utf-8") as file:
    # json.load() le o arquivo e converte para Python
    # "loaded_fruits" = frutas carregadas
    loaded_fruits = json.load(file)

# Exibimos cada fruta com preco formatado
for fruit in loaded_fruits:
    # "fruit" = fruta
    # :.2f formata o numero com 2 casas decimais
    print(f"{fruit['name']} - R$ {fruit['price']:.2f}")
```

---

## Exercício 5 — Converter Lista JSON para Python e Calcular Total — Nível: Intermediario
**Conceitos:** json.loads, for, acumulador, lista

### Enunciado
Crie um programa que receba uma string JSON contendo uma lista de precos de produtos e calcule o total e a media dos precos.

### Dicas
- Use `json.loads()` para converter a string JSON em lista Python
- Use um acumulador para somar os precos
- Divida o total pela quantidade para obter a media

### Proposta de Teste
- String JSON: `[12.50, 8.99, 25.00, 3.75, 15.80]`
- Saida esperada:
  ```
  Total: R$ 66.04
  Media: R$ 13.21
  ```
- Caso de borda: lista com um único preco `[10.00]` — Total: R$ 10.00, Media: R$ 10.00

### Resposta Comentada
```python
# Importamos o modulo json
import json

# String JSON contendo uma lista de precos
# "json_text" = texto JSON
json_text = '[12.50, 8.99, 25.00, 3.75, 15.80]'

# json.loads() converte a string JSON para uma lista Python
# "prices" = precos
prices = json.loads(json_text)

# Calculamos o total somando todos os precos
# "total" = total (acumulador)
total = 0
for price in prices:
    # "price" = preco — somamos cada preco ao total
    total = total + price

# Calculamos a media dividindo o total pela quantidade
# "average" = media
# len() retorna a quantidade de elementos na lista
average = total / len(prices)

# Exibimos os resultados formatados com 2 casas decimais
print(f"Total: R$ {total:.2f}")
print(f"Media: R$ {average:.2f}")
```

---

## Exercício 6 — Tratar JSON Inválido com try/except — Nível: Intermediario
**Conceitos:** json.loads, json.JSONDecodeError, try/except

### Enunciado
Crie uma função que receba uma string e tente converter para JSON. Se a string for um JSON válido, exiba os dados. Se for inválido, exiba uma mensagem de erro amigavel informando o problema.

### Dicas
- Use `try/except json.JSONDecodeError` para capturar o erro
- A variável do erro contem detalhes sobre o que esta errado
- Teste com pelo menos uma string valida e uma inválida

### Proposta de Teste
- String valida: `{"name": "Ana", "age": 25}` — deve exibir os dados normalmente
- String inválida: `{"name": "Ana" "age": 25}` (falta virgula) — deve exibir mensagem de erro
- Caso de borda: string vazia `""` — deve exibir mensagem de erro

### Resposta Comentada
```python
# Importamos o modulo json
import json

def try_parse_json(text):
    """
    Tenta converter uma string para JSON de forma segura.
    "try_parse_json" = tentar analisar JSON
    "text" = texto a ser analisado
    """
    try:
        # Tentamos converter a string para Python
        # "data" = dados
        data = json.loads(text)
        # Se deu certo, exibimos os dados
        print("JSON valido! Dados:")
        # json.dumps() formata para exibicao legivel
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except json.JSONDecodeError as error:
        # Se o JSON e invalido, exibimos mensagem amigavel
        # "error" = erro
        print(f"JSON invalido! Erro: {error}")

# Teste 1 — JSON valido
# "valid_json" = JSON valido
print("--- Teste 1: JSON valido ---")
valid_json = '{"name": "Ana", "age": 25}'
try_parse_json(valid_json)

print()

# Teste 2 — JSON invalido (falta virgula)
# "invalid_json" = JSON invalido
print("--- Teste 2: JSON invalido ---")
invalid_json = '{"name": "Ana" "age": 25}'
try_parse_json(invalid_json)

print()

# Teste 3 — String vazia
# "empty" = vazio
print("--- Teste 3: String vazia ---")
empty = ""
try_parse_json(empty)
```

---

## Exercício 7 — Adicionar Produto a Arquivo JSON Existente — Nível: Intermediario
**Conceitos:** json.load, json.dump, append, leitura e escrita

### Enunciado
Crie um programa que: (1) crie um arquivo JSON com 2 produtos, (2) leia o arquivo, (3) adicione um novo produto a lista, e (4) salve a lista atualizada de volta no arquivo. Exiba a lista antes e depois da adicao.

### Dicas
- Leia o arquivo com `json.load()`, modifique a lista em Python, e salve com `json.dump()`
- Use `append()` para adicionar o novo produto a lista
- Abra o arquivo duas vezes: uma para ler e outra para escrever

### Proposta de Teste
- Produtos iniciais: Arroz (R$ 5.99), Feijao (R$ 7.50)
- Novo produto: Leite (R$ 4.80)
- Saida esperada: lista com 3 produtos apos a adicao
- Caso de borda: execute o programa duas vezes — o arquivo deve ter apenas 3 produtos (não 4), pois o programa recria o arquivo inicial

### Resposta Comentada
```python
# Importamos o modulo json
import json

# Criamos a lista inicial com 2 produtos
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99},
    {"name": "Feijao", "price": 7.50}
]

# Salvamos a lista inicial no arquivo
# "w" = write = escrita
with open("estoque.json", "w", encoding="utf-8") as file:
    # "file" = arquivo
    json.dump(products, file, indent=4, ensure_ascii=False)

# Lemos o arquivo para obter a lista atual
# "r" = read = leitura
with open("estoque.json", "r", encoding="utf-8") as file:
    # "current_products" = produtos atuais
    current_products = json.load(file)

# Exibimos a lista antes da adicao
print("Antes da adicao:")
for product in current_products:
    # "product" = produto
    print(f"  {product['name']} - R$ {product['price']:.2f}")

# Criamos o novo produto
# "new_product" = novo produto
new_product = {"name": "Leite", "price": 4.80}

# Adicionamos o novo produto a lista
# append() adiciona ao final da lista
current_products.append(new_product)

# Salvamos a lista atualizada de volta no arquivo
with open("estoque.json", "w", encoding="utf-8") as file:
    json.dump(current_products, file, indent=4, ensure_ascii=False)

# Exibimos a lista depois da adicao
print("\nDepois da adicao:")
for product in current_products:
    print(f"  {product['name']} - R$ {product['price']:.2f}")

# Informamos o total
print(f"\nTotal de produtos: {len(current_products)}")
```

---

## Exercício 8 — Converter JSON Aninhado e Acessar Dados — Nível: Intermediario
**Conceitos:** json.loads, JSON aninhado, acesso encadeado

### Enunciado
Crie um programa que tenha uma string JSON representando uma escola com nome, cidade e uma lista de alunos (cada aluno com nome e nota). Converta para Python e exiba: o nome da escola, a cidade, e o nome e nota de cada aluno.

### Dicas
- Use `json.loads()` para converter a string JSON
- Acesse dados aninhados encadeando chaves: `dados["chave1"]["chave2"]`
- Use um loop `for` para percorrer a lista de alunos

### Proposta de Teste
- Escola: "Escola Futuro", Cidade: "Curitiba", Alunos: Ana (8.5), Bruno (7.0), Carla (9.5)
- Saida esperada:
  ```
  Escola: Escola Futuro
  Cidade: Curitiba
  Alunos:
    Ana - Nota: 8.5
    Bruno - Nota: 7.0
    Carla - Nota: 9.5
  ```
- Caso de borda: escola sem alunos (lista vazia) — deve exibir "Nenhum aluno cadastrado."

### Resposta Comentada
```python
# Importamos o modulo json
import json

# String JSON com dados aninhados de uma escola
# "json_text" = texto JSON
json_text = '''
{
    "school_name": "Escola Futuro",
    "city": "Curitiba",
    "students": [
        {"name": "Ana", "grade": 8.5},
        {"name": "Bruno", "grade": 7.0},
        {"name": "Carla", "grade": 9.5}
    ]
}
'''

# json.loads() converte a string JSON para dicionario Python
# "school" = escola
school = json.loads(json_text)

# Acessamos os dados simples
# "school_name" = nome da escola
print(f"Escola: {school['school_name']}")
# "city" = cidade
print(f"Cidade: {school['city']}")

# Acessamos a lista aninhada de alunos
# "students" = estudantes/alunos
print("Alunos:")
if len(school["students"]) == 0:
    # Se a lista de alunos estiver vazia
    print("  Nenhum aluno cadastrado.")
else:
    # Percorremos cada aluno na lista
    for student in school["students"]:
        # "student" = estudante/aluno
        # "name" = nome, "grade" = nota
        print(f"  {student['name']} - Nota: {student['grade']}")
```

---

## Exercício 9 — Filtrar Dados de um JSON e Salvar Resultado — Nível: Intermediario
**Conceitos:** json.load, json.dump, for, if, filtragem

### Enunciado
Crie um arquivo JSON com 5 produtos (nome, preco, quantidade). Depois, leia o arquivo, filtre apenas os produtos com preco acima de R$ 5.00, e salve os produtos filtrados em um novo arquivo chamado `produtos_caros.json`.

### Dicas
- Use `json.load()` para ler e `json.dump()` para salvar
- Use um loop `for` com `if` para filtrar os produtos
- Crie uma lista vazia e adicione apenas os produtos que atendem ao critério

### Proposta de Teste
- Produtos: Arroz (5.99), Sal (1.50), Feijao (7.50), Açúcar (3.25), Leite (4.80)
- Produtos com preco > 5.00: Arroz e Feijao
- Saida esperada: arquivo `produtos_caros.json` com 2 produtos
- Caso de borda: se nenhum produto tiver preco > 5.00, o arquivo deve conter uma lista vazia `[]`

### Resposta Comentada
```python
# Importamos o modulo json
import json

# Criamos a lista de produtos
# "products" = produtos
products = [
    {"name": "Arroz", "price": 5.99, "quantity": 100},
    {"name": "Sal", "price": 1.50, "quantity": 200},
    {"name": "Feijao", "price": 7.50, "quantity": 80},
    {"name": "Acucar", "price": 3.25, "quantity": 120},
    {"name": "Leite", "price": 4.80, "quantity": 60}
]

# Salvamos todos os produtos no arquivo original
with open("todos_produtos.json", "w", encoding="utf-8") as file:
    # "file" = arquivo
    json.dump(products, file, indent=4, ensure_ascii=False)

# Lemos o arquivo original
with open("todos_produtos.json", "r", encoding="utf-8") as file:
    # "loaded_products" = produtos carregados
    loaded_products = json.load(file)

# Filtramos apenas os produtos com preco acima de 5.00
# "expensive_products" = produtos caros — lista vazia para receber os filtrados
expensive_products = []

for product in loaded_products:
    # "product" = produto
    # Verificamos se o preco e maior que 5.00
    if product["price"] > 5.00:
        # Adicionamos o produto a lista de caros
        expensive_products.append(product)

# Salvamos os produtos filtrados em novo arquivo
with open("produtos_caros.json", "w", encoding="utf-8") as file:
    json.dump(expensive_products, file, indent=4, ensure_ascii=False)

# Exibimos o resultado
print(f"Total de produtos: {len(loaded_products)}")
print(f"Produtos com preco > R$ 5.00: {len(expensive_products)}")
for product in expensive_products:
    print(f"  {product['name']} - R$ {product['price']:.2f}")
```

---

## Exercício 10 — Ler JSON de Arquivo com Tratamento de Erros Completo — Nível: Intermediario
**Conceitos:** json.load, FileNotFoundError, json.JSONDecodeError, try/except

### Enunciado
Crie uma função `load_data` que receba o nome de um arquivo e tente ler seu conteúdo como JSON. A função deve tratar dois tipos de erro: arquivo não encontrado e JSON inválido. Teste a função com 3 cenários: arquivo válido, arquivo inexistente e arquivo com conteúdo inválido.

### Dicas
- Use `try/except` com dois blocos `except` (um para cada tipo de erro)
- Retorne `None` quando houver erro e os dados quando der certo
- Crie um arquivo com conteúdo inválido para testar o `JSONDecodeError`

### Proposta de Teste
- Arquivo válido com `{"status": "ok"}` — deve retornar o dicionário
- Arquivo inexistente — deve exibir "Arquivo não encontrado" e retornar None
- Arquivo com conteúdo `{invalido}` — deve exibir "JSON inválido" e retornar None

### Resposta Comentada
```python
# Importamos o modulo json
import json

def load_data(file_path):
    """
    Carrega dados de um arquivo JSON com tratamento de erros.
    "load_data" = carregar dados
    "file_path" = caminho do arquivo
    """
    try:
        # Tentamos abrir e ler o arquivo
        with open(file_path, "r", encoding="utf-8") as file:
            # json.load() le e converte o conteudo
            # "data" = dados
            data = json.load(file)
            # Se deu certo, retornamos os dados
            return data
    except FileNotFoundError:
        # O arquivo nao foi encontrado
        print(f"Erro: arquivo '{file_path}' nao encontrado.")
        # Retornamos None para indicar falha
        return None
    except json.JSONDecodeError as error:
        # O conteudo do arquivo nao e JSON valido
        # "error" = erro
        print(f"Erro: JSON invalido em '{file_path}'. Detalhe: {error}")
        return None

# --- Preparacao dos arquivos de teste ---

# Arquivo valido
with open("valido.json", "w", encoding="utf-8") as file:
    # Escrevemos um JSON valido
    json.dump({"status": "ok"}, file)

# Arquivo com conteudo invalido
with open("invalido.json", "w", encoding="utf-8") as file:
    # Escrevemos texto que NAO e JSON valido
    file.write("{invalido}")

# --- Testes ---

# Teste 1 — Arquivo valido
print("Teste 1 — Arquivo valido:")
# "result" = resultado
result = load_data("valido.json")
print(f"Resultado: {result}")

print()

# Teste 2 — Arquivo inexistente
print("Teste 2 — Arquivo inexistente:")
result = load_data("nao_existe.json")
print(f"Resultado: {result}")

print()

# Teste 3 — Arquivo com JSON invalido
print("Teste 3 — JSON invalido:")
result = load_data("invalido.json")
print(f"Resultado: {result}")
```

---

## Exercício 11 — Converter Cadastro de Alunos entre JSON e Python — Nível: Avancado
**Conceitos:** json.loads, json.dumps, json.dump, JSON aninhado, for, funções

### Enunciado
Crie um programa com duas funções: (1) uma que receba uma string JSON com uma lista de alunos (nome, notas como lista) e calcule a media de cada aluno, e (2) outra que salve o resultado (alunos com suas medias) em um arquivo JSON. Exiba o resultado no terminal e salve no arquivo.

### Dicas
- Cada aluno tem uma lista de notas — use `sum()` e `len()` para calcular a media
- Crie um novo dicionário para cada aluno com o campo "average" (media) adicionado
- Use `json.dump()` para salvar o resultado no arquivo

### Proposta de Teste
- Alunos: Ana (notas: 8.0, 7.5, 9.0), Bruno (notas: 6.0, 5.5, 7.0), Carla (notas: 10.0, 9.5, 9.0)
- Medias esperadas: Ana: 8.17, Bruno: 6.17, Carla: 9.50
- Caso de borda: aluno com apenas 1 nota — a media deve ser igual a essa nota

### Resposta Comentada
```python
# Importamos o modulo json
import json

def calculate_averages(json_text):
    """
    Recebe uma string JSON com alunos e notas, calcula a media de cada um.
    "calculate_averages" = calcular medias
    "json_text" = texto JSON
    """
    # Convertemos a string JSON para lista Python
    # "students" = estudantes/alunos
    students = json.loads(json_text)

    # Lista para armazenar os resultados
    # "results" = resultados
    results = []

    for student in students:
        # "student" = estudante/aluno
        # "name" = nome, "grades" = notas
        name = student["name"]
        grades = student["grades"]

        # Calculamos a media: soma das notas dividida pela quantidade
        # sum() soma todos os valores, len() conta quantos sao
        # "average" = media
        average = sum(grades) / len(grades)

        # Criamos um novo dicionario com o nome e a media
        # round() arredonda para 2 casas decimais
        results.append({"name": name, "average": round(average, 2)})

    # Retornamos a lista de resultados
    return results


def save_results(results, file_path):
    """
    Salva os resultados em um arquivo JSON.
    "save_results" = salvar resultados
    "results" = resultados, "file_path" = caminho do arquivo
    """
    with open(file_path, "w", encoding="utf-8") as file:
        # "file" = arquivo
        # Salvamos com formatacao legivel
        json.dump(results, file, indent=4, ensure_ascii=False)


# --- Programa principal ---

# String JSON com dados dos alunos
# "json_text" = texto JSON
json_text = '''
[
    {"name": "Ana", "grades": [8.0, 7.5, 9.0]},
    {"name": "Bruno", "grades": [6.0, 5.5, 7.0]},
    {"name": "Carla", "grades": [10.0, 9.5, 9.0]}
]
'''

# Calculamos as medias
# "results" = resultados
results = calculate_averages(json_text)

# Exibimos no terminal
print("Medias dos alunos:")
for result in results:
    # "result" = resultado
    print(f"  {result['name']}: {result['average']}")

# Salvamos no arquivo
save_results(results, "medias_alunos.json")
print("\nResultados salvos em 'medias_alunos.json'.")
```

---

## Exercício 12 — Sistema de Configuracoes com JSON — Nível: Avancado
**Conceitos:** json.load, json.dump, funções, dicionário, tratamento de erros

### Enunciado
Crie um programa que gerencie configuracoes de um aplicativo usando um arquivo JSON. O programa deve ter funções para: (1) criar configuracoes padrão, (2) salvar configuracoes, (3) carregar configuracoes, e (4) atualizar uma configuração específica. Demonstre o uso de todas as funções.

### Dicas
- Crie um dicionário com configuracoes padrão (idioma, tema, tamanho de fonte, etc.)
- A função de carregar deve tratar o caso do arquivo não existir (criando as configuracoes padrão)
- A função de atualizar deve modificar apenas o campo desejado e salvar

### Proposta de Teste
- Configuracoes padrão: idioma "pt-BR", tema "claro", fonte tamanho 14
- Atualizar tema para "escuro" — o arquivo deve refletir a mudanca
- Caso de borda: carregar configuracoes quando o arquivo não existe — deve criar com valores padrão

### Resposta Comentada
```python
# Importamos o modulo json
import json

# Caminho do arquivo de configuracoes
# "config_file" = arquivo de configuracao
CONFIG_FILE = "app_config.json"

def get_default_settings():
    """
    Retorna as configuracoes padrao do aplicativo.
    "get_default_settings" = obter configuracoes padrao
    """
    # "settings" = configuracoes
    # Cada chave e uma configuracao com seu valor padrao
    settings = {
        "language": "pt-BR",
        "theme": "claro",
        "font_size": 14,
        "notifications": True,
        "auto_save": True
    }
    # Retornamos o dicionario com as configuracoes padrao
    return settings


def save_settings(settings):
    """
    Salva as configuracoes em um arquivo JSON.
    "save_settings" = salvar configuracoes
    "settings" = configuracoes
    """
    # Abrimos o arquivo para escrita
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        # "file" = arquivo
        # Salvamos com formatacao legivel
        json.dump(settings, file, indent=4, ensure_ascii=False)


def load_settings():
    """
    Carrega as configuracoes do arquivo JSON.
    Se o arquivo nao existir, cria com valores padrao.
    "load_settings" = carregar configuracoes
    """
    try:
        # Tentamos ler o arquivo de configuracoes
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            # "settings" = configuracoes
            settings = json.load(file)
            return settings
    except FileNotFoundError:
        # Arquivo nao existe — criamos com valores padrao
        print("Arquivo de configuracoes nao encontrado. Criando com valores padrao.")
        # "default_settings" = configuracoes padrao
        default_settings = get_default_settings()
        # Salvamos as configuracoes padrao
        save_settings(default_settings)
        return default_settings


def update_setting(key, value):
    """
    Atualiza uma configuracao especifica e salva no arquivo.
    "update_setting" = atualizar configuracao
    "key" = chave (nome da configuracao), "value" = valor (novo valor)
    """
    # Carregamos as configuracoes atuais
    # "settings" = configuracoes
    settings = load_settings()
    # Atualizamos o valor da chave especificada
    settings[key] = value
    # Salvamos as configuracoes atualizadas
    save_settings(settings)
    # Informamos a mudanca
    print(f"Configuracao '{key}' atualizada para '{value}'.")


# --- Programa principal ---

# Carregamos as configuracoes (cria o arquivo se nao existir)
# "settings" = configuracoes
print("--- Carregando configuracoes ---")
settings = load_settings()
print(f"Configuracoes atuais:")
print(json.dumps(settings, indent=4, ensure_ascii=False))

print()

# Atualizamos o tema para "escuro"
print("--- Atualizando tema ---")
update_setting("theme", "escuro")

print()

# Carregamos novamente para confirmar a mudanca
print("--- Configuracoes apos atualizacao ---")
settings = load_settings()
print(json.dumps(settings, indent=4, ensure_ascii=False))
```

---

[<- Voltar ao Módulo 21](21-manipulacao-json.md) | [Glossário](00-glossario.md)
