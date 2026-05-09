# 26 — pip e Gerenciamento de Dependências

[<- Anterior: Estruturação de Projetos](25-estruturação-projetos.md) | [Glossário](00-glossário.md) | [Próximo: Boas Práticas ->](27-boas-práticas.md)

---

## Introdução

No módulo anterior, você aprendeu a organizar seus projetos em pastas e arquivos de forma profissional. Agora vamos aprender algo que todo desenvolvedor Python precisa dominar: como **instalar e gerenciar bibliotecas externas** — códigos que outras pessoas criaram e que você pode usar nos seus projetos.

Imagine que você esta montando uma estante em casa. Você tem as ferramentas básicas: martelo, chave de fenda, parafusos. Mas para um trabalho mais sofisticado, você precisa de ferramentas especializadas: uma furadeira eletrica, um nível a laser, uma serra circular. Você não precisa fabricar essas ferramentas — basta ir a uma loja e comprar.

Em Python, funciona da mesma forma. A linguagem ja vem com muitas ferramentas prontas (a **biblioteca padrão** — módulos como `math`, `random`, `json`, `os`). Mas existem milhares de ferramentas adicionais criadas pela comunidade que você pode "comprar" (instalar) gratuitamente. O **pip** e a "loja de ferramentas" do Python — o gerenciador de pacotes que permite instalar, atualizar e remover bibliotecas externas.

Neste módulo, você vai aprender:

- O que e o pip e como ele funciona
- Como instalar, atualizar e remover pacotes com pip
- O que sao ambientes virtuais (venv) e por que sao essenciais
- Como criar, ativar e desativar ambientes virtuais
- Como usar o arquivo `requirements.txt` para gerenciar dependências
- Exemplos práticos com pacotes populares como `requests`

> **Dica:** Consulte o [Glossário](00-glossário.md) sempre que encontrar um termo desconhecido.

---

## Como Executar os Exemplos Deste Módulo

Os exemplos deste módulo envolvem comandos no terminal e instalacao de pacotes. Para praticar:

1. Abra o terminal (no Linux, pressione `Ctrl + Alt + T`)
2. Crie uma pasta para os exercícios:
   ```bash
   mkdir -p ~/meus-projetos/python-curso/módulo-26
   ```
   > O comando `mkdir -p` significa "make directory" (criar diretório/pasta). A opcao `-p` cria pastas intermediarias se não existirem.
3. Navegue ate a pasta:
   ```bash
   cd ~/meus-projetos/python-curso/módulo-26
   ```
   > O comando `cd` significa "change directory" (mudar de diretório/pasta).
4. Verifique que você esta na pasta correta:
   ```bash
   pwd
   ```
   > O comando `pwd` significa "print working directory" (mostrar diretório atual).

   Saida esperada:
   ```
   /home/seu-usuario/meus-projetos/python-curso/módulo-26
   ```

---

## O Que e o pip?

O **pip** e o gerenciador de pacotes oficial do Python. A sigla pip significa "Pip Installs Packages" (pip instala pacotes). Ele e a ferramenta que permite você instalar, atualizar e remover **pacotes** (bibliotecas) criados por outros desenvolvedores.

**Analogia:** Pense no pip como um aplicativo de loja no seu celular. Quando você quer um aplicativo novo, você abre a loja, procura o aplicativo, e instala com um toque. O pip funciona da mesma forma: você digita um comando no terminal, e ele baixa e instala a biblioteca que você precisa. A "loja" do pip se chama **PyPI** (Python Package Index — Índice de Pacotes Python), que e um repositório online com mais de 500 mil pacotes gratuitos.

### Verificando se o pip Esta Instalado

O pip ja vem instalado junto com o Python 3 na maioria das distribuicoes Linux. Vamos verificar:

1. Abra o terminal (no Linux, pressione `Ctrl + Alt + T`)
2. Digite o seguinte comando e pressione Enter:

```bash
pip3 --version
```

> O comando `pip3 --version` pede ao pip que mostre qual versão esta instalada. Usamos `pip3` (com o número 3) para garantir que estamos usando o pip do Python 3.

Saida esperada (a versão pode variar):
```
pip 23.0.1 from /usr/lib/python3/dist-packages/pip (python 3.11)
```

> A saida mostra a versão do pip, o caminho onde ele esta instalado e a versão do Python associada.

**Se aparecer um erro "comando não encontrado":**

Isso significa que o pip não esta instalado. Para instalar no Ubuntu/Debian:

```bash
sudo apt update
```

> O comando `sudo apt update` atualiza a lista de pacotes disponiveis. `sudo` significa "super user do" (executar como administrador) — e necessário para instalar programas no sistema.

