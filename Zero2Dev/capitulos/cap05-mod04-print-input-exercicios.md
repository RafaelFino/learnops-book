# Exercícios — Módulo 5.4: print() e input()

[← Voltar ao Módulo 5.4](cap05-mod04-print-input-conteudo.md)

---

## Orientações

- Crie um arquivo `.py` separado para cada exercício (ex: `ex01_cartao.py`)
- Execute com `python3 nome_do_arquivo.py`
- Tente resolver sozinho antes de consultar as dicas
- Faça commit dos exercícios: `git add . && git commit -m "feat: exercises module 5.4"`

---

## Exercício 1 — Cartão de Visita (Básico)

Crie um programa que pede nome, profissão e telefone, e exibe um cartão formatado.

Exemplo de saída:

```
+------------------------------+
| Nome: Joao Silva             |
| Profissao: Programador       |
| Tel: (11) 99999-0000         |
+------------------------------+
```

Dica: use `print()` para desenhar as bordas e f-strings para os dados.

---

## Exercício 2 — Calculadora de Gorjeta (Básico)

Crie um programa que pede o valor da conta de um restaurante e a porcentagem de gorjeta desejada, e calcula:
- Valor da gorjeta
- Valor total (conta + gorjeta)

Caso de uso real: aplicativos como iFood e Uber Eats calculam gorjeta exatamente assim.

```python
# Dica: porcentagem e o valor dividido por 100
# Se o usuario digitar 15 (%), a conta e: valor * (15 / 100)
```

Exemplo de saída:

```
Valor da conta: R$ 85.00
Porcentagem de gorjeta: 15

Gorjeta (15%): R$ 12.75
Total: R$ 97.75
```

---

## Exercício 3 — Conversor de Temperatura (Básico)

Crie um programa que pede uma temperatura em Celsius e converte para Fahrenheit e Kelvin.

Fórmulas:
- Fahrenheit = Celsius * 1.8 + 32
- Kelvin = Celsius + 273.15

Caso de uso real: estações meteorológicas convertem temperaturas entre escalas o tempo todo. APIs de clima como OpenWeatherMap retornam dados em Kelvin.

---

## Exercício 4 — Ficha de Personagem (Intermediário)

Crie um programa que simula a criação de um personagem de RPG. Peça:
- Nome do personagem
- Classe (guerreiro, mago, arqueiro)
- Nível (número inteiro)
- Pontos de vida (número inteiro)

Exiba uma ficha formatada com bordas e alinhamento.

Caso de uso real: jogos como World of Warcraft e Final Fantasy armazenam dados de personagens exatamente assim — cada atributo é uma variável com tipo específico.

---

## Exercício 5 — Calculadora de Combustível (Intermediário)

Crie um programa que pede:
- Distância da viagem em km
- Consumo do carro em km/litro
- Preço do litro de combustível

E calcula:
- Litros necessários (distância / consumo)
- Custo total da viagem (litros * preço)

Caso de uso real: apps como Waze e Google Maps estimam custo de combustível usando exatamente esse cálculo.

Exemplo de saída:

```
=== Calculadora de Combustivel ===

Distancia (km): 450
Consumo (km/l): 12
Preco do litro: R$ 5.89

--- Resultado ---
Litros necessarios: 37.50
Custo da viagem: R$ 220.88
```

---

## Exercício 6 — Quiz Interativo (Intermediário)

Crie um programa que faz 3 perguntas de conhecimentos gerais, compara a resposta do usuário com a resposta correta e conta os acertos.

Dica: use `.lower().strip()` para normalizar a resposta do usuário antes de comparar.

Caso de uso real: plataformas como Duolingo e Khan Academy usam essa lógica para verificar respostas de exercícios.

---

## Exercício 7 — Gerador de Recibo (Avançado)

Crie um programa que simula um caixa de loja. Peça 3 produtos (nome e preço de cada) e exiba um recibo formatado com:
- Lista de produtos com preços
- Subtotal
- Imposto (15%)
- Total final

Caso de uso real: todo sistema de PDV (Ponto de Venda) em supermercados e lojas gera recibos assim.

Exemplo de saída:

```
========== RECIBO ==========
Arroz              R$  5.99
Feijao             R$  8.50
Macarrao           R$  3.75
----------------------------
Subtotal:          R$ 18.24
Imposto (15%):     R$  2.74
TOTAL:             R$ 20.98
========== OBRIGADO ========
```


### Exercício Desafio: Gerador de Cartão de Visita

Crie um programa que peça ao usuário:
- Nome completo
- Profissão
- Telefone
- Email

E gere um cartão de visita formatado:

```python
# Pedir dados ao usuario
# "name" = nome
name = input("Seu nome completo: ")
# "profession" = profissao
profession = input("Sua profissao: ")
# "phone" = telefone
phone = input("Seu telefone: ")
# "email" = email do usuario
email = input("Seu email: ")

# Montar o cartao
print()
print("+" + "-" * 40 + "+")
print("|" + name.center(40) + "|")
print("|" + profession.center(40) + "|")
print("|" + " " * 40 + "|")
print("|" + f"Tel: {phone}".center(40) + "|")
print("|" + email.center(40) + "|")
print("+" + "-" * 40 + "+")
```

Saída esperada (exemplo):

```
+----------------------------------------+
|            Maria da Silva              |
|          Desenvolvedora Python         |
|                                        |
|          Tel: (11) 99999-0000          |
|          maria@email.com               |
+----------------------------------------+
```

**Dica:** Use o método `.center()` para centralizar texto dentro de um espaço fixo. Experimente também `.ljust()` e `.rjust()` para alinhar à esquerda e à direita.

### Dicas e Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `SyntaxError: EOL while scanning` | Aspas não fechadas no `print()` | Verificar se abriu e fechou aspas |
| Texto colado sem espaço | Faltou espaço dentro das aspas | Adicionar espaços: `print("Olá", nome)` |
| `input()` não aparece | Programa esperando digitação | Digite algo e pressione Enter |
| Número vira texto | `input()` sempre retorna string | Normal neste módulo — conversão vem depois |
| f-string não funciona | Esqueceu o `f` antes das aspas | `f"Olá {nome}"` e não `"Olá {nome}"` |


---

[← Voltar ao Módulo 5.4](cap05-mod04-print-input-conteudo.md)
