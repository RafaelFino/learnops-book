# 3.2 — Comandos Básicos: Navegação e Manipulação de Arquivos

[← Anterior: Terminal vs Interpretador de Comandos](cap03-mod01-terminal-vs-shell.md) · [Próximo: Pipes e Redirecionamento →](cap03-mod03-pipes-redirecionamento.md)

---

## Introdução

No módulo anterior, desmontamos a "caixa preta" do terminal e entendemos que ele é composto por três camadas: o emulador (a janela), o shell (o interpretador) e o kernel (o executor). Agora que sabemos como as peças se encaixam, é hora de usar essa máquina de verdade.

No Capítulo 2, já usamos vários comandos ao longo dos módulos — `ls` para listar arquivos, `cd` para navegar entre diretórios, `chmod` para mudar permissões, `apt` para instalar pacotes. Mas usamos esses comandos de forma pontual, para resolver problemas específicos de cada módulo. Nunca paramos para estudar os comandos em si — suas opções, variações e combinações.

Este módulo é diferente. Aqui vamos estudar os comandos de navegação e manipulação de arquivos de forma **sistemática e profunda**. Vamos entender não apenas o que cada comando faz, mas **por que** ele existe, **como** funciona internamente e **quando** usar cada opção.

Lembre-se: **"Conceitos são para sempre, ferramentas apenas os implementam."** Os conceitos de navegação em sistemas de arquivos, criação, cópia, movimentação e remoção de arquivos existem em todo sistema operacional. O que muda são os nomes dos comandos. Se você entender o conceito por trás de cada operação, vai se sentir em casa em qualquer sistema — Linux, macOS, Windows ou até sistemas que ainda não foram inventados.

E aqui vai o outro mantra: **"Qual problema você quer resolver?"** Cada comando que vamos estudar existe porque resolve um problema real. O `find` existe porque projetos grandes têm milhares de arquivos e você precisa encontrar um específico. O `grep` existe porque logs de servidores têm milhões de linhas e você precisa achar a que contém o erro. O `tar` existe porque enviar 500 arquivos separados pela rede é impraticável.

Vamos começar pelo mais fundamental: saber onde você está e para onde pode ir.

---

## A Anatomia de um Comando

Antes de estudar comandos específicos, vamos entender a estrutura que todo comando segue. No módulo 2.8, já vimos comandos sendo usados, mas nunca formalizamos a estrutura.

Todo comando no terminal segue este formato:

```
comando [opcoes] [argumentos]
```

| Parte | O que e | Exemplo |
|-------|---------|---------|
| Comando | O programa a ser executado | `ls`, `cp`, `mkdir` |
| Opcoes | Modificadores do comportamento, comecam com `-` ou `--` | `-l`, `-a`, `--help` |
| Argumentos | Os alvos do comando, sobre o que ele age | `/home`, `arquivo.txt` |

Exemplo concreto:

```bash
ls -la /home/ana
```

- `ls` — o comando (listar arquivos)
- `-la` — as opções (`-l` = formato longo, `-a` = incluir ocultos)
- `/home/ana` — o argumento (qual diretório listar)

### Opções Curtas e Longas

A maioria dos comandos aceita opções em dois formatos:

| Formato | Exemplo | Significado |
|---------|---------|-------------|
| Curto, uma letra | `-l` | Formato longo |
| Curto, combinado | `-la` | Mesmo que `-l -a` |
| Longo, palavra | `--all` | Incluir ocultos |
| Longo com valor | `--color=auto` | Cor automática |

```bash
# Estes tres comandos fazem a mesma coisa:
ls -l -a
ls -la
ls --all -l
```

As opções curtas podem ser combinadas: `-la` é o mesmo que `-l -a`. Isso não funciona com opções longas — `--all` não pode ser combinado com outras.

### Obtendo Ajuda sobre Comandos

Quando você não sabe o que um comando faz ou quais opções ele aceita, existem várias formas de descobrir:

```bash
# Forma 1: opcao --help (quase todo comando tem)
ls --help

# Forma 2: manual completo (man = manual)
man ls

# Forma 3: resumo rapido (whatis)
whatis ls

# Forma 4: onde o comando esta instalado
which ls

# Forma 5: tipo do comando (builtin, alias, programa)
type ls
```

Saída esperada (whatis ls):
```
ls (1)               - list directory contents
```

Saída esperada (which ls):
```
/usr/bin/ls
```

Saída esperada (type ls):
```
ls is aliased to 'ls --color=auto'
```

O comando `man` (manual) é o mais completo. Ele abre uma página de documentação detalhada que você navega com as setas do teclado e sai com a tecla `q`. As páginas do man são organizadas em seções:

| Seção | Conteúdo |
|-------|----------|
| NAME | Nome e descrição curta |
| SYNOPSIS | Formato de uso |
| DESCRIPTION | Descrição detalhada |
| OPTIONS | Todas as opcoes disponiveis |
| EXAMPLES | Exemplos de uso |
| SEE ALSO | Comandos relacionados |

```bash
# Abrir o manual do comando cp
man cp

# Navegar: setas para cima/baixo, q para sair
# Buscar: / seguido do texto, n para proximo resultado
```

---

## Navegação: Sabendo Onde Você Está e Para Onde Ir

### pwd — Onde Estou?

O comando `pwd` (print working directory, ou "imprimir diretório de trabalho") mostra o caminho completo do diretório onde você está agora.

```bash
# Onde estou?
pwd
```

Saída esperada:
```
/home/ana
```

Parece simples, mas é um dos comandos mais importantes. Quando você está perdido em uma estrutura de diretórios complexa, `pwd` é seu GPS. Muitos erros de iniciantes acontecem porque a pessoa acha que está em um diretório mas está em outro.

### cd — Mudando de Diretório

O comando `cd` (change directory, ou "mudar diretório") é como andar pelos corredores de um prédio. Você sai de uma sala e entra em outra.

```bash
# Ir para um diretorio especifico (caminho absoluto)
cd /home/ana/projetos

# Ir para um subdiretorio (caminho relativo)
cd projetos

# Voltar um diretorio (diretorio pai)
cd ..

# Voltar dois diretorios
cd ../..

# Ir para o diretorio home
cd ~
# ou simplesmente:
cd

# Ir para o diretorio anterior (onde voce estava antes)
cd -

# Ir para a raiz do sistema
cd /
```

Saída esperada (cd -):
```
/home/ana/projetos
```

O `cd -` é especialmente útil — ele funciona como o botão "voltar" do navegador. Se você estava em `/home/ana/projetos` e foi para `/etc/nginx`, o `cd -` te leva de volta para `/home/ana/projetos`.

### Caminhos Absolutos vs Relativos

Essa distinção é fundamental e já vimos brevemente no módulo 2.4 (Estrutura de Diretórios). Vamos reforçar:

| Tipo | Comeca com | Exemplo | Significado |
|------|-----------|---------|-------------|
| Absoluto | `/` | `/home/ana/projetos` | Caminho completo desde a raiz |
| Relativo | Sem `/` | `projetos` ou `./projetos` | Caminho a partir do diretório atual |
| Home | `~` | `~/projetos` | Caminho a partir do home do usuario |

```bash
# Suponha que voce esta em /home/ana

# Caminho absoluto: funciona de qualquer lugar
cd /home/ana/projetos/site

# Caminho relativo: depende de onde voce esta
cd projetos/site

# Os dois comandos acima levam ao mesmo lugar,
# mas o relativo so funciona se voce estiver em /home/ana
```

Os atalhos de diretório que você precisa memorizar:

| Símbolo | Significado | Exemplo |
|---------|-------------|---------|
| `.` | Diretório atual | `./script.sh` = script no diretório atual |
| `..` | Diretório pai, um nível acima | `cd ..` = subir um nível |
| `~` | Home do usuario atual | `cd ~` = ir para /home/ana |
| `~joao` | Home de outro usuario | `cd ~joao` = ir para /home/joao |
| `-` | Diretório anterior | `cd -` = voltar para onde estava |

