# 26 — Exercícios: pip e Gerenciamento de Dependências

[<- Voltar para o módulo](26-pip-dependências.md) | [Glossário](00-glossário.md)

---

> **Antes de começar:** Muitos exercícios deste módulo envolvem comandos no terminal. Leia cada enunciado com atenção, execute os comandos passo a passo e compare a saida obtida com a saida esperada. Tente resolver cada exercício sozinho antes de consultar a resposta.

---

### Exercício 1 — Verificando a Versão do pip

#### Enunciado

Abra o terminal e descubra qual versão do pip esta instalada no seu sistema. Anote a versão e o caminho de instalacao.

#### Dicas

- Use o comando que mostra a versão do pip
- O comando usa a opcao `--version`
- Lembre-se de usar `pip3` para garantir que esta usando o Python 3

#### Proposta de Teste

Execute o comando no terminal e verifique:
- **Caso básico:** O terminal deve exibir uma linha com a versão do pip, o caminho de instalacao e a versão do Python associada
- **Caso de borda:** Se aparecer "comando não encontrado", significa que o pip não esta instalado — consulte a secao de instalacao no módulo principal

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Verificamos a versao do pip instalada no sistema
# "--version" = mostrar a versao
pip3 --version
```

Saida esperada:
```
pip 23.0.1 from /usr/lib/python3/dist-packages/pip (python 3.11)
```

> A versão e o caminho podem ser diferentes no seu computador. O importante e que o comando funcione sem erros.

---

### Exercício 2 — Criando um Ambiente Virtual

#### Enunciado

Crie uma pasta chamada `exercicio-venv` dentro da sua pasta de projetos. Dentro dela, crie um ambiente virtual chamado `venv`. Depois, liste o conteúdo da pasta para confirmar que o ambiente foi criado.

#### Dicas

- Use `mkdir` para criar a pasta
- Use `cd` para entrar na pasta
- Use `python3 -m venv venv` para criar o ambiente virtual
- Use `ls` para listar o conteúdo

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos criar o ambiente virtual, o comando `ls` deve mostrar a pasta `venv` dentro de `exercicio-venv`
- **Caso de borda:** Se aparecer um erro ao criar o venv, verifique se o pacote `python3-venv` esta instalado com `sudo apt install python3-venv`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Criamos a pasta do exercicio
# "mkdir" = make directory (criar diretorio/pasta)
mkdir -p ~/meus-projetos/exercicio-venv
```

```bash
# Entramos na pasta criada
# "cd" = change directory (mudar de diretorio)
cd ~/meus-projetos/exercicio-venv
```

```bash
# Criamos o ambiente virtual
# "python3 -m venv" = executar o modulo venv do Python 3
# O ultimo "venv" e o nome da pasta do ambiente virtual
python3 -m venv venv
```

```bash
# Listamos o conteudo da pasta para confirmar
# "ls" = list (listar arquivos e pastas)
ls
```

Saida esperada:
```
venv
```

> A pasta `venv` aparece na listagem, confirmando que o ambiente virtual foi criado com sucesso.

---

### Exercício 3 — Ativando e Desativando o Ambiente Virtual

#### Enunciado

Usando a pasta do exercício anterior, ative o ambiente virtual, verifique que ele esta ativo observando o terminal, e depois desative-o.

#### Dicas