```bash
sudo apt install python3-pip
```

> O comando `sudo apt install python3-pip` instala o pip para Python 3. O sistema vai pedir sua senha — digite e pressione Enter (a senha não aparece na tela enquanto você digita, isso e normal).

Saida esperada:
```
Lendo listas de pacotes... Pronto
Construindo arvore de dependencias... Pronto
python3-pip ja e a versao mais recente (23.0.1).
```

Apos a instalacao, verifique novamente:

```bash
pip3 --version
```

---

## Instalando Pacotes com pip

O comando principal do pip e o `pip install`, que baixa e instala um pacote do PyPI.

### Sintaxe Básica

```bash
pip3 install nome-do-pacote
```

> O comando `pip3 install` diz ao pip para baixar e instalar o pacote especificado. O pip automaticamente baixa o pacote da internet, resolve as dependências (outros pacotes necessários) e instala tudo.

### Exemplo Prático: Instalando o Pacote requests

O pacote **requests** e uma das bibliotecas mais populares do Python. Ele facilita fazer requisicoes HTTP — ou seja, acessar páginas da internet e APIs a partir do seu programa Python.

**Analogia:** Imagine que você quer pedir uma pizza por telefone. Você poderia discar cada número, esperar o tom, falar com a atendente, soletrar seu endereco... Ou você poderia usar um aplicativo de delivery que faz tudo isso por você com poucos toques. O `requests` e como o aplicativo de delivery: ele simplifica o processo de "conversar" com servidores na internet.

Para instalar o requests:

```bash
pip3 install requests
```

Saida esperada:
```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Collecting charset-normalizer<4,>=2
  Downloading charset_normalizer-3.3.2-py3-none-any.whl (48 kB)
Collecting idna<4,>=2.5
  Downloading idna-3.6-py3-none-any.whl (61 kB)
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.1.0-py3-none-any.whl (104 kB)
Collecting certifi>=2017.4.17
  Downloading certifi-2024.2.2-py3-none-any.whl (163 kB)
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.1.0
```

> Observe que o pip instalou não apenas o `requests`, mas também outros pacotes como `urllib3`, `idna`, `charset-normalizer` e `certifi`. Esses sao as **dependências** do requests — pacotes que ele precisa para funcionar. O pip resolve isso automaticamente para você.

### Testando o Pacote Instalado

Apos instalar, vamos testar se o pacote funciona. Crie um arquivo chamado `test_requests.py`:

```python
# Importamos o pacote requests que acabamos de instalar
# "requests" = requisicoes (pedidos a servidores na internet)
import requests

# Fazemos uma requisicao GET para uma API publica de teste
# "response" = resposta do servidor
# "get" = obter/buscar
response = requests.get("https://httpbin.org/json")

# Verificamos o codigo de status da resposta
# "status_code" = codigo de status (200 significa sucesso)
print(f"Codigo de status: {response.status_code}")

# Exibimos o conteudo da resposta em formato JSON
# "json" = formato de dados (JavaScript Object Notation)
print(f"Resposta: {response.json()}")
```

Para executar:

```bash
python3 test_requests.py
```

> O comando `python3 test_requests.py` executa o arquivo Python que acabamos de criar.

Saida esperada:
```
Codigo de status: 200
Resposta: {'slideshow': {'author': 'Yours Truly', 'date': 'date of publication', 'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, {'items': ['Why <em>WonderWidgets</em> are great', 'Who <em>buys</em> WonderWidgets'], 'title': 'Overview', 'type': 'all'}], 'title': 'Sample Slide Show'}}
```

> O código `200` significa que a requisicao foi bem-sucedida. A resposta e um dicionário Python com dados de exemplo.

---

## Outros Comandos Úteis do pip

Além de instalar pacotes, o pip oferece outros comandos importantes:

### Listar Pacotes Instalados

```bash
pip3 list
```

> O comando `pip3 list` mostra todos os pacotes Python instalados no seu sistema, junto com suas versoes.

Saida esperada (resumida):
```
Package            Version
------------------ ---------
certifi            2024.2.2
charset-normalizer 3.3.2
idna               3.6
pip                23.0.1
requests           2.31.0
setuptools         66.1.1
urllib3             2.1.0
```

### Ver Informações de um Pacote

```bash
pip3 show requests
```

> O comando `pip3 show` exibe informações detalhadas sobre um pacote específico: versão, autor, descricao, dependências e localizacao no disco.

Saida esperada:
```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
License: Apache 2.0
Location: /usr/lib/python3/dist-packages
Requires: certifi, charset-normalizer, idna, urllib3
```

### Atualizar um Pacote

