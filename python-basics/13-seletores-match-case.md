# 13 — Seletores: match/case

[<- Anterior: Condicionais](12-condicionais.md) | [Glossário](00-glossário.md) | [Próximo: Controles de Repetição ->](14-controles-repetição.md)

---

## Introdução

No módulo anterior, você aprendeu a usar `if/elif/else` para tomar decisoes. Quando você tem muitas opcoes para comparar com um único valor (como um menu com 7 opcoes), o código pode ficar longo com muitos `elif`. O Python 3.10 introduziu uma alternativa mais organizada para esses casos: o `match/case`.

Pense no `match/case` como um cardapio de restaurante: você olha o cardapio (match), encontra o prato que quer (case) e faz o pedido. Se nenhum prato servir, você pede o prato do dia (case padrão).

Em outras linguagens de programação, essa estrutura e chamada de `switch/case`. O Python usa `match/case`, mas a ideia e a mesma.

> **Atenção:** O `match/case` so funciona a partir do **Python 3.10**. Se sua versão for anterior, use `if/elif/else`. Para verificar sua versão, digite no terminal: `python3 --version`.

---

## Como Executar os Exemplos Deste Módulo

1. Copie o código e cole em um novo arquivo no VSCode
2. Salve na pasta `~/meus-projetos/python-curso/modulo-13/`
3. No terminal: `cd ~/meus-projetos/python-curso/modulo-13`
4. Execute: `python3 nome_do_arquivo.py`

---

## Sintaxe Básica do match/case

```python
# Exemplo basico de match/case
# "command" = comando
command = input("Digite um comando (iniciar/parar/ajuda): ")

# match compara o valor da variavel com cada case
match command:
    case "iniciar":
        # Executa se command for "iniciar"
        print("Sistema iniciado!")
    case "parar":
        # Executa se command for "parar"
        print("Sistema parado.")
    case "ajuda":
        # Executa se command for "ajuda"
        print("Comandos disponiveis: iniciar, parar, ajuda")
    case _:
        # O underscore (_) e o caso padrao — executa se nenhum case anterior combinou
        # E como o "else" do if/elif/else
        print(f"Comando '{command}' nao reconhecido.")
```

**Saida esperada (se digitar "ajuda"):**
```
Comandos disponiveis: iniciar, parar, ajuda
```

### Anatomia do match/case

```
match variavel:           <-- o valor que queremos comparar
    case valor_1:         <-- se variavel == valor_1, executa este bloco
        instrucoes
    case valor_2:         <-- se variavel == valor_2, executa este bloco
        instrucoes
    case _:               <-- caso padrao (nenhum anterior combinou)
        instrucoes
```

> **Nota:** O `_` (underscore) no último `case` funciona como um "coringa" — combina com qualquer valor. E equivalente ao `else` do `if/elif/else`.

---

## Comparando match/case com if/elif/else

Vamos resolver o mesmo problema das duas formas para você ver a diferença:

### Com if/elif/else

```python
# Dia da semana com if/elif/else
# "day" = dia
day = int(input("Numero do dia (1-7): "))

if day == 1:
    print("Segunda-feira")
elif day == 2:
    print("Terca-feira")
elif day == 3:
    print("Quarta-feira")
elif day == 4:
    print("Quinta-feira")
elif day == 5:
    print("Sexta-feira")
elif day == 6:
    print("Sabado")
elif day == 7:
    print("Domingo")
else:
    print("Dia invalido!")
```

### Com match/case

```python
# Dia da semana com match/case — mais limpo e organizado
# "day" = dia
day = int(input("Numero do dia (1-7): "))

match day:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terca-feira")
    case 3:
        print("Quarta-feira")
    case 4:
        print("Quinta-feira")
    case 5:
        print("Sexta-feira")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Dia invalido!")
```

Ambos produzem o mesmo resultado. O `match/case` e mais limpo quando você esta comparando um único valor contra várias opcoes fixas.

### Quando usar cada um?

| Situacao | Melhor opcao |
|----------|-------------|
| Comparar um valor contra opcoes fixas | `match/case` |
| Verificar faixas de valores (>, <, >=) | `if/elif/else` |
| Combinar condições com and/or | `if/elif/else` |
| Poucas opcoes (2-3) | `if/elif/else` |
| Muitas opcoes fixas (4+) | `match/case` |

---

## Combinando Valores em um Único case

Você pode combinar vários valores em um único `case` usando o operador `|` (que significa "ou"):

```python
# Combinando valores com | (ou)
# "month" = mes
month = int(input("Numero do mes (1-12): "))

match month:
    case 1 | 2 | 3:
        # Meses 1, 2 ou 3
        # "season" = estacao
        season = "Verao"
    case 4 | 5 | 6:
        season = "Outono"
    case 7 | 8 | 9:
        season = "Inverno"
    case 10 | 11 | 12:
        season = "Primavera"
    case _:
        season = "Mes invalido"

print(f"Mes {month}: {season}")
```

**Saida esperada (se digitar 7):**
```
Mes 7: Inverno
```

---

## Verificando a Versão do Python

O `match/case` requer Python 3.10 ou superior. Para verificar sua versão:

```bash
python3 --version
```

Se a versão for anterior a 3.10 (por exemplo, 3.8 ou 3.9), o `match/case` não vai funcionar e você vera um `SyntaxError`. Nesse caso, use `if/elif/else` como alternativa — o resultado e o mesmo.

