# 13.5 — Apresentação e Defesa do Projeto

[← Anterior: Documentação Técnica](cap13-mod04-documentação.md) · [Próximo: Usando IA no Desenvolvimento →](cap13-mod06-ia-no-desenvolvimento.md)

---

## Introdução

No módulo anterior, você completou a documentação do seu TCC — README, comentários, Swagger e dicionário de dados. O projeto está pronto tecnicamente. Agora falta a última etapa: apresentar e defender o que você construiu.

Apresentar um projeto técnico é uma habilidade que vai muito além do TCC. No mundo profissional, você vai precisar apresentar ideias em reuniões, defender decisões técnicas em code reviews, explicar sistemas para colegas novos e convencer gestores de que uma abordagem é melhor que outra. Saber comunicar o que você fez é tão importante quanto saber fazer.

Este módulo vai te preparar para apresentar o TCC com clareza e confiança. Não é sobre decorar um texto — e sobre entender tão bem o que você construiu que consegue explicar para qualquer pessoa.

---

## O que é uma Defesa de Projeto?

A defesa do TCC é uma apresentação onde você:

1. Explica qual problema o projeto resolve
2. Mostra como o sistema funciona (demonstração ao vivo)
3. Descreve as decisões técnicas que tomou
4. Responde perguntas sobre o projeto

Não é uma prova. Não é uma arguição hostil. É uma conversa técnica onde você demonstra o que aprendeu e o que construiu. Os avaliadores querem ver que você entende o que fez — não que decorou respostas.

### O que os Avaliadores Procuram

| Critério | O que demonstra | Como mostrar |
|----------|----------------|-------------|
| Clareza na explicação | Você entende o que fez | Explicar sem jargao desnecessário |
| Demonstração funcional | O sistema funciona | Mostrar ao vivo, com dados reais |
| Decisões justificadas | Você pensou antes de fazer | Explicar por que escolheu cada tecnologia e abordagem |
| Conhecimento técnico | Você aprendeu os conceitos | Responder perguntas com segurança |
| Organização | Você sabe se comunicar | Apresentação estruturada e dentro do tempo |

---

## Estrutura da Apresentação

Uma apresentação de TCC típica dura entre 15 e 30 minutos. Organize assim:

### Parte 1: O Problema (3-5 minutos)

Comece pelo problema, não pela tecnologia. O avaliador precisa entender POR QUE o projeto existe antes de ver COMO funciona.

**O que falar:**
- Qual problema você identificou
- Por que esse problema importa
- Para quem o sistema e útil
- O que existia antes (planilha, caderno, nada)

**Exemplo:**
> "Muitas pessoas não sabem quanto gastam por mês. Anotar despesas em cadernos e trabalhoso e fácil de esquecer. O FinControl resolve isso: é uma API que permite registrar receitas e despesas, categorizar e consultar resumos. Com ele, o usuário sabe exatamente para onde vai o dinheiro."

### Parte 2: A Solução (5-8 minutos)

Agora mostre o que você construiu. Use diagramas e demonstração ao vivo.

**O que mostrar:**
- Diagrama de arquitetura (camadas do sistema)
- Diagrama ER (modelo de dados)
- Lista de funcionalidades implementadas
- Tecnologias usadas e por que

**Dica:** não leia slides. Use os diagramas como apoio visual e explique com suas palavras.

### Parte 3: Demonstração ao Vivo (5-10 minutos)

Esta é a parte mais importante. Mostre o sistema funcionando de verdade.

**Roteiro de demonstração:**

1. Mostrar o servidor iniciando
2. Mostrar o Swagger (se API)
3. Criar dados de exemplo (categorias, transações)
4. Listar dados
5. Mostrar filtros e busca funcionando
6. Mostrar uma regra de negócio (tentar criar dado inválido, mostrar o erro)
7. Mostrar estatisticas ou resumos

**Prepare os dados antes:** não perca tempo digitando JSONs longos durante a apresentação. Tenha comandos curl prontos em um arquivo ou use o Swagger.

**Tenha um plano B:** se algo der errado na demonstração ao vivo (e as vezes da), tenha screenshots ou um video gravado como backup.

### Parte 4: Decisões Técnicas (3-5 minutos)

Explique as decisões mais importantes que você tomou:

- Por que escolheu essa stack (Python + FastAPI + SQLite)
- Por que organizou o código em camadas
- Quais regras de negócio implementou e por que
- O que ficou fora do escopo e por que

**Exemplo:**
> "Escolhi SQLite porque não precisa de instalação separada e os dados ficam em um único arquivo. Para um projeto individual, é mais que suficiente. Se fosse um sistema com múltiplos usuários simultâneos, eu usaria PostgreSQL."

### Parte 5: Perguntas (5-10 minutos)

Os avaliadores vão fazer perguntas. Não entre em panico — eles querem entender, não te derrubar.

---

## Perguntas Típicas e Como Responder

### Perguntas sobre Decisões

