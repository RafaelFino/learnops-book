# Exercícios — Módulo 6.5: Docker Compose

[← Voltar ao Módulo 6.5](cap06-mod05-docker-compose-conteudo.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. Só depois consulte a Resposta Comentada

> **Como testar cada exercício:**
> 1. Crie uma pasta separada para cada exercício
> 2. Crie os arquivos conforme o enunciado
> 3. Suba o ambiente com `docker compose up -d`
> 4. Verifique com `docker compose ps` e `docker compose logs`
> 5. Limpe com `docker compose down` ao final

---

## Exercício 1 — Dois Serviços Simples — Nível: Básico

### Enunciado

Crie um `docker-compose.yml` que suba dois serviços:
1. Um container nginx servindo a página padrão na porta 8080
2. Um container Redis na porta 6379

Verifique que ambos estão rodando e acesse o nginx pelo navegador.

### Dicas
- Use `image:` para ambos (não precisa de Dockerfile)
- nginx usa porta 80 internamente
- Redis usa porta 6379 internamente
- Use `docker compose ps` para verificar

### Proposta de Teste
- **Caso básico:** `docker compose ps` mostra 2 serviços rodando
- **Caso de verificação:** `curl http://localhost:8080` retorna HTML do nginx

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `docker-compose.yml`:
```yaml
# docker-compose.yml - Dois servicos simples
services:
  # Servidor web nginx
  web:
    image: nginx:latest
    ports:
      - "8080:80"  # porta 8080 do host -> porta 80 do container

  # Cache Redis
  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"  # porta 6379 do host -> porta 6379 do container
```

Comandos:
```bash
# Subir os servicos
docker compose up -d

# Verificar que estao rodando
docker compose ps
# Deve mostrar 2 servicos com STATUS "Up"

# Testar o nginx
curl http://localhost:8080
# Retorna HTML com "Welcome to nginx!"

# Ver logs
docker compose logs

# Limpar
docker compose down
```

---

## Exercício 2 — App Python com Variáveis de Ambiente — Nível: Básico

### Enunciado

Crie uma aplicação Python que leia configurações de variáveis de ambiente e as imprima. Use Docker Compose para definir as variáveis.

O programa deve ler e imprimir:
- `APP_NAME` (nome da aplicação)
- `APP_VERSION` (versão)
- `APP_ENV` (ambiente: development, production)
- `APP_DEBUG` (true/false)

### Dicas
- Use `os.getenv("NOME", "valor_padrao")` para ler variáveis
- Defina as variáveis na seção `environment` do Compose
- Use `build: .` para construir a imagem a partir do Dockerfile

### Proposta de Teste
- **Caso básico:** a saída mostra todas as variáveis com os valores definidos no Compose
- **Caso de verificação:** mudar um valor no Compose e reconstruir mostra o novo valor

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `config.py`:
```python
# config.py - Le configuracoes de variaveis de ambiente
import os

# "app_name" = nome da aplicacao
app_name = os.getenv("APP_NAME", "App Sem Nome")
# "app_version" = versao da aplicacao
app_version = os.getenv("APP_VERSION", "0.0.0")
# "app_env" = ambiente (development, production)
app_env = os.getenv("APP_ENV", "development")
# "app_debug" = modo debug ativado ou nao
app_debug = os.getenv("APP_DEBUG", "false")

print("=== CONFIGURACAO DA APLICACAO ===")
print(f"  Nome:    {app_name}")
print(f"  Versao:  {app_version}")
print(f"  Ambiente: {app_env}")
print(f"  Debug:   {app_debug}")
print("================================")
```

Arquivo `Dockerfile`:
```dockerfile
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY config.py .
CMD ["python3", "config.py"]
```

Arquivo `docker-compose.yml`:
```yaml
services:
  app:
    build: .
    environment:
      APP_NAME: Minha Aplicacao Docker
      APP_VERSION: "1.0.0"
      APP_ENV: development
      APP_DEBUG: "true"
```

Comandos:
```bash
docker compose up --build
# Mostra as configuracoes lidas das variaveis de ambiente
docker compose down
```

---

## Exercício 3 — Persistência com Volumes — Nível: Intermediário

### Enunciado

Crie um `docker-compose.yml` com PostgreSQL que:
1. Use um volume nomeado para persistir dados
2. Crie uma tabela e insira dados
3. Pare e remova os containers (`docker compose down`)
4. Suba novamente e verifique que os dados ainda existem

### Dicas
- O PostgreSQL guarda dados em `/var/lib/postgresql/data`
- Use `docker compose exec` para rodar comandos SQL
- Use `psql -U usuario -d banco -c "SQL"` para executar SQL
- NÃO use `-v` no `docker compose down` (isso remove volumes)

### Proposta de Teste
- **Caso básico:** dados inseridos antes do `down` existem após o `up`
- **Caso de verificação:** `docker compose down -v` seguido de `up` mostra tabela inexistente

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `docker-compose.yml`:
```yaml
services:
  banco:
    image: postgres:16
    environment:
      POSTGRES_USER: aluno
      POSTGRES_PASSWORD: teste123
      POSTGRES_DB: exercicio
    ports:
      - "5432:5432"
    volumes:
      - dados-exercicio:/var/lib/postgresql/data

volumes:
  dados-exercicio:
```

Comandos:
```bash
# Subir o banco
docker compose up -d

# Aguardar inicializacao
sleep 5

# Criar tabela e inserir dados
docker compose exec banco psql -U aluno -d exercicio -c \
  "CREATE TABLE alunos (id SERIAL, nome TEXT, nota REAL);"

docker compose exec banco psql -U aluno -d exercicio -c \
  "INSERT INTO alunos (nome, nota) VALUES ('Maria', 9.5), ('Joao', 8.0);"

# Verificar dados
docker compose exec banco psql -U aluno -d exercicio -c \
  "SELECT * FROM alunos;"
# Mostra: Maria 9.5, Joao 8.0

# Parar (sem -v = volumes preservados)
docker compose down

# Subir novamente
docker compose up -d
sleep 3

# Dados ainda existem!
docker compose exec banco psql -U aluno -d exercicio -c \
  "SELECT * FROM alunos;"
# Ainda mostra: Maria 9.5, Joao 8.0

# Limpar tudo (com -v = volumes removidos)
docker compose down -v
```

---

## Exercício 4 — Múltiplos Serviços com Dependências — Nível: Avançado

### Enunciado

Crie um ambiente com 3 serviços:
1. PostgreSQL (banco de dados)
2. Redis (cache)
3. Uma aplicação Python que imprime as configurações de conexão com ambos

A aplicação deve depender do banco e do Redis (usar `depends_on`).

### Dicas
- Defina variáveis de ambiente na app para os endereços do banco e Redis
- Use os nomes dos serviços como hostnames
- A app deve imprimir as URLs de conexão para verificar que está configurada corretamente

### Proposta de Teste
- **Caso básico:** `docker compose ps` mostra 3 serviços rodando
- **Caso de verificação:** logs da app mostram URLs corretas para banco e Redis

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `app.py`:
```python
# app.py - App com multiplas dependencias
import os

print("=== AMBIENTE MULTI-SERVICO ===")
print()
# "db_url" = endereco do banco de dados
db_url = os.getenv("DATABASE_URL", "nao configurado")
print(f"  Banco de dados: {db_url}")
# "redis_url" = endereco do Redis
redis_url = os.getenv("REDIS_URL", "nao configurado")
print(f"  Redis: {redis_url}")
print()
print("  Todos os servicos configurados!")
print("================================")
```

Arquivo `Dockerfile`:
```dockerfile
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app.py .
CMD ["python3", "app.py"]
```

Arquivo `docker-compose.yml`:
```yaml
services:
  banco:
    image: postgres:16
    environment:
      POSTGRES_USER: aluno
      POSTGRES_PASSWORD: senha123
      POSTGRES_DB: multi_servico

  cache:
    image: redis:7-alpine

  app:
    build: .
    environment:
      DATABASE_URL: postgresql://aluno:senha123@banco:5432/multi_servico
      REDIS_URL: redis://cache:6379
    depends_on:
      - banco
      - cache
```

Comandos:
```bash
docker compose up --build
# Mostra as URLs de conexao configuradas
docker compose down
```

---

[← Voltar ao Módulo 6.5](cap06-mod05-docker-compose-conteudo.md)
