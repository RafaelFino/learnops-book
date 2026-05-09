# Curso de Programação com Python — Documentação Completa

Bem-vindo ao curso de programação com Python!

Este material foi criado com muito carinho para guiar você, passo a passo, desde o zero absoluto até a construção de um projeto real. Não importa se você nunca abriu um terminal ou se não sabe o que é uma "variável" — aqui, tudo será explicado com calma, paciência e exemplos do dia a dia.

---

## Sobre Este Material

Este é um curso completo de **lógica de programação e desenvolvimento com Python**, voltado para estudantes iniciantes de um curso técnico. O material foi pensado para pessoas de todas as idades — jovens e adultos — que estão começando sua jornada como desenvolvedores de software.

Você não precisa ter experiência prévia com programação, matemática avançada ou informática. Tudo o que você precisa é de vontade de aprender e um computador com Linux.

### O que você vai aprender?

Ao longo de 33 módulos organizados em ordem progressiva, você vai:

- Entender o que é um programa de computador e como ele funciona
- Preparar seu computador para programar em Python
- Aprender os fundamentos da linguagem Python (variáveis, condições, repetições, funções)
- Trabalhar com estruturas de dados (listas, dicionários, tuplas, conjuntos)
- Ler e escrever arquivos
- Criar classes e objetos
- Organizar projetos profissionais
- Construir um projeto completo de cadastro de produtos (CRUD) que evolui em 4 fases: memória → banco de dados → interface web → documentação da API

### Para quem é este material?

Este material é para **qualquer pessoa** que deseja aprender a programar, independentemente da idade ou experiência de vida. Ele foi escrito pensando em:

- Pessoas que nunca tiveram contato com programação
- Pessoas com pouca familiaridade com computadores e o sistema Linux
- Pessoas com base matemática limitada (apenas as quatro operações básicas)
- Pessoas que não falam inglês

Se você consegue ligar um computador e tem curiosidade, você já tem tudo o que precisa para começar. Aprender a programar é como aprender a cozinhar: no início parece complicado, mas com prática e paciência, logo você estará criando suas próprias "receitas" (programas).

### Convenção de idioma: por que o código está em inglês?

Ao longo de todo este material, você vai notar algo importante: **os nomes dentro do código estão em inglês**, mas **todas as explicações e comentários estão em português**.

Isso acontece porque, no mundo profissional do desenvolvimento de software, é uma convenção universal escrever código em inglês. Nomes de variáveis, funções, classes e métodos são escritos em inglês para que qualquer desenvolvedor no mundo consiga ler e entender o código.

Mas não se preocupe! Você **não precisa saber inglês** para acompanhar este curso. Cada termo em inglês que aparecer no código será:

1. **Traduzido** — você sempre verá a tradução para o português
2. **Explicado** — o significado do termo será detalhado nos comentários do código
3. **Repetido** — termos importantes aparecerão várias vezes ao longo dos módulos, para que você se familiarize naturalmente

Veja um exemplo de como isso funciona na prática:

```python
# Criando uma lista de compras (shopping list)
# "shopping_list" = lista de compras
shopping_list = ["arroz", "feijão", "macarrão"]

# Percorrendo cada item (item = item/elemento) da lista
for item in shopping_list:
    # print() exibe o valor no terminal
    print(item)
```

Pense assim: é como aprender a cozinhar usando uma receita que tem os nomes dos ingredientes em outro idioma, mas com a tradução e a explicação de cada um ao lado. Com o tempo, você vai se acostumando com os termos e isso se tornará natural.

---

## Como Usar Este Material (Guia de Estudos)

Este material foi organizado para que você estude de forma autônoma, no seu próprio ritmo. Aqui está o passo a passo recomendado para aproveitar ao máximo cada módulo:

### Passo 1 — Leia a teoria com calma

Cada módulo começa com uma explicação teórica do assunto. Leia com atenção, sem pressa. Se encontrar um termo que não conhece, consulte o [Glossário do Curso](00-glossario.md). É completamente normal precisar reler um trecho mais de uma vez — até programadores experientes fazem isso.

### Passo 2 — Execute os exemplos de código