```bash
pip3 install --upgrade requests
```

> O comando `pip3 install --upgrade` (ou `-U`) atualiza um pacote para a versão mais recente disponível no PyPI.

Saida esperada:
```
Requirement already satisfied: requests in /usr/lib/python3/dist-packages (2.31.0)
```

> Se o pacote ja estiver na versão mais recente, o pip informa que o requisito ja esta satisfeito.

### Desinstalar um Pacote

```bash
pip3 uninstall requests
```

> O comando `pip3 uninstall` remove um pacote instalado. O pip vai pedir confirmacao antes de remover.

Saida esperada:
```
Found existing installation: requests 2.31.0
Uninstalling requests-2.31.0:
  Would remove:
    /usr/lib/python3/dist-packages/requests/*
Proceed (Y/n)? y
  Successfully uninstalled requests-2.31.0
```

> Digite `y` (yes/sim) e pressione Enter para confirmar a remoção. Se você digitar `n` (no/não), a remoção sera cancelada.

### Instalar uma Versão Específica

As vezes você precisa instalar uma versão específica de um pacote, não a mais recente:

```bash
pip3 install requests==2.28.0
```

> O operador `==` indica a versão exata que você quer instalar. Isso e útil quando um projeto depende de uma versão específica de uma biblioteca.

Saida esperada:
```
Collecting requests==2.28.0
  Downloading requests-2.28.0-py3-none-any.whl (62 kB)
Successfully installed requests-2.28.0
```

---

## Ambientes Virtuais (venv): Por Que Sao Essenciais

Ate agora, instalamos pacotes diretamente no sistema. Isso funciona para testes rapidos, mas causa problemas serios em projetos reais. Vamos entender por que.

### O Problema: Conflito de Dependências

**Analogia:** Imagine que você tem dois aquarios em casa. Um aquario tem peixes tropicais que precisam de agua quente (28 graus). O outro tem peixes de agua fria (18 graus). Se você colocar todos os peixes no mesmo aquario, não consegue agradar a todos — a temperatura que serve para um grupo prejudica o outro.

Em Python, o mesmo problema acontece com projetos. Imagine:

- **Projeto A** precisa do pacote `requests` na versão 2.28
- **Projeto B** precisa do pacote `requests` na versão 2.31

Se ambos os projetos usam o mesmo Python do sistema, você so pode ter **uma versão** do `requests` instalada. Instalar a versão 2.31 para o Projeto B vai quebrar o Projeto A.

### A Solução: Ambientes Virtuais

Um **ambiente virtual** (virtual environment) e como criar um aquario separado para cada projeto. Cada ambiente virtual tem sua propria copia do Python e seus proprios pacotes instalados, completamente isolados dos outros projetos e do sistema.

**Analogia:** Pense em cada ambiente virtual como uma **caixa de ferramentas separada** para cada projeto. A caixa do projeto da estante tem martelo, pregos e serra. A caixa do projeto eletrico tem alicate, fios e fita isolante. Cada caixa tem exatamente o que o projeto precisa, sem misturar ferramentas.

### Vantagens dos Ambientes Virtuais

1. **Isolamento:** Cada projeto tem seus proprios pacotes, sem conflitos
2. **Reproducibilidade:** Você sabe exatamente quais pacotes cada projeto usa
3. **Limpeza:** Não polui o Python do sistema com pacotes desnecessarios
4. **Colaboracao:** Facilita compartilhar o projeto com outras pessoas

---

## Criando e Usando Ambientes Virtuais

O Python 3 ja vem com o módulo `venv` para criar ambientes virtuais. Não precisa instalar nada extra.

### Passo 1: Criar o Ambiente Virtual

Primeiro, navegue ate a pasta do seu projeto:

```bash
cd ~/meus-projetos/python-curso/modulo-26
```

> O comando `cd` muda para o diretório especificado.

Agora, crie o ambiente virtual:

```bash
python3 -m venv venv
```

> Vamos entender cada parte deste comando:
> - `python3` — executa o interpretador Python 3
> - `-m venv` — executa o módulo `venv` (módulo de ambientes virtuais)
> - `venv` (o último) — e o nome da pasta onde o ambiente virtual sera criado
>
> Você pode escolher qualquer nome para a pasta, mas `venv` e a convencao mais comum.

Saida esperada:
```
(nenhuma saida — o comando cria a pasta silenciosamente)
```

Verifique que a pasta foi criada:

```bash
ls -la
```

> O comando `ls -la` lista todos os arquivos e pastas do diretório atual, incluindo arquivos ocultos. A opcao `-l` mostra detalhes e `-a` mostra arquivos ocultos.