### ls — Listando Conteúdo

O comando `ls` (list, ou "listar") mostra o conteúdo de um diretório. É provavelmente o comando que você mais vai usar na vida.

```bash
# Listar o diretorio atual
ls

# Listar um diretorio especifico
ls /etc

# Listar com detalhes (formato longo)
ls -l

# Listar incluindo arquivos ocultos
ls -a

# Listar com detalhes e ocultos (combinacao mais usada)
ls -la
```

Saída esperada (ls -la):
```
total 32
drwxr-xr-x  5 ana ana 4096 jan 15 10:30 .
drwxr-xr-x  3 root root 4096 jan 10 08:00 ..
-rw-r--r--  1 ana ana  220 jan 10 08:00 .bash_logout
-rw-r--r--  1 ana ana 3771 jan 10 08:00 .bashrc
drwxr-xr-x  2 ana ana 4096 jan 12 14:20 projetos
-rw-r--r--  1 ana ana  807 jan 10 08:00 .profile
-rw-r--r--  1 ana ana  150 jan 15 10:30 notas.txt
drwxr-xr-x  3 ana ana 4096 jan 14 09:15 scripts
```

Vamos decodificar cada coluna da saída do `ls -l`:

| Coluna | Exemplo | Significado |
|--------|---------|-------------|
| 1 | `drwxr-xr-x` | Tipo e permissões (d = diretório, - = arquivo) |
| 2 | `5` | Número de links |
| 3 | `ana` | Dono do arquivo |
| 4 | `ana` | Grupo do arquivo |
| 5 | `4096` | Tamanho em bytes |
| 6 | `jan 15 10:30` | Data da última modificacao |
| 7 | `projetos` | Nome do arquivo ou diretório |

As permissões (`drwxr-xr-x`) já estudamos em detalhes no módulo 2.5. Se não lembrar, volte e releia — é um dos conceitos mais importantes do Linux.

### Opções Úteis do ls

| Opcao | O que faz | Quando usar |
|-------|-----------|-------------|
| `-l` | Formato longo com detalhes | Quando precisa ver permissões, tamanho, data |
| `-a` | Mostra arquivos ocultos | Quando precisa ver .bashrc, .gitignore, etc. |
| `-h` | Tamanhos legiveis (KB, MB, GB) | Sempre que usar -l |
| `-R` | Recursivo, lista subdiretorios | Quando quer ver toda a árvore |
| `-t` | Ordena por data de modificacao | Quando quer ver os mais recentes primeiro |
| `-S` | Ordena por tamanho | Quando quer encontrar arquivos grandes |
| `-r` | Inverte a ordem | Combinar com -t ou -S |
| `-d` | Mostra o diretório em si, não o conteúdo | Quando quer ver permissões de um diretório |
| `--color` | Cores por tipo de arquivo | Geralmente ja e padrão |

```bash
# Combinacao mais util: detalhes + ocultos + tamanho legivel
ls -lah

# Listar por data, mais recente primeiro
ls -lt

# Listar por tamanho, maior primeiro
ls -lSh

# Listar por tamanho, menor primeiro (invertido)
ls -lShr

# Listar recursivamente (cuidado em diretorios grandes!)
ls -R

# Ver permissoes de um diretorio (nao do conteudo)
ls -ld /home/ana
```

Saída esperada (ls -lah):
```
total 32K
drwxr-xr-x  5 ana ana 4.0K jan 15 10:30 .
drwxr-xr-x  3 root root 4.0K jan 10 08:00 ..
-rw-r--r--  1 ana ana  220 jan 10 08:00 .bash_logout
-rw-r--r--  1 ana ana 3.7K jan 10 08:00 .bashrc
drwxr-xr-x  2 ana ana 4.0K jan 12 14:20 projetos
-rw-r--r--  1 ana ana  807 jan 10 08:00 .profile
-rw-r--r--  1 ana ana  150 jan 15 10:30 notas.txt
```

Note que com `-h`, os tamanhos aparecem como `4.0K` e `3.7K` em vez de `4096` e `3771`. Muito mais legível.

### tree — Visualizando a Estrutura

O comando `tree` mostra a estrutura de diretórios em formato de árvore visual. Não vem instalado por padrão, mas é fácil de instalar:

```bash
# Instalar o tree
sudo apt install tree

# Ver a arvore do diretorio atual
tree

# Limitar a profundidade (2 niveis)
tree -L 2

# Mostrar apenas diretorios
tree -d

# Mostrar com tamanhos
tree -sh
```

Saída esperada (tree -L 2):
```
.
├── projetos
│   ├── site
│   └── api
├── scripts
│   ├── backup.sh
│   └── setup.sh
└── notas.txt

4 directories, 3 files
```

O `tree` é excelente para entender a organização de um projeto. Quando você baixar um projeto do GitHub e quiser entender a estrutura, `tree -L 2` é geralmente o primeiro comando a executar.

---

## Criando: Arquivos e Diretórios

### mkdir — Criando Diretórios

O comando `mkdir` (make directory, ou "criar diretório") cria novos diretórios.

```bash
# Criar um diretorio
mkdir projetos

# Criar varios diretorios de uma vez
mkdir docs testes config

# Criar diretorio com subdiretorios (opcao -p = parents)
mkdir -p projetos/site/css/componentes

# Sem -p, o comando falha se o diretorio pai nao existir:
mkdir projetos/api/rotas  # ERRO se "api" nao existir
mkdir -p projetos/api/rotas  # OK, cria tudo que falta
```

Saída esperada (mkdir sem -p quando pai não existe):
```
mkdir: cannot create directory 'projetos/api/rotas': No such file or directory
```

A opção `-p` (parents) é uma das mais úteis — ela cria toda a cadeia de diretórios necessária. Sem ela, você teria que criar cada nível separadamente: primeiro `projetos`, depois `projetos/api`, depois `projetos/api/rotas`.

### touch — Criando Arquivos Vazios

O comando `touch` cria arquivos vazios ou atualiza a data de modificação de arquivos existentes.

```bash
# Criar um arquivo vazio
touch readme.md

# Criar varios arquivos de uma vez
touch index.html style.css script.js

# Se o arquivo ja existe, touch atualiza a data de modificacao
touch arquivo-existente.txt
```

O nome `touch` (tocar) vem da ideia de "tocar" o arquivo para atualizar seu timestamp — como se você estivesse dizendo ao sistema "eu mexi neste arquivo agora". Essa funcionalidade original é útil em sistemas de build que recompilam arquivos baseados na data de modificação.

Na prática, a maioria dos desenvolvedores usa `touch` para criar arquivos vazios rapidamente. Mas existem outras formas de criar arquivos com conteúdo:

```bash
# Criar arquivo com conteudo usando echo
echo "# Meu Projeto" > readme.md

# Criar arquivo com multiplas linhas usando cat e heredoc
cat > config.txt << EOF
servidor=localhost
porta=8080
debug=true
EOF

# Verificar o conteudo
cat config.txt
```

Saída esperada:
```
servidor=localhost
porta=8080
debug=true
```

O `<< EOF` é chamado de **heredoc** (here document). Ele permite escrever múltiplas linhas de texto que terminam quando a palavra `EOF` aparece sozinha em uma linha. Você pode usar qualquer palavra no lugar de `EOF` — é apenas um marcador de fim.

### Criando Estruturas de Projeto

Na prática, quando você inicia um novo projeto, precisa criar vários diretórios e arquivos de uma vez. Veja como fazer isso de forma eficiente:

```bash
# Criar estrutura de um projeto web
mkdir -p meu-site/{css,js,img,pages}
touch meu-site/index.html
touch meu-site/css/style.css
touch meu-site/js/app.js
touch meu-site/readme.md

# Verificar a estrutura criada
tree meu-site
```

