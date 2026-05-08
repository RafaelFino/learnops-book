# 8.1 — Exercícios: O que são Bancos de Dados

[← Voltar ao conteúdo: O que são Bancos de Dados](cap08-mod01-intro-bancos-conteudo.md)

---

## Sobre Estes Exercícios

Estes exercícios cobrem os conceitos do módulo 8.1: persistência de dados, problemas de usar arquivos, evolução dos bancos de dados, ACID, banco como recurso externo e tipos de bancos. A maioria é conceitual e de reflexão — o código começa no módulo 8.4.

---

## Exercício 1: Dados que Desaparecem (Reflexão)

Liste 5 aplicativos ou sistemas que você usa no dia a dia (redes sociais, bancos, lojas, jogos, etc.). Para cada um, responda:

a) Que tipos de dados ele armazena? (textos, imagens, números, datas...)
b) O que aconteceria se todos esses dados fossem perdidos de uma hora para outra?
c) Quantos registros você estima que o sistema tenha no total, considerando todos os usuários do mundo?
d) Esse sistema provavelmente usa banco relacional, NoSQL ou ambos? Justifique.

**Dica**: pense em sistemas variados — um banco financeiro tem necessidades muito diferentes de um jogo online.

**Exemplo de resposta para o WhatsApp**:
- Dados: mensagens de texto, imagens, vídeos, contatos, status de entrega, grupos
- Se perdesse: bilhões de conversas perdidas, impacto pessoal e profissional enorme
- Estimativa: mais de 100 bilhões de mensagens por dia, trilhões de registros no total
- Provavelmente ambos: relacional para cadastro de usuários e grupos, NoSQL para mensagens (volume massivo)

---

## Exercício 2: Problemas de Arquivos (Análise)

Releia o exemplo do programa `produtos_arquivo.py` do módulo e responda:

a) O que acontece se dois programas tentarem salvar no mesmo arquivo `produtos.json` ao mesmo tempo? Descreva passo a passo o que pode dar errado.

b) Imagine que o arquivo `produtos.json` tem 1 milhão de produtos. Quanto tempo você estima que levaria para encontrar um produto específico pelo nome? E se tivesse 100 milhões? Explique por que fica lento.

c) Se o computador desligar no exato momento em que o programa está escrevendo o arquivo (entre o `open()` e o `json.dump()`), o que acontece com os dados? O arquivo fica corrompido? Explique.

d) Por que a abordagem de arquivo funciona para um programa pessoal (lista de compras, por exemplo) mas não para um sistema com milhares de usuários simultâneos (como um e-commerce)?

e) Proponha uma solução para o problema de acesso simultâneo usando apenas arquivos (sem banco de dados). Quais seriam as limitações da sua solução?

---

## Exercício 3: ACID no Dia a Dia (Aplicação)

O conceito ACID (Atomicidade, Consistência, Isolamento, Durabilidade) aparece em muitas situações do mundo real, não apenas em bancos de dados. Para cada cenário abaixo, identifique qual propriedade ACID está sendo violada e explique o que daria errado:

a) **Transferência bancária**: o sistema debita R$ 500 da conta A, mas trava antes de creditar na conta B. O dinheiro "sumiu".

b) **Compra online**: dois clientes compram o último item em estoque ao mesmo tempo. Ambos recebem confirmação de compra, mas só existe 1 unidade.

c) **Cadastro de aluno**: o sistema cadastra o aluno na turma, mas uma queda de energia apaga o registro antes de ser gravado no disco.

d) **Atualização de preço**: enquanto o gerente atualiza o preço de um produto de R$ 10 para R$ 15, um cliente faz uma compra e paga R$ 10 (o preço antigo que ainda estava na tela).

e) Para cada cenário, explique como um banco de dados com ACID resolveria o problema.

---

## Exercício 4: Recurso Externo (Conceitual)

O módulo explica que o banco de dados é o primeiro "recurso externo" que você vai usar — algo que existe fora do seu programa.

a) Usando a analogia do restaurante (aplicação = cliente, banco = cozinha), descreva o que acontece em cada etapa quando seu programa Python quer buscar todos os produtos com preço maior que R$ 10:
   - O que o "cliente" faz?
   - O que o "garçom" (conector) faz?
   - O que a "cozinha" (banco) faz?
   - O que volta para o "cliente"?