**"Por que você escolheu FastAPI em vez de Flask?"**
> "FastAPI tem validação automática com Pydantic, gera documentação Swagger automaticamente e tem suporte nativo a tipagem. Para uma API REST, essas funcionalidades economizam muito código. Flask é mais flexível, mas eu precisaria adicionar essas funcionalidades manualmente."

**"Por que SQLite e não PostgreSQL?"**
> "SQLite não precisa de instalação separada — já vem com Python. Para um projeto individual com volume baixo de dados, e a escolha mais prática. Se o projeto crescesse para múltiplos usuários simultâneos, eu migraria para PostgreSQL. A arquitetura em camadas facilita essa troca — só preciso mudar o repositório."

**"Por que separar em camadas?"**
> "A separacao em camadas permite que eu mude uma parte sem afetar as outras. Se eu quiser trocar o banco de dados, só mudo o repositório. Se eu quiser mudar uma regra de negócio, só mudo o serviço. Além disso, facilita testes — posso testar a lógica de negócio sem precisar do banco."

### Perguntas sobre Limitações

**"O que você faria diferente se comecasse de novo?"**
Essa é uma pergunta excelente. Mostra maturidade reconhecer limitações:
> "Eu adicionaria testes automatizados desde o início. Testei tudo manualmente, o que funciona para um projeto pequeno, mas não escala. Também separaria melhor a configuração — hoje o caminho do banco esta hardcoded, deveria vir de variável de ambiente."

**"Quais são as limitações do sistema?"**
> "O sistema não tem autenticação — qualquer pessoa pode acessar os dados. Também não tem backup automático do banco. E o SQLite não suporta acessos simultâneos, então não funcionaria para múltiplos usuários ao mesmo tempo."

### Perguntas sobre Conceitos

**"O que é uma API REST?"**
> "É uma forma de comunicação entre sistemas usando HTTP. REST define convenções: usar verbos HTTP (GET para buscar, POST para criar), URLs que representam recursos (/products, /categories), e respostas em JSON. O FastAPI implementa essas convenções."

**"O que é arquitetura em camadas?"**
> "É uma forma de organizar o código onde cada camada tem uma responsabilidade específica. O controller recebe requisições, o service aplica regras de negócio, e o repository acessa o banco. Nenhuma camada faz o trabalho da outra."

**"O que é uma chave estrangeira?"**
> "É um campo em uma tabela que referência a chave primária de outra tabela. No meu projeto, a tabela transactions tem um campo category_id que referência o id da tabela categories. Isso garante que toda transação pertence a uma categoria válida."

### A Resposta Mais Honesta

Se você não sabe a resposta para uma pergunta, diga:
> "Não sei a resposta exata para isso, mas sei que esta relacionado com [conceito]. Posso pesquisar e te responder depois."

Isso é muito melhor do que inventar uma resposta errada. Avaliadores respeitam honestidade.

---

## Preparando a Apresentação

### Slides ou Não?

Para o TCC, slides simples ajudam a organizar a apresentação. Mas não exagere — o foco e a demonstração ao vivo, não os slides.

**Estrutura sugerida de slides:**

| Slide | Conteúdo |
|-------|---------|
| 1 | Título do projeto, seu nome |
| 2 | O problema (1-2 frases) |
| 3 | A solução (1-2 frases + screenshot) |
| 4 | Diagrama de arquitetura |
| 5 | Diagrama ER |
| 6 | Funcionalidades implementadas (lista) |
| 7 | Tecnologias usadas (tabela) |
| 8 | Demonstração ao vivo (slide em branco ou com URL) |
| 9 | Decisões técnicas (3-4 bullets) |
| 10 | Limitações e próximos passos |
| 11 | Obrigado + contato |

Máximo: 10-12 slides. Menos é mais.

### Ferramentas para Slides

Você não precisa de ferramentas caras ou complexas. Opcoes gratuitas que funcionam bem:

| Ferramenta | Vantagem | Desvantagem |
|-----------|----------|-------------|
| Google Slides | Gratuito, colaborativo, funciona no navegador | Precisa de internet |
| LibreOffice Impress | Gratuito, offline, compatível com PowerPoint | Interface menos moderna |
| Canva | Templates bonitos, fácil de usar | Versão gratuita limitada |
| Markdown + Marp | Slides em Markdown (para quem gosta de código) | Curva de aprendizado |
| PDF simples | Universal, não depende de software | Sem animacoes |

Para o TCC, Google Slides ou LibreOffice Impress são mais que suficientes. O conteúdo importa infinitamente mais que o visual.

### Preparando a Demonstração ao Vivo

A demonstração e a parte mais crítica da apresentação. Se funcionar, você ganha confiança e credibilidade. Se falhar, você precisa de um plano B. Prepare-se para os dois cenários.

**Antes da apresentação:**

1. Reinicie o computador (limpa processos que podem interferir)
2. Feche programas desnecessários (especialmente os que usam muita memória)
3. Desative notificacoes (nada pior que uma notificacao pessoal aparecendo na tela)
4. Teste a conexão com o projetor ou tela externa
5. Tenha o terminal aberto e pronto
6. Tenha os comandos curl em um arquivo para copiar e colar