Saída esperada:
```
meu-site
├── css
│   └── style.css
├── img
├── index.html
├── js
│   └── app.js
├── pages
└── readme.md

4 directories, 4 files
```

O `{css,js,img,pages}` é uma funcionalidade do bash chamada **brace expansion** (expansão de chaves). O bash expande `meu-site/{css,js,img,pages}` em quatro argumentos separados: `meu-site/css meu-site/js meu-site/img meu-site/pages`. É um atalho poderoso para criar múltiplos diretórios ou arquivos com padrões similares.

```bash
# Mais exemplos de brace expansion
touch arquivo{1,2,3}.txt        # Cria arquivo1.txt, arquivo2.txt, arquivo3.txt
touch log-{jan,fev,mar}.txt     # Cria log-jan.txt, log-fev.txt, log-mar.txt
mkdir -p src/{models,views,controllers}  # Estrutura MVC
```

---

## Copiando, Movendo e Renomeando

### cp — Copiando Arquivos e Diretórios

O comando `cp` (copy, ou "copiar") cria uma cópia de um arquivo ou diretório.

```bash
# Copiar um arquivo
cp original.txt copia.txt

# Copiar um arquivo para outro diretorio
cp readme.md /home/ana/backup/

# Copiar um arquivo para outro diretorio com novo nome
cp readme.md /home/ana/backup/readme-backup.md

# Copiar varios arquivos para um diretorio
cp arquivo1.txt arquivo2.txt arquivo3.txt /home/ana/backup/

# Copiar um diretorio inteiro (opcao -r = recursivo)
cp -r projetos/ projetos-backup/

# Copiar preservando permissoes e datas (opcao -p = preserve)
cp -p importante.txt backup/

# Copiar com confirmacao antes de sobrescrever (opcao -i = interactive)
cp -i original.txt destino.txt

# Combinacao mais segura: recursivo + preservar + interativo
cp -rpi projetos/ backup/
```

Saída esperada (cp -i quando arquivo já existe):
```
cp: overwrite 'destino.txt'? y
```

Pontos importantes sobre o `cp`:

| Situação | Comportamento | Como evitar problemas |
|----------|--------------|----------------------|
| Destino ja existe | Sobrescreve sem avisar | Usar `-i` para confirmar |
| Copiar diretório sem `-r` | Erro | Sempre usar `-r` para diretórios |
| Copiar para diretório que não existe | Erro | Criar o diretório antes com `mkdir -p` |
| Copiar arquivo grande | Pode demorar | Usar `-v` para ver progresso |

### mv — Movendo e Renomeando

O comando `mv` (move, ou "mover") faz duas coisas: move arquivos entre diretórios e renomeia arquivos. No Linux, renomear é a mesma operação que mover — você está "movendo" o arquivo para o mesmo diretório com um nome diferente.

```bash
# Renomear um arquivo
mv nome-antigo.txt nome-novo.txt

# Mover um arquivo para outro diretorio
mv relatorio.txt /home/ana/documentos/

# Mover e renomear ao mesmo tempo
mv rascunho.txt /home/ana/documentos/relatorio-final.txt

# Mover varios arquivos para um diretorio
mv *.txt /home/ana/documentos/

# Mover um diretorio inteiro (nao precisa de -r como o cp)
mv projetos-antigos/ /home/ana/arquivo/

# Mover com confirmacao antes de sobrescrever
mv -i arquivo.txt destino/
```

A diferença fundamental entre `cp` e `mv`:
- `cp` cria uma **cópia** — o original continua existindo
- `mv` **move** — o original desaparece do local de origem

Pense assim: `cp` é como fotocopiar um documento (agora existem dois), e `mv` é como pegar o documento e colocar em outra gaveta (só existe um, mas em outro lugar).

### Renomeando em Massa

Renomear um arquivo é simples com `mv`. Mas e se você precisar renomear 100 arquivos? Aí entra o poder do terminal combinado com o que aprendemos no módulo 2.8 sobre loops:

```bash
# Renomear todos os .jpeg para .jpg
for f in *.jpeg; do
    mv "$f" "${f%.jpeg}.jpg"
done

# Adicionar prefixo a todos os arquivos
for f in *.txt; do
    mv "$f" "backup-$f"
done

# Substituir espacos por hifens nos nomes
for f in *\ *; do
    mv "$f" "${f// /-}"
done
```

O `${f%.jpeg}` é uma funcionalidade do bash chamada **parameter expansion** (expansão de parâmetro). O `%` remove o sufixo especificado do valor da variável. Então se `f` é `foto.jpeg`, `${f%.jpeg}` resulta em `foto`, e `${f%.jpeg}.jpg` resulta em `foto.jpg`.

---

## Removendo: Arquivos e Diretórios

### rm — Removendo Arquivos

O comando `rm` (remove, ou "remover") apaga arquivos. **Atenção: no Linux, não existe lixeira no terminal.** Quando você remove um arquivo com `rm`, ele desaparece permanentemente. Não tem Ctrl+Z, não tem "desfazer", não tem lixeira para recuperar.

```bash
# Remover um arquivo
rm arquivo.txt

# Remover com confirmacao (RECOMENDADO para iniciantes)
rm -i arquivo.txt

# Remover varios arquivos
rm arquivo1.txt arquivo2.txt arquivo3.txt

# Remover todos os arquivos .tmp do diretorio atual
rm *.tmp

# Remover um diretorio vazio
rmdir diretorio-vazio/

# Remover um diretorio e todo seu conteudo (CUIDADO!)
rm -r diretorio/

# Forcar remocao sem perguntar (MUITO CUIDADO!)
rm -rf diretorio/
```

Saída esperada (rm -i):
```
rm: remove regular file 'arquivo.txt'? y
```

### O Perigo do rm -rf

O comando `rm -rf` é o mais perigoso do Linux. O `-r` significa recursivo (apaga tudo dentro) e o `-f` significa force (não pergunta nada). Juntos, eles apagam tudo silenciosamente.

Comandos que você **NUNCA** deve executar:

```bash
# NUNCA EXECUTE ESTES COMANDOS!

# Apaga TUDO do sistema - destroi o Linux inteiro
# rm -rf /

# Apaga tudo do diretorio home - perde todos os seus arquivos
# rm -rf ~

# Apaga tudo do diretorio atual - pode ser desastroso
# rm -rf *
```

Boas práticas para evitar desastres:

1. **Sempre use `rm -i`** até ter confiança — ele pergunta antes de cada arquivo
2. **Sempre verifique com `ls` antes de `rm`** — veja o que vai ser apagado
3. **Nunca use `rm -rf` com variáveis** sem verificar — se `$DIR` estiver vazio, `rm -rf $DIR/` vira `rm -rf /`
4. **Use `trash-cli`** se quiser uma lixeira no terminal — `sudo apt install trash-cli`, depois use `trash` em vez de `rm`

```bash
# Pratica segura: verificar antes de apagar
ls *.tmp          # Primeiro, veja o que vai ser apagado
rm -i *.tmp       # Depois, apague com confirmacao

# Pratica mais segura: usar trash em vez de rm
sudo apt install trash-cli
trash arquivo.txt          # Move para a lixeira
trash-list                 # Ver o que esta na lixeira
trash-restore              # Restaurar um arquivo
trash-empty                # Esvaziar a lixeira
```

---

## Visualizando Conteúdo de Arquivos

Existem vários comandos para ver o conteúdo de arquivos sem abrir um editor. Cada um é ideal para uma situação diferente.

### cat — Ver o Arquivo Inteiro

O comando `cat` (concatenate, ou "concatenar") mostra o conteúdo completo de um arquivo. O nome vem da função original: concatenar (juntar) vários arquivos em um só. Mas no dia a dia, é usado principalmente para ver o conteúdo de arquivos pequenos.

