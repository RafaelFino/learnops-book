# 3.6 — Ferramentas de Rede: curl e wget

[← Anterior: Editores de Texto no Terminal: vim e micro](cap03-mod05-editores-terminal.md) · [Próximo: O que é Controle de Versão e por que Importa →](cap04-mod01-controle-versao.md)

---

## Introdução

Ao longo deste capítulo, construímos um arsenal completo de ferramentas de terminal: navegamos pelo sistema de arquivos, manipulamos arquivos, conectamos comandos com pipes, monitoramos processos e editamos texto. Tudo isso aconteceu dentro do seu computador — trabalhamos com arquivos locais, processos locais, dados locais.

Mas o mundo real da tecnologia não funciona assim. Programas conversam com outros programas pela rede. Seu navegador busca páginas na internet. Aplicativos no celular enviam dados para servidores. Serviços em nuvem trocam informações entre si o tempo todo. A internet é, essencialmente, uma rede gigante de computadores que se comunicam.

E se você pudesse fazer isso direto do terminal? Sem abrir o navegador, sem interface gráfica — apenas digitar um comando e receber dados de qualquer lugar do mundo?

É exatamente isso que as ferramentas deste módulo fazem. O **curl** e o **wget** são comandos que permitem fazer requisições de rede direto do terminal. Com eles, você pode:

- Baixar arquivos da internet
- Acessar páginas web e ver o código HTML
- Testar APIs (interfaces de comunicação entre programas)
- Enviar dados para servidores
- Automatizar downloads em scripts
- Verificar se um serviço está funcionando

Lembre-se do mantra: **"Qual problema você quer resolver?"** O problema é: como interagir com a rede e a internet usando apenas o terminal? A solução: curl e wget.

Este é o último módulo do Capítulo 3, e ele faz uma ponte importante com o futuro. No Capítulo 10, vamos construir APIs com Python e FastAPI. Para testar essas APIs, vamos usar exatamente o `curl`. Então o que você aprender aqui vai ser usado diretamente quando começar a programar sistemas que se comunicam pela rede.

---

## Como Computadores se Comunicam: O Básico

Antes de usar curl e wget, precisamos entender o mínimo sobre como computadores se comunicam pela rede. Não vamos entrar em profundidade aqui — isso será aprofundado nos Capítulos 9 e 10 — mas precisamos de alguns conceitos básicos.

### Endereços IP e Portas

No módulo 1.9, vimos que a internet é uma rede de computadores conectados. Cada computador na rede tem um **endereço IP** (Internet Protocol) — um número que o identifica, como um endereço postal identifica uma casa.

```
Exemplos de enderecos IP:
192.168.1.1       <- endereco na rede local (sua casa)
10.0.0.5          <- endereco em rede privada (empresa)
142.250.79.46     <- endereco publico (Google)
```

Mas um computador pode rodar vários serviços ao mesmo tempo — um servidor web, um banco de dados, um serviço de email. Como saber para qual serviço enviar a mensagem? Para isso existem as **portas** — números de 0 a 65535 que identificam qual serviço deve receber a comunicação.

A analogia: o endereço IP é como o endereço de um prédio comercial. A porta é o número da sala dentro do prédio. O prédio é o computador, e cada sala é um serviço diferente.

| Porta | Servico | O que faz |
|-------|---------|-----------|
| 80 | HTTP | Páginas web sem criptografia |
| 443 | HTTPS | Páginas web com criptografia |
| 22 | SSH | Acesso remoto seguro ao terminal |
| 21 | FTP | Transferencia de arquivos |
| 25 | SMTP | Envio de email |
| 3306 | MySQL | Banco de dados MySQL |
| 5432 | PostgreSQL | Banco de dados PostgreSQL |
| 8080 | HTTP alternativo | Servidores de desenvolvimento |

Quando você digita `https://www.google.com` no navegador, o que acontece por baixo dos panos é:
1. O navegador descobre o IP do `www.google.com` (usando DNS — Domain Name System)
2. Conecta no IP `142.250.79.46` na porta `443` (HTTPS)
3. Envia uma requisição pedindo a página
4. Recebe a resposta com o HTML da página
5. Renderiza o HTML na tela

O curl e o wget fazem os passos 1 a 4. O passo 5 (renderizar) é trabalho do navegador — no terminal, você vê o HTML cru.

### URLs: Endereços da Web

Uma **URL** (Uniform Resource Locator — Localizador Uniforme de Recursos) é o endereço completo de um recurso na internet. Vamos destrinchar as partes:

```
https://api.exemplo.com:8080/v1/usuarios?nome=ana&ativo=true
|_____|  |_____________| |__| |_________| |________________|
protocolo    servidor    porta   caminho    parametros
```

| Parte | O que e | Exemplo |
|-------|---------|---------|
| Protocolo | Como se comunicar | https, http, ftp |
| Servidor | Onde esta o recurso | api.exemplo.com |
| Porta | Qual servico no servidor | 8080 (opcional, padrão depende do protocolo) |
| Caminho | Qual recurso específico | /v1/usuarios |
| Parametros | Filtros e opcoes | ?nome=ana&ativo=true |

### HTTP: O Protocolo da Web

O **HTTP** (HyperText Transfer Protocol — Protocolo de Transferência de Hipertexto) é o protocolo que a web usa para comunicação. Ele funciona no modelo **requisição-resposta**: o cliente (seu navegador ou o curl) envia uma requisição, e o servidor envia uma resposta.

Cada requisição HTTP tem um **método** que indica o que o cliente quer fazer:

| Método | O que faz | Analogia | Exemplo |
|--------|-----------|----------|---------|
| GET | Buscar dados | Pedir um livro na biblioteca | Acessar uma página web |
| POST | Enviar dados novos | Entregar um formulário preenchido | Criar uma conta |
| PUT | Atualizar dados existentes | Devolver um livro com anotacoes | Atualizar perfil |
| DELETE | Remover dados | Pedir para remover um livro do catalogo | Apagar uma conta |
| PATCH | Atualizar parcialmente | Corrigir uma página do livro | Mudar apenas o email |
| HEAD | Buscar apenas cabecalhos | Perguntar se o livro existe sem pegar | Verificar se URL existe |

Esses métodos correspondem exatamente às operações CRUD que vimos no módulo 3.2:
- **C**reate = POST
- **R**ead = GET
- **U**pdate = PUT/PATCH
- **D**elete = DELETE

Cada resposta HTTP vem com um **código de status** — um número que indica o que aconteceu:

| Faixa | Significado | Exemplos comuns |
|-------|-------------|-----------------|
| 1xx | Informativo | 100 Continue |
| 2xx | Sucesso | 200 OK, 201 Created, 204 No Content |
| 3xx | Redirecionamento | 301 Moved Permanently, 302 Found |
| 4xx | Erro do cliente | 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found |
| 5xx | Erro do servidor | 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable |

O código mais famoso é o **404 Not Found** — "não encontrado". Quando você acessa uma página que não existe, o servidor responde com 404. O **200 OK** é o código de sucesso — tudo funcionou como esperado.

---

## curl: O Canivete Suíço da Rede

O **curl** (Client URL — URL do Cliente) é uma das ferramentas mais versáteis do Linux. Criado em 1998 por Daniel Stenberg, o curl permite transferir dados de e para servidores usando diversos protocolos (HTTP, HTTPS, FTP, SFTP e muitos outros).

O curl é usado por milhões de desenvolvedores diariamente para testar APIs, baixar arquivos, automatizar interações com serviços web e diagnosticar problemas de rede. Está instalado por padrão em praticamente todo sistema Linux e macOS.

### Requisições GET Básicas

O uso mais simples do curl é fazer uma requisição GET — buscar dados de uma URL:

```bash
# Acessar uma pagina web (mostra o HTML)
curl https://www.example.com

# Acessar uma API publica (mostra dados em JSON)
curl https://api.github.com

# Acessar com mais detalhes (mostra cabecalhos da resposta)
curl -i https://www.example.com
# -i = include headers (incluir cabecalhos)

# Mostrar APENAS os cabecalhos (sem o corpo)
curl -I https://www.example.com
# -I = HEAD request (requisicao HEAD)

# Modo silencioso (sem barra de progresso)
curl -s https://api.github.com
# -s = silent (silencioso)

# Modo verbose (mostra tudo: conexao, cabecalhos enviados e recebidos)
curl -v https://www.example.com
# -v = verbose (detalhado)
```

Saída esperada (curl -I https://www.example.com):
```
HTTP/2 200
content-type: text/html; charset=UTF-8
content-length: 1256
last-modified: Thu, 17 Oct 2019 07:18:26 GMT
server: ECS (dcb/7F83)
```

Cada linha é um **cabeçalho** (header) da resposta:
- `HTTP/2 200` — versão do protocolo e código de status (200 = sucesso)
- `content-type: text/html` — o tipo do conteúdo (HTML neste caso)
- `content-length: 1256` — tamanho do conteúdo em bytes
- `server: ECS` — qual software de servidor está respondendo

### Salvando a Resposta em Arquivo

```bash
# Salvar a saida em um arquivo (com o nome que voce escolher)
curl -o pagina.html https://www.example.com
# -o = output (saida para arquivo com nome especificado)

# Salvar com o nome original do arquivo na URL
curl -O https://exemplo.com/relatorio.pdf
# -O = remote-name (usar o nome do arquivo remoto)

# Baixar e salvar silenciosamente
curl -sO https://exemplo.com/dados.csv

# Baixar mostrando barra de progresso
curl -# -O https://exemplo.com/arquivo-grande.zip
# -# = progress bar (barra de progresso simples)
```

### Enviando Dados: Requisições POST

Para enviar dados para um servidor, usamos o método POST com a opção `-X POST` e `-d` para os dados:

```bash
# Enviar dados de formulario
curl -X POST -d "nome=Ana&email=ana@exemplo.com" https://api.exemplo.com/usuarios

# Enviar dados em formato JSON
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ana", "email": "ana@exemplo.com"}' \
  https://api.exemplo.com/usuarios
# -X POST = metodo POST
# -H = header (cabecalho personalizado)
# -d = data (dados a enviar)

# Enviar dados de um arquivo
curl -X POST \
  -H "Content-Type: application/json" \
  -d @dados.json \
  https://api.exemplo.com/usuarios
# @dados.json = ler dados do arquivo dados.json
```

A barra invertida `\` no final da linha permite quebrar um comando longo em várias linhas para facilitar a leitura. O bash entende que o comando continua na próxima linha.

### Outros Métodos HTTP

```bash
# PUT - atualizar um recurso existente
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ana Silva", "email": "ana.silva@exemplo.com"}' \
  https://api.exemplo.com/usuarios/42

# PATCH - atualizar parcialmente
curl -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"email": "novo@exemplo.com"}' \
  https://api.exemplo.com/usuarios/42

# DELETE - remover um recurso
curl -X DELETE https://api.exemplo.com/usuarios/42

# HEAD - verificar se o recurso existe (sem baixar o conteudo)
curl -I https://api.exemplo.com/usuarios/42
```

### Cabeçalhos Personalizados

Muitas APIs exigem cabeçalhos específicos — autenticação, tipo de conteúdo, versão da API:

```bash
# Enviar cabecalho de autenticacao
curl -H "Authorization: Bearer meu-token-secreto" \
  https://api.exemplo.com/dados-protegidos

# Enviar API key
curl -H "X-API-Key: abc123def456" \
  https://api.exemplo.com/dados