**Arquivo de demonstração (`demo.sh`):**

Crie um arquivo com todos os comandos que você vai usar na demonstração:

```bash
#!/bin/bash
# demo.sh — Comandos para demonstracao do TCC
# Uso: copie e cole cada bloco no terminal

# === 1. Iniciar o servidor ===
# uvicorn main:app --reload

# === 2. Criar categorias ===
echo "--- Criando categorias ---"
curl -s -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Alimentacao", "description": "Gastos com comida"}' | python3 -m json.tool

curl -s -X POST http://localhost:8000/categories \
  -H "Content-Type: application/json" \
  -d '{"name": "Transporte", "description": "Gastos com locomocao"}' | python3 -m json.tool

# === 3. Criar transacoes ===
echo "--- Criando transacoes ---"
curl -s -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{"description": "Almoco", "amount": 25.50, "type": "expense", "category_id": 1, "date": "2026-04-28"}' | python3 -m json.tool

curl -s -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{"description": "Salario", "amount": 5000.00, "type": "income", "category_id": 1, "date": "2026-04-01"}' | python3 -m json.tool

# === 4. Listar transacoes ===
echo "--- Listando transacoes ---"
curl -s http://localhost:8000/transactions | python3 -m json.tool

# === 5. Mostrar filtros ===
echo "--- Filtrando por tipo ---"
curl -s "http://localhost:8000/transactions?type=expense" | python3 -m json.tool

# === 6. Mostrar regra de negocio (erro) ===
echo "--- Tentando criar com categoria inexistente ---"
curl -s -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{"description": "Teste", "amount": 10, "type": "expense", "category_id": 999, "date": "2026-04-28"}' | python3 -m json.tool

# === 7. Estatisticas ===
echo "--- Consultando saldo ---"
curl -s http://localhost:8000/transactions/balance | python3 -m json.tool
```

O `python3 -m json.tool` formata o JSON na saída, tornando mais legível na apresentação.

**Dica:** use `| python3 -m json.tool` para formatar a saída JSON. Saída formatada é muito mais fácil de ler em uma apresentação do que JSON em uma única linha.

### Plano B: Quando a Demo Falha

Coisas que podem dar errado e como se preparar:

| Problema | Plano B |
|----------|---------|
| Servidor não inicia | Tenha screenshots de tudo funcionando |
| Banco corrompido | Tenha um banco de backup com dados de exemplo |
| Erro inesperado | Tenha um video gravado da demonstração |
| Projetor não funciona | Tenha o projeto no celular para mostrar na tela |
| Internet cai | Tudo roda local (SQLite + FastAPI), não precisa de internet |

**Como gravar um video de backup:**

No macOS, use QuickTime Player (Arquivo > Nova Gravacao de Tela). No Linux, use OBS Studio ou SimpleScreenRecorder. Grave a demonstração completa uma vez e salve o video. Se algo der errado ao vivo, você mostra o video.

---

## Erros Comuns em Apresentações Técnicas

### Erro 1: Falar Demais sobre Tecnologia, Pouco sobre o Problema

Muitos alunos começam falando "usei Python, FastAPI, SQLite, Pydantic, Uvicorn..." sem explicar POR QUE o projeto existe. O avaliador quer saber qual problema você resolveu — a tecnologia e o meio, não o fim.

**Como evitar:** comece sempre pelo problema. A tecnologia vem depois.

### Erro 2: Demonstração Sem Roteiro

Abrir o Swagger e clicar aleatoriamente não é uma demonstração. É uma exploracao confusa que não mostra nada com clareza.

**Como evitar:** tenha um roteiro escrito. Siga a ordem: criar dados, listar, filtrar, mostrar erro, mostrar estatistica. Cada passo demonstra uma funcionalidade específica.

### Erro 3: Ler Slides

Slides são apoio visual, não roteiro. Se você esta lendo o que está escrito no slide, o slide tem texto demais ou você não ensaiou o suficiente.

**Como evitar:** slides devem ter no máximo 3-5 bullets ou um diagrama. Você explica com suas palavras.

### Erro 4: Não Saber Responder Perguntas Básicas

Se o avaliador pergunta "o que é uma chave estrangeira?" e você não sabe responder, isso indica que você não entendeu o que construiu.

**Como evitar:** revise os conceitos fundamentais dos capítulos 8, 10 e 11 antes da apresentação. Você deve saber explicar: banco de dados relacional, arquitetura em camadas, API REST, CRUD, chave primária/estrangeira.

### Erro 5: Apresentação Muito Longa

Ultrapassar o tempo e desrespeitoso com os avaliadores e com outros alunos que estão esperando. Além disso, apresentações longas perdem a atenção do público.

**Como evitar:** ensaie cronometrando. Se esta passando de 20 minutos, corte conteúdo. A demonstração ao vivo e a parte mais importante — se precisar cortar algo, corte slides, não a demo.

### Erro 6: Não Mostrar Erros

