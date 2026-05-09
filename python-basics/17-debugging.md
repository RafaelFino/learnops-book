# 17 — Debugging Básico: Identificando e Corrigindo Erros

[<- Anterior: Exercícios de Lógica](16-exercícios-lógica.md) | [Glossário](00-glossário.md) | [Próximo: Tratamento de Erros ->](18-tratamento-erros.md)

---

## Introdução

Errar faz parte da programação. Não importa quanta experiência você tenha — todo programador encontra erros no código todos os dias. A diferença entre um iniciante e um programador experiente não e a quantidade de erros que cometem, mas a habilidade de **encontrar e corrigir** esses erros rapidamente.

O processo de encontrar e corrigir erros se chama **debugging** (depuracao). Neste módulo, você vai aprender a ler mensagens de erro do Python, usar `print()` como ferramenta de investigacao e conhecer o debugger do VSCode.

Pense no debugging como ser um detetive: o erro e o crime, a mensagem de erro e a pista, e você e o investigador que precisa descobrir o que aconteceu e onde.

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-17/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-17`
4. Execute: `python3 nome_do_arquivo.py`

---

## Tipos de Erros Mais Comuns

O Python mostra mensagens de erro detalhadas quando algo da errado. Aprender a ler essas mensagens e a habilidade mais importante deste módulo.

### SyntaxError — Erro de Sintaxe

Acontece quando você escreve algo que o Python não consegue entender — como um erro de gramatica em um texto. O Python nem consegue executar o programa.

```python
# CODIGO COM ERRO — falta fechar o parentese
print("Ola mundo"
```

**Mensagem de erro:**
```
  File "exemplo.py", line 2
    print("Ola mundo"
                     ^
SyntaxError: unexpected EOF while parsing
```

**Como ler a mensagem:**
- `File "exemplo.py", line 2` — o erro esta no arquivo "exemplo.py", na linha 2
- O `^` aponta para onde o Python percebeu o problema
- `SyntaxError` — tipo do erro (erro de sintaxe)
- `unexpected EOF while parsing` — "fim inesperado do arquivo durante a análise" — falta algo (neste caso, o parentese de fechamento)

**Correcao:**
```python
# CORRETO — parentese fechado
print("Ola mundo")
```

### NameError — Variável Não Encontrada

Acontece quando você usa um nome que o Python não reconhece — geralmente uma variável que não foi criada ou que foi escrita com erro de digitacao.

```python
# CODIGO COM ERRO — variavel "nome" nao existe (o correto seria "name")
name = "Maria"
print(nome)
```

**Mensagem de erro:**
```
Traceback (most recent call last):
  File "exemplo.py", line 3, in <module>
    print(nome)
NameError: name 'nome' is not defined
```

**Como ler:**
- `line 3` — o erro esta na linha 3
- `print(nome)` — esta e a linha que causou o erro
- `NameError: name 'nome' is not defined` — "Erro de Nome: o nome 'nome' não esta definido" — o Python não encontrou nenhuma variável chamada `nome`

**Correcao:** A variável se chama `name`, não `nome`. Corrija a digitacao.

### TypeError — Tipo Errado

Acontece quando você tenta fazer uma operação com tipos incompativeis.

```python
# CODIGO COM ERRO — tentando somar texto com numero
age = "25"
result = age + 5
```

**Mensagem de erro:**
```
TypeError: can only concatenate str (not "int") to str
```

**Traducao:** "Erro de Tipo: so consigo juntar texto com texto, não texto com número inteiro."

**Correcao:** Converta o texto para número: `age = int("25")`

### ValueError — Valor Inválido

Acontece quando você passa um valor que não faz sentido para uma função.

```python
# CODIGO COM ERRO — tentando converter texto para numero
number = int("abc")
```

**Mensagem de erro:**
```
ValueError: invalid literal for int() with base 10: 'abc'
```

**Traducao:** "Erro de Valor: 'abc' não e um valor válido para converter em número inteiro."

### IndexError — Índice Fora do Alcance

Acontece quando você tenta acessar uma posição que não existe em uma lista ou string.

```python
# CODIGO COM ERRO — a lista tem 3 itens (posicoes 0, 1, 2)
fruits = ["maca", "banana", "laranja"]
print(fruits[5])  # posicao 5 nao existe!
```

**Mensagem de erro:**
```
IndexError: list index out of range
```

**Traducao:** "Erro de Índice: o índice da lista esta fora do alcance."

### ZeroDivisionError — Divisao por Zero

Acontece quando você tenta dividir por zero.

```python
# CODIGO COM ERRO — divisao por zero
result = 10 / 0
```

**Mensagem de erro:**
```
ZeroDivisionError: division by zero
```

**Traducao:** "Erro de Divisao por Zero: divisao por zero." Dividir por zero não faz sentido matematicamente.

---

## Tabela Resumo dos Erros

| Erro | Significado | Causa Comum |
|------|-------------|-------------|
| `SyntaxError` | Erro de escrita | Parentese, aspas ou dois-pontos faltando |
| `NameError` | Nome não encontrado | Variável não criada ou digitada errado |
| `TypeError` | Tipo incompativel | Somar texto com número, por exemplo |
| `ValueError` | Valor inválido | Converter "abc" para int() |
| `IndexError` | Posição inexistente | Acessar posição que não existe na lista |
| `ZeroDivisionError` | Divisao por zero | Dividir qualquer número por 0 |
| `IndentationError` | Indentacao errada | Espacos incorretos (veja módulo 10) |

---

## Técnica 1: Usando print() para Depuracao

A forma mais simples de investigar um erro e adicionar `print()` no código para ver o que esta acontecendo em cada passo. E como colocar cameras de segurança em pontos estrategicos para observar o que acontece.

```python
# Programa com um bug — o resultado esta errado
# Vamos usar print() para investigar

# "price" = preco, "quantity" = quantidade
price = float(input("Preco: "))
quantity = int(input("Quantidade: "))

# Adicionamos prints para ver os valores
print(f"DEBUG - price: {price}, tipo: {type(price)}")
print(f"DEBUG - quantity: {quantity}, tipo: {type(quantity)}")

# "discount" = desconto (10%)
discount = price * quantity * 0.10
print(f"DEBUG - discount: {discount}")

# "total" = total
total = price * quantity - discount
print(f"DEBUG - total: {total}")

print(f"Total a pagar: R$ {total}")
```

> **Dica:** Use o prefixo "DEBUG" nos prints de depuracao para diferencia-los dos prints normais. Depois de encontrar e corrigir o erro, remova os prints de debug.

---

## Técnica 2: O Debugger do VSCode

O VSCode tem uma ferramenta chamada **debugger** que permite executar o programa passo a passo, parando em pontos específicos para inspecionar o valor das variáveis.

### Como usar o debugger

**Passo 1 — Criar um breakpoint (ponto de parada)**

Clique na margem esquerda do editor (a area cinza a esquerda dos números de linha). Um circulo vermelho aparece — esse e o breakpoint. O programa vai parar nessa linha quando você executar com o debugger.

**Passo 2 — Iniciar o debugger**

Pressione `F5` ou va em Run > Start Debugging. Escolha "Python File" se perguntado.

**Passo 3 — Inspecionar variáveis**

Quando o programa parar no breakpoint, você pode:
- Ver o valor de todas as variáveis no painel "Variables" (a esquerda)
- Passar o mouse sobre uma variável no código para ver seu valor
- Usar os botoes de controle para avancar passo a passo:
  - **Step Over (F10)** — executa a linha atual e vai para a proxima
  - **Step Into (F11)** — entra dentro de uma função
  - **Continue (F5)** — continua ate o próximo breakpoint
  - **Stop** — para o debugger

> **Nota:** O debugger e uma ferramenta poderosa, mas para iniciantes, o `print()` de depuracao e mais simples e direto. Use o debugger quando o print não for suficiente ou quando quiser entender o fluxo do programa passo a passo.

---

## Dicas Gerais de Debugging

1. **Leia a mensagem de erro** — ela quase sempre diz o que aconteceu e onde
2. **Olhe o número da linha** — va direto para a linha indicada no erro
3. **Verifique a linha anterior** — as vezes o erro real esta na linha de cima (ex: parentese não fechado)
4. **Use print() para ver valores** — quando não entender por que algo esta errado, imprima os valores das variáveis
5. **Compare com exemplos que funcionam** — se seu código não funciona, compare com um exemplo similar que funciona
6. **Pesquise a mensagem de erro** — copie a mensagem e pesquise na internet. Alguem provavelmente ja teve o mesmo problema
7. **Faca uma pausa** — se estiver travado ha muito tempo, descanse e volte depois. Muitas vezes a solução aparece quando você para de forcar

---

## Para Saber Mais

- [W3Schools — Python Try Except](https://www.w3schools.com/python/python_try_except.asp) — _Erros e excecoes_
- [W3Schools — Python Syntax](https://www.w3schools.com/python/python_syntax.asp) — _Sintaxe correta do Python_
- [Documentação Python — Erros e Exceções](https://docs.python.org/pt-br/3/tutorial/errors.html) — _Referencia oficial_

---

## Perguntas Frequentes (FAQ)

**P: O que e debugging?**
R: E o processo de encontrar e corrigir erros (bugs) no código. O nome vem de "bug" (inseto em ingles) — conta a lenda que um dos primeiros erros de computador foi causado por um inseto real preso na máquina.

**P: Por que meu programa da erro?**
R: Erros acontecem por diversos motivos: digitacao errada, lógica incorreta, tipos incompativeis, valores inesperados. A mensagem de erro do Python quase sempre indica o motivo e a linha onde ocorreu.

**P: Como leio uma mensagem de erro?**
R: Olhe de baixo para cima. A ultima linha diz o tipo de erro e a descricao. As linhas acima mostram o caminho ate o erro (arquivo, linha, código). O número da linha e a informação mais importante.

**P: O que e "Traceback"?**
R: E o rastro que o Python mostra quando ocorre um erro. Mostra o caminho que o programa percorreu ate chegar ao ponto do erro. Leia de baixo para cima — a ultima linha e o erro, as anteriores sao o caminho.

**P: O que e um "bug"?**
R: E um erro no programa que faz ele se comportar de forma diferente do esperado. Pode ser um erro de sintaxe (o programa não roda) ou um erro de lógica (o programa roda mas da resultado errado).

**P: Qual a diferença entre erro de sintaxe e erro de lógica?**
R: Erro de sintaxe impede o programa de rodar — o Python avisa imediatamente. Erro de lógica permite que o programa rode, mas o resultado esta errado. Erros de lógica sao mais dificeis de encontrar porque não geram mensagem de erro.

**P: O que fazer quando o erro esta em uma linha diferente da indicada?**
R: Isso acontece com frequência. O Python detecta o erro na linha indicada, mas a causa real pode estar na linha anterior (ex: parentese não fechado na linha de cima). Sempre verifique a linha indicada E a anterior.

**P: O que e um breakpoint?**
R: E um ponto de parada que você coloca no código. Quando o debugger chega nessa linha, ele para e permite que você inspecione o estado do programa (valores das variáveis, fluxo de execução).

**P: Preciso usar o debugger do VSCode?**
R: Não e obrigatório. O `print()` de depuracao resolve a maioria dos problemas para iniciantes. O debugger e uma ferramenta mais avancada que se torna útil conforme seus programas ficam mais complexos.

**P: O que e "Step Over" no debugger?**
R: Executa a linha atual e vai para a proxima, sem entrar dentro de funções. E como pular um passo da receita e ir para o próximo.

**P: O que e "Step Into" no debugger?**
R: Entra dentro de uma função para ver o que acontece la dentro, linha por linha. E como abrir uma caixa para ver o que tem dentro.

**P: Posso ter erros que não geram mensagem?**
R: Sim! Erros de lógica não geram mensagem — o programa roda normalmente mas produz resultado errado. Esses sao os mais dificeis de encontrar. Use `print()` para verificar valores intermediarios.

**P: O que e `Ctrl + C` no terminal?**
R: Interrompe o programa que esta rodando. Útil quando o programa trava em um loop infinito ou quando você quer parar a execução manualmente.

**P: O que significa "EOF" nas mensagens de erro?**
R: EOF = End Of File = Fim do Arquivo. Geralmente aparece quando o Python chegou ao final do arquivo sem encontrar algo que esperava (como um parentese de fechamento).

**P: Posso ignorar mensagens de erro?**
R: Não! Mensagens de erro sao informações valiosas. Ignorar um erro e como ignorar uma luz de alerta no painel do carro — o problema so vai piorar.

**P: O que fazer se não entendo a mensagem de erro?**
R: Copie a mensagem de erro e pesquise na internet. Sites como Stack Overflow tem respostas para praticamente qualquer erro do Python. Você também pode perguntar ao professor.

**P: Devo remover os prints de debug depois?**
R: Sim! Prints de depuracao sao temporarios — servem apenas para investigar o problema. Depois de corrigir o erro, remova-os para manter o código limpo.

**P: E normal gastar muito tempo debugando?**
R: Sim! Programadores profissionais gastam uma parte significativa do tempo debugando. Com experiência, você fica mais rápido em identificar e corrigir erros, mas debugging sempre fara parte do trabalho.

**P: O que e um "warning" (aviso)?**
R: E uma mensagem que o Python mostra para alertar sobre algo que pode ser um problema, mas que não impede a execução. Warnings sao menos graves que erros, mas não devem ser ignorados.

**P: Debugging e frustrante. Como lidar?**
R: E completamente normal sentir frustracao. Faca pausas regulares, respire fundo e lembre-se: cada bug que você resolve te torna um programador melhor. A satisfacao de encontrar e corrigir um erro e uma das melhores sensacoes da programação.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado:

**[Acessar Exercícios do Módulo 17](17-debugging-exercícios.md)**

---

[<- Anterior: Exercícios de Lógica](16-exercícios-lógica.md) | [Glossário](00-glossário.md) | [Próximo: Tratamento de Erros ->](18-tratamento-erros.md)