# Multiplos cabecalhos
curl -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer token123" \
  https://api.exemplo.com/usuarios

# Simular um navegador (util quando o servidor bloqueia curl)
curl -H "User-Agent: Mozilla/5.0" \
  https://www.exemplo.com
```

### Autenticação

```bash
# Autenticacao basica (usuario e senha)
curl -u usuario:senha https://api.exemplo.com/protegido

# Autenticacao basica (pede a senha interativamente)
curl -u usuario https://api.exemplo.com/protegido

# Autenticacao com token Bearer
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  https://api.exemplo.com/protegido
```

### Seguindo Redirecionamentos

Muitos sites redirecionam de HTTP para HTTPS, ou de `www` para sem `www`. Por padrão, o curl não segue redirecionamentos:

```bash
# Sem -L: para no redirecionamento
curl http://google.com
# Resposta: 301 Moved Permanently

# Com -L: segue o redirecionamento automaticamente
curl -L http://google.com
# Resposta: conteudo da pagina final
# -L = location (seguir redirecionamentos)
```

### Timeout e Limites

```bash
# Definir timeout de conexao (em segundos)
curl --connect-timeout 5 https://servidor-lento.com

# Definir timeout total da operacao
curl --max-time 30 https://servidor-lento.com

# Limitar velocidade de download
curl --limit-rate 100K -O https://exemplo.com/arquivo-grande.zip
# Limita a 100 KB/s

# Retomar download interrompido
curl -C - -O https://exemplo.com/arquivo-grande.zip
# -C - = continue (continuar de onde parou)
```

### Opções Mais Usadas do curl

| Opcao | Forma longa | O que faz |
|-------|-------------|-----------|
| `-o` | `--output` | Salvar em arquivo com nome especificado |
| `-O` | `--remote-name` | Salvar com nome original da URL |
| `-s` | `--silent` | Modo silencioso, sem barra de progresso |
| `-S` | `--show-error` | Mostrar erros mesmo no modo silencioso |
| `-v` | `--verbose` | Modo detalhado, mostra tudo |
| `-i` | `--include` | Incluir cabecalhos na saida |
| `-I` | `--head` | Mostrar apenas cabecalhos |
| `-L` | `--location` | Seguir redirecionamentos |
| `-X` | `--request` | Especificar método HTTP |
| `-H` | `--header` | Adicionar cabecalho personalizado |
| `-d` | `--data` | Enviar dados no corpo da requisicao |
| `-u` | `--user` | Autenticação usuario:senha |
| `-k` | `--insecure` | Ignorar erros de certificado SSL |
| `-w` | `--write-out` | Formato personalizado de saida |
| `-C` | `--continue-at` | Retomar download interrompido |

### curl com Pipes

O curl se integra perfeitamente com pipes, seguindo a filosofia Unix:

```bash
# Baixar e processar JSON com jq (se instalado)
curl -s https://api.github.com/users/torvalds | jq '.name, .bio'

# Baixar e contar linhas
curl -s https://www.example.com | wc -l

# Baixar e buscar texto especifico
curl -s https://www.example.com | grep "<title>"

# Baixar e salvar apenas parte do conteudo
curl -s https://api.exemplo.com/dados | grep "erro" > erros.txt

# Verificar se um site esta no ar (apenas o codigo de status)
curl -s -o /dev/null -w "%{http_code}" https://www.google.com
# -o /dev/null = descarta o corpo da resposta
# -w "%{http_code}" = mostra apenas o codigo HTTP
# Saida: 200
```

O último exemplo é muito usado em scripts de monitoramento — verifica se um serviço está respondendo sem baixar todo o conteúdo.

### Formato de Saída Personalizado

A opção `-w` (write-out) permite extrair informações específicas da requisição:

```bash
# Medir tempo de resposta
curl -s -o /dev/null -w "Tempo total: %{time_total}s\n" https://www.google.com
# Saida: Tempo total: 0.245s

# Informacoes detalhadas de performance
curl -s -o /dev/null -w "\
  DNS: %{time_namelookup}s\n\
  Conexao: %{time_connect}s\n\
  TLS: %{time_appconnect}s\n\
  Primeiro byte: %{time_starttransfer}s\n\
  Total: %{time_total}s\n\
  Codigo: %{http_code}\n\
  Tamanho: %{size_download} bytes\n" \
  https://www.google.com
```

Saída esperada:
```
  DNS: 0.012s
  Conexao: 0.045s
  TLS: 0.120s
  Primeiro byte: 0.180s
  Total: 0.245s
  Codigo: 200
  Tamanho: 14573 bytes
```

Isso é extremamente útil para diagnosticar problemas de performance — você pode ver exatamente onde o tempo está sendo gasto: na resolução DNS, na conexão, na negociação TLS ou na resposta do servidor.

---

## wget: O Especialista em Downloads

O **wget** (Web Get — Buscar da Web) é uma ferramenta focada em downloads. Enquanto o curl é um canivete suíço que faz muitas coisas, o wget é especialista em uma: baixar arquivos de forma confiável.

O wget foi criado em 1996 por Hrvoje Nikšić e tem características que o tornam ideal para downloads:
- Retoma downloads interrompidos automaticamente
- Baixa sites inteiros recursivamente
- Funciona em background
- Lida bem com conexões instáveis

### Downloads Básicos

```bash
# Baixar um arquivo
wget https://exemplo.com/relatorio.pdf

# Baixar e salvar com outro nome
wget -O meu-relatorio.pdf https://exemplo.com/relatorio.pdf

# Baixar em modo silencioso
wget -q https://exemplo.com/relatorio.pdf

# Baixar mostrando barra de progresso
wget --show-progress https://exemplo.com/arquivo-grande.zip