Mostrar apenas o "caminho feliz" (tudo funcionando) não demonstra robustez. Avaliadores querem ver que o sistema trata erros.

**Como evitar:** inclua no roteiro pelo menos 2 cenários de erro: tentar criar dado inválido e buscar registro inexistente. Mostre que o sistema retorna mensagens claras.

---

## Comunicação Técnica: Uma Habilidade para a Vida

### Por que Comunicação Importa para Desenvolvedores

Existe um mito de que programadores só precisam saber programar. Na realidade, comunicação é uma das habilidades mais valorizadas na indústria:

| Situação | Habilidade necessária |
|----------|----------------------|
| Code review | Explicar por que o código está errado e sugerir melhoria |
| Reunião de planejamento | Estimar esforco e explicar complexidade técnica |
| Entrevista de emprego | Apresentar projetos e explicar decisões |
| Documentação | Escrever de forma clara para outros desenvolvedores |
| Mentoria | Ensinar conceitos para colegas mais novos |
| Incidente em produção | Comunicar o problema e a solução rapidamente |

Desenvolvedores que comunicam bem são promovidos mais rápido, conseguem melhores empregos e tem mais influencia nas decisões técnicas da equipe.

### A Regra do "Explique para sua Avo"

Se você consegue explicar um conceito técnico para alguém que não é de tecnologia, você realmente entende o conceito. Se você só consegue explicar usando jargao técnico, provavelmente esta repetindo definições sem entender de verdade.

Pratique explicar:
- "O que seu projeto faz?" → sem usar termos como API, REST, endpoint, CRUD
- "Por que isso é útil?" → conecte com um problema real que a pessoa entende
- "Como funciona?" → use analogias do dia a dia

### Feedback: O Presente que Ninguém Quer Receber

Depois da apresentação, você vai receber feedback. Pode ser difícil ouvir críticas, mas feedback e a forma mais rápida de melhorar.

**Como receber feedback:**
1. Escute sem interromper
2. Anote os pontos principais
3. Não se defenda — agradeca
4. Reflita depois, com calma
5. Implemente o que fizer sentido

**Como dar feedback (para colegas):**
1. Comece com algo positivo ("gostei de como você explicou X")
2. Seja específico ("na parte Y, ficou confuso porque...")
3. Sugira alternativa ("talvez se você mostrasse Z primeiro...")
4. Termine com encorajamento ("no geral, o projeto esta muito bom")

---

## Após a Apresentação

### Publicando o Projeto

Depois da defesa, publique o projeto no GitHub (se ainda não fez):

1. Crie um repositório público no GitHub
2. Faça push do código
3. Adicione uma descrição curta no repositório
4. Adicione topics relevantes (python, fastapi, sqlite, api-rest, crud)
5. Fixe o repositório no seu perfil (pin)

Esse projeto e o primeiro item do seu portfolio profissional. Recrutadores vão ve-lo.

### Melhorando o Projeto Depois

O TCC não precisa terminar na entrega. Você pode continuar melhorando:

- Adicionar autenticação (JWT)
- Adicionar testes automatizados (pytest)
- Containerizar com Docker
- Adicionar frontend simples (HTML + JavaScript)
- Implementar funcionalidades que ficaram fora do escopo
- Refatorar código com base no feedback recebido

Cada melhoria é um novo commit, uma nova habilidade praticada é um portfolio mais forte.

### Ensaiando

Ensaie a apresentação pelo menos 2 vezes:

1. **Ensaio sozinho:** fale em voz alta, cronometrando. Ajuste o que esta longo demais ou curto demais.
2. **Ensaio com alguém:** apresente para um amigo ou familiar. Peça feedback sobre clareza e ritmo.

A demonstração ao vivo merece ensaio extra. Teste:
- O servidor inicia sem erros?
- Os dados de exemplo estão prontos?
- Os comandos curl funcionam?
- O Swagger carrega corretamente?

### Checklist Pre-Apresentação

- [ ] Slides prontos (se usar)
- [ ] Servidor testado e funcionando
- [ ] Dados de exemplo preparados
- [ ] Comandos curl prontos em um arquivo
- [ ] Backup: screenshots ou video da demonstração
- [ ] Cronometro: apresentação dentro do tempo
- [ ] Ensaio feito pelo menos 1 vez

---

## Lidando com o Nervosismo

### E Normal Ficar Nervoso

Todo mundo fica nervoso antes de apresentar. Programadores experientes que apresentam em conferências internacionais ficam nervosos. Professores universitários ficam nervosos. Até Steve Jobs ficava nervoso antes dos keynotes da Apple (segundo relatos de colegas).

O nervosismo não é seu inimigo — e energia. A questão e canalizar essa energia para a apresentação em vez de deixar que ela te paralise.

### Técnicas que Funcionam

