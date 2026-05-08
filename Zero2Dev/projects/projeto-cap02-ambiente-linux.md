# Projeto do Capítulo 2 — Configurando seu Ambiente Linux

[← Voltar ao Capítulo 2](../capitulos/cap02-mod08-shell-scripting.md)

---

## Visão Geral

Neste projeto, você vai colocar a mão na massa e configurar um ambiente Linux completo. Até agora você aprendeu o que é Linux, como ele funciona, quais são as distribuições e como o sistema é organizado. Agora é hora de transformar esse conhecimento em prática.

Configurar um ambiente de desenvolvimento é uma das primeiras coisas que todo profissional de tecnologia faz ao começar em um novo emprego ou projeto. Saber fazer isso com confiança é uma habilidade que você vai usar durante toda a sua carreira.

---

## Objetivo

Instalar e configurar um ambiente Linux funcional, personalizado e pronto para desenvolvimento, documentando cada passo do processo.

---

## O que Você Vai Aprender

- Como instalar Linux (em máquina virtual ou dual boot)
- Como navegar pela estrutura de diretórios
- Como configurar permissões e usuários
- Como instalar pacotes e ferramentas essenciais
- Como personalizar o terminal
- Como documentar um processo técnico

---

## Pré-requisitos

- Ter lido todos os módulos do capítulo 2 (2.1 a 2.8)
- Ter um computador com pelo menos 4GB de RAM e 20GB de espaço livre
- Conexão com a internet para baixar a distribuição

---

## Instruções Passo a Passo

### Etapa 1 — Escolher a Distribuição

Baseado no que aprendeu no módulo 2.2, escolha uma distribuição Linux. Para iniciantes, recomendamos:

| Distribuição | Por que escolher | Dificuldade |
|-------------|-----------------|-------------|
| Ubuntu | Mais popular, maior comunidade, mais tutoriais | Fácil |
| Linux Mint | Baseado no Ubuntu, interface familiar para quem vem do Windows | Fácil |
| Fedora | Mais atualizado, usado por muitos desenvolvedores | Médio |

Documente no seu relatório: qual distribuição escolheu e por quê.

### Etapa 2 — Instalar o Linux

Você tem duas opções:

**Opção A — Máquina Virtual (recomendado para iniciantes)**
1. Baixe e instale o VirtualBox (gratuito): https://www.virtualbox.org/
2. Baixe a ISO da distribuição escolhida
3. Crie uma nova máquina virtual com: 2GB RAM, 20GB disco, 2 CPUs
4. Monte a ISO e siga o instalador

**Opção B — Dual Boot (para quem quer mais performance)**
1. Crie um pendrive bootável com o Rufus (Windows) ou Etcher
2. Redimensione o disco para liberar espaço
3. Reinicie pelo pendrive e siga o instalador
4. CUIDADO: faça backup dos seus dados antes

Documente: qual opção escolheu, quais dificuldades encontrou, como resolveu.

### Etapa 3 — Explorar a Estrutura de Diretórios

Após a instalação, abra o terminal e explore:

```bash
# Veja onde você está
pwd

# Liste os diretórios raiz
ls /

# Explore os diretórios principais
ls /home
ls /etc
ls /var
ls /tmp
```

Conecte com o módulo 2.4: identifique pelo menos 5 diretórios e explique o propósito de cada um.

### Etapa 4 — Configurar Usuário e Permissões

1. Verifique seu usuário atual: `whoami`
2. Verifique os grupos do seu usuário: `groups`
3. Crie um diretório para seus projetos: `mkdir ~/projetos`
4. Verifique as permissões: `ls -la ~/projetos`
5. Experimente mudar permissões: `chmod 755 ~/projetos`

Conecte com o módulo 2.5: explique o que significa `755` e por que é uma permissão comum.

### Etapa 5 — Instalar Pacotes Essenciais

Instale as ferramentas que todo desenvolvedor precisa:

```bash
# Atualizar lista de pacotes (Ubuntu/Mint)
sudo apt update

# Instalar ferramentas essenciais
sudo apt install -y git curl wget vim build-essential

# Verificar instalação
git --version
curl --version
```

Conecte com o módulo 2.6: explique o que o `apt` faz e por que usamos `sudo`.

### Etapa 6 — Personalizar o Terminal

1. Abra o arquivo de configuração do bash: `nano ~/.bashrc`
2. Adicione um alias útil no final do arquivo:
   ```bash
   alias projetos='cd ~/projetos && ls -la'
   ```
3. Salve e aplique: `source ~/.bashrc`
4. Teste: digite `projetos` no terminal

Conecte com o módulo 2.8: explique o que é o `.bashrc` e como aliases funcionam.

### Etapa 7 — Montar o Relatório

Crie um documento com:

```
# Meu Ambiente Linux — [Seu Nome]

## Distribuição Escolhida
- Nome e versão: ...
- Por que escolhi: ...
- Método de instalação: VM / Dual Boot

## Processo de Instalação
- Dificuldades encontradas: ...
- Como resolvi: ...
- Tempo total: ...

## Estrutura de Diretórios
(Liste 5 diretórios e explique cada um)

## Usuário e Permissões
- Usuário: ...
- Grupos: ...
- Explicação de chmod 755: ...

## Pacotes Instalados
(Liste os pacotes e para que servem)

## Personalização
- Aliases criados: ...
- Outras personalizações: ...

## Reflexão
- O que foi mais difícil?
- O que foi mais surpreendente?
- Você se sente confortável usando o terminal?
```

---

## Entregáveis

- Relatório completo em Markdown ou Google Docs
- Screenshot do terminal com o Linux funcionando

---

## Critérios de Avaliação

Seu projeto está pronto quando:

- [ ] Linux instalado e funcionando (VM ou dual boot)
- [ ] Estrutura de diretórios explorada e documentada
- [ ] Permissões configuradas e explicadas
- [ ] Pacotes essenciais instalados
- [ ] Terminal personalizado com pelo menos 1 alias
- [ ] Relatório completo com conexões aos módulos do capítulo

---

## Dicas

- Se a instalação travar, pesquise o erro exato no Google — a comunidade Linux é enorme e provavelmente alguém já teve o mesmo problema
- Máquina virtual é mais segura para iniciantes — você não arrisca perder dados
- Não tenha medo de errar no terminal — o pior que pode acontecer é precisar reinstalar (e isso também é aprendizado)
- Anote TUDO que fizer — documentar o processo é tão importante quanto o resultado

---

## Mídias Recomendadas

- **Revolution OS** (documentário, 2001) — conta a história do Linux e do movimento open source. Vai te dar contexto sobre por que o Linux existe e por que é tão importante.
- **Mr. Robot** (série, 2015-2019) — o protagonista usa Linux e terminal o tempo todo. Mesmo sendo ficção, mostra como profissionais de tecnologia trabalham com essas ferramentas no dia a dia.
- **The Code: Story of Linux** (documentário, 2001) — documentário finlandês sobre a criação do Linux por Linus Torvalds. Curto e direto ao ponto.

---

[← Voltar ao Capítulo 2](../capitulos/cap02-mod08-shell-scripting.md)