# Baixar em background (libera o terminal)
wget -b https://exemplo.com/arquivo-enorme.iso
# O progresso e salvo em wget-log
# Use tail -f wget-log para acompanhar
```

Saída esperada (wget normal):
```
--2025-01-15 11:30:00--  https://exemplo.com/relatorio.pdf
Resolving exemplo.com... 93.184.216.34
Connecting to exemplo.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1048576 (1.0M) [application/pdf]
Saving to: 'relatorio.pdf'

relatorio.pdf       100%[===================>]   1.00M  2.50MB/s    in 0.4s

2025-01-15 11:30:01 (2.50 MB/s) - 'relatorio.pdf' saved [1048576/1048576]
```

### Retomando Downloads

Uma das maiores vantagens do wget é retomar downloads interrompidos:

```bash
# Retomar download interrompido
wget -c https://exemplo.com/arquivo-grande.iso
# -c = continue (continuar de onde parou)

# Se a conexao cair no meio de um download de 2GB,
# basta executar o mesmo comando com -c
# O wget verifica quanto ja foi baixado e continua do ponto onde parou
```

### Baixando Múltiplos Arquivos

```bash
# Baixar varios arquivos de uma lista
wget -i lista-urls.txt
# O arquivo lista-urls.txt contem uma URL por linha

# Exemplo de lista-urls.txt:
# https://exemplo.com/arquivo1.pdf
# https://exemplo.com/arquivo2.pdf
# https://exemplo.com/arquivo3.pdf

# Baixar todos os arquivos PDF de uma pagina
wget -r -l 1 -A "*.pdf" https://exemplo.com/documentos/
# -r = recursive (recursivo)
# -l 1 = level 1 (apenas 1 nivel de profundidade)
# -A = accept (aceitar apenas arquivos que casam com o padrao)
```

### Download Recursivo (Espelhamento de Sites)

O wget pode baixar um site inteiro, seguindo links:

```bash
# Baixar um site inteiro para leitura offline
wget -r -l 3 -p -k https://www.exemplo.com
# -r = recursive (seguir links)
# -l 3 = ate 3 niveis de profundidade
# -p = page-requisites (baixar CSS, imagens, JS necessarios)
# -k = convert-links (converter links para funcionar offline)

# Espelhar um site (copia exata)
wget --mirror -p -k https://www.exemplo.com
# --mirror = -r -N -l inf (recursivo, com timestamps, sem limite de profundidade)

# Limitar a velocidade para nao sobrecarregar o servidor
wget --mirror --limit-rate=200k https://www.exemplo.com
```

### Opções Mais Usadas do wget

| Opcao | O que faz |
|-------|-----------|
| `-O arquivo` | Salvar com nome especificado |
| `-c` | Continuar download interrompido |
| `-q` | Modo silencioso |
| `-b` | Executar em background |
| `-r` | Download recursivo |
| `-l N` | Limitar profundidade recursiva a N níveis |
| `-A padrão` | Aceitar apenas arquivos que casam com o padrão |
| `-R padrão` | Rejeitar arquivos que casam com o padrão |
| `-i arquivo` | Ler URLs de um arquivo |
| `-p` | Baixar requisitos da página (CSS, imagens) |
| `-k` | Converter links para funcionar offline |
| `--mirror` | Espelhar site completo |
| `--limit-rate=N` | Limitar velocidade de download |
| `--no-check-certificate` | Ignorar erros de certificado SSL |
| `-t N` | Número de tentativas em caso de falha |
| `-w N` | Esperar N segundos entre downloads |

---

## curl vs wget: Quando Usar Cada Um

| Caracteristica | curl | wget |
|---------------|------|------|
| Foco principal | Transferencia de dados versatil | Download de arquivos |
| Métodos HTTP | Todos: GET, POST, PUT, DELETE, etc. | Principalmente GET |
| Enviar dados | Sim, com -d e -X | Limitado |
| Cabecalhos personalizados | Sim, com -H | Limitado |
| Testar APIs | Excelente | Não recomendado |
| Download recursivo | Não | Sim, nativo |
| Retomar downloads | Sim, com -C - | Sim, com -c |
| Download em background | Não nativo | Sim, com -b |
| Protocolos suportados | 25+ protocolos | HTTP, HTTPS, FTP |
| Saida padrão | stdout (tela) | Arquivo |
| Integra com pipes | Perfeitamente | Limitado |
| Instalado por padrão | Quase sempre | Quase sempre |

Regra prática:
- **Use curl** para: testar APIs, enviar dados, verificar cabeçalhos, integrar com pipes, scripts de monitoramento
- **Use wget** para: baixar arquivos, retomar downloads, baixar sites inteiros, downloads em lote

---

## Outras Ferramentas de Rede Essenciais

Além do curl e wget, existem outras ferramentas de rede que todo desenvolvedor deve conhecer. Não vamos nos aprofundar em cada uma, mas é importante saber que existem e o que fazem.

### ping — Verificando Conectividade

O `ping` envia pacotes para um servidor e mede o tempo de resposta. É a primeira ferramenta que você usa quando algo "não está funcionando":

```bash
# Verificar se um servidor esta acessivel
ping google.com

# Enviar apenas 4 pacotes (em vez de infinito)
ping -c 4 google.com

# Verificar conectividade na rede local
ping 192.168.1.1
```

Saída esperada:
```
PING google.com (142.250.79.46) 56(84) bytes of data.
64 bytes from 142.250.79.46: icmp_seq=1 ttl=118 time=12.3 ms
64 bytes from 142.250.79.46: icmp_seq=2 ttl=118 time=11.8 ms
64 bytes from 142.250.79.46: icmp_seq=3 ttl=118 time=12.1 ms
64 bytes from 142.250.79.46: icmp_seq=4 ttl=118 time=11.9 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 11.800/12.025/12.300/0.183 ms
```

O número `time=12.3 ms` é a **latência** — quanto tempo o pacote levou para ir e voltar. Valores abaixo de 50ms são bons para a maioria dos usos. Se o ping não responde, o servidor pode estar fora do ar ou bloqueando ping.

### traceroute — Rastreando o Caminho

O `traceroute` mostra o caminho que os pacotes percorrem do seu computador até o destino, passando por cada roteador intermediário:

```bash
# Rastrear o caminho ate um servidor
traceroute google.com

