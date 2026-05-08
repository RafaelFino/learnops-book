# Exercícios — Módulo 5.7: Operadores Matemáticos e Lógicos

[← Voltar ao Módulo 5.7](cap05-mod07-operadores-conteudo.md)

---

## Orientações

- Crie um arquivo `.py` separado para cada exercício
- Execute com `python3 nome_do_arquivo.py`
- Nos exercícios de trace, escreva a resposta no papel ANTES de executar
- Faça commit ao terminar: `git add . && git commit -m "feat: exercises module 5.7"`

---

## Exercício 1 — Calculadora de Troco (Básico)

Crie um programa que pede o valor da compra e o valor pago. Calcule e exiba o troco. Se o valor pago for menor que a compra, exiba "Valor insuficiente".

Caso de uso real: todo caixa de supermercado calcula troco. Sistemas de PDV fazem essa verificação milhares de vezes por dia.

---

## Exercício 2 — Par ou Ímpar (Básico)

Crie um programa que pede um número e diz se é par ou ímpar usando o operador `%` (módulo).

Dica: um número é par se `número % 2 == 0`.

Caso de uso real: algoritmos de distribuição de carga usam par/ímpar para alternar entre servidores. Se o ID do pedido é par, vai para o servidor A; se ímpar, vai para o B.

---

## Exercício 3 — Trace Mental: Aritméticos (Básico)

Sem executar, calcule o resultado de cada expressão. Depois execute para verificar:

```python
# 1.
print(2 + 3 * 4)

# 2.
print((2 + 3) * 4)

# 3.
print(10 % 3 + 2 ** 3)

# 4.
print(15 // 4 + 15 % 4)

# 5.
print(2 ** 3 ** 2)  # Cuidado: ** e avaliado da direita para a esquerda!
```

---

## Exercício 4 — Trace Mental: Lógicos (Básico)

Sem executar, determine se cada expressão é True ou False:

```python
# 1.
print(True and False or True)

# 2.
print(not (5 > 3 and 2 < 1))

# 3.
print(10 >= 10 and not False)

# 4.
print("python" in "eu amo Python")

# 5.
print(not (True or False) and True)
```

Dica: lembre-se da precedência: `not` primeiro, depois `and`, depois `or`.

---

## Exercício 5 — Calculadora de Desconto (Intermediário)

Crie um programa que pede o preço original e a porcentagem de desconto. Calcule e exiba:
- Valor do desconto
- Preço com desconto
- Economia em relação ao original

Caso de uso real: sites de e-commerce como Amazon e Mercado Livre calculam descontos em tempo real. Black Friday é basicamente um festival de operadores aritméticos.

---

## Exercício 6 — Verificador de Triângulo (Intermediário)

Crie um programa que pede 3 valores (lados de um triângulo) e verifica:
1. Se formam um triângulo válido (cada lado deve ser menor que a soma dos outros dois)
2. Se é equilátero (3 lados iguais), isósceles (2 lados iguais) ou escaleno (3 lados diferentes)

Use operadores de comparação e lógicos.

Caso de uso real: softwares de CAD (Computer-Aided Design) como AutoCAD validam geometrias usando essas mesmas verificações antes de renderizar formas.

---

## Exercício 7 — Simulador de Nota Fiscal (Intermediário)

Crie um programa que pede 3 produtos (nome e preço) e calcula:
- Subtotal
- ICMS (18% do subtotal)
- PIS (1.65% do subtotal)
- COFINS (7.6% do subtotal)
- Total com impostos

Use operadores aritméticos e de atribuição composta (`+=`).

Caso de uso real: todo sistema de emissão de nota fiscal (NF-e) calcula impostos automaticamente. Empresas como TOTVS e SAP processam milhões de notas fiscais por mês.

---

## Exercício 8 — Tabela Verdade Interativa (Intermediário)

Crie um programa que pede dois valores booleanos (True/False) ao usuário e exibe a tabela verdade completa para AND, OR e NOT:

```
Valor A: True
Valor B: False

A AND B = False
A OR B  = True
NOT A   = False
NOT B   = True
```

Caso de uso real: engenheiros de hardware usam tabelas verdade para projetar circuitos lógicos. Cada porta lógica dentro do processador do seu computador implementa uma dessas operações.

---

## Exercício 9 — Classificador de Faixa Etária (Avançado)

Crie um programa que pede a idade e classifica em:
- Bebê (0-2)
- Criança (3-11)
- Adolescente (12-17)
- Adulto (18-59)
- Idoso (60+)

Além disso, verifique usando operadores lógicos:
- Pode votar? (16+ anos)
- Pode dirigir? (18+ anos)
- Pode se aposentar? (65+ anos para homens, 62+ para mulheres — peça o sexo)

Caso de uso real: sistemas do governo (INSS, TSE) classificam cidadãos por faixa etária para determinar direitos e obrigações.

---

## Exercício 10 — Calculadora de Empréstimo (Avançado)

Crie um programa que pede:
- Valor do empréstimo
- Taxa de juros mensal (%)
- Número de parcelas

Calcule usando juros simples:
- Juros total = valor * (taxa/100) * parcelas
- Valor total = valor + juros
- Valor da parcela = valor total / parcelas

Caso de uso real: bancos e fintechs como Nubank calculam parcelas de empréstimos e financiamentos usando fórmulas similares (na prática usam juros compostos, que é mais complexo).


### Exercício Desafio: Calculadora de Desconto Progressivo

```python
# "price" = preco original
price = float(input("Preco do produto: R$ "))

# Desconto progressivo:
# Ate R$50: sem desconto
# R$50 a R$200: 10% de desconto
# Acima de R$200: 15% de desconto
if price <= 50:
    # "discount" = percentual de desconto
    discount = 0
elif price <= 200:
    discount = 10
else:
    discount = 15

# "discount_value" = valor do desconto em reais
discount_value = price * discount / 100
# "final_price" = preco final com desconto
final_price = price - discount_value

print(f"Preco original: R$ {price:.2f}")
print(f"Desconto: {discount}% (R$ {discount_value:.2f})")
print(f"Preco final: R$ {final_price:.2f}")
```

Saída esperada:

```
Preco do produto: R$ 150
Preco original: R$ 150.00
Desconto: 10% (R$ 15.00)
Preco final: R$ 135.00
```

### Dicas e Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| Divisão inteira inesperada | Usar `//` em vez de `/` | `//` trunca, `/` mantém decimais |
| `%` não calcula porcentagem | `%` é módulo (resto), não porcentagem | Para 10%: `valor * 10 / 100` |
| Precedência errada | Multiplicação antes de soma | Usar parênteses: `(a + b) * c` |


---

[← Voltar ao Módulo 5.7](cap05-mod07-operadores-conteudo.md)