- Use `source venv/bin/activate` para ativar
- Observe se `(venv)` aparece no inicio da linha do terminal
- Use `deactivate` para desativar
- Observe se `(venv)` desaparece apos desativar

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos ativar, o terminal deve mostrar `(venv)` no inicio da linha. Apos desativar, `(venv)` deve desaparecer
- **Caso de borda:** Execute `which python3` com o ambiente ativo — o caminho deve apontar para dentro da pasta `venv`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Navegamos ate a pasta do exercicio (se ainda nao estiver nela)
# "cd" = change directory (mudar de diretorio)
cd ~/meus-projetos/exercicio-venv
```

```bash
# Ativamos o ambiente virtual
# "source" = executar script no terminal atual
# "activate" = ativar
source venv/bin/activate
```

Saida esperada:
```
(venv) usuario@computador:~/meus-projetos/exercicio-venv$
```

```bash
# Verificamos qual Python esta sendo usado
# "which" = qual (mostra o caminho do programa)
which python3
```

Saida esperada:
```
/home/usuario/meus-projetos/exercicio-venv/venv/bin/python3
```

```bash
# Desativamos o ambiente virtual
# "deactivate" = desativar
deactivate
```

Saida esperada:
```
usuario@computador:~/meus-projetos/exercicio-venv$
```

> O `(venv)` desapareceu, confirmando que o ambiente virtual foi desativado.

---

### Exercício 4 — Instalando um Pacote no Ambiente Virtual

#### Enunciado

Com o ambiente virtual ativo (da pasta `exercicio-venv`), instale o pacote `rich` (uma biblioteca para formatar saidas coloridas no terminal). Depois, liste os pacotes instalados para confirmar a instalacao.

#### Dicas

- Certifique-se de que o ambiente virtual esta ativo (você ve `(venv)` no terminal)
- Use `pip3 install rich` para instalar
- Use `pip3 list` para listar os pacotes instalados

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos instalar, o comando `pip3 list` deve mostrar o pacote `rich` na lista
- **Caso de borda:** Desative o ambiente virtual e execute `pip3 list` novamente — o pacote `rich` não deve aparecer na lista do sistema (a menos que ja estivesse instalado antes)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Navegamos ate a pasta do exercicio
# "cd" = change directory (mudar de diretorio)
cd ~/meus-projetos/exercicio-venv
```

```bash
# Ativamos o ambiente virtual
# "source" = executar script no terminal atual
source venv/bin/activate
```

```bash
# Instalamos o pacote rich no ambiente virtual
# "install" = instalar
# "rich" = rico (biblioteca para saidas formatadas no terminal)
pip3 install rich
```

Saida esperada:
```
Collecting rich
  Downloading rich-13.7.0-py3-none-any.whl (240 kB)
Collecting markdown-it-py>=2.2.0
  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Collecting pygments<3.0.0,>=2.13.0
  Downloading pygments-2.17.2-py3-none-any.whl (1.2 MB)
Collecting mdurl~=0.1
  Downloading mdurl-0.1.2-py3-none-any.whl (10 kB)
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-3.0.0 mdurl-0.1.2 pygments-2.17.2 rich-13.7.0
```

```bash
# Listamos os pacotes instalados no ambiente virtual
# "list" = listar
pip3 list
```

Saida esperada:
```
Package        Version
-------------- -------
markdown-it-py 3.0.0
mdurl          0.1.2
pip            23.0.1
pygments       2.17.2
rich           13.7.0
setuptools     66.1.1
```

> O pacote `rich` e suas dependências (`markdown-it-py`, `mdurl`, `pygments`) foram instalados com sucesso no ambiente virtual.

---

### Exercício 5 — Gerando o requirements.txt

#### Enunciado

Com o ambiente virtual ativo e o pacote `rich` instalado (exercício anterior), gere o arquivo `requirements.txt`. Depois, exiba o conteúdo do arquivo no terminal para verificar.

#### Dicas

- Use `pip3 freeze` para ver a lista de pacotes no formato correto
- Use o operador `>` para redirecionar a saida para um arquivo
- Use `cat` para exibir o conteúdo do arquivo

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** O arquivo `requirements.txt` deve conter o pacote `rich` e suas dependências, cada um com a versão exata no formato `pacote==versao`
- **Caso de borda:** Execute `pip3 freeze` sem redirecionar para arquivo — a saida no terminal deve ser identica ao conteúdo do `requirements.txt`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Geramos o arquivo requirements.txt com pip freeze
# "freeze" = congelar (registrar o estado atual das dependencias)
# O operador ">" redireciona a saida para o arquivo
pip3 freeze > requirements.txt
```

```bash
# Exibimos o conteudo do arquivo para verificar
# "cat" = concatenate (exibir conteudo de arquivo)
cat requirements.txt
```

Saida esperada:
```
markdown-it-py==3.0.0
mdurl==0.1.2
pygments==2.17.2
rich==13.7.0
```

> O arquivo lista todos os pacotes com suas versoes exatas. Qualquer pessoa pode usar este arquivo para instalar as mesmas dependências.

---

### Exercício 6 — Recriando o Ambiente a Partir do requirements.txt

#### Enunciado

Simule a situacao de configurar o projeto em um novo computador. Apague a pasta `venv`, crie um novo ambiente virtual e instale as dependências a partir do `requirements.txt`.

#### Dicas

- Primeiro desative o ambiente virtual se estiver ativo
- Use `rm -rf venv` para apagar a pasta do ambiente virtual
- Crie um novo ambiente virtual com `python3 -m venv venv`
- Ative o novo ambiente e instale com `pip3 install -r requirements.txt`

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos instalar com `-r requirements.txt`, o comando `pip3 list` deve mostrar os mesmos pacotes que estavam no ambiente anterior
- **Caso de borda:** Verifique que o pacote `rich` esta na lista com a mesma versão que estava no `requirements.txt`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Desativamos o ambiente virtual (se estiver ativo)
# "deactivate" = desativar
deactivate
```

