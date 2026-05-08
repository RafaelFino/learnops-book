# Exercícios — Módulo 6.3: Docker na Prática

[← Voltar ao Módulo 6.3](cap06-mod03-docker-basico-conteudo.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. Só depois consulte a Resposta Comentada

> **Como testar cada exercício:**
> 1. Abra o terminal (`Ctrl + Alt + T`)
> 2. Execute os comandos Docker conforme o enunciado
> 3. Compare a saída com a Proposta de Teste
> 4. Limpe os containers e imagens ao final de cada exercício

---

## Exercício 1 — Explorando Imagens — Nível: Básico

### Enunciado

Baixe a imagem `alpine:latest` (Alpine Linux, uma distribuição minúscula) e responda:

1. Qual o tamanho da imagem Alpine?
2. Abra um shell interativo dentro de um container Alpine
3. Dentro do container, execute `cat /etc/os-release` para ver informações do sistema
4. Compare o tamanho da imagem Alpine com a imagem Ubuntu 22.04

### Dicas
- Use `docker pull` para baixar imagens
- Use `docker images` para ver tamanhos
- Alpine usa `sh` em vez de `bash` como shell padrão
- Use `docker run -it alpine sh` para abrir o shell

### Proposta de Teste
- **Caso básico:** `docker images` mostra Alpine com ~7 MB e Ubuntu com ~77 MB
- **Caso de verificação:** dentro do container Alpine, `cat /etc/os-release` mostra "Alpine Linux"

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro! Use a resposta apenas como referência de aprendizado.

```bash
# Baixar a imagem Alpine
docker pull alpine:latest

# Baixar a imagem Ubuntu para comparacao
docker pull ubuntu:22.04

# Ver o tamanho das imagens
# Alpine tem ~7 MB, Ubuntu tem ~77 MB
# Alpine e cerca de 10x menor!
docker images

# Abrir shell interativo no Alpine
# Alpine usa "sh" porque nao vem com bash instalado
docker run -it --rm alpine sh

# Dentro do container Alpine:
# Ver informacoes do sistema operacional
cat /etc/os-release
# Saida: NAME="Alpine Linux", VERSION_ID=3.19...

# Sair do container
exit
```

---

## Exercício 2 — Container Python com Script — Nível: Básico

### Enunciado

Rode um container Python que execute o seguinte cálculo e imprima o resultado:
- Calcule a soma dos números de 1 a 100
- Imprima o resultado

Use `docker run` com a flag `-c` do Python para executar código inline (sem criar arquivo).

### Dicas
- O Python aceita código inline com `python3 -c "codigo_aqui"`
- Use `--rm` para que o container se auto-destrua
- A função `sum()` e `range()` do Python podem ajudar
- Lembre-se de usar aspas corretamente (aspas duplas fora, aspas simples dentro, ou vice-versa)

### Proposta de Teste
- **Caso básico:** a saída deve ser `5050` (soma de 1 a 100)
- **Caso de verificação:** o container não deve aparecer em `docker ps -a` (por causa do `--rm`)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```bash
# Rodar Python dentro de um container descartavel
# --rm = remove o container automaticamente ao terminar
# python3 -c = executa codigo Python inline
docker run --rm python:3.12-slim python3 -c "print(sum(range(1, 101)))"
# Saida esperada: 5050

# Verificar que o container foi removido automaticamente
docker ps -a
# O container nao aparece na lista
```

---

## Exercício 3 — Servidor Web com Nome e Porta — Nível: Básico

### Enunciado

1. Rode um container nginx em background com o nome `meu-site` na porta 9090
2. Verifique que está rodando com `docker ps`
3. Acesse `http://localhost:9090` no navegador (ou use `curl`)
4. Veja os logs do container
5. Pare e remova o container

### Dicas
- Use `-d` para background, `--name` para nomear, `-p` para porta
- O nginx escuta na porta 80 dentro do container
- Use `curl http://localhost:9090` se não tiver navegador disponível
- Lembre de parar antes de remover

### Proposta de Teste
- **Caso básico:** `docker ps` mostra o container `meu-site` rodando com porta `0.0.0.0:9090->80/tcp`
- **Caso de verificação:** `curl http://localhost:9090` retorna HTML com "Welcome to nginx!"

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```bash
# Rodar nginx em background com nome e porta customizados
# -d = background
# --name meu-site = nome do container
# -p 9090:80 = porta 9090 do host -> porta 80 do container
docker run -d --name meu-site -p 9090:80 nginx

# Verificar que esta rodando
docker ps
# Deve mostrar meu-site com STATUS "Up" e PORTS "0.0.0.0:9090->80/tcp"

# Acessar o servidor web via terminal
# curl faz uma requisicao HTTP e mostra a resposta
curl http://localhost:9090
# Saida: HTML com "Welcome to nginx!"

# Ver os logs do container
# Mostra as requisicoes HTTP que o nginx recebeu
docker logs meu-site

# Parar o container
docker stop meu-site

# Remover o container
docker rm meu-site
```

---

## Exercício 4 — Banco de Dados em Container — Nível: Intermediário

### Enunciado

1. Rode um container PostgreSQL com as seguintes configurações:
   - Nome: `banco-teste`
   - Usuário: `estudante`
   - Senha: `python123`
   - Banco de dados: `meu_curso`
   - Porta: 5432
2. Verifique que está rodando
3. Conecte-se ao banco usando `docker exec` e o cliente `psql`
4. Dentro do psql, liste os bancos de dados existentes
5. Saia do psql e pare/remova o container

### Dicas
- As variáveis de ambiente do PostgreSQL são: `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
- Para conectar ao psql dentro do container: `docker exec -it banco-teste psql -U estudante -d meu_curso`
- Dentro do psql, use `\l` para listar bancos e `\q` para sair
- Use `-e` para cada variável de ambiente

### Proposta de Teste
- **Caso básico:** `docker ps` mostra `banco-teste` rodando com porta 5432
- **Caso de verificação:** dentro do psql, `\l` mostra o banco `meu_curso` na lista

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```bash
# Rodar PostgreSQL com configuracoes via variaveis de ambiente
# -d = background
# --name = nome do container
# -e = variaveis de ambiente para configurar o banco
# -p = mapeamento de porta
docker run -d \
  --name banco-teste \
  -e POSTGRES_USER=estudante \
  -e POSTGRES_PASSWORD=python123 \
  -e POSTGRES_DB=meu_curso \
  -p 5432:5432 \
  postgres:16

# Aguardar alguns segundos para o banco inicializar
# PostgreSQL precisa de tempo para criar o banco na primeira vez
sleep 5

# Verificar que esta rodando
docker ps
# Deve mostrar banco-teste com STATUS "Up"

# Conectar ao banco via psql dentro do container
# -U estudante = usuario
# -d meu_curso = banco de dados
docker exec -it banco-teste psql -U estudante -d meu_curso

# Dentro do psql:
# Listar todos os bancos de dados
# \l
# Deve mostrar meu_curso na lista

# Sair do psql
# \q

# Parar e remover o container
docker stop banco-teste
docker rm banco-teste
```

---

## Exercício 5 — Investigando um Container — Nível: Intermediário

### Enunciado

1. Rode um container Ubuntu 22.04 em modo interativo
2. Dentro do container, descubra:
   - Qual o sistema operacional? (`cat /etc/os-release`)
   - Qual o hostname do container? (`hostname`)
   - Qual o IP do container? (`hostname -I`)
   - Quantos processos estão rodando? (`ps aux`)
   - Quanto de memória está disponível? (`free -h`)
3. Compare: quantos processos rodam no container vs no seu computador host?

### Dicas
- Use `docker run -it ubuntu:22.04 bash`
- Alguns comandos podem não estar disponíveis no container mínimo — isso é normal
- Se `ps` não estiver disponível, instale com `apt update && apt install -y procps`
- Use `--rm` para limpar automaticamente

### Proposta de Teste
- **Caso básico:** o container mostra Ubuntu 22.04 como SO e tem muito menos processos que o host
- **Caso de verificação:** o hostname do container é diferente do hostname do seu computador (é o ID do container)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```bash
# Rodar Ubuntu interativo e descartavel
docker run -it --rm ubuntu:22.04 bash

# Dentro do container:

# Ver o sistema operacional
cat /etc/os-release
# Mostra: PRETTY_NAME="Ubuntu 22.04.4 LTS"

# Ver o hostname (e o ID curto do container)
hostname
# Mostra algo como: a1b2c3d4e5f6

# Ver o IP do container
hostname -I
# Mostra algo como: 172.17.0.2

# Instalar ferramentas que nao vem no Ubuntu minimo
apt update && apt install -y procps
# Isso instala o comando "ps"

# Ver processos rodando
ps aux
# Mostra apenas 2-3 processos (bash e ps)
# Compare com seu host que tem 100+ processos!

# Ver memoria disponivel
free -h
# Mostra a memoria total do host (containers compartilham a RAM)

# Sair do container
exit
# Container e removido automaticamente por causa do --rm
```

---

## Exercício 6 — Limpeza Geral — Nível: Avançado

### Enunciado

Após fazer todos os exercícios anteriores, seu sistema pode ter containers parados e imagens acumuladas. Faça uma limpeza completa:

1. Liste todos os containers (rodando e parados)
2. Pare todos os containers que estiverem rodando
3. Remova todos os containers parados
4. Liste todas as imagens
5. Remova as imagens que você não vai mais usar
6. Verifique quanto espaço foi liberado

### Dicas
- `docker ps -a` lista todos os containers
- `docker container prune` remove todos os containers parados
- `docker image prune` remove imagens não utilizadas
- `docker system prune` faz uma limpeza geral (containers, imagens, redes)
- `docker system df` mostra quanto espaço Docker está usando

### Proposta de Teste
- **Caso básico:** após a limpeza, `docker ps -a` mostra lista vazia
- **Caso de verificação:** `docker system df` mostra espaço reclaimável reduzido

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

```bash
# Listar todos os containers (rodando e parados)
docker ps -a

# Parar todos os containers que estiverem rodando
# $(docker ps -q) retorna os IDs de todos os containers rodando
docker stop $(docker ps -q) 2>/dev/null

# Remover todos os containers parados
docker container prune -f
# -f = force (nao pede confirmacao)

# Ver quanto espaco Docker esta usando
docker system df
# Mostra: Images, Containers, Local Volumes, Build Cache

# Listar imagens restantes
docker images

# Remover imagens especificas que nao precisa mais
docker rmi alpine:latest ubuntu:22.04 nginx:latest 2>/dev/null

# Ou fazer limpeza geral (remove tudo que nao esta em uso)
docker system prune -f
# Remove: containers parados, redes nao usadas, imagens sem container

# Verificar o resultado
docker system df
# Espaco usado deve ter diminuido significativamente

# Verificar que tudo esta limpo
docker ps -a
# Lista vazia
docker images
# Apenas imagens que voce decidiu manter
```

---

[← Voltar ao Módulo 6.3](cap06-mod03-docker-basico-conteudo.md)