# Versao mais rapida (usa ICMP em vez de UDP)
traceroute -I google.com
```

Saída esperada (simplificada):
```
traceroute to google.com (142.250.79.46), 30 hops max
 1  gateway (192.168.1.1)  1.234 ms
 2  10.0.0.1  5.678 ms
 3  isp-router.net  12.345 ms
 4  backbone.net  15.678 ms
 5  google-edge.net  11.234 ms
 6  142.250.79.46  12.100 ms
```

Cada linha é um "salto" (hop) — um roteador pelo qual o pacote passou. Se um salto mostra tempos muito altos ou `* * *` (sem resposta), pode indicar onde está o problema de rede.

### dig e nslookup — Consultando DNS

O DNS (Domain Name System) traduz nomes como `google.com` para endereços IP como `142.250.79.46`. O `dig` e o `nslookup` permitem consultar o DNS:

```bash
# Consultar o IP de um dominio
dig google.com

# Versao simplificada
dig +short google.com
# Saida: 142.250.79.46

# Consultar com nslookup (mais simples)
nslookup google.com

# Consultar registros MX (email)
dig google.com MX +short
```

### ss e netstat — Conexões de Rede

O `ss` (socket statistics) mostra as conexões de rede ativas no sistema:

```bash
# Mostrar todas as conexoes TCP ativas
ss -t

# Mostrar portas em escuta (listening)
ss -tlnp
# -t = TCP
# -l = listening (em escuta)
# -n = numerico (mostra numeros em vez de nomes)
# -p = process (mostra qual processo esta usando)

# Verificar se a porta 8080 esta em uso
ss -tlnp | grep 8080
```

Saída esperada (ss -tlnp):
```
State   Recv-Q  Send-Q  Local Address:Port  Peer Address:Port  Process
LISTEN  0       128     *:22                *:*                users:(("sshd",pid=500,fd=3))
LISTEN  0       128     *:80                *:*                users:(("nginx",pid=1200,fd=6))
LISTEN  0       128     *:8080              *:*                users:(("python3",pid=1350,fd=4))
```

Isso mostra que o SSH está escutando na porta 22, o Nginx na porta 80 e um programa Python na porta 8080.

### host — Resolução de Nomes Simples

```bash
# Resolver um nome para IP
host google.com
# Saida: google.com has address 142.250.79.46

# Resolver um IP para nome (reverso)
host 142.250.79.46
# Saida: 46.79.250.142.in-addr.arpa domain name pointer ...
```

### Tabela de Referência de Ferramentas de Rede

| Comando | O que faz | Quando usar |
|---------|-----------|-------------|
| `curl` | Transferir dados via URL | Testar APIs, baixar dados, scripts |
| `wget` | Baixar arquivos | Downloads, espelhamento de sites |
| `ping` | Testar conectividade | Verificar se servidor esta acessível |
| `traceroute` | Rastrear caminho de rede | Diagnosticar problemas de rota |
| `dig` | Consultar DNS | Verificar resolução de nomes |
| `nslookup` | Consultar DNS (simples) | Verificacao rápida de DNS |
| `host` | Resolver nomes | Verificacao rápida de IP |
| `ss` | Conexões de rede | Ver portas em uso, conexões ativas |
| `ip addr` | Enderecos de rede | Ver IP do seu computador |
| `ifconfig` | Configuração de rede (antigo) | Ver IP, alternativa ao ip addr |

---

## Cenários Práticos

### Cenário 1: Testando uma API

Você está desenvolvendo uma API e quer testar se ela funciona:

```bash
# Verificar se o servidor esta respondendo
curl -s -o /dev/null -w "%{http_code}" http://localhost:8080/health
# Esperado: 200

# Listar todos os usuarios
curl -s http://localhost:8080/api/usuarios | jq .

# Criar um novo usuario
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ana", "email": "ana@exemplo.com"}' \
  http://localhost:8080/api/usuarios

# Atualizar um usuario
curl -X PUT \
  -H "Content-Type: application/json" \
  -d '{"nome": "Ana Silva"}' \
  http://localhost:8080/api/usuarios/1

# Deletar um usuario
curl -X DELETE http://localhost:8080/api/usuarios/1

# Verificar o codigo de resposta de cada operacao
curl -s -o /dev/null -w "%{http_code}\n" -X DELETE http://localhost:8080/api/usuarios/1
# Esperado: 204 (No Content) ou 200 (OK)
```

### Cenário 2: Monitoramento Simples

Um script que verifica se seus serviços estão no ar:

```bash
# Script simples de monitoramento
#!/bin/bash

# Lista de servicos para verificar
URLS="https://www.google.com https://api.github.com https://meu-site.com"

for url in $URLS; do
    # Pegar o codigo HTTP
    status=$(curl -s -o /dev/null -w "%{http_code}" --max-time 10 "$url")

    if [ "$status" = "200" ]; then
        echo "OK  [$status] $url"
    else
        echo "FALHA [$status] $url"
    fi
done
```

Saída esperada:
```
OK  [200] https://www.google.com
OK  [200] https://api.github.com
FALHA [000] https://meu-site.com
```

O código `000` significa que o curl não conseguiu conectar — o servidor pode estar fora do ar ou o domínio não existe.

### Cenário 3: Baixando Documentação para Leitura Offline

```bash
# Baixar a documentacao do Python para ler offline
wget -r -l 2 -p -k --limit-rate=500k \
  https://docs.python.org/pt-br/3/tutorial/

