# 20 — Leitura e Escrita de Arquivos: .txt e .csv

[<- Anterior: Estruturas de Dados](19-estruturas-dados.md) | [Glossário](00-glossário.md) | [Próximo: Manipulação JSON ->](21-manipulação-json.md)

---

## Introdução

Ate agora, todos os dados dos seus programas existiam apenas enquanto o programa estava rodando. Quando você fechava o programa, tudo desaparecia — como escrever na areia da praia e ver a onda apagar tudo.

Mas e se você quiser **guardar** informações para usar depois? E se quiser salvar uma lista de compras, um cadastro de alunos ou um relatório de vendas?

E ai que entram os **arquivos**. Trabalhar com arquivos e como usar um caderno: você pode **escrever** informações nele, **fechar** o caderno, e quando precisar, **abrir** novamente e **ler** o que escreveu. As informações ficam guardadas mesmo depois que você fecha o caderno.

Neste módulo, você vai aprender a:

- **Abrir** arquivos de texto (.txt) e CSV (.csv)
- **Ler** o conteúdo de arquivos
- **Escrever** dados em arquivos
- **Adicionar** informações a arquivos existentes
- Trabalhar com **CSV** (formato de tabelas simples)
- **Tratar erros** comuns ao trabalhar com arquivos

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-20/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-20`
4. Execute: `python3 nome_do_arquivo.py`

> **Importante:** Alguns exemplos criam arquivos no mesmo diretório onde você executa o programa. Verifique a pasta apos executar para ver os arquivos criados.

---

## O Que e um Arquivo de Texto

Um arquivo de texto e um arquivo que contem apenas caracteres legiveis — letras, números, espacos e símbolos. Você pode abrir um arquivo `.txt` em qualquer editor de texto (como o VSCode ou o Bloco de Notas).

Pense em um arquivo de texto como uma **folha de papel**: cada linha do arquivo e como uma linha escrita no papel.

---

## Abrindo Arquivos com open() e o Gerenciador de Contexto with

Para trabalhar com arquivos em Python, usamos a função `open()`. Ela abre o arquivo e nos da acesso ao conteúdo.

A forma **recomendada** de abrir arquivos e usando o **gerenciador de contexto** `with`. Pense no `with` como um assistente responsável: ele abre o arquivo para você, deixa você trabalhar, e quando você termina, ele **fecha o arquivo automaticamente** — mesmo que aconteca um erro no meio do caminho.

Sem o `with`, você precisaria lembrar de fechar o arquivo manualmente. Esquecer de fechar um arquivo e como deixar a torneira aberta — pode causar problemas.

```python
# Forma RECOMENDADA — com gerenciador de contexto (with)
# "with" garante que o arquivo sera fechado automaticamente
# open() = abrir, "r" = read = leitura
with open("meu_arquivo.txt", "r") as file:
    # "file" = arquivo — variavel que representa o arquivo aberto
    # "content" = conteudo
    content = file.read()
    # read() = ler — le todo o conteudo do arquivo
    print(content)
# Aqui fora do with, o arquivo ja foi fechado automaticamente
```

> **Nota:** O `as file` da um nome (apelido) ao arquivo aberto. Você pode usar qualquer nome, mas `file` (arquivo) e o mais comum.

---

## Modos de Abertura de Arquivos

Quando você abre um arquivo, precisa dizer ao Python **o que pretende fazer** com ele. Isso e feito pelo segundo parametro da função `open()`, chamado de **modo de abertura**.

Pense assim: quando você pega um caderno, você decide antes se vai **ler** o que esta escrito, **escrever** algo novo (apagando o que tinha), ou **acrescentar** algo no final.

| Modo | Significado | O que faz |
|------|-------------|-----------|
| `"r"` | read (leitura) | Abre para leitura. O arquivo precisa existir. |
| `"w"` | write (escrita) | Abre para escrita. Cria o arquivo se não existir. **Apaga todo o conteúdo anterior!** |
| `"a"` | append (adicao) | Abre para adicao. Cria o arquivo se não existir. Escreve no **final** sem apagar nada. |

> **Cuidado com o modo "w"!** Ele apaga tudo que existia no arquivo. E como arrancar todas as páginas de um caderno antes de começar a escrever. Se você quer manter o que ja tem e adicionar mais, use `"a"`.

```python
# Modo "r" — leitura (read)
# O arquivo PRECISA existir, senao da erro
with open("dados.txt", "r") as file:
    # "content" = conteudo
    content = file.read()