b) Liste 3 outros exemplos de "recursos externos" que programas usam no mundo real (além de bancos de dados). Para cada um, explique por que é externo e não interno ao programa.

c) Quais problemas podem acontecer quando seu programa depende de um recurso externo? Liste pelo menos 3 problemas e como você lidaria com cada um.

---

## Exercício 5: Evolução dos Bancos de Dados (Pesquisa)

Pesquise e escreva um parágrafo (5-8 linhas) sobre cada tema:

a) **Edgar Codd e a IBM**: Codd publicou o modelo relacional em 1970 enquanto trabalhava na IBM. Mas a IBM demorou mais de 10 anos para implementar o modelo (DB2 só saiu em 1983). Por que a IBM resistiu? O que aconteceu nesse meio tempo?

b) **DB-Engines Ranking**: Acesse o site db-engines.com e veja o ranking atual dos bancos de dados mais populares. Quais são os 5 primeiros? Quantos são relacionais e quantos são NoSQL? O ranking mudou nos últimos 5 anos?

c) **SQLite no mundo**: O módulo menciona que o SQLite é "provavelmente o banco mais implantado do planeta". Pesquise: em quais dispositivos e aplicações o SQLite está embutido? Por que ele é tão popular para uso embutido?

d) **Oracle e Larry Ellison**: Larry Ellison leu o artigo de Codd e criou a Oracle. Pesquise a história: como Ellison conseguiu criar um banco relacional comercial antes da própria IBM? O que isso nos ensina sobre inovação?

---

## Exercício 6: Tipos de Bancos de Dados (Classificação)

Para cada cenário abaixo, escolha o tipo de banco de dados mais adequado (Relacional, Documentos, Chave-Valor, Grafos ou Colunar) e justifique sua escolha:

a) Sistema de folha de pagamento de uma empresa com 5.000 funcionários. Precisa calcular salários, descontos, impostos e gerar relatórios mensais.

b) Aplicativo de delivery de comida que precisa armazenar cardápios de restaurantes. Cada restaurante tem pratos com atributos diferentes (pizza tem tamanho e sabor, sushi tem quantidade de peças, hambúrguer tem ponto da carne).

c) Sistema de recomendação da Netflix que precisa saber "quem assistiu o quê" e "filmes similares a este" para sugerir novos títulos.

d) Sistema de cache para um site de notícias que recebe 10 milhões de visitas por dia. Precisa armazenar temporariamente as páginas mais acessadas para não sobrecarregar o banco principal.

e) Sistema de análise de logs de uma empresa que gera 500 GB de logs por dia. Precisa responder perguntas como "quantos erros 500 tivemos na última hora?" e "qual endpoint é mais lento?".

f) Sistema de controle de estoque de um supermercado com 50.000 produtos, fornecedores, compras e vendas.

---

## Exercício 7: Comparando Abordagens (Código e Análise)

Análise os dois trechos de código abaixo. Ambos fazem a mesma coisa: armazenam e buscam produtos. O primeiro usa arquivo JSON, o segundo usa banco de dados (pseudocódigo).

**Abordagem 1: Arquivo JSON**

```python
# Buscar produto por ID em arquivo JSON
import json

def find_product_by_id(product_id):
    # "find" = encontrar, "product" = produto
    with open("produtos.json", "r") as file:
        products = json.load(file)  # carrega TODOS os produtos
    for product in products:  # percorre um por um
        if product["id"] == product_id:
            return product
    return None
```

**Abordagem 2: Banco de dados (pseudocódigo)**

```python
# Buscar produto por ID no banco de dados
def find_product_by_id(product_id):
    # "query" = consulta
    query = "SELECT * FROM produtos WHERE id = ?"
    result = database.execute(query, (product_id,))
    return result  # banco usa indice, vai direto ao registro
```

Responda:

a) Se o arquivo/banco tem 10 produtos, qual abordagem é mais rápida? E se tem 10 milhões?

b) Qual é a complexidade Big O de cada abordagem? (Lembre-se do capítulo 5.17)

c) A abordagem 1 carrega todos os produtos na memória RAM. Se cada produto ocupa 1 KB e existem 10 milhões de produtos, quanta RAM seria necessária? Isso é viável?

d) Na abordagem 2, o banco usa um índice. Que estrutura de dados você acha que o banco usa internamente para esse índice? (Dica: você estudou no capítulo 7)