```bash
# Apagamos a pasta do ambiente virtual
# "rm" = remove (remover), "-rf" = recursive force (recursivo e forcado)
# CUIDADO: este comando apaga a pasta e todo seu conteudo sem pedir confirmacao
rm -rf venv
```

```bash
# Verificamos que a pasta foi apagada
# "ls" = list (listar)
ls
```

Saida esperada:
```
requirements.txt
```

```bash
# Criamos um novo ambiente virtual
# "python3 -m venv venv" = criar ambiente virtual na pasta venv
python3 -m venv venv
```

```bash
# Ativamos o novo ambiente virtual
# "source" = executar script no terminal atual
source venv/bin/activate
```

```bash
# Instalamos todas as dependencias a partir do requirements.txt
# "-r" = read (ler o arquivo)
pip3 install -r requirements.txt
```

Saida esperada:
```
Collecting markdown-it-py==3.0.0
  Using cached markdown_it_py-3.0.0-py3-none-any.whl
Collecting mdurl==0.1.2
  Using cached mdurl-0.1.2-py3-none-any.whl
Collecting pygments==2.17.2
  Using cached pygments-2.17.2-py3-none-any.whl
Collecting rich==13.7.0
  Using cached rich-13.7.0-py3-none-any.whl
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-3.0.0 mdurl-0.1.2 pygments-2.17.2 rich-13.7.0
```

```bash
# Verificamos que os pacotes foram instalados corretamente
# "list" = listar
pip3 list
```

Saida esperada:
```
Package        Version
-------------- -------
markdown-it-py 3.0.0
mdurl          0.1.2
pip            23.0.1
pygments       2.17.2
rich           13.7.0
setuptools     66.1.1
```

> O ambiente foi recriado com sucesso. Todos os pacotes estão nas mesmas versoes do ambiente original.

---

### Exercício 7 — Consultando Informações de um Pacote

#### Enunciado

Com o ambiente virtual ativo e o pacote `rich` instalado, use o pip para exibir informações detalhadas sobre o pacote `rich`. Identifique: o nome do autor, a versão instalada e quais sao as dependências do pacote.

#### Dicas

- Use o comando `pip3 show` seguido do nome do pacote
- Procure os campos "Author", "Version" e "Requires" na saida

#### Proposta de Teste

Execute o comando no terminal e verifique:
- **Caso básico:** A saida deve mostrar o nome do pacote, versão, autor e dependências
- **Caso de borda:** Tente `pip3 show pacote-inexistente` — o pip deve informar que o pacote não foi encontrado

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Exibimos informacoes detalhadas sobre o pacote rich
# "show" = mostrar
pip3 show rich
```

Saida esperada:
```
Name: rich
Version: 13.7.0
Summary: Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal.
Home-page: https://github.com/Textualize/rich
Author: Will McGugan
License: MIT
Location: /home/usuario/meus-projetos/exercicio-venv/venv/lib/python3.11/site-packages
Requires: markdown-it-py, pygments
```

```bash
# Testamos com um pacote que nao existe
# O pip deve informar que nao encontrou o pacote
pip3 show pacote-inexistente
```

Saida esperada:
```
WARNING: Package(s) not found: pacote-inexistente
```

> O campo "Requires" mostra as dependências do pacote: `markdown-it-py` e `pygments`. O campo "Author" mostra o autor: Will McGugan. O campo "Version" mostra a versão: 13.7.0.

---

### Exercício 8 — Desinstalando um Pacote

#### Enunciado

Com o ambiente virtual ativo, desinstale o pacote `rich`. Depois, verifique que ele foi removido listando os pacotes instalados.

#### Dicas

- Use `pip3 uninstall rich` para remover o pacote
- O pip vai pedir confirmacao — digite `y` para confirmar
- Use `pip3 list` para verificar que o pacote foi removido
- Observe que as dependências do `rich` (como `pygments`) continuam instaladas

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos desinstalar, o comando `pip3 list` não deve mais mostrar o pacote `rich`
- **Caso de borda:** As dependências do `rich` (`pygments`, `markdown-it-py`) ainda devem aparecer na lista — o pip não remove dependências automaticamente

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Desinstalamos o pacote rich
# "uninstall" = desinstalar/remover
pip3 uninstall rich
```

