# Referência Rápida — Comandos e Funções Python

[← Voltar ao índice do Glossário](00-glossario.md)

Este arquivo é uma referência rápida dos comandos e funções mais usados do Python ao longo do curso. Consulte sempre que precisar lembrar como usar algo.

---

## Funções Básicas (Built-in)

Funções que já vêm prontas no Python — você não precisa instalar nada para usá-las.

| Função | O que faz | Exemplo | Resultado |
|--------|-----------|---------|-----------|
| `print()` | Exibe valores no terminal | `print("Olá")` | `Olá` |
| `input()` | Lê texto digitado pelo usuário | `nome = input("Seu nome: ")` | Espera digitação |
| `type()` | Mostra o tipo de um valor | `type(42)` | `<class 'int'>` |
| `int()` | Converte para número inteiro | `int("42")` | `42` |
| `float()` | Converte para número decimal | `float("3.14")` | `3.14` |
| `str()` | Converte para texto (string) | `str(42)` | `"42"` |
| `bool()` | Converte para verdadeiro/falso | `bool(1)` | `True` |
| `len()` | Conta o tamanho (quantidade de itens) | `len("Python")` | `6` |
| `range()` | Gera sequência de números | `range(5)` | `0, 1, 2, 3, 4` |
| `abs()` | Valor absoluto (sem sinal negativo) | `abs(-7)` | `7` |
| `round()` | Arredonda um número decimal | `round(3.7)` | `4` |
| `max()` | Retorna o maior valor | `max(3, 7, 1)` | `7` |
| `min()` | Retorna o menor valor | `min(3, 7, 1)` | `1` |
| `sum()` | Soma todos os itens de uma lista | `sum([1, 2, 3])` | `6` |
| `sorted()` | Retorna lista ordenada | `sorted([3, 1, 2])` | `[1, 2, 3]` |
| `enumerate()` | Numera itens de uma lista | `enumerate(["a", "b"])` | `(0, "a"), (1, "b")` |
| `zip()` | Combina duas listas em pares | `zip([1, 2], ["a", "b"])` | `(1, "a"), (2, "b")` |
| `isinstance()` | Verifica se valor é de um tipo | `isinstance(42, int)` | `True` |
| `open()` | Abre um arquivo | `open("dados.txt", "r")` | Objeto de arquivo |

 [W3Schools — Python Built-in Functions](https://www.w3schools.com/python/python_ref_functions.asp)

---

## Operadores Matemáticos

| Operador | O que faz | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `+` | Soma (adição) | `5 + 3` | `8` |
| `-` | Subtração | `10 - 4` | `6` |
| `*` | Multiplicação | `3 * 4` | `12` |
| `/` | Divisão (com decimais) | `7 / 2` | `3.5` |
| `//` | Divisão inteira (sem decimais) | `7 // 2` | `3` |
| `%` | Módulo (resto da divisão) | `10 % 3` | `1` |
| `**` | Exponenciação (potência) | `2 ** 3` | `8` |

 [W3Schools — Python Operators](https://www.w3schools.com/python/python_operators.asp)

---

## Operadores de Comparação

| Operador | O que faz | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `==` | Igual a | `5 == 5` | `True` |
| `!=` | Diferente de | `5 != 3` | `True` |
| `>` | Maior que | `7 > 3` | `True` |
| `<` | Menor que | `3 < 7` | `True` |
| `>=` | Maior ou igual a | `5 >= 5` | `True` |
| `<=` | Menor ou igual a | `3 <= 7` | `True` |

 [W3Schools — Python Operators](https://www.w3schools.com/python/python_operators.asp)

---

## Operadores Lógicos

| Operador | O que faz | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `and` | Verdadeiro se AMBOS forem verdadeiros | `True and False` | `False` |
| `or` | Verdadeiro se PELO MENOS UM for verdadeiro | `True or False` | `True` |
| `not` | Inverte o valor (verdadeiro vira falso) | `not True` | `False` |

 [W3Schools — Python Operators](https://www.w3schools.com/python/python_operators.asp)

---

## Métodos de String

Métodos são ações que você pode executar em strings (textos). Use com `texto.metodo()`.

| Método | O que faz | Exemplo | Resultado |
|--------|-----------|---------|-----------|
| `.upper()` | Converte para MAIÚSCULAS | `"olá".upper()` | `"OLÁ"` |
| `.lower()` | Converte para minúsculas | `"OLÁ".lower()` | `"olá"` |
| `.strip()` | Remove espaços do início e fim | `" olá ".strip()` | `"olá"` |
| `.split()` | Divide texto em lista | `"a,b,c".split(",")` | `["a", "b", "c"]` |
| `.replace()` | Substitui texto | `"olá".replace("o", "a")` | `"alá"` |
| `.find()` | Encontra posição de um texto | `"Python".find("th")` | `2` |
| `.count()` | Conta ocorrências | `"banana".count("a")` | `3` |
| `.startswith()` | Verifica se começa com | `"Python".startswith("Py")` | `True` |
| `.endswith()` | Verifica se termina com | `"arquivo.py".endswith(".py")` | `True` |
| `.join()` | Junta lista em texto | `", ".join(["a", "b"])` | `"a, b"` |
| `.format()` | Formata texto com valores | `"Olá {}".format("Ana")` | `"Olá Ana"` |
| `.isdigit()` | Verifica se é só números | `"123".isdigit()` | `True` |
| `.isalpha()` | Verifica se é só letras | `"abc".isalpha()` | `True` |

 [W3Schools — Python String Methods](https://www.w3schools.com/python/python_ref_string.asp)

---

## Métodos de Lista

Métodos são ações que você pode executar em listas. Use com `lista.metodo()`.

| Método | O que faz | Exemplo |
|--------|-----------|---------|
| `.append(x)` | Adiciona item ao final | `lista.append("novo")` |
| `.insert(i, x)` | Insere item na posição i | `lista.insert(0, "primeiro")` |
| `.remove(x)` | Remove primeira ocorrência de x | `lista.remove("item")` |
| `.pop(i)` | Remove e retorna item da posição i | `lista.pop(0)` |
| `.pop()` | Remove e retorna o último item | `lista.pop()` |
| `.sort()` | Ordena a lista (modifica a original) | `lista.sort()` |
| `.reverse()` | Inverte a ordem da lista | `lista.reverse()` |
| `.index(x)` | Retorna posição de x | `lista.index("item")` |
| `.count(x)` | Conta ocorrências de x | `lista.count("item")` |
| `.extend(outra)` | Adiciona itens de outra lista | `lista.extend([1, 2])` |
| `.clear()` | Remove todos os itens | `lista.clear()` |
| `.copy()` | Cria uma cópia da lista | `nova = lista.copy()` |

 [W3Schools — Python List Methods](https://www.w3schools.com/python/python_ref_list.asp)

---

## Métodos de Dicionário

| Método | O que faz | Exemplo |
|--------|-----------|---------|
| `.keys()` | Retorna todas as chaves | `dicio.keys()` |
| `.values()` | Retorna todos os valores | `dicio.values()` |
| `.items()` | Retorna pares (chave, valor) | `dicio.items()` |
| `.get(chave)` | Retorna valor da chave (sem erro se não existir) | `dicio.get("nome")` |
| `.get(chave, padrão)` | Retorna valor ou padrão se não existir | `dicio.get("nome", "N/A")` |
| `.update(outro)` | Atualiza com dados de outro dicionário | `dicio.update({"nome": "Ana"})` |
| `.pop(chave)` | Remove e retorna valor da chave | `dicio.pop("nome")` |
| `.clear()` | Remove todos os itens | `dicio.clear()` |

 [W3Schools — Python Dictionary Methods](https://www.w3schools.com/python/python_ref_dictionary.asp)

---

## Métodos de Conjunto (Set)

| Método | O que faz | Exemplo |
|--------|-----------|---------|
| `.add(x)` | Adiciona um elemento | `conjunto.add(5)` |
| `.remove(x)` | Remove elemento (erro se não existir) | `conjunto.remove(5)` |
| `.discard(x)` | Remove elemento (sem erro se não existir) | `conjunto.discard(5)` |
| `.union(outro)` | União de dois conjuntos | `a.union(b)` |
| `.intersection(outro)` | Interseção (elementos em comum) | `a.intersection(b)` |
| `.difference(outro)` | Diferença (elementos que estão em a mas não em b) | `a.difference(b)` |

 [W3Schools — Python Set Methods](https://www.w3schools.com/python/python_ref_set.asp)

---

## Funções do Módulo json

| Função | O que faz | Exemplo |
|--------|-----------|---------|
| `json.loads(texto)` | Converte string JSON → Python | `json.loads('{"nome": "Ana"}')` |
| `json.dumps(dados)` | Converte Python → string JSON | `json.dumps({"nome": "Ana"})` |
| `json.load(arquivo)` | Lê JSON de um arquivo | `json.load(open("dados.json"))` |
| `json.dump(dados, arquivo)` | Escreve Python em arquivo JSON | `json.dump(dados, open("dados.json", "w"))` |

 [W3Schools — Python JSON](https://www.w3schools.com/python/python_json.asp)

---

## Comandos de Terminal Linux

Comandos que você digita no terminal para interagir com o computador.

| Comando | O que faz | Exemplo |
|---------|-----------|---------|
| `cd pasta` | Muda para outra pasta (change directory) | `cd ~/meus-projetos` |
| `cd ..` | Volta uma pasta acima | `cd ..` |
| `ls` | Lista arquivos na pasta atual | `ls` |
| `ls -la` | Lista arquivos com detalhes (incluindo ocultos) | `ls -la` |
| `pwd` | Mostra a pasta atual (print working directory) | `pwd` |
| `mkdir nome` | Cria uma nova pasta | `mkdir meu-projeto` |
| `touch nome` | Cria um arquivo vazio | `touch programa.py` |
| `rm arquivo` | Remove (apaga) um arquivo | `rm programa.py` |
| `rm -r pasta` | Remove uma pasta e tudo dentro dela | `rm -r pasta-antiga` |
| `cp origem destino` | Copia um arquivo | `cp programa.py copia.py` |
| `mv origem destino` | Move ou renomeia um arquivo | `mv antigo.py novo.py` |
| `cat arquivo` | Mostra o conteúdo de um arquivo | `cat programa.py` |
| `python3 arquivo.py` | Executa um programa Python | `python3 meu_programa.py` |
| `python3 --version` | Mostra a versão do Python instalada | `python3 --version` |
| `pip install pacote` | Instala uma biblioteca Python | `pip install fastapi` |
| `pip freeze` | Lista bibliotecas instaladas | `pip freeze` |
| `chmod +x arquivo` | Dá permissão de execução a um arquivo | `chmod +x script.py` |
| `Ctrl + C` | Interrompe um programa em execução | — |
| `Ctrl + Alt + T` | Abre o terminal (atalho do Linux) | — |

 [W3Schools — Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp)

---

## Palavras-Chave do Python (Keywords)

Palavras reservadas que têm significado especial na linguagem. Você não pode usá-las como nomes de variáveis ou funções.

| Palavra-chave | O que faz | Exemplo |
|---------------|-----------|---------|
| `if` | Condição: "se" | `if age >= 18:` |
| `elif` | Condição: "senão se" | `elif age >= 12:` |
| `else` | Condição: "senão" / bloco sem erro em try | `else:` |
| `for` | Loop: "para cada" | `for item in list:` |
| `while` | Loop: "enquanto" | `while count < 10:` |
| `break` | Interrompe o loop | `break` |
| `continue` | Pula para próxima volta do loop | `continue` |
| `def` | Define uma função | `def calculate():` |
| `return` | Retorna valor de uma função | `return result` |
| `class` | Define uma classe | `class Product:` |
| `self` | Referência ao próprio objeto | `self.name = name` |
| `import` | Importa um módulo | `import json` |
| `from` | Importa parte de um módulo | `from math import sqrt` |
| `as` | Cria um apelido (alias) | `import json as j` |
| `in` | Pertencimento / iteração | `for x in lista:` / `if x in lista:` |
| `is` | Verifica identidade | `if x is None:` |
| `not` | Nega uma condição | `if not found:` |
| `and` | E lógico (ambos verdadeiros) | `if a > 0 and b > 0:` |
| `or` | Ou lógico (pelo menos um verdadeiro) | `if a > 0 or b > 0:` |
| `try` | Tenta executar código | `try:` |
| `except` | Captura erro | `except ValueError:` |
| `finally` | Executa sempre (com ou sem erro) | `finally:` |
| `raise` | Levanta uma exceção | `raise ValueError("erro")` |
| `with` | Gerenciador de contexto | `with open("f.txt") as f:` |
| `pass` | Não faz nada (placeholder) | `def todo(): pass` |
| `del` | Deleta variável/item | `del lista[0]` |
| `global` | Declara variável global | `global counter` |
| `lambda` | Função anônima (avançado) | `dobro = lambda x: x * 2` |
| `True` | Valor booleano verdadeiro | `is_active = True` |
| `False` | Valor booleano falso | `is_active = False` |
| `None` | Valor vazio/nulo | `result = None` |
| `match` | Compara padrões (Python 3.10+) | `match option:` |
| `case` | Define um padrão em match | `case 1:` |

 [W3Schools — Python Keywords](https://www.w3schools.com/python/python_ref_keywords.asp)

---

## Estruturas de Controle (Resumo)

```python
# Condicional (if/elif/else)
if condition:       # se a condição for verdadeira
    pass            # faça algo
elif other:         # senão, se outra condição
    pass            # faça outra coisa
else:               # senão (nenhuma condição anterior)
    pass            # faça isso

# Loop for
for item in collection:    # para cada item na coleção
    pass                   # faça algo com item

# Loop for com range
for i in range(5):         # para i de 0 até 4
    pass                   # faça algo

# Loop while
while condition:           # enquanto a condição for verdadeira
    pass                   # faça algo

# Tratamento de erros
try:                       # tente fazer isso
    pass                   # código que pode dar erro
except ValueError:         # se der erro de valor
    pass                   # trate o erro
finally:                   # sempre execute isso
    pass                   # código de limpeza

# Função
def function_name(parameter):    # definir função com parâmetro
    # corpo da função
    return result                # retornar resultado

# Classe
class ClassName:                 # definir classe
    def __init__(self, attr):    # método inicializador
        self.attr = attr         # definir atributo
    
    def method(self):            # definir método
        return self.attr         # retornar atributo
```

 [W3Schools — Python Tutorial](https://www.w3schools.com/python/)

---

[← Voltar ao índice do Glossário](00-glossario.md)
