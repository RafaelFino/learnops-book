# Exercícios de Lógica — Parte 1: Validação de Dados

[<- Voltar ao Módulo 16](16-exercícios-lógica.md) | [Glossário](00-glossário.md) | [Parte 2 ->](16-exercícios-lógica-parte2.md)

> **Como testar:** Salve na pasta `~/meus-projetos/python-curso/modulo-16/` e execute com `python3 nome_do_arquivo.py`.

---

## Exercício 1 — Validar Idade — Nível: Básico
**Conceitos praticados:** condicionais, comparação, input/output

### Enunciado
Crie uma função `validate_age` que receba uma idade e retorne True se for valida (entre 0 e 150) ou False caso contrario. Peca a idade ao usuario e exiba se e valida.

### Dicas
- Use `and` para combinar duas condições: `age >= 0 and age <= 150`
- Trate o caso de números negativos

### Proposta de Teste
- Idade: `25` — Saida: `Idade valida`
- Idade: `-5` — Saida: `Idade invalida`
- Idade: `200` — Saida: `Idade invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que valida se a idade esta no intervalo aceitavel
# "validate_age" = validar idade
# "age" = idade
def validate_age(age):
    # Retorna True se a idade estiver entre 0 e 150 (inclusive)
    # and = E — ambas as condicoes precisam ser verdadeiras
    return age >= 0 and age <= 150

# Pedimos a idade ao usuario e convertemos para inteiro
# "user_age" = idade do usuario
user_age = int(input("Digite sua idade: "))

# Verificamos se e valida usando a funcao
if validate_age(user_age):
    print("Idade valida!")
else:
    print("Idade invalida! Digite um valor entre 0 e 150.")
```

---

## Exercício 2 — Validar Nota — Nível: Básico
**Conceitos praticados:** condicionais, funções, comparação

### Enunciado
Crie uma função `validate_grade` que receba uma nota e retorne True se estiver entre 0 e 10. Peca a nota ao usuario e, se for valida, classifique: Aprovado (>= 7), Recuperacao (>= 5), Reprovado (< 5).

### Dicas
- Primeiro valide, depois classifique
- Use if/elif/else para a classificação

### Proposta de Teste
- Nota: `8.5` — Saida: `Aprovado`
- Nota: `5.0` — Saida: `Recuperacao`
- Nota: `3.0` — Saida: `Reprovado`
- Nota: `11` — Saida: `Nota invalida`

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que valida se a nota esta no intervalo 0-10
# "validate_grade" = validar nota
# "grade" = nota
def validate_grade(grade):
    # Retorna True se a nota estiver entre 0 e 10
    return grade >= 0 and grade <= 10

# Pedimos a nota ao usuario
# "student_grade" = nota do aluno
student_grade = float(input("Digite a nota (0 a 10): "))

# Primeiro verificamos se a nota e valida
if validate_grade(student_grade):
    # Nota valida — classificamos
    if student_grade >= 7:
        # Nota 7 ou mais = aprovado
        print("Aprovado!")
    elif student_grade >= 5:
        # Nota 5 a 6.9 = recuperacao
        print("Recuperacao")
    else:
        # Nota abaixo de 5 = reprovado
        print("Reprovado")
else:
    # Nota fora do intervalo valido
    print("Nota invalida! Digite um valor entre 0 e 10.")
```

---

## Exercício 3 — Validar CPF (Formato) — Nível: Intermediario
**Conceitos praticados:** strings, len(), condicionais, funções

### Enunciado
Crie uma função `validate_cpf_format` que receba um CPF como texto (apenas números, sem pontos ou tracos) e retorne True se tiver exatamente 11 digitos numericos.

### Dicas
- Use `len()` para verificar o tamanho
- Use `.isdigit()` para verificar se sao todos números

### Proposta de Teste
- CPF: `12345678900` — Saida: `Formato valido`
- CPF: `1234` — Saida: `Formato invalido` (menos de 11 digitos)
- CPF: `1234567890a` — Saida: `Formato invalido` (contem letra)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que valida o formato do CPF
# "validate_cpf_format" = validar formato do CPF
# "cpf" = o CPF como texto
def validate_cpf_format(cpf):
    # Verificamos duas condicoes:
    # 1. Tem exatamente 11 caracteres (len = length = comprimento)
    # 2. Todos os caracteres sao digitos numericos (isdigit = e digito)
    # and = E — ambas precisam ser verdadeiras
    return len(cpf) == 11 and cpf.isdigit()

# Pedimos o CPF ao usuario
# "user_cpf" = CPF do usuario
user_cpf = input("Digite o CPF (apenas numeros, 11 digitos): ")

# Verificamos o formato
if validate_cpf_format(user_cpf):
    print("Formato valido!")
else:
    print("Formato invalido! O CPF deve ter exatamente 11 digitos numericos.")
```