Saida esperada:
```
Found existing installation: rich 13.7.0
Uninstalling rich-13.7.0:
  Would remove:
    /home/usuario/.../venv/lib/python3.11/site-packages/rich/*
Proceed (Y/n)? y
  Successfully uninstalled rich-13.7.0
```

> O pip pede confirmacao antes de remover. Digitamos `y` (yes/sim) e pressionamos Enter.

```bash
# Verificamos que o pacote foi removido
# "list" = listar
pip3 list
```

Saida esperada:
```
Package        Version
-------------- -------
markdown-it-py 3.0.0
mdurl          0.1.2
pip            23.0.1
pygments       2.17.2
setuptools     66.1.1
```

> O pacote `rich` não aparece mais na lista. Porém, suas dependências (`markdown-it-py`, `mdurl`, `pygments`) continuam instaladas. O pip não remove dependências automaticamente porque outros pacotes podem precisar delas.

---

### Exercício 9 — Instalando uma Versão Específica

#### Enunciado

Com o ambiente virtual ativo, instale a versão `13.5.0` do pacote `rich` (não a mais recente). Depois, verifique que a versão correta foi instalada.

#### Dicas

- Use o operador `==` para especificar a versão exata
- Use `pip3 show rich` para verificar a versão instalada

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** O comando `pip3 show rich` deve mostrar `Version: 13.5.0`
- **Caso de borda:** Tente instalar uma versão que não existe (como `pip3 install rich==999.0.0`) — o pip deve informar que a versão não foi encontrada

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Instalamos uma versao especifica do pacote rich
# O operador "==" indica a versao exata desejada
pip3 install rich==13.5.0
```

Saida esperada:
```
Collecting rich==13.5.0
  Downloading rich-13.5.0-py3-none-any.whl (239 kB)
Successfully installed rich-13.5.0
```

```bash
# Verificamos a versao instalada
# "show" = mostrar informacoes do pacote
pip3 show rich
```

Saida esperada:
```
Name: rich
Version: 13.5.0
Summary: Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal.
...
```

```bash
# Testamos com uma versao inexistente
pip3 install rich==999.0.0
```

Saida esperada:
```
ERROR: Could not find a version that satisfies the requirement rich==999.0.0
ERROR: No matching distribution found for rich==999.0.0
```

> O pip informa que não encontrou a versão 999.0.0. Isso e útil para saber que você digitou a versão correta.

---

### Exercício 10 — Usando um Pacote Instalado em um Programa

#### Enunciado

Com o ambiente virtual ativo e o pacote `rich` instalado, crie um programa Python chamado `formatted_output.py` que use a biblioteca `rich` para exibir uma mensagem formatada no terminal. O programa deve exibir um texto em negrito e um texto em italico.

#### Dicas

- Importe a função `print` do módulo `rich` (ela substitui o print padrão)
- Use `[bold]texto[/bold]` para negrito e `[italic]texto[/italic]` para italico
- A função `print` do `rich` interpreta essas marcacoes automaticamente

#### Proposta de Teste

Execute o programa e verifique:
- **Caso básico:** O terminal deve exibir o texto com formatacao (negrito e italico podem aparecer como cores ou estilos diferentes dependendo do terminal)
- **Caso de borda:** Se você executar o programa sem o ambiente virtual ativo (e sem `rich` instalado no sistema), deve aparecer um erro `ModuleNotFoundError`

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

Crie o arquivo `formatted_output.py`:

```python
# Programa que usa a biblioteca rich para formatar saidas no terminal
# "formatted_output" = saida formatada

