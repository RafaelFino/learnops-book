# 6.5 — Docker Compose: Orquestrando Múltiplos Containers

[← Anterior: Dockerfile e Imagens](cap06-mod04-dockerfile-imagens-conteudo.md) · [Próximo: Projeto do Capítulo 6 →](../projects/projeto-cap06-docker.md)

---

## Introdução

No módulo anterior, você aprendeu a criar Dockerfiles e construir imagens para suas aplicações Python. Agora consegue empacotar qualquer programa em um container que roda em qualquer lugar.

Mas aplicações reais raramente funcionam sozinhas. Um sistema típico precisa de:
- Uma **aplicação** (seu código Python)
- Um **banco de dados** (PostgreSQL, MySQL, SQLite)
- Talvez um **cache** (Redis)
- Talvez um **servidor web** (nginx)

No módulo 6.3, você rodou um container PostgreSQL com `docker run`. Funciona, mas imagine ter que digitar comandos separados para cada serviço, lembrar as portas, variáveis de ambiente, nomes e dependências entre eles. Com 3-4 serviços, já fica confuso. Com 10, é inviável.

**Docker Compose** resolve esse problema. É uma ferramenta que permite definir e rodar **múltiplos containers** com um único arquivo de configuração. Em vez de vários comandos `docker run`, você escreve um arquivo `docker-compose.yml` que descreve todos os serviços, e sobe tudo com um único comando: `docker compose up`.

Neste módulo, vamos aprender a usar Docker Compose para orquestrar ambientes com múltiplos containers — a habilidade que vai transformar seu fluxo de desenvolvimento.

---

## Como Executar os Exemplos Deste Módulo

Para acompanhar este módulo:

1. Docker instalado e funcionando (módulo 6.3)
2. Docker Compose instalado (vem junto com Docker Desktop no macOS; no Linux, foi instalado como plugin no módulo 6.3)
3. Editor de texto e terminal abertos

Verifique que o Docker Compose está disponível:

```bash
# Verificar versao do Docker Compose
docker compose version
```

**Saída esperada**:
```
Docker Compose version v2.27.0
```

Se o comando não funcionar, tente `docker-compose version` (com hífen — versão antiga). Se nenhum funcionar, reinstale o Docker seguindo as instruções do módulo 6.3.

---

## O Problema: Múltiplos Containers Manualmente

Vamos ver o problema que Docker Compose resolve. Imagine que você tem uma aplicação Python que precisa de um banco de dados PostgreSQL. Sem Compose, você faria:

```bash
# Passo 1: Criar uma rede para os containers se comunicarem
docker network create minha-rede

# Passo 2: Rodar o banco de dados
docker run -d \
  --name meu-banco \
  --network minha-rede \
  -e POSTGRES_USER=aluno \
  -e POSTGRES_PASSWORD=senha123 \
  -e POSTGRES_DB=meu_app \
  -p 5432:5432 \
  -v dados-banco:/var/lib/postgresql/data \
  postgres:16

# Passo 3: Rodar a aplicacao
docker run -d \
  --name minha-app \
  --network minha-rede \
  -e DATABASE_URL=postgresql://aluno:senha123@meu-banco:5432/meu_app \
  -p 8000:8000 \
  minha-imagem-python
```

São 3 comandos longos, com muitas flags, que precisam ser executados na ordem certa. Se você errar uma variável de ambiente, um nome de rede ou uma porta, nada funciona. E para parar tudo:

```bash
docker stop minha-app meu-banco
docker rm minha-app meu-banco
docker network rm minha-rede
```

Agora imagine fazer isso toda vez que quiser trabalhar no projeto. Toda manhã, digitar esses comandos. Toda noite, parar tudo. E se um colega novo entrar na equipe, explicar cada flag de cada comando.

---

## A Solução: docker-compose.yml

Com Docker Compose, tudo isso vira um único arquivo:

```yaml
# docker-compose.yml - Define todos os servicos do projeto
services:
  # Servico 1: Banco de dados PostgreSQL
  banco:
    image: postgres:16
    environment:
      POSTGRES_USER: aluno
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: meu_app
    ports:
      - "5432:5432"
    volumes:
      - dados-banco:/var/lib/postgresql/data

  # Servico 2: Aplicacao Python
  app:
    build: .
    environment:
      DATABASE_URL: postgresql://aluno:senha123@banco:5432/meu_app
    ports:
      - "8000:8000"
    depends_on:
      - banco

# Volumes persistentes
volumes:
  dados-banco:
```

E para subir tudo:

```bash
# Subir todos os servicos
docker compose up -d
```

Um comando. Tudo sobe. A rede é criada automaticamente. As dependências são respeitadas (o banco sobe antes da app). As variáveis de ambiente estão documentadas no arquivo.

Para parar tudo:

```bash
# Parar e remover todos os servicos
docker compose down
```

A diferença é brutal. O `docker-compose.yml` serve como **documentação viva** do ambiente — qualquer pessoa que ler o arquivo sabe exatamente quais serviços o projeto precisa e como eles se conectam.

---

## Anatomia do docker-compose.yml

Vamos entender cada parte do arquivo:

### Estrutura Básica

```yaml
# Versao do formato (opcional em versoes recentes)
# services: define os containers que serao criados
services:
  nome-do-servico:
    # configuracoes do servico
    image: imagem:tag
    # ou
    build: ./caminho

# volumes: define volumes persistentes
volumes:
  nome-do-volume:

# networks: define redes customizadas (opcional)
networks:
  nome-da-rede:
```

### Propriedades de um Serviço

| Propriedade | O que faz | Exemplo |
|-------------|-----------|---------|
| `image` | Usa uma imagem pronta do Docker Hub | `image: postgres:16` |
| `build` | Constrói imagem a partir de um Dockerfile | `build: .` |
| `ports` | Mapeia portas host:container | `ports: ["8080:80"]` |
| `environment` | Define variáveis de ambiente | `environment: {VAR: valor}` |
| `volumes` | Monta volumes para persistência | `volumes: ["dados:/app/data"]` |
| `depends_on` | Define ordem de inicialização | `depends_on: [banco]` |
| `command` | Sobrescreve o CMD do Dockerfile | `command: python3 app.py` |
| `restart` | Política de reinício | `restart: unless-stopped` |

---

## Exemplo Prático 1: App Python + PostgreSQL

Vamos criar um exemplo completo e funcional.

### Estrutura do Projeto

```bash
mkdir -p ~/meus-projetos/docker-compose-exemplo
cd ~/meus-projetos/docker-compose-exemplo
```

### O Programa Python

Crie o arquivo `app.py`:

```python
# app.py - Aplicacao que se conecta ao PostgreSQL via container
import os
import time

def main():
    """Programa principal que demonstra conexao com banco"""
    # "database_url" = endereco do banco de dados
    database_url = os.getenv("DATABASE_URL", "nao definido")
    # "app_name" = nome da aplicacao
    app_name = os.getenv("APP_NAME", "Minha App")

    print("=" * 50)
    print(f"  {app_name}")
    print("=" * 50)
    print(f"  Database URL: {database_url}")
    print(f"  Status: Rodando em container Docker")
    print("=" * 50)
    print()

    # Simular uma aplicacao que roda continuamente
    # "counter" = contador
    counter = 0
    while True:
        counter += 1
        print(f"[{app_name}] Heartbeat #{counter} - Aplicacao ativa")
        time.sleep(5)  # esperar 5 segundos

if __name__ == "__main__":
    main()
```

### O Dockerfile

Crie o `Dockerfile`:

```dockerfile
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py .
CMD ["python3", "app.py"]
```

### O docker-compose.yml

Crie o `docker-compose.yml`:

```yaml
services:
  # Banco de dados PostgreSQL
  banco:
    image: postgres:16
    environment:
      POSTGRES_USER: aluno
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: curso_docker
    ports:
      - "5432:5432"
    volumes:
      - dados-postgres:/var/lib/postgresql/data

  # Aplicacao Python
  app:
    build: .
    environment:
      DATABASE_URL: postgresql://aluno:senha123@banco:5432/curso_docker
      APP_NAME: Docker Compose Demo
    depends_on:
      - banco

volumes:
  dados-postgres:
```