```bash
# Ver o conteudo de um arquivo
cat readme.md

# Ver com numeros de linha
cat -n readme.md

# Ver com numeros de linha apenas nas linhas nao vazias
cat -b readme.md

# Concatenar dois arquivos e salvar em um terceiro
cat parte1.txt parte2.txt > completo.txt
```

Saída esperada (cat -n readme.md):
```
     1  # Meu Projeto
     2
     3  Este e um projeto de exemplo.
     4
     5  ## Como usar
     6
     7  Execute o comando abaixo:
     8  python3 app.py
```

O `cat` é ótimo para arquivos pequenos (até umas 50 linhas). Para arquivos grandes, ele despeja tudo na tela de uma vez, o que não é prático. Para esses casos, use `less` ou `head`/`tail`.

### less — Navegar pelo Arquivo

O comando `less` abre o arquivo em um visualizador que permite navegar para cima e para baixo, buscar texto e ir para linhas específicas. É ideal para arquivos grandes.

```bash
# Abrir um arquivo no less
less /var/log/syslog

# Navegacao dentro do less:
# Setas ou j/k     = mover linha a linha
# Espaco ou PgDown = proxima pagina
# b ou PgUp        = pagina anterior
# g                = ir para o inicio
# G                = ir para o final
# /texto           = buscar "texto" para frente
# ?texto           = buscar "texto" para tras
# n                = proxima ocorrencia da busca
# N                = ocorrencia anterior
# q                = sair

# Abrir mostrando numeros de linha
less -N /var/log/syslog
```

O nome `less` é um trocadilho com o comando mais antigo `more` (que só permitia avançar, não voltar). A piada é: "less is more" (menos é mais) — o `less` faz mais que o `more`, apesar do nome sugerir o contrário. Humor de programador dos anos 1980.

### head e tail — Ver o Início ou o Final

O `head` mostra as primeiras linhas de um arquivo, e o `tail` mostra as últimas. São perfeitos para dar uma espiada rápida sem abrir o arquivo inteiro.

```bash
# Ver as primeiras 10 linhas (padrao)
head readme.md

# Ver as primeiras 5 linhas
head -n 5 readme.md

# Ver as ultimas 10 linhas (padrao)
tail readme.md

# Ver as ultimas 20 linhas
tail -n 20 readme.md

# Ver as ultimas linhas em tempo real (acompanhar logs!)
tail -f /var/log/syslog
```

O `tail -f` (follow) é um dos comandos mais úteis para desenvolvedores. Ele fica "seguindo" o arquivo — quando novas linhas são adicionadas, elas aparecem automaticamente na tela. É perfeito para acompanhar logs de aplicações em tempo real:

```bash
# Acompanhar o log de um servidor web
tail -f /var/log/nginx/access.log

# Acompanhar os ultimos 50 linhas e continuar seguindo
tail -n 50 -f /var/log/syslog

# Para parar de seguir: Ctrl+C
```

### wc — Contando Linhas, Palavras e Caracteres

O comando `wc` (word count, ou "contar palavras") conta linhas, palavras e caracteres de um arquivo.

```bash
# Contagem completa: linhas, palavras, caracteres
wc readme.md

# Contar apenas linhas
wc -l readme.md

# Contar apenas palavras
wc -w readme.md

# Contar apenas caracteres
wc -c readme.md

# Contar linhas de varios arquivos
wc -l *.md
```

Saída esperada (wc readme.md):
```
  42  156  1024 readme.md
```

Isso significa: 42 linhas, 156 palavras, 1024 caracteres (bytes).

Saída esperada (wc -l *.md):
```
   42 readme.md
  150 notas.md
   85 plano.md
  277 total
```

O `wc -l` é extremamente útil combinado com outros comandos via pipe. Por exemplo, para contar quantos arquivos existem em um diretório:

```bash
# Contar quantos arquivos .py existem no projeto
find . -name "*.py" | wc -l
```

### diff — Comparando Arquivos

O comando `diff` (difference, ou "diferença") compara dois arquivos e mostra as diferenças entre eles. É o ancestral das ferramentas de comparação que você vai usar no Git (Capítulo 4).

```bash
# Comparar dois arquivos
diff arquivo1.txt arquivo2.txt

# Comparar lado a lado
diff -y arquivo1.txt arquivo2.txt

# Comparar ignorando espacos em branco
diff -w arquivo1.txt arquivo2.txt

# Formato unificado (mais legivel, usado pelo git)
diff -u arquivo1.txt arquivo2.txt
```

Saída esperada (diff -u):
```
--- arquivo1.txt    2025-01-15 10:00:00
+++ arquivo2.txt    2025-01-15 11:00:00
@@ -1,4 +1,4 @@
 Linha 1: igual
-Linha 2: texto antigo
+Linha 2: texto novo
 Linha 3: igual
 Linha 4: igual
```

As linhas com `-` existem apenas no primeiro arquivo, e as linhas com `+` existem apenas no segundo. Esse formato é exatamente o que o `git diff` usa — quando chegarmos ao Capítulo 4, você já vai saber ler essas diferenças.

---

## Buscando Arquivos e Conteúdo

Projetos reais têm centenas ou milhares de arquivos. Encontrar o que você precisa sem ferramentas de busca seria impossível. O Linux tem dois comandos poderosos para isso: `find` (busca por nome/propriedades) e `grep` (busca por conteúdo).

### find — Encontrando Arquivos

O comando `find` procura arquivos e diretórios baseado em critérios como nome, tipo, tamanho, data e permissões.

```bash
# Encontrar arquivo por nome no diretorio atual e subdiretorios
find . -name "readme.md"

# Encontrar ignorando maiusculas/minusculas
find . -iname "README.md"

# Encontrar todos os arquivos .py
find . -name "*.py"

# Encontrar todos os arquivos .py e .js
find . -name "*.py" -o -name "*.js"

# Encontrar apenas diretorios
find . -type d

# Encontrar apenas arquivos (nao diretorios)
find . -type f

# Encontrar arquivos maiores que 10MB
find . -size +10M

# Encontrar arquivos menores que 1KB
find . -size -1k

# Encontrar arquivos modificados nos ultimos 7 dias
find . -mtime -7

# Encontrar arquivos modificados ha mais de 30 dias
find . -mtime +30

# Encontrar e executar um comando em cada resultado
find . -name "*.tmp" -exec rm {} \;

# Encontrar arquivos vazios
find . -empty
```

Saída esperada (find . -name "*.md"):
```
./readme.md
./docs/guia.md
./docs/api.md
./notas/reuniao.md
```

O `find` é extremamente versátil. A sintaxe do `-exec` pode parecer estranha: o `{}` é substituído pelo nome de cada arquivo encontrado, e o `\;` marca o fim do comando. Então `find . -name "*.tmp" -exec rm {} \;` encontra todos os arquivos `.tmp` e executa `rm` em cada um.

| Critério | Opcao | Exemplo |
|----------|-------|---------|
| Nome exato | `-name` | `find . -name "app.py"` |
| Nome sem case | `-iname` | `find . -iname "README*"` |
| Tipo arquivo | `-type f` | `find . -type f` |
| Tipo diretório | `-type d` | `find . -type d` |
| Tamanho maior | `-size +N` | `find . -size +100M` |
| Tamanho menor | `-size -N` | `find . -size -1k` |
| Modificado ha menos de N dias | `-mtime -N` | `find . -mtime -7` |
| Modificado ha mais de N dias | `-mtime +N` | `find . -mtime +30` |
| Permissão | `-perm` | `find . -perm 755` |
| Dono | `-user` | `find . -user ana` |
| Vazio | `-empty` | `find . -empty` |

### grep — Buscando Conteúdo Dentro de Arquivos

Se o `find` procura arquivos pelo nome, o `grep` procura **texto dentro dos arquivos**. O nome vem de uma operação do editor `ed`: "g/re/p" (global/regular expression/print — busca global por expressão regular e imprime).

