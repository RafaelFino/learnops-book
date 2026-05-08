# 5.15 — Exercícios: Tratamento de Erros

[← Voltar ao Módulo 5.15](cap05-mod15-tratamento-erros-conteudo.md)

---

## Como usar estes exercícios

1. Leia o enunciado com atenção
2. Tente resolver sozinho antes de olhar as dicas
3. Salve cada exercício em um arquivo separado na pasta `~/meus-projetos/python-curso/módulo-15/`
4. Execute com `python3 nome_do_arquivo.py`
5. Teste com entradas válidas E inválidas — o programa nunca deve parar com Traceback

---

## Exercício 1 — Entrada segura com intervalo (Nível: Fácil)

Crie uma função `safe_range_input(message, min_val, max_val)` que:
- Pede um número inteiro ao usuário
- Trata `ValueError` se o usuário digitar texto
- Verifica se o número está entre `min_val` e `max_val`
- Repete até receber um valor válido

Use a função para pedir a idade do usuário (entre 0 e 150).

**Saída esperada:**
```
Sua idade (0-150): abc
Erro: digite um numero inteiro!
Sua idade (0-150): -5
Erro: o valor deve ser entre 0 e 150.
Sua idade (0-150): 200
Erro: o valor deve ser entre 0 e 150.
Sua idade (0-150): 25
Idade registrada: 25
```

**Dica:** Combine `try`/`except` com `if` para validar o intervalo.


### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# "safe_range_input" = entrada segura com intervalo
# "message" = mensagem, "min_val" = valor minimo, "max_val" = valor maximo
def safe_range_input(message, min_val, max_val):
    while True:
        try:
            # "value" = valor
            value = int(input(message))
            if value < min_val or value > max_val:
                print(f"Erro: o valor deve ser entre {min_val} e {max_val}.")
                continue
            return value
        except ValueError:
            print("Erro: digite um numero inteiro!")

# "age" = idade
age = safe_range_input("Sua idade (0-150): ", 0, 150)
print(f"Idade registrada: {age}")
```

</details>

---

## Exercício 2 — Calculadora robusta (Nível: Médio)

Crie uma calculadora que:
1. Pede dois números e um operador (+, -, *, /)
2. Trata `ValueError` na entrada dos números
3. Trata divisão por zero
4. Trata operador inválido
5. Pergunta se o usuário quer fazer outro cálculo
6. O programa NUNCA deve parar com Traceback

**Saída esperada:**
```
=== Calculadora ===
Primeiro numero: abc
Erro: digite um numero valido!
Primeiro numero: 10
Operador (+, -, *, /): %
Erro: operador invalido! Use +, -, * ou /
Operador (+, -, *, /): /
Segundo numero: 0
Erro: divisao por zero!
Segundo numero: 5
Resultado: 10.0 / 5.0 = 2.0

Outro calculo? (s/n): s
Primeiro numero: 7
Operador (+, -, *, /): *
Segundo numero: 3
Resultado: 7.0 * 3.0 = 21.0

Outro calculo? (s/n): n
Ate mais!
```

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# "safe_float_input" = entrada segura de decimal
def safe_float_input(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Erro: digite um numero valido!")

# "safe_operator_input" = entrada segura de operador
def safe_operator_input():
    # "valid_operators" = operadores validos
    valid_operators = ["+", "-", "*", "/"]
    while True:
        # "op" = operador
        op = input("Operador (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        print("Erro: operador invalido! Use +, -, * ou /")

# "calculate" = calcular
def calculate(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2

def main():
    print("=== Calculadora ===")
    while True:
        num1 = safe_float_input("Primeiro numero: ")
        op = safe_operator_input()

        # Para divisao, garantir que o segundo numero nao e zero
        while True:
            num2 = safe_float_input("Segundo numero: ")
            if op == "/" and num2 == 0:
                print("Erro: divisao por zero!")
            else:
                break

        result = calculate(num1, num2, op)
        print(f"Resultado: {num1} {op} {num2} = {result}")

        # "again" = novamente
        again = input("\nOutro calculo? (s/n): ").strip().lower()
        if again != "s":
            break

    print("Ate mais!")

if __name__ == "__main__":
    main()
```

</details>

---

## Exercício 3 — Sistema de cadastro seguro (Nível: Difícil)

Crie um sistema de cadastro de produtos que:
1. Pede nome (texto, não pode ser vazio)
2. Pede preço (float, deve ser positivo)
3. Pede quantidade em estoque (int, deve ser >= 0)
4. Armazena em uma lista de dicionários
5. Permite listar todos os produtos cadastrados
6. Permite buscar produto por nome (trate o caso de não encontrar)
7. Trate TODOS os erros possíveis — o programa nunca deve parar com Traceback

**Menu esperado:**
```
=== Cadastro de Produtos ===
1. Cadastrar produto
2. Listar produtos
3. Buscar produto
4. Sair
Opcao: _
```

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# "products" = produtos (lista global)
products = []

def safe_float_input(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("Erro: o valor deve ser positivo!")
                continue
            return value
        except ValueError:
            print("Erro: digite um numero valido!")

def safe_int_input(message):
    while True:
        try:
            value = int(input(message))
            if value < 0:
                print("Erro: o valor nao pode ser negativo!")
                continue
            return value
        except ValueError:
            print("Erro: digite um numero inteiro!")

# "register_product" = cadastrar produto
def register_product():
    # "name" = nome
    name = ""
    while not name.strip():
        name = input("Nome do produto: ")
        if not name.strip():
            print("Erro: o nome nao pode ser vazio!")

    # "price" = preco
    price = safe_float_input("Preco (R$): ")
    # "stock" = estoque
    stock = safe_int_input("Quantidade em estoque: ")

    products.append({"name": name.strip(), "price": price, "stock": stock})
    print(f"Produto '{name.strip()}' cadastrado com sucesso!\n")

# "list_products" = listar produtos
def list_products():
    if not products:
        print("Nenhum produto cadastrado.\n")
        return
    print(f"\n{'Nome':<20} {'Preco':>10} {'Estoque':>10}")
    print("-" * 42)
    for product in products:
        print(f"{product['name']:<20} R$ {product['price']:>7.2f} {product['stock']:>10}")
    print()

# "search_product" = buscar produto
def search_product():
    # "query" = busca
    query = input("Nome do produto: ").strip().lower()
    # "found" = encontrados
    found = [p for p in products if query in p["name"].lower()]
    if not found:
        print(f"Nenhum produto encontrado com '{query}'.\n")
    else:
        for product in found:
            print(f"  {product['name']} - R$ {product['price']:.2f} - Estoque: {product['stock']}")
        print()

def main():
    print("=== Cadastro de Produtos ===\n")
    while True:
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Buscar produto")
        print("4. Sair")
        # "option" = opcao
        option = input("Opcao: ").strip()

        if option == "1":
            register_product()
        elif option == "2":
            list_products()
        elif option == "3":
            search_product()
        elif option == "4":
            print("Ate mais!")
            break
        else:
            print("Opcao invalida! Digite 1, 2, 3 ou 4.\n")

if __name__ == "__main__":
    main()
```

</details>

---

[← Voltar ao Módulo 5.15](cap05-mod15-tratamento-erros-conteudo.md)
