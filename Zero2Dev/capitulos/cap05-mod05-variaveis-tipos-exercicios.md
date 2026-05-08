# Exercícios — Módulo 5.5: Variáveis e Tipos de Dados

[← Voltar ao Módulo 5.5](cap05-mod05-variaveis-tipos-conteudo.md)

---

## Orientações

- Crie um arquivo `.py` separado para cada exercício
- Execute com `python3 nome_do_arquivo.py`
- Use `type()` para verificar os tipos sempre que tiver dúvida
- Faça commit ao terminar: `git add . && git commit -m "feat: exercises module 5.5"`

---

## Exercício 1 — Ficha Pessoal (Básico)

Crie um programa que pede nome, idade, altura e se a pessoa é estudante (sim/não). Guarde cada dado no tipo correto:
- Nome → str
- Idade → int
- Altura → float
- Estudante → bool (converta "sim"/"não" para True/False)

Exiba todos os dados com seus tipos usando `type()`.

Caso de uso real: sistemas de RH de empresas armazenam dados de funcionários com tipos específicos para cada campo — texto para nome, número para salário, booleano para "ativo/inativo".

---

## Exercício 2 — Trace Mental (Básico)

Sem executar o código, escreva no papel qual será a saída de cada programa. Depois execute para verificar:

**Programa A:**
```python
x = 10
y = 20
x = y
y = 5
print("x:", x, "y:", y)
```

**Programa B:**
```python
a = "Python"
b = a
a = "Java"
print("a:", a, "b:", b)
```

**Programa C:**
```python
price = 100
price = price * 0.9
price = price - 5
print("Preco final:", price)
```

Caso de uso real: programadores fazem "trace" (acompanhar a execução mentalmente) o tempo todo para encontrar bugs. É uma das habilidades mais importantes de debugging.

---

## Exercício 3 — Tipos Misturados (Básico)

Crie variáveis de cada tipo (int, float, str, bool) e responda experimentando no código:

1. O que acontece quando você soma int + float? Qual o tipo do resultado?
2. O que acontece quando você multiplica str * int? (ex: `"ha" * 3`)
3. O que acontece quando você soma str + str?
4. O que acontece quando você soma int + bool? (True vale 1, False vale 0)

Use `type()` para confirmar cada resultado.

---

## Exercício 4 — Conversor de Unidades (Intermediário)

Crie um programa que converte entre unidades de medida. Peça um valor em metros e exiba:
- Em centímetros (metros * 100)
- Em milímetros (metros * 1000)
- Em quilômetros (metros / 1000)
- Em polegadas (metros * 39.37)
- Em pés (metros * 3.281)

Use variáveis com nomes descritivos em inglês e comentários traduzindo.

Caso de uso real: aplicativos de engenharia e construção civil fazem conversões de unidades constantemente. APIs internacionais frequentemente retornam medidas em unidades diferentes das que usamos no Brasil.

---

## Exercício 5 — Calculadora de Salário (Intermediário)

Crie um programa que pede:
- Salário bruto mensal (float)
- Porcentagem de desconto de INSS (float, ex: 11)
- Porcentagem de desconto de IR (float, ex: 15)
- Valor do vale-transporte (float)

Calcule e exiba:
- Desconto INSS
- Desconto IR (sobre o valor após INSS)
- Salário líquido (bruto - INSS - IR - VT)

Caso de uso real: todo sistema de folha de pagamento faz esse cálculo. Empresas como TOTVS e SAP processam milhões de folhas de pagamento usando essa lógica.

---

## Exercício 6 — Swap sem Variável Temporária (Intermediário)

Crie duas variáveis `a = 10` e `b = 20`. Troque os valores entre elas de duas formas:

1. Usando a forma Python: `a, b = b, a`
2. Usando uma variável temporária (como seria em C):
```python
temp = a
a = b
b = temp
```

Exiba os valores antes e depois de cada troca.

Caso de uso real: algoritmos de ordenação (como Bubble Sort, que veremos no módulo 5.16) trocam valores entre posições constantemente.

---

## Exercício 7 — Simulador de Conta Bancária (Avançado)

Crie um programa que simula uma conta bancária simples:
- Defina um saldo inicial (float)
- Peça ao usuário 3 operações: cada uma é um valor (positivo = depósito, negativo = saque)
- Após cada operação, exiba o saldo atualizado
- No final, exiba um extrato com todas as operações e o saldo final

Use variáveis com nomes claros: `balance`, `transaction1`, `transaction2`, `transaction3`.

Caso de uso real: todo aplicativo bancário (Nubank, Inter, Itaú) mantém o saldo como uma variável que é atualizada a cada transação.



---

## Exercicio 7 — Troca de Valores — Nivel: Intermediario

### Enunciado

Crie um programa que tem duas variaveis `a` e `b` com valores diferentes. Troque os valores entre elas (o valor de `a` vai para `b` e vice-versa) e mostre o antes e depois. Faca de duas formas: usando uma variavel temporaria e usando troca direta do Python.

### Dicas

1. Forma 1: use uma variavel `temp` para guardar um valor temporariamente
2. Forma 2: Python permite `a, b = b, a` (troca direta)
3. Mostre os valores antes e depois da troca para confirmar

### Proposta de Teste

- **Caso basico:** a=10, b=20 -> depois: a=20, b=10
- **Caso de borda:** a=5, b=5 -> depois: a=5, b=5 (nada muda)


### Exercício Desafio: Calculadora de IMC

Crie um programa que calcule o IMC (Índice de Massa Corporal):

```python
# Pedir dados ao usuario
# "weight" = peso em kg
weight = float(input("Seu peso em kg: "))
# "height" = altura em metros
height = float(input("Sua altura em metros: "))

# Calcular IMC: peso dividido pela altura ao quadrado
# "bmi" = indice de massa corporal
bmi = weight / (height ** 2)

# Mostrar resultado
print(f"Seu IMC e: {bmi:.1f}")
```

Saída esperada (exemplo):

```
Seu peso em kg: 70
Sua altura em metros: 1.75
Seu IMC e: 22.9
```

**Dica:** O operador `**` calcula potência. `height ** 2` é o mesmo que `height * height`. O `:.1f` formata o número com 1 casa decimal.

### Dicas e Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `NameError: name 'x' is not defined` | Variável não foi criada antes de usar | Criar a variável antes de referenciar |
| `TypeError: can't multiply str by str` | Tentou operar com strings | Converter para `int()` ou `float()` |
| Resultado com muitas casas decimais | Float tem precisão extendida | Usar `:.2f` para formatar |
| Variável com nome errado | Python diferencia maiúsculas | `Nome` e `nome` são variáveis diferentes |
| `SyntaxError` ao nomear variável | Usou palavra reservada ou espaço | Nomes sem espaço, sem acentos |


---

[← Voltar ao Módulo 5.5](cap05-mod05-variaveis-tipos-conteudo.md)