# Baixar todos os PDFs de uma pagina
wget -r -l 1 -A "*.pdf" -nd https://exemplo.com/documentos/
# -nd = no directories (salvar tudo no diretorio atual, sem criar subdiretorios)
```

### Cenário 4: Diagnosticando Problemas de Rede

Quando algo "não funciona", siga esta sequência:

```bash
# 1. Verificar se tem internet
ping -c 3 8.8.8.8
# 8.8.8.8 e o DNS do Google - se responde, voce tem internet

# 2. Verificar se o DNS funciona
dig google.com +short
# Se nao resolver, o problema e no DNS

# 3. Verificar se o servidor especifico responde
ping -c 3 api.exemplo.com

# 4. Verificar se a porta esta aberta
curl -v --connect-timeout 5 https://api.exemplo.com
# Se "Connection refused", a porta esta fechada
# Se "Connection timed out", firewall pode estar bloqueando

# 5. Rastrear o caminho
traceroute api.exemplo.com
# Identificar onde o pacote para

# 6. Verificar cabecalhos da resposta
curl -I https://api.exemplo.com
# Ver codigo de status e cabecalhos
```

---

## JSON: O Formato de Dados da Web

Quando você usa curl para acessar APIs, a maioria das respostas vem em formato **JSON** (JavaScript Object Notation — Notação de Objetos JavaScript). JSON é o formato padrão para troca de dados na web moderna.

### Estrutura do JSON

```json
{
  "nome": "Ana Silva",
  "idade": 25,
  "ativo": true,
  "email": null,
  "linguagens": ["Python", "JavaScript", "Go"],
  "endereco": {
    "cidade": "Sao Paulo",
    "estado": "SP"
  }
}
```

JSON tem apenas alguns tipos de dados:
- **String**: texto entre aspas duplas — `"Ana Silva"`
- **Number**: números — `25`, `3.14`
- **Boolean**: verdadeiro ou falso — `true`, `false`
- **Null**: valor vazio — `null`
- **Array**: lista ordenada entre colchetes — `["Python", "JavaScript"]`
- **Object**: conjunto de pares chave-valor entre chaves — `{"nome": "Ana"}`

### jq: Processando JSON no Terminal

O `jq` é uma ferramenta para processar JSON no terminal — como o `grep` e `awk` são para texto, o `jq` é para JSON:

```bash
# Instalar o jq
sudo apt install jq

# Formatar JSON de forma legivel (pretty print)
curl -s https://api.github.com/users/torvalds | jq .

# Extrair um campo especifico
curl -s https://api.github.com/users/torvalds | jq '.name'
# Saida: "Linus Torvalds"

# Extrair varios campos
curl -s https://api.github.com/users/torvalds | jq '{nome: .name, bio: .bio, repos: .public_repos}'

# Extrair elementos de um array
curl -s https://api.github.com/users/torvalds/repos | jq '.[0].name'
# Saida: nome do primeiro repositorio

# Filtrar array
curl -s https://api.github.com/users/torvalds/repos | jq '.[] | select(.language == "C") | .name'