# Importamos a funcao print do modulo rich
# Essa funcao substitui o print padrao e aceita marcacoes de formatacao
# "rich" = rico (biblioteca para saidas ricas/formatadas)
from rich import print

# Exibimos uma mensagem com texto em negrito
# "bold" = negrito
# As marcacoes [bold] e [/bold] indicam inicio e fim do negrito
print("[bold]Esta mensagem esta em negrito![/bold]")

# Exibimos uma mensagem com texto em italico
# "italic" = italico
# As marcacoes [italic] e [/italic] indicam inicio e fim do italico
print("[italic]Esta mensagem esta em italico![/italic]")

# Exibimos uma mensagem combinando negrito e cor
# "green" = verde
print("[bold green]Sucesso! Tudo funcionou corretamente.[/bold green]")

# Exibimos uma mensagem com texto normal e formatado juntos
print("Texto normal e [bold red]texto em vermelho negrito[/bold red] na mesma linha.")
```

Para executar:

```bash
python3 formatted_output.py
```

> O comando `python3 formatted_output.py` executa o programa.

Saida esperada:
```
Esta mensagem esta em negrito!
Esta mensagem esta em italico!
Sucesso! Tudo funcionou corretamente.
Texto normal e texto em vermelho negrito na mesma linha.
```

> No terminal, as mensagens aparecerao com formatacao visual (negrito, italico, cores). A saida acima mostra apenas o texto — no seu terminal, você vera as cores e estilos aplicados.

---

### Exercício 11 — Projeto Completo com Dependências

#### Enunciado

Crie um projeto completo do zero seguindo todas as boas práticas aprendidas neste módulo. O projeto deve:

1. Ter sua propria pasta
2. Ter um ambiente virtual
3. Instalar o pacote `requests`
4. Ter um arquivo `requirements.txt`
5. Ter um programa que faz uma requisicao HTTP e exibe o resultado

O programa deve acessar a URL `https://httpbin.org/ip` e exibir o endereco IP retornado.

#### Dicas

- Siga o fluxo completo: criar pasta, criar venv, ativar, instalar pacote, gerar requirements.txt, criar programa
- A URL `https://httpbin.org/ip` retorna um JSON simples com o campo `origin`
- Use `response.json()` para converter a resposta em dicionário Python

#### Proposta de Teste

Execute o programa e verifique:
- **Caso básico:** O programa deve exibir uma mensagem com o seu endereco IP, algo como `Seu IP e: 203.0.113.42`
- **Caso de borda:** Desconecte a internet e execute novamente — o programa deve gerar um erro de conexão (isso e esperado, pois precisa de internet para acessar a API)

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

Passo 1 — Criar a estrutura:

```bash
# Criamos a pasta do projeto
# "mkdir -p" = criar diretorio (e intermediarios se necessario)
mkdir -p ~/meus-projetos/meu-ip
```

```bash
# Entramos na pasta do projeto
# "cd" = change directory (mudar de diretorio)
cd ~/meus-projetos/meu-ip
```

```bash
# Criamos o ambiente virtual
# "python3 -m venv venv" = criar ambiente virtual na pasta venv
python3 -m venv venv
```

```bash
# Ativamos o ambiente virtual
# "source" = executar script no terminal atual
source venv/bin/activate
```

Passo 2 — Instalar dependências:

```bash
# Instalamos o pacote requests
# "install" = instalar
pip3 install requests
```

Passo 3 — Gerar requirements.txt:

```bash
# Geramos o arquivo de dependencias
# "freeze" = congelar (registrar estado atual)
# ">" = redirecionar saida para arquivo
pip3 freeze > requirements.txt
```

Passo 4 — Criar o programa `my_ip.py`:

```python
# Programa que consulta e exibe o endereco IP do usuario
# "my_ip" = meu IP (endereco de internet)

# Importamos o pacote requests para fazer requisicoes HTTP
# "requests" = requisicoes
import requests

# Definimos a URL da API que retorna o IP
# "url" = endereco na internet
# "api" = interface de programacao de aplicacoes
url = "https://httpbin.org/ip"

# Fazemos a requisicao GET (buscar dados) para a API
# "response" = resposta do servidor
# "get" = obter/buscar
response = requests.get(url)

# Verificamos se a requisicao foi bem-sucedida
# "status_code" = codigo de status (200 = sucesso)
if response.status_code == 200:
    # Convertemos a resposta JSON para dicionario Python
    # "data" = dados
    data = response.json()
    # Exibimos o endereco IP retornado pela API
    # "origin" = origem (endereco IP)
    print(f"Seu IP e: {data['origin']}")
else:
    # Se houve erro, exibimos o codigo de status
    print(f"Erro ao consultar IP. Codigo: {response.status_code}")
```