```bash
# Buscar a palavra "erro" em um arquivo
grep "erro" log.txt

# Buscar ignorando maiusculas/minusculas
grep -i "erro" log.txt

# Buscar em todos os arquivos do diretorio atual
grep "erro" *

# Buscar recursivamente em todos os subdiretorios
grep -r "erro" .

# Buscar recursivamente apenas em arquivos .py
grep -r "erro" --include="*.py" .

# Mostrar o numero da linha onde encontrou
grep -n "erro" log.txt

# Contar quantas vezes aparece
grep -c "erro" log.txt

# Mostrar linhas que NAO contem o texto
grep -v "debug" log.txt

# Mostrar 2 linhas antes e depois do resultado (contexto)
grep -B 2 -A 2 "erro" log.txt

# Buscar palavra exata (nao parte de outra palavra)
grep -w "erro" log.txt
```

Saída esperada (grep -rn "erro" --include="*.py" .):
```
./app/main.py:42:    print("Erro ao conectar ao banco")
./app/utils.py:15:    raise ValueError("Erro de validacao")
./tests/test_app.py:28:    assert "erro" in response.text
```

Cada resultado mostra: `arquivo:linha:conteúdo`. Isso é extremamente útil para encontrar onde algo está definido ou usado em um projeto grande.

| Opcao | O que faz | Quando usar |
|-------|-----------|-------------|
| `-i` | Ignora maiusculas e minusculas | Quando não sabe se e "Erro" ou "erro" |
| `-r` | Busca recursiva em subdiretorios | Quando quer buscar no projeto inteiro |
| `-n` | Mostra número da linha | Quando precisa saber onde esta |
| `-c` | Conta ocorrências | Quando quer saber quantas vezes aparece |
| `-l` | Mostra apenas nomes dos arquivos | Quando quer saber quais arquivos tem o texto |
| `-v` | Inverte a busca, mostra o que NAO tem | Quando quer filtrar linhas indesejadas |
| `-w` | Busca palavra exata | Quando "erro" não deve casar com "erroneo" |
| `-B N` | Mostra N linhas antes | Quando precisa de contexto |
| `-A N` | Mostra N linhas depois | Quando precisa de contexto |
| `--include` | Filtra por tipo de arquivo | Quando quer buscar so em .py, .js, etc. |

### Combinando find e grep

O verdadeiro poder aparece quando você combina os dois:

```bash
# Encontrar todos os arquivos .py que contem "import requests"
grep -rl "import requests" --include="*.py" .

# Encontrar arquivos grandes modificados recentemente
find . -size +1M -mtime -7 -type f

# Encontrar e listar detalhes de todos os scripts shell
find . -name "*.sh" -exec ls -lh {} \;

# Contar linhas de codigo em todos os arquivos Python do projeto
find . -name "*.py" -exec wc -l {} + | tail -1
```

Saída esperada (último comando):
```
  2847 total
```

---

## Informações sobre Arquivos

Além de listar e buscar, existem comandos para obter informações detalhadas sobre arquivos.

### file — Identificando o Tipo de Arquivo

O comando `file` identifica o tipo de um arquivo pelo seu conteúdo, não pela extensão. Isso é importante porque no Linux, extensões são apenas convenções — um arquivo chamado `foto.txt` pode na verdade ser uma imagem.

```bash
# Identificar o tipo de um arquivo
file readme.md
file foto.jpg
file programa
file backup.tar.gz
```

Saída esperada:
```
readme.md:      UTF-8 Unicode text
foto.jpg:       JPEG image data, JFIF standard 1.01
programa:       ELF 64-bit LSB executable, x86-64
backup.tar.gz:  gzip compressed data
```

### stat — Informações Detalhadas

O comando `stat` mostra informações detalhadas sobre um arquivo: tamanho, permissões, datas de acesso, modificação e criação, inode e muito mais.

```bash
# Informacoes completas de um arquivo
stat readme.md
```

Saída esperada:
```
  File: readme.md
  Size: 1024        Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d  Inode: 262145      Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/     ana)   Gid: ( 1000/     ana)
Access: 2025-01-15 10:30:00.000000000 -0300
Modify: 2025-01-15 10:25:00.000000000 -0300
Change: 2025-01-15 10:25:00.000000000 -0300
 Birth: 2025-01-10 08:00:00.000000000 -0300
```

Note as três datas diferentes:
- **Access**: última vez que o arquivo foi lido
- **Modify**: última vez que o conteúdo foi alterado
- **Change**: última vez que os metadados (permissões, dono) foram alterados

### du — Espaço em Disco

O comando `du` (disk usage, ou "uso de disco") mostra quanto espaço arquivos e diretórios ocupam.

```bash
# Tamanho de um diretorio e seus subdiretorios
du -sh projetos/

# Tamanho de cada subdiretorio
du -sh projetos/*/

# Tamanho de cada arquivo e diretorio, ordenado por tamanho
du -sh * | sort -rh

# Top 10 maiores diretorios a partir do atual
du -sh */ | sort -rh | head -10
```

Saída esperada (du -sh */):
```
4.2M    projetos/
1.8M    documentos/
256K    scripts/
128K    config/
```

A opção `-s` (summary) mostra apenas o total de cada argumento, e `-h` (human-readable) mostra em KB, MB, GB.

### df — Espaço Livre no Disco

O comando `df` (disk free, ou "disco livre") mostra o espaço total, usado e disponível em cada partição do sistema.

```bash
# Espaco em disco de todas as particoes
df -h

# Espaco em disco apenas da particao onde estamos
df -h .
```

Saída esperada (df -h):
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   22G   26G  46% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
/dev/sda2       200G   85G  105G  45% /home
```

---

## Compactação e Descompactação

Quando você precisa enviar muitos arquivos pela rede, fazer backup ou economizar espaço em disco, a compactação é essencial. O Linux tem várias ferramentas para isso.

### tar — Empacotando Arquivos

O comando `tar` (tape archive, ou "arquivo de fita") originalmente foi criado para gravar dados em fitas magnéticas — o meio de backup dos anos 1970-80. Hoje, é usado para empacotar vários arquivos em um único arquivo.

O `tar` sozinho apenas empacota (junta vários arquivos em um). Para comprimir (reduzir o tamanho), ele usa compressores como gzip, bzip2 ou xz.

```bash
# Criar um arquivo tar (apenas empacotar, sem comprimir)
tar -cf backup.tar projetos/
# -c = create (criar)
# -f = file (nome do arquivo de saida)

# Criar um arquivo tar.gz (empacotar + comprimir com gzip)
tar -czf backup.tar.gz projetos/
# -z = gzip

# Criar um arquivo tar.bz2 (compressao melhor, mais lento)
tar -cjf backup.tar.bz2 projetos/
# -j = bzip2

# Criar um arquivo tar.xz (melhor compressao, mais lento ainda)
tar -cJf backup.tar.xz projetos/
# -J = xz

# Listar o conteudo de um arquivo tar sem extrair
tar -tf backup.tar.gz

# Extrair um arquivo tar.gz
tar -xzf backup.tar.gz
# -x = extract (extrair)

# Extrair em um diretorio especifico
tar -xzf backup.tar.gz -C /home/ana/restaurado/

# Criar com verbose (mostra cada arquivo sendo adicionado)
tar -czvf backup.tar.gz projetos/
# -v = verbose
```

Saída esperada (tar -czvf):
```
projetos/
projetos/readme.md
projetos/app.py
projetos/config.json
projetos/tests/
projetos/tests/test_app.py
```

As opções do `tar` são famosas por serem confusas. Aqui vai um resumo prático:

| Ação | Comando | Lembrete |
|------|---------|----------|
| Criar .tar.gz | `tar -czf arquivo.tar.gz pasta/` | c = create, z = gzip, f = file |
| Extrair .tar.gz | `tar -xzf arquivo.tar.gz` | x = extract |
| Criar .tar.bz2 | `tar -cjf arquivo.tar.bz2 pasta/` | j = bzip2 |
| Extrair .tar.bz2 | `tar -xjf arquivo.tar.bz2` | |
| Criar .tar.xz | `tar -cJf arquivo.tar.xz pasta/` | J maiusculo = xz |
| Extrair .tar.xz | `tar -xJf arquivo.tar.xz` | |
| Listar conteúdo | `tar -tf arquivo.tar.gz` | t = list |

### zip e unzip — Formato Universal

O formato ZIP é o mais universal — funciona no Linux, Windows e macOS sem instalar nada extra.

```bash
# Comprimir arquivos em zip
zip backup.zip arquivo1.txt arquivo2.txt

