# 🎮 PUBG Update Discord Bot

Bot para Discord que monitora automaticamente **updates e manutenções do PUBG**, avisando o servidor sem que os jogadores precisem abrir o jogo.

O projeto foi criado para squads que querem se organizar melhor e também serve como **projeto de portfólio**, demonstrando integração com APIs externas, tarefas agendadas e deploy em nuvem.

---

## ✨ Funcionalidades

- 🔔 **Aviso automático de atualização**
  - Executa toda **terça-feira às 13:00**
  - Envia mensagem apenas quando existe update ou manutenção
  - Evita notificações duplicadas no mesmo dia

- 💬 **Comando manual**
  - `!pubg` → verifica manualmente se há update ou manutenção

- ☁️ **Execução em nuvem**
  - Bot online 24/7 usando Railway
  - Não depende de VS Code ou computador ligado

- 🔐 **Configuração segura**
  - Uso de variáveis de ambiente
  - Token do Discord não versionado

---

## 🛠️ Tecnologias utilizadas

- 🐍 **Python 3**
- 💬 **discord.py**
- ☁️ **Railway**
- 📦 **python-dotenv**
- 📡 **Requests**

---

## 📁 Estrutura do projeto

pubg-discord-bot/
├── bot.py # Bot principal (comando + task automática)
├── pubg_checker.py # Lógica de verificação de updates
├── requirements.txt # Dependências do projeto
├── .gitignore # Arquivos ignorados
└── README.md # Documentação

yaml
Copy code

---

## ⚙️ Configuração

O bot utiliza as seguintes variáveis de ambiente:

```env
DISCORD_TOKEN=seu_token_do_discord
CHANNEL_ID=1451220733576478851
Em produção, essas variáveis devem ser configuradas diretamente na plataforma de deploy (Railway).

▶️ Execução local (opcional)
bash
Copy code
python bot.py
Após iniciar, o bot ficará aguardando comandos no Discord.

💬 Comandos disponíveis
Comando	Descrição
!pubg	Verifica manualmente se há update ou manutenção

⏱️ Funcionamento automático
Verificação executada a cada 60 minutos

Notificação automática apenas:

✔ terça-feira

✔ às 13:00

✔ quando existe update confirmado

🔒 Segurança
Boas práticas aplicadas no projeto:

Token do Discord não está no repositório

Arquivo .env está no .gitignore

Variáveis sensíveis via environment variables

🎯 Objetivo do projeto
Este projeto foi desenvolvido para resolver um problema real de jogadores de PUBG:
descobrir se haverá atualização ou manutenção sem precisar abrir o jogo.

Também demonstra:

criação de bots para Discord

integração com fontes externas

tarefas agendadas

deploy em nuvem

boas práticas de segurança

👤 Autor
Desenvolvido por fallonrain
🔗 https://github.com/fallonrain

yaml
Copy code
