🎮 PUBG Update Discord Bot

Bot para Discord que monitora automaticamente updates e manutenções do PUBG, avisando o servidor sem que os jogadores precisem abrir o jogo.

O projeto resolve um problema real de squads que querem se organizar antes de jogar, oferecendo checagem automática semanal e consulta manual via comando.

✨ Funcionalidades

🔔 Aviso automático de atualização

Executa toda terça-feira às 13:00

Envia mensagem apenas se houver update ou manutenção

Evita notificações duplicadas no mesmo dia

💬 Comando manual

!pubg → verifica imediatamente se há update/manutenção

☁️ Execução em nuvem

Bot online 24/7 via Railway

Não depende de execução local

🔐 Configuração segura

Uso de variáveis de ambiente

Token do Discord não versionado

🛠️ Tecnologias

Python 3

discord.py

Railway

dotenv

Requests

📁 Estrutura do projeto
pubg-discord-bot/
├── bot.py               # Bot principal (comandos + task automática)
├── pubg_checker.py      # Lógica de verificação de updates
├── requirements.txt     # Dependências
├── .gitignore           # Arquivos ignorados
└── README.md            # Documentação

⚙️ Configuração

O bot utiliza as seguintes variáveis de ambiente:

DISCORD_TOKEN=seu_token_do_discord
CHANNEL_ID=id_do_canal_para_notificacoes


Em produção, essas variáveis devem ser configuradas diretamente na plataforma de deploy (Railway).

▶️ Execução local (opcional)
python bot.py


Após iniciar, o bot ficará aguardando comandos no Discord.

💬 Comandos disponíveis
Comando	Descrição
!pubg	Verifica manualmente se há update ou manutenção
⏱️ Funcionamento automático

Verificação executada a cada 60 minutos

Notificação automática apenas:

na terça-feira

às 13:00

quando existe update confirmado

🔒 Segurança

Token do Discord não está no repositório

Arquivo .env ignorado pelo Git

Configuração sensível feita via variáveis de ambiente

🎯 Objetivo do projeto

Este projeto foi desenvolvido como:

Solução prática para jogadores de PUBG

Exercício de integração com APIs externas

Demonstração de:

bots para Discord

tarefas agendadas

deploy em nuvem

boas práticas de configuração e segurança

👤 Autor

Desenvolvido por fallonrain
GitHub: https://github.com/fallonrain
