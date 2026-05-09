# 02 — Diferenças entre Scripts, Compilados e VM

[← Anterior: Introdução à Programação](01-introducao-programacao.md) · [Glossário](00-glossario.md) · [Próximo: Preparação do Ambiente →](03-preparacao-ambiente.md)

---

## Introdução

No módulo anterior, você aprendeu que um programa é um conjunto de instruções escritas em uma linguagem de programação. Mas como o computador entende essas instruções? Afinal, ele só entende zeros e uns (linguagem de máquina).

Neste módulo, vamos entender as **três formas principais** de transformar código escrito por humanos em algo que o computador consiga executar. Não se preocupe em decorar tudo — o objetivo é entender o contexto geral e saber onde o Python se encaixa.

---

## O Problema: Humanos vs Máquinas

Imagine que você escreveu uma carta em português e precisa enviá-la para alguém que só fala japonês. Você tem três opções:

1. **Traduzir a carta inteira** antes de enviar (o destinatário recebe tudo traduzido de uma vez)
2. **Contratar um tradutor simultâneo** que traduz frase por frase na hora da leitura
3. **Traduzir para um idioma intermediário** que um assistente bilíngue consegue ler e traduzir para japonês

Essas três opções correspondem exatamente às três formas de executar programas:

---

## 1. Programas Compilados