| Técnica | Como fazer | Por que funciona |
|---------|-----------|-----------------|
| Respiracao 4-7-8 | Inspire 4s, segure 7s, expire 8s (3x) | Ativa o sistema nervoso parasimpatico |
| Preparação excessiva | Ensaie mais do que acha necessário | Confiança vem de preparação |
| Visualização | Imagine a apresentação indo bem | O cerebro não distingue bem entre imaginacao vivida e realidade |
| Chegue cedo | Esteja no local 15 min antes | Familiaridade com o ambiente reduz ansiedade |
| Fale devagar | Conscientemente reduza a velocidade | Nervosismo acelera a fala — compensar ajuda |

### O que Fazer se Travar

Se você esquecer o que ia falar no meio da apresentação:

1. Respire (pausa de 2-3 segundos parece muito para você, mas não para o público)
2. Olhe para o slide atual (ele é seu guia)
3. Diga "vamos ver..." e passe para o próximo ponto
4. Ninguém percebe uma pausa curta — parece natural

### A Regra dos 5 Minutos

Os primeiros 5 minutos são os mais dificeis. Depois que você começa a falar e ve que o público esta prestando atenção, o nervosismo diminui naturalmente. Por isso, ensaie especialmente o início — se os primeiros 5 minutos fluirem, o resto vem.

---

## Dicas de Comunicação

### Fale para Pessoas, Não para Telas

Olhe para os avaliadores, não para o computador. Use os slides como apoio, não como roteiro.

### Use Linguagem Clara

Evite jargao desnecessário. Se usar um termo técnico, explique brevemente:
- Bom: "O sistema usa paginação — ou seja, em vez de retornar todos os registros de uma vez, retorna em páginas de 10."
- Ruim: "Implementei paginação offset-based com query parameters skip e limit no endpoint de listagem."

### Mostre Entusiasmo

Você construiu algo do zero. Isso é impressionante. Mostre que você se orgulha do que fez — sem exagero, mas com confiança.

### Admita Limitações

Ninguém espera um projeto perfeito. Mostrar que você conhece as limitações do seu sistema demonstra maturidade técnica. "Se eu tivesse mais tempo, adicionaria X" é uma frase poderosa.

### Controle o Ritmo

Quando estamos nervosos, tendemos a falar rápido demais. Conscientemente reduza a velocidade. Faça pausas entre seções. Uma pausa de 2 segundos parece uma eternidade para você, mas para o público e natural e da tempo de absorver a informação.

### Use Exemplos Concretos

Em vez de falar em abstrato ("o sistema válida dados"), mostre um exemplo concreto ("se eu tentar criar uma transação com valor negativo, olha o que acontece..."). Exemplos concretos são mais memoraveis é mais convincentes.

---

## Exemplo de Roteiro Completo

Para ajudar você a visualizar como a apresentação deve fluir, aqui esta um roteiro detalhado para o exemplo do FinControl:

### Minuto 0-1: Abertura

> "Boa tarde. Meu nome e [nome] e vou apresentar o FinControl, um sistema de controle financeiro pessoal."

### Minuto 1-4: O Problema

> "Muitas pessoas não sabem quanto gastam por mês. Eu mesmo tinha esse problema — anotava despesas em um caderno, mas nunca somava no final do mês. Planilhas ajudam, mas são trabalhosas de manter.
>
> O FinControl resolve isso: é uma API REST que permite registrar receitas e despesas, categorizar por tipo de gasto e consultar resumos. Com ele, você sabe exatamente para onde vai o dinheiro."

### Minuto 4-7: Arquitetura e Modelo

> "O sistema foi construido com Python, FastAPI e SQLite. Organizei o código em 3 camadas: routers que recebem as requisições, services que aplicam as regras de negócio, e repositories que acessam o banco.
>
> [Mostrar diagrama de arquitetura]
>
> O banco tem duas tabelas: categories e transactions. Cada transação pertence a uma categoria.
>
> [Mostrar diagrama ER]"

### Minuto 7-15: Demonstração ao Vivo

> "Vou mostrar o sistema funcionando. O servidor já está rodando.
>
> Primeiro, vou criar duas categorias: Alimentacao e Transporte.
> [Executar curl]
>
> Agora vou registrar algumas transações — um almoço de 25 reais e o salário de 5000 reais.
> [Executar curl]
>
> Vamos listar todas as transações.
> [Executar curl]
>
> Agora vou mostrar os filtros — só despesas.
> [Executar curl]
>
> E se eu tentar criar uma transação com categoria inexistente? Olha o erro.
> [Executar curl — mostrar erro 400]
>
> Por fim, o saldo: receitas menos despesas.
> [Executar curl]"

### Minuto 15-18: Decisões e Limitações

> "Escolhi SQLite porque não precisa de instalação e os dados ficam em um arquivo. Para um projeto individual, e suficiente.
>
> Separei em camadas para facilitar manutenção — se eu quiser trocar o banco, só mudo o repositório.
>
> Limitações: não tem autenticação, não tem backup automático, e o SQLite não suporta acessos simultâneos."

### Minuto 18-20: Encerramento

> "O projeto está no GitHub em [URL]. O README tem instruções completas de instalação e uso. Obrigado — estou aberto a perguntas."

---

## Apresentação como Habilidade Profissional

### O Desenvolvedor que Comunica Bem

