# Projeto do Capítulo 4 — Criando e Gerenciando um Repositório Git

[← Voltar ao Capítulo 4](../capitulos/cap04-mod04-branches-merges.md)

---

## Visão Geral

Neste projeto, você vai criar seu primeiro repositório Git do zero, praticar os comandos essenciais e simular um fluxo de trabalho real com branches e merges. Git é a ferramenta de controle de versão mais usada no mundo — praticamente todo projeto de software usa Git. Dominar o básico agora vai te dar confiança para trabalhar em qualquer equipe.

Pense neste projeto como montar sua primeira "máquina do tempo" para código. Você vai criar pontos de salvamento (commits), explorar linhas alternativas do tempo (branches) e juntar tudo no final (merge).

---

## Objetivo

Criar um repositório Git local, praticar o ciclo completo de versionamento (add, commit, branch, merge) e publicar o resultado no GitHub, documentando cada passo.

---

## O que Você Vai Aprender

- Como inicializar um repositório Git
- Como fazer commits com mensagens descritivas
- Como criar e alternar entre branches
- Como fazer merge de branches
- Como publicar um repositório no GitHub
- Como documentar um projeto com README

---

## Pré-requisitos

- Ter lido todos os módulos do capítulo 4 (4.1 a 4.4)
- Ter Git instalado (do projeto do capítulo 2)
- Ter uma conta no GitHub (gratuita)
- Saber usar o terminal

---

## Instruções Passo a Passo

### Etapa 1 — Configurar o Git

Se ainda não configurou, faça agora:

```bash
# Configurar nome e email
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Verificar configuração
git config --list
```

### Etapa 2 — Criar o Repositório

```bash
# Criar pasta do projeto
mkdir ~/projetos/meu-primeiro-repo
cd ~/projetos/meu-primeiro-repo

# Inicializar o Git
git init

# Verificar que o Git foi inicializado
ls -la  # Deve mostrar a pasta .git
git status
```

Conecte com o módulo 4.2: explique o que a pasta `.git` contém e por que ela é importante.

### Etapa 3 — Primeiro Commit

Crie um arquivo README e faça seu primeiro commit:

```bash
# Criar o README
cat > README.md << 'EOF'
# Meu Primeiro Repositório

Este é o meu primeiro projeto usando Git.
Estou aprendendo controle de versão no curso De Zero a Dev.

## Sobre
- Autor: [Seu Nome]
- Data: [Data de hoje]
- Capítulo: 4 — Controle de Versão com Git
EOF

# Adicionar ao staging
git add README.md

# Verificar status
git status

# Fazer o commit
git commit -m "docs: add initial README"

# Ver o histórico
git log
```

Conecte com o módulo 4.2: explique a diferença entre `git add` (staging) e `git commit` (salvar).

### Etapa 4 — Adicionar Mais Conteúdo

```bash
# Criar um arquivo de anotações
cat > anotacoes.md << 'EOF'
# Anotações do Curso

## Capítulo 1 — Fundamentos
- Computador = CPU + RAM + Armazenamento
- CPU é o "cozinheiro", RAM é a "bancada"

## Capítulo 2 — Linux
- Linux é open source
- Estrutura de diretórios: /, /home, /etc, /var

## Capítulo 3 — Terminal
- Pipes conectam saída de um comando com entrada de outro
- Redirecionamento: > sobrescreve, >> adiciona
EOF

# Adicionar e commitar
git add anotacoes.md
git commit -m "docs: add course notes"

# Ver histórico com 2 commits
git log --oneline
```

### Etapa 5 — Trabalhar com Branches

Agora vamos simular um fluxo de trabalho real:

```bash
# Criar uma branch para adicionar conteúdo novo
git checkout -b feature/capitulo-4-notas

# Verificar em qual branch está
git branch

# Adicionar conteúdo na branch
cat >> anotacoes.md << 'EOF'

## Capítulo 4 — Git
- Git é uma "máquina do tempo" para código
- Commits são pontos de salvamento
- Branches são linhas alternativas do tempo
- Merge junta branches de volta
EOF

# Commitar na branch
git add anotacoes.md
git commit -m "docs: add chapter 4 notes"

# Ver que a branch tem um commit a mais
git log --oneline
```

Conecte com o módulo 4.4: explique o que é uma branch e por que usamos branches em vez de trabalhar direto na main.

### Etapa 6 — Fazer Merge

```bash
# Voltar para a main
git checkout main

# Ver que o arquivo NÃO tem as notas do cap 4 (está na outra branch)
cat anotacoes.md

# Fazer merge da branch
git merge feature/capitulo-4-notas

# Ver que agora o arquivo TEM as notas do cap 4
cat anotacoes.md

# Ver o histórico completo
git log --oneline --graph

# Deletar a branch (já foi mergeada)
git branch -d feature/capitulo-4-notas
```

### Etapa 7 — Publicar no GitHub

1. Acesse https://github.com e crie um novo repositório (sem README, sem .gitignore)
2. Copie a URL do repositório
3. No terminal:

```bash
# Adicionar o repositório remoto
git remote add origin https://github.com/SEU-USUARIO/meu-primeiro-repo.git

# Enviar para o GitHub
git push -u origin main
```

4. Acesse o repositório no GitHub e verifique que os arquivos estão lá

Conecte com o módulo 4.3: explique a diferença entre repositório local e remoto.

### Etapa 8 — Montar o Relatório

Adicione ao README do repositório:

```markdown
## O que Aprendi

### Comandos Git que Usei
| Comando | O que faz |
|---------|-----------|
| git init | Inicializa um repositório |
| git add | Adiciona arquivos ao staging |
| git commit | Salva um ponto no histórico |
| git branch | Lista ou cria branches |
| git checkout | Alterna entre branches |
| git merge | Junta branches |
| git push | Envia para o repositório remoto |

### Reflexão
1. O que é mais difícil no Git: entender os conceitos ou memorizar os comandos?
2. Por que branches são úteis em projetos com múltiplas pessoas?
3. O que aconteceria se duas pessoas editassem o mesmo arquivo ao mesmo tempo?
```

---

## Entregáveis

- Repositório Git local com pelo menos 3 commits
- Pelo menos 1 branch criada e mergeada
- Repositório publicado no GitHub
- README completo com tabela de comandos e reflexão

---

## Critérios de Avaliação

Seu projeto está pronto quando:

- [ ] Repositório inicializado com `git init`
- [ ] Pelo menos 3 commits com mensagens descritivas
- [ ] Branch criada, usada e mergeada
- [ ] Repositório publicado no GitHub
- [ ] README com tabela de comandos e reflexão
- [ ] Histórico do Git mostra o fluxo completo (`git log --oneline --graph`)

---

## Dicas

- Faça commits pequenos e frequentes — é melhor ter 10 commits pequenos do que 1 gigante
- Mensagens de commit devem explicar O QUE mudou, não COMO mudou
- Se algo der errado, `git status` é seu melhor amigo — ele sempre mostra o estado atual
- Não tenha medo de criar branches — elas são baratas e fáceis de deletar

---

## Mídias Recomendadas

- **Learn Git Branching** (tutorial interativo) — o melhor recurso visual para entender branches e merges. Faça os exercícios: https://learngitbranching.js.org/?locale=pt_BR
- **Oh My Git!** (jogo) — aprenda Git jogando. Divertido e educativo: https://ohmygit.org/
- **Fabio Akita — Git** (YouTube) — explicação profunda de como Git funciona por dentro, para quem quer ir além do básico.

---

[← Voltar ao Capítulo 4](../capitulos/cap04-mod04-branches-merges.md)