# Contar elementos
curl -s https://api.github.com/users/torvalds/repos | jq 'length'
```

O `jq` é extremamente útil quando você trabalha com APIs. No Capítulo 10, quando construirmos nossa própria API, vamos usar `curl | jq` constantemente para testar e inspecionar as respostas.

---

## Conexão com a Programação

As ferramentas de rede deste módulo são a ponte entre o terminal e o mundo da programação web:

**APIs são o futuro**: a maioria dos sistemas modernos se comunica através de APIs REST — exatamente o que testamos com curl. No Capítulo 10, você vai construir sua própria API com Python e FastAPI. O curl será sua ferramenta de teste principal. Saber usar curl agora significa que você já vai chegar no Capítulo 10 sabendo testar o que construiu.

**HTTP é universal**: os métodos HTTP (GET, POST, PUT, DELETE) e os códigos de status (200, 404, 500) são a linguagem universal da web. Todo framework web em qualquer linguagem — Python, JavaScript, Go, Java, C# — usa esses mesmos conceitos. Aprender HTTP agora é um investimento que vale para toda a carreira.

**JSON é a língua franca dos dados**: quando programas se comunicam pela rede, quase sempre usam JSON. No Capítulo 5, vamos aprender a trabalhar com JSON em Python. No Capítulo 7, vamos armazenar dados em bancos de dados. No Capítulo 10, vamos enviar e receber JSON via API. O formato que você viu neste módulo vai aparecer em praticamente todo capítulo daqui para frente.

**Automação e scripts**: os exemplos de monitoramento que vimos (verificar se um serviço está no ar, medir tempo de resposta) são a base de scripts de automação reais. Empresas usam scripts similares para monitorar centenas de serviços 24 horas por dia. No Capítulo 2, aprendemos shell scripting básico — agora você tem as ferramentas de rede para criar scripts que interagem com o mundo exterior.

**Debugging de rede**: quando seu programa não consegue se conectar a um serviço, as ferramentas deste módulo (ping, traceroute, dig, curl -v) são as primeiras que você usa para diagnosticar. Saber ler a saída do `curl -v` e entender códigos HTTP é uma habilidade de debugging essencial.

---

## Como a IA pode te ajudar aqui
**Prompt 1 — Explorar o conceito:**
> "Preciso testar uma API REST que requer autenticação OAuth2 com token Bearer. O endpoint é POST /api/v2/pedidos e preciso enviar um JSON com campos 'produto', 'quantidade' e 'preco'. Monte o comando curl completo e explique cada parte."

**Prompt 2 — Entender erros comuns:**
> "Estou recebendo erro 403 Forbidden quando acesso uma API com curl, mas funciona no navegador. O que pode estar causando isso e como resolvo?"

**Prompt 3 — Aprofundar o tema:**
> "Quero criar um script bash que monitore 5 URLs a cada 5 minutos e me avise se alguma retornar código diferente de 200. Me ajude a montar o script usando curl."

---

## Resumo do Módulo

| Conceito | Definição |
|----------|-----------|
| URL | Endereco completo de um recurso na internet |
| HTTP | Protocolo de comunicação da web, baseado em requisicao-resposta |
| Método HTTP | Tipo de ação: GET busca, POST cria, PUT atualiza, DELETE remove |
| Código de status | Número que indica o resultado: 200 sucesso, 404 não encontrado, 500 erro |
| Cabecalho HTTP | Metadados da requisicao ou resposta: tipo de conteúdo, autenticação, etc. |
| curl | Ferramenta versatil para transferir dados via URL |
| wget | Ferramenta especializada em downloads de arquivos |
| JSON | Formato padrão para troca de dados na web |
| API | Interface de comunicação entre programas |
| DNS | Sistema que traduz nomes de dominio para enderecos IP |
| Porta | Número que identifica qual servico em um servidor |
| Latencia | Tempo que um pacote leva para ir e voltar na rede |
| Redirecionamento | Quando um servidor manda o cliente buscar em outra URL |
| jq | Ferramenta para processar e filtrar dados JSON no terminal |

---

## Glossário do Módulo

| Termo | Definição |
|-------|-----------|
| API | Application Programming Interface, interface de comunicação entre programas |
| Bearer token | Token de autenticação enviado no cabecalho Authorization |
| Content-Type | Cabecalho HTTP que indica o formato dos dados: JSON, HTML, etc. |
| CORS | Cross-Origin Resource Sharing, politica de segurança do navegador |
| curl | Client URL, ferramenta de linha de comando para transferir dados via URL |
| DELETE | Método HTTP para remover um recurso |
| dig | Domain Information Groper, ferramenta para consultar DNS |
| DNS | Domain Name System, sistema que traduz nomes para enderecos IP |
| FTP | File Transfer Protocol, protocolo para transferencia de arquivos |
| GET | Método HTTP para buscar dados |
| Header | Cabecalho, metadados enviados junto com requisicoes e respostas HTTP |
| HTTP | HyperText Transfer Protocol, protocolo de comunicação da web |
| HTTPS | HTTP Secure, versão criptografada do HTTP |
| IP | Internet Protocol, protocolo que define enderecos de rede |
| jq | Ferramenta de linha de comando para processar dados JSON |
| JSON | JavaScript Object Notation, formato de dados baseado em texto |
| Latencia | Tempo de ida e volta de um pacote na rede, medido em milissegundos |
| PATCH | Método HTTP para atualizar parcialmente um recurso |
| ping | Ferramenta que testa conectividade enviando pacotes ICMP |
| Porta | Número de 0 a 65535 que identifica um servico em um computador |
| POST | Método HTTP para criar um novo recurso |
| PUT | Método HTTP para atualizar um recurso existente |
| REST | Representational State Transfer, estilo de arquitetura para APIs web |
| ss | Socket Statistics, ferramenta que mostra conexões de rede |
| SSL | Secure Sockets Layer, protocolo de criptografia para comunicação segura |
| Status code | Código de status HTTP, número que indica o resultado da requisicao |
| TLS | Transport Layer Security, versão moderna do SSL |
| traceroute | Ferramenta que mostra o caminho dos pacotes na rede |
| URL | Uniform Resource Locator, endereco completo de um recurso na internet |
| User-Agent | Cabecalho HTTP que identifica o cliente que faz a requisicao |
| wget | Web Get, ferramenta de linha de comando especializada em downloads |

---

## Na Cultura Popular

- **Mr. Robot** (série, 2015-2019) — o protagonista usa curl e wget em vários episódios para baixar dados de servidores, testar vulnerabilidades em APIs e automatizar ataques. A série mostra de forma realista como ferramentas de rede de linha de comando são usadas tanto para fins legítimos quanto para hacking.

- **O Quinto Poder** (filme, 2013) — conta a história do WikiLeaks e de Julian Assange. O filme mostra como dados eram transferidos pela internet entre servidores ao redor do mundo, usando protocolos e ferramentas de rede. Embora não mostre curl especificamente, ilustra a importância de entender como dados trafegam pela rede.

- **The Social Network** (filme, 2010) — nas cenas iniciais, Mark Zuckerberg usa scripts para baixar fotos de sites de faculdades automaticamente (web scraping). Embora o filme não mostre os comandos exatos, a técnica é essencialmente o que wget faz com download recursivo.

---

## Para Saber Mais

- *Everything curl — Daniel Stenberg* — https://everything.curl.dev — *livro gratuito e completo escrito pelo criador do curl, cobre tudo sobre a ferramenta*
- *curl Cookbook* — https://catonmat.net/cookbooks/curl — *receitas práticas de curl para situações comuns*
- *jq Manual* — https://stedolan.github.io/jq/manual/ — *documentação oficial do jq com exemplos*
- *Repositório do Fino — learn-ops-content* — https://github.com/RafaelFino/learn-ops-content — *material complementar sobre ferramentas de rede e Linux*
- *HTTP Status Codes — httpstatuses.com* — https://httpstatuses.com — *referência completa de todos os códigos de status HTTP com explicações*

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre curl e wget?**
R: O curl é versátil — faz requisições com qualquer método HTTP, envia dados, manipula cabeçalhos e integra com pipes. O wget é especialista em downloads — retoma downloads interrompidos, baixa sites inteiros e funciona em background. Use curl para testar APIs e interagir com serviços. Use wget para baixar arquivos.

**P: O que significa o código 200?**
R: O código HTTP 200 significa "OK" — a requisição foi bem-sucedida e o servidor retornou os dados solicitados. É o código mais comum e indica que tudo funcionou como esperado.

**P: O que significa o código 404?**
R: O código 404 significa "Not Found" — o recurso solicitado não existe no servidor. Pode ser uma URL digitada errado, uma página que foi removida ou um endpoint de API que não existe. É o erro mais famoso da internet.

**P: O que é uma API REST?**
R: REST (Representational State Transfer) é um estilo de arquitetura para APIs web. Uma API REST usa métodos HTTP (GET, POST, PUT, DELETE) para operar sobre recursos identificados por URLs. Por exemplo, `GET /usuarios` lista usuários, `POST /usuarios` cria um novo, `DELETE /usuarios/42` remove o usuário 42. Vamos aprofundar isso no Capítulo 10.

**P: O que é JSON e por que é tão usado?**
R: JSON (JavaScript Object Notation) é um formato de texto para representar dados estruturados. É usado porque é legível por humanos, fácil de processar por programas, leve (pouco overhead) e suportado por praticamente toda linguagem de programação. Quando dois sistemas precisam trocar dados, JSON é quase sempre a escolha.

**P: Preciso instalar o jq?**
R: O jq não vem instalado por padrão, mas é altamente recomendado se você trabalha com APIs. Sem jq, a saída JSON do curl é uma linha longa e ilegível. Com jq, fica formatada e você pode extrair campos específicos. Instale com `sudo apt install jq`.

**P: O curl funciona com HTTPS?**
R: Sim, o curl suporta HTTPS nativamente. Ele verifica o certificado SSL do servidor por padrão. Se o certificado for inválido (comum em ambientes de desenvolvimento), você pode usar `-k` para ignorar a verificação — mas nunca faça isso em produção.

**P: Como sei qual método HTTP usar?**
R: A convenção REST é: GET para buscar dados, POST para criar novos dados, PUT para atualizar dados existentes (substituição completa), PATCH para atualizar parcialmente e DELETE para remover. A documentação da API que você está usando deve especificar qual método cada endpoint espera.

**P: O que é o User-Agent e por que alguns sites bloqueiam o curl?**
R: O User-Agent é um cabeçalho que identifica quem está fazendo a requisição. O curl se identifica como "curl/versão". Alguns sites bloqueiam requisições que não parecem vir de um navegador real, como proteção contra bots. Você pode contornar isso com `-H "User-Agent: Mozilla/5.0"`, mas respeite os termos de uso do site.

**P: Posso usar curl em scripts bash?**
R: Sim, e é um dos usos mais comuns. Scripts de monitoramento, testes automatizados de API, integração contínua — todos usam curl extensivamente. A opção `-s` (silent) é essencial em scripts para suprimir a barra de progresso, e `-w` permite extrair informações específicas como código de status e tempo de resposta.

**P: O que acontece se a internet cair no meio de um download com wget?**
R: O wget salva o que já foi baixado. Quando a internet voltar, execute o mesmo comando com `-c` (continue) e ele retoma de onde parou. Isso é uma das maiores vantagens do wget sobre o curl para downloads grandes.

**P: Como faço para ver o que o curl está enviando e recebendo?**
R: Use a opção `-v` (verbose). Ela mostra tudo: a resolução DNS, a conexão TCP, a negociação TLS, os cabeçalhos enviados (marcados com `>`), os cabeçalhos recebidos (marcados com `<`) e o corpo da resposta. É a ferramenta de debugging mais importante do curl.

---

## Exercícios Práticos

### Exercício 1 — Explorando com curl

1. Use `curl` para acessar `https://www.example.com` e observe o HTML retornado
2. Use `curl -I` para ver apenas os cabeçalhos da resposta. Anote o código de status e o Content-Type
3. Use `curl -s -o /dev/null -w "%{http_code}"` para verificar o código de status de 3 sites diferentes (google.com, github.com, e um site que não existe)
4. Use `curl -v https://www.example.com` e identifique na saída: a resolução DNS, a conexão TCP, os cabeçalhos enviados e os cabeçalhos recebidos
5. Acesse a API pública do GitHub: `curl -s https://api.github.com | head -20` e observe o formato JSON da resposta

