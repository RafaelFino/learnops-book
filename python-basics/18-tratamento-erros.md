# 18 — Tratamento de Erros: try, except, finally

[<- Anterior: Debugging](17-debugging.md) | [Glossário](00-glossário.md) | [Próximo: Estruturas de Dados ->](19-estruturas-dados.md)

---

## Introdução

No módulo anterior, você aprendeu a identificar erros. Agora vai aprender a **tratar** esses erros para que seu programa não pare de funcionar quando algo inesperado acontece.

Imagine que você esta cozinhando e percebe que falta um ingrediente. Você tem duas opcoes: desistir da receita (o programa para com erro) ou improvisar com o que tem (tratar o erro e continuar). O tratamento de erros e a segunda opcao — você prepara o programa para lidar com situacoes inesperadas.

Em Python, usamos as estruturas `try`, `except`, `else` e `finally` para tratar erros em tempo de execução (chamados de **exceções**).

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-18/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-18`
4. Execute: `python3 nome_do_arquivo.py`

---

## Erros de Sintaxe vs Exceções

Existem dois tipos de erros em Python:

- **Erros de sintaxe** (SyntaxError): o Python detecta antes de executar. Sao erros de escrita — como esquecer um parentese. Não podem ser tratados com try/except.

- **Exceções** (erros em tempo de execução): acontecem durante a execução do programa. Sao situacoes inesperadas — como o usuario digitar texto quando o programa espera um número. Podem ser tratados com try/except.

---

## A Estrutura try/except

A forma mais básica de tratar erros:

```python
# Sem tratamento — o programa para se o usuario digitar texto
# number = int(input("Digite um numero: "))  # ValueError se digitar "abc"

# Com tratamento — o programa nao para
try:
    # O bloco try contem o codigo que PODE gerar um erro
    # "number" = numero
    number = int(input("Digite um numero: "))
    print(f"Voce digitou: {number}")
except ValueError:
    # O bloco except executa APENAS se ocorrer o erro especificado
    # ValueError acontece quando a conversao falha
    print("Erro: voce nao digitou um numero valido!")

# O programa continua normalmente apos o try/except
print("Programa encerrado.")
```

**Se o usuario digitar "5":**
```
Digite um numero: 5
Voce digitou: 5
Programa encerrado.
```

**Se o usuario digitar "abc":**
```
Digite um numero: abc
Erro: voce nao digitou um numero valido!
Programa encerrado.
```

> **Nota:** O programa não para quando o erro acontece — ele executa o bloco `except` e continua normalmente. Sem o try/except, o programa pararia com uma mensagem de erro.

### Anatomia do try/except

```
try:
    codigo_que_pode_dar_erro    <-- tenta executar este codigo
except TipoDoErro:
    codigo_de_tratamento        <-- executa se o erro especificado ocorrer
```

---

## Tratando Diferentes Tipos de Erro

Você pode ter vários blocos `except` para tratar diferentes tipos de erro:

```python
# Tratando diferentes tipos de erro
try:
    # "numerator" = numerador, "denominator" = denominador
    numerator = int(input("Numerador: "))
    denominator = int(input("Denominador: "))
    # "result" = resultado
    result = numerator / denominator
    print(f"Resultado: {result}")
except ValueError:
    # Erro de conversao — o usuario nao digitou um numero
    print("Erro: digite apenas numeros!")
except ZeroDivisionError:
    # Erro de divisao por zero
    print("Erro: nao e possivel dividir por zero!")
```

---

## O Bloco else — Quando Não Ha Erro

O bloco `else` executa **apenas quando nenhum erro ocorreu** no bloco `try`:

```python
try:
    # "age" = idade
    age = int(input("Sua idade: "))
except ValueError:
    print("Erro: digite um numero inteiro!")
else:
    # Este bloco executa APENAS se nao houve erro no try
    # E um bom lugar para codigo que depende do sucesso do try
    print(f"Voce tem {age} anos.")
    if age >= 18:
        print("Voce e maior de idade.")