# Modo "w" — escrita (write)
# CUIDADO: apaga tudo que existia no arquivo!
# Se o arquivo nao existir, cria um novo
with open("dados.txt", "w") as file:
    # write() = escrever
    file.write("Novo conteudo")

# Modo "a" — adicao (append)
# Escreve no FINAL do arquivo, sem apagar nada
# Se o arquivo nao existir, cria um novo
with open("dados.txt", "a") as file:
    # write() = escrever — adiciona no final
    file.write("Mais uma linha")
```

---

## Encoding UTF-8 — Acentos e Caracteres Especiais

Quando trabalhamos com textos em portugues, usamos acentos (a, e, o), cedilha (c) e outros caracteres especiais. Para que o Python leia e escreva esses caracteres corretamente, precisamos informar o **encoding** (codificacao) do arquivo.

O encoding mais usado e o **UTF-8**, que suporta praticamente todos os caracteres de todos os idiomas do mundo. Pense no encoding como um **dicionário de traducao** entre os caracteres que você ve na tela e os números que o computador armazena.

```python
# Abrindo arquivo com encoding UTF-8
# "encoding" = codificacao — garante que acentos funcionem
with open("texto_portugues.txt", "r", encoding="utf-8") as file:
    # "content" = conteudo
    content = file.read()
    print(content)

# Escrevendo arquivo com encoding UTF-8
with open("texto_portugues.txt", "w", encoding="utf-8") as file:
    # Acentos e caracteres especiais serao salvos corretamente
    file.write("Programacao em Python e fantastico!\n")
    file.write("Voce esta aprendendo muito bem!\n")
```

> **Dica:** Sempre use `encoding="utf-8"` ao abrir arquivos que contenham texto em portugues. Isso evita problemas com acentos e caracteres especiais.

---

## Leitura de Arquivos de Texto

Existem várias formas de ler o conteúdo de um arquivo. Cada uma e útil em situacoes diferentes.

Para os exemplos a seguir, vamos criar primeiro um arquivo de teste:

```python
# Criando um arquivo de exemplo para os proximos testes
# "w" = write = escrita, encoding UTF-8 para acentos
with open("exemplo.txt", "w", encoding="utf-8") as file:
    # Escrevemos 4 linhas no arquivo
    # "\n" = quebra de linha (pula para a proxima linha)
    file.write("Primeira linha do arquivo\n")
    file.write("Segunda linha do arquivo\n")
    file.write("Terceira linha do arquivo\n")
    file.write("Quarta e ultima linha")
```

> Execute este código primeiro para criar o arquivo `exemplo.txt` na sua pasta.

### read() — Ler Todo o Conteúdo de Uma Vez

O método `read()` le **todo** o conteúdo do arquivo e retorna como uma única string. E como ler uma carta inteira de uma vez.

```python
# Lendo todo o conteudo do arquivo
# "r" = read = leitura
with open("exemplo.txt", "r", encoding="utf-8") as file:
    # read() le TUDO de uma vez
    # "content" = conteudo
    content = file.read()
    print(content)
    print("---")
    # type() mostra o tipo — sera <class 'str'>
    print(type(content))
```

Saida esperada:
```
Primeira linha do arquivo
Segunda linha do arquivo
Terceira linha do arquivo
Quarta e ultima linha
---
<class 'str'>
```

### readline() — Ler Uma Linha por Vez

O método `readline()` le **uma única linha** do arquivo a cada chamada. E como ler um livro linha por linha, passando o dedo por cada frase.

```python
# Lendo uma linha por vez
with open("exemplo.txt", "r", encoding="utf-8") as file:
    # readline() le a proxima linha do arquivo
    # "first_line" = primeira linha
    first_line = file.readline()
    print(f"Linha 1: {first_line}", end="")
    # "second_line" = segunda linha
    second_line = file.readline()
    print(f"Linha 2: {second_line}", end="")
```

Saida esperada:
```
Linha 1: Primeira linha do arquivo
Linha 2: Segunda linha do arquivo
```

> **Nota:** Cada linha lida com `readline()` inclui o caractere `\n` (quebra de linha) no final. Por isso usamos `end=""` no print() para evitar uma linha em branco extra.

### readlines() — Ler Todas as Linhas como Lista

O método `readlines()` le **todas as linhas** e retorna uma **lista** onde cada elemento e uma linha do arquivo. E como arrancar cada linha do papel e colocar em fichas separadas.

```python
# Lendo todas as linhas como uma lista
with open("exemplo.txt", "r", encoding="utf-8") as file:
    # readlines() retorna uma lista de strings
    # "lines" = linhas
    lines = file.readlines()
    print(lines)
    print(f"Total de linhas: {len(lines)}")
