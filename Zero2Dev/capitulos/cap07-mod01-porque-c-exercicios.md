# 7.1 — Exercícios: Por que Aprender C?

[← Voltar ao conteúdo: Por que Aprender C?](cap07-mod01-porque-c-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios são de pesquisa e reflexão — ainda não vamos escrever código em C (isso começa no módulo 7.2). O objetivo aqui é consolidar os conceitos apresentados no módulo e preparar sua mentalidade para a transição de Python para C.

Para cada exercício, escreva suas respostas em um arquivo de texto ou em um documento. Não existe resposta "certa" ou "errada" nos exercícios de reflexão — o importante é pensar sobre os conceitos.

---

## Exercício 1 — C no Seu Dia a Dia (Pesquisa)

### Enunciado

Liste pelo menos 8 softwares, dispositivos ou tecnologias que você usa no dia a dia que são escritos em C ou dependem diretamente de código C.

Para cada item, preencha a tabela:

| Item | O que faz | Escrito em | Por que C foi escolhida |
|------|----------|-----------|------------------------|
| Exemplo: Linux | Sistema operacional | C | Precisa controlar hardware diretamente |
| 1. | | | |
| 2. | | | |
| 3. | | | |
| 4. | | | |
| 5. | | | |
| 6. | | | |
| 7. | | | |
| 8. | | | |

### Dicas

- Pense em categorias: sistema operacional, navegador, banco de dados, ferramentas de terminal, dispositivos físicos (roteador, TV, micro-ondas), aplicativos de celular (que usam SQLite por baixo)
- Pesquise "escrito em que linguagem" para softwares que você usa
- Lembre que muitos softwares usam C indiretamente — por exemplo, qualquer aplicativo que roda em Linux depende do kernel (escrito em C)

---

## Exercício 2 — Python vs C: Tabela Comparativa Completa (Pesquisa)

### Enunciado

Crie uma tabela comparativa detalhada entre Python e C com pelo menos 10 critérios. Para cada critério, indique qual linguagem é mais adequada e explique por quê.

Use as informações do módulo como base, mas adicione pelo menos 3 critérios que você pesquisou por conta própria.

| Critério | Python | C | Qual e melhor neste aspecto? | Por que? |
|----------|--------|---|------------------------------|----------|
| Velocidade de execução | | | | |
| Facilidade de aprendizado | | | | |
| Gerenciamento de memória | | | | |
| ... | | | | |

### Dicas

- Pense em critérios como: velocidade de execução, facilidade de aprendizado, gerenciamento de memória, portabilidade, ecossistema de bibliotecas, uso em sistemas embarcados, uso em web, comunidade, mercado de trabalho, segurança, debugging, tempo de desenvolvimento
- Não existe linguagem "melhor" em tudo — cada uma tem vantagens em diferentes aspectos
- Pesquise o índice TIOBE (ranking de linguagens de programação) para ver a posição de cada uma

---

## Exercício 3 — Linha do Tempo da Linguagem C (Pesquisa)

### Enunciado

Crie uma linha do tempo com pelo menos 10 marcos importantes na história de C e das tecnologias que ela influenciou. Para cada marco, inclua:

- Ano
- O que aconteceu
- Por que foi importante

Comece em 1966 (BCPL) e termine em 2023 (C23).

### Exemplo de formato

```
1966 — BCPL criada por Martin Richards
       Importancia: linguagem que inspirou B, que inspirou C

1969 — Ken Thompson cria o Unix em Assembly
       Importancia: sistema operacional que motivou a criacao de C

...continue ate 2023...
```

### Dicas

- Use as informações do módulo como base
- Pesquise marcos adicionais: quando o Linux foi criado? Quando o Git foi criado? Quando o Python foi criado?
- Inclua pelo menos 2 marcos que não foram mencionados no módulo (pesquise por conta própria)

---

## Exercício 4 — Compilado vs Interpretado: Análise Prática (Reflexão)

### Enunciado

Imagine que você precisa criar dois programas diferentes:

**Programa A**: Um script que lê um arquivo CSV com 100 linhas de dados de vendas e gera um relatório em texto com totais e médias.

**Programa B**: Um sistema que processa 10 milhões de transações financeiras por segundo em uma bolsa de valores, onde cada milissegundo de atraso pode significar milhões de reais de prejuízo.

Para cada programa, responda:

1. Qual linguagem você escolheria (Python ou C)? Justifique.
2. Quanto tempo de desenvolvimento você estima para cada linguagem?
3. Qual seria a velocidade de execução em cada linguagem (estimativa relativa)?
4. Quais riscos existem em cada escolha?
5. Se o Programa A precisasse processar 100 milhões de linhas em vez de 100, sua escolha mudaria? Por quê?

### Dicas

- Pense no trade-off entre tempo de desenvolvimento e velocidade de execução
- Considere que o Programa A provavelmente será executado uma vez por dia, enquanto o Programa B roda continuamente
- Lembre que muitos sistemas reais usam as duas linguagens: Python para a lógica de negócio e C para as partes críticas

---

## Exercício 5 — O Legado de Dennis Ritchie (Pesquisa e Reflexão)

### Enunciado

Dennis Ritchie faleceu em 11 de outubro de 2011, uma semana depois de Steve Jobs. A morte de Jobs foi manchete mundial. A morte de Ritchie passou quase despercebida.

Pesquise e responda:

1. Liste pelo menos 5 tecnologias criadas por Dennis Ritchie (diretamente ou como co-criador) que você usa ou que afetam sua vida diariamente.

2. Liste pelo menos 5 tecnologias criadas ou popularizadas por Steve Jobs que você usa ou que afetam sua vida diariamente.

3. Compare as duas listas. Qual das duas pessoas teve mais impacto na tecnologia que você usa hoje? Justifique sua resposta.

4. Por que você acha que Ritchie recebeu menos atenção da mídia? O que isso diz sobre como a sociedade valoriza diferentes tipos de contribuição tecnológica?

5. Pesquise o **Prêmio Turing** (Turing Award). O que é? Quem já ganhou? Dennis Ritchie ganhou em que ano e por qual contribuição?

### Dicas

- Pense em contribuições diretas (C, Unix) e indiretas (Linux descende de Unix, macOS descende de Unix, Android roda sobre Linux)
- Considere que Jobs criou produtos que as pessoas usam diretamente (iPhone, Mac), enquanto Ritchie criou infraestrutura que as pessoas usam indiretamente
- Não existe resposta "certa" — o objetivo é refletir sobre diferentes tipos de contribuição

---

## Exercício 6 — Rust: A Possível Sucessora de C (Pesquisa)

### Enunciado

A linguagem **Rust** (criada pela Mozilla em 2010) é frequentemente mencionada como uma possível substituta de C em alguns cenários. Em 2022, o kernel do Linux começou a aceitar código Rust pela primeira vez na história — um evento significativo, já que o kernel sempre foi exclusivamente C.

Pesquise e responda:

1. O que é Rust? Quem criou e por quê?
2. Qual é o principal problema de C que Rust tenta resolver? (dica: tem a ver com segurança de memória)
3. O que são "memory safety bugs"? Por que eles são perigosos?
4. Como Rust resolve esse problema sem usar garbage collector (como Python)?
5. Se Rust é "melhor" que C em segurança, por que C ainda é mais usada? Liste pelo menos 3 razões.
6. Você acha que Rust vai substituir C completamente? Por que sim ou por que não?

### Dicas

- Pesquise "Rust vs C" para encontrar comparações
- O conceito-chave de Rust é o "ownership system" (sistema de propriedade) — pesquise o que é
- A Microsoft revelou que 70% das vulnerabilidades de segurança do Windows são causadas por problemas de memória em código C/C++ — isso motivou o interesse em Rust
- Pesquise "Rust in Linux kernel" para entender o contexto da adoção de Rust no Linux

---

## Exercício 7 — Mapa Mental: A Influência de C (Criação)

### Enunciado

Crie um mapa mental (pode ser em texto, desenho ou usando uma ferramenta online como draw.io) mostrando a influência de C na tecnologia moderna.

No centro, coloque "Linguagem C (1972)". A partir daí, crie ramificações para:

1. **Linguagens derivadas**: C++, Java, C#, JavaScript, Go, Rust, Swift, etc.
2. **Sistemas operacionais**: Unix, Linux, macOS, Windows, Android, iOS
3. **Softwares escritos em C**: Git, SQLite, PostgreSQL, Redis, Nginx, etc.
4. **Conceitos introduzidos por C**: ponteiros, structs, compilação, tipos estáticos, etc.
5. **Pessoas-chave**: Dennis Ritchie, Ken Thompson, Brian Kernighan, Bjarne Stroustrup, etc.

Para cada item, adicione uma breve nota explicando a conexão com C.

### Dicas

- Use as informações do módulo como base
- Adicione pelo menos 3 itens que você pesquisou por conta própria
- Se preferir fazer em texto, use indentação para mostrar a hierarquia:
  ```
  Linguagem C (1972)
    ├── Linguagens derivadas
    │   ├── C++ (1979) — C com orientacao a objetos
    │   ├── Java (1995) — sintaxe baseada em C
    │   └── ...
    ├── Sistemas operacionais
    │   ├── Unix (1973) — reescrito em C
    │   └── ...
    └── ...
  ```

---

## Gabarito Parcial

### Exercício 1 — Exemplos de respostas possíveis

| Item | O que faz | Escrito em | Por que C |
|------|----------|-----------|-----------|
| Linux | Sistema operacional | C | Controle direto de hardware |
| Git | Controle de versão | C | Performance com milhares de arquivos |
| SQLite | Banco de dados | C | Eficiência em dispositivos com pouca memória |
| Python (CPython) | Interpretador | C | O motor precisa ser rápido |
| Bash | Shell do terminal | C | Interação direta com o sistema operacional |
| Nginx | Servidor web | C | Atender milhares de conexões simultaneas |
| curl | Transferencia de dados | C | Performance e portabilidade |
| OpenSSL | Criptografia | C | Operações matematicas intensivas |

### Exercício 4 — Direcionamento

- Programa A (100 linhas de CSV): Python é a escolha óbvia. O volume de dados é pequeno, a velocidade não é crítica, e Python tem bibliotecas prontas (csv, pandas) que resolvem o problema em poucas linhas.
- Programa B (10 milhões de transações/segundo): C (ou C++) é necessário. Cada milissegundo conta, e Python seria ordens de magnitude mais lento.
- Se o Programa A crescer para 100 milhões de linhas: a escolha pode mudar. Python com pandas (que usa C por baixo) provavelmente ainda funciona, mas se a performance for insuficiente, as partes críticas poderiam ser reescritas em C.

---

[← Voltar ao conteúdo: Por que Aprender C?](cap07-mod01-porque-c-conteudo.md) · [Próximo: Ambiente C →](cap07-mod02-ambiente-c-conteudo.md)
