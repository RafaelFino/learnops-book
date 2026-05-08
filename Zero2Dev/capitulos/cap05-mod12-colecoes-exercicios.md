# 5.12 — Exercícios: Coleções

[← Voltar ao conteúdo do módulo](cap05-mod12-colecoes-conteudo.md)

---

## Orientações

- Resolva cada exercício em um arquivo separado
- Use funções para organizar seu código (módulo 5.11)
- Teste com diferentes dados para garantir que funciona

---

## Exercício 1 — Lista de Compras Interativa

Crie um programa com menu que permite:
1. Adicionar item à lista
2. Remover item da lista
3. Mostrar lista completa
4. Buscar item na lista
5. Sair

Use `while True` para o menu e funções para cada operação.

---

## Exercício 2 — Cadastro de Alunos

Crie um programa que cadastra alunos em uma lista de dicionários. Cada aluno tem: nome, idade e 3 notas. O programa deve:
1. Pedir dados de 3 alunos
2. Calcular a média de cada aluno
3. Exibir um relatório com nome, média e situação (aprovado/reprovado)

**Dica:** Use uma função `calculate_average(grades)` que recebe uma lista de notas.

---

## Exercício 3 — Contador de Palavras

Crie um programa que recebe uma frase do usuário e conta quantas vezes cada palavra aparece, usando um dicionário.

**Exemplo:** "o gato viu o rato e o rato viu o gato"
**Saída:** `{'o': 4, 'gato': 2, 'viu': 2, 'rato': 2, 'e': 1}`

**Dica:** Use `frase.split()` para separar as palavras e um dicionário para contar.

---

## Exercício 4 — Agenda Telefônica

Crie uma agenda telefônica com menu:
1. Adicionar contato (nome e telefone)
2. Buscar contato por nome
3. Remover contato
4. Listar todos os contatos
5. Sair

Armazene os contatos em um dicionário onde a chave é o nome e o valor é o telefone.

---

## Exercício 5 — Estoque de Produtos

Crie um sistema de estoque usando lista de dicionários. Cada produto tem: nome, preço e quantidade. O programa deve:
1. Cadastrar produtos
2. Listar produtos com valor total (preço x quantidade)
3. Buscar produto por nome
4. Atualizar quantidade de um produto
5. Mostrar valor total do estoque

---

## Exercício 6 — Notas e Estatísticas

Crie um programa que pede 10 notas ao usuário e armazena em uma lista. Depois calcule e exiba:
- Maior nota
- Menor nota
- Média das notas
- Quantas notas acima da média
- Lista ordenada das notas

**Dica:** Use `max()`, `min()`, `sum()`, `len()` e `sort()`.

---

## Exercício 7 — Tradutor Simples

Crie um dicionário com 10 palavras em português como chaves e suas traduções em inglês como valores. Crie um programa que pede uma palavra ao usuário e mostra a tradução. Se a palavra não existir, mostre "Palavra não encontrada".

---

## Desafio Extra — Jogo de Quiz

Crie um jogo de quiz usando uma lista de dicionários. Cada pergunta é um dicionário com: pergunta, alternativas (lista) e resposta correta (índice). O programa faz 5 perguntas, conta os acertos e mostra o resultado final.


---

## Exercício 6 — Agenda de Contatos com Dicionários — Nível: Intermediário

### Enunciado

Crie um programa que gerencia uma agenda de contatos usando uma lista de dicionários. Cada contato tem nome, telefone e email. O programa deve permitir: adicionar contato, listar todos, buscar por nome (parcial, case-insensitive) e remover por nome.

### Dicas

1. Cada contato é um dicionário: `{"name": "Maria", "phone": "99999-1111", "email": "maria@email.com"}`
2. A lista de contatos é uma lista de dicionários
3. Para busca parcial, use `search.lower() in contact["name"].lower()`
4. Para remover, encontre o índice e use `pop()`

### Proposta de Teste

- **Caso básico:** Adicionar "Maria" e "Pedro", buscar "mar" → encontra Maria
- **Caso de borda:** Buscar nome que não existe → mensagem "não encontrado"
- **Caso de borda:** Remover de lista vazia → mensagem adequada

---

## Exercício 7 — Estatísticas de Notas com Tuplas — Nível: Avançado

### Enunciado

Crie um programa que recebe notas de alunos como tuplas `(nome, nota1, nota2, nota3)` e calcula: média de cada aluno, maior e menor média da turma, quantidade de aprovados (média >= 7) e reprovados, e o aluno com a maior média.

### Dicas

1. Use uma lista de tuplas: `[("Ana", 8, 7, 9), ("Pedro", 5, 6, 4)]`
2. Para calcular a média de uma tupla: `sum(aluno[1:]) / 3`
3. Use variáveis para rastrear maior e menor média
4. Conte aprovados e reprovados com contadores

### Proposta de Teste

- **Caso básico:** 3 alunos com notas variadas → médias corretas, aprovados/reprovados corretos
- **Caso de borda:** Todos aprovados → reprovados = 0
- **Caso de borda:** Empate na maior média → mostrar qualquer um dos empatados




### Resposta Comentada (estrutura)

```python
# "students" = alunos (lista de tuplas)
students = [
    ("Ana", 8, 7, 9),
    ("Pedro", 5, 6, 4),
    ("Maria", 10, 9, 8)
]

# "approved" = aprovados, "failed" = reprovados
approved = 0
failed = 0
# "best_student" = melhor aluno
best_student = ""
# "best_average" = melhor media
best_average = 0

for student in students:
    # "name" = nome
    name = student[0]
    # "average" = media (soma das 3 notas dividido por 3)
    average = sum(student[1:]) / 3
    print(f"{name}: media {average:.1f}")
    if average >= 7:
        approved += 1
    else:
        failed += 1
    if average > best_average:
        best_average = average
        best_student = name

print(f"\nAprovados: {approved}")
print(f"Reprovados: {failed}")
print(f"Melhor aluno: {best_student} (media {best_average:.1f})")
```

Saida esperada:

```
Ana: media 8.0
Pedro: media 5.0
Maria: media 9.0

Aprovados: 2
Reprovados: 1
Melhor aluno: Maria (media 9.0)
```


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

[← Voltar ao conteúdo do módulo](cap05-mod12-colecoes-conteudo.md)