```

---

## O Bloco finally — Sempre Executa

O bloco `finally` executa **sempre**, independente de ter ocorrido erro ou não. E útil para ações de "limpeza" que precisam acontecer de qualquer forma:

```python
try:
    # "number" = numero
    number = int(input("Digite um numero: "))
    # "result" = resultado
    result = 100 / number
    print(f"Resultado: {result}")
except ValueError:
    print("Erro: digite um numero valido!")
except ZeroDivisionError:
    print("Erro: nao divida por zero!")
finally:
    # Este bloco SEMPRE executa, com ou sem erro
    # E como a etapa de "limpar a cozinha" — acontece independente
    # de a receita ter dado certo ou nao
    print("Operacao finalizada.")
```

**Se digitar "5":**
```
Resultado: 20.0
Operacao finalizada.
```

**Se digitar "0":**
```
Erro: nao divida por zero!
Operacao finalizada.
```

**Se digitar "abc":**
```
Erro: digite um numero valido!
Operacao finalizada.
```

---

## Estrutura Completa: try/except/else/finally

```python
try:
    # Codigo que pode gerar erro
    # "value" = valor
    value = int(input("Numero: "))
    result = 100 / value
except ValueError:
    # Executa se ValueError ocorrer
    print("Nao e um numero!")
except ZeroDivisionError:
    # Executa se ZeroDivisionError ocorrer
    print("Nao divida por zero!")
else:
    # Executa APENAS se nenhum erro ocorreu
    print(f"Resultado: {result}")
finally:
    # Executa SEMPRE (com ou sem erro)
    print("Fim da operacao.")
```

### Ordem de execução

| Situacao | try | except | else | finally |
|----------|-----|--------|------|---------|
| Sem erro | Executa | Pula | Executa | Executa |
| Com erro tratado | Para no erro | Executa | Pula | Executa |
| Com erro não tratado | Para no erro | Pula | Pula | Executa |

---

## Exemplo Prático: Entrada Segura de Dados

Um padrão muito útil e pedir dados ao usuario repetidamente ate que ele digite algo válido:

```python
# Funcao que pede um numero inteiro de forma segura
# "safe_int_input" = entrada segura de inteiro
# "message" = mensagem a exibir
def safe_int_input(message):
    while True:
        try:
            # Tentamos converter a entrada para int
            # "value" = valor
            value = int(input(message))
            # Se chegou aqui, a conversao deu certo — retornamos o valor
            return value
        except ValueError:
            # Se deu erro, avisamos e o while repete (pede novamente)
            print("Valor invalido! Digite um numero inteiro.")