### Subindo o Ambiente

```bash
# Subir todos os servicos em background
docker compose up -d
```

**Saída esperada**:
```
[+] Building 5.2s (7/7) FINISHED
...
[+] Running 3/3
 ✔ Network docker-compose-exemplo_default  Created
 ✔ Container docker-compose-exemplo-banco-1  Started
 ✔ Container docker-compose-exemplo-app-1    Started
```

Repare que o Docker Compose:
1. Criou uma rede automaticamente
2. Construiu a imagem da app (porque usamos `build: .`)
3. Baixou a imagem do PostgreSQL
4. Iniciou o banco primeiro (por causa do `depends_on`)
5. Iniciou a app depois

### Verificando os Serviços

```bash
# Ver os servicos rodando
docker compose ps
```

**Saída esperada**:
```
NAME                                 IMAGE                COMMAND                  STATUS
docker-compose-exemplo-app-1         docker-compose-...   "python3 app.py"         Up 30 seconds
docker-compose-exemplo-banco-1       postgres:16          "docker-entrypoint.s…"   Up 31 seconds
```

```bash
# Ver os logs da aplicacao
docker compose logs app
```

**Saída esperada**:
```
app-1  | ==================================================
app-1  |   Docker Compose Demo
app-1  | ==================================================
app-1  |   Database URL: postgresql://aluno:senha123@banco:5432/curso_docker
app-1  |   Status: Rodando em container Docker
app-1  | ==================================================
app-1  |
app-1  | [Docker Compose Demo] Heartbeat #1 - Aplicacao ativa
app-1  | [Docker Compose Demo] Heartbeat #2 - Aplicacao ativa
```

### Parando o Ambiente

```bash
# Parar todos os servicos
docker compose down
```

**Saída esperada**:
```
[+] Running 3/3
 ✔ Container docker-compose-exemplo-app-1    Removed
 ✔ Container docker-compose-exemplo-banco-1  Removed
 ✔ Network docker-compose-exemplo_default    Removed
```

---

## Volumes: Persistindo Dados

No exemplo anterior, usamos um volume chamado `dados-postgres`. Vamos entender por que isso é importante.

### O Problema: Dados Efêmeros

Por padrão, tudo que está dentro de um container é **efêmero** — quando o container é removido, os dados são perdidos. Se o PostgreSQL guarda dados dentro do container e você roda `docker compose down`, os dados somem.

### A Solução: Volumes

Volumes são "pastas compartilhadas" entre o container e o host. Os dados ficam no volume, que persiste mesmo quando o container é removido.

```yaml
services:
  banco:
    image: postgres:16
    volumes:
      # Volume nomeado: Docker gerencia onde os dados ficam
      - dados-postgres:/var/lib/postgresql/data

volumes:
  dados-postgres:  # Declarar o volume
```

Existem dois tipos de volumes:

### 1. Volumes Nomeados (Recomendado para Dados)

```yaml
volumes:
  - dados-postgres:/var/lib/postgresql/data
```

O Docker gerência onde os dados ficam no disco. Você não precisa se preocupar com o caminho. Os dados persistem entre `docker compose down` e `docker compose up`.

### 2. Bind Mounts (Recomendado para Código em Desenvolvimento)

```yaml
volumes:
  - ./meu-codigo:/app
```

Monta uma pasta do seu computador dentro do container. Mudanças no seu computador aparecem instantaneamente no container e vice-versa. Perfeito para desenvolvimento — você edita o código no VSCode e o container vê as mudanças em tempo real.

### Exemplo: Desenvolvimento com Hot Reload

```yaml
services:
  app:
    build: .
    volumes:
      # Montar o codigo local dentro do container
      # Mudancas no codigo aparecem instantaneamente
      - ./:/app
    ports:
      - "8000:8000"
```

