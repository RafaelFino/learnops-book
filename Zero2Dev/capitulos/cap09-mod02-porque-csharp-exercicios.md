# 9.2 — Exercícios: Por que C# e .NET?

[← Voltar ao conteúdo: Por que C# e .NET?](cap09-mod02-porque-csharp-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem os conceitos do módulo 9.2: a história e motivação do C#, a plataforma .NET, comparações com Python e C, tipos de dados e o modelo de compilação. São exercícios de pesquisa, reflexão e comparação — o código em C# começa no módulo 9.3.

---

## Exercício 1 — Pesquisa de Mercado

Acesse sites de vagas de emprego (LinkedIn, Glassdoor, Gupy, Indeed) e pesquise por vagas que pedem C# ou .NET. Anote:

1. Quantas vagas encontrou na sua região?
2. Quais são os requisitos mais comuns além de C# (banco de dados, frameworks, ferramentas)?
3. Qual a faixa salarial para júnior, pleno e sênior?
4. Que tipo de empresa contrata (jogos, fintech, consultoria, produto, etc.)?
5. Quantas vagas mencionam .NET Core ou .NET 6+ especificamente?

Compare com uma pesquisa similar para Python. Qual linguagem tem mais vagas na sua região? Qual paga melhor?

---

## Exercício 2 — Tradução de Tipos

Para cada trecho de código Python abaixo, reescreva usando a sintaxe de declaração de variáveis do C# (com tipo explícito):

```python
# Trecho 1
name = "João"
age = 25
height = 1.75
is_student = True

# Trecho 2
product_name = "Notebook"
product_price = 3499.90
quantity_in_stock = 42
is_available = True

# Trecho 3
city = "São Paulo"
population = 12300000
area_km2 = 1521.11
is_capital = False
```

Dica: use `string` para texto, `int` para inteiros, `double` para decimais gerais, `decimal` para dinheiro, e `bool` para verdadeiro/falso.

Pergunta extra: no Trecho 2, por que `product_price` deveria ser `decimal` em vez de `double`?

---

## Exercício 3 — Jogos com Unity

Pesquise 5 jogos que foram feitos com Unity (e portanto usam C#). Para cada jogo, anote:

1. Nome do jogo
2. Plataformas onde roda (PC, mobile, console)
3. Estúdio que desenvolveu
4. Ano de lançamento
5. Se é indie ou de uma grande empresa

Depois responda: qual desses jogos você já jogou ou conhece? Saber que foi feito com C# muda sua percepção sobre a linguagem?

---

## Exercício 4 — Fluxo de Compilação

Desenhe (em papel ou texto) o fluxo completo de compilação e execução para cada linguagem:

1. **Python**: `programa.py` → ??? → resultado
2. **C**: `programa.c` → ??? → resultado
3. **C#**: `Programa.cs` → ??? → ??? → resultado

Para cada etapa, explique com suas palavras:
- O que entra?
- O que sai?
- Quem faz a transformação?
- Quando os erros são detectados?

Qual modelo detecta mais erros antes do programa rodar? Por quê?

---

## Exercício 5 — Tipos de Dados na Prática

Para cada valor abaixo, diga qual tipo C# você usaria e justifique sua escolha:

1. O nome completo de um cliente → `___` porque...
2. A idade de uma pessoa → `___` porque...
3. O preço de um produto em reais → `___` porque...
4. Se um usuário está ativo ou não → `___` porque...
5. O saldo de uma conta bancária → `___` porque...
6. A quantidade de itens em estoque → `___` porque...
7. A temperatura em graus Celsius → `___` porque...
8. O CPF de uma pessoa (com pontos e traço) → `___` porque...
9. O número de habitantes de um país → `___` porque...
10. A nota de um aluno (0.0 a 10.0) → `___` porque...

Atenção especial: por que o CPF deve ser `string` e não `long`, mesmo sendo composto de números?

---

## Exercício 6 — Comparação de Ecossistemas

Complete a tabela comparando os ecossistemas das três linguagens:

| Aspecto | Python | C | C# |
|---------|--------|---|-----|
| Gerenciador de pacotes | pip | ... | ... |
| Repositório de pacotes | PyPI | ... | ... |
| Ferramenta de build | ... | gcc/make | ... |
| IDE mais popular | ... | ... | ... |
| Framework web principal | Django/Flask | ... | ... |
| Comando para rodar | `python3 arquivo.py` | ... | ... |

---

## Exercício 7 — Timeline do .NET

Sem consultar o módulo, tente preencher os marcos da evolução do .NET:

1. 2000 — O que foi lançado? Qual a limitação principal?
2. 2005 — Qual funcionalidade importante foi adicionada ao C# 2.0?
3. 2016 — O que mudou radicalmente na plataforma .NET?
4. 2020 — O que foi unificado?
5. 2024 — Qual é a versão atual do .NET?

Depois confira suas respostas com o módulo. Quantas você acertou?

---

## Exercício 8 — Reflexão: Por que uma Nova Linguagem?

Escreva um parágrafo de 5-8 linhas respondendo: "Por que aprender C# em vez de continuar usando Python para aprender OOP?"

Use pelo menos 3 argumentos do módulo, mas escreva com suas palavras. Considere:
- A questão da tipagem (dinâmica vs estática)
- A questão do encapsulamento (convenção vs enforcement)
- A questão do mercado de trabalho
- A questão da transferência de conhecimento para outras linguagens

---

## Exercício 9 — Anders Hejlsberg

Pesquise sobre Anders Hejlsberg e responda:

1. Em que país ele nasceu?
2. Quais linguagens de programação ele criou? (Liste pelo menos 3)
3. Em que empresa ele trabalha?
4. Por que ele é considerado um dos maiores designers de linguagens da história?

Curiosidade: tente encontrar uma palestra ou entrevista dele no YouTube. Ouvir o criador da linguagem falar sobre suas decisões de design é uma experiência única.

---

## Exercício 10 — Mapa Mental

Crie um mapa mental (em papel ou ferramenta digital) com C# no centro e ramificações para:

1. **História**: quem criou, quando, por quê
2. **Características**: tipagem, compilação, GC, OOP
3. **Onde é usado**: jogos, web, desktop, mobile, cloud
4. **Comparação**: vs Python, vs C, vs Java
5. **Ecossistema**: .NET, NuGet, dotnet CLI, IDEs

Esse mapa vai servir como referência rápida ao longo de todo o capítulo 9.

---

## Exercício 11 — Vantagens e Desvantagens

Para cada linguagem (Python, C, C#), liste pelo menos 3 vantagens e 3 desvantagens. Depois responda: em qual cenário cada linguagem seria a melhor escolha?

| Linguagem | Vantagens | Desvantagens | Melhor cenário |
|-----------|-----------|-------------|----------------|
| Python | 1. ... 2. ... 3. ... | 1. ... 2. ... 3. ... | ... |
| C | 1. ... 2. ... 3. ... | 1. ... 2. ... 3. ... | ... |
| C# | 1. ... 2. ... 3. ... | 1. ... 2. ... 3. ... | ... |

---

## Exercício 12 — Erros em Compilação vs Runtime

Explique com suas palavras a diferença entre:
1. Um erro detectado em tempo de compilação (compile-time error)
2. Um erro detectado em tempo de execução (runtime error)

Dê um exemplo de cada tipo. Qual é mais perigoso em um sistema em produção? Por quê?

Agora pense: em Python, a maioria dos erros de tipo são detectados quando? E em C#? Qual abordagem é mais segura para sistemas críticos (bancos, hospitais, aviação)?

---

[← Voltar ao conteúdo: Por que C# e .NET?](cap09-mod02-porque-csharp-conteudo.md)