Passo 5 — Executar:

```bash
# Executamos o programa
# "python3" = interpretador Python 3
python3 my_ip.py
```

Saida esperada:
```
Seu IP e: 203.0.113.42
```

> O endereco IP exibido sera o do seu computador/conexão. Cada pessoa vera um IP diferente.

Passo 6 — Verificar a estrutura final:

```bash
# Listamos os arquivos do projeto
# "ls" = list (listar)
ls
```

Saida esperada:
```
my_ip.py  requirements.txt  venv
```

> O projeto esta completo: programa (`my_ip.py`), dependências (`requirements.txt`) e ambiente virtual (`venv`).

---

### Exercício 12 — Criando um requirements.txt Manual

#### Enunciado

Crie um novo projeto com ambiente virtual. Em vez de usar `pip freeze`, crie o arquivo `requirements.txt` manualmente, listando apenas o pacote `requests` com uma versão específica. Depois, instale as dependências a partir desse arquivo e verifique que tudo funciona.

#### Dicas

- Crie o arquivo `requirements.txt` com um editor de texto ou com o comando `echo`
- Liste apenas o pacote principal (não as dependências dele)
- Use o formato `pacote==versao`
- Instale com `pip3 install -r requirements.txt`

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos instalar com `-r requirements.txt`, o comando `pip3 list` deve mostrar o `requests` e suas dependências automaticas
- **Caso de borda:** Crie o `requirements.txt` com um pacote que não existe (como `pacote-falso==1.0`) e tente instalar — o pip deve informar o erro

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Criamos a pasta do projeto
# "mkdir -p" = criar diretorio (e intermediarios)
mkdir -p ~/meus-projetos/req-manual
```

```bash
# Entramos na pasta
# "cd" = change directory (mudar de diretorio)
cd ~/meus-projetos/req-manual
```

```bash
# Criamos o ambiente virtual
# "python3 -m venv venv" = criar ambiente virtual
python3 -m venv venv
```

```bash
# Ativamos o ambiente virtual
# "source" = executar script no terminal atual
source venv/bin/activate
```

```bash
# Criamos o requirements.txt manualmente com o comando echo
# "echo" = ecoar (exibir texto)
# O operador ">" redireciona o texto para o arquivo
echo "requests==2.31.0" > requirements.txt
```

```bash
# Verificamos o conteudo do arquivo
# "cat" = exibir conteudo de arquivo
cat requirements.txt
```

Saida esperada:
```
requests==2.31.0
```

```bash
# Instalamos as dependencias a partir do arquivo
# "-r" = read (ler o arquivo)
pip3 install -r requirements.txt
```

Saida esperada:
```
Collecting requests==2.31.0
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting certifi>=2017.4.17
Collecting charset-normalizer<4,>=2
Collecting idna<4,>=2.5
Collecting urllib3<3,>=1.21.1
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.1.0
```

> Mesmo listando apenas o `requests`, o pip instalou automaticamente todas as dependências necessarias.

---

### Exercício 13 — Atualizando um Pacote

#### Enunciado

Com o ambiente virtual ativo, instale a versão `2.28.0` do pacote `requests`. Depois, atualize para a versão mais recente usando o comando de atualização do pip. Verifique a versão antes e depois da atualização.

#### Dicas

- Instale a versão antiga com `pip3 install requests==2.28.0`
- Verifique a versão com `pip3 show requests`
- Atualize com `pip3 install --upgrade requests`
- Verifique a versão novamente apos a atualização

#### Proposta de Teste

Execute os comandos no terminal e verifique:
- **Caso básico:** Apos instalar a versão 2.28.0, o `pip3 show requests` deve mostrar `Version: 2.28.0`. Apos atualizar, a versão deve ser mais recente (como 2.31.0 ou superior)
- **Caso de borda:** Tente atualizar um pacote que ja esta na versão mais recente — o pip deve informar que o requisito ja esta satisfeito

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Instalamos uma versao antiga do requests
# "==" indica a versao exata desejada
pip3 install requests==2.28.0
```