Na indústria de tecnologia, existe uma correlacao forte entre habilidade de comunicação e progressao de carreira:

| Nível | Habilidade técnica | Habilidade de comunicação |
|-------|-------------------|--------------------------|
| Junior | Escreve código que funciona | Explica o que fez para o time |
| Pleno | Escreve código bem estruturado | Propoe soluções em reuniões |
| Senior | Projeta sistemas complexos | Apresenta arquitetura para stakeholders |
| Staff/Principal | Define direção técnica | Influencia decisões da empresa |

Perceba: a habilidade técnica cresce, mas a habilidade de comunicação cresce junto. Desenvolvedores que só sabem programar mas não sabem comunicar ficam estagnados.

### Tipos de Comunicação Técnica

Ao longo da carreira, você vai precisar de diferentes tipos de comunicação:

| Tipo | Quando | Exemplo |
|------|--------|---------|
| Escrita técnica | Documentação, PRs, design docs | README, comentários, ADRs |
| Apresentação formal | Defesa de TCC, tech talks, conferências | Slides + demonstração |
| Discussao técnica | Code reviews, reuniões de design | Argumentar por uma abordagem |
| Explicação informal | Pair programming, mentoria | Ensinar um conceito para colega |
| Comunicação de incidente | Quando algo quebra em produção | Descrever problema, impacto e solução |

O TCC exercita principalmente a apresentação formal e a escrita técnica. Mas as habilidades são transferíveis — quem apresenta bem também escreve bem e discute bem.

---

## Como a IA pode te ajudar aqui

**Prompt 1 — Entender erros comuns:**
> "Me ajude a criar um roteiro de apresentação de 15 minutos para meu TCC. O projeto e [descrição]. Quero cobrir: problema, solução, demonstração, decisões técnicas e limitações."

**Prompt 2 — Praticar com projetos:**
> "Quais perguntas um avaliador provavelmente faria sobre um projeto de API REST com FastAPI e SQLite? Me ajude a preparar respostas."

**Prompt 3 — Revisar com a IA:**
> "Revise este texto da minha apresentação e me diga se está claro para alguém que não é técnico."

---

## Casos de Uso no Mundo Real

### Caso 1: Apresentações Técnicas em Empresas

Em empresas de tecnologia, desenvolvedores apresentam projetos regularmente. No Nubank, por exemplo, engenheiros fazem "tech talks" internas onde explicam sistemas que construiram. No Google, engenheiros apresentam design docs para colegas antes de começar a implementação. A habilidade de apresentar um projeto técnico com clareza e valorizada em toda a indústria.

### Caso 2: Entrevistas Técnicas

Em entrevistas para vagas de desenvolvedor, é comum pedirem que você apresente um projeto pessoal. Recrutadores querem ver que você consegue explicar o que fez, por que fez e quais foram os desafios. O TCC é um projeto perfeito para isso — você conhece cada detalhe porque construiu do zero.

### Caso 3: Conferências e Meetups

Desenvolvedores experientes apresentam em conferências (como Python Brasil, TDC, GopherCon) e meetups locais. Essas apresentações seguem a mesma estrutura: problema, solução, demonstração, lições aprendidas. Começar apresentando o TCC e o primeiro passo para eventualmente apresentar em eventos maiores.

---

## Resumo do Módulo

| Conceito | Definição |
|----------|-----------|
| Defesa de projeto | Apresentação onde você explica e demonstra o que construiu |
| Demonstração ao vivo | Mostrar o sistema funcionando em tempo real |
| Decisão técnica | Escolha de tecnologia ou abordagem com justificativa |
| Limitação | Aspecto do sistema que poderia ser melhor |
| Roteiro | Estrutura planejada da apresentação |
| Plano B | Alternativa preparada caso algo de errado |

---

## Glossário do Módulo

| Termo | Definição |
|-------|-----------|
| Code review | Revisao de código por outros desenvolvedores |
| Defesa | Apresentação formal de um projeto com perguntas |
| Demo | Demonstração ao vivo de um sistema funcionando |
| Design doc | Documento de design técnico apresentado antes da implementação |
| Meetup | Encontro informal de profissionais de uma area |
| Plano B | Alternativa preparada para caso de falha |
| Roteiro | Sequência planejada de tópicos para uma apresentação |
| Slide | Página individual de uma apresentação visual |
| Tech talk | Apresentação técnica interna em uma empresa |

---

## Na Cultura Popular

- **Steve Jobs e as apresentações da Apple** — Jobs era famoso por suas apresentações de produtos. Ele ensaiava dezenas de vezes, cada detalhe era planejado, e a demonstração ao vivo era sempre o ponto alto. Você não precisa ser Steve Jobs, mas a lição e clara: preparação faz toda a diferença.

- **Shark Tank / Dragons' Den** (serie de TV) — empreendedores apresentam seus projetos para investidores em poucos minutos. Precisam explicar o problema, a solução e por que funciona — com clareza e confiança. A estrutura e a mesma da defesa do TCC: problema, solução, demonstração, perguntas.