### Exercício 2 — Trabalhando com APIs

1. Acesse a API do GitHub para ver informações de um usuário:
   ```bash
   curl -s https://api.github.com/users/torvalds
   ```
2. Se tiver o `jq` instalado (`sudo apt install jq`), extraia apenas o nome e a bio:
   ```bash
   curl -s https://api.github.com/users/torvalds | jq '{nome: .name, bio: .bio}'
   ```
3. Liste os repositórios públicos do mesmo usuário:
   ```bash
   curl -s https://api.github.com/users/torvalds/repos | jq '.[].name'
   ```
4. Meça o tempo de resposta da API:
   ```bash
   curl -s -o /dev/null -w "Tempo: %{time_total}s\n" https://api.github.com
   ```

### Exercício 3 — Downloads com wget

1. Baixe a página principal do example.com:
   ```bash
   wget https://www.example.com
   ```
2. Observe o arquivo criado (`index.html`) e veja seu conteúdo com `cat`
3. Baixe o mesmo arquivo com um nome personalizado:
   ```bash
   wget -O exemplo.html https://www.example.com
   ```
4. Crie um arquivo `urls.txt` com 3 URLs (uma por linha) e baixe todas de uma vez:
   ```bash
   wget -i urls.txt
   ```
5. Tente baixar uma URL que não existe e observe a mensagem de erro e o código de status

---

[← Anterior: Editores de Texto no Terminal: vim e micro](cap03-mod05-editores-terminal.md) · [Próximo: O que é Controle de Versão e por que Importa →](cap04-mod01-controle-versao.md)