Saida esperada:
```
total 12
drwxr-xr-x 3 usuario usuario 4096 jan 15 10:00 .
drwxr-xr-x 4 usuario usuario 4096 jan 15 09:55 ..
drwxr-xr-x 5 usuario usuario 4096 jan 15 10:00 venv
```

> A pasta `venv` foi criada. Dentro dela, o Python copiou tudo que precisa para funcionar de forma isolada.

### Passo 2: Ativar o Ambiente Virtual

Criar o ambiente virtual não e suficiente — você precisa **ativa-lo** para que o terminal passe a usar o Python e o pip daquele ambiente.

```bash
source venv/bin/activate
```

> O comando `source` executa um script no terminal atual. O script `venv/bin/activate` configura o terminal para usar o Python e o pip do ambiente virtual.

Saida esperada:
```
(venv) usuario@computador:~/meus-projetos/python-curso/modulo-26$
```

> Observe que o nome do ambiente virtual `(venv)` apareceu no inicio da linha do terminal. Isso indica que o ambiente virtual esta **ativo**. A partir de agora, qualquer pacote que você instalar com `pip` sera instalado apenas dentro deste ambiente virtual.

### Verificando o Ambiente Ativo

Apos ativar, você pode verificar qual Python e qual pip estão sendo usados:

```bash
which python3
```

> O comando `which` mostra o caminho completo do programa que sera executado.

Saida esperada:
```
/home/usuario/meus-projetos/python-curso/modulo-26/venv/bin/python3
```

> Observe que o caminho aponta para dentro da pasta `venv`, não para o Python do sistema. Isso confirma que o ambiente virtual esta ativo.

```bash
which pip3
```

Saida esperada:
```
/home/usuario/meus-projetos/python-curso/modulo-26/venv/bin/pip3
```

> O pip também aponta para dentro da pasta `venv`.

### Passo 3: Instalar Pacotes no Ambiente Virtual

Com o ambiente virtual ativo (você ve `(venv)` no terminal), instale pacotes normalmente:

```bash
pip3 install requests
```

Saida esperada:
```
Collecting requests
  Downloading requests-2.31.0-py3-none-any.whl (62 kB)
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.1.0
```

> O pacote foi instalado **apenas** dentro do ambiente virtual. Outros projetos e o sistema não sao afetados.

Verifique os pacotes instalados no ambiente:

```bash
pip3 list
```

Saida esperada:
```
Package            Version
------------------ ---------
certifi            2024.2.2
charset-normalizer 3.3.2
idna               3.6
pip                23.0.1
requests           2.31.0
setuptools         66.1.1
urllib3             2.1.0
```

> A lista mostra apenas os pacotes do ambiente virtual — muito mais limpa que a lista do sistema.

### Passo 4: Desativar o Ambiente Virtual

Quando terminar de trabalhar no projeto, desative o ambiente virtual:

```bash
deactivate
```

> O comando `deactivate` desativa o ambiente virtual e retorna o terminal ao estado normal (usando o Python e pip do sistema).

Saida esperada:
```
usuario@computador:~/meus-projetos/python-curso/modulo-26$
```

> Observe que o `(venv)` desapareceu do inicio da linha. O terminal voltou ao normal.

---

## Fluxo Completo de Trabalho com Ambientes Virtuais

Vamos resumir o fluxo que você vai seguir sempre que trabalhar em um projeto Python:

**1. Criar o projeto (apenas uma vez):**

```bash
mkdir ~/meus-projetos/meu-novo-projeto
```

> Cria a pasta do projeto.

```bash
cd ~/meus-projetos/meu-novo-projeto
```

> Entra na pasta do projeto.

```bash
python3 -m venv venv
```

> Cria o ambiente virtual dentro da pasta do projeto.

**2. Toda vez que for trabalhar no projeto:**

```bash
cd ~/meus-projetos/meu-novo-projeto
```

> Navega ate a pasta do projeto.

```bash
source venv/bin/activate
```

> Ativa o ambiente virtual. Você vera `(venv)` no terminal.

**3. Trabalhar normalmente** — instalar pacotes, escrever código, executar programas.

**4. Quando terminar:**

```bash
deactivate
```

> Desativa o ambiente virtual.

> **Dica importante:** A pasta `venv` não deve ser compartilhada nem enviada para repositorios de código (como o Git). Ela e específica do seu computador. Em vez disso, usamos o arquivo `requirements.txt` para registrar quais pacotes o projeto precisa — e e isso que vamos aprender agora.

---

## O Arquivo requirements.txt