Com esse bind mount, você edita `app.py` no VSCode e o container vê a mudança imediatamente. Não precisa reconstruir a imagem a cada alteração.

### Verificando Volumes

```bash
# Listar volumes
docker volume ls

# Inspecionar um volume (ver onde os dados ficam)
docker volume inspect dados-postgres

# Remover volumes nao utilizados
docker volume prune
```

### Cuidado com docker compose down -v

```bash
# Parar servicos (volumes PRESERVADOS)
docker compose down

# Parar servicos E REMOVER volumes (dados PERDIDOS!)
docker compose down -v
```

A flag `-v` remove os volumes junto com os containers. Use com cuidado — se o volume tem dados do banco, eles serão perdidos permanentemente.

### Testando a Persistência

Vamos verificar que os dados realmente persistem:

```bash
# Subir o ambiente
docker compose up -d

# Conectar ao banco e criar uma tabela
docker compose exec banco psql -U aluno -d curso_docker -c "CREATE TABLE teste (id SERIAL, nome TEXT);"
docker compose exec banco psql -U aluno -d curso_docker -c "INSERT INTO teste (nome) VALUES ('Docker Compose');"

# Verificar que os dados existem
docker compose exec banco psql -U aluno -d curso_docker -c "SELECT * FROM teste;"
# Deve mostrar: 1 | Docker Compose

# Parar tudo (sem -v, volumes preservados)
docker compose down

# Subir novamente
docker compose up -d

# Verificar que os dados ainda existem!
docker compose exec banco psql -U aluno -d curso_docker -c "SELECT * FROM teste;"
# Ainda mostra: 1 | Docker Compose

# Limpar
docker compose down
```

Os dados sobreviveram ao `down` e `up` porque estão no volume, não no container. Essa é a magia dos volumes.

---

## Comunicação entre Containers

Uma das funcionalidades mais poderosas do Docker Compose é a **comunicação automática entre containers**. Quando você define serviços no `docker-compose.yml`, eles podem se comunicar usando o **nome do serviço** como hostname.

### Como Funciona

No nosso exemplo, a app se conecta ao banco usando `banco` como hostname:

```yaml
app:
  environment:
    DATABASE_URL: postgresql://aluno:senha123@banco:5432/curso_docker
    #                                        ^^^^^ nome do servico
```

O Docker Compose cria uma rede interna e configura DNS automaticamente. Quando a app tenta acessar `banco`, o Docker resolve para o IP do container do PostgreSQL.

```mermaid
flowchart LR
    APP[Container App - Python] -->|banco:5432| DB[Container Banco - PostgreSQL]
    APP -->|Rede interna Docker| DB
```

Você não precisa saber o IP do container — use sempre o nome do serviço. O IP pode mudar a cada restart, mas o nome é fixo.

### Portas Internas vs Externas

Uma distinção importante:

- **Portas internas** (entre containers): os containers se comunicam pelas portas internas, sem precisar de mapeamento. A app acessa o banco na porta 5432 diretamente.

- **Portas externas** (host → container): o mapeamento `ports: ["5432:5432"]` permite que VOCÊ acesse o banco do seu computador. Se não precisar acessar de fora, pode omitir o `ports`.

```yaml
services:
  banco:
    image: postgres:16
    # ports: ["5432:5432"]  # Descomente se quiser acessar do host
    # Mesmo sem ports, a app consegue acessar na porta 5432 internamente
```

---

## Comandos Essenciais do Docker Compose

| Comando | O que faz |
|---------|-----------|
| `docker compose up` | Sobe todos os serviços (foreground) |
| `docker compose up -d` | Sobe todos os serviços em background |
| `docker compose up --build` | Reconstrói imagens antes de subir |
| `docker compose down` | Para e remove containers e redes |
| `docker compose down -v` | Para, remove containers, redes E volumes |
| `docker compose ps` | Lista serviços rodando |
| `docker compose logs` | Mostra logs de todos os serviços |
| `docker compose logs app` | Mostra logs de um serviço específico |
| `docker compose logs -f` | Mostra logs em tempo real (follow) |
| `docker compose exec app bash` | Abre shell em um serviço rodando |
| `docker compose stop` | Para serviços sem remover |
| `docker compose start` | Inicia serviços parados |
| `docker compose restart` | Reinicia serviços |
| `docker compose build` | Reconstrói imagens sem subir |

