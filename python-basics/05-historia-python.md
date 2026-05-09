# 05 — História do Python e Suas Premissas

[← Anterior: Execução, Permissões e Pastas](04-execucao-permissoes-pastas.md) · [Glossário](00-glossario.md) · [Próximo: Entrada e Saída de Dados →](06-entrada-saida.md)

---

## Introdução

Antes de mergulhar na programação prática, vale a pena conhecer um pouco sobre a linguagem que vamos usar. Saber de onde o Python veio, quem o criou e qual sua filosofia ajuda a entender por que ele funciona da forma que funciona — e por que é uma escolha tão boa para quem está começando.

---

## Quem Criou o Python?

O Python foi criado por **Guido van Rossum**, um programador holandês, no final dos anos 1980. A primeira versão pública foi lançada em **1991**.

O nome "Python" não vem da cobra — vem do grupo de comédia britânico **Monty Python**, do qual Guido era fã. Ele queria um nome curto, único e um pouco divertido.

Guido liderou o desenvolvimento do Python por quase 30 anos e era carinhosamente chamado de "BDFL" (Benevolent Dictator For Life — Ditador Benevolente Vitalício), porque ele tinha a palavra final sobre as decisões da linguagem. Em 2018, ele se aposentou desse papel, e hoje o Python é mantido por uma comunidade global de desenvolvedores.

---

## A Filosofia do Python: O Zen of Python

O Python tem uma filosofia de design que guia como a linguagem é construída e como o código deve ser escrito. Essa filosofia é chamada de **Zen of Python** e pode ser vista digitando o seguinte comando no terminal:

```bash
python3 -c "import this"
```

> **Nota:** Esse comando pede ao Python para executar a instrução `import this`, que exibe o Zen of Python.

O texto completo está em inglês, mas aqui estão os princípios mais importantes traduzidos e explicados de forma simples:

### Princípios mais importantes

| Princípio (em inglês) | Tradução | O que significa na prática |
|----------------------|----------|---------------------------|
| Beautiful is better than ugly | Bonito é melhor que feio | Escreva código limpo e organizado |
| Simple is better than complex | Simples é melhor que complexo | Prefira soluções simples |
| Readability counts | Legibilidade conta | Código deve ser fácil de ler |
| There should be one obvious way to do it | Deve haver uma maneira óbvia de fazer | Não complique o que pode ser simples |
| Errors should never pass silently | Erros nunca devem passar em silêncio | Trate os erros, não os ignore |
| Now is better than never | Agora é melhor que nunca | Comece, mesmo que não esteja perfeito |

Esses princípios refletem a essência do Python: **simplicidade, clareza e praticidade**. Quando você escrever código Python, tente seguir esses princípios — escreva código que outra pessoa (ou você mesmo no futuro) consiga ler e entender facilmente.

---

## Por que Python é Popular para Iniciantes?

O Python se tornou uma das linguagens mais populares do mundo, especialmente para quem está começando. Aqui estão os motivos:

### 1. Sintaxe limpa e legível

O código Python se parece com inglês simples. Compare:

**Python:**
```python
# Se a idade for maior ou igual a 18, exibir mensagem
if age >= 18:
    print("Você é maior de idade")
```

**Java (mesma lógica, mais complexo):**
```java
if (age >= 18) {
    System.out.println("Você é maior de idade");
}
```

Perceba como o Python é mais limpo: sem chaves `{}`, sem ponto e vírgula `;`, sem `System.out.println`. Apenas indentação e palavras simples.

### 2. Comunidade acolhedora

A comunidade Python é conhecida por ser amigável e receptiva com iniciantes. Existem milhares de tutoriais, fóruns e grupos de ajuda em português e inglês.

### 3. Vasta documentação

O Python tem uma documentação oficial completa, inclusive em português brasileiro. Além disso, sites como W3Schools oferecem tutoriais práticos e acessíveis.

### 4. Versatilidade

Python pode ser usado para praticamente tudo — de scripts simples a inteligência artificial. Isso significa que o que você aprende aqui pode ser aplicado em muitas áreas diferentes.

---

## Onde Python é Usado no Mundo Real?

Python não é apenas uma linguagem para aprender — é usada por empresas e profissionais no mundo inteiro para resolver problemas reais:

| Área | Como Python é usado | Exemplos |
|------|---------------------|----------|
| **Ciência de Dados** | Analisar grandes volumes de dados, criar gráficos e relatórios | Análise de vendas, pesquisas, estatísticas |
| **Inteligência Artificial** | Criar sistemas que aprendem com dados | Reconhecimento de imagens, assistentes virtuais |
| **Automação** | Automatizar tarefas repetitivas | Renomear arquivos, enviar e-mails automáticos |
| **Desenvolvimento Web** | Criar sites e APIs | Lojas online, sistemas de cadastro |
| **Jogos** | Criar jogos simples e protótipos | Jogos 2D, simulações |
| **Educação** | Ensinar programação | Cursos, tutoriais, exercícios (como este!) |

Ao aprender Python, você está aprendendo uma ferramenta que pode abrir portas em muitas áreas profissionais.

---

## Versões do Python: Python 2 vs Python 3

Existem duas versões principais do Python:

- **Python 2** — versão antiga, descontinuada em 2020. Não recebe mais atualizações.
- **Python 3** — versão atual e a que usamos neste curso. Recebe atualizações regulares.