# Usando a funcao — o programa so continua quando o usuario digitar um numero valido
# "age" = idade
age = safe_int_input("Sua idade: ")
print(f"Idade registrada: {age}")
```

---

## Resumo

| Estrutura | Quando executa |
|-----------|---------------|
| `try:` | Sempre tenta executar |
| `except TipoErro:` | Quando o erro especificado ocorre no try |
| `else:` | Quando nenhum erro ocorre no try |
| `finally:` | Sempre, com ou sem erro |

---

## Para Saber Mais

- [W3Schools — Python Try Except](https://www.w3schools.com/python/python_try_except.asp) — _Tratamento de erros_
- [Documentação Python — Erros e Exceções](https://docs.python.org/pt-br/3/tutorial/errors.html) — _Referencia oficial_

---

## Perguntas Frequentes (FAQ)

**P: O que e uma exceção?**
R: E um erro que acontece durante a execução do programa (não durante a escrita). Quando uma exceção ocorre e não e tratada, o programa para. Com try/except, você pode capturar a exceção e decidir o que fazer.

**P: Qual a diferença entre erro de sintaxe e exceção?**
R: Erro de sintaxe e detectado antes da execução — o Python nem consegue rodar o programa. Exceção acontece durante a execução — o programa comeca a rodar e para quando encontra o problema. So exceções podem ser tratadas com try/except.

**P: Posso tratar qualquer tipo de erro com try/except?**
R: Quase todos os erros de execução (exceções) podem ser tratados. Erros de sintaxe (SyntaxError) não podem ser tratados com try/except porque o programa nem chega a executar.

**P: O que acontece se eu não especificar o tipo de erro no except?**
R: `except:` sem tipo captura QUALQUER exceção. Isso funciona, mas não e recomendado porque pode esconder erros que você não esperava. Sempre especifique o tipo de erro quando possível.

**P: Posso ter vários except?**
R: Sim! Você pode ter quantos blocos except precisar, cada um tratando um tipo diferente de erro. O Python verifica de cima para baixo e executa o primeiro que corresponder.

**P: O else e obrigatório?**
R: Não, e opcional. Use quando tiver código que so deve executar se o try foi bem-sucedido. Na prática, muitos programadores colocam esse código dentro do try mesmo.

**P: O finally e obrigatório?**
R: Não, e opcional. Use quando precisar garantir que algo aconteca independente de erros — como fechar um arquivo ou uma conexão com banco de dados.

**P: Posso ter try dentro de try?**
R: Sim, mas tente evitar. Try/except aninhados tornam o código confuso. Prefira tratar cada erro no nível adequado.

**P: O que e "capturar" uma exceção?**
R: E o ato de interceptar um erro com except antes que ele pare o programa. Quando você "captura" uma exceção, você decide o que fazer com ela em vez de deixar o programa parar.

**P: Posso acessar a mensagem de erro dentro do except?**
R: Sim! Use `except ValueError as e:` — a variável `e` contera a mensagem de erro. Exemplo: `print(f"Erro: {e}")`.

**P: O que e "raise"?**
R: E uma palavra-chave que permite você mesmo gerar uma exceção. Exemplo: `raise ValueError("Preco invalido")`. Útil para validação de dados. E um conceito mais avancado.

**P: Devo usar try/except em todo o código?**
R: Não! Use apenas onde erros sao esperados — como entrada de dados do usuario, operações com arquivos ou divisoes. Usar try/except em excesso torna o código difícil de ler.

**P: O que e "tratar" um erro?**
R: E decidir o que fazer quando o erro acontece, em vez de deixar o programa parar. Pode ser: exibir uma mensagem amigavel, pedir os dados novamente, usar um valor padrão, ou registrar o erro para análise.

**P: Posso tratar ValueError e TypeError no mesmo except?**
R: Sim! Use parenteses: `except (ValueError, TypeError):`. Isso captura ambos os tipos de erro no mesmo bloco.

**P: O que acontece se o erro não for do tipo especificado no except?**
R: O except não captura e o erro "sobe" — o programa para com a mensagem de erro normal. Por isso e importante especificar os tipos corretos.

**P: Posso usar try/except com loops?**
R: Sim, e muito comum! O padrão de "pedir dados ate serem validos" usa try/except dentro de while, como no exemplo de entrada segura deste módulo.

**P: O que e "Exception"?**
R: E a classe base de todas as exceções em Python. `except Exception:` captura quase todos os erros. E mais seguro que `except:` sozinho, mas ainda e genérico demais para a maioria dos casos.

**P: Posso criar meus proprios tipos de exceção?**
R: Sim, mas e um conceito avancado que esta fora do escopo deste curso. Por enquanto, use os tipos de exceção que o Python ja oferece.

**P: O que e "propagacao de exceção"?**
R: Quando um erro não e tratado em uma função, ele "sobe" para quem chamou a função. Se ninguem tratar, o programa para. E como uma bola quente sendo passada — se ninguem segurar, cai no chao.

**P: E normal ter dificuldade com try/except no inicio?**
R: Sim! Saber quando e onde usar try/except vem com experiência. Comece tratando os erros mais obvios (como entrada de dados) e va expandindo conforme se sentir confortavel. Com prática, tratar erros se torna natural.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado:

**[Acessar Exercícios do Módulo 18](18-tratamento-erros-exercícios.md)**

---

[<- Anterior: Debugging](17-debugging.md) | [Glossário](00-glossário.md) | [Próximo: Estruturas de Dados ->](19-estruturas-dados.md)