O comando mais usado no dia a dia é `docker compose up -d` (subir) e `docker compose down` (parar).

---

## Exemplo Prático 2: App Python + Redis

Vamos criar outro exemplo com um serviço diferente — Redis, um banco de dados em memória muito usado como cache.

Crie uma nova pasta:

```bash
mkdir -p ~/meus-projetos/docker-compose-redis
cd ~/meus-projetos/docker-compose-redis
```

Crie `app.py`:

```python
# app.py - Aplicacao que demonstra uso de cache com Redis
import time
import os
import json

def main():
    """Demonstra conceito de cache usando arquivo como simulacao"""
    # Em uma aplicacao real, usariamos a biblioteca redis
    # Aqui simulamos o conceito para nao precisar de dependencias externas
    
    print("=" * 50)
    print("  APP COM CACHE - Docker Compose Demo")
    print("=" * 50)
    
    # "redis_host" = endereco do Redis
    redis_host = os.getenv("REDIS_HOST", "redis")
    redis_port = os.getenv("REDIS_PORT", "6379")
    print(f"  Redis configurado em: {redis_host}:{redis_port}")
    print()
    
    # Simular operacoes de cache
    # "cache" = armazenamento temporario
    cache = {}
    
    # Simular requisicoes
    for i in range(1, 6):
        # "key" = chave, "value" = valor
        key = f"usuario_{i}"
        value = f"Dados do usuario {i}"
        cache[key] = value
        print(f"  [CACHE SET] {key} = {value}")
        time.sleep(1)
    
    print()
    print("  Cache preenchido! Consultando...")
    print()
    
    for key, value in cache.items():
        print(f"  [CACHE GET] {key} -> {value}")
    
    print()
    print("  Aplicacao finalizada com sucesso!")

if __name__ == "__main__":
    main()
```

Crie `Dockerfile`:

```dockerfile
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py .
CMD ["python3", "app.py"]
```

Crie `docker-compose.yml`:

```yaml
services:
  # Cache Redis
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  # Aplicacao Python
  app:
    build: .
    environment:
      REDIS_HOST: redis
      REDIS_PORT: "6379"
    depends_on:
      - redis

```

```bash
# Subir o ambiente
docker compose up --build

# A app roda, mostra as operacoes de cache e encerra
# O Redis continua rodando em background
```

---

## Boas Práticas com Docker Compose

### 1. Sempre Use Versões Específicas de Imagens

```yaml
# BOM: versao especifica
image: postgres:16

# RUIM: latest pode mudar e quebrar seu ambiente
image: postgres:latest
```

### 2. Defina Variáveis Sensíveis em Arquivo .env

Em vez de colocar senhas diretamente no `docker-compose.yml`, use um arquivo `.env`:

Crie `.env`:
```
POSTGRES_PASSWORD=senha_secreta_123
POSTGRES_USER=aluno
```

No `docker-compose.yml`:
```yaml
services:
  banco:
    image: postgres:16
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
```

O Docker Compose lê automaticamente o arquivo `.env` da mesma pasta. Adicione `.env` ao `.gitignore` para não versionar senhas.

### 3. Use depends_on com Consciência

`depends_on` controla a ordem de inicialização, mas não garante que o serviço está pronto. Para bancos de dados, sua aplicação deve ter lógica de retry.

### 4. Nomeie seus Containers

```yaml
services:
  banco:
    image: postgres:16
    container_name: meu-projeto-banco
```

Facilita identificar containers quando você tem múltiplos projetos rodando.

---

## Casos de Uso no Mundo Real

### 1. Ambiente de Desenvolvimento Local

O caso de uso mais comum de Docker Compose para desenvolvedores. Em vez de instalar PostgreSQL, Redis, Elasticsearch e outros serviços no seu computador (poluindo o sistema e causando conflitos de versão), você define tudo no `docker-compose.yml`.

