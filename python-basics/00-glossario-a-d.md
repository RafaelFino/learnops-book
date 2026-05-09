# Glossário — Letras A a D

[← Voltar ao índice do Glossário](00-glossario.md)

---

## A

### Acumulador
Padrão de programação onde uma variável vai somando (acumulando) valores ao longo de um loop. É como um cofrinho: a cada volta do loop, você coloca mais uma moeda, e no final tem o total acumulado.

 [W3Schools — Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

### Algoritmo
Sequência finita e ordenada de passos para resolver um problema ou realizar uma tarefa. Pense em uma receita de cozinha: ela descreve cada etapa, na ordem certa, para preparar um prato. Um algoritmo é a mesma coisa, mas para o computador.

 [W3Schools — Python Introduction](https://www.w3schools.com/python/python_intro.asp) · [Documentação Python](https://docs.python.org/pt-br/3/)

### Ambiente de Desenvolvimento
Conjunto de ferramentas configuradas no computador para programar. Neste curso, o ambiente inclui o sistema operacional Linux, o terminal, o Python instalado e o editor VSCode. É como preparar a bancada da cozinha com todos os utensílios antes de começar a cozinhar.

 [W3Schools — Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp)

### API (Application Programming Interface)
Interface de Programação de Aplicações. Conjunto de regras que permite que programas diferentes se comuniquem entre si. Pense em um garçom de restaurante: você (o programa) faz um pedido ao garçom (a API), e ele leva o pedido à cozinha (outro programa) e traz a resposta.

 [W3Schools — What is an API?](https://www.w3schools.com/js/js_api_intro.asp)

### Argumento
Valor que você passa para uma função quando a chama. Se a função é como uma máquina de suco, o argumento é a fruta que você coloca dentro dela. Veja também: Parâmetro.

 [W3Schools — Python Functions](https://www.w3schools.com/python/python_functions.asp)

### as
Palavra-chave do Python usada para criar um apelido (alias). Tem dois usos principais: (1) em imports: `import json as j` permite usar `j` em vez de `json`; (2) com `with`: `with open("arquivo.txt") as f` dá o nome `f` ao arquivo aberto.

### ASGI (Asynchronous Server Gateway Interface)
Padrão que servidores como o Uvicorn usam para se comunicar com frameworks como o FastAPI. É a evolução do WSGI, suportando operações assíncronas. Para iniciantes, basta saber que o Uvicorn é o servidor e o FastAPI é a aplicação — o ASGI é a "ponte" entre eles.

 [Documentação FastAPI](https://fastapi.tiangolo.com/)

 [W3Schools — Python Modules](https://www.w3schools.com/python/python_modules.asp)

### Atributo
Característica ou propriedade de um objeto em orientação a objetos. Se um objeto é um "carro", seus atributos podem ser "cor", "marca" e "ano". Em Python, atributos são definidos dentro do método `__init__` de uma classe.

 [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp)

---

## B

### Banco de Dados
Sistema que armazena dados de forma organizada para que possam ser consultados, atualizados e gerenciados. Pense em um arquivo de fichas organizado em uma gaveta — cada ficha contém informações sobre algo e você pode buscar, adicionar ou remover fichas.

 [W3Schools — Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)

### Bloco de Código
Conjunto de linhas de código que pertencem a uma mesma estrutura (como um if, for ou função). Em Python, blocos são definidos pela indentação — todas as linhas recuadas no mesmo nível fazem parte do mesmo bloco.

 [W3Schools — Python Indentation](https://www.w3schools.com/python/python_syntax.asp)

### Boas Práticas
Conjunto de convenções e padrões que tornam o código mais legível, organizado e profissional. Em Python, as boas práticas são definidas pelo PEP 8. É como manter a cozinha limpa e organizada enquanto cozinha.

 [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)

### Bool / Booleano
Tipo de dado que só pode ter dois valores: `True` (verdadeiro) ou `False` (falso). É como um interruptor de luz: ou está ligado ou está desligado.

 [W3Schools — Python Booleans](https://www.w3schools.com/python/python_booleans.asp)

### Break
Comando usado dentro de loops (for ou while) para interromper a repetição imediatamente. É como apertar o botão de parada de emergência.

 [W3Schools — Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

### Bytecode
Código intermediário gerado quando uma linguagem como Java ou Python é compilada/interpretada. Não é legível por humanos nem diretamente pelo processador — precisa de uma máquina virtual (como a JVM) para ser executado.

 [Documentação Python — Compilação](https://docs.python.org/pt-br/3/glossary.html)

---

## C

### CamelCase
Convenção de nomenclatura onde cada palavra começa com letra maiúscula, sem espaços. Exemplo: `MinhaClasse`, `ProdutoEletronico`. Em Python, CamelCase é usado para nomes de classes. Veja também: snake_case.

 [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp)

### Chmod
Comando do terminal Linux que altera as permissões de um arquivo. "chmod" vem de "change mode" (mudar modo). Exemplo: `chmod +x arquivo.py` permite que o arquivo seja executado.

 [W3Schools — Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)

### Classe
Molde ou receita para criar objetos em orientação a objetos. Uma classe define quais atributos e métodos os objetos terão. É como uma forma de bolo: a forma é a classe, e cada bolo feito com ela é um objeto. Em Python, classes são definidas com a palavra-chave `class`.

 [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp)

### class (palavra-chave)
Palavra-chave do Python usada para definir uma classe. Exemplo: `class Product:` cria uma classe chamada Product. Nomes de classes seguem a convenção CamelCase.

 [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp)

### Comentário
Texto no código ignorado pelo Python, serve apenas para explicar o que o código faz. Comentários começam com `#`. São como anotações em uma receita.

 [W3Schools — Python Comments](https://www.w3schools.com/python/python_comments.asp)

### Commit
No contexto de bancos de dados, é o ato de confirmar e salvar as alterações feitas. Quando você insere, atualiza ou exclui dados no SQLite, as mudanças ficam "pendentes" até você chamar `commit()`. É como clicar em "Salvar" depois de editar um documento.

 [Documentação Python — sqlite3](https://docs.python.org/pt-br/3/library/sqlite3.html)

### Compilador
Programa que traduz todo o código-fonte para linguagem de máquina de uma só vez, antes da execução. É como traduzir um livro inteiro antes de publicá-lo.

 [W3Schools — Python Introduction](https://www.w3schools.com/python/python_intro.asp)

### Concatenação
Operação de juntar duas ou mais strings (textos) em uma só. É como emendar dois pedaços de barbante para formar um mais longo.

 [W3Schools — Python Strings](https://www.w3schools.com/python/python_strings.asp)

### Condição / Condicional
Estrutura que permite ao programa tomar decisões. Usa `if` (se), `elif` (senão se) e `else` (senão). É como decidir o que vestir: "se estiver frio, uso casaco; senão, uso camiseta".

 [W3Schools — Python If...Else](https://www.w3schools.com/python/python_conditions.asp)

### Conjunto (Set)
Estrutura de dados que armazena elementos únicos, sem ordem definida e sem duplicatas. É como uma coleção de figurinhas onde cada figurinha aparece apenas uma vez.

 [W3Schools — Python Sets](https://www.w3schools.com/python/python_sets.asp)

### Construtor (__init__)
Método especial de uma classe que é executado automaticamente quando um novo objeto é criado. Em Python, o construtor é o método `__init__`. É como o momento em que você preenche a ficha de cadastro ao criar uma conta — os dados iniciais são definidos ali.

 [W3Schools — Python Classes](https://www.w3schools.com/python/python_classes.asp)

### Contador
Variável usada dentro de um loop para contar quantas vezes algo aconteceu. Começa em zero e aumenta de 1 em 1 a cada volta. É como contar nos dedos.

 [W3Schools — Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

### Continue
Comando usado dentro de loops para pular para a próxima repetição, ignorando o restante do bloco atual. É como pular uma página de um livro.

 [W3Schools — Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

### Convenção de Idioma
Padrão adotado neste curso onde todo código Python utiliza nomes em inglês (variáveis, funções, classes) seguindo a prática profissional, enquanto todos os comentários e explicações são em português brasileiro, com tradução de cada termo em inglês.

 [W3Schools — Python Variables](https://www.w3schools.com/python/python_variables.asp)

### Conversão de Tipos (Type Casting)
Processo de transformar um valor de um tipo para outro. Exemplo: `int("42")` transforma o texto "42" no número 42. É como converter metros para centímetros — o valor é o mesmo, mas a representação muda.

 [W3Schools — Python Casting](https://www.w3schools.com/python/python_casting.asp)

### CORS (Cross-Origin Resource Sharing)
Política de segurança dos navegadores que controla quais sites podem acessar uma API. Se um site em um domínio tenta acessar uma API em outro domínio, o navegador pode bloquear a requisição. O FastAPI tem ferramentas para configurar CORS.

 [W3Schools — HTTP Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)

### CRUD
Sigla para Create (Criar), Read (Ler), Update (Atualizar) e Delete (Excluir). São as quatro operações básicas de qualquer sistema de cadastro. Pense em uma agenda de contatos: adicionar, consultar, editar e apagar.

 [W3Schools — Python MySQL](https://www.w3schools.com/python/python_mysql_getstarted.asp)

### CSV
Formato de arquivo onde dados são separados por vírgulas (Comma-Separated Values). É como uma planilha simples em formato de texto.

 [Documentação Python — Módulo csv](https://docs.python.org/pt-br/3/library/csv.html)

### Cursor
No contexto de bancos de dados, é o objeto que executa comandos SQL. Pense nele como uma "caneta" que escreve e lê no banco de dados. Você cria um cursor a partir da conexão e usa `cursor.execute()` para executar comandos.

 [Documentação Python — sqlite3](https://docs.python.org/pt-br/3/library/sqlite3.html)

---

## D

### Debugging / Depuração
Processo de encontrar e corrigir erros (bugs) no código. É como ser um detetive investigando por que uma receita não deu certo.

 [W3Schools — Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

### Decorador (Decorator)
Recurso do Python que permite modificar o comportamento de uma função ou classe. Em FastAPI, decoradores como `@app.get()` e `@app.post()` associam funções Python a rotas HTTP. É como colocar um selo em uma carta — o selo (decorador) adiciona informação sobre para onde a carta (função) deve ir.

 [W3Schools — Python Decorators](https://www.w3schools.com/python/python_decorators.asp)

### def
Palavra-chave do Python usada para definir (criar) uma função. "def" vem de "define" (definir em inglês). Exemplo: `def calculate_total():` cria uma função chamada calculate_total.

 [W3Schools — Python Functions](https://www.w3schools.com/python/python_functions.asp)

### del
Palavra-chave do Python usada para deletar (remover) uma variável, item de lista ou chave de dicionário. Exemplo: `del lista[0]` remove o primeiro item da lista. É como apagar um item de uma lista de compras.

 [W3Schools — Python Variables](https://www.w3schools.com/python/python_variables.asp)

### DELETE
Método HTTP usado para remover um recurso do servidor. Em APIs, DELETE é usado para excluir registros (como apagar um produto do cadastro).

 [W3Schools — HTTP Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)

### Dicionário (dict)
Estrutura de dados que armazena pares de chave e valor. É como uma agenda telefônica: o nome é a chave e o número é o valor. Criados com chaves `{}`.

 [W3Schools — Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

### Diretório / Pasta
Local no sistema de arquivos onde arquivos e outros diretórios são organizados. É como uma gaveta em um armário.

 [W3Schools — Python File Handling](https://www.w3schools.com/python/python_file_handling.asp)

### Divisão Inteira
Operação que divide dois números e retorna apenas a parte inteira, descartando decimais. Em Python: `//`. Exemplo: `7 // 2` = `3`. É como dividir 7 pizzas entre 2 pessoas — cada uma fica com 3 inteiras, o pedaço que sobra é ignorado.

 [W3Schools — Python Operators](https://www.w3schools.com/python/python_operators.asp)

### DRY (Don't Repeat Yourself)
Princípio de programação: "não se repita". Em vez de escrever o mesmo código várias vezes, crie uma função e reutilize. É como escrever uma receita uma vez e consultá-la sempre que precisar.

 [W3Schools — Python Functions](https://www.w3schools.com/python/python_functions.asp)

---

[← Voltar ao índice do Glossário](00-glossario.md) · [Próximo: E-I →](00-glossario-e-i.md)