# Comprimir um diretorio inteiro
zip -r backup.zip projetos/

# Descomprimir
unzip backup.zip

# Descomprimir em um diretorio especifico
unzip backup.zip -d /home/ana/restaurado/

# Listar conteudo sem extrair
unzip -l backup.zip
```

### Quando Usar Cada Formato

| Formato | Compressao | Velocidade | Quando usar |
|---------|-----------|------------|-------------|
| .tar.gz | Boa | Rápido | Uso geral no Linux, backups |
| .tar.bz2 | Melhor | Medio | Quando tamanho importa mais que velocidade |
| .tar.xz | Excelente | Lento | Distribuição de software, arquivos grandes |
| .zip | Boa | Rápido | Quando precisa compartilhar com Windows e macOS |

---

## Links: Atalhos no Sistema de Arquivos

O Linux permite criar **links** — referências que apontam para outros arquivos ou diretórios. Existem dois tipos: links simbólicos (soft links) e links rígidos (hard links).

### Links Simbólicos (Soft Links)

Um **link simbólico** é como um atalho do Windows — é um arquivo especial que aponta para outro arquivo. Se o arquivo original for movido ou apagado, o link quebra.

```bash
# Criar um link simbolico
ln -s /home/ana/projetos/app/config.json ~/config-link.json
# -s = symbolic (simbolico)

# Verificar que e um link
ls -l ~/config-link.json
```

Saída esperada:
```
lrwxrwxrwx 1 ana ana 38 jan 15 10:30 config-link.json -> /home/ana/projetos/app/config.json
```

O `l` no início das permissões indica que é um link simbólico, e a seta `->` mostra para onde ele aponta.

Links simbólicos são muito usados no Linux:
- `/usr/bin/python3` geralmente é um link para `/usr/bin/python3.10` (ou a versão instalada)
- Configurações de sites no Nginx usam links de `sites-available/` para `sites-enabled/`
- Desenvolvedores criam links para acessar diretórios profundos com caminhos curtos

```bash
# Exemplo pratico: criar atalho para um projeto profundo
ln -s /home/ana/trabalho/empresa/projetos/2025/api-principal ~/api

# Agora em vez de:
cd /home/ana/trabalho/empresa/projetos/2025/api-principal

# Voce pode simplesmente:
cd ~/api
```

### Links Rígidos (Hard Links)

Um **link rígido** é diferente: ele cria outra entrada no sistema de arquivos que aponta para os mesmos dados no disco. Se o arquivo original for apagado, o link rígido continua funcionando porque os dados ainda existem.

```bash
# Criar um link rigido
ln arquivo-original.txt link-rigido.txt

# Verificar que ambos apontam para o mesmo inode
ls -li arquivo-original.txt link-rigido.txt
```

Saída esperada:
```
262145 -rw-r--r-- 2 ana ana 1024 jan 15 10:30 arquivo-original.txt
262145 -rw-r--r-- 2 ana ana 1024 jan 15 10:30 link-rigido.txt
```

Note que o número do **inode** (262145) é o mesmo para ambos — eles são o mesmo arquivo no disco, apenas com nomes diferentes. O número `2` na terceira coluna indica que existem 2 links para esse inode.

Na prática, links simbólicos são muito mais usados que links rígidos. Links rígidos têm limitações: não funcionam entre partições diferentes e não podem apontar para diretórios.

---

## Curingas (Wildcards): Padrões de Busca

**Curingas** (wildcards, ou "caracteres coringa") são caracteres especiais que o shell expande para corresponder a padrões de nomes de arquivos. Já usamos alguns nos exemplos anteriores (`*.txt`, `*.py`), mas vamos formalizar.

| Curinga | Significado | Exemplo | Corresponde a |
|---------|-------------|---------|---------------|
| `*` | Qualquer sequência de caracteres | `*.txt` | readme.txt, notas.txt, a.txt |
| `?` | Exatamente um caractere | `arquivo?.txt` | arquivo1.txt, arquivoA.txt |
| `[abc]` | Um dos caracteres listados | `arquivo[123].txt` | arquivo1.txt, arquivo2.txt, arquivo3.txt |
| `[a-z]` | Um caractere no intervalo | `[a-z]*.py` | app.py, main.py, utils.py |
| `[!abc]` | Qualquer caractere EXCETO os listados | `*[!0-9].txt` | readme.txt, mas não arquivo1.txt |

```bash
# Listar todos os arquivos markdown
ls *.md

# Listar arquivos que comecam com "cap" e terminam com ".md"
ls cap*.md

# Listar arquivos com exatamente um caractere antes de .txt
ls ?.txt

# Listar arquivos que comecam com a, b ou c
ls [abc]*

# Listar arquivos que comecam com letra maiuscula
ls [A-Z]*

# Copiar todos os arquivos de imagem para uma pasta
cp *.{jpg,png,gif} imagens/

