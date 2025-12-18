import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks
from datetime import datetime
from pubg_checker import check_pubg_update

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

last_notification_date = None


@client.event
async def on_ready():
    print(f"🤖 Bot conectado como {client.user}")
    check_update_task.start()


@tasks.loop(minutes=60)
async def check_update_task():
    global last_notification_date

    now = datetime.now()

    # Checar somente terça-feira às 13:00
    if now.weekday() != 1 or now.hour != 13:
        return

    # Evitar enviar mais de uma vez no mesmo dia
    if last_notification_date == now.date():
        return

    result = check_pubg_update()
    if not result or not result["has_update"]:
        print("🔍 Checado, sem update.")
        last_notification_date = now.date()
        return

    channel = client.get_channel(CHANNEL_ID)
    if not channel:
        print("❌ Canal não encontrado.")
        return

    message = (
        f"🚨 **ATENÇÃO SQUAD!** 🚨\n\n"
        f"🎮 **PUBG terá update/manutenção hoje!**\n"
        f"📰 {result['title']}\n"
        f"📅 {result['date']}\n"
        f"🔗 {result['url']}\n\n"
        f"⚠️ Evitem abrir o jogo agora."
    )

    await channel.send(message)
    last_notification_date = now.date()
    print("✅ Aviso enviado com sucesso.")


client.run(TOKEN)
