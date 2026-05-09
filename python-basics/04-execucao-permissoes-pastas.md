# 04 — Execução de Programas Python, Permissões e Estrutura de Pastas

[← Anterior: Preparação do Ambiente](03-preparacao-ambiente.md) · [Glossário](00-glossario.md) · [Próximo: História do Python →](05-historia-python.md)

---

## Introdução

No módulo anterior, instalamos o Python e o VSCode. Agora vamos aprender a **executar programas Python** no terminal, entender **permissões de arquivo** no Linux e organizar nossos arquivos em **pastas** de forma profissional.

Pense neste módulo como aprender a usar a cozinha: você já tem os utensílios (Python e VSCode), agora precisa saber como ligar o fogão (executar programas), onde guardar cada coisa (estrutura de pastas) e quais gavetas você tem permissão para abrir (permissões de arquivo).

---

## Executando um Programa Python

### Passo 1: Abra o terminal

Pressione **`Ctrl + Alt + T`** para abrir o terminal.

### Passo 2: Navegue até a pasta do seu arquivo

Use o comando `cd` ("change directory" = mudar de diretório/pasta) para ir até onde seu arquivo Python está salvo.

**Se você salvou na pasta `meus-projetos` dentro da sua pasta pessoal:**

```bash
cd ~/meus-projetos
```

> **Nota:** O símbolo `~` (til) representa sua pasta pessoal (home). É um atalho para não precisar digitar o caminho completo.

**Para confirmar que está na pasta certa, use `pwd`** ("print working directory" = mostrar diretório atual):

```bash
pwd
```

**Saída esperada:**

```
/home/seu-usuario/meus-projetos
```

**Para ver os arquivos na pasta, use `ls`** ("list" = listar):

```bash
ls
```

**Saída esperada (se você criou o arquivo no módulo anterior):**

```
ola.py
```

### Passo 3: Execute o programa

**Digite o comando:**

```bash
python3 ola.py
```

> **Nota:** `python3` chama o interpretador Python. `ola.py` é o nome do arquivo que você quer executar. O Python vai ler o arquivo linha por linha e executar cada instrução.

**Saída esperada:**

```
Olá, mundo! Meu ambiente está funcionando!
```

Se você viu essa mensagem, parabéns! Você acabou de executar seu primeiro programa Python! 

### Erros comuns ao executar

**`No such file or directory` (arquivo não encontrado):**
```
python3: can't open file 'ola.py': [Errno 2] No such file or directory
```
Isso significa que o terminal não encontrou o arquivo. Verifique:
- Você está na pasta correta? Use `pwd` para conferir
- O arquivo existe? Use `ls` para ver os arquivos na pasta
- O nome está escrito corretamente? (Atenção a maiúsculas/minúsculas!)

**`command not found` (comando não encontrado):**
```
bash: python3: comando não encontrado
```
O Python pode não estar instalado. Volte ao [Módulo 03](03-preparacao-ambiente.md) e siga as instruções de instalação.

**`SyntaxError` (erro de sintaxe):**
```
  File "ola.py", line 1
    prnt("Olá")
    ^^^^
SyntaxError: invalid syntax
```
Há um erro no código (neste exemplo, `prnt` em vez de `print`). Abra o arquivo no VSCode, corrija o erro e execute novamente.

---

## Permissões de Arquivo no Linux

No Linux, cada arquivo tem **permissões** que controlam quem pode fazer o quê com ele. Existem três tipos de permissão:

| Permissão | Letra | O que permite |
|-----------|-------|--------------|
| Leitura | `r` (read) | Ver o conteúdo do arquivo |
| Escrita | `w` (write) | Modificar o arquivo |
| Execução | `x` (execute) | Executar o arquivo como programa |

### Verificando permissões

**Use o comando `ls -l`** (listar com detalhes):

```bash
ls -l ola.py
```

**Saída esperada (algo parecido com):**

```
-rw-rw-r-- 1 usuario usuario 89 jan 15 10:30 ola.py
```

Os primeiros caracteres (`-rw-rw-r--`) mostram as permissões:
- `-` = é um arquivo (não uma pasta)
- `rw-` = o dono pode ler (r) e escrever (w), mas não executar (-)
- `rw-` = o grupo pode ler e escrever
- `r--` = outros podem apenas ler

### Alterando permissões com chmod

