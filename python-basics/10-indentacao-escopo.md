# 10 — Indentacao e Escopo de Blocos de Código

[<- Anterior: Manipulação de Strings](09-manipulacao-strings.md) | [Glossário](00-glossario.md) | [Próximo: Operadores ->](11-operadores.md)

---

## Introdução

Este módulo trata de um assunto que pode parecer simples, mas e absolutamente fundamental em Python: a **indentacao**. Em muitas linguagens de programação, a indentacao e apenas uma questao estetica — o código funciona com ou sem ela. Em Python, a indentacao **faz parte da linguagem**. Se você indentar errado, o programa não funciona.

Pense na indentacao como a organização de itens dentro de caixas. Quando você coloca itens dentro de uma caixa, eles ficam "recuados" em relação a caixa. Em Python, linhas de código que pertencem a um bloco (como o corpo de um `if`, `for` ou função) precisam estar recuadas para dentro, mostrando que fazem parte daquele bloco.

Este módulo prepara você para os proximos módulos (condicionais, loops e funções), que dependem diretamente da indentacao para funcionar.

> **Dica:** Consulte o [Glossário](00-glossario.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve com extensão `.py` na pasta `~/meus-projetos/python-curso/modulo-10/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-10`
4. Execute: `python3 nome_do_arquivo.py`

---

## O que e Indentacao?

[Indentacao](00-glossario-e-i.md#indentacao) e o espacamento a esquerda de uma linha de código. Em Python, esse espacamento não e apenas visual — ele define a **estrutura** do programa.

### Python vs outras linguagens

Em linguagens como Java, C ou JavaScript, os blocos de código sao delimitados por chaves `{}`:

```
// Exemplo em Java (NAO e Python!)
if (age >= 18) {
    System.out.println("Maior de idade");
    System.out.println("Pode votar");
}
```

Em Python, não existem chaves. Os blocos sao definidos pela **indentacao**:

```python
# Exemplo em Python
# As linhas indentadas (recuadas) pertencem ao bloco do if
# "age" = idade
age = 20

if age >= 18:
    # Estas duas linhas estao indentadas — pertencem ao bloco do if
    # Elas so executam se a condicao (age >= 18) for verdadeira
    print("Maior de idade")
    print("Pode votar")

# Esta linha NAO esta indentada — nao pertence ao bloco do if
# Ela executa sempre, independente da condicao
print("Fim do programa")
```

**Saida esperada:**
```
Maior de idade
Pode votar
Fim do programa
```

> **Nota:** Não se preocupe em entender o `if` completamente agora — vamos aprofundar no módulo 12. O foco aqui e entender como a indentacao define o que esta "dentro" e o que esta "fora" do bloco.

---

## Como Indentar Corretamente

### A regra de ouro: 4 espacos

O padrão do Python (definido pelo PEP 8) e usar **4 espacos** para cada nível de indentacao. No VSCode, quando você pressiona a tecla `Tab`, ele automaticamente insere 4 espacos.

```python
# Nivel 0 — sem indentacao (linha principal)
print("Nivel 0")

# Nivel 1 — 4 espacos de indentacao (dentro de um bloco)
if True:
    print("Nivel 1 — dentro do if")

    # Nivel 2 — 8 espacos (bloco dentro de bloco)
    if True:
        print("Nivel 2 — dentro do if interno")
```

**Saida esperada:**
```
Nivel 0
Nivel 1 — dentro do if
Nivel 2 — dentro do if interno
```

### Visualizando a indentacao

Imagine a indentacao como caixas dentro de caixas:

```
Programa (nivel 0)
|
|-- if condicao:
|   |
|   |-- codigo dentro do if (nivel 1)
|   |-- mais codigo dentro do if (nivel 1)
|   |
|   |-- if outra_condicao:
|   |   |
|   |   |-- codigo dentro do if interno (nivel 2)
|   |
|-- codigo fora do if (nivel 0)
```

Tudo que esta "dentro" de um bloco precisa estar recuado um nível a mais. Quando o recuo volta ao nível anterior, o bloco terminou.

---

## Tabs vs Espacos

Existem duas formas de criar indentacao: usando a tecla **Tab** ou usando **espacos**. O Python aceita ambas, mas **nunca misture as duas no mesmo arquivo**. Misturar tabs e espacos causa erros.

A recomendacao oficial (PEP 8) e usar **espacos** — especificamente, 4 espacos por nível. O VSCode, por padrão, converte a tecla Tab em 4 espacos automaticamente, então você pode usar a tecla Tab sem preocupacao.

Para verificar se o VSCode esta configurado corretamente, olhe no canto inferior direito da tela. Deve aparecer "Spaces: 4". Se aparecer "Tab Size: 4", clique e mude para "Indent Using Spaces".

---

## Erros Comuns de Indentacao

### IndentationError: unexpected indent

Esse erro aparece quando uma linha esta indentada sem motivo:

```python
# ERRADO — a segunda linha esta indentada sem necessidade
print("Ola")
    print("Mundo")  # IndentationError!
```

**Mensagem de erro:**
```
IndentationError: unexpected indent
```

Traduzindo: "Erro de Indentacao: indentacao inesperada". A segunda linha esta recuada, mas não ha nenhum bloco (if, for, função) que justifique essa indentacao.

**Correcao:**
```python
# CORRETO — ambas as linhas no mesmo nivel
print("Ola")
print("Mundo")
```

### IndentationError: expected an indented block

Esse erro aparece quando você cria um bloco (if, for, função) mas não coloca nada indentado dentro dele:

```python
# ERRADO — o if espera um bloco indentado, mas nao tem
age = 20
if age >= 18:
print("Maior de idade")  # IndentationError!
```

**Mensagem de erro:**
```
IndentationError: expected an indented block
```

Traduzindo: "Erro de Indentacao: esperava um bloco indentado". Depois do `if age >= 18:`, o Python espera pelo menos uma linha indentada.

**Correcao:**
```python
# CORRETO — a linha dentro do if esta indentada com 4 espacos
age = 20
if age >= 18:
    print("Maior de idade")
```

### TabError: inconsistent use of tabs and spaces

Esse erro aparece quando você mistura tabs e espacos no mesmo arquivo:

```python
# ERRADO — mistura de tabs e espacos (invisivel a olho nu!)
if True:
	print("Com tab")      # esta linha usa tab
    print("Com espacos")  # esta linha usa espacos — TabError!
```

**Mensagem de erro:**
```
TabError: inconsistent use of tabs and spaces in indentation
```

Traduzindo: "Erro de Tab: uso inconsistente de tabs e espacos na indentacao".

**Correcao:** Use apenas espacos (4 espacos por nível). No VSCode, selecione todo o código (`Ctrl + A`) e use o comando "Convert Indentation to Spaces" na paleta de comandos (`Ctrl + Shift + P`).

---

## Conexão com os Proximos Módulos

A indentacao e essencial para tudo que vem a seguir no curso:

- **Condicionais (módulo 12):** O código dentro de `if`, `elif` e `else` precisa estar indentado
- **Loops (módulo 14):** O código dentro de `for` e `while` precisa estar indentado
- **Funções (módulo 15):** O corpo de uma função precisa estar indentado
- **Classes (módulo 22):** Métodos e atributos dentro de uma classe precisam estar indentados

Dominar a indentacao agora vai evitar muita dor de cabeca nos proximos módulos. Se você entendeu que "linhas recuadas pertencem ao bloco acima", você ja tem o conceito principal.

---

## Resumo

| Conceito | Descricao |
|----------|-----------|
| Indentacao | Espacamento a esquerda que define blocos de código |
| Padrão PEP 8 | 4 espacos por nível de indentacao |
| Bloco de código | Conjunto de linhas indentadas que pertencem a uma estrutura (if, for, def) |
| IndentationError | Erro causado por indentacao incorreta |
| TabError | Erro causado por mistura de tabs e espacos |

---

## Para Saber Mais

- [W3Schools — Python Indentation](https://www.w3schools.com/python/python_syntax.asp) — _Indentacao e sintaxe do Python_
- [W3Schools — Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — _Condicionais (usa indentacao)_
- [PEP 8 — Indentation](https://peps.python.org/pep-0008/#indentation) — _Guia oficial de indentacao_
- [Documentação Python — Estruturas de Controle](https://docs.python.org/pt-br/3/tutorial/controlflow.html) — _Referencia oficial_

---

## Perguntas Frequentes (FAQ)

**P: Por que Python usa indentacao em vez de chaves como outras linguagens?**
R: O criador do Python, Guido van Rossum, acreditava que a indentacao torna o código mais legivel. Em vez de depender de chaves que podem ser esquecidas, o Python forca você a organizar o código visualmente. Com o tempo, a maioria dos programadores concorda que isso torna o código mais limpo.

**P: Quantos espacos devo usar?**
R: O padrão e 4 espacos por nível de indentacao, conforme o PEP 8. Tecnicamente, qualquer número funciona (2, 3, 4, 8), desde que seja consistente. Mas use 4 — e o que todo mundo usa e o que o VSCode configura por padrão.

**P: Posso usar Tab em vez de espacos?**
R: O Python aceita Tab, mas a recomendacao oficial e usar espacos. O VSCode converte Tab em 4 espacos automaticamente, então você pode pressionar Tab sem preocupacao. O importante e nunca misturar tabs e espacos no mesmo arquivo.

**P: Como sei se estou usando tabs ou espacos?**
R: No VSCode, olhe no canto inferior direito da tela. Deve aparecer "Spaces: 4". Você também pode ativar a opcao "Render Whitespace" nas configuracoes para ver os espacos como pontinhos.

**P: O que e um "bloco de código"?**
R: E um conjunto de linhas que pertencem a uma mesma estrutura. Por exemplo, todas as linhas indentadas depois de um `if:` formam o bloco do if. Quando a indentacao volta ao nível anterior, o bloco terminou.

**P: O que significa os dois pontos (:) no final de uma linha?**
R: Os dois pontos indicam que um novo bloco de código vai começar na proxima linha. Você vai ver isso em `if:`, `for:`, `while:`, `def:` e `class:`. Depois dos dois pontos, a proxima linha precisa estar indentada.

**P: Posso ter blocos dentro de blocos?**
R: Sim! Isso se chama "aninhamento". Cada nível de bloco adiciona mais 4 espacos de indentacao. Um if dentro de outro if tera 8 espacos de indentacao (4 + 4).

**P: O que acontece se eu indentar uma linha sem motivo?**
R: O Python mostra `IndentationError: unexpected indent`. Toda indentacao precisa ter um motivo — uma estrutura (if, for, def) que justifique o bloco.

**P: O que e `pass`?**
R: E uma palavra-chave que não faz nada. E usada como placeholder quando você precisa de um bloco indentado mas ainda não escreveu o código. Exemplo: `if True: pass` — cria um bloco vazio sem erro.

**P: A indentacao afeta a velocidade do programa?**
R: Não. A indentacao e processada apenas quando o Python le o código. Depois disso, não tem nenhum impacto na velocidade de execução.

**P: E possível ter indentacao errada que não gera erro mas muda o comportamento?**
R: Sim! Se você indentar uma linha no nível errado, ela pode pertencer a um bloco diferente do que você pretendia. O programa roda sem erro, mas faz algo diferente do esperado. Por isso, preste muita atenção na indentacao.

**P: O que e "escopo"?**
R: Escopo e a regiao do código onde uma variável existe e pode ser acessada. Variáveis criadas dentro de um bloco (como dentro de uma função) podem não ser acessiveis fora dele. Vamos aprofundar isso no módulo 15 (Funções).

**P: Como o VSCode me ajuda com indentacao?**
R: O VSCode indenta automaticamente quando você pressiona Enter depois de uma linha com `:`. Ele também mostra linhas verticais que conectam os níveis de indentacao, facilitando a visualizacao dos blocos.

**P: O que fazer se meu código tem erros de indentacao e eu não consigo encontrar?**
R: No VSCode, ative "Render Whitespace" para ver espacos e tabs. Selecione todo o código (Ctrl+A) e use "Convert Indentation to Spaces" na paleta de comandos (Ctrl+Shift+P). Isso padroniza toda a indentacao.

**P: Linhas em branco precisam de indentacao?**
R: Não. Linhas em branco podem estar completamente vazias. Elas sao ignoradas pelo Python e servem apenas para separar visualmente partes do código.

**P: Comentários precisam de indentacao?**
R: Sim, se estiverem dentro de um bloco. Um comentário dentro de um if deve estar indentado no mesmo nível que o código do bloco. Isso mantem a organização visual.

**P: O que e PEP 8?**
R: E o guia de estilo oficial do Python que define convencoes de formatacao, incluindo indentacao (4 espacos), comprimento de linhas (máximo 79 caracteres) e nomenclatura. Vamos estudar o PEP 8 em detalhes no módulo 27.

**P: Posso ter um bloco com apenas uma linha?**
R: Sim! Um bloco pode ter quantas linhas você precisar — inclusive apenas uma. `if True: print("ola")` também funciona em uma única linha, mas para legibilidade, prefira colocar o bloco na linha seguinte com indentacao.

**P: Indentacao e a mesma coisa que "recuo" de texto?**
R: Exatamente! Indentar e recuar o texto para a direita. Em editores de texto comuns, você recua paragrafos. Em Python, você recua linhas de código para indicar que pertencem a um bloco.

**P: Vou errar muito com indentacao no inicio?**
R: Provavelmente sim, e isso e completamente normal. Erros de indentacao sao os mais comuns entre iniciantes. A boa noticia e que o Python sempre avisa quando algo esta errado, e com prática você vai indentar corretamente sem nem pensar. Tenha paciencia consigo mesmo.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

**[Acessar Exercícios do Módulo 10](10-indentacao-escopo-exercicios.md)**

---

[<- Anterior: Manipulação de Strings](09-manipulacao-strings.md) | [Glossário](00-glossario.md) | [Próximo: Operadores ->](11-operadores.md)
