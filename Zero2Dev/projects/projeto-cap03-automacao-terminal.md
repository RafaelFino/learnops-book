# Projeto do Capítulo 3 — Automação com o Terminal

[← Voltar ao Capítulo 3](../capitulos/cap03-mod06-ferramentas-rede.md)

---

## Visão Geral

Neste projeto, você vai usar tudo que aprendeu sobre o terminal para automatizar tarefas reais. Em vez de fazer coisas manualmente — clicar, arrastar, renomear arquivo por arquivo — você vai criar comandos que fazem o trabalho por você em segundos.

Automação é uma das habilidades mais valorizadas em tecnologia. Profissionais que sabem automatizar tarefas repetitivas economizam horas de trabalho e reduzem erros. Este projeto vai te dar uma amostra desse poder.

---

## Objetivo

Criar um conjunto de comandos e um script simples que automatizem tarefas do dia a dia usando o terminal, aplicando os conceitos de navegação, pipes, redirecionamento e ferramentas de rede aprendidos no capítulo 3.

---

## O que Você Vai Aprender

- Como encadear comandos para resolver problemas reais
- Como usar pipes e redirecionamento para processar informações
- Como criar um script bash simples que automatiza uma tarefa
- Como documentar comandos e seus resultados

---

## Pré-requisitos

- Ter lido todos os módulos do capítulo 3 (3.1 a 3.6)
- Ter um ambiente Linux funcionando (do projeto do capítulo 2)
- Saber abrir e usar o terminal

---

## Instruções Passo a Passo

### Etapa 1 — Organização Automática de Arquivos

Crie uma estrutura de teste e organize automaticamente:

```bash
# Criar pasta de teste com arquivos misturados
mkdir -p ~/projetos/organizador
cd ~/projetos/organizador

# Criar arquivos de exemplo
touch relatorio.txt notas.txt foto1.jpg foto2.jpg musica.mp3 video.mp4 script.sh dados.csv

# Criar subpastas por tipo
mkdir -p documentos imagens audio video scripts dados

# Mover arquivos para as pastas corretas
mv *.txt documentos/
mv *.jpg imagens/
mv *.mp3 audio/
mv *.mp4 video/
mv *.sh scripts/
mv *.csv dados/

# Verificar resultado
ls -R
```

Documente: o que cada comando faz e por que funciona.

### Etapa 2 — Análise de Informações com Pipes

Use pipes para extrair informações úteis:

```bash
# Contar quantos arquivos existem em cada subpasta
find ~/projetos/organizador -type f | wc -l

# Listar todos os arquivos ordenados por tamanho
ls -lhS ~/projetos/organizador/**/*

# Encontrar os 5 maiores arquivos do sistema
du -ah /home | sort -rh | head -5

# Contar quantas linhas tem um arquivo
cat /etc/passwd | wc -l

# Filtrar apenas usuários com shell bash
grep "bash" /etc/passwd | cut -d: -f1
```

Conecte com o módulo 3.3: explique como o pipe (`|`) conecta a saída de um comando com a entrada do próximo.

### Etapa 3 — Monitoramento do Sistema

Use os comandos de monitoramento para entender o estado do seu sistema:

```bash
# Ver processos em execução (os 10 que mais usam CPU)
ps aux --sort=-%cpu | head -11

# Ver uso de memória
free -h

# Ver uso de disco
df -h

# Ver processos em tempo real (saia com 'q')
top -n 1
```

Conecte com o módulo 3.4: documente o que cada coluna significa na saída do `ps`.

### Etapa 4 — Busca de Informações na Rede

Use as ferramentas de rede para buscar informações:

```bash
# Verificar se um site está acessível
curl -I https://www.google.com 2>/dev/null | head -5

# Baixar um arquivo de exemplo
wget -q https://raw.githubusercontent.com/RafaelFino/learn-ops-content/main/README.md -O readme-exemplo.md

# Ver o conteúdo baixado
head -20 readme-exemplo.md
```

