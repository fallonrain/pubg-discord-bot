🎮 PUBG Update Discord Bot

Bot para Discord que verifica automaticamente se haverá update ou manutenção do PUBG e avisa o servidor sem precisar abrir o jogo.

O bot também permite consulta manual via comando, ideal para squads que querem se organizar antes de jogar.

🚀 Funcionalidades

🔔 Aviso automático

Checa se há update/manutenção do PUBG

Executa automaticamente toda terça-feira às 13:00

Envia alerta apenas quando realmente existir atualização

💬 Comando manual

!pubg → verifica imediatamente se há update ou manutenção

☁️ Deploy em nuvem

Funciona 24/7 usando Railway

Não depende de VS Code aberto

🔐 Configuração segura

Tokens e IDs via variáveis de ambiente

Nenhuma informação sensível no código

🛠️ Tecnologias utilizadas

Python 3

discord.py

Railway (deploy)

dotenv (ambiente local)

Requests / scraping de notícias

📦 Estrutura do projeto
pubg-discord-bot/
│
├── bot.py               # Bot principal (comando + task automática)
├── pubg_checker.py      # Verificação de updates/manutenção
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Arquivos ignorados (env, venv, etc)
└── README.md            # Documentação

⚙️ Configuração
Variáveis de ambiente

O bot utiliza as seguintes variáveis:

DISCORD_TOKEN=seu_token_aqui
CHANNEL_ID=123456789012345678


📌 Em produção, essas variáveis devem ser configuradas diretamente na plataforma de deploy (ex: Railway).

▶️ Executar localmente (opcional)
python bot.py


O bot irá conectar ao Discord e ficar aguardando comandos.

🧪 Comandos disponíveis
Comando	Descrição
!pubg	Verifica manualmente se há update ou manutenção
📅 Funcionamento automático

⏰ Executa a cada 1 hora

📆 Dispara alerta somente terça-feira às 13:00

📢 Evita envio duplicado no mesmo dia

🧠 Silencioso quando não há update

🔒 Segurança

Token do Discord não é versionado

.env está no .gitignore

Configuração via variáveis de ambiente

🎯 Objetivo do projeto

Este projeto foi criado para resolver um problema real de jogadores de PUBG:
saber se haverá atualização sem precisar abrir o jogo.

Também serve como projeto de portfólio, demonstrando:

Integração com API externa

Bot para Discord

Tasks agendadas

Deploy em nuvem

Boas práticas de segurança

🧑‍💻 Autor

Desenvolvido por fallonrain
🔗 https://github.com/fallonrain
