# 5.13 — Exercícios: Estrutura de um Programa Completo

[← Voltar ao conteúdo do módulo](cap05-mod13-estrutura-programa-conteudo.md)

---

## Orientações

- Use a estrutura completa em todos os exercícios: comentário inicial, constantes, funções, main(), ponto de entrada
- Separe funções de dados e funções de interface
- Nomes descritivos para tudo

---

## Exercício 1 — Refatorar o Jogo de Adivinhação

Pegue o jogo de adivinhação do módulo 5.10 e reorganize usando a estrutura completa:
- Constantes: `SECRET_NUMBER`, `MAX_ATTEMPTS`
- Funções: `get_guess()`, `check_guess()`, `show_result()`
- `main()` coordenando o fluxo
- Ponto de entrada `if __name__ == "__main__":`

---

## Exercício 2 — Lista de Tarefas (To-Do List)

Crie um programa completo de lista de tarefas com menu:
1. Adicionar tarefa
2. Listar tarefas (mostrando se está pendente ou concluída)
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair

Cada tarefa é um dicionário: `{"description": "...", "done": False}`.
Use a estrutura completa do módulo.

---

## Exercício 3 — Calculadora Científica

Crie uma calculadora com menu que oferece:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Potência
6. Raiz quadrada (use `number ** 0.5`)
7. Histórico de operações
8. Sair

Armazene o histórico em uma lista. Use funções para cada operação.

---

## Exercício 4 — Sistema de Votação

Crie um sistema de votação com:
- Lista de candidatos (constante)
- Função para votar (válida se o candidato existe)
- Função para mostrar resultados parciais
- Função para encerrar votação e mostrar vencedor
- Menu principal em main()

---

## Desafio Extra — Mini Sistema Bancário

Crie um sistema bancário simplificado:
- Cadastrar conta (nome, saldo inicial)
- Depositar
- Sacar (verificar saldo)
- Transferir entre contas
- Extrato (histórico de operações)
- Listar todas as contas

Use lista de dicionários para contas e para o histórico de cada conta.


---

## Exercício 5 — Refatorar Código Desorganizado — Nível: Intermediário

### Enunciado

O código abaixo funciona, mas está desorganizado. Refatore-o usando a estrutura completa: constantes no topo, funções de dados separadas das funções de interface, função `main()` e ponto de entrada.

```python
items = []
while True:
    print("1-Add 2-List 3-Quit")
    x = input("> ")
    if x == "1":
        n = input("Item: ")
        items.append(n)
        print("OK")
    elif x == "2":
        for i in items:
            print(f"- {i}")
    elif x == "3":
        break
```

### Dicas

1. Identifique as responsabilidades: dados (adicionar, listar) e interface (menu, input)
2. Crie constantes para as opções do menu
3. Cada função deve fazer uma coisa só
4. A função `main()` deve coordenar o fluxo
5. Use nomes descritivos em vez de `x`, `n`, `i`

### Proposta de Teste

- **Caso básico:** Adicionar "Leite" e "Pão", listar — deve mostrar ambos
- **Caso de borda:** Listar com lista vazia — deve mostrar mensagem adequada

### Resposta Comentada

```python
# ============================================
# Lista de Compras
# ============================================

# --- Constantes ---
MENU_OPTIONS = ["Adicionar item", "Listar itens", "Sair"]

# --- Funcoes de dados ---

# "add_item" = adicionar item
def add_item(items, name):
    items.append(name)

# --- Funcoes de interface ---

# "show_menu" = mostrar menu
def show_menu():
    print()
    for i, option in enumerate(MENU_OPTIONS, 1):
        print(f"  {i}. {option}")

# "show_items" = mostrar itens
def show_items(items):
    if len(items) == 0:
        print("  Lista vazia.")
        return
    for item in items:
        print(f"  - {item}")

# --- Funcao principal ---
def main():
    # "items" = lista de itens
    items = []
    while True:
        show_menu()
        # "choice" = escolha
        choice = input("\nOpcao: ")
        if choice == "1":
            name = input("Item: ").strip()
            if name:
                add_item(items, name)
                print(f"  '{name}' adicionado!")
        elif choice == "2":
            show_items(items)
        elif choice == "3":
            print("  Ate logo!")
            break

# --- Ponto de entrada ---
if __name__ == "__main__":
    main()
```

---

## Exercício 6 — Identificar Problemas — Nível: Básico

### Enunciado

Analise o código abaixo e liste todos os problemas de organização que encontrar. Não precisa corrigir — apenas identifique e explique por que cada um é um problema.

```python
contacts = []
MAX = 50
def f(n, p):
    contacts.append({"n": n, "p": p})
    print("ok")
while True:
    print("1-add 2-list 3-quit")
    x = input()
    if x == "1":
        f(input("name:"), input("phone:"))
    elif x == "2":
        for c in contacts:
            print(c)
    elif x == "3":
        break
```

### Dicas

1. Olhe para os nomes de variáveis e funções
2. Verifique se há separação entre dados e interface
3. A constante está sendo usada?
4. A função `f` mistura responsabilidades?
5. Tem função `main()`?

### Proposta de Teste

Identifique pelo menos 6 problemas. Compare com a lista da resposta.

### Resposta Comentada

Problemas encontrados:
1. `f()` — nome não descritivo (deveria ser `add_contact`)
2. `n`, `p` — parâmetros com nomes curtos (deveria ser `name`, `phone`)
3. `f()` usa variável global `contacts` em vez de receber como parâmetro
4. `f()` mistura dados (`append`) com interface (`print`)
5. `MAX = 50` definido mas nunca usado
6. Sem função `main()` — código roda solto
7. Sem ponto de entrada (`if __name__`)
8. `print(c)` mostra o dicionário bruto em vez de formatar
9. Sem validação de entrada
10. Sem comentários explicativos

---

[← Voltar ao conteúdo do módulo](cap05-mod13-estrutura-programa-conteudo.md)