Um [compilador](00-glossario-a-d.md#compilador) traduz **todo o código de uma vez** para linguagem de máquina, antes de executar. O resultado é um arquivo executável que o computador roda diretamente.

**Analogia:** É como traduzir um livro inteiro para outro idioma antes de publicá-lo. O processo de tradução demora, mas depois o livro pode ser lido rapidamente por qualquer pessoa que fale aquele idioma.

**Exemplos de linguagens compiladas:**
- **C** — usada para criar sistemas operacionais (como o Linux!)
- **C++** — usada em jogos e programas que precisam de alta velocidade
- **Go** — usada em servidores e ferramentas de infraestrutura

**Vantagens:**
- Programas compilados são muito rápidos na execução
- O código-fonte não precisa estar presente para executar

**Desvantagens:**
- Precisa compilar (traduzir) toda vez que faz uma alteração no código
- O programa compilado funciona apenas no sistema operacional para o qual foi compilado

---

## 2. Scripts (Programas Interpretados)

Um [interpretador](00-glossario-e-i.md#interpretador) lê e executa o código **linha por linha**, na hora, sem precisar traduzir tudo antes. O código-fonte é o próprio programa.

**Analogia:** É como ter um tradutor simultâneo ao seu lado que traduz cada frase na hora em que você fala. Não precisa esperar a tradução do texto inteiro — a comunicação acontece em tempo real.

**Exemplos de linguagens interpretadas:**
- **Python**  — a linguagem que vamos usar neste curso!
- **JavaScript** — usada em sites e aplicações web
- **Ruby** — usada em desenvolvimento web

**Vantagens:**
- Não precisa compilar — você escreve o código e executa na hora
- Ótimo para aprender, porque você vê o resultado imediatamente
- Funciona em qualquer sistema que tenha o interpretador instalado

**Desvantagens:**
- Geralmente mais lento que programas compilados (porque traduz na hora)
- Precisa ter o interpretador instalado no computador

### Por que Python é interpretado?

Python foi criado com foco em **simplicidade e produtividade**. Ser interpretado significa que você pode:

- Escrever uma linha de código e ver o resultado imediatamente
- Testar ideias rapidamente sem esperar compilação
- Focar no aprendizado sem se preocupar com processos complexos

Para iniciantes, isso é uma grande vantagem: você escreve, executa e vê o resultado na hora.

---

## 3. Programas em Máquina Virtual (VM)

Algumas linguagens usam uma abordagem intermediária: o código é compilado para um formato intermediário chamado [bytecode](00-glossario-a-d.md#bytecode), que é executado por uma **máquina virtual** — um programa que simula um computador dentro do computador.

**Analogia:** É como traduzir um livro para um idioma universal (esperanto, por exemplo) que um assistente especial consegue ler e traduzir para qualquer outro idioma. O livro é traduzido uma vez para o idioma intermediário, e depois o assistente (máquina virtual) traduz para o idioma do computador.

**Exemplos:**
- **Java** — usa a JVM ([Java Virtual Machine](00-glossario-j-p.md#jvm-java-virtual-machine))
- **C#** — usa o [.NET](00-glossario-j-p.md#net) (CLR — Common Language Runtime)

**Vantagens:**
- O mesmo programa roda em diferentes sistemas operacionais (Windows, Linux, Mac) sem recompilar
- Boa velocidade de execução

**Desvantagens:**
- Precisa ter a máquina virtual instalada
- Processo de desenvolvimento um pouco mais complexo que linguagens interpretadas

---

## Comparação Resumida

| Característica | Compilado (C) | Interpretado (Python) | VM (Java) |
|---------------|--------------|----------------------|-----------|
| Como executa | Traduz tudo antes | Traduz linha por linha | Traduz para bytecode + VM |
| Velocidade | Muito rápido | Mais lento | Rápido |
| Facilidade | Mais complexo | Mais simples | Intermediário |
| Precisa instalar | Compilador | Interpretador | Máquina Virtual |
| Ideal para | Sistemas, jogos | Aprendizado, automação, dados | Empresas, Android |

---

## Onde o Python se Encaixa?

O Python é uma linguagem **interpretada** (script). Isso significa que:

1. Você escreve o código em um arquivo `.py`
2. O interpretador Python lê o arquivo linha por linha
3. Cada linha é executada na hora

Para você, como estudante, isso é ótimo: basta escrever o código, salvar e executar. Sem etapas extras de compilação.

> **Nota:** Na prática, o Python faz uma compilação interna para bytecode (arquivos `.pyc`), mas isso acontece automaticamente e você não precisa se preocupar com isso. Para todos os efeitos práticos, Python funciona como uma linguagem interpretada.

---

## Não Se Preocupe com Isso no Dia a Dia

Este módulo é para você entender o **contexto geral** de como programas funcionam. No dia a dia do curso, você não precisa pensar sobre compilação, interpretação ou máquinas virtuais.

O que importa é: você vai escrever código Python, salvar em um arquivo e executar no terminal. Simples assim.

Nos próximos módulos, vamos preparar seu computador para fazer exatamente isso.

---

## Para Saber Mais

-  [W3Schools — Python Introduction](https://www.w3schools.com/python/python_intro.asp) — _Por que Python e como ele funciona_
-  [Documentação Oficial Python](https://docs.python.org/pt-br/3/tutorial/index.html) — _Tutorial oficial em português_

---

## Perguntas Frequentes (FAQ)

**P: Preciso entender compilação para programar em Python?**
R: Não! Python é interpretado, então você não precisa se preocupar com compilação. Basta escrever o código e executar.

**P: Python é lento por ser interpretado?**
R: Para o que vamos fazer neste curso (e para a maioria das aplicações), a velocidade do Python é mais que suficiente. A "lentidão" só é relevante em casos muito específicos de alto desempenho.

**P: O que é melhor: compilado ou interpretado?**
R: Não existe "melhor" — cada abordagem tem suas vantagens. Para aprender programação, linguagens interpretadas como Python são ideais porque permitem ver resultados imediatamente.

**P: Vou precisar aprender Java ou C também?**
R: Não neste curso. Mencionamos essas linguagens apenas para contexto. Aprender Python é um excelente primeiro passo, e os conceitos que você aprende aqui se aplicam a qualquer linguagem no futuro.

**P: O que são esses arquivos .pyc que às vezes aparecem?**
R: São arquivos de bytecode que o Python cria automaticamente para acelerar a execução. Você pode ignorá-los completamente — o Python cuida disso sozinho.

**P: O que é bytecode?**
R: É um formato intermediário entre o código que você escreve e a linguagem de máquina. O Python converte seu código para bytecode automaticamente — você não precisa fazer nada.

**P: Posso criar jogos com Python?**
R: Sim! Existem bibliotecas como Pygame que permitem criar jogos 2D. Mas para jogos profissionais 3D, outras linguagens como C++ são mais comuns.

**P: O que é uma máquina virtual (VM)?**
R: É um programa que simula um computador dentro do computador. A JVM (Java Virtual Machine) é um exemplo — ela permite que programas Java rodem em qualquer sistema operacional.

**P: Por que existem tantas linguagens de programação?**
R: Cada linguagem foi criada para resolver tipos diferentes de problemas. Algumas são melhores para velocidade, outras para facilidade de uso, outras para áreas específicas como web ou dados.

**P: Python pode ser compilado?**
R: Existem ferramentas que compilam Python (como Cython), mas isso é avançado e não é necessário para este curso. Na prática, Python funciona como linguagem interpretada.

**P: O que significa "código-fonte"?**
R: É o texto que o programador escreve — as instruções em linguagem de programação. É o arquivo `.py` que você cria no VSCode.

**P: O que é "linguagem de máquina"?**
R: São instruções em formato binário (zeros e uns) que o processador do computador entende diretamente. Humanos não escrevem em linguagem de máquina — usamos linguagens de programação que são traduzidas para ela.

**P: Preciso entender como o computador funciona por dentro?**
R: Não para este curso. Entender o básico (que o computador segue instruções) é suficiente. Detalhes de hardware e arquitetura são temas para cursos mais avançados.

**P: O que é um "framework"?**
R: É um conjunto de ferramentas prontas que facilitam o desenvolvimento. Neste curso, vamos usar o FastAPI, que é um framework para criar APIs web. Pense nele como um kit de construção com peças pré-fabricadas.

**P: Qual a diferença entre programa e aplicativo?**
R: Na prática, são a mesma coisa. "Aplicativo" (ou "app") é o termo mais usado para programas de celular ou programas com interface gráfica. "Programa" é o termo mais geral.

**P: O que é "open source" (código aberto)?**
R: Significa que o código-fonte é público — qualquer pessoa pode ver, usar e contribuir. Python é open source.

**P: Posso misturar linguagens em um projeto?**
R: Sim! Projetos grandes frequentemente usam várias linguagens. Mas para aprender, é melhor focar em uma só — e Python é uma ótima escolha.

**P: O que é um "script"?**
R: É um programa escrito em linguagem interpretada, geralmente um arquivo de texto com instruções que são executadas linha por linha. Seus arquivos `.py` são scripts Python.

**P: Preciso memorizar as diferenças entre compilado, interpretado e VM?**
R: Não! O importante é entender o conceito geral. No dia a dia, você só precisa saber que Python é interpretado e que basta escrever e executar.

**P: O que é o .NET?**
R: É uma plataforma de desenvolvimento da Microsoft, similar à JVM do Java. Linguagens como C# rodam no .NET. Não vamos usar .NET neste curso — mencionamos apenas para contexto.

---

[← Anterior: Introdução à Programação](01-introducao-programacao.md) · [Glossário](00-glossario.md) · [Próximo: Preparação do Ambiente →](03-preparacao-ambiente.md)
