# Exercícios — Módulo 5.6: Conversão de Tipos e Manipulação de Strings

[← Voltar ao Módulo 5.6](cap05-mod06-conversao-strings-conteudo.md)

---

## Orientações

- Crie um arquivo `.py` separado para cada exercício
- Execute com `python3 nome_do_arquivo.py`
- Faça commit ao terminar: `git add . && git commit -m "feat: exercises module 5.6"`

---

## Exercício 1 — Formatador de Nome (Básico)

Crie um programa que pede o nome completo do usuário e exibe:
- Nome em MAIÚSCULAS (`upper()`)
- Nome em minúsculas (`lower()`)
- Nome formatado (`title()`)
- Quantidade de caracteres (`len()`)
- Iniciais (primeira letra de cada palavra)

Caso de uso real: sistemas de cadastro padronizam nomes automaticamente. Bancos armazenam nomes em maiúsculas por padrão.

---

## Exercício 2 — Validador de Entrada (Básico)

Crie um programa que pede um valor e verifica:
1. Se contém apenas dígitos (`isdigit()`) → converte para int e mostra o dobro
2. Se contém apenas letras (`isalpha()`) → mostra em maiúsculas
3. Caso contrário → mostra "Entrada mista" e o tamanho

Caso de uso real: formulários web validam cada campo antes de aceitar. Um campo de CEP só aceita dígitos, um campo de nome só aceita letras.

---

## Exercício 3 — Gerador de Email Corporativo (Básico)

Crie um programa que pede nome e sobrenome e gera um email no formato `nome.sobrenome@empresa.com`, tudo em minúsculas, sem espaços extras.

Exemplo: entrada "  Maria   Silva  " → saída "maria.silva@empresa.com"

Use `strip()`, `lower()` e `split()`.

Caso de uso real: empresas geram emails corporativos automaticamente quando um novo funcionário é cadastrado no sistema de RH.

---

## Exercício 4 — Formatador de CPF (Intermediário)

Crie um programa que pede um CPF como sequência de 11 dígitos e formata no padrão XXX.XXX.XXX-XX.

Exemplo: entrada "12345678901" → saída "123.456.789-01"

Use fatiamento de strings: `cpf[0:3]`, `cpf[3:6]`, etc.

Valide se a entrada tem exatamente 11 caracteres e se são todos dígitos.

Caso de uso real: sistemas bancários e governamentais formatam e validam CPFs constantemente. A Receita Federal processa milhões de CPFs por dia.

---

## Exercício 5 — Analisador de Texto (Intermediário)

Crie um programa que pede uma frase e exibe:
- Quantidade de caracteres (com e sem espaços)
- Quantidade de palavras (`split()` e `len()`)
- Primeira e última palavra
- Frase invertida (dica: `texto[::-1]`)
- Quantas vezes a letra "a" aparece (`count()`)

Caso de uso real: editores de texto como Word e Google Docs contam palavras e caracteres em tempo real. Redes sociais como Twitter limitam posts por quantidade de caracteres.

---

## Exercício 6 — Conversor de Temperatura Completo (Intermediário)

Crie um programa que pede um valor e a escala de origem (C, F ou K) e converte para as outras duas escalas.

Fórmulas:
- C para F: `F = C * 1.8 + 32`
- C para K: `K = C + 273.15`
- F para C: `C = (F - 32) / 1.8`
- K para C: `C = K - 273.15`

Use `upper()` para normalizar a escala digitada. Valide se a escala é válida.

Caso de uso real: APIs de clima retornam temperaturas em diferentes escalas. Aplicativos precisam converter para a escala preferida do usuário.

---

## Exercício 7 — Cifra de César Simples (Avançado)

Crie um programa que pede uma mensagem e um número de deslocamento, e "criptografa" a mensagem deslocando cada letra no alfabeto.

Exemplo com deslocamento 3: "abc" → "def", "xyz" → "abc"

Dica: use `ord()` para obter o código numérico de uma letra e `chr()` para converter de volta.