Quando começa a trabalhar: `docker compose up -d`. Quando termina: `docker compose down`. Seu computador fica limpo, e o ambiente é idêntico para toda a equipe.

### 2. Testes de Integração

Antes de fazer deploy, é importante testar se todos os serviços funcionam juntos. Docker Compose permite subir o ambiente completo (app + banco + cache + filas) em segundos, rodar os testes e derrubar tudo.

Pipelines de CI/CD usam Docker Compose exatamente para isso: criam o ambiente, rodam os testes, destroem o ambiente. Tudo automatizado.

### 3. Demonstrações e Protótipos

Quer mostrar seu projeto para alguém? Em vez de pedir para a pessoa instalar Python, PostgreSQL, Redis e configurar tudo, mande o `docker-compose.yml`. A pessoa roda `docker compose up` e tem o projeto inteiro funcionando.

---

## Como a IA pode te ajudar aqui
**Prompt 1 — Criar com ajuda da IA:**
> "Escreva um docker-compose.yml para uma aplicação Python com PostgreSQL e Redis"

**Prompt 2 — Aprofundar o tema:**
> "Meus containers não conseguem se comunicar. O que pode estar errado?"

**Prompt 3 — Entender o porquê:**
> "Como faço para que meu container Python reinicie automaticamente quando eu mudo o código?"

---

## Resumo do Módulo

| Conceito | Definição |
|----------|-----------|
| Docker Compose | Ferramenta para definir e rodar aplicações multi-container |
| docker-compose.yml | Arquivo YAML que descreve os serviços, redes e volumes |
| Serviço | Um container definido no docker-compose.yml |
| `docker compose up` | Comando que cria e inicia todos os serviços |
| `docker compose down` | Comando que para e remove todos os serviços |
| Volume nomeado | Volume gerenciado pelo Docker para persistir dados |
| Bind mount | Montagem de pasta do host dentro do container |
| depends_on | Define ordem de inicialização entre serviços |
| Rede interna | Rede criada automaticamente pelo Compose para comunicação entre containers |
| DNS interno | Resolução de nomes que permite usar o nome do serviço como hostname |

---

## Glossário do Módulo

| Termo | Definição |
|-------|-----------|
| Bind mount | Montagem de um diretório do host dentro do container, refletindo mudanças em tempo real |
| Cache | Armazenamento temporário de dados para acesso rápido |
| depends_on | Propriedade do Compose que define dependências entre serviços |
| DNS (Domain Name System) | Sistema que traduz nomes em endereços IP; Docker Compose configura DNS interno automaticamente |
| docker-compose.yml | Arquivo de configuração YAML que define serviços, redes e volumes |
| Docker Compose | Ferramenta do ecossistema Docker para orquestrar múltiplos containers |
| Efêmero | Temporário, que não persiste; dados dentro de containers são efêmeros por padrão |
| Foreground | Modo de execução que ocupa o terminal e mostra logs em tempo real |
| Hot reload | Técnica onde mudanças no código são refletidas automaticamente sem reiniciar |
| Hostname | Nome que identifica um computador ou container na rede |
| Orquestração | Gerenciamento coordenado de múltiplos containers |
| Persistência | Capacidade de manter dados mesmo após o container ser removido |
| Redis | Banco de dados em memória, muito usado como cache e fila de mensagens |
| Serviço | No contexto do Compose, um container definido no docker-compose.yml |
| Volume | Mecanismo do Docker para persistir dados fora do ciclo de vida do container |
| Volume nomeado | Volume gerenciado pelo Docker, identificado por nome |
| YAML | Formato de arquivo de configuração legível por humanos, usado pelo Docker Compose |

---

## Na Cultura Popular

- **Silicon Valley** (série, 2014-2019) — Em vários episódios, os personagens precisam escalar rapidamente sua infraestrutura. Docker Compose é a ferramenta que permite definir ambientes complexos de forma simples — exatamente o tipo de problema que startups enfrentam.