O arquivo `requirements.txt` e como uma **lista de compras** do seu projeto. Ele registra todos os pacotes que o projeto precisa, com suas versoes exatas. Quando outra pessoa (ou você mesmo em outro computador) quiser rodar o projeto, basta "ir ao mercado" e comprar tudo que esta na lista.

### Gerando o requirements.txt Automaticamente

Com o ambiente virtual ativo, use o comando `pip freeze`:

```bash
pip3 freeze
```

> O comando `pip3 freeze` lista todos os pacotes instalados no ambiente virtual, no formato `pacote==versao`. O nome "freeze" (congelar) vem da ideia de "congelar" o estado atual das dependências.

Saida esperada:
```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.1.0
```

Para salvar essa lista em um arquivo `requirements.txt`:

```bash
pip3 freeze > requirements.txt
```

> O operador `>` redireciona a saida do comando para um arquivo. Em vez de mostrar a lista no terminal, o comando salva no arquivo `requirements.txt`.

Verifique que o arquivo foi criado:

```bash
cat requirements.txt
```

> O comando `cat` exibe o conteúdo de um arquivo no terminal.

Saida esperada:
```
certifi==2024.2.2
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
urllib3==2.1.0
```

### Instalando Dependências a Partir do requirements.txt

Quando você (ou outra pessoa) precisar configurar o projeto em um novo computador, basta:

**1. Criar e ativar o ambiente virtual:**

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

**2. Instalar todas as dependências de uma vez:**

```bash
pip3 install -r requirements.txt
```

> O comando `pip3 install -r` (a opcao `-r` significa "read" — ler) le o arquivo `requirements.txt` e instala todos os pacotes listados, nas versoes exatas especificadas.

Saida esperada:
```
Collecting certifi==2024.2.2
  Using cached certifi-2024.2.2-py3-none-any.whl
Collecting charset-normalizer==3.3.2
  Using cached charset_normalizer-3.3.2-py3-none-any.whl
Collecting idna==3.6
  Using cached idna-3.6-py3-none-any.whl
Collecting requests==2.31.0
  Using cached requests-2.31.0-py3-none-any.whl
Collecting urllib3==2.1.0
  Using cached urllib3-2.1.0-py3-none-any.whl
Installing collected packages: urllib3, idna, charset-normalizer, certifi, requests
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 idna-3.6 requests-2.31.0 urllib3-2.1.0
```

> Todos os pacotes foram instalados nas versoes exatas. O projeto esta pronto para rodar.

### Criando o requirements.txt Manualmente

Você também pode criar o `requirements.txt` manualmente, listando apenas os pacotes que você instalou diretamente (sem as dependências automaticas):

```
requests==2.31.0
```

> Quando você instalar o `requests`, o pip automaticamente instalara as dependências dele (`certifi`, `urllib3`, etc.). Por isso, listar apenas o `requests` ja e suficiente.

Ambas as abordagens funcionam. O `pip freeze` e mais completo (lista tudo), enquanto a abordagem manual e mais limpa (lista apenas o essencial).

---

## Exemplo Prático Completo: Projeto com Dependências

Vamos criar um projeto completo do zero, usando tudo que aprendemos neste módulo.

### O Projeto: Consultar Previsao do Tempo

Vamos criar um programa que consulta uma API pública e exibe dados formatados.

**Passo 1: Criar a estrutura do projeto**

```bash
mkdir ~/meus-projetos/consulta-clima
```

> Cria a pasta do projeto.

```bash
cd ~/meus-projetos/consulta-clima
```

> Entra na pasta do projeto.

```bash
python3 -m venv venv
```

> Cria o ambiente virtual.

```bash
source venv/bin/activate
```

> Ativa o ambiente virtual. Você vera `(venv)` no terminal.

**Passo 2: Instalar as dependências**

```bash
pip3 install requests
```

> Instala o pacote requests no ambiente virtual.

**Passo 3: Gerar o requirements.txt**

```bash
pip3 freeze > requirements.txt
```

> Salva a lista de dependências no arquivo.

**Passo 4: Criar o programa**

Crie o arquivo `weather.py` com o seguinte conteúdo:

