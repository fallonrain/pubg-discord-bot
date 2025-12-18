# 🤖 PUBG Discord Update Bot

Bot para Discord desenvolvido em **Python** que monitora fontes oficiais do PUBG e **avisa automaticamente** em um canal do servidor quando há **update ou manutenção programada**, evitando que os jogadores abram o jogo à toa.

---

## 🎯 Objetivo do Projeto

Este bot foi criado para resolver um problema real:  
descobrir se haverá atualização do PUBG **sem precisar abrir o jogo**, usando apenas informações oficiais.

O bot roda 24/7 na nuvem e envia avisos automáticos toda **terça-feira às 13:00**.

---

## ✨ Funcionalidades

- 🔍 Consulta automática à **Steam News API**
- 🧠 Detecção de update/manutenção por palavras-chave
- ⏰ Verificação automática semanal (terça-feira às 13h)
- 📢 Envio de mensagem automática em canal específico
- 💬 Comando manual `!pubg` para consulta instantânea
- ☁️ Deploy em cloud (Railway)
- 🔐 Uso de variáveis de ambiente para segurança

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **discord.py**
- **Requests**
- **Steam Web API (News)**
- **Railway (deploy 24/7)**
- **Git & GitHub**

---

## 🚀 Como rodar localmente

```bash
git clone https://github.com/fallonrain/pubg-discord-bot.git
cd pubg-discord-bot
pip install -r requirements.txt
python bot.py