- **Mr. Robot** (série, 2015-2019) — A série mostra ambientes de servidores complexos com múltiplos serviços interconectados. Docker Compose é como esses ambientes são gerenciados no mundo real — cada serviço em seu container, todos orquestrados por um arquivo de configuração.

---

## Para Saber Mais

- [Docker Compose Documentation](https://docs.docker.com/compose/) — *Documentação oficial completa do Docker Compose*

- [Awesome Compose — GitHub](https://github.com/docker/awesome-compose) — *Repositório oficial com dezenas de exemplos de docker-compose.yml para diferentes stacks*

- [Play with Docker](https://labs.play-with-docker.com/) — *Ambiente no navegador para praticar Docker Compose sem instalar nada*

- [LINUXtips — Docker Compose](https://www.youtube.com/@LINUXtips) — *Episódios dedicados ao Docker Compose na série Descomplicando Docker*

- [Docker Compose File Reference](https://docs.docker.com/compose/compose-file/) — *Referência completa de todas as propriedades do docker-compose.yml*

---

## Perguntas Frequentes (FAQ)

**P: Qual a diferença entre `docker compose` e `docker-compose`?**
R: `docker compose` (sem hífen) é a versão nova (V2), integrada ao Docker CLI como plugin. `docker-compose` (com hífen) é a versão antiga (V1), um binário separado. Use `docker compose` — é mais rápido e é o padrão atual.

**P: O `depends_on` garante que o banco está pronto antes da app iniciar?**
R: Não completamente. `depends_on` garante que o container do banco INICIA antes da app, mas não que o banco está PRONTO para aceitar conexões. O PostgreSQL pode levar alguns segundos para inicializar. Em aplicações reais, a app deve ter lógica de retry (tentar conectar várias vezes).

**P: Posso usar Docker Compose em produção?**
R: Para projetos pequenos, sim. Para projetos grandes com alta disponibilidade, Kubernetes é mais adequado. Docker Compose é perfeito para desenvolvimento local e projetos de pequeno/médio porte.

**P: Como faço para ver os logs de um serviço específico?**
R: `docker compose logs nome-do-servico`. Adicione `-f` para seguir em tempo real: `docker compose logs -f app`.

**P: Posso rodar apenas um serviço do Compose?**
R: Sim. `docker compose up -d banco` sobe apenas o serviço `banco` (e suas dependências). Útil quando você quer rodar a app localmente mas precisa do banco em container.

**P: O que acontece com meus dados quando rodo `docker compose down`?**
R: Containers e redes são removidos, mas volumes nomeados são preservados. Seus dados no banco continuam lá. Se usar `docker compose down -v`, os volumes também são removidos e os dados são perdidos.

**P: Posso ter múltiplos arquivos docker-compose.yml?**
R: Sim. Use `-f` para especificar: `docker compose -f docker-compose.dev.yml up`. É comum ter um arquivo para desenvolvimento e outro para produção.

**P: Como atualizo um serviço sem derrubar os outros?**
R: `docker compose up -d --build app` reconstrói e reinicia apenas o serviço `app`, sem afetar o banco ou outros serviços.

**P: Docker Compose cria uma rede automaticamente?**
R: Sim. O Compose cria uma rede padrão chamada `{nome-da-pasta}_default`. Todos os serviços são conectados a essa rede e podem se comunicar pelo nome do serviço.

**P: Posso usar Docker Compose com imagens que não têm Dockerfile?**
R: Sim. Use `image:` em vez de `build:`. Exemplo: `image: postgres:16` usa a imagem pronta do Docker Hub sem precisar de Dockerfile.

---

## Exercícios de Fixação

Os exercícios deste módulo estão em um arquivo separado para facilitar a consulta:

**[Acessar Exercícios do Módulo 6.5](cap06-mod05-docker-compose-exercicios.md)**

---

[← Anterior: Dockerfile e Imagens](cap06-mod04-dockerfile-imagens-conteudo.md) · [Próximo: Projeto do Capítulo 6 →](../projects/projeto-cap06-docker.md)