---

## Para Saber Mais

- [How to Write a Good README](https://www.makeareadme.com/) — *Guia para READMEs que também ajuda a estruturar a apresentação do projeto*
- [Repositórios do Fino](https://github.com/RafaelFino) — *Veja como projetos reais são apresentados no GitHub*
- [Conventional Commits](https://www.conventionalcommits.org/pt-br/) — *Padrão de commits que mostra profissionalismo no histórico do projeto*
- [GitHub Student Developer Pack](https://education.github.com/pack) — *Ferramentas gratuitas para estudantes*

---

## Perguntas Frequentes (FAQ)

**P: E se o sistema travar durante a demonstração?**
R: Acontece. Respire, reinicie o servidor e continue. Se não resolver rápido, use o plano B (screenshots ou video). Avaliadores entendem que software falha — o que importa e como você lida com a situação.

**P: Preciso decorar a apresentação?**
R: Não. Decore a estrutura (problema, solução, demo, decisões), não o texto. Se você entende o que construiu, as palavras vem naturalmente.

**P: Posso ler anotações durante a apresentação?**
R: Ter anotações como apoio é normal. Ler um texto inteiro não é. Use os slides como guia e fale com suas palavras.

**P: Quanto tempo devo gastar na demonstração?**
R: A demonstração deve ser a parte mais longa — entre 5 e 10 minutos. E a prova de que o sistema funciona. Slides são apoio; a demo e o show.

**P: E se eu não souber responder uma pergunta?**
R: Diga honestamente que não sabe e que pode pesquisar. Isso é muito melhor do que inventar uma resposta errada.

**P: Posso apresentar com um colega?**
R: O TCC e individual, então a apresentação também. Mas você pode pedir para um colega assistir ao ensaio e dar feedback.

**P: Preciso de slides profissionais?**
R: Não. Slides simples e limpos são melhores que slides cheios de animacoes e efeitos. O conteúdo importa mais que o visual.

**P: E se meu projeto não ficou completo?**
R: Apresente o que você tem. Explique o que falta e por que não conseguiu terminar. Um projeto incompleto bem apresentado é melhor que um projeto completo mal apresentado.

**P: Quanto tempo devo gastar preparando a apresentação?**
R: Entre 2 e 4 horas. Isso inclui: criar slides (1h), preparar a demonstração (30min), ensaiar 2-3 vezes (1-2h). Não subestime o ensaio — e a parte mais importante da preparação.

**P: Posso mostrar o código durante a apresentação?**
R: Sim, mas com moderacao. Mostrar 1-2 trechos de código que ilustram decisões importantes (como uma regra de negócio no serviço) e bom. Mostrar centenas de linhas de código e entediante e confuso.

**P: E se o avaliador discordar de uma decisão minha?**
R: Escute o argumento, reconheça o ponto e explique seu raciocínio. "Você tem razao que PostgreSQL seria melhor para produção. Escolhi SQLite porque para o escopo do TCC a simplicidade era mais importante que a escalabilidade." Mostrar que você entende os trade-offs é mais valioso do que ter feito a escolha "perfeita".

**P: Preciso falar sobre o que aprendi no curso?**
R: Não diretamente, mas indiretamente sim. Quando você explica suas decisões de arquitetura, modelagem e implementação, esta demonstrando o que aprendeu. Não precisa dizer "no capítulo 10 eu aprendi que..." — basta aplicar o conhecimento.

**P: Posso usar o Swagger como demonstração em vez de curl?**
R: Sim. O Swagger é uma forma excelente de demonstrar a API — e visual, interativo e mostra a documentação ao mesmo tempo. Muitos avaliadores preferem ver o Swagger. Tenha os comandos curl como backup caso o Swagger tenha algum problema.

**P: Devo mostrar o código-fonte durante a apresentação?**
R: Mostre 1-2 trechos curtos que ilustram decisões importantes — por exemplo, uma regra de negócio no serviço ou a estrutura de um modelo Pydantic. Não mostre o código inteiro — e entediante e confuso. O código está no GitHub para quem quiser ver depois.

**P: Como lido com perguntas que não entendi?**
R: Peça para o avaliador repetir ou reformular. "Desculpe, pode reformular a pergunta?" e perfeitamente aceitavel. É melhor pedir esclarecimento do que responder algo que não foi perguntado.


---

## O Dia da Apresentação

### Checklist do Dia

Na manha da apresentação (ou na noite anterior):

- [ ] Computador carregado (leve o carregador também)
- [ ] Projeto funcionando (teste uma última vez)
- [ ] Banco de dados limpo ou com dados de exemplo
- [ ] Slides no computador (e em um pendrive como backup)
- [ ] Arquivo demo.sh com comandos prontos
- [ ] Video de backup da demonstração (se gravou)
- [ ] Adaptador de video (se precisar conectar no projetor)
- [ ] Agua (apresentar da sede)

### Depois da Apresentação

Independente de como foi:

1. Respire. Você terminou.
2. Anote o feedback recebido (você vai esquecer se não anotar)
3. Agradeca os avaliadores
4. Comemore — você construiu um projeto completo do zero

Se recebeu críticas, não leve para o lado pessoal. Críticas técnicas são sobre o projeto, não sobre você. Use-as para melhorar.

---

## Exercícios Práticos

### Exercício 1: Prepare o Roteiro

Escreva o roteiro da sua apresentação com:
1. O que você vai falar em cada parte (problema, solução, demo, decisões)
2. Quanto tempo cada parte deve durar
3. Quais diagramas vai mostrar
4. Quais funcionalidades vai demonstrar ao vivo

### Exercício 2: Prepare a Demonstração

1. Crie um arquivo `demo.sh` com todos os comandos curl que você vai usar
2. Prepare dados de exemplo que mostrem as funcionalidades
3. Teste a demonstração completa do início ao fim
4. Prepare o plano B (screenshots ou video)

### Exercício 3: Ensaie

1. Apresente para você mesmo cronometrando (alvo: 15-20 minutos)
2. Apresente para um colega ou familiar e peça feedback
3. Ajuste o roteiro com base no feedback
4. Ensaie a demonstração ao vivo pelo menos 2 vezes

### Exercício 4: Prepare Respostas para Perguntas

1. Liste 10 perguntas que um avaliador poderia fazer sobre seu projeto
2. Escreva respostas curtas e claras para cada uma
3. Inclua perguntas sobre: tecnologia escolhida, arquitetura, limitações, o que faria diferente
4. Peça para um colega fazer as perguntas e pratique responder em voz alta

### Exercício 5: Grave um Video

1. Grave a apresentação completa (slides + demonstração)
2. Assista ao video e anote pontos de melhoria
3. Preste atenção em: velocidade da fala, clareza, contato visual, tempo total
4. Regrave se necessário

Gravar e assistir a si mesmo e desconfortavel, mas e a forma mais eficaz de melhorar. Você vai perceber habitos que não nota ao vivo (falar rápido demais, olhar para baixo, usar "tipo" e "ne" em excesso).

---

## Conclusão do Capítulo 12

Este capítulo te guiou pelo processo completo de construir um projeto do zero:

1. Definir o problema e planejar (módulo 12.1)
2. Modelar dados e projetar arquitetura (módulo 12.2)
3. Desenvolver incrementalmente (módulo 12.3)
4. Documentar com qualidade (módulo 12.4)
5. Apresentar e defender (módulo 12.5)
6. Usar IA como ferramenta (módulo 12.6)

Esse processo não é exclusivo do TCC — e o processo que desenvolvedores profissionais usam todos os dias. A escala muda, as ferramentas mudam, mas os princípios são os mesmos.

Você está pronto.


### Nota sobre Comunicação Técnica

Saber programar é essencial, mas saber comunicar o que você programou é igualmente importante. Na carreira de desenvolvedor, você vai precisar explicar decisões técnicas para pessoas não-técnicas (gerentes, clientes, stakeholders), defender suas escolhas em code reviews, e documentar sistemas para outros desenvolvedores. A apresentação do TCC é uma oportunidade de praticar essa habilidade.

### Dicas para Apresentações Técnicas

| Dica | Por que funciona |
|------|-----------------|
| Comece pelo problema, não pela solução | O público precisa entender o contexto antes de avaliar a solução |
| Use diagramas em vez de texto | Arquitetura é visual — um diagrama vale mais que mil palavras |
| Mostre o sistema funcionando | Demo ao vivo impressiona mais que slides |
| Prepare-se para perguntas difíceis | Antecipar objeções mostra domínio do assunto |
| Pratique o tempo | Respeitar o tempo mostra profissionalismo |

### Estrutura Sugerida para a Apresentação

Uma apresentação técnica eficiente segue esta estrutura:

1. **O Problema** (2 min) — Qual problema você resolveu e por que importa
2. **A Solução** (3 min) — Como você resolveu, quais tecnologias usou e por quê
3. **Arquitetura** (3 min) — Diagrama de camadas, fluxo de dados, decisões técnicas
4. **Demo** (5 min) — Mostrar o sistema funcionando com cenários reais
5. **Aprendizados** (2 min) — O que deu certo, o que faria diferente, próximos passos

### Erros Comuns em Apresentações Técnicas

| Erro | Consequência | Como evitar |
|------|-------------|-------------|
| Começar pelo código | Público se perde sem contexto | Sempre começar pelo problema |
| Slides com muito texto | Ninguém lê, apresentador vira leitor | Máximo 6 linhas por slide |
| Demo sem plano B | Se falhar, apresentação trava | Ter screenshots ou vídeo gravado |
| Não ensaiar | Estoura o tempo, esquece pontos | Ensaiar pelo menos 3 vezes |
| Ignorar perguntas | Parece inseguro | Responder com honestidade, "não sei" é válido |

---

[← Anterior: Documentação Técnica](cap13-mod04-documentação.md) · [Próximo: Usando IA no Desenvolvimento →](cap13-mod06-ia-no-desenvolvimento.md)