O comando [chmod](00-glossario-a-d.md#chmod) ("change mode" = mudar modo) altera as permissões de um arquivo.

**Para dar permissão de execução:**

```bash
chmod +x ola.py
```

> **Nota:** `+x` significa "adicionar permissão de execução". Depois disso, você pode executar o arquivo diretamente com `./ola.py` (além de `python3 ola.py`).

**Para a maioria dos casos neste curso, você não precisa se preocupar com permissões.** O comando `python3 arquivo.py` funciona sem precisar de permissão de execução no arquivo. Mas é bom saber que permissões existem, caso encontre o erro "permissão negada".

**Se aparecer "Permission denied" (permissão negada):**

```bash
chmod +x nome_do_arquivo.py
```

---

## Estrutura de Pastas de um Projeto

Manter seus arquivos organizados em pastas é fundamental. É como organizar uma casa: cada cômodo tem uma função, e você sabe onde encontrar cada coisa.

### Estrutura recomendada para o curso

```
~/meus-projetos/
├── python-curso/           ← Pasta principal do curso
│   ├── modulo-06/          ← Exercícios do módulo 06
│   │   ├── exercicio_01.py
│   │   └── exercicio_02.py
│   ├── modulo-07/          ← Exercícios do módulo 07
│   │   ├── exercicio_01.py
│   │   └── exercicio_02.py
│   ├── crud-projeto/       ← Projeto CRUD (módulos 29-32)
│   │   ├── main.py
│   │   └── database.py
│   └── testes/             ← Seus testes e experimentos
│       └── teste_rapido.py
```

> **Nota:** O símbolo `├──` e `└──` são apenas para visualização da hierarquia. Não fazem parte dos nomes das pastas.

### Criando pastas no terminal

**Para criar a estrutura acima:**

```bash
mkdir -p ~/meus-projetos/python-curso
```

> **Nota:** `mkdir` significa "make directory" (criar diretório/pasta). O `-p` cria todas as pastas intermediárias que não existem.

```bash
cd ~/meus-projetos/python-curso
```

```bash
mkdir modulo-06 modulo-07 crud-projeto testes
```

**Para verificar que as pastas foram criadas:**

```bash
ls
```

**Saída esperada:**

```
crud-projeto  modulo-06  modulo-07  testes
```

### Navegando entre pastas

| Comando | O que faz | Exemplo |
|---------|-----------|---------|
| `cd pasta` | Entra na pasta | `cd modulo-06` |
| `cd ..` | Volta uma pasta acima | `cd ..` |
| `cd ~` | Vai para a pasta pessoal (home) | `cd ~` |
| `cd ~/meus-projetos` | Vai direto para uma pasta específica | `cd ~/meus-projetos` |
| `pwd` | Mostra a pasta atual | `pwd` |
| `ls` | Lista o conteúdo da pasta atual | `ls` |

### Caminhos absolutos vs relativos

- **Caminho absoluto**: começa com `/` ou `~` e indica o caminho completo desde a raiz do sistema. Exemplo: `/home/usuario/meus-projetos/python-curso/ola.py`
- **Caminho relativo**: indica o caminho a partir da pasta onde você está. Exemplo: se você está em `python-curso`, o caminho relativo para `ola.py` dentro de `modulo-06` é `modulo-06/ola.py`

É como dar um endereço: o caminho absoluto é o endereço completo (Rua X, número Y, bairro Z, cidade W), e o caminho relativo é "a segunda porta à direita" (depende de onde você está).

---

## Resumo dos Comandos Aprendidos

| Comando | O que faz |
|---------|-----------|
| `python3 arquivo.py` | Executa um programa Python |
| `python3 --version` | Mostra a versão do Python |
| `cd pasta` | Muda para outra pasta |
| `cd ..` | Volta uma pasta acima |
| `pwd` | Mostra a pasta atual |
| `ls` | Lista arquivos na pasta |
| `ls -l` | Lista com detalhes (permissões) |
| `mkdir nome` | Cria uma pasta |
| `mkdir -p caminho` | Cria pastas intermediárias |
| `chmod +x arquivo` | Dá permissão de execução |

---

## Para Saber Mais

-  [W3Schools — Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp) — _Primeiros passos com Python_
-  [Documentação Python — Usando Python no Unix](https://docs.python.org/pt-br/3/using/unix.html) — _Referência para Linux_

---

## Perguntas Frequentes (FAQ)

**P: Posso executar Python de dentro do VSCode?**
R: Sim! O VSCode tem um terminal integrado. Pressione `` Ctrl + ` `` (crase) para abrir o terminal dentro do VSCode. Os comandos são os mesmos.

**P: Qual a diferença entre `python` e `python3`?**
R: Em muitos sistemas Linux, `python` pode apontar para o Python 2 (versão antiga). Sempre use `python3` para garantir que está usando a versão correta (Python 3).

**P: Preciso criar uma pasta para cada módulo?**
R: Não é obrigatório, mas é recomendado. Manter os arquivos organizados facilita encontrar seus exercícios e projetos depois.

**P: O que acontece se eu executar um arquivo que não é Python?**
R: O Python vai tentar ler o arquivo e provavelmente vai mostrar um erro de sintaxe. Certifique-se de que o arquivo tem a extensão `.py`.

**P: Posso usar espaços nos nomes de pastas e arquivos?**
R: Tecnicamente sim, mas é uma má prática. Use hífens (`-`) ou underscores (`_`) em vez de espaços. Exemplo: `meu-projeto` ou `meu_projeto` em vez de `meu projeto`.

**P: O que é o `~` (til) no terminal?**
R: É um atalho para a sua pasta pessoal (home). Em vez de digitar `/home/seu-usuario`, você pode usar `~`. Exemplo: `cd ~/meus-projetos` é o mesmo que `cd /home/seu-usuario/meus-projetos`.

**P: O que é a extensão `.py`?**
R: É a extensão de arquivo que indica que o arquivo contém código Python. Assim como `.txt` indica texto e `.jpg` indica imagem, `.py` indica Python.

**P: Posso ter vários arquivos Python na mesma pasta?**
R: Sim! É muito comum ter vários arquivos `.py` na mesma pasta, especialmente em projetos maiores.

**P: O que é `./` antes do nome do arquivo?**
R: `./` significa "na pasta atual". `./ola.py` significa "o arquivo ola.py que está na pasta onde eu estou agora". É uma forma explícita de indicar o caminho relativo.

**P: O que acontece se eu digitar um comando errado no terminal?**
R: O terminal vai mostrar uma mensagem de erro. Não se preocupe — digitar comandos errados não danifica o computador. Basta ler o erro e tentar novamente.

**P: O que é `ls -la`? Por que tem `-la`?**
R: O `-l` mostra detalhes (permissões, tamanho, data) e o `-a` mostra arquivos ocultos (que começam com ponto). Juntos, `-la` mostra tudo com detalhes.

**P: O que são arquivos ocultos no Linux?**
R: São arquivos cujo nome começa com ponto (`.`), como `.gitignore` ou `.bashrc`. Eles não aparecem com `ls` normal, apenas com `ls -a`.

**P: O que é `chmod 755` ou `chmod 644`?**
R: São formas numéricas de definir permissões. 7 = ler+escrever+executar, 6 = ler+escrever, 5 = ler+executar, 4 = apenas ler. Para este curso, `chmod +x` é suficiente.

**P: Posso apagar uma pasta com arquivos dentro?**
R: Sim, com `rm -r nome-da-pasta`. Mas cuidado! Esse comando apaga tudo dentro da pasta sem pedir confirmação. Sempre verifique o que está apagando.

**P: O que é o "caminho" (path) de um arquivo?**
R: É o endereço completo do arquivo no sistema. Exemplo: `/home/usuario/meus-projetos/ola.py`. É como o endereço de uma casa — indica exatamente onde o arquivo está.

**P: Posso renomear um arquivo pelo terminal?**
R: Sim! Use o comando `mv nome-antigo.py nome-novo.py`. O comando `mv` (move) também serve para renomear.

**P: O que é a pasta `/` (raiz)?**
R: É a pasta principal do sistema Linux, de onde todas as outras pastas se originam. É como o tronco de uma árvore — todas as pastas são galhos que saem dele.

**P: O que é a pasta `home`?**
R: É a pasta pessoal de cada usuário no Linux. Seus documentos, downloads e projetos ficam dentro de `/home/seu-usuario/`. O atalho `~` aponta para ela.

**P: Posso criar pastas dentro de pastas?**
R: Sim! Isso é muito comum e recomendado para organizar projetos. Use `mkdir -p pasta1/pasta2/pasta3` para criar toda a hierarquia de uma vez.

**P: O que fazer se aparecer "Permission denied"?**
R: Significa que você não tem permissão para executar aquela ação. Tente adicionar `sudo` antes do comando (para ações de administrador) ou use `chmod` para alterar as permissões do arquivo.

---

[← Anterior: Preparação do Ambiente](03-preparacao-ambiente.md) · [Glossário](00-glossario.md) · [Próximo: História do Python →](05-historia-python.md)