---

## Exercício 8: Projeto de Reflexão — Seu Sistema Ideal

Imagine que você foi contratado para criar um sistema de gerenciamento para uma biblioteca do seu bairro. O sistema precisa:

- Cadastrar livros (título, autor, ISBN, ano, editora)
- Cadastrar membros (nome, email, telefone)
- Registrar empréstimos e devoluções
- Controlar multas por atraso
- Gerar relatórios (livros mais emprestados, membros com multas pendentes)

Responda:

a) Que tipo de banco de dados você usaria? Justifique.

b) Liste todas as entidades que o sistema precisaria (não precisa detalhar colunas ainda — isso é tema do módulo 8.3).

c) Quais problemas aconteceriam se você usasse apenas arquivos JSON para esse sistema?

d) Quais propriedades ACID são mais importantes para esse sistema? Dê um exemplo concreto de cada uma.

e) O sistema precisa funcionar com acesso simultâneo (vários bibliotecários usando ao mesmo tempo)?  Se sim, como o banco de dados ajuda nisso?

---

## Gabarito Comentado

### Exercício 3 — ACID no Dia a Dia

a) **Atomicidade** violada. A transação (débito + crédito) não foi executada como "tudo ou nada" — apenas metade aconteceu. Com ACID, se o crédito falhar, o débito é automaticamente revertido (rollback).

b) **Isolamento** violado. As duas transações de compra não foram isoladas uma da outra — ambas viram o estoque como 1 e prosseguiram. Com ACID, o banco bloquearia o registro do estoque para a primeira transação, e a segunda esperaria ou receberia erro.

c) **Durabilidade** violada. O dado foi confirmado mas não sobreviveu à falha. Com ACID, o banco usa write-ahead logging (WAL) — grava a operação em um log antes de confirmar, permitindo recuperação após falhas.

d) **Isolamento** violado. O cliente leu um dado que estava sendo modificado por outra transação. Com ACID, o banco garantiria que o cliente vê o preço antigo OU o novo, nunca um estado intermediário.

### Exercício 6 — Tipos de Bancos

a) **Relacional** — dados altamente estruturados com relacionamentos claros (funcionário → departamento → empresa), necessidade de integridade absoluta (não pode errar salário), relatórios com JOINs e agregações.

b) **Documentos** — cada restaurante tem atributos diferentes, schema flexível é ideal. Um documento JSON por prato permite campos variáveis sem alterar a estrutura do banco.

c) **Grafos** — o problema é essencialmente sobre relacionamentos: "quem assistiu o quê", "filmes similares". Grafos representam essas conexões naturalmente e permitem consultas como "encontre filmes assistidos por pessoas que assistiram os mesmos filmes que eu".

d) **Chave-Valor** — acesso extremamente rápido por chave (URL da página), dados temporários (cache expira), não precisa de consultas complexas. Redis é a escolha clássica.

e) **Colunar** — consultas analíticas em grandes volumes de dados, lendo apenas as colunas necessárias (timestamp, status_code, endpoint) de bilhões de registros. ClickHouse ou similar.

f) **Relacional** — dados estruturados com relacionamentos claros (produto → fornecedor, venda → produto → cliente), necessidade de integridade (estoque não pode ficar negativo), relatórios com JOINs.

### Exercício 7 — Comparando Abordagens

a) Com 10 produtos, ambas são praticamente instantâneas — a diferença é imperceptível. Com 10 milhões, o arquivo precisa carregar tudo na memória e percorrer um por um (segundos ou minutos), enquanto o banco usa índice e encontra em milissegundos.

b) Arquivo: O(n) — busca linear, percorre todos os registros. Banco com índice: O(log n) — busca binária na árvore B do índice.

c) 10 milhões × 1 KB = 10 GB de RAM. A maioria dos computadores pessoais tem 8-16 GB de RAM total. Carregar 10 GB só para buscar um produto é inviável — não sobraria memória para o sistema operacional e outros programas.

d) O banco provavelmente usa uma **árvore B** (B-tree) — a estrutura que vimos no capítulo 7 quando falamos sobre busca eficiente. Árvores B são otimizadas para acesso em disco e permitem busca em O(log n).

---

[← Voltar ao conteúdo: O que são Bancos de Dados](cap08-mod01-intro-bancos-conteudo.md)