Saida esperada:
```
Collecting requests==2.28.0
  Downloading requests-2.28.0-py3-none-any.whl (62 kB)
Successfully installed requests-2.28.0
```

```bash
# Verificamos a versao instalada
# "show" = mostrar informacoes do pacote
pip3 show requests
```

Saida esperada:
```
Name: requests
Version: 2.28.0
...
```

```bash
# Atualizamos para a versao mais recente
# "--upgrade" = atualizar para a versao mais recente
pip3 install --upgrade requests
```

Saida esperada:
```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Successfully installed requests-2.31.0
```

```bash
# Verificamos a versao apos a atualizacao
pip3 show requests
```

Saida esperada:
```
Name: requests
Version: 2.31.0
...
```

> A versão mudou de 2.28.0 para 2.31.0 (ou a mais recente disponível). O comando `--upgrade` sempre instala a versão mais recente.

---

### Exercício 14 — Programa Completo com Tratamento de Erros

#### Enunciado

Crie um programa chamado `package_info.py` que pede ao usuario o nome de um pacote Python e tenta importa-lo. Se o pacote estiver instalado, o programa exibe uma mensagem de sucesso. Se não estiver instalado, o programa exibe uma mensagem orientando o usuario a instalar com pip.

#### Dicas

- Use `input()` para pedir o nome do pacote ao usuario
- Use `importlib.import_module()` para tentar importar o pacote dinamicamente
- Use `try/except` para capturar o erro `ModuleNotFoundError`
- O módulo `importlib` faz parte da biblioteca padrão (não precisa instalar)

#### Proposta de Teste

Execute o programa e verifique:
- **Caso básico:** Digite `json` (pacote da biblioteca padrão) — o programa deve informar que o pacote esta disponível
- **Caso de borda:** Digite `pacote_inexistente` — o programa deve informar que o pacote não foi encontrado e sugerir a instalacao com pip

#### Resposta Comentada

> Tente resolver o exercício sozinho primeiro! Use a resposta apenas como referência de aprendizado.

Crie o arquivo `package_info.py`:

```python
# Programa que verifica se um pacote Python esta instalado
# "package_info" = informacoes do pacote

# Importamos o modulo importlib para importar pacotes dinamicamente
# "importlib" = biblioteca de importacao (import library)
# "import_module" = importar modulo
import importlib

# Pedimos ao usuario o nome do pacote que deseja verificar
# "package_name" = nome do pacote
# input() sempre retorna uma string
package_name = input("Digite o nome do pacote que deseja verificar: ")

# Tentamos importar o pacote usando try/except
# "try" = tentar
try:
    # Tentamos importar o pacote pelo nome informado
    # import_module() importa um modulo pelo nome (como string)
    importlib.import_module(package_name)
    # Se chegou aqui, o pacote foi importado com sucesso
    print(f"O pacote '{package_name}' esta instalado e disponivel!")
# "except" = exceto (capturar erro)
# ModuleNotFoundError = erro de modulo nao encontrado
except ModuleNotFoundError:
    # Se o pacote nao foi encontrado, orientamos o usuario
    print(f"O pacote '{package_name}' NAO esta instalado.")
    # Sugerimos o comando de instalacao
    print(f"Para instalar, execute: pip3 install {package_name}")
```

Para executar:

```bash
python3 package_info.py
```

> O comando `python3 package_info.py` executa o programa.

Saida esperada (caso básico — digitando `json`):
```
Digite o nome do pacote que deseja verificar: json
O pacote 'json' esta instalado e disponivel!
```

Saida esperada (caso de borda — digitando `pacote_inexistente`):
```
Digite o nome do pacote que deseja verificar: pacote_inexistente
O pacote 'pacote_inexistente' NAO esta instalado.
Para instalar, execute: pip3 install pacote_inexistente
```

> O programa usa `try/except` para lidar com o erro de forma elegante, em vez de deixar o programa quebrar com uma mensagem de erro confusa.

---

[<- Voltar para o módulo](26-pip-dependências.md) | [Glossário](00-glossário.md)