---

## Exercício 4 — Validar Senha — Nível: Intermediario
**Conceitos praticados:** strings, loops, condicionais, funções

### Enunciado
Crie uma função `validate_password` que receba uma senha e verifique se atende aos critérios: pelo menos 8 caracteres, pelo menos uma letra e pelo menos um número. Retorne True se atender a todos.

### Dicas
- Use `len()` para o tamanho
- Percorra cada caractere com `for` e verifique com `.isalpha()` (e letra) e `.isdigit()` (e número)

### Proposta de Teste
- Senha: `abc12345` — Saida: `Senha valida`
- Senha: `abc` — Saida: `Senha invalida` (muito curta)
- Senha: `abcdefgh` — Saida: `Senha invalida` (sem número)
- Senha: `12345678` — Saida: `Senha invalida` (sem letra)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que valida a forca da senha
# "validate_password" = validar senha
# "password" = senha
def validate_password(password):
    # Verificamos o tamanho minimo
    if len(password) < 8:
        # Senha muito curta — retorna False imediatamente
        return False

    # Verificamos se tem pelo menos uma letra e um numero
    # "has_letter" = tem letra, "has_number" = tem numero
    has_letter = False
    has_number = False

    # Percorremos cada caractere da senha
    for char in password:
        # "char" = caractere
        # .isalpha() retorna True se for uma letra (a-z, A-Z)
        if char.isalpha():
            has_letter = True
        # .isdigit() retorna True se for um digito (0-9)
        if char.isdigit():
            has_number = True

    # A senha e valida se tiver letra E numero
    return has_letter and has_number

# Pedimos a senha ao usuario
# "user_password" = senha do usuario
user_password = input("Digite uma senha: ")

# Verificamos a senha
if validate_password(user_password):
    print("Senha valida!")
else:
    print("Senha invalida! A senha deve ter pelo menos 8 caracteres, uma letra e um numero.")
```

---

## Exercício 5 — Validar Email (Simplificado) — Nível: Avancado
**Conceitos praticados:** strings, in, condicionais, funções, lógica composta

### Enunciado
Crie uma função `validate_email` que receba um email e verifique se: contem exatamente um `@`, tem pelo menos um caractere antes do `@`, e tem pelo menos um `.` depois do `@`.

### Dicas
- Use `.count("@")` para contar quantos `@` existem
- Use `.find("@")` para encontrar a posição do `@`
- Use fatiamento para pegar a parte depois do `@`

### Proposta de Teste
- Email: `usuario@email.com` — Saida: `Email valido`
- Email: `usuario` — Saida: `Email invalido` (sem @)
- Email: `@email.com` — Saida: `Email invalido` (nada antes do @)
- Email: `usuario@email` — Saida: `Email invalido` (sem ponto depois do @)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```python
# Funcao que valida o formato basico de um email
# "validate_email" = validar email
# "email" = endereco de email
def validate_email(email):
    # Verificacao 1: deve ter exatamente um @
    # count("@") conta quantas vezes @ aparece
    if email.count("@") != 1:
        return False

    # Encontramos a posicao do @
    # "at_position" = posicao do @ (at = arroba em ingles)
    at_position = email.find("@")

    # Verificacao 2: deve ter pelo menos um caractere antes do @
    # Se a posicao do @ for 0, nao tem nada antes
    if at_position == 0:
        return False

    # Verificacao 3: deve ter pelo menos um ponto depois do @
    # Pegamos a parte depois do @ usando fatiamento
    # "after_at" = parte depois do @
    after_at = email[at_position + 1:]

    # Verificamos se tem pelo menos um ponto na parte depois do @
    if "." not in after_at:
        return False

    # Se passou por todas as verificacoes, o email e valido
    return True

# Pedimos o email ao usuario
# "user_email" = email do usuario
user_email = input("Digite seu email: ")

# Verificamos o email
if validate_email(user_email):
    print("Email valido!")
else:
    print("Email invalido! Verifique o formato (exemplo: usuario@email.com)")
```

---

[<- Voltar ao Módulo 16](16-exercícios-lógica.md) | [Parte 2 — Processamento de Listas ->](16-exercícios-lógica-parte2.md)
