# 03 — Preparação do Ambiente de Desenvolvimento

[← Anterior: Scripts, Compilados e VM](02-scripts-compilados-vm.md) · [Glossário](00-glossario.md) · [Próximo: Execução, Permissões e Pastas →](04-execucao-permissoes-pastas.md)

---

## Introdução

Antes de começar a programar, precisamos preparar as ferramentas no seu computador. É como organizar a bancada da cozinha antes de cozinhar: você precisa ter os utensílios certos no lugar certo.

Neste módulo, vamos instalar e configurar duas ferramentas essenciais:

1. **Python** — a linguagem de programação que vamos usar
2. **VSCode** — o editor de código onde vamos escrever nossos programas

Todas as instruções são para o sistema operacional **Linux**. Cada passo será explicado em detalhes, com o comando exato que você deve digitar e a saída que deve aparecer na tela.

---

## O que é o Terminal?

O [terminal](00-glossario-q-z.md#terminal) é um programa que permite você "conversar" com o computador digitando comandos de texto. Em vez de clicar em botões e ícones, você escreve o que quer que o computador faça.

Pode parecer estranho no início, mas o terminal é uma ferramenta muito poderosa que programadores usam todos os dias.

### Como abrir o terminal

No Linux, pressione as teclas **`Ctrl + Alt + T`** ao mesmo tempo. Uma janela escura com texto vai aparecer — esse é o terminal.

Você verá algo parecido com isso:

```
usuario@computador:~$
```

Isso é o **prompt** — o terminal está esperando que você digite um comando. O símbolo `$` indica que ele está pronto para receber instruções.

> **Atenção:** Não se preocupe se o texto no seu terminal for um pouco diferente. O importante é que ele esteja aberto e esperando um comando.

---

## Passo 1: Verificar se o Python já está instalado

Muitas distribuições Linux já vêm com o Python instalado. Vamos verificar.

**Digite o seguinte comando no terminal e pressione Enter:**

```bash
python3 --version
```

> **Nota:** `python3` é o comando que chama o interpretador Python. `--version` pede que ele mostre qual versão está instalada.

**Saída esperada (algo parecido com):**

```
Python 3.10.12
```

O número da versão pode ser diferente no seu computador (por exemplo, 3.8, 3.11, 3.12). O importante é que comece com **3** (Python 3).

**Se aparecer um erro como:**

```
comando não encontrado: python3
```

Isso significa que o Python não está instalado. Siga para o próximo passo.

---

## Passo 2: Instalar o Python (se necessário)

Se o Python não estiver instalado, vamos instalá-lo. **Digite os seguintes comandos no terminal, um por vez:**

**Primeiro, atualize a lista de programas disponíveis:**

```bash
sudo apt update
```

> **Nota:** `sudo` significa "super user do" — executa o comando como administrador. O sistema pode pedir sua senha. Digite a senha e pressione Enter (a senha não aparece na tela enquanto você digita — isso é normal!).

> **Nota:** `apt update` atualiza a lista de programas que podem ser instalados.

**Saída esperada:** Várias linhas de texto mostrando o progresso da atualização, terminando com algo como "Lendo listas de pacotes... Pronto".

**Depois, instale o Python:**

```bash
sudo apt install python3 python3-pip -y
```

> **Nota:** `apt install` instala um programa. `python3` é o Python e `python3-pip` é o gerenciador de pacotes do Python. O `-y` confirma automaticamente a instalação.

**Saída esperada:** Várias linhas mostrando o download e instalação, terminando com "Pronto" ou similar.

**Verifique se a instalação funcionou:**

```bash
python3 --version
```

Agora deve aparecer a versão do Python instalada.

---

## Passo 3: Instalar o VSCode

O [VSCode](00-glossario-q-z.md#vscode-visual-studio-code) (Visual Studio Code) é o editor de código que vamos usar para escrever nossos programas. Ele é gratuito, popular e tem muitas funcionalidades que facilitam a programação.

### Opção A: Instalar pelo terminal (recomendado)

**Digite os seguintes comandos no terminal, um por vez:**

```bash
sudo apt install software-properties-common apt-transport-https wget -y
```

```bash
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
```

```bash
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
```

```bash
sudo apt update
```

```bash
sudo apt install code -y
```

> **Atenção:** Esses comandos adicionam o repositório oficial do VSCode e instalam o programa. Não se preocupe em entender cada comando agora — o importante é que o VSCode seja instalado.

**Verifique se a instalação funcionou:**

```bash
code --version
```

**Saída esperada:** Um número de versão, como `1.85.0` ou similar.

### Opção B: Instalar pelo site

Se os comandos acima não funcionarem, você pode baixar o VSCode diretamente do site oficial:

1. Abra o navegador de internet
2. Acesse: `https://code.visualstudio.com/`
3. Clique no botão de download para Linux (.deb)
4. Após o download, abra o terminal e digite:

```bash
sudo dpkg -i ~/Downloads/code_*.deb
```

> **Nota:** Esse comando instala o arquivo que você baixou. O `~/Downloads/` é a pasta onde o navegador salva os downloads.

---

## Passo 4: Abrir o VSCode

Agora que o VSCode está instalado, vamos abri-lo.

**No terminal, digite:**

```bash
code
```

O VSCode vai abrir em uma nova janela. Você verá uma tela de boas-vindas com várias opções.

> **Dica:** Você também pode abrir o VSCode pelo menu de aplicativos do Linux, procurando por "Visual Studio Code" ou "Code".

---

## Passo 5: Instalar a extensão Python no VSCode

Para que o VSCode funcione bem com Python, precisamos instalar uma extensão (um complemento que adiciona funcionalidades).

1. Com o VSCode aberto, clique no ícone de **quadradinhos** na barra lateral esquerda (ou pressione `Ctrl + Shift + X`). Isso abre o painel de extensões.

2. Na barra de busca que aparece, digite: `Python`

3. Procure a extensão chamada **"Python"** da **Microsoft** (geralmente é a primeira da lista)

4. Clique no botão **"Install"** (Instalar)

5. Aguarde a instalação terminar

Pronto! Agora o VSCode está configurado para trabalhar com Python.

### Extensões recomendadas para iniciantes

Além da extensão Python, estas extensões podem ajudar:

| Extensão | O que faz |
|----------|-----------|
| **Python** (Microsoft) | Suporte completo a Python (obrigatória) |
| **Portuguese (Brazil) Language Pack** | Traduz o VSCode para português |
| **indent-rainbow** | Colore a indentação para facilitar a visualização |

---

## Passo 6: Criar seu primeiro arquivo Python no VSCode

Vamos criar um arquivo Python para testar se tudo está funcionando.

1. No VSCode, clique em **File** (Arquivo) → **New File** (Novo Arquivo), ou pressione `Ctrl + N`

2. Uma aba em branco vai aparecer. Digite o seguinte código:

```python
# Meu primeiro programa em Python!
# print() exibe uma mensagem no terminal
print("Olá, mundo! Meu ambiente está funcionando!")
```

3. Salve o arquivo: pressione `Ctrl + S`

4. Na janela que aparece, escolha uma pasta para salvar (sugestão: crie uma pasta chamada `meus-projetos` na sua pasta pessoal)

5. Dê o nome `ola.py` ao arquivo (a extensão `.py` indica que é um arquivo Python)

6. Clique em **Save** (Salvar)

> **Nota:** No próximo módulo, vamos aprender a executar esse arquivo no terminal.

---

## Resumo do que Instalamos

| Ferramenta | Para que serve | Como verificar |
|------------|---------------|----------------|
| Python 3 | Executar programas Python | `python3 --version` |
| pip | Instalar bibliotecas Python | `pip3 --version` |
| VSCode | Escrever código | `code --version` |
| Extensão Python | Suporte a Python no VSCode | Verificar no painel de extensões |

---

## Para Saber Mais

-  [W3Schools — Python Getting Started](https://www.w3schools.com/python/python_getstarted.asp) — _Como instalar e começar com Python_
-  [Documentação Oficial Python — Instalação](https://docs.python.org/pt-br/3/using/unix.html) — _Instalação no Linux_
-  [VSCode — Documentação](https://code.visualstudio.com/docs) — _Guia completo do VSCode (em inglês)_

---

## Perguntas Frequentes (FAQ)

**P: Meu terminal mostra `python` em vez de `python3`. Qual usar?**
R: Em algumas distribuições Linux, o comando `python` aponta para o Python 2 (versão antiga). Sempre use `python3` para garantir que está usando a versão correta. Se `python3` não funcionar, tente `python` e verifique a versão com `python --version`.

**P: O sistema pediu minha senha e nada aparece quando digito. Está quebrado?**
R: Não! Isso é um recurso de segurança do Linux. Quando você digita a senha no terminal, os caracteres não aparecem na tela (nem asteriscos). Apenas digite a senha normalmente e pressione Enter.

**P: Posso usar outro editor em vez do VSCode?**
R: Sim! Qualquer editor de texto serve para escrever Python. Mas o VSCode é recomendado porque tem muitas funcionalidades que facilitam o aprendizado, como destaque de cores no código e detecção de erros.

**P: O que é `sudo`?**
R: `sudo` significa "super user do" — permite executar comandos como administrador do sistema. É necessário para instalar programas. O sistema pede sua senha para confirmar que você tem permissão.

**P: E se algum comando der erro?**
R: Leia a mensagem de erro com atenção — ela geralmente indica o problema. Erros comuns: falta de conexão com a internet (para downloads), senha incorreta, ou o programa já estar instalado. Se não conseguir resolver, peça ajuda ao professor.

**P: Preciso de internet para programar?**
R: Você precisa de internet apenas para instalar o Python, o VSCode e as extensões. Depois de instalado, você pode programar sem internet.

**P: O que é uma "extensão" do VSCode?**
R: É um complemento que adiciona funcionalidades ao VSCode. A extensão Python, por exemplo, adiciona destaque de cores para código Python, detecção de erros e autocompletar. É como instalar um aplicativo extra no seu editor.

**P: O que é `apt`?**
R: `apt` é o gerenciador de pacotes do Linux (em distribuições baseadas em Debian/Ubuntu). Ele permite instalar, atualizar e remover programas. É como uma loja de aplicativos do terminal.

**P: O que significa `apt update`?**
R: Atualiza a lista de programas disponíveis para instalação. É como atualizar o catálogo de uma loja — não instala nada, apenas verifica o que está disponível.

**P: O que significa o `-y` no final do comando de instalação?**
R: O `-y` responde "sim" automaticamente quando o sistema pergunta se você quer continuar com a instalação. Sem ele, o sistema pede confirmação manual.

**P: Posso instalar o Python no Windows em vez do Linux?**
R: Este curso foi feito para Linux, mas o Python funciona em Windows também. Os comandos do terminal serão diferentes. Se você usa Windows, consulte o professor para orientações específicas.

**P: O que é uma "distribuição Linux"?**
R: É uma versão do sistema operacional Linux. Ubuntu, Mint, Fedora e Debian são exemplos de distribuições. Cada uma tem pequenas diferenças, mas os comandos básicos são os mesmos.

**P: O VSCode é gratuito?**
R: Sim! O VSCode é completamente gratuito e desenvolvido pela Microsoft. Você pode baixar e usar sem pagar nada.

**P: O que é o "prompt" do terminal?**
R: É o texto que aparece antes do cursor no terminal (geralmente algo como `usuario@computador:~$`). Ele indica que o terminal está pronto para receber um comando.

**P: O que significa o `$` no terminal?**
R: O `$` indica que você está usando o terminal como usuário normal (não como administrador). Quando você usa `sudo`, o sistema executa o comando como administrador temporariamente.

**P: Posso ter mais de uma versão do Python instalada?**
R: Sim! É possível ter Python 3.8, 3.10 e 3.12 no mesmo computador. O comando `python3` geralmente aponta para a versão mais recente. Para este curso, qualquer versão 3.8 ou superior funciona.

**P: O que é `pip`?**
R: É o gerenciador de pacotes do Python — permite instalar bibliotecas extras. Vamos aprender sobre ele em detalhes no módulo 26. Por enquanto, ele foi instalado junto com o Python.

**P: O terminal me assusta. É normal?**
R: Completamente normal! O terminal parece intimidador no início porque não tem botões ou ícones — só texto. Mas com prática, você vai se acostumar e perceber que é uma ferramenta muito poderosa e eficiente.

**P: O que fazer se o VSCode não abrir?**
R: Tente fechar e abrir novamente. Se persistir, verifique se a instalação foi concluída com sucesso executando `code --version` no terminal. Se aparecer um erro, tente reinstalar seguindo os passos deste módulo.

**P: Posso personalizar as cores do VSCode?**
R: Sim! O VSCode tem muitos temas de cores. Vá em File → Preferences → Color Theme para escolher. Isso é puramente estético e não afeta o funcionamento.

---

[← Anterior: Scripts, Compilados e VM](02-scripts-compilados-vm.md) · [Glossário](00-glossario.md) · [Próximo: Execução, Permissões e Pastas →](04-execucao-permissoes-pastas.md)
