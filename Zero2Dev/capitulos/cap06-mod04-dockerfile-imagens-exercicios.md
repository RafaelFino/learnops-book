# Exercícios — Módulo 6.4: Dockerfile e Imagens

[← Voltar ao Módulo 6.4](cap06-mod04-dockerfile-imagens-conteudo.md)

> **Como usar estes exercícios:**
> 1. Leia o enunciado com atenção
> 2. Leia as dicas antes de começar
> 3. Tente resolver sozinho
> 4. Use a Proposta de Teste para verificar se sua solução funciona
> 5. Só depois consulte a Resposta Comentada

> **Como testar cada exercício:**
> 1. Crie uma pasta separada para cada exercício
> 2. Crie os arquivos Python e o Dockerfile conforme o enunciado
> 3. Construa a imagem com `docker build -t nome .`
> 4. Rode o container com `docker run --rm nome`
> 5. Compare a saída com a Proposta de Teste

---

## Exercício 1 — Hello World em Container — Nível: Básico

### Enunciado

Crie um programa Python que imprima "Meu primeiro container!" e a data/hora atual. Empacote em uma imagem Docker e rode.

### Dicas
- Use `from datetime import datetime` para obter a data
- Use `python:3.12-slim` como imagem base
- Não esqueça do `WORKDIR`
- Use `--rm` ao rodar para limpar automaticamente

### Proposta de Teste
- **Caso básico:** a saída mostra "Meu primeiro container!" seguido da data/hora
- **Caso de verificação:** rodar `docker images` mostra a imagem criada

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `hello.py`:
```python
# hello.py - Primeiro programa em container
from datetime import datetime

# "message" = mensagem
message = "Meu primeiro container!"
print(message)
print(f"Data e hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
```

Arquivo `Dockerfile`:
```dockerfile
# Imagem base Python slim
FROM python:3.12-slim
# Diretorio de trabalho
WORKDIR /app
# Copiar o script
COPY hello.py .
# Comando de execucao
CMD ["python3", "hello.py"]
```

Comandos:
```bash
# Construir a imagem com nome "hello"
docker build -t hello .

# Rodar o container (--rm remove ao terminar)
docker run --rm hello
# Saida: Meu primeiro container!
#        Data e hora: 27/04/2026 10:30:00
```

---

## Exercício 2 — Calculadora em Container — Nível: Básico

### Enunciado

Crie um programa Python que funcione como uma calculadora simples. O programa deve:
1. Pedir dois números ao usuário
2. Pedir a operação (+, -, *, /)
3. Mostrar o resultado

Empacote em uma imagem Docker e rode em modo interativo.

### Dicas
- Use `input()` para pedir dados ao usuário
- Rode com `docker run -it --rm` para modo interativo
- Lembre-se do tratamento de divisão por zero
- Use `float()` para converter os números

### Proposta de Teste
- **Caso básico:** entrada 10, 5, + → saída "Resultado: 15.0"
- **Caso de borda:** entrada 10, 0, / → mensagem de erro (não pode dividir por zero)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `calc.py`:
```python
# calc.py - Calculadora simples em container
# "number" = numero, "operation" = operacao, "result" = resultado

print("=== CALCULADORA ===")
# Pedir os numeros ao usuario
num1 = float(input("Primeiro numero: "))  # primeiro numero
num2 = float(input("Segundo numero: "))   # segundo numero
op = input("Operacao (+, -, *, /): ")     # operacao

# Calcular o resultado
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Erro: nao pode dividir por zero!")
        exit()
    result = num1 / num2
else:
    print(f"Operacao '{op}' nao reconhecida!")
    exit()

print(f"Resultado: {num1} {op} {num2} = {result}")
```

Arquivo `Dockerfile`:
```dockerfile
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY calc.py .
CMD ["python3", "calc.py"]
```

Comandos:
```bash
# Construir
docker build -t calc .

# Rodar em modo interativo (necessario por causa do input)
# -it = interativo + terminal
docker run -it --rm calc
```

---

## Exercício 3 — Containerizar Programa do Capítulo 5 — Nível: Intermediário

### Enunciado

Pegue um dos programas que você criou no capítulo 5 (pode ser um exercício ou o projeto do gerenciador de contatos) e containerize-o:

1. Crie um Dockerfile para o programa
2. Crie um `.dockerignore` adequado
3. Construa a imagem
4. Rode o container
5. Compare o tamanho da imagem usando `python:3.12` vs `python:3.12-slim`

### Dicas
- Se o programa usa `input()`, rode com `-it`
- Crie o `.dockerignore` para excluir `__pycache__`, `.git`, `venv`
- Use `ENV PYTHONUNBUFFERED=1` para que `print()` funcione corretamente
- Se o programa tem múltiplos arquivos, use `COPY . .` (com `.dockerignore`)

### Proposta de Teste
- **Caso básico:** o programa funciona dentro do container exatamente como fora dele
- **Caso de verificação:** a imagem slim é significativamente menor que a imagem full

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `.dockerignore`:
```
__pycache__/
*.pyc
.git/
.gitignore
venv/
.venv/
.vscode/
*.swp
Dockerfile
.dockerignore
README.md
```

Arquivo `Dockerfile`:
```dockerfile
# Imagem base slim
FROM python:3.12-slim

# Saida sem buffer
ENV PYTHONUNBUFFERED=1

# Diretorio de trabalho
WORKDIR /app

# Copiar todos os arquivos Python
COPY . .

# Comando de execucao (ajuste o nome do arquivo)
CMD ["python3", "gerenciador.py"]
```

