# Exercícios — Módulo 20: Leitura e Escrita de Arquivos

[<- Voltar ao Módulo 20](20-leitura-escrita-arquivos.md) | [Glossário](00-glossario.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. So depois consulte a Resposta Comentada
>
> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-20/` e execute com `python3 nome_do_arquivo.py`. Verifique os arquivos criados na pasta apos a execução.

---

## Exercício 1 — Escrever e Ler um Arquivo de Texto — Nível: Básico
**Conceitos:** open, write, read, with

### Enunciado
Crie um programa que escreva 3 frases em um arquivo chamado `frases.txt` e depois leia e exiba o conteúdo do arquivo no terminal.

### Dicas
- Use o modo `"w"` para escrever e `"r"` para ler
- Lembre-se de incluir `\n` no final de cada frase para pular de linha
- Use `encoding="utf-8"` para garantir que acentos funcionem
- Abra o arquivo duas vezes: uma para escrever e outra para ler

### Proposta de Teste
- O arquivo `frases.txt` deve ser criado na pasta
- A saida no terminal deve exibir as 3 frases, cada uma em uma linha separada
- Abra o arquivo `frases.txt` no VSCode para confirmar que o conteúdo esta correto

### Resposta Comentada
```python
# Abrimos o arquivo para escrita
# "w" = write = escrita, cria o arquivo se nao existir
with open("frases.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo — variavel que representa o arquivo aberto
    # Escrevemos 3 frases, cada uma com \n para pular de linha
    file.write("Python e uma linguagem incrivel para iniciantes.\n")
    file.write("Aprender a programar abre muitas portas.\n")
    file.write("Pratique todos os dias para melhorar.\n")

# Abrimos o arquivo para leitura
# "r" = read = leitura
with open("frases.txt", "r", encoding="utf-8") as file:
    # read() le todo o conteudo do arquivo
    # "content" = conteudo
    content = file.read()
    # Exibimos o conteudo no terminal
    print(content)
```

---

## Exercício 2 — Contar Linhas de um Arquivo — Nível: Básico
**Conceitos:** open, readlines, len

### Enunciado
Crie um arquivo com 5 nomes de cidades (um por linha). Depois, leia o arquivo e exiba quantas linhas ele tem.

### Dicas
- Use `readlines()` para obter uma lista de linhas
- Use `len()` para contar quantos elementos a lista tem
- Lembre-se de incluir `\n` ao escrever cada cidade

### Proposta de Teste
- Escreva 5 cidades — Saida: `O arquivo tem 5 linhas.`
- Adicione mais 2 cidades e execute novamente — Saida: `O arquivo tem 7 linhas.`

### Resposta Comentada
```python
# Criamos o arquivo com 5 cidades
# "w" = write = escrita
with open("cidades.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo
    # Escrevemos 5 cidades, uma por linha
    file.write("Sao Paulo\n")
    file.write("Rio de Janeiro\n")
    file.write("Belo Horizonte\n")
    file.write("Curitiba\n")
    file.write("Salvador\n")

# Lemos o arquivo e contamos as linhas
# "r" = read = leitura
with open("cidades.txt", "r", encoding="utf-8") as file:
    # readlines() retorna uma lista onde cada elemento e uma linha
    # "lines" = linhas
    lines = file.readlines()
    # len() = length = comprimento/quantidade
    print(f"O arquivo tem {len(lines)} linhas.")
```

---

## Exercício 3 — Ler Linha a Linha e Numerar — Nível: Básico
**Conceitos:** open, for, enumerate, strip

### Enunciado
Crie um arquivo com 4 tarefas do dia (uma por linha). Depois, leia o arquivo e exiba cada tarefa numerada, sem o caractere `\n` no final.

### Dicas
- Use `for line in file` para iterar linha a linha
- Use `strip()` para remover o `\n` do final de cada linha
- Use `enumerate(start=1)` para numerar a partir de 1

### Proposta de Teste
- Tarefas: "Estudar Python", "Fazer exercícios", "Ler documentação", "Revisar código"
- Saida esperada:
  ```
  1. Estudar Python
  2. Fazer exercícios
  3. Ler documentação
  4. Revisar código
  ```
- Se adicionar uma 5a tarefa, a saida deve ter 5 linhas numeradas

### Resposta Comentada
```python
# Criamos o arquivo com 4 tarefas
# "w" = write = escrita
with open("tarefas.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo
    # Escrevemos cada tarefa em uma linha
    file.write("Estudar Python\n")
    file.write("Fazer exercicios\n")
    file.write("Ler documentacao\n")
    file.write("Revisar codigo\n")

# Lemos o arquivo e exibimos as tarefas numeradas
# "r" = read = leitura
with open("tarefas.txt", "r", encoding="utf-8") as file:
    # enumerate() retorna pares (indice, valor)
    # start=1 faz a contagem comecar em 1
    for number, line in enumerate(file, start=1):
        # "number" = numero, "line" = linha
        # strip() remove espacos e \n das pontas
        # "task" = tarefa
        task = line.strip()
        # Exibimos o numero e a tarefa
        print(f"{number}. {task}")
```

---

## Exercício 4 — Adicionar Itens a um Arquivo Existente — Nível: Básico
**Conceitos:** open, modo "a", append

### Enunciado
Crie um arquivo `diario.txt` com 2 entradas. Depois, adicione mais 2 entradas sem apagar as anteriores. Exiba o conteúdo final.

### Dicas
- Use o modo `"w"` para criar o arquivo inicial
- Use o modo `"a"` (append) para adicionar sem apagar
- Leia o arquivo no final para verificar que todas as 4 entradas estão la

### Proposta de Teste
- Apos criar com 2 entradas e adicionar 2 — o arquivo deve ter 4 linhas
- O conteúdo das 2 primeiras entradas deve estar intacto
- Caso de borda: execute o programa duas vezes — o arquivo tera 6 linhas (2 originais + 2 adicionadas + 2 adicionadas novamente)

### Resposta Comentada
```python
# Criamos o arquivo com 2 entradas iniciais
# "w" = write = escrita — cria o arquivo (ou apaga se ja existir)
with open("diario.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo
    file.write("Dia 1: Aprendi sobre variaveis\n")
    file.write("Dia 2: Aprendi sobre listas\n")

# Adicionamos mais 2 entradas SEM apagar as anteriores
# "a" = append = adicionar no final
with open("diario.txt", "a", encoding="utf-8") as file:
    file.write("Dia 3: Aprendi sobre arquivos\n")
    file.write("Dia 4: Aprendi sobre CSV\n")

# Lemos e exibimos o conteudo completo
# "r" = read = leitura
with open("diario.txt", "r", encoding="utf-8") as file:
    # read() le todo o conteudo
    # "content" = conteudo
    content = file.read()
    print(content)
```

---

## Exercício 5 — Buscar Palavra em Arquivo — Nível: Intermediario
**Conceitos:** open, for, in, lower, strip

### Enunciado
Crie um arquivo com 6 frases. Depois, peca ao usuario uma palavra e exiba todas as linhas do arquivo que contem essa palavra (ignorando maiusculas/minusculas).

### Dicas
- Use `for line in file` para percorrer cada linha
- Use `lower()` tanto na linha quanto na palavra buscada para ignorar maiusculas
- Use o operador `in` para verificar se a palavra esta na linha

### Proposta de Teste
- Arquivo com frases sobre programação. Buscar "python" — deve exibir apenas as linhas que contem "python" ou "Python"
- Buscar "xyz" — deve exibir "Nenhuma linha encontrada."
- Buscar "PYTHON" (maiusculo) — deve encontrar as mesmas linhas que "python"

### Resposta Comentada
```python
# Criamos um arquivo com 6 frases
with open("frases.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo
    file.write("Python e uma linguagem muito popular.\n")
    file.write("Java tambem e muito usada no mercado.\n")
    file.write("Aprender Python abre muitas portas.\n")
    file.write("JavaScript domina o desenvolvimento web.\n")
    file.write("Eu adoro programar em Python todos os dias.\n")
    file.write("C e uma linguagem de baixo nivel.\n")

# Pedimos a palavra ao usuario
# "search_word" = palavra de busca
search_word = input("Digite a palavra para buscar: ")

# "found" = encontrado — controla se achamos alguma linha
found = False

# Lemos o arquivo e buscamos a palavra
with open("frases.txt", "r", encoding="utf-8") as file:
    for line in file:
        # "clean_line" = linha limpa (sem \n)
        clean_line = line.strip()
        # lower() converte para minusculas para comparacao
        # Verificamos se a palavra esta na linha (ignorando maiusculas)
        if search_word.lower() in clean_line.lower():
            # Exibimos a linha que contem a palavra
            print(f"  -> {clean_line}")
            # Marcamos que encontramos pelo menos uma linha
            found = True

# Se nao encontramos nenhuma linha
if not found:
    print("Nenhuma linha encontrada.")
```

---

## Exercício 6 — Ler CSV e Calcular Media — Nível: Intermediario
**Conceitos:** csv.reader, int, float, acumulador

### Enunciado
Crie um arquivo CSV com nomes e notas de 4 alunos. Depois, leia o arquivo e calcule a media das notas.

### Dicas
- Use `csv.reader` para ler o arquivo
- Lembre-se de pular o cabecalho com `next(reader)`
- Converta as notas de string para float com `float()`
- Some todas as notas e divida pela quantidade de alunos

### Proposta de Teste
- Notas: 8.5, 7.0, 9.0, 6.5 — Media esperada: `7.75`
- Notas: 10.0, 10.0, 10.0, 10.0 — Media esperada: `10.0`

### Resposta Comentada
```python
# Importamos o modulo csv
import csv

# Criamos o arquivo CSV com notas
with open("notas.csv", "w", encoding="utf-8", newline="") as file:
    # "file" = arquivo
    # "writer" = escritor de CSV
    writer = csv.writer(file)
    # Escrevemos o cabecalho (header)
    # "student" = estudante, "grade" = nota
    writer.writerow(["student", "grade"])
    # Escrevemos os dados de cada aluno
    writer.writerow(["Ana", "8.5"])
    writer.writerow(["Bruno", "7.0"])
    writer.writerow(["Carla", "9.0"])
    writer.writerow(["Daniel", "6.5"])

# Lemos o CSV e calculamos a media
# "total" = total (acumulador), "count" = contador
total = 0
count = 0

with open("notas.csv", "r", encoding="utf-8") as file:
    # csv.reader() cria o leitor
    reader = csv.reader(file)
    # next() pula o cabecalho
    next(reader)

    # Percorremos cada linha de dados
    for row in reader:
        # row[1] e a nota (segunda coluna)
        # "grade" = nota — convertemos de string para float
        grade = float(row[1])
        # Somamos ao total
        total = total + grade
        # Incrementamos o contador
        count = count + 1

# Calculamos a media
# "average" = media
average = total / count
# Exibimos o resultado
print(f"Media das notas: {average}")
```

---

## Exercício 7 — Escrever CSV a Partir de Dicionários — Nível: Intermediario
**Conceitos:** csv.DictWriter, writeheader, writerows

### Enunciado
Crie uma lista de 3 produtos (cada um com nome, preco e quantidade) usando dicionários. Salve esses produtos em um arquivo CSV usando `csv.DictWriter`. Depois, leia e exiba o conteúdo do arquivo.

### Dicas
- Defina os `fieldnames` com os nomes das colunas
- Use `writeheader()` para escrever o cabecalho
- Use `writerows()` para escrever todos os dicionários de uma vez
- Leia o arquivo no final para verificar

### Proposta de Teste
- 3 produtos salvos — o arquivo deve ter 4 linhas (1 cabecalho + 3 dados)
- O cabecalho deve ser `name,price,quantity`
- Caso de borda: produto com preco `0.0` deve ser salvo corretamente

### Resposta Comentada
```python
# Importamos o modulo csv
import csv

# Criamos uma lista de produtos como dicionarios
# "products" = produtos
products = [
    {"name": "Arroz", "price": "5.99", "quantity": "100"},
    {"name": "Feijao", "price": "7.50", "quantity": "80"},
    {"name": "Macarrao", "price": "3.25", "quantity": "150"}
]

# Definimos os nomes das colunas
# "fieldnames" = nomes dos campos
fieldnames = ["name", "price", "quantity"]

# Escrevemos o arquivo CSV
# newline="" evita linhas em branco extras
with open("produtos.csv", "w", encoding="utf-8", newline="") as file:
    # "file" = arquivo
    # DictWriter = escritor de dicionarios
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    # writeheader() escreve a linha de cabecalho
    writer.writeheader()
    # writerows() escreve todos os dicionarios como linhas
    writer.writerows(products)

# Lemos e exibimos o conteudo do arquivo
with open("produtos.csv", "r", encoding="utf-8") as file:
    # read() le todo o conteudo
    print(file.read())
```

---

## Exercício 8 — Ler CSV com DictReader e Filtrar — Nível: Intermediario
**Conceitos:** csv.DictReader, float, if, filtro

### Enunciado
Usando o arquivo `produtos.csv` do exercício anterior (ou crie um novo), leia os produtos com `csv.DictReader` e exiba apenas os produtos com preco acima de 5.00.

### Dicas
- Use `csv.DictReader` para acessar valores pelo nome da coluna
- Converta o preco de string para float com `float()`
- Use `if` para filtrar os produtos

### Proposta de Teste
- Produtos: Arroz (5.99), Feijao (7.50), Macarrao (3.25) — Devem aparecer: Arroz e Feijao
- Caso de borda: se todos os precos forem abaixo de 5.00, exibir "Nenhum produto encontrado."

### Resposta Comentada
```python
# Importamos o modulo csv
import csv

# Primeiro, criamos o arquivo CSV para garantir que existe
# "products" = produtos
products = [
    {"name": "Arroz", "price": "5.99", "quantity": "100"},
    {"name": "Feijao", "price": "7.50", "quantity": "80"},
    {"name": "Macarrao", "price": "3.25", "quantity": "150"}
]

# "fieldnames" = nomes dos campos
fieldnames = ["name", "price", "quantity"]

# Escrevemos o CSV
with open("produtos.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

# Agora lemos e filtramos
# "found" = encontrado — controla se achamos algum produto
found = False

with open("produtos.csv", "r", encoding="utf-8") as file:
    # DictReader le cada linha como dicionario
    reader = csv.DictReader(file)

    print("Produtos com preco acima de R$ 5.00:")
    for row in reader:
        # "row" = linha — e um dicionario
        # Convertemos o preco de string para float
        # "price" = preco
        price = float(row["price"])
        # Verificamos se o preco e maior que 5.00
        if price > 5.00:
            # Exibimos o produto
            print(f"  {row['name']} — R$ {row['price']}")
            # Marcamos que encontramos pelo menos um
            found = True

# Se nenhum produto foi encontrado
if not found:
    print("Nenhum produto encontrado.")
```

---

## Exercício 9 — Tratamento de Arquivo Inexistente — Nível: Intermediario
**Conceitos:** try, except, FileNotFoundError

### Enunciado
Crie um programa que peca ao usuario o nome de um arquivo e tente ler seu conteúdo. Se o arquivo não existir, exiba uma mensagem amigavel em vez de o programa parar com erro.

### Dicas
- Use `input()` para pedir o nome do arquivo
- Use `try/except FileNotFoundError` para tratar o erro
- Exiba uma mensagem clara informando que o arquivo não foi encontrado

### Proposta de Teste
- Digite o nome de um arquivo que existe (crie um antes) — deve exibir o conteúdo
- Digite `arquivo_que_nao_existe.txt` — Saida: `Erro: o arquivo 'arquivo_que_nao_existe.txt' nao foi encontrado.`
- Digite um nome vazio e pressione Enter — o programa deve tratar o erro

### Resposta Comentada
```python
# Pedimos o nome do arquivo ao usuario
# "file_name" = nome do arquivo
file_name = input("Digite o nome do arquivo: ")

# Tentamos abrir e ler o arquivo
try:
    # "r" = read = leitura
    with open(file_name, "r", encoding="utf-8") as file:
        # "file" = arquivo
        # read() le todo o conteudo
        # "content" = conteudo
        content = file.read()
        # Verificamos se o arquivo esta vazio
        if content:
            # Se tem conteudo, exibimos
            print("Conteudo do arquivo:")
            print(content)
        else:
            # Se esta vazio
            print("O arquivo existe, mas esta vazio.")
except FileNotFoundError:
    # O arquivo nao foi encontrado
    print(f"Erro: o arquivo '{file_name}' nao foi encontrado.")
    print("Verifique se o nome esta correto e se voce esta na pasta certa.")
```

---

## Exercício 10 — Registro de Log em Arquivo — Nível: Intermediario
**Conceitos:** open, modo "a", função, datetime

### Enunciado
Crie uma função `add_log(message)` que adiciona uma mensagem com data e hora a um arquivo `log.txt`. Chame a função 3 vezes com mensagens diferentes e exiba o conteúdo final do arquivo.

### Dicas
- Use o modo `"a"` para adicionar sem apagar
- Use `from datetime import datetime` para obter a data e hora atual
- `datetime.now().strftime("%Y-%m-%d %H:%M:%S")` formata a data e hora
- Crie uma função que recebe a mensagem como parametro

### Proposta de Teste
- Chame `add_log("Programa iniciado")`, `add_log("Dados carregados")`, `add_log("Programa encerrado")`
- O arquivo deve ter 3 linhas, cada uma com data/hora e a mensagem
- Execute o programa novamente — o arquivo deve ter 6 linhas (3 anteriores + 3 novas)

### Resposta Comentada
```python
# Importamos datetime para obter data e hora
from datetime import datetime

def add_log(message):
    """
    Adiciona uma mensagem com data/hora ao arquivo de log.
    "add_log" = adicionar registro, "message" = mensagem
    """
    # Obtemos a data e hora atual formatada
    # "timestamp" = marca de tempo
    # strftime() formata a data como texto
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Abrimos o arquivo em modo adicao
    # "a" = append = adicionar no final
    with open("log.txt", "a", encoding="utf-8") as file:
        # "file" = arquivo
        # Escrevemos a data/hora e a mensagem
        file.write(f"[{timestamp}] {message}\n")


# Chamamos a funcao 3 vezes com mensagens diferentes
add_log("Programa iniciado")
add_log("Dados carregados")
add_log("Programa encerrado")

# Exibimos o conteudo do arquivo de log
with open("log.txt", "r", encoding="utf-8") as file:
    # read() le todo o conteudo
    print("Conteudo do log:")
    print(file.read())
```

---

## Exercício 11 — Copiar Conteúdo Entre Arquivos — Nível: Avancado
**Conceitos:** open, read, write, try/except

### Enunciado
Crie um programa que leia o conteúdo de um arquivo de origem e copie para um arquivo de destino. Trate o caso do arquivo de origem não existir.

### Dicas
- Abra o arquivo de origem para leitura e o de destino para escrita
- Use `try/except` para tratar `FileNotFoundError`
- Leia todo o conteúdo com `read()` e escreva com `write()`

### Proposta de Teste
- Crie `origem.txt` com 3 linhas. Copie para `destino.txt` — o conteúdo deve ser identico
- Tente copiar de um arquivo que não existe — Saida: mensagem de erro amigavel
- Caso de borda: copiar um arquivo vazio — `destino.txt` deve ser criado vazio

### Resposta Comentada
```python
def copy_file(source_path, destination_path):
    """
    Copia o conteudo de um arquivo para outro.
    "copy_file" = copiar arquivo
    "source_path" = caminho de origem
    "destination_path" = caminho de destino
    """
    try:
        # Abrimos o arquivo de origem para leitura
        with open(source_path, "r", encoding="utf-8") as source_file:
            # "source_file" = arquivo de origem
            # Lemos todo o conteudo
            # "content" = conteudo
            content = source_file.read()

        # Abrimos o arquivo de destino para escrita
        with open(destination_path, "w", encoding="utf-8") as dest_file:
            # "dest_file" = arquivo de destino
            # Escrevemos o conteudo copiado
            dest_file.write(content)

        # Informamos o sucesso
        print(f"Arquivo copiado de '{source_path}' para '{destination_path}'.")
    except FileNotFoundError:
        # O arquivo de origem nao foi encontrado
        print(f"Erro: o arquivo '{source_path}' nao foi encontrado.")


# Criamos um arquivo de origem para teste
with open("origem.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo
    file.write("Linha 1: Ola, mundo!\n")
    file.write("Linha 2: Testando copia.\n")
    file.write("Linha 3: Fim do arquivo.\n")

# Copiamos o arquivo
# "source" = origem, "destination" = destino
copy_file("origem.txt", "destino.txt")

# Verificamos o conteudo do destino
with open("destino.txt", "r", encoding="utf-8") as file:
    print("\nConteudo do destino:")
    print(file.read())
```

---

## Exercício 12 — Cadastro Simples em CSV — Nível: Avancado
**Conceitos:** csv.DictWriter, csv.DictReader, funções, lista de dicionários

### Enunciado
Crie um programa com duas funções: `save_students(students)` que salva uma lista de alunos em um CSV, e `load_students()` que carrega os alunos do CSV. Cada aluno tem nome, idade e curso. Salve 3 alunos, carregue do arquivo e exiba.

### Dicas
- Use `csv.DictWriter` para salvar e `csv.DictReader` para carregar
- Defina os `fieldnames` como `["name", "age", "course"]`
- A função `load_students()` deve retornar uma lista de dicionários
- Trate o caso do arquivo não existir em `load_students()`

### Proposta de Teste
- Salve 3 alunos e carregue — os dados devem ser identicos
- Chame `load_students()` antes de salvar (arquivo não existe) — deve retornar lista vazia
- Caso de borda: aluno com nome contendo virgula (ex: "Silva, Ana") — o CSV deve tratar corretamente

### Resposta Comentada
```python
# Importamos o modulo csv
import csv

def save_students(students):
    """
    Salva a lista de alunos em um arquivo CSV.
    "save_students" = salvar estudantes
    "students" = estudantes
    """
    # Definimos os nomes das colunas
    # "fieldnames" = nomes dos campos
    fieldnames = ["name", "age", "course"]

    # Abrimos o arquivo para escrita
    with open("alunos.csv", "w", encoding="utf-8", newline="") as file:
        # "file" = arquivo
        # DictWriter = escritor de dicionarios
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Escrevemos o cabecalho
        writer.writeheader()
        # Escrevemos todos os alunos
        writer.writerows(students)

    # Informamos quantos alunos foram salvos
    print(f"{len(students)} aluno(s) salvo(s).")


def load_students():
    """
    Carrega alunos do arquivo CSV.
    "load_students" = carregar estudantes
    Retorna uma lista de dicionarios.
    """
    # "students" = estudantes — lista que vai receber os dados
    students = []

    try:
        # Tentamos abrir o arquivo
        with open("alunos.csv", "r", encoding="utf-8") as file:
            # DictReader le cada linha como dicionario
            reader = csv.DictReader(file)
            # Adicionamos cada aluno a lista
            for row in reader:
                # dict(row) cria uma copia do dicionario
                students.append(dict(row))
    except FileNotFoundError:
        # Se o arquivo nao existe, retornamos lista vazia
        print("Arquivo nao encontrado. Retornando lista vazia.")

    # Retornamos a lista de alunos
    return students


# --- Programa principal ---

# Criamos uma lista de alunos
# "students" = estudantes
students = [
    {"name": "Ana", "age": "20", "course": "Informatica"},
    {"name": "Bruno", "age": "25", "course": "Administracao"},
    {"name": "Carla", "age": "22", "course": "Engenharia"}
]

# Salvamos no arquivo
save_students(students)

# Carregamos do arquivo
# "loaded" = carregados
loaded = load_students()

# Exibimos os alunos carregados
print("\nAlunos carregados do arquivo:")
for student in loaded:
    # "student" = estudante
    print(f"  {student['name']}, {student['age']} anos, {student['course']}")
```

---

## Exercício 13 — Contar Palavras em um Arquivo — Nível: Avancado
**Conceitos:** open, read, split, len, dicionário

### Enunciado
Crie um arquivo com um paragrafo de texto. Depois, leia o arquivo e conte quantas vezes cada palavra aparece. Exiba as palavras e suas contagens.

### Dicas
- Use `read()` para ler todo o conteúdo
- Use `lower()` para ignorar maiusculas/minusculas
- Use `split()` para separar o texto em palavras
- Use um dicionário para contar as ocorrências de cada palavra

### Proposta de Teste
- Texto: "python e legal python e fácil" — "python" deve aparecer 2 vezes, "e" deve aparecer 2 vezes
- Caso de borda: arquivo vazio — deve exibir "O arquivo esta vazio."

### Resposta Comentada
```python
# Criamos um arquivo com um paragrafo
with open("texto.txt", "w", encoding="utf-8") as file:
    # "file" = arquivo
    file.write("Python e uma linguagem incrivel\n")
    file.write("Python e facil de aprender\n")
    file.write("Aprender Python e muito divertido\n")

# Lemos o arquivo
with open("texto.txt", "r", encoding="utf-8") as file:
    # read() le todo o conteudo
    # "content" = conteudo
    content = file.read()

# Verificamos se o arquivo esta vazio
if not content.strip():
    # Se o conteudo esta vazio (ou so tem espacos)
    print("O arquivo esta vazio.")
else:
    # Convertemos para minusculas e separamos em palavras
    # "words" = palavras
    words = content.lower().split()

    # Criamos um dicionario para contar as palavras
    # "word_count" = contagem de palavras
    word_count = {}

    # Percorremos cada palavra
    for word in words:
        # "word" = palavra
        # Se a palavra ja esta no dicionario, incrementamos
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            # Se nao esta, adicionamos com contagem 1
            word_count[word] = 1

    # Exibimos as contagens
    print("Contagem de palavras:")
    for word, count in word_count.items():
        # "word" = palavra, "count" = contagem
        print(f"  '{word}': {count} vez(es)")
```

---

[<- Voltar ao Módulo 20](20-leitura-escrita-arquivos.md) | [Glossário](00-glossario.md)