```

Saida esperada:
```
['Primeira linha do arquivo\n', 'Segunda linha do arquivo\n', 'Terceira linha do arquivo\n', 'Quarta e ultima linha']
Total de linhas: 4
```

> **Nota:** Observe que cada linha (exceto a ultima) termina com `\n`. Você pode usar `strip()` para remover esse caractere.

### Iteração Linha a Linha — A Forma Mais Comum

A forma mais prática e **eficiente** de ler um arquivo linha por linha e usar o `for` diretamente no arquivo. E como folhear um caderno página por página.

Esta e a forma **recomendada** para arquivos grandes, porque não carrega tudo na memória de uma vez.

```python
# Iterando linha a linha — forma recomendada
with open("exemplo.txt", "r", encoding="utf-8") as file:
    # "line" = linha — cada iteracao le uma linha
    for line in file:
        # strip() remove espacos e quebras de linha (\n) das pontas
        # "clean_line" = linha limpa
        clean_line = line.strip()
        print(f"-> {clean_line}")
```

Saida esperada:
```
-> Primeira linha do arquivo
-> Segunda linha do arquivo
-> Terceira linha do arquivo
-> Quarta e ultima linha
```

### Comparação dos Métodos de Leitura

| Método | O que retorna | Quando usar |
|--------|---------------|-------------|
| `read()` | Uma única string com tudo | Arquivos pequenos que cabem na memória |
| `readline()` | Uma string (uma linha) | Quando precisa processar linha por linha com controle manual |
| `readlines()` | Uma lista de strings | Quando precisa de todas as linhas como lista |
| `for line in file` | Uma string por iteração | Forma recomendada para arquivos de qualquer tamanho |

---

## Escrita de Arquivos de Texto

### write() — Escrever uma String

O método `write()` escreve uma string no arquivo. Ele **não adiciona quebra de linha automaticamente** — você precisa incluir `\n` quando quiser pular de linha.

```python
# Escrevendo em um arquivo
# "w" = write = escrita — CUIDADO: apaga o conteudo anterior!
with open("saida.txt", "w", encoding="utf-8") as file:
    # write() escreve a string no arquivo
    file.write("Linha 1: Ola, mundo!\n")
    file.write("Linha 2: Aprendendo arquivos em Python\n")
    file.write("Linha 3: Isso e muito util!")

