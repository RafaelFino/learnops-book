# 5.18 — Exercícios: Usando IA para Aprender

[← Voltar ao Módulo 5.18](cap05-mod18-ia-para-programacao-conteudo.md)

---

## Como usar estes exercícios

Estes exercícios são diferentes dos anteriores — em vez de escrever código, você vai praticar a habilidade de se comunicar com IA. Use qualquer ferramenta de IA disponível (ChatGPT, Claude, Gemini, Kiro).

---

## Exercício 1 — Melhorar prompts (Nível: Fácil)

Para cada prompt vago abaixo, reescreva de forma específica e contextualizada:

### Prompt A (vago)
```
Me ajuda com Python
```

### Prompt B (vago)
```
Meu código não funciona
```

### Prompt C (vago)
```
Explica funções
```

### Prompt D (vago)
```
Faz um programa de cadastro
```

### Prompt E (vago)
```
O que é bug?
```


### Respostas Sugeridas

<details>
<summary>Clique para ver as respostas</summary>

**Prompt A melhorado:**
"Estou aprendendo Python e tenho dúvida sobre como percorrer uma lista de dicionários. Tenho uma lista de alunos onde cada aluno é um dicionário com 'nome' e 'nota'. Como faço para imprimir apenas os alunos com nota acima de 7? Mostre um exemplo com comentários em português."

**Prompt B melhorado:**
"Estou recebendo este erro no Python: TypeError: can only concatenate str (not 'int') to str. Meu código é: `print('Idade: ' + idade)` onde `idade = 25`. O que está causando o erro e como corrijo?"

**Prompt C melhorado:**
"Explique funções em Python para um iniciante. Cubra: o que são, por que usar, como criar com def, parâmetros, return, e dê 3 exemplos progressivos (simples, médio, com múltiplos parâmetros). Comentários em português."

**Prompt D melhorado:**
"Crie uma função Python que cadastra produtos em uma lista de dicionários. Cada produto tem: nome (texto, não pode ser vazio), preço (float, positivo) e quantidade (int, >= 0). A função deve validar todos os campos e usar try/except para tratar erros de entrada. Nomes de variáveis em inglês com comentários em português."

**Prompt E melhorado:**
"Explique o que é um bug em programação, de onde vem o termo, quais são os 3 tipos de bugs (sintaxe, execução, lógica) e dê um exemplo de cada tipo em Python. Use linguagem simples para iniciantes."

</details>

---

## Exercício 2 — Aprender um conceito novo (Nível: Médio)

Escolha UM dos conceitos abaixo (que não foram cobertos em profundidade no curso) e use IA para aprender:

- List comprehension em Python
- A função `enumerate()` em Python
- F-strings avançadas (formatação de números, alinhamento)
- A função `zip()` para combinar listas
- O operador ternário em Python

**Tarefa:**
1. Peça à IA para explicar o conceito com exemplos
2. Peça 2 exercícios práticos sobre o conceito
3. Resolva os exercícios
4. Peça à IA para revisar suas soluções

**Documente o processo:** anote qual prompt usou, o que aprendeu e o que faria diferente.

---

## Exercício 3 — Debugging assistido por IA (Nível: Difícil)

O programa abaixo tem 3 bugs. Em vez de corrigi-los sozinho, use IA de forma inteligente:

```python
# Programa com 3 bugs — use IA para ajudar a encontrar
def calculate_statistics(numbers):
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    
    max_val = numbers[0]
    min_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
        if num < max_val:  # Bug 1
            min_val = num
    
    return {
        "total": total,
        "average": average,
        "max": max_val,
        "min": min_val,
        "count": len(numbers)
    }

data = []  # Bug 2 — lista vazia
stats = calculate_statistics(data)
print(f"Estatisticas: {stats}")

data2 = [10, 5, 8, "3", 7]  # Bug 3 — tipo errado
stats2 = calculate_statistics(data2)
print(f"Estatisticas: {stats2}")
```

**Regras:**
1. NÃO peça à IA para corrigir o código inteiro
2. Descreva cada bug que encontrou e peça uma DICA de como corrigir
3. Implemente a correção você mesmo
4. Depois de corrigir, peça à IA para revisar sua solução

**Documente:** para cada bug, anote o prompt que usou e a dica que recebeu.

### Respostas Comentadas

<details>
<summary>Clique para ver as respostas</summary>

**Bug 1:** Na linha `if num < max_val:`, deveria ser `if num < min_val:`. O código compara com `max_val` em vez de `min_val`, então o mínimo nunca é atualizado corretamente.

**Bug 2:** A lista `data` está vazia. Quando a função tenta `average = total / len(numbers)`, dá `ZeroDivisionError` porque `len([])` é 0. Correção: adicionar verificação `if len(numbers) == 0: return None` no início da função.

**Bug 3:** A lista `data2` contém a string `"3"` em vez do número `3`. Quando o loop tenta `total += num` com `"3"`, dá `TypeError`. Correção: converter para número ou validar os tipos antes de processar.

</details>



---

## Exercicio 5 — Avaliar Resposta da IA — Nivel: Intermediario

### Enunciado

Peca a uma IA para escrever uma funcao Python que verifica se um numero e primo. Analise a resposta: o codigo esta correto? Tem algum bug? Funciona para casos de borda (0, 1, 2, numeros negativos)? Escreva sua analise em um comentario no topo do arquivo.

### Dicas

1. Teste o codigo da IA com: 0, 1, 2, 3, 4, 17, -5
2. Um numero primo e divisivel apenas por 1 e por ele mesmo
3. 0 e 1 NAO sao primos — a IA trata isso?
4. Numeros negativos NAO sao primos — a IA trata isso?

### Proposta de Teste

- Execute o codigo da IA com os valores acima
- Documente quais casos funcionam e quais falham
- Se encontrar bugs, corrija e explique a correcao


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


### Exercício Extra: Comparando Prompts

Teste os dois prompts abaixo com uma IA e compare as respostas:

**Prompt vago:**
> "Me explica Python"

**Prompt específico:**
> "Explique a diferença entre lista e tupla em Python, com um exemplo prático de quando usar cada uma. Mostre o código com comentários em português."

Anote as diferenças:
- Qual resposta foi mais útil?
- Qual tinha exemplos de código?
- Qual você conseguiu aplicar imediatamente?

**Reflexão:** A qualidade da resposta da IA depende diretamente da qualidade do prompt. Quanto mais contexto e especificidade você fornecer, melhor será o resultado. Isso vale para qualquer ferramenta de IA, não apenas para programação.

### Checklist de um Bom Prompt para Programação

| Elemento | Exemplo |
|----------|---------|
| Linguagem | "em Python 3" |
| Nível | "para iniciante" |
| Formato | "com comentários em português" |
| Contexto | "estou aprendendo sobre listas" |
| Saída esperada | "mostre a saída esperada do código" |
| Restrições | "sem usar bibliotecas externas" |

---

[← Voltar ao Módulo 5.18](cap05-mod18-ia-para-programacao-conteudo.md)