Conecte com o módulo 3.6: explique a diferença entre `curl` e `wget`.

### Etapa 5 — Criar um Script de Automação

Crie seu primeiro script bash que automatiza uma tarefa:

```bash
# Criar o script
cat > ~/projetos/organizador/relatorio.sh << 'EOF'
#!/bin/bash
# Script: Relatorio do Sistema
# Autor: [Seu Nome]
# Data: [Data de hoje]

echo "=== Relatorio do Sistema ==="
echo ""
echo "--- Data e Hora ---"
date
echo ""
echo "--- Usuario ---"
whoami
echo ""
echo "--- Uso de Disco ---"
df -h /
echo ""
echo "--- Uso de Memoria ---"
free -h
echo ""
echo "--- Processos Ativos ---"
ps aux | wc -l
echo ""
echo "--- Arquivos no Projeto ---"
find ~/projetos/organizador -type f | wc -l
echo ""
echo "=== Fim do Relatorio ==="
EOF

# Dar permissão de execução
chmod +x ~/projetos/organizador/relatorio.sh

# Executar
bash ~/projetos/organizador/relatorio.sh
```

Conecte com o módulo 2.8: explique o que o `#!/bin/bash` faz e por que precisamos do `chmod +x`.

### Etapa 6 — Salvar Resultado em Arquivo

Use redirecionamento para salvar a saída do script:

```bash
# Salvar saída em arquivo
bash ~/projetos/organizador/relatorio.sh > ~/projetos/organizador/relatorio-saida.txt

# Verificar o arquivo salvo
cat ~/projetos/organizador/relatorio-saida.txt
```

Conecte com o módulo 3.3: explique a diferença entre `>` (sobrescrever) e `>>` (adicionar ao final).

### Etapa 7 — Montar o Relatório Final

Crie um documento com:

```
# Automação com Terminal — [Seu Nome]

## Etapa 1: Organização de Arquivos
- Comandos usados: ...
- O que aprendi: ...

## Etapa 2: Pipes
- Comandos mais úteis: ...
- Como o pipe funciona: ...

## Etapa 3: Monitoramento
- Estado do meu sistema: ...
- O que cada coluna do ps significa: ...

## Etapa 4: Ferramentas de Rede
- Diferença entre curl e wget: ...

## Etapa 5: Script
- O que meu script faz: ...
- O que é #!/bin/bash: ...
- O que é chmod +x: ...

## Reflexão
- Qual comando foi mais útil?
- O que você automatizaria no seu dia a dia?
- Você se sente confortável criando scripts?
```

---

## Entregáveis

- Relatório completo em Markdown
- O script `relatorio.sh` funcionando
- A saída do script salva em `relatorio-saida.txt`

---

## Critérios de Avaliação

Seu projeto está pronto quando:

- [ ] Arquivos organizados automaticamente por tipo
- [ ] Pipes usados para extrair informações do sistema
- [ ] Monitoramento do sistema documentado
- [ ] Ferramentas de rede utilizadas com sucesso
- [ ] Script bash criado, com permissão de execução, e funcionando
- [ ] Saída do script salva em arquivo via redirecionamento
- [ ] Relatório completo com conexões aos módulos do capítulo

---

## Dicas

- Teste cada comando individualmente antes de encadear com pipes
- Se um comando der erro, leia a mensagem de erro com atenção — ela geralmente diz o que está errado
- Use `man <comando>` para ver o manual de qualquer comando
- Não decore comandos — entenda o que cada parte faz. Com o tempo, os mais usados ficam naturais

---

## Mídias Recomendadas

- **Mr. Robot** (série, 2015-2019) — o protagonista usa o terminal Linux extensivamente. Observe como ele encadeia comandos e automatiza tarefas.
- **The Art of Command Line** (GitHub) — guia prático e conciso sobre dominar o terminal. Excelente referência para ir além do básico: https://github.com/jlevy/the-art-of-command-line

---

[← Voltar ao Capítulo 3](../capitulos/cap03-mod06-ferramentas-rede.md)