```python
# Programa que consulta dados de uma API publica
# "weather" = clima/tempo

# Importamos o pacote requests para fazer requisicoes HTTP
# "requests" = requisicoes
import requests

# Funcao que busca dados de uma API publica de teste
# "fetch" = buscar, "data" = dados
def fetch_data():
    # URL da API publica de teste (nao precisa de cadastro)
    # "url" = endereco na internet
    url = "https://httpbin.org/get"

    # Fazemos a requisicao GET (buscar dados)
    # "response" = resposta do servidor
    response = requests.get(url)

    # Verificamos se a requisicao foi bem-sucedida
    # "status_code" = codigo de status (200 = sucesso)
    if response.status_code == 200:
        # Convertemos a resposta para dicionario Python
        # "data" = dados
        data = response.json()
        # Exibimos a origem da requisicao
        # "origin" = origem (endereco IP)
        print(f"Sua requisicao veio do IP: {data['origin']}")
        # Exibimos a URL acessada
        print(f"URL acessada: {data['url']}")
    else:
        # Se houve erro, exibimos o codigo de status
        print(f"Erro na requisicao. Codigo: {response.status_code}")

# Chamamos a funcao principal
# Verificamos se o arquivo esta sendo executado diretamente
if __name__ == "__main__":
    # Exibimos uma mensagem de boas-vindas
    print("Consultando API publica...")
    # Chamamos a funcao que busca os dados
    fetch_data()
    # Exibimos mensagem de conclusao
    print("Consulta finalizada!")
```

**Passo 5: Executar o programa**

```bash
python3 weather.py
```

> O comando `python3 weather.py` executa o programa que acabamos de criar.

Saida esperada:
```
Consultando API publica...
Sua requisicao veio do IP: 203.0.113.42
URL acessada: https://httpbin.org/get
Consulta finalizada!
```

> O IP exibido sera diferente no seu computador — ele mostra o endereco de internet da sua conexão.

**Passo 6: Verificar a estrutura final do projeto**

```bash
ls -la
```

Saida esperada:
```
total 16
drwxr-xr-x 3 usuario usuario 4096 jan 15 10:30 .
drwxr-xr-x 5 usuario usuario 4096 jan 15 10:25 ..
-rw-r--r-- 1 usuario usuario  120 jan 15 10:28 requirements.txt
drwxr-xr-x 5 usuario usuario 4096 jan 15 10:26 venv
-rw-r--r-- 1 usuario usuario  850 jan 15 10:29 weather.py
```

> O projeto tem: o arquivo do programa (`weather.py`), o arquivo de dependências (`requirements.txt`) e a pasta do ambiente virtual (`venv`).

---

## Pacotes Populares do Python

Existem milhares de pacotes disponiveis no PyPI. Aqui estão alguns dos mais populares que você pode encontrar ao longo da sua jornada como desenvolvedor:

| Pacote | Para que serve | Comando de instalacao |
|--------|---------------|----------------------|
| `requests` | Fazer requisicoes HTTP (acessar APIs e sites) | `pip3 install requests` |
| `flask` | Criar aplicações web simples | `pip3 install flask` |
| `fastapi` | Criar APIs HTTP modernas e rapidas | `pip3 install fastapi` |
| `uvicorn` | Servidor para rodar aplicações FastAPI | `pip3 install uvicorn` |
| `pillow` | Manipular imagens (redimensionar, cortar, filtros) | `pip3 install pillow` |
| `python-dotenv` | Carregar variáveis de ambiente de arquivos `.env` | `pip3 install python-dotenv` |
| `rich` | Formatar saidas coloridas e tabelas no terminal | `pip3 install rich` |

> **Nota:** Você não precisa instalar todos esses pacotes agora. Esta tabela serve como referência para quando você precisar de funcionalidades especificas nos seus projetos futuros. Nos módulos 31 e 32 deste curso, você vai usar o `fastapi` e o `uvicorn` para criar uma API HTTP.

---

## Boas Práticas com pip e Ambientes Virtuais

1. **Sempre use ambientes virtuais** — Nunca instale pacotes diretamente no Python do sistema para projetos reais. Use `python3 -m venv venv` em cada projeto.

2. **Mantenha o requirements.txt atualizado** — Sempre que instalar ou remover um pacote, atualize o arquivo com `pip3 freeze > requirements.txt`.

3. **Não compartilhe a pasta venv** — A pasta `venv` e específica do seu computador. Compartilhe apenas o `requirements.txt`. Se você usar Git, adicione `venv/` ao arquivo `.gitignore`.

4. **Use versoes especificas** — No `requirements.txt`, use `==` para fixar versoes exatas. Isso garante que todos que usarem o projeto terao as mesmas versoes dos pacotes.

5. **Instale apenas o necessário** — Não instale pacotes "por precaucao". Instale apenas o que o projeto realmente precisa.

6. **Verifique a fonte dos pacotes** — Antes de instalar um pacote, verifique se ele e confiavel. Pacotes populares com muitos downloads no PyPI sao geralmente seguros.

---

## Para Saber Mais