Caso de uso real: a Cifra de César é um dos algoritmos de criptografia mais antigos (usada por Júlio César em 50 a.C.). Embora simples demais para uso real hoje, o conceito de deslocar caracteres é a base de algoritmos modernos de criptografia.

---

## Exercício 8 — Gerador de Senha (Avançado)

Crie um programa que pede o nome completo e a data de nascimento (DD/MM/AAAA) e gera uma senha combinando:
- Duas primeiras letras do primeiro nome (maiúsculas)
- Dois últimos dígitos do ano
- Duas primeiras letras do sobrenome (minúsculas)
- Dia de nascimento

Exemplo: "Maria Silva", "15/03/1990" → "MA90si15"

Use `split()`, fatiamento e concatenação.

Caso de uso real: muitos sistemas geram senhas temporárias automaticamente para novos usuários, combinando dados pessoais com regras de formatação.



---

## Exercicio 7 — Formatador de CPF — Nivel: Intermediario

### Enunciado

Crie um programa que recebe um CPF como texto (apenas numeros, 11 digitos) e formata no padrao XXX.XXX.XXX-XX. Valide que tem exatamente 11 digitos numericos.

### Dicas

1. Use `isdigit()` para verificar se sao apenas numeros
2. Use `len()` para verificar o tamanho
3. Use fatiamento (slicing) para separar as partes: `cpf[:3]`, `cpf[3:6]`, etc.
4. Use f-string para montar o formato final

### Proposta de Teste

- **Caso basico:** "12345678901" -> "123.456.789-01"
- **Caso de borda:** "1234567890" (10 digitos) -> erro
- **Caso de borda:** "1234567890a" (com letra) -> erro

---

## Exercicio 8 — Conversor de Temperatura — Nivel: Basico

### Enunciado

Crie um programa que converte temperatura entre Celsius e Fahrenheit. O usuario digita o valor e a unidade (C ou F), e o programa converte para a outra unidade. Formulas: F = C * 9/5 + 32 e C = (F - 32) * 5/9.

### Dicas

1. Leia a entrada como string e separe o numero da unidade
2. Use `float()` para converter o numero
3. Use `upper()` para normalizar a unidade (c -> C)
4. Mostre o resultado com 1 casa decimal

### Proposta de Teste

- **Caso basico:** "100 C" -> "212.0 F"
- **Caso basico:** "32 F" -> "0.0 C"
- **Caso de borda:** "0 C" -> "32.0 F"


### Exercício Desafio: Conversor de Temperatura

Crie um programa que converta entre Celsius e Fahrenheit:

```python
# Pedir a temperatura e a escala
# "temp" = temperatura digitada
temp = float(input("Digite a temperatura: "))
# "scale" = escala (C ou F)
scale = input("Escala (C para Celsius, F para Fahrenheit): ").upper()

if scale == "C":
    # Converter Celsius para Fahrenheit
    # "result" = resultado da conversao
    result = (temp * 9/5) + 32
    print(f"{temp:.1f} C = {result:.1f} F")
elif scale == "F":
    # Converter Fahrenheit para Celsius
    result = (temp - 32) * 5/9
    print(f"{temp:.1f} F = {result:.1f} C")
else:
    print("Escala invalida. Use C ou F.")
```

Saída esperada:

```
Digite a temperatura: 100
Escala (C para Celsius, F para Fahrenheit): C
100.0 C = 212.0 F
```

### Dicas e Erros Comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `ValueError: could not convert` | Texto não é número válido | Verificar se digitou número correto |
| `.upper()` não funciona em número | Método de string usado em int/float | Converter para string primeiro |
| Resultado errado na conversão | Ordem das operações matemáticas | Usar parênteses para garantir precedência |
| `int()` perde casas decimais | `int()` trunca, não arredonda | Usar `float()` para manter decimais |


---

[← Voltar ao Módulo 5.6](cap05-mod06-conversao-strings-conteudo.md)