**Sempre use Python 3.** Se você encontrar tutoriais ou exemplos na internet que usam `print "texto"` (sem parênteses), eles são de Python 2 e podem não funcionar. No Python 3, o correto é `print("texto")` (com parênteses).

Para verificar sua versão:

```bash
python3 --version
```

**Saída esperada:**

```
Python 3.10.12
```

O número pode variar, mas deve começar com **3**.

---

## Para Saber Mais

-  [W3Schools — Python Introduction](https://www.w3schools.com/python/python_intro.asp) — _Introdução ao Python_
-  [Documentação Oficial Python em Português](https://docs.python.org/pt-br/3/) — _Referência completa_
-  [Python.org — About Python](https://www.python.org/about/) — _Sobre o Python (em inglês)_

---

## Perguntas Frequentes (FAQ)

**P: Preciso saber a história do Python para programar?**
R: Não é obrigatório, mas entender a filosofia da linguagem ajuda a escrever código melhor. Os princípios de simplicidade e legibilidade do Python vão guiar você ao longo de todo o curso.

**P: Python é gratuito?**
R: Sim! Python é completamente gratuito e de código aberto. Qualquer pessoa pode usar, modificar e distribuir.

**P: Python vai continuar sendo relevante no futuro?**
R: Python é uma das linguagens que mais cresce no mundo. É amplamente usada em áreas como inteligência artificial e ciência de dados, que estão em alta. As perspectivas são muito boas.

**P: Posso ganhar dinheiro programando em Python?**
R: Sim! Desenvolvedores Python são muito procurados no mercado de trabalho. Áreas como desenvolvimento web, ciência de dados e automação oferecem muitas oportunidades.

**P: O que significa "código aberto" (open source)?**
R: Significa que o código-fonte do Python é público — qualquer pessoa pode ver como ele funciona, sugerir melhorias e contribuir. É como uma receita compartilhada que qualquer pessoa pode usar e melhorar.

**P: Quem mantém o Python hoje?**
R: O Python é mantido pela Python Software Foundation (PSF) e por uma comunidade global de milhares de desenvolvedores voluntários. Guido van Rossum se aposentou da liderança em 2018.

**P: O que é o "Zen of Python"?**
R: É um conjunto de princípios que guiam o design da linguagem Python. Você pode vê-lo digitando `python3 -c "import this"` no terminal. Os princípios mais importantes são: simplicidade, legibilidade e praticidade.

**P: Por que o nome "Python" e não outro?**
R: Guido van Rossum era fã do grupo de comédia britânico Monty Python. Ele queria um nome curto, único e divertido para a linguagem.

**P: Python é usado por empresas grandes?**
R: Sim! Google, Netflix, Instagram, Spotify, NASA e muitas outras empresas usam Python em seus sistemas.

**P: O que é "inteligência artificial"?**
R: É a área da computação que cria sistemas capazes de aprender com dados e tomar decisões. Python é a linguagem mais popular para IA por causa de bibliotecas como TensorFlow e PyTorch.

**P: O que é "ciência de dados"?**
R: É a área que analisa grandes volumes de dados para encontrar padrões e tomar decisões. Python é muito usado por causa de bibliotecas como Pandas e NumPy.

**P: O que é "automação"?**
R: É usar programas para realizar tarefas repetitivas automaticamente. Por exemplo: renomear centenas de arquivos, enviar e-mails automáticos ou organizar planilhas. Python é excelente para isso.

**P: Qual a diferença entre Python 2 e Python 3?**
R: Python 2 é a versão antiga, descontinuada em 2020. Python 3 é a versão atual. A principal diferença visível é que no Python 3, `print` é uma função: `print("texto")` com parênteses.

**P: Posso usar Python 2?**
R: Não é recomendado. Python 2 não recebe mais atualizações de segurança. Sempre use Python 3.

**P: O que é uma "biblioteca" em Python?**
R: É um conjunto de código pronto que outras pessoas escreveram e que você pode usar no seu programa. É como usar um ingrediente pronto (molho de tomate) em vez de fazer tudo do zero.

**P: O que é "desenvolvimento web"?**
R: É a criação de sites e aplicações que funcionam na internet. Python é usado para o "backend" (a parte do servidor que processa dados). Neste curso, vamos usar FastAPI para criar uma API web.

**P: Python é bom para jogos?**
R: Python pode ser usado para jogos simples (com Pygame), mas para jogos profissionais 3D, linguagens como C++ são mais comuns por serem mais rápidas.

**P: O que é uma "API"?**
R: API (Application Programming Interface) é um conjunto de regras que permite que programas se comuniquem. Neste curso, vamos criar uma API para o projeto CRUD nos módulos finais.

**P: Preciso saber tudo sobre Python para conseguir um emprego?**
R: Não! Ninguém sabe tudo sobre uma linguagem. O importante é ter uma base sólida (que este curso oferece) e saber buscar informações quando precisar.

**P: O que é a "comunidade Python"?**
R: É o grupo global de pessoas que usam, desenvolvem e ensinam Python. Inclui fóruns, grupos de discussão, conferências (como a PyCon) e projetos colaborativos. A comunidade é conhecida por ser acolhedora com iniciantes.

---

[← Anterior: Execução, Permissões e Pastas](04-execucao-permissoes-pastas.md) · [Glossário](00-glossario.md) · [Próximo: Entrada e Saída de Dados →](06-entrada-saida.md)