# Mover todos os logs de janeiro
mv log-jan-*.txt arquivo/
```

Os curingas são expandidos pelo **shell** (bash), não pelo comando. Quando você digita `ls *.md`, o bash primeiro expande `*.md` para a lista de todos os arquivos `.md` e depois passa essa lista para o `ls`. O `ls` nunca vê o `*` — ele recebe `readme.md notas.md plano.md`.

Isso é importante porque significa que curingas funcionam com **qualquer** comando, não apenas com `ls`:

```bash
# Todos estes usam curingas da mesma forma:
cat *.txt          # Mostrar conteudo de todos os .txt
wc -l *.py         # Contar linhas de todos os .py
grep "erro" *.log  # Buscar "erro" em todos os .log
rm *.tmp           # Remover todos os .tmp
cp *.md backup/    # Copiar todos os .md para backup
```

---

## Tabela de Referência Rápida

Esta tabela reúne todos os comandos do módulo para consulta rápida:

| Comando | O que faz | Exemplo mais comum |
|---------|-----------|-------------------|
| `pwd` | Mostra o diretório atual | `pwd` |
| `cd` | Muda de diretório | `cd ~/projetos` |
| `ls` | Lista arquivos e diretórios | `ls -lah` |
| `tree` | Mostra estrutura em árvore | `tree -L 2` |
| `mkdir` | Cria diretórios | `mkdir -p pasta/sub` |
| `touch` | Cria arquivo vazio | `touch readme.md` |
| `cp` | Copia arquivos e diretórios | `cp -r origem/ destino/` |
| `mv` | Move ou renomeia | `mv antigo.txt novo.txt` |
| `rm` | Remove arquivos | `rm -i arquivo.txt` |
| `rmdir` | Remove diretório vazio | `rmdir pasta-vazia/` |
| `cat` | Mostra conteúdo do arquivo | `cat -n arquivo.txt` |
| `less` | Navega pelo arquivo | `less arquivo-grande.log` |
| `head` | Mostra primeiras linhas | `head -n 20 arquivo.txt` |
| `tail` | Mostra ultimas linhas | `tail -f log.txt` |
| `wc` | Conta linhas, palavras, caracteres | `wc -l *.py` |
| `diff` | Compara dois arquivos | `diff -u v1.txt v2.txt` |
| `find` | Busca arquivos por critérios | `find . -name "*.py"` |
| `grep` | Busca texto dentro de arquivos | `grep -rn "erro" .` |
| `file` | Identifica tipo do arquivo | `file documento.pdf` |
| `stat` | Informações detalhadas | `stat arquivo.txt` |
| `du` | Espaco usado por arquivos | `du -sh */` |
| `df` | Espaco livre no disco | `df -h` |
| `tar` | Empacota e comprime | `tar -czf backup.tar.gz pasta/` |
| `zip` | Comprime em formato zip | `zip -r backup.zip pasta/` |
| `ln` | Cria links | `ln -s alvo link` |
| `man` | Manual do comando | `man grep` |

---

## Conexão com a Programação

Todos os comandos deste módulo são ferramentas que você vai usar diariamente como desenvolvedor. Mas além do uso prático, eles ensinam conceitos fundamentais:

**Operações CRUD**: os comandos de arquivo implementam as quatro operações básicas de dados que vamos estudar em profundidade no Capítulo 7:
- **C**reate (criar): `touch`, `mkdir`, `cp`
- **R**ead (ler): `cat`, `less`, `head`, `tail`, `ls`, `find`, `grep`
- **U**pdate (atualizar): `mv` (renomear), editores de texto
- **D**elete (apagar): `rm`, `rmdir`

Essas mesmas quatro operações existem em bancos de dados (INSERT, SELECT, UPDATE, DELETE), em APIs REST (POST, GET, PUT, DELETE) e em praticamente todo sistema de software. O terminal é onde você prática CRUD pela primeira vez.

**Busca e filtragem**: o `find` e o `grep` são versões simples dos mesmos conceitos que existem em bancos de dados (WHERE, LIKE), em linguagens de programação (filter, search) e em APIs (query parameters). Aprender a buscar eficientemente no terminal prepara você para buscar eficientemente em qualquer contexto.

**Compressão e empacotamento**: o conceito de empacotar vários itens em um (tar) e comprimir para reduzir tamanho (gzip) aparece em muitos contextos: arquivos ZIP que você baixa da internet, imagens Docker que empacotam aplicações, bundles de JavaScript que comprimem código para a web.

---

## Como a IA pode te ajudar aqui
**Prompt 1 — Explorar o conceito:**
> "Preciso encontrar todos os arquivos Python maiores que 100KB que foram modificados na última semana no meu projeto. Monte o comando find para mim e explique cada parte."

**Prompt 2 — Comparar alternativas:**
> "Qual a diferença entre cp -r e cp -a? Quando devo usar cada um? Me dê exemplos práticos."

**Prompt 3 — Entender erros comuns:**
> "Estou recebendo o erro 'Permission denied' quando tento copiar um arquivo para /etc/. O que está acontecendo e como resolvo?"

---

## Resumo do Módulo

| Conceito | Definição |
|----------|-----------|
| Caminho absoluto | Caminho completo desde a raiz do sistema, comeca com / |
| Caminho relativo | Caminho a partir do diretório atual, sem / no inicio |
| Curinga wildcard | Caractere especial que o shell expande para corresponder a padrões de nomes |
| Brace expansion | Recurso do bash que expande chaves em multiplos argumentos |
| Parameter expansion | Recurso do bash para manipular valores de variáveis |
| Heredoc | Forma de escrever multiplas linhas de texto em um comando |
| Inode | Estrutura interna do sistema de arquivos que armazena metadados |
| Link simbolico | Arquivo especial que aponta para outro arquivo ou diretório |
| Link rigido | Entrada adicional no sistema de arquivos que aponta para o mesmo inode |
| Compressao | Processo de reduzir o tamanho de arquivos |
| Empacotamento | Processo de juntar vários arquivos em um único arquivo |
| CRUD | Create, Read, Update, Delete - as quatro operações básicas de dados |
| Pipe | Operador que conecta a saida de um comando a entrada de outro |
| Expressao regular | Padrão de texto usado para buscas avancadas |

---

## Glossário do Módulo

| Termo | Definição |
|-------|-----------|
| Absolute path | Caminho absoluto, caminho completo desde a raiz do sistema |
| Brace expansion | Expansao de chaves, recurso do bash que gera multiplos argumentos |
| bzip2 | Algoritmo de compressao com melhor taxa que gzip, mais lento |
| cat | Concatenate, comando que mostra conteúdo de arquivos |
| cd | Change directory, comando para mudar de diretório |
| cp | Copy, comando para copiar arquivos e diretórios |
| CRUD | Create Read Update Delete, as quatro operações básicas de dados |
| Curinga | Caractere especial como * e ? que corresponde a padrões de nomes |
| df | Disk free, comando que mostra espaco livre no disco |
| diff | Difference, comando que compara dois arquivos |
| du | Disk usage, comando que mostra espaco usado por arquivos |
| file | Comando que identifica o tipo de um arquivo pelo conteúdo |
| find | Comando que busca arquivos por nome, tipo, tamanho e outros critérios |
| grep | Global Regular Expression Print, comando que busca texto dentro de arquivos |
| gzip | Algoritmo de compressao rápido e eficiente, padrão no Linux |
| Hard link | Link rigido, entrada no sistema de arquivos que aponta para o mesmo inode |
| head | Comando que mostra as primeiras linhas de um arquivo |
| Heredoc | Here document, forma de escrever texto de multiplas linhas em scripts |
| Inode | Estrutura de dados do sistema de arquivos que armazena metadados de um arquivo |
| less | Comando para navegar pelo conteúdo de arquivos grandes |
| ln | Link, comando para criar links simbolicos e rigidos |
| ls | List, comando para listar arquivos e diretórios |
| man | Manual, comando que exibe a documentação de outros comandos |
| mkdir | Make directory, comando para criar diretórios |
| mv | Move, comando para mover ou renomear arquivos |
| Parameter expansion | Expansao de parametro, recurso do bash para manipular variáveis |
| pwd | Print working directory, comando que mostra o diretório atual |
| Recursive | Recursivo, opcao que faz o comando agir em subdiretorios |
| Relative path | Caminho relativo, caminho a partir do diretório atual |
| rm | Remove, comando para apagar arquivos |
| rmdir | Remove directory, comando para apagar diretórios vazios |
| Soft link | Link simbolico, arquivo que aponta para outro arquivo |
| stat | Comando que mostra informações detalhadas sobre um arquivo |
| Symlink | Abreviacao de symbolic link, link simbolico |
| tail | Comando que mostra as ultimas linhas de um arquivo |
| tar | Tape archive, comando para empacotar e comprimir arquivos |
| touch | Comando para criar arquivos vazios ou atualizar timestamps |
| tree | Comando que mostra estrutura de diretórios em formato de árvore |
| Verbose | Modo detalhado que mostra cada operação sendo executada |
| wc | Word count, comando que conta linhas, palavras e caracteres |
| Wildcard | Curinga, caractere especial para padrões de nomes de arquivos |
| xz | Algoritmo de compressao com excelente taxa, mais lento que gzip |
| zip | Formato de compressao universal, compatível com Windows e macOS |

---

## Na Cultura Popular

- **Mr. Robot** (série, 2015-2019) — em praticamente todo episódio, o protagonista usa comandos como `find`, `grep`, `cat`, `ls` e `rm` para navegar em sistemas, buscar informações e manipular arquivos. A série é notável por mostrar comandos reais — se você prestar atenção, vai reconhecer muitos dos comandos deste módulo.

- **Jurassic Park** (filme, 1993) — na famosa cena em que a personagem Lex diz "It's a Unix system! I know this!", ela está usando um navegador de arquivos 3D chamado FSN (File System Navigator), que realmente existia no Unix da Silicon Graphics. A cena mostra a navegação por diretórios — o mesmo conceito de `cd` e `ls`, mas com uma interface visual tridimensional.

- **The Social Network** (filme, 2010) — nas cenas iniciais, Mark Zuckerberg usa o terminal para criar o Facemash, navegando entre diretórios, editando arquivos e executando scripts. Os comandos mostrados são reais e incluem vários dos que estudamos neste módulo.

---

## Para Saber Mais

- *Linux Command Line Basics — Ubuntu Documentation* — https://help.ubuntu.com/community/UsingTheTerminal — *guia oficial do Ubuntu para uso do terminal*
- *The Linux Command Line — William Shotts* — https://linuxcommand.org/tlcl.php — *livro gratuito e completo sobre linha de comando no Linux, excelente referência*
- *ExplainShell* — https://explainshell.com — *cole qualquer comando e veja a explicação de cada parte, ótimo para entender comandos complexos*
- *Repositório do Fino — learn-ops-content* — https://github.com/RafaelFino/learn-ops-content — *material complementar sobre Linux e comandos*
- *cheat.sh* — https://cheat.sh — *folha de referência rápida para comandos, acessível direto do terminal com `curl cheat.sh/comando`*

---

## Perguntas Frequentes (FAQ)

**P: Preciso decorar todos esses comandos?**
R: Não. Ninguém decora tudo — nem desenvolvedores com 20 anos de experiência. O que acontece é que os comandos mais usados (`ls`, `cd`, `cp`, `mv`, `rm`, `grep`, `find`) viram automáticos com a prática. Para os outros, use `man`, `--help` ou pergunte à IA. O importante é saber que o comando existe e o que ele faz — a sintaxe exata você consulta quando precisa.

**P: Qual a diferença entre rm e rmdir?**
R: O `rmdir` só remove diretórios vazios — se tiver qualquer arquivo dentro, ele recusa. O `rm -r` remove o diretório e tudo dentro dele. O `rmdir` é mais seguro porque nunca apaga conteúdo acidentalmente.

**P: Por que ls -la mostra arquivos que começam com ponto?**
R: No Linux, arquivos que começam com `.` (ponto) são considerados ocultos. O `ls` normal não os mostra. A opção `-a` (all) mostra todos, incluindo os ocultos. Arquivos de configuração como `.bashrc`, `.gitignore` e `.profile` são ocultos por convenção — eles existem mas não poluem a listagem normal.

**P: O que acontece se eu copiar um arquivo para um destino que já existe?**
R: O `cp` sobrescreve o arquivo de destino sem avisar. Isso pode causar perda de dados. Use `cp -i` (interactive) para que ele pergunte antes de sobrescrever, ou `cp -n` (no-clobber) para nunca sobrescrever.

**P: Posso recuperar um arquivo apagado com rm?**
R: Na maioria dos casos, não. O `rm` remove a referência ao arquivo no sistema de arquivos. Os dados podem ainda estar no disco por um tempo, mas recuperá-los requer ferramentas especializadas e não é garantido. A melhor proteção é fazer backups regulares e usar `trash-cli` em vez de `rm`.

**P: Qual a diferença entre find e grep?**
R: O `find` busca **arquivos** pelo nome, tipo, tamanho, data e outras propriedades. O `grep` busca **texto dentro** dos arquivos. Use `find` quando sabe o nome do arquivo mas não sabe onde está. Use `grep` quando sabe o que o arquivo contém mas não sabe qual é.

**P: Por que tar e gzip são comandos separados?**
R: Porque seguem a filosofia Unix: cada programa faz uma coisa bem. O `tar` empacota (junta vários arquivos em um), e o `gzip` comprime (reduz o tamanho). Juntos, eles empacotam e comprimem. Hoje, o `tar` aceita as opções `-z`, `-j` e `-J` para chamar o compressor automaticamente, mas internamente são programas separados trabalhando juntos.

**P: O que é um inode?**
R: Um inode é uma estrutura de dados no sistema de arquivos que armazena informações sobre um arquivo: permissões, dono, tamanho, datas e a localização dos dados no disco. O nome do arquivo não está no inode — ele está na entrada do diretório que aponta para o inode. É por isso que links rígidos funcionam: dois nomes diferentes podem apontar para o mesmo inode.

**P: Quando devo usar caminho absoluto e quando usar relativo?**
R: Use caminho absoluto em scripts (para garantir que funcione independente de onde o script é executado) e quando precisa ser preciso. Use caminho relativo no dia a dia interativo (é mais curto e rápido de digitar) e quando o contexto é claro. Em projetos de código, caminhos relativos são preferidos porque o projeto pode estar em qualquer lugar do disco.

**P: O grep funciona com acentos e caracteres especiais?**
R: Sim, desde que o sistema esteja configurado com UTF-8 (o que é padrão em distribuições modernas). Você pode buscar `grep "ação" arquivo.txt` normalmente. Para caracteres que têm significado especial no grep (como `.`, `*`, `[`), use `\` antes deles ou a opção `-F` (fixed string) para tratar o texto literalmente.

**P: Como sei se devo usar sudo antes de um comando?**
R: Se o comando envolve arquivos fora do seu diretório home (como `/etc`, `/var`, `/usr`), provavelmente precisa de `sudo`. Se envolve instalar ou remover pacotes, precisa de `sudo`. Se envolve gerenciar serviços, precisa de `sudo`. Para arquivos dentro do seu home, geralmente não precisa. Na dúvida, tente sem `sudo` primeiro — se der "Permission denied", aí use `sudo`.

**P: O que significa o ponto e dois pontos nos caminhos?**
R: O `.` (ponto) representa o diretório atual. O `..` (dois pontos) representa o diretório pai (um nível acima). Então `cd ..` sobe um nível, `cd ../..` sobe dois níveis, e `./script.sh` executa um script no diretório atual. Esses são atalhos universais que funcionam em qualquer sistema Unix/Linux.

---

## Exercícios Práticos

**Exercício 1 — Navegação e Exploração**

1. Descubra em qual diretório você está com `pwd`
2. Navegue até a raiz do sistema (`cd /`) e liste o conteúdo com `ls -la`
3. Navegue até `/var/log` e descubra quantos arquivos existem lá (`ls | wc -l`)
4. Volte para seu home com `cd ~`
5. Crie a seguinte estrutura de diretórios usando um único comando `mkdir -p`:
   ```
   ~/exercício/
   ├── src/
   │   ├── models/
   │   ├── views/
   │   └── controllers/
   ├── tests/
   ├── docs/
   └── config/
   ```
6. Verifique a estrutura com `tree ~/exercício`

**Exercício 2 — Manipulação de Arquivos**

1. Dentro de `~/exercício/src/`, crie três arquivos: `app.py`, `utils.py` e `config.py`
2. Escreva uma linha de conteúdo em cada arquivo usando `echo "conteúdo" > arquivo`
3. Copie todos os arquivos `.py` para `~/exercício/tests/` com um único comando
4. Renomeie `~/exercício/src/config.py` para `~/exercício/src/settings.py`
5. Crie um arquivo `~/exercício/docs/readme.md` com pelo menos 3 linhas usando heredoc
6. Verifique o conteúdo de cada arquivo com `cat`
7. Conte quantas linhas tem cada arquivo com `wc -l`

**Exercício 3 — Busca e Compactação**

1. Use `find` para encontrar todos os arquivos `.py` dentro de `~/exercício/`
2. Use `grep` para encontrar qual arquivo contém uma palavra específica que você escreveu
3. Use `du -sh` para ver o tamanho total do diretório `~/exercício/`
4. Crie um arquivo compactado `exercício-backup.tar.gz` com todo o conteúdo de `~/exercício/`
5. Liste o conteúdo do arquivo compactado sem extrair (`tar -tf`)
6. Extraia o backup em um diretório diferente (`~/exercício-restaurado/`)
7. Use `diff -r` para comparar os dois diretórios e confirmar que são iguais

---

[← Anterior: Terminal vs Interpretador de Comandos](cap03-mod01-terminal-vs-shell.md) · [Próximo: Pipes e Redirecionamento →](cap03-mod03-pipes-redirecionamento.md)
