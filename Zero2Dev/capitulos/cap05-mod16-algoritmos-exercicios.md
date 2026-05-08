# 5.16 — Exercícios: Resolvendo Problemas com Algoritmos

[← Voltar ao Módulo 5.16](cap05-mod16-algoritmos-conteudo.md)

---

## Como usar estes exercícios

1. Para cada exercício, siga o método dos 4 passos: entender, planejar (pseudocódigo), implementar, testar
2. Tente resolver sozinho antes de olhar as respostas
3. Salve cada exercício em um arquivo separado na pasta `~/meus-projetos/python-curso/módulo-16/`
4. Execute com `python3 nome_do_arquivo.py`

---

## Exercício 1 — Segundo maior número (Nível: Fácil)

Crie uma função `find_second_max(numbers)` que encontra o segundo maior número em uma lista, **sem usar sorted()**.

**Casos de teste:**
```python
print(find_second_max([3, 7, 2, 9, 4]))    # 7
print(find_second_max([10, 10, 10]))        # 10
print(find_second_max([5]))                 # None
print(find_second_max([1, 2]))              # 1
```

**Dica:** Mantenha duas variáveis: `max_value` e `second_max`.


### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# "find_second_max" = encontrar segundo maximo
def find_second_max(numbers):
    if len(numbers) < 2:
        return None

    # Inicializa com os dois primeiros, na ordem correta
    if numbers[0] >= numbers[1]:
        max_value = numbers[0]
        second_max = numbers[1]
    else:
        max_value = numbers[1]
        second_max = numbers[0]

    # Percorre o restante
    for number in numbers[2:]:
        if number > max_value:
            second_max = max_value  # O antigo maximo vira segundo
            max_value = number
        elif number > second_max:
            second_max = number

    return second_max

# Testes
print(find_second_max([3, 7, 2, 9, 4]))  # 7
print(find_second_max([10, 10, 10]))      # 10
print(find_second_max([5]))               # None
print(find_second_max([1, 2]))            # 1
```

</details>

---

## Exercício 2 — Remover duplicatas mantendo ordem (Nível: Médio)

Crie uma função `remove_duplicates(items)` que remove itens duplicados de uma lista, mantendo a ordem original dos elementos.

**Casos de teste:**
```python
print(remove_duplicates([1, 2, 3, 2, 1, 4, 3, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates(["a", "b", "a", "c", "b"]))  # ["a", "b", "c"]
print(remove_duplicates([]))                           # []
print(remove_duplicates([1, 1, 1]))                    # [1]
```

**Dica:** Use uma lista para o resultado e verifique se o item já está nela antes de adicionar.

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# "remove_duplicates" = remover duplicatas
def remove_duplicates(items):
    # "seen" = ja vistos
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

# Testes
print(remove_duplicates([1, 2, 3, 2, 1, 4, 3, 5]))
print(remove_duplicates(["a", "b", "a", "c", "b"]))
print(remove_duplicates([]))
print(remove_duplicates([1, 1, 1]))
```

</details>

---

## Exercício 3 — Cifra de César (Nível: Difícil)

A Cifra de César é um dos métodos de criptografia mais antigos do mundo, usado por Júlio César para enviar mensagens secretas. A ideia é deslocar cada letra do alfabeto por um número fixo de posições.

Exemplo com deslocamento 3: A vira D, B vira E, C vira F, ..., Z vira C.

Crie duas funções:
- `encrypt(text, shift)` — criptografa o texto
- `decrypt(text, shift)` — descriptografa o texto

**Regras:**
- Apenas letras são deslocadas (números, espaços e pontuação ficam iguais)
- Mantenha maiúsculas e minúsculas
- O alfabeto é circular: depois de Z vem A

**Casos de teste:**
```python
print(encrypt("Hello World!", 3))    # "Khoor Zruog!"
print(decrypt("Khoor Zruog!", 3))    # "Hello World!"
print(encrypt("Python 3.12", 5))     # "Udymts 3.12"
print(decrypt("Udymts 3.12", 5))     # "Python 3.12"
```

**Dica:** Use `ord()` para obter o código numérico de um caractere e `chr()` para converter de volta. A letra 'a' tem código 97, 'z' tem 122, 'A' tem 65, 'Z' tem 90.

### Resposta Comentada

<details>
<summary>Clique para ver a resposta</summary>

```python
# "encrypt" = criptografar
# "text" = texto, "shift" = deslocamento
def encrypt(text, shift):
    # "result" = resultado
    result = ""
    for char in text:
        if char.isalpha():  # Verifica se e letra
            # Determina o inicio do alfabeto (maiusculo ou minusculo)
            # "base" = base (codigo ASCII de 'a' ou 'A')
            base = ord('A') if char.isupper() else ord('a')
            # Desloca a letra e usa % 26 para circular
            # "shifted" = deslocado
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Nao e letra — mantem como esta
            result += char
    return result

# "decrypt" = descriptografar
def decrypt(text, shift):
    # Descriptografar e criptografar com deslocamento negativo
    return encrypt(text, -shift)

# Testes
print(encrypt("Hello World!", 3))
print(decrypt("Khoor Zruog!", 3))
print(encrypt("Python 3.12", 5))
print(decrypt("Udymts 3.12", 5))
```

A sacada é que descriptografar é o mesmo que criptografar com deslocamento negativo. Se criptografamos com +3, descriptografamos com -3.

</details>


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


---

[← Voltar ao Módulo 5.16](cap05-mod16-algoritmos-conteudo.md)