# Verificando o que foi escrito
with open("saida.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Saida esperada:
```
Linha 1: Ola, mundo!
Linha 2: Aprendendo arquivos em Python
Linha 3: Isso e muito util!
```

### writelines() — Escrever uma Lista de Strings

O método `writelines()` recebe uma **lista de strings** e escreve todas no arquivo. Assim como `write()`, ele **não adiciona quebras de linha** — você precisa incluir `\n` em cada string.

```python
# Escrevendo uma lista de linhas
# "lines" = linhas
lines = [
    "Arroz\n",
    "Feijao\n",
    "Macarrao\n",
    "Leite\n",
    "Pao\n"
]

# writelines() escreve todas as strings da lista
with open("lista_compras.txt", "w", encoding="utf-8") as file:
    # writelines() = escrever linhas
    file.writelines(lines)

# Verificando
with open("lista_compras.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Saida esperada:
```
Arroz
Feijao
Macarrao
Leite
Pao
```

### Modo Adicao ("a") — Acrescentar sem Apagar

O modo `"a"` (append = adicionar) escreve no **final** do arquivo sem apagar o que ja existe. E como escrever mais itens no final de uma lista de compras que ja tem alguns itens.

```python
# Primeiro, criamos um arquivo com conteudo inicial
with open("diario.txt", "w", encoding="utf-8") as file:
    file.write("Segunda: Estudei variaveis\n")
    file.write("Terca: Estudei listas\n")

# Agora, ADICIONAMOS mais linhas sem apagar as anteriores
# "a" = append = adicionar no final
with open("diario.txt", "a", encoding="utf-8") as file:
    file.write("Quarta: Estudei arquivos\n")
    file.write("Quinta: Estudei CSV\n")

# Verificando — todas as 4 linhas estao la
with open("diario.txt", "r", encoding="utf-8") as file:
    print(file.read())
```

Saida esperada:
```
Segunda: Estudei variaveis
Terca: Estudei listas
Quarta: Estudei arquivos
Quinta: Estudei CSV
```

---

## Leitura e Escrita de Arquivos CSV

### O Que e um Arquivo CSV

CSV significa **Comma-Separated Values** (Valores Separados por Virgula). E um formato simples para armazenar dados em forma de **tabela**, onde cada linha e um registro e os valores sao separados por um caractere delimitador (geralmente virgula ou ponto e virgula).

Pense em um arquivo CSV como uma **planilha simples**: cada linha e uma fileira da planilha, e cada valor separado por virgula e uma coluna.

Exemplo de conteúdo de um arquivo CSV:

```
nome,idade,cidade
Ana,25,Sao Paulo
Bruno,30,Rio de Janeiro
Carla,22,Belo Horizonte
```

Isso equivale a esta tabela:

| nome | idade | cidade |
|------|-------|--------|
| Ana | 25 | Sao Paulo |
| Bruno | 30 | Rio de Janeiro |
| Carla | 22 | Belo Horizonte |

Python tem um módulo chamado `csv` na biblioteca padrão que facilita a leitura e escrita de arquivos CSV.

### Criando um Arquivo CSV de Exemplo

Antes de ler, vamos criar um arquivo CSV para usar nos exemplos:

```python
# Criando um arquivo CSV de exemplo
# Escrevemos manualmente para entender o formato
with open("alunos.csv", "w", encoding="utf-8") as file:
    # A primeira linha e o cabecalho (header = cabecalho)
    file.write("name,age,city\n")
    # Cada linha seguinte e um registro (record = registro)
    file.write("Ana,25,Sao Paulo\n")
    file.write("Bruno,30,Rio de Janeiro\n")
    file.write("Carla,22,Belo Horizonte\n")
    file.write("Daniel,28,Curitiba\n")
```

### csv.reader — Lendo CSV como Listas

O `csv.reader` le cada linha do CSV e transforma em uma **lista** de valores. E como pegar cada fileira da planilha e colocar os valores em uma lista.

```python
# Importamos o modulo csv da biblioteca padrao
import csv

# Abrindo o arquivo CSV para leitura
with open("alunos.csv", "r", encoding="utf-8") as file:
    # csv.reader() cria um leitor de CSV
    # "reader" = leitor
    reader = csv.reader(file)

    # Cada "row" (linha/fileira) e uma lista de valores
    for row in reader:
        # "row" = linha/fileira — e uma lista como ['Ana', '25', 'Sao Paulo']
        print(row)
```

Saida esperada:
```
['name', 'age', 'city']
['Ana', '25', 'Sao Paulo']
['Bruno', '30', 'Rio de Janeiro']
['Carla', '22', 'Belo Horizonte']
['Daniel', '28', 'Curitiba']
```

> **Nota:** A primeira linha e o cabecalho. Todos os valores sao **strings**, mesmo os números. Se precisar de números, converta com `int()` ou `float()`.

### Separando o Cabecalho dos Dados

Muitas vezes queremos tratar o cabecalho de forma diferente dos dados:

```python
import csv

with open("alunos.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    # next() pega a proxima linha — usamos para separar o cabecalho
    # "header" = cabecalho
    header = next(reader)
    print(f"Colunas: {header}")
    print("---")

    # As linhas restantes sao os dados
    for row in reader:
        # Acessamos cada valor pelo indice (posicao)
        # row[0] = nome, row[1] = idade, row[2] = cidade
        # "name" = nome, "age" = idade, "city" = cidade
        name = row[0]
        age = row[1]
        city = row[2]
        print(f"{name} tem {age} anos e mora em {city}")
```

Saida esperada:
```
Colunas: ['name', 'age', 'city']
---
Ana tem 25 anos e mora em Sao Paulo
Bruno tem 30 anos e mora em Rio de Janeiro
Carla tem 22 anos e mora em Belo Horizonte
Daniel tem 28 anos e mora em Curitiba
```

### csv.DictReader — Lendo CSV como Dicionários

O `csv.DictReader` e ainda mais prático: ele le cada linha como um **dicionário**, onde as chaves sao os nomes das colunas do cabecalho. E como ter fichas organizadas onde cada campo tem um rotulo.

```python
import csv

with open("alunos.csv", "r", encoding="utf-8") as file:
    # DictReader = leitor de dicionarios
    # Usa a primeira linha como chaves do dicionario
    reader = csv.DictReader(file)

    # Cada "row" agora e um dicionario
    for row in reader:
        # Acessamos pelo nome da coluna — muito mais claro!
        # row["name"] em vez de row[0]
        print(f"{row['name']} tem {row['age']} anos e mora em {row['city']}")
```

Saida esperada:
```
Ana tem 25 anos e mora em Sao Paulo
Bruno tem 30 anos e mora em Rio de Janeiro
Carla tem 22 anos e mora em Belo Horizonte
Daniel tem 28 anos e mora em Curitiba
```

> **Vantagem do DictReader:** Você acessa os valores pelo **nome da coluna** em vez de pelo número da posição. Isso torna o código mais legivel e menos propenso a erros.

### csv.writer — Escrevendo CSV

O `csv.writer` escreve dados em formato CSV. Você passa uma lista de valores e ele cuida de separar com virgulas.

```python
import csv

# Dados para escrever — lista de listas
# "products" = produtos
products = [
    ["name", "price", "quantity"],
    ["Arroz", "5.99", "100"],
    ["Feijao", "7.50", "80"],
    ["Macarrao", "3.25", "150"],
    ["Leite", "4.80", "60"]
]

# Escrevendo o arquivo CSV
# newline="" evita linhas em branco extras no Windows
with open("produtos.csv", "w", encoding="utf-8", newline="") as file:
    # csv.writer() cria um escritor de CSV
    # "writer" = escritor
    writer = csv.writer(file)

    # writerows() escreve todas as linhas de uma vez
    # "rows" = linhas/fileiras
    writer.writerows(products)

# Verificando o resultado
with open("produtos.csv", "r", encoding="utf-8") as file:
    print(file.read())
```

Saida esperada:
```
name,price,quantity
Arroz,5.99,100
Feijao,7.50,80
Macarrao,3.25,150
Leite,4.80,60
```

> **Nota sobre `newline=""`:** No Windows, sem esse parametro, o arquivo CSV pode ter linhas em branco extras entre cada registro. Usar `newline=""` resolve esse problema. No Linux, não causa problemas, mas e uma boa prática incluir sempre.

### Escrevendo Linha por Linha com writerow()

Você também pode escrever uma linha de cada vez com `writerow()` (no singular):

```python
import csv

with open("notas.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    # writerow() escreve UMA linha (row = linha/fileira)
    # Primeiro escrevemos o cabecalho
    writer.writerow(["student", "grade", "status"])

    # Depois escrevemos cada registro
    # "student" = estudante, "grade" = nota, "status" = situacao
    writer.writerow(["Ana", "8.5", "Aprovada"])
    writer.writerow(["Bruno", "6.0", "Aprovado"])
    writer.writerow(["Carla", "4.5", "Reprovada"])

# Verificando
with open("notas.csv", "r", encoding="utf-8") as file:
    print(file.read())
```

Saida esperada:
```
student,grade,status
Ana,8.5,Aprovada
Bruno,6.0,Aprovado
Carla,4.5,Reprovada
```

### csv.DictWriter — Escrevendo CSV a Partir de Dicionários

O `csv.DictWriter` escreve dicionários como linhas CSV. Você define os nomes das colunas e passa dicionários com os dados.

```python
import csv

# Dados como lista de dicionarios
# "students" = estudantes
students = [
    {"name": "Ana", "age": "25", "city": "Sao Paulo"},
    {"name": "Bruno", "age": "30", "city": "Rio de Janeiro"},
    {"name": "Carla", "age": "22", "city": "Belo Horizonte"}
]

# Definimos os nomes das colunas
# "fieldnames" = nomes dos campos
fieldnames = ["name", "age", "city"]

with open("estudantes.csv", "w", encoding="utf-8", newline="") as file:
    # DictWriter = escritor de dicionarios
    # Passamos o arquivo e os nomes das colunas
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # writeheader() escreve a linha de cabecalho
    # "header" = cabecalho
    writer.writeheader()

    # writerows() escreve todos os dicionarios como linhas
    writer.writerows(students)

# Verificando
with open("estudantes.csv", "r", encoding="utf-8") as file:
    print(file.read())
```

Saida esperada:
```
name,age,city
Ana,25,Sao Paulo
Bruno,30,Rio de Janeiro
Carla,22,Belo Horizonte
```

### Comparação: reader/writer vs DictReader/DictWriter

| Ferramenta | Trabalha com | Quando usar |
|------------|-------------|-------------|
| `csv.reader` | Listas | Quando você sabe a posição de cada coluna |
| `csv.DictReader` | Dicionários | Quando quer acessar valores pelo nome da coluna (mais legivel) |
| `csv.writer` | Listas | Quando seus dados ja estão em listas |
| `csv.DictWriter` | Dicionários | Quando seus dados estão em dicionários (mais organizado) |

---

## Tratamento de Erros com Arquivos

Ao trabalhar com arquivos, erros podem acontecer. Os dois mais comuns sao:

- **FileNotFoundError** — o arquivo que você tentou abrir não existe. E como procurar um livro na estante e ele não estar la.
- **PermissionError** — você não tem permissão para acessar o arquivo. E como tentar abrir uma porta trancada sem a chave.

### FileNotFoundError — Arquivo Não Encontrado

```python
# Tentando abrir um arquivo que nao existe
try:
    with open("arquivo_inexistente.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    # O arquivo nao foi encontrado
    print("Erro: o arquivo nao foi encontrado!")
    print("Verifique se o nome esta correto e se voce esta na pasta certa.")
```

Saida esperada:
```
Erro: o arquivo nao foi encontrado!
Verifique se o nome esta correto e se voce esta na pasta certa.
```

### PermissionError — Sem Permissão de Acesso

```python
# Tentando abrir um arquivo sem permissao
# (este exemplo pode nao gerar erro no seu computador,
# mas mostra como tratar caso aconteca)
try:
    with open("/etc/shadow", "r") as file:
        content = file.read()
except PermissionError:
    # Sem permissao para acessar o arquivo
    print("Erro: voce nao tem permissao para acessar este arquivo!")
    print("Verifique as permissoes com 'ls -l' no terminal.")
except FileNotFoundError:
    # O arquivo nao existe
    print("Erro: arquivo nao encontrado!")
```

Saida esperada:
```
Erro: voce nao tem permissao para acessar este arquivo!
Verifique as permissoes com 'ls -l' no terminal.
```

### Tratamento Completo — Combinando Vários Erros

Na prática, e comum tratar vários tipos de erro ao mesmo tempo:

```python
def read_file(file_path):
    """
    Funcao que le um arquivo de forma segura.
    "file_path" = caminho do arquivo
    "read_file" = ler arquivo
    """
    try:
        # Tentamos abrir e ler o arquivo
        with open(file_path, "r", encoding="utf-8") as file:
            # "content" = conteudo
            content = file.read()
            return content
    except FileNotFoundError:
        # Arquivo nao encontrado
        print(f"Erro: o arquivo '{file_path}' nao foi encontrado.")
        return None
    except PermissionError:
        # Sem permissao
        print(f"Erro: sem permissao para ler '{file_path}'.")
        return None
    except Exception as error:
        # Qualquer outro erro inesperado
        # "error" = erro
        print(f"Erro inesperado: {error}")
        return None

# Testando a funcao
# "result" = resultado
result = read_file("arquivo_que_nao_existe.txt")

# Verificamos se a leitura foi bem-sucedida
if result is None:
    print("Nao foi possivel ler o arquivo.")
else:
    print(f"Conteudo: {result}")
```

Saida esperada:
```
Erro: o arquivo 'arquivo_que_nao_existe.txt' nao foi encontrado.
Nao foi possivel ler o arquivo.
```

---

## Exemplo Prático Completo — Agenda de Contatos em Arquivo

Vamos juntar tudo em um exemplo prático: uma agenda de contatos que salva e le dados de um arquivo CSV.

```python
import csv

def save_contacts(contacts, file_path):
    """
    Salva a lista de contatos em um arquivo CSV.
    "save_contacts" = salvar contatos
    "contacts" = contatos, "file_path" = caminho do arquivo
    """
    # Definimos os nomes das colunas
    # "fieldnames" = nomes dos campos
    fieldnames = ["name", "phone", "email"]

    # Abrimos o arquivo para escrita
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        # Criamos o escritor de dicionarios
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Escrevemos o cabecalho
        writer.writeheader()
        # Escrevemos todos os contatos
        writer.writerows(contacts)

    # Informamos quantos contatos foram salvos
    print(f"{len(contacts)} contato(s) salvo(s) em '{file_path}'.")


def load_contacts(file_path):
    """
    Carrega contatos de um arquivo CSV.
    "load_contacts" = carregar contatos
    """
    # "contacts" = contatos — lista que vai receber os dados
    contacts = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # DictReader le cada linha como dicionario
            reader = csv.DictReader(file)
            # Adicionamos cada contato a lista
            for row in reader:
                contacts.append(dict(row))
    except FileNotFoundError:
        # Se o arquivo nao existe, retornamos lista vazia
        print(f"Arquivo '{file_path}' nao encontrado. Iniciando lista vazia.")

    return contacts


# --- Programa principal ---

# Criamos alguns contatos
# "contacts" = contatos
contacts = [
    {"name": "Ana", "phone": "11-99999-0001", "email": "ana@email.com"},
    {"name": "Bruno", "phone": "21-99999-0002", "email": "bruno@email.com"},
    {"name": "Carla", "phone": "31-99999-0003", "email": "carla@email.com"}
]

# Salvamos no arquivo
save_contacts(contacts, "agenda.csv")

# Carregamos do arquivo
# "loaded_contacts" = contatos carregados
loaded_contacts = load_contacts("agenda.csv")

# Exibimos os contatos carregados
print("\nContatos carregados:")
for contact in loaded_contacts:
    # "contact" = contato
    print(f"  {contact['name']} - {contact['phone']} - {contact['email']}")
```

Saida esperada:
```
3 contato(s) salvo(s) em 'agenda.csv'.

Contatos carregados:
  Ana - 11-99999-0001 - ana@email.com
  Bruno - 21-99999-0002 - bruno@email.com
  Carla - 31-99999-0003 - carla@email.com
```

---

## Resumo dos Principais Comandos

| Comando | O que faz | Exemplo |
|---------|-----------|---------|
| `open("arq.txt", "r")` | Abre para leitura | `with open("dados.txt", "r") as f:` |
| `open("arq.txt", "w")` | Abre para escrita (apaga tudo!) | `with open("saida.txt", "w") as f:` |
| `open("arq.txt", "a")` | Abre para adicao (no final) | `with open("log.txt", "a") as f:` |
| `file.read()` | Le todo o conteúdo | `content = file.read()` |
| `file.readline()` | Le uma linha | `line = file.readline()` |
| `file.readlines()` | Le todas as linhas como lista | `lines = file.readlines()` |
| `for line in file` | Itera linha a linha | `for line in file:` |
| `file.write("texto")` | Escreve uma string | `file.write("Ola\n")` |
| `file.writelines(lista)` | Escreve lista de strings | `file.writelines(lines)` |
| `csv.reader(file)` | Le CSV como listas | `reader = csv.reader(file)` |
| `csv.DictReader(file)` | Le CSV como dicionários | `reader = csv.DictReader(file)` |
| `csv.writer(file)` | Escreve CSV a partir de listas | `writer = csv.writer(file)` |
| `csv.DictWriter(file, ...)` | Escreve CSV a partir de dicionários | `writer = csv.DictWriter(file, fieldnames=...)` |

---

## Para Saber Mais

- [W3Schools — Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)
  _Aqui você encontra exemplos interativos de leitura e escrita de arquivos_

- [W3Schools — Python File Open](https://www.w3schools.com/python/python_file_open.asp)
  _Explicacao detalhada dos modos de abertura de arquivos_

- [W3Schools — Python File Write](https://www.w3schools.com/python/python_file_write.asp)
  _Exemplos de escrita e adicao em arquivos_

- [Documentação Oficial Python — Leitura e Escrita de Arquivos](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files)
  _Referencia completa sobre operações com arquivos em Python_

- [Documentação Oficial Python — Módulo csv](https://docs.python.org/pt-br/3/library/csv.html)
  _Referencia completa sobre leitura e escrita de arquivos CSV_

- [W3Schools — Python CSV](https://www.w3schools.com/python/python_csv.asp)
  _Tutorial prático sobre como trabalhar com arquivos CSV_

---

## Perguntas Frequentes (FAQ)

**P: O que e um arquivo de texto?**
R: E um arquivo que contem apenas caracteres legiveis — letras, números, espacos e símbolos. Arquivos `.txt` e `.csv` sao exemplos de arquivos de texto. Você pode abri-los em qualquer editor de texto.

**P: O que significa "abrir" um arquivo em Python?**
R: Abrir um arquivo e como pegar um caderno da estante: você pede ao Python para acessar o arquivo no disco do computador para que você possa ler ou escrever nele. Usamos a função `open()` para isso.

**P: O que e o gerenciador de contexto with?**
R: O `with` e uma estrutura do Python que garante que o arquivo sera fechado automaticamente quando você terminar de usa-lo. E como um assistente que abre a porta para você e fecha quando você sai — você não precisa se preocupar em fechar.

**P: O que acontece se eu esquecer de fechar um arquivo?**
R: O arquivo pode ficar "travado" e outros programas podem não conseguir acessa-lo. Além disso, dados que você escreveu podem não ser salvos corretamente. Por isso, sempre use `with` — ele fecha automaticamente.

**P: Qual a diferença entre os modos "w" e "a"?**
R: O modo `"w"` (write) **apaga todo o conteúdo** do arquivo antes de escrever. O modo `"a"` (append) **adiciona no final** sem apagar nada. Se você quer manter o que ja tem e acrescentar mais, use `"a"`.

**P: O modo "w" apaga o arquivo inteiro mesmo?**
R: Sim! Assim que você abre um arquivo com modo `"w"`, todo o conteúdo anterior e apagado, mesmo que você não escreva nada. Tenha muito cuidado ao usar esse modo.

**P: O que e encoding UTF-8?**
R: UTF-8 e um padrão de codificacao que permite representar caracteres de praticamente todos os idiomas do mundo, incluindo acentos e cedilha do portugues. Sempre use `encoding="utf-8"` ao trabalhar com textos em portugues.

**P: Preciso sempre usar encoding="utf-8"?**
R: E altamente recomendado, especialmente quando seu texto contem acentos ou caracteres especiais. Sem o encoding correto, você pode ver caracteres estranhos no lugar dos acentos.

**P: O que e o \n que aparece no final das linhas?**
R: O `\n` e o caractere de **quebra de linha** (newline). Ele indica onde uma linha termina e a proxima comeca. Quando você escreve `\n` em um arquivo, o texto pula para a linha seguinte.

**P: Por que readline() inclui \n no final?**
R: Porque o `\n` faz parte do conteúdo da linha no arquivo. Use `strip()` para remover espacos e quebras de linha das pontas da string: `line.strip()`.

**P: Qual a diferença entre read() e readlines()?**
R: `read()` retorna **uma única string** com todo o conteúdo. `readlines()` retorna uma **lista de strings**, onde cada elemento e uma linha do arquivo. Use `read()` quando quer o texto inteiro, e `readlines()` quando quer trabalhar com cada linha separadamente.

**P: O que e um arquivo CSV?**
R: CSV significa "Comma-Separated Values" (Valores Separados por Virgula). E um formato simples para armazenar dados em forma de tabela, onde cada linha e um registro e os valores sao separados por virgulas. E muito usado para trocar dados entre programas.

**P: Qual a diferença entre csv.reader e csv.DictReader?**
R: O `csv.reader` le cada linha como uma **lista** — você acessa valores pela posição (índice). O `csv.DictReader` le cada linha como um **dicionário** — você acessa valores pelo nome da coluna. O DictReader e mais legivel e menos propenso a erros.

**P: O que e o cabecalho (header) de um CSV?**
R: E a primeira linha do arquivo CSV que contem os nomes das colunas. Por exemplo: `name,age,city`. O `csv.DictReader` usa essa linha automaticamente como chaves dos dicionários.

**P: Por que usar newline="" ao abrir CSV para escrita?**
R: No Windows, sem `newline=""`, o arquivo CSV pode ter linhas em branco extras entre cada registro. Esse parametro evita esse problema. No Linux não causa problemas, mas e uma boa prática incluir sempre para garantir compatibilidade.

**P: O que e FileNotFoundError?**
R: E um erro que acontece quando você tenta abrir um arquivo que não existe. E como procurar um livro na estante e ele não estar la. Use `try/except` para tratar esse erro e exibir uma mensagem amigavel.

**P: O que e PermissionError?**
R: E um erro que acontece quando você não tem permissão para acessar um arquivo. No Linux, cada arquivo tem permissões que controlam quem pode ler, escrever ou executar. Use `try/except` para tratar esse erro.

**P: Posso ler e escrever no mesmo arquivo ao mesmo tempo?**
R: Sim, existe o modo `"r+"` que permite leitura e escrita. Porém, para iniciantes, e mais seguro e claro abrir o arquivo duas vezes — uma para ler e outra para escrever. Isso evita confusoes.

**P: Como sei em qual pasta o arquivo sera criado?**
R: O arquivo e criado na mesma pasta onde você executou o programa Python. Use o comando `pwd` no terminal para ver em qual pasta você esta. Se quiser criar em outra pasta, use o caminho completo: `open("/home/usuario/dados.txt", "w")`.

**P: E normal ter dificuldade com arquivos no inicio?**
R: Sim, completamente normal! Trabalhar com arquivos envolve entender o sistema de arquivos do computador, caminhos de pastas e permissões. Com prática, isso se torna natural. Não desanime — cada erro e uma oportunidade de aprender.

---

## Exercícios de Fixacao

Pratique o que aprendeu com os exercícios do módulo:

[Exercícios do Módulo 20 — Leitura e Escrita de Arquivos](20-leitura-escrita-arquivos-exercícios.md)

---

[<- Anterior: Estruturas de Dados](19-estruturas-dados.md) | [Glossário](00-glossário.md) | [Próximo: Manipulação JSON ->](21-manipulação-json.md)
