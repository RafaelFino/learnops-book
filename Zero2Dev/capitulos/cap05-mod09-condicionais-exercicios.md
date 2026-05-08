# Exercícios — Módulo 5.9: Condicionais: if, elif e else

[← Voltar ao Módulo 5.9](cap05-mod09-condicionais-conteudo.md)

---

## Orientações

- Crie um arquivo `.py` separado para cada exercício
- Teste cada programa com diferentes entradas (inclusive entradas inesperadas)
- Exercícios de trace: escreva a resposta antes de executar
- Faça commit ao terminar: `git add . && git commit -m "feat: exercises module 5.9"`

---

## Exercício 1 — Classificador de Temperatura (Básico)

Crie um programa que pede a temperatura em Celsius e classifica:
- Abaixo de 0: "Congelante — cuidado com gelo nas estradas"
- 0 a 15: "Frio — use agasalho"
- 15 a 25: "Agradavel — temperatura ideal"
- 25 a 35: "Quente — beba bastante agua"
- Acima de 35: "Muito quente — evite exposicao ao sol"

Caso de uso real: aplicativos de clima como Climatempo e Weather.com classificam temperaturas e dão recomendações usando exatamente essa lógica.

---

## Exercício 2 — Calculadora de Frete (Básico)

Crie um programa que pede a distância em km e calcula o frete:
- Até 100 km: R$ 5.00 por km
- De 100 a 500 km: R$ 3.50 por km
- Acima de 500 km: R$ 2.00 por km

Caso de uso real: transportadoras como Correios e Jadlog calculam frete por faixa de distância. APIs de frete (como a do Mercado Livre) usam essa lógica.

---

## Exercício 3 — Validador de Senha (Intermediário)

Crie um programa que pede uma senha e verifica se atende aos critérios:
- Pelo menos 8 caracteres (`len()`)
- Contém pelo menos uma letra (`any(c.isalpha() for c in password)` — ou use um loop simples)
- Contém pelo menos um número (`any(c.isdigit() for c in password)`)
- Não é igual a "12345678" nem a "password"

Exiba quais critérios foram atendidos e quais falharam.

Caso de uso real: todo site que pede cadastro válida senhas com regras similares. Bancos como Nubank e Itaú têm regras ainda mais rigorosas.

---

## Exercício 4 — Jogo de Adivinhação (Intermediário)

Crie um programa que:
1. Define um número secreto (ex: `secret = 42`)
2. Pede ao usuário para adivinhar
3. Diz se o palpite é "muito alto", "muito baixo" ou "acertou!"
4. Se acertou, mostra quantas tentativas foram necessárias

Por enquanto, o programa só permite uma tentativa (no módulo 5.10, com loops, vamos permitir múltiplas tentativas).

Caso de uso real: jogos de adivinhação são a base de algoritmos de busca binária — uma das técnicas mais importantes da computação.

---

## Exercício 5 — Simulador de Semáforo (Intermediário)

Crie um programa que pede a cor do semáforo (verde, amarelo, vermelho) e exibe a ação correta:
- Verde: "Siga em frente"
- Amarelo: "Atencao — reduza a velocidade"
- Vermelho: "Pare — aguarde o sinal verde"
- Qualquer outra cor: "Cor inválida"

Use `lower().strip()` para normalizar a entrada. Implemente com if/elif/else E com match/case (se seu Python for 3.10+).

Caso de uso real: sistemas de controle de tráfego usam condicionais para determinar o comportamento de semáforos, cancelas e sinalizações.

---

## Exercício 6 — Classificador de IMC Completo (Intermediário)

Crie um programa que pede peso e altura, calcula o IMC e classifica:
- Abaixo de 18.5: Abaixo do peso
- 18.5 a 24.9: Peso normal
- 25.0 a 29.9: Sobrepeso
- 30.0 a 34.9: Obesidade grau I
- 35.0 a 39.9: Obesidade grau II
- 40.0 ou mais: Obesidade grau III

Adicione validação: peso deve ser entre 20 e 300 kg, altura entre 0.5 e 2.5 m.

Caso de uso real: aplicativos de saúde como Samsung Health e Apple Health calculam e classificam IMC. Sistemas hospitalares usam essa classificação para triagem de pacientes.

---

## Exercício 7 — Trace de Condicionais (Intermediário)

Sem executar, determine a saída de cada programa:

**Programa A:**
```python
x = 15
if x > 20:
    print("A")
elif x > 10:
    print("B")
elif x > 5:
    print("C")
else:
    print("D")
```

**Programa B:**
```python
a = True
b = False
c = True

if a and b:
    print("Caso 1")
elif a or b:
    if c:
        print("Caso 2")
    else:
        print("Caso 3")
else:
    print("Caso 4")
```

**Programa C:**
```python
score = 75
bonus = score > 70
penalty = score < 50
result = "aprovado" if bonus and not penalty else "reprovado"
print(result)
```

---

## Exercício 8 — Sistema de Login (Avançado)

Crie um programa que simula um sistema de login:
1. Defina usuário e senha corretos como constantes
2. Peça usuário e senha ao usuário
3. Verifique se ambos estão corretos
4. Se o usuário estiver correto mas a senha errada, diga "Senha incorreta"
5. Se o usuário não existir, diga "Usuario não encontrado"
6. Se ambos estiverem corretos, diga "Login realizado com sucesso!"

Caso de uso real: todo sistema web implementa essa lógica de autenticação. Na prática, senhas são armazenadas criptografadas (hash), mas a lógica de verificação é a mesma.

---

## Exercício 9 — Calculadora de Imposto de Renda (Avançado)

Crie um programa que pede o salário mensal e calcula o imposto de renda usando a tabela simplificada:
- Até R$ 2.259,20: isento
- De R$ 2.259,21 a R$ 2.826,65: 7,5%
- De R$ 2.826,66 a R$ 3.751,05: 15%
- De R$ 3.751,06 a R$ 4.664,68: 22,5%
- Acima de R$ 4.664,68: 27,5%

Exiba a faixa, a alíquota e o valor do imposto.

Caso de uso real: a Receita Federal calcula o imposto de renda de milhões de brasileiros usando essa tabela. Sistemas de folha de pagamento aplicam essa lógica todo mês.


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


### Exercício Extra: Classificador de Triângulos

Crie um programa que receba três lados e classifique o triângulo:

```python
# "a", "b", "c" = lados do triangulo
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))

# Verificar se forma triangulo (cada lado menor que a soma dos outros dois)
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triangulo equilatero (3 lados iguais)")
    elif a == b or a == c or b == c:
        print("Triangulo isosceles (2 lados iguais)")
    else:
        print("Triangulo escaleno (3 lados diferentes)")
else:
    print("Esses lados nao formam um triangulo")
```

Saída esperada:

```
Lado a: 3
Lado b: 3
Lado c: 3
Triangulo equilatero (3 lados iguais)
```

---

[← Voltar ao Módulo 5.9](cap05-mod09-condicionais-conteudo.md)