---

## Resumo

| Conceito | Descricao |
|----------|-----------|
| `match variavel:` | Inicia a comparação do valor da variável |
| `case valor:` | Verifica se a variável e igual ao valor |
| `case _:` | Caso padrão (coringa) — equivalente ao else |
| `case a \| b:` | Combina valores — "a ou b" |
| Requisito | Python 3.10 ou superior |

---

## Para Saber Mais

- [W3Schools — Python Conditions](https://www.w3schools.com/python/python_conditions.asp) — _Condicionais em Python (inclui match/case)_
- [Documentação Python — Match Statement](https://docs.python.org/pt-br/3/tutorial/controlflow.html#match-statements) — _Referencia oficial_

---

## Perguntas Frequentes (FAQ)

**P: match/case e a mesma coisa que switch/case de outras linguagens?**
R: Sim, a ideia e a mesma: comparar um valor contra várias opcoes. O Python usa `match/case` em vez de `switch/case`, mas o conceito e identico.

**P: Preciso usar match/case ou posso continuar com if/elif/else?**
R: Você pode usar qualquer um. O `if/elif/else` funciona em todas as versoes do Python e resolve qualquer situacao. O `match/case` e uma alternativa mais limpa para quando você compara um valor contra muitas opcoes fixas.

**P: O que acontece se minha versão do Python for anterior a 3.10?**
R: O `match/case` não vai funcionar e você vera um `SyntaxError`. Use `if/elif/else` como alternativa — o resultado e o mesmo.

**P: O que e o `_` (underscore) no case?**
R: E o caso padrão, também chamado de "coringa" ou "wildcard". Ele combina com qualquer valor que não tenha sido capturado pelos cases anteriores. E equivalente ao `else` do `if/elif/else`.

**P: O case padrão (_) e obrigatório?**
R: Não, e opcional. Mas e uma boa prática incluir para tratar valores inesperados, assim como o `else` no `if/elif/else`.

**P: Posso usar match/case com strings?**
R: Sim! Você pode comparar strings, números, booleanos e outros tipos. `case "opcao1":` verifica se o valor e exatamente "opcao1".

**P: O match/case diferencia maiusculas de minusculas?**
R: Sim, assim como qualquer comparação de strings em Python. `"Sim"` e `"sim"` sao diferentes. Converta para minusculas antes se quiser ignorar: `match resposta.lower():`.

**P: Posso fazer cálculos dentro do case?**
R: Não diretamente. O `case` compara com valores fixos, não com expressoes. Para verificar faixas (como `nota >= 7`), use `if/elif/else`.

**P: O que significa `|` no case?**
R: Significa "ou". `case 1 | 2 | 3:` combina com o valor 1, 2 ou 3. E como escrever `if x == 1 or x == 2 or x == 3:`.

**P: Posso ter código antes ou depois do match?**
R: Sim! O `match` e apenas uma estrutura dentro do programa. Você pode ter código antes (para ler dados) e depois (para exibir resultados).

**P: O match/case e mais rápido que if/elif/else?**
R: Na prática, a diferença de velocidade e insignificante. Escolha pela legibilidade, não pela velocidade.

**P: Posso aninhar match dentro de match?**
R: Tecnicamente sim, mas isso torna o código muito confuso. Prefira reorganizar a lógica de outra forma.

**P: O que e "pattern matching"?**
R: E o nome técnico da funcionalidade do match/case em Python. Significa "correspondencia de padrões" — o Python tenta encontrar qual padrão (case) corresponde ao valor dado (match).

**P: Posso usar variáveis no case?**
R: Cuidado! `case x:` não compara com uma variável `x` — ele captura o valor em uma nova variável chamada `x`. Para comparar com uma variável existente, use `if/elif/else` ou guards (recurso avancado).

**P: O que sao "guards" no match/case?**
R: Sao condições extras adicionadas com `if` dentro do case: `case x if x > 0:`. E um recurso avancado que não vamos aprofundar neste curso.

**P: Posso usar match/case para menus de programa?**
R: Sim, e um dos usos mais comuns! Menus com várias opcoes ficam muito limpos com match/case.

**P: O match/case substitui completamente o if/elif/else?**
R: Não. O `if/elif/else` e mais versatil — funciona com faixas, condições compostas e qualquer tipo de expressao. O `match/case` e melhor apenas para comparacoes de igualdade com valores fixos.

**P: Posso misturar match/case com if/elif/else no mesmo programa?**
R: Sim, sem problema! Use cada um onde fizer mais sentido.

**P: O que acontece se nenhum case combinar e não tiver case _?**
R: O Python simplesmente pula o match inteiro e continua com o código seguinte. Nenhum erro e gerado.

**P: E importante aprender match/case?**
R: E bom conhecer, mas não e essencial. Tudo que o match/case faz pode ser feito com if/elif/else. Considere o match/case como uma ferramenta extra no seu repertorio.

---

## Exercícios de Fixacao

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

**[Acessar Exercícios do Módulo 13](13-seletores-match-case-exercícios.md)**

---

[<- Anterior: Condicionais](12-condicionais.md) | [Glossário](00-glossário.md) | [Próximo: Controles de Repetição ->](14-controles-repetição.md)