Comandos:
```bash
# Construir com imagem slim
docker build -t meu-programa-slim .

# Construir com imagem full (para comparar)
# Crie um Dockerfile.full com FROM python:3.12
docker build -t meu-programa-full -f Dockerfile.full .

# Comparar tamanhos
docker images | grep meu-programa
# meu-programa-slim ~140 MB
# meu-programa-full ~920 MB

# Rodar (com -it se usa input)
docker run -it --rm meu-programa-slim
```

---

## Exercício 4 — Otimização de Cache — Nível: Intermediário

### Enunciado

Crie um programa Python que use a biblioteca `requests` (ou qualquer outra do pip). Crie dois Dockerfiles diferentes:

1. `Dockerfile.ruim` — copia tudo antes de instalar dependências
2. `Dockerfile.bom` — copia requirements.txt primeiro, instala, depois copia o código

Construa ambos, modifique o código Python (sem mudar requirements.txt) e reconstrua. Compare o tempo de rebuild.

### Dicas
- Crie um `requirements.txt` com pelo menos uma dependência
- Use `time docker build` para medir o tempo
- Na segunda build, mude apenas o arquivo `.py`
- Observe as mensagens "CACHED" na saída do build

### Proposta de Teste
- **Caso básico:** ambos os Dockerfiles produzem imagens funcionais
- **Caso de verificação:** o rebuild do `Dockerfile.bom` é significativamente mais rápido

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `requirements.txt`:
```
requests==2.31.0
```

Arquivo `app.py`:
```python
# app.py - Programa que usa biblioteca externa
import requests
print("Biblioteca requests importada com sucesso!")
print(f"Versao do requests: {requests.__version__}")
```

Arquivo `Dockerfile.ruim`:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
# RUIM: copia tudo antes de instalar dependencias
# Qualquer mudanca no codigo invalida o cache do pip install
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "app.py"]
```

Arquivo `Dockerfile.bom`:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
# BOM: copia requirements primeiro
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Depois copia o codigo
COPY . .
CMD ["python3", "app.py"]
```

Comandos:
```bash
# Primeira build de ambos
docker build -t app-ruim -f Dockerfile.ruim .
docker build -t app-bom -f Dockerfile.bom .

# Modificar o codigo (sem mudar requirements.txt)
echo '# comentario novo' >> app.py

# Rebuild - observe a diferenca
docker build -t app-ruim -f Dockerfile.ruim .
# pip install roda de novo (sem cache)

docker build -t app-bom -f Dockerfile.bom .
# pip install usa CACHED (muito mais rapido!)
```

---

## Exercício 5 — Gerador de Senhas em Container — Nível: Avançado

### Enunciado

Crie um programa Python que gere senhas aleatórias. O programa deve:
1. Aceitar o tamanho da senha como argumento de linha de comando
2. Gerar uma senha com letras, números e caracteres especiais
3. Imprimir a senha gerada

Containerize o programa e rode passando o argumento via `docker run`.

### Dicas
- Use `sys.argv` para receber argumentos de linha de comando
- Use o módulo `random` e `string` para gerar senhas
- Argumentos passados após o nome da imagem no `docker run` substituem o CMD
- Exemplo: `docker run --rm gerador 16` passa "16" como argumento

### Proposta de Teste
- **Caso básico:** `docker run --rm gerador 12` gera uma senha de 12 caracteres
- **Caso de borda:** `docker run --rm gerador` (sem argumento) usa tamanho padrão (ex: 8)

### Resposta Comentada

> **Importante:** Tente resolver sozinho primeiro!

Arquivo `gerador.py`:
```python
# gerador.py - Gerador de senhas aleatorias
import random
import string
import sys

def gerar_senha(tamanho=8):
    """Gera uma senha aleatoria com letras, numeros e simbolos"""
    # "characters" = caracteres disponiveis
    characters = string.ascii_letters + string.digits + "!@#$%&*"
    # "password" = senha
    password = ''.join(random.choice(characters) for _ in range(tamanho))
    return password

# Verificar se o usuario passou o tamanho como argumento
if len(sys.argv) > 1:
    try:
        tamanho = int(sys.argv[1])  # converter argumento para numero
    except ValueError:
        print(f"Erro: '{sys.argv[1]}' nao e um numero valido")
        sys.exit(1)
else:
    tamanho = 8  # tamanho padrao

# Gerar e mostrar a senha
senha = gerar_senha(tamanho)
print(f"Senha gerada ({tamanho} caracteres): {senha}")
```

Arquivo `Dockerfile`:
```dockerfile
FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY gerador.py .
# ENTRYPOINT define o comando fixo
# Argumentos do docker run sao passados como parametros
ENTRYPOINT ["python3", "gerador.py"]
```

Comandos:
```bash
# Construir
docker build -t gerador .

# Rodar com tamanho padrao (8)
docker run --rm gerador
# Saida: Senha gerada (8 caracteres): aB3$kL9!

# Rodar com tamanho especifico
docker run --rm gerador 16
# Saida: Senha gerada (16 caracteres): xY7@mN2$pQ4&wR8!

# Rodar com tamanho grande
docker run --rm gerador 32
# Saida: Senha gerada (32 caracteres): ...
```

---

[← Voltar ao Módulo 6.4](cap06-mod04-dockerfile-imagens-conteudo.md)
