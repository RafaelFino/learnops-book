# Exercícios — Módulo 5.8: Indentação, Escopo e Estrutura

[← Voltar ao Módulo 5.8](cap05-mod08-indentacao-escopo-conteudo.md)

---

## Orientações

- Atenção especial à indentação — cada espaço importa
- Nos exercícios de "encontre o erro", tente identificar o problema sem executar primeiro
- Faça commit ao terminar: `git add . && git commit -m "feat: exercises module 5.8"`

---

## Exercício 1 — Encontre o Erro (Básico)

Identifique e corrija os erros de indentação em cada programa. Não execute antes de tentar corrigir mentalmente:

**Programa A:**
```python
age = 20
if age >= 18:
print("Maior de idade")
    print("Pode votar")
```

**Programa B:**
```python
name = input("Nome: ")
    city = input("Cidade: ")
print(f"Ola, {name} de {city}")
```

**Programa C:**
```python
x = 10
if x > 5:
    print("Maior que 5")
        print("Continuando...")
    print("Fim do if")
```

---

## Exercício 2 — Blocos Aninhados (Básico)

Escreva um programa com 3 níveis de indentação. Use variáveis `age`, `has_ticket` e `is_vip`:
- Nível 0: verifica se age >= 18
- Nível 1: verifica se has_ticket é True
- Nível 2: verifica se is_vip é True e exibe mensagem diferente

Cada nível deve imprimir em qual nível está.

Caso de uso real: sistemas de controle de acesso em eventos verificam múltiplas condições em sequência — idade, ingresso, tipo de ingresso (VIP, pista, camarote).

---

## Exercício 3 — Reestruturar Código (Intermediário)

O código abaixo funciona mas está mal organizado. Reestruture seguindo o padrão profissional (constantes no topo, funções no meio, programa principal no final):

```python
x = float(input("Valor: "))
y = x * 0.15
z = x + y
print(f"Subtotal: R$ {x:.2f}")
print(f"Imposto: R$ {y:.2f}")
print(f"Total: R$ {z:.2f}")
w = float(input("Outro valor: "))
a = w * 0.15
b = w + a
print(f"Subtotal: R$ {w:.2f}")
print(f"Imposto: R$ {a:.2f}")
print(f"Total: R$ {b:.2f}")
```

Dica: o código repete a mesma lógica duas vezes. Crie uma função `calculate_total(value, tax_rate)` e use constantes para a taxa.

Caso de uso real: código duplicado é um dos problemas mais comuns em projetos reais. Refatorar (reorganizar sem mudar o comportamento) é uma atividade diária de programadores.

---

## Exercício 4 — Trace de Escopo (Intermediário)

Sem executar, diga qual será a saída de cada programa:

**Programa A:**
```python
x = 10

def change_x():
    x = 20
    print(f"Dentro: x = {x}")

change_x()
print(f"Fora: x = {x}")
```

**Programa B:**
```python
status = "indefinido"

age = 25
if age >= 18:
    status = "adulto"

print(f"Status: {status}")
```

Depois execute para verificar. Explique por que o resultado é esse.

---

## Exercício 5 — Programa Bem Estruturado (Avançado)

Crie um programa completo e bem estruturado que simula uma loja simples:
- Constantes: taxa de imposto, desconto para compras acima de R$ 200
- Função: `calculate_final_price(price, quantity)` que aplica imposto e desconto
- Programa principal: pede produto, preço e quantidade, chama a função e exibe resultado

Siga a estrutura: imports → constantes → funções → programa principal.

Caso de uso real: todo sistema de e-commerce segue essa estrutura — constantes de configuração, funções de cálculo e fluxo principal de interação com o usuário.



---

## Exercicio 7 — Corrigir Indentacao — Nivel: Basico

### Enunciado

O codigo abaixo tem erros de indentacao. Corrija-o para que funcione corretamente e mostre "Aprovado" para notas >= 7 e "Reprovado" para notas < 7.

```python
grade = float(input("Nota: "))
if grade >= 7:
print("Aprovado")
    print("Parabens!")
else:
        print("Reprovado")
    print("Estude mais")
print("Fim")
```

### Dicas

1. Tudo dentro do `if` deve ter 4 espacos de indentacao
2. Tudo dentro do `else` deve ter 4 espacos de indentacao
3. A linha "Fim" esta fora do if/else — sem indentacao extra
4. Todas as linhas de um mesmo bloco devem ter a mesma indentacao

### Proposta de Teste

- **Caso basico:** Nota 8 -> "Aprovado", "Parabens!", "Fim"
- **Caso basico:** Nota 5 -> "Reprovado", "Estude mais", "Fim"


### Dicas Gerais para os Exercícios

- Comece pelo exercício mais simples e avance gradualmente
- Teste cada parte do código separadamente antes de juntar tudo
- Use `print()` para verificar valores intermediários quando algo não funcionar
- Releia o enunciado se o resultado não for o esperado — às vezes o problema está na interpretação
- Não tenha medo de errar — cada erro é uma oportunidade de aprender como Python funciona

### Tabela de Referência Rápida

| Conceito | Exemplo | Resultado |
|----------|---------|-----------|
| Criar variável | `x = 10` | x vale 10 |
| Ler entrada | `nome = input("Nome: ")` | Espera digitação |
| Converter para inteiro | `int("42")` | 42 |
| Converter para decimal | `float("3.14")` | 3.14 |
| Converter para texto | `str(42)` | "42" |
| Formatar com f-string | `f"Valor: {x}"` | "Valor: 10" |
| Formatar decimais | `f"{x:.2f}"` | "10.00" |


### Exercício Extra: Identificando Erros de Indentação

Analise cada trecho abaixo e identifique o erro de indentação. Corrija mentalmente antes de testar:

**Trecho 1:**
```python
# "age" = idade
age = 18
if age >= 18:
print("Maior de idade")  # Erro: falta indentacao
```

**Trecho 2:**
```python
# "numbers" = lista de numeros
numbers = [1, 2, 3]
for n in numbers:
    print(n)
        print("proximo")  # Erro: indentacao excessiva
```

**Trecho 3:**
```python
# "x" = valor para testar
x = 10
if x > 5:
    print("maior que 5")
  print("continuando")  # Erro: indentacao inconsistente (2 espacos vs 4)
```

**Respostas:**
1. Falta 4 espaços antes do `print` dentro do `if`
2. O segundo `print` tem 8 espaços mas deveria ter 4 (mesmo nível do primeiro)
3. Mistura de 2 e 4 espaços — Python exige consistência dentro do mesmo bloco

---

[← Voltar ao Módulo 5.8](cap05-mod08-indentacao-escopo-conteudo.md)