- [W3Schools — Python pip](https://www.w3schools.com/python/python_pip.asp)
  _Aqui você encontra uma introdução ao pip com exemplos simples e interativos_
- [Documentação Oficial Python — venv](https://docs.python.org/pt-br/3/library/venv.html)
  _Referencia completa sobre o módulo venv para criação de ambientes virtuais_
- [Documentação Oficial Python — Instalando Módulos](https://docs.python.org/pt-br/3/installing/index.html)
  _Guia oficial sobre como instalar pacotes Python com pip_
- [PyPI — Python Package Index](https://pypi.org/)
  _O repositório oficial de pacotes Python — aqui você pode buscar e descobrir novos pacotes_
- [W3Schools — Python Modules](https://www.w3schools.com/python/python_modules.asp)
  _Mais informações sobre módulos e como importa-los_
- [Real Python — Virtual Environments (em ingles)](https://realpython.com/python-virtual-environments-a-primer/)
  _Um guia detalhado sobre ambientes virtuais para quem quiser se aprofundar_

> **Dica:** Consulte o [Glossário](00-glossário.md) para revisar termos como "pacote", "dependência", "ambiente virtual" e outros conceitos deste módulo.

---

## Perguntas Frequentes (FAQ)

**P: O que e o pip?**
**R:** O pip e o gerenciador de pacotes oficial do Python. Ele permite instalar, atualizar e remover bibliotecas (pacotes) criadas por outros desenvolvedores. Pense nele como uma "loja de aplicativos" para o Python — você digita um comando e ele baixa e instala o que você precisa.

**P: Qual a diferença entre pip e pip3?**
**R:** Em muitos sistemas Linux, `pip` pode estar associado ao Python 2 (versão antiga), enquanto `pip3` esta associado ao Python 3 (versão atual). Para garantir que você esta usando o pip do Python 3, sempre use `pip3`. Dentro de um ambiente virtual, tanto `pip` quanto `pip3` funcionam da mesma forma.

**P: O que e um pacote Python?**
**R:** Um pacote e um conjunto de código Python criado por alguem e disponibilizado para que outros desenvolvedores possam usar. Por exemplo, o pacote `requests` facilita fazer requisicoes HTTP. Em vez de escrever centenas de linhas de código para acessar uma API, você instala o `requests` e usa poucas linhas.

**P: O que e o PyPI?**
**R:** PyPI (Python Package Index) e o repositório oficial de pacotes Python. E como um grande mercado online onde desenvolvedores publicam seus pacotes gratuitamente. Quando você executa `pip3 install nome-do-pacote`, o pip baixa o pacote do PyPI.

**P: O que sao dependências?**
**R:** Dependências sao pacotes que um pacote precisa para funcionar. Por exemplo, o `requests` depende do `urllib3` e do `certifi`. Quando você instala o `requests`, o pip automaticamente instala essas dependências. E como comprar um movel que precisa de parafusos específicos — a loja inclui os parafusos na caixa.

**P: O que e um ambiente virtual?**
**R:** Um ambiente virtual e uma copia isolada do Python criada dentro da pasta do seu projeto. Ele tem seu proprio pip e seus proprios pacotes, separados do Python do sistema e de outros projetos. Pense nele como uma "caixa de ferramentas" exclusiva para cada projeto.

**P: Por que preciso usar ambientes virtuais?**
**R:** Sem ambientes virtuais, todos os seus projetos compartilham os mesmos pacotes. Se o Projeto A precisa da versão 1.0 de um pacote e o Projeto B precisa da versão 2.0, você tem um conflito. Ambientes virtuais resolvem isso isolando os pacotes de cada projeto.

**P: O que acontece se eu não usar ambiente virtual?**
**R:** Seus pacotes serao instalados no Python do sistema, o que pode causar conflitos entre projetos, dificultar a reproducao do projeto em outro computador e poluir o sistema com pacotes desnecessarios. Para projetos de estudo simples pode funcionar, mas para projetos reais e uma ma prática.

**P: Preciso criar um ambiente virtual para cada projeto?**
**R:** Sim, essa e a prática recomendada. Cada projeto deve ter seu proprio ambiente virtual. Isso garante que as dependências de um projeto não interfiram nas de outro.

**P: A pasta venv ocupa muito espaco?**
**R:** Uma pasta `venv` básica ocupa cerca de 10 a 20 MB. Conforme você instala pacotes, o tamanho aumenta. Isso e normal e não deve ser uma preocupacao — o beneficio do isolamento compensa o espaco usado.

**P: Posso apagar a pasta venv e criar de novo?**
**R:** Sim, sem problema. A pasta `venv` pode ser recriada a qualquer momento. Basta executar `python3 -m venv venv` novamente e depois `pip3 install -r requirements.txt` para reinstalar os pacotes. Por isso o `requirements.txt` e tao importante — ele e o "backup" das suas dependências.

**P: O que e o requirements.txt?**
**R:** E um arquivo de texto simples que lista todos os pacotes que seu projeto precisa, com suas versoes. Ele funciona como uma "lista de compras" — quando alguem quiser rodar seu projeto, basta instalar tudo que esta na lista com `pip3 install -r requirements.txt`.

**P: Qual a diferença entre pip install e pip install -r?**
**R:** O `pip3 install nome-do-pacote` instala um único pacote. O `pip3 install -r requirements.txt` le um arquivo e instala todos os pacotes listados nele de uma vez. O `-r` vem de "read" (ler).

**P: O que faz o comando pip freeze?**
**R:** O `pip3 freeze` lista todos os pacotes instalados no ambiente atual, no formato `pacote==versao`. E usado para gerar o `requirements.txt`. O nome "freeze" (congelar) vem da ideia de registrar o estado exato das dependências naquele momento.

**P: E normal ter dificuldade com o terminal?**
**R:** Completamente normal. O terminal pode parecer intimidador no inicio, mas com prática ele se torna uma ferramenta poderosa. Cada comando que você aprende e uma nova habilidade. Não tenha pressa — releia as instruções quantas vezes precisar.

**P: Preciso decorar todos os comandos do pip?**
**R:** Não. Os comandos mais usados sao `pip3 install`, `pip3 freeze` e `pip3 list`. Com o tempo, você vai memorizar naturalmente. Enquanto isso, consulte este módulo sempre que precisar.

**P: O que acontece se eu instalar um pacote sem ativar o ambiente virtual?**
**R:** O pacote sera instalado no Python do sistema (instalacao global). Isso não e um erro grave, mas pode causar conflitos com outros projetos. Se isso acontecer, você pode desinstalar o pacote com `pip3 uninstall nome-do-pacote` e reinstala-lo dentro do ambiente virtual.

**P: Como sei se o ambiente virtual esta ativo?**
**R:** Quando o ambiente virtual esta ativo, você ve o nome dele entre parenteses no inicio da linha do terminal, por exemplo: `(venv) usuario@computador:~$`. Se não aparecer `(venv)`, o ambiente não esta ativo.

**P: Posso ter mais de um ambiente virtual no mesmo projeto?**
**R:** Tecnicamente sim, mas não e recomendado. O padrão e ter um único ambiente virtual por projeto, geralmente na pasta `venv`. Ter multiplos ambientes virtuais no mesmo projeto causa confusao.

**P: O que e o source no comando source venv/bin/activate?**
**R:** O `source` e um comando do terminal Linux que executa um script no contexto do terminal atual. Sem o `source`, o script seria executado em um processo separado e as configuracoes do ambiente virtual não seriam aplicadas ao seu terminal.

**P: Consigo usar o pip no Windows?**
**R:** Sim, o pip funciona no Windows também. A principal diferença e no comando de ativacao do ambiente virtual: no Windows, você usa `venv\Scripts\activate` em vez de `source venv/bin/activate`. Neste curso, focamos no Linux, mas os conceitos sao os mesmos.

---

## Resumo dos Comandos

Aqui esta uma tabela de referência rapida com todos os comandos que você aprendeu neste módulo:

| Comando | O que faz |
|---------|-----------|
| `pip3 --version` | Mostra a versão do pip instalada |
| `pip3 install pacote` | Instala um pacote |
| `pip3 install pacote==1.0` | Instala uma versão específica |
| `pip3 install --upgrade pacote` | Atualiza um pacote para a versão mais recente |
| `pip3 uninstall pacote` | Remove um pacote |
| `pip3 list` | Lista todos os pacotes instalados |
| `pip3 show pacote` | Mostra informações detalhadas de um pacote |
| `pip3 freeze` | Lista pacotes no formato `pacote==versao` |
| `pip3 freeze > requirements.txt` | Salva a lista de pacotes em um arquivo |
| `pip3 install -r requirements.txt` | Instala todos os pacotes de um arquivo |
| `python3 -m venv venv` | Cria um ambiente virtual na pasta `venv` |
| `source venv/bin/activate` | Ativa o ambiente virtual |
| `deactivate` | Desativa o ambiente virtual |

---

## Exercícios de Fixacao

Os exercícios deste módulo estão no arquivo separado: [Exercícios — pip e Dependências](26-pip-dependências-exercícios.md)

---

[<- Anterior: Estruturação de Projetos](25-estruturação-projetos.md) | [Glossário](00-glossário.md) | [Próximo: Boas Práticas ->](27-boas-práticas.md)