Depois de ler a teoria, você encontrará exemplos de código. **Não apenas leia os exemplos — copie e execute cada um deles no seu computador.** Programar é como andar de bicicleta: você só aprende fazendo. A seção [Como Copiar e Executar os Códigos](#como-copiar-e-executar-os-códigos) explica exatamente como fazer isso.

### Passo 3 — Faça os exercícios de fixação

Ao final de cada módulo, há exercícios práticos para você resolver. Cada exercício tem a seguinte estrutura:

- **Enunciado** — A descrição do problema que você precisa resolver
- **Dicas** — Sugestões de como pensar sobre a solução (leia antes de começar!)
- **Proposta de Teste** — Exemplos de entrada e saída esperada para você verificar se seu programa funciona corretamente. Por exemplo: "execute o programa e digite 5 — a saída deve ser 25". Sempre teste seu programa com as entradas sugeridas antes de consultar a resposta.
- **Resposta Comentada** — A solução completa com explicações detalhadas em cada linha do código. Use apenas como referência de aprendizado, depois de tentar resolver sozinho.

**Dica importante:** Tente resolver cada exercício sozinho primeiro. Consulte as dicas se precisar de ajuda. Use a proposta de teste para verificar se sua solução está correta. Só depois consulte a resposta comentada.

### Passo 4 — Consulte o glossário quando necessário

Sempre que encontrar um termo desconhecido, consulte o [Glossário do Curso](00-glossario.md). Ele contém explicações simples de todos os termos técnicos usados ao longo dos módulos, com links para fontes externas caso você queira se aprofundar.

### Passo 5 — Revise antes de avançar

Antes de passar para o próximo módulo, releia rapidamente os pontos principais e tente refazer pelo menos um exercício sem consultar a resposta. Isso ajuda a fixar o conhecimento — é como revisar os ingredientes de uma receita antes de tentar fazê-la de memória.

---

## Como Copiar e Executar os Códigos

Ao longo dos módulos, você encontrará blocos de código Python que pode copiar e executar no seu computador. Aqui está o passo a passo detalhado de como fazer isso:

### 1. Copie o código

Nos blocos de código (aqueles trechos com fundo diferente), selecione todo o texto do código e copie. Você pode usar o atalho `Ctrl + C` para copiar.

### 2. Cole o código em um arquivo

Abra o seu editor de código (VSCode, por exemplo) e cole o código em um novo arquivo. Use o atalho `Ctrl + V` para colar. Salve o arquivo com a extensão `.py` (por exemplo: `meu_programa.py`). Se você ainda não sabe como fazer isso, o [Módulo 03 — Preparação do Ambiente](03-preparacao-ambiente.md) explica tudo em detalhes.

### 3. Abra o terminal

No Linux, pressione `Ctrl + Alt + T` para abrir o terminal. O terminal é como uma janela de conversa com o computador — você digita comandos e ele executa.

### 4. Navegue até a pasta do seu arquivo

Use o comando `cd` (que significa "change directory", ou "mudar de diretório/pasta") para ir até a pasta onde você salvou o arquivo. Por exemplo:

```bash
cd ~/meus-projetos/python
```

> O símbolo `~` representa a sua pasta pessoal (home). O comando acima significa: "vá para a pasta `python` que está dentro da pasta `meus-projetos` na minha pasta pessoal".

Se você não tem certeza de em qual pasta está, use o comando `pwd` (que significa "print working directory", ou "mostrar o diretório atual"):

```bash
pwd
```

Para ver os arquivos que estão na pasta atual, use o comando `ls` (que significa "list", ou "listar"):

```bash
ls
```

### 5. Execute o programa

Digite o seguinte comando no terminal, substituindo `meu_programa.py` pelo nome do seu arquivo:

```bash
python3 meu_programa.py
```

> `python3` é o comando que chama o interpretador Python — o programa que lê e executa o seu código.

**Exemplo completo:** Se você salvou o seguinte código em um arquivo chamado `ola.py`:

```python
# Exibindo uma mensagem de boas-vindas no terminal
# print() = função que mostra texto na tela
print("Olá, mundo! Bem-vindo ao Python!")
```

E executou com:

```bash
python3 ola.py
```

A **saída esperada** no terminal será:

```
Olá, mundo! Bem-vindo ao Python!
```

### Erros comuns e como resolver

Não se preocupe se aparecer um erro — isso é completamente normal e faz parte do aprendizado. Aqui estão os erros mais comuns:

**`comando não encontrado` (command not found)**
Isso significa que o Python pode não estar instalado no seu computador, ou o comando está escrito de forma diferente. Consulte o [Módulo 03 — Preparação do Ambiente](03-preparacao-ambiente.md) para instruções de instalação.

**`arquivo não encontrado` (No such file or directory)**
Isso significa que o terminal não encontrou o arquivo que você tentou executar. Verifique se:
- Você está na pasta correta (use `pwd` para conferir)
- O nome do arquivo está escrito corretamente (use `ls` para ver os arquivos na pasta)
- O arquivo foi salvo com a extensão `.py`

**`permissão negada` (Permission denied)**
Isso significa que o sistema não permitiu a execução do arquivo. Consulte o [Módulo 04 — Execução, Permissões e Pastas](04-execucao-permissoes-pastas.md) para entender como resolver.

**`SyntaxError` (Erro de sintaxe)**
Isso significa que há um erro na escrita do código — como um parêntese esquecido ou uma palavra escrita errada. Releia o código com atenção e compare com o exemplo original. O [Módulo 17 — Debugging](17-debugging.md) ensina a ler e entender mensagens de erro.

---

## Progressão de Estudos (Ordem Recomendada)

Os módulos deste curso foram organizados em uma ordem específica, do mais simples ao mais complexo. Cada módulo constrói sobre o que foi aprendido nos anteriores — como os andares de uma casa, onde cada andar precisa do anterior para se sustentar.

**Por que seguir esta ordem?** Porque cada conceito novo depende de conceitos anteriores. Por exemplo, para entender "condicionais" (módulo 12), você precisa primeiro entender "operadores" (módulo 11). E para entender "operadores", você precisa saber o que são "variáveis" (módulo 7). Pular módulos é como tentar construir o segundo andar de uma casa sem ter construído o primeiro.

Aqui está a ordem recomendada de estudos:

| # | Módulo | Descrição |
|---|--------|-----------|
| — | [Glossário do Curso](00-glossario.md) |  Consulte a qualquer momento quando encontrar um termo desconhecido |
| 01 | [Introdução à Programação](01-introducao-programacao.md) | O que é um programa de computador e o que significa programar |
| 02 | [Scripts, Compilados e VM](02-scripts-compilados-vm.md) | Diferenças entre tipos de programas e onde o Python se encaixa |
| 03 | [Preparação do Ambiente](03-preparacao-ambiente.md) | Como instalar Python e VSCode no Linux |
| 04 | [Execução, Permissões e Pastas](04-execucao-permissoes-pastas.md) | Como executar programas, permissões de arquivo e organização de pastas |
| 05 | [História do Python](05-historia-python.md) | Quem criou o Python, sua filosofia e onde é usado no mundo real |
| 06 | [Entrada e Saída de Dados](06-entrada-saida.md) | Aprendendo input() e print() em profundidade |
| 07 | [Variáveis e Tipos Básicos](07-variaveis-tipos.md) | O que são variáveis e os tipos de dados int, float, str e bool |
| 08 | [Conversão de Tipos](08-conversao-tipos.md) | Como converter valores entre diferentes tipos de dados |
| 09 | [Manipulação de Strings](09-manipulacao-strings.md) | Formatação, fatiamento e métodos de texto |
| 10 | [Indentação e Escopo](10-indentacao-escopo.md) | Por que a indentação é fundamental em Python |
| 11 | [Operadores](11-operadores.md) | Operadores matemáticos, de comparação e lógicos |
| 12 | [Condicionais](12-condicionais.md) | Tomando decisões com if, elif e else |
| 13 | [Seletores (match/case)](13-seletores-match-case.md) | Comparando valores com múltiplos padrões |
| 14 | [Controles de Repetição](14-controles-repeticao.md) | Automatizando tarefas com for e while |
| 15 | [Funções](15-funcoes.md) | Organizando código em blocos reutilizáveis |
| 16 | [Exercícios de Lógica](16-exercicios-logica.md) | Treino intensivo de raciocínio lógico |
| 17 | [Debugging](17-debugging.md) | Identificando e corrigindo erros nos programas |
| 18 | [Tratamento de Erros](18-tratamento-erros.md) | Lidando com situações inesperadas (try/except) |
| 19 | [Estruturas de Dados](19-estruturas-dados.md) | Listas, tuplas, dicionários e conjuntos |
| 20 | [Leitura e Escrita de Arquivos](20-leitura-escrita-arquivos.md) | Salvando e lendo dados em arquivos .txt e .csv |
| 21 | [Manipulação de JSON](21-manipulacao-json.md) | Trabalhando com o formato JSON |
| 22 | [Classes e Objetos](22-classes-objetos.md) | Introdução à orientação a objetos |
| 23 | [Exercícios Integradores](23-exercicios-integradores.md) | Praticando todos os conceitos juntos |
| 24 | [Módulos e Imports](24-modulos-imports.md) | Importando bibliotecas e organizando código |
| 25 | [Estruturação de Projetos](25-estruturacao-projetos.md) | Organizando pastas e arquivos de um projeto |
| 26 | [pip e Dependências](26-pip-dependencias.md) | Instalando e gerenciando bibliotecas externas |
| 27 | [Boas Práticas](27-boas-praticas.md) | Escrevendo código limpo e profissional (PEP 8) |
| 28 | [Modelagem de Dados](28-modelagem-dados.md) | Planejando a estrutura dos dados antes de programar |
| 29 | [Projeto CRUD — Memória](29-crud-memoria.md) | Cadastro de produtos com listas e dicionários |
| 30 | [Projeto CRUD — SQLite](30-crud-sqlite.md) | Evoluindo o CRUD com banco de dados |
| 31 | [Projeto CRUD — FastAPI](31-crud-fastapi.md) | Evoluindo o CRUD com interface web HTTP |
| 32 | [Projeto CRUD — Swagger](32-crud-swagger.md) | Documentando a API do projeto |

---

## Dependências entre Módulos

Os módulos deste curso estão conectados entre si. Cada grupo de módulos constrói uma base que será usada pelos módulos seguintes. Entender essas conexões ajuda você a perceber por que a ordem de estudo é importante.

### Grupo 1 — Fundamentos Teóricos (Módulos 01 a 05)

Estes módulos apresentam os conceitos iniciais: o que é programação, como preparar o computador e como executar programas. Eles são a **fundação da casa** — sem eles, nada do que vem depois faz sentido.

- **Módulo 01** (Introdução) → base para tudo
- **Módulo 02** (Scripts/Compilados/VM) → entender onde o Python se encaixa
- **Módulo 03** (Preparação do Ambiente) → sem isso, você não consegue programar
- **Módulo 04** (Execução/Permissões/Pastas) → sem isso, você não consegue rodar seus programas
- **Módulo 05** (História do Python) → contexto e motivação

### Grupo 2 — Fundamentos da Linguagem (Módulos 06 a 11)

Aqui você aprende os blocos básicos da linguagem Python. É como aprender as letras e palavras antes de escrever frases.

- **Módulo 06** (Entrada e Saída) → como o programa conversa com você
- **Módulo 07** (Variáveis e Tipos) → depende do módulo 06 (usa input/print)
- **Módulo 08** (Conversão de Tipos) → depende do módulo 07 (precisa entender tipos)
- **Módulo 09** (Strings) → depende dos módulos 07 e 08 (manipula o tipo str)
- **Módulo 10** (Indentação) → prepara para condicionais, loops e funções
- **Módulo 11** (Operadores) → depende do módulo 07 (opera sobre variáveis)

### Grupo 3 — Controle de Fluxo (Módulos 12 a 16)

Aqui seus programas começam a tomar decisões e repetir ações. É como aprender a escrever frases completas depois de conhecer as palavras.

- **Módulo 12** (Condicionais) → depende dos módulos 10 e 11 (indentação + operadores)
- **Módulo 13** (match/case) → depende do módulo 12 (alternativa a if/elif/else)
- **Módulo 14** (Loops) → depende dos módulos 10, 11 e 12 (indentação + operadores + condições)
- **Módulo 15** (Funções) → depende de todos os anteriores (usa tudo que foi aprendido)
- **Módulo 16** (Exercícios de Lógica) → consolida módulos 12 a 15

### Grupo 4 — Tópicos Intermediários (Módulos 17 a 22)

Aqui você aprende a lidar com erros, organizar dados e trabalhar com arquivos. É como aprender a organizar sua cozinha depois de saber cozinhar o básico.

- **Módulo 17** (Debugging) → depende de todos os anteriores (precisa ter código para depurar)
- **Módulo 18** (Tratamento de Erros) → depende do módulo 17 (entender erros antes de tratá-los)
- **Módulo 19** (Estruturas de Dados) → depende dos módulos 07, 14 e 15 (variáveis + loops + funções)
- **Módulo 20** (Arquivos) → depende do módulo 19 (trabalha com dados estruturados)
- **Módulo 21** (JSON) → depende dos módulos 19 e 20 (dicionários + arquivos)
- **Módulo 22** (Classes e Objetos) → depende dos módulos 07, 15 e 19 (variáveis + funções + estruturas)

### Grupo 5 — Organização e Boas Práticas (Módulos 23 a 28)

Aqui você aprende a organizar projetos como um profissional. É como aprender a manter a cozinha limpa e organizada enquanto cozinha.

- **Módulo 23** (Exercícios Integradores) → consolida módulos 06 a 22
- **Módulo 24** (Módulos e Imports) → depende do módulo 15 (funções) e 22 (classes)
- **Módulo 25** (Estruturação de Projetos) → depende do módulo 24 (imports)
- **Módulo 26** (pip e Dependências) → depende do módulo 25 (estrutura de projetos)
- **Módulo 27** (Boas Práticas) → depende de todos os anteriores
- **Módulo 28** (Modelagem de Dados) → prepara para o projeto CRUD

### Grupo 6 — Projeto CRUD (Módulos 29 a 32)

O grande projeto final! Aqui você constrói um sistema completo de cadastro de produtos que evolui em 4 fases. É como preparar um grande banquete depois de ter aprendido todas as técnicas de cozinha.

- **Módulo 29** (CRUD Memória) → depende dos módulos 15, 19 e 28 (funções + estruturas + modelagem)
- **Módulo 30** (CRUD SQLite) → depende do módulo 29 (evolui o projeto)
- **Módulo 31** (CRUD FastAPI) → depende dos módulos 26 e 30 (pip + CRUD SQLite)
- **Módulo 32** (CRUD Swagger) → depende do módulo 31 (evolui a API)

### Por que não pular módulos?

Cada módulo foi pensado como um degrau de uma escada. Pular um degrau pode fazer você tropeçar nos seguintes. Mesmo que um módulo pareça simples, ele pode conter detalhes importantes que serão usados mais adiante. Tenha paciência e siga a ordem — seu "eu do futuro" vai agradecer.

---

## Quando Avançar para o Próximo Módulo?

Uma dúvida muito comum é: "como sei que estou pronto para passar para o próximo módulo?" Aqui estão alguns critérios que podem ajudar:

 **Você está pronto para avançar quando:**

- Consegue explicar, com suas próprias palavras, os conceitos principais do módulo
- Consegue resolver a maioria dos exercícios de fixação **sem consultar os exemplos** do módulo
- Consegue executar seus programas no terminal sem precisar reler as instruções de execução
- Sente que entendeu a lógica por trás dos exemplos, não apenas copiou o código

 **Considere revisar o módulo quando:**

- Precisa consultar os exemplos para resolver todos os exercícios
- Não consegue explicar o que um trecho de código faz sem ler os comentários
- Sente que está "decorando" em vez de "entendendo"

**Lembre-se:** Não existe vergonha em reler um módulo ou refazer exercícios. Programadores profissionais revisam conceitos o tempo todo. O importante é que você se sinta confortável com o conteúdo antes de seguir em frente.

Aprender a programar é uma jornada, não uma corrida. Cada pessoa tem seu próprio ritmo, e isso é perfeitamente normal. O mais importante é não desistir — cada linha de código que você escreve é um passo a mais na sua formação como desenvolvedor.

---

## Glossário

Ao longo dos módulos, você encontrará diversos termos técnicos. Para facilitar seus estudos, criamos um **glossário completo** com explicações simples e acessíveis de todos os termos utilizados no curso.

  **[Acesse o Glossário do Curso](00-glossario.md)**

O glossário está dividido em arquivos para facilitar a consulta:
- [Termos A-D](00-glossario-a-d.md) — Algoritmo, API, Bool, Classe, CRUD, Dicionário...
- [Termos E-I](00-glossario-e-i.md) — Escopo, Expressão, FastAPI, Função, HTTP, Indentação...
- [Termos J-P](00-glossario-j-p.md) — JSON, Lista, Loop, Módulo, Objeto, PEP 8, Python...
- [Termos Q-Z](00-glossario-q-z.md) — Range, Return, Script, SQLite, String, Tupla, Variável...
- [Comandos e Funções Python](00-glossario-comandos.md) — Referência rápida de funções, operadores, métodos e comandos de terminal

**Quando consultar o glossário?**

- Sempre que encontrar uma palavra ou termo que você não conhece
- Quando quiser relembrar o significado de um conceito já estudado
- Quando quiser encontrar links para fontes externas de aprofundamento

O glossário é como um dicionário do curso — mantenha-o sempre à mão. Não há problema nenhum em consultá-lo quantas vezes precisar. Até programadores experientes consultam referências e documentações todos os dias.
