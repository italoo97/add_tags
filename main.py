import discord
from discord.ext import commands
import asyncio
import json

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

TOKEN = config["TOKEN"]
Tag = config["Tag"]["enabled"]

intents = discord.Intents.all()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def load_extensions():
    extensions = {
        "Tag": Tag,
    }
    
    for name, enabled in extensions.items():
        if enabled:
            try:
                await bot.load_extension(f"cogs.{name.lower().replace(' ', '')}")
                print(f"✅ Carregando módulo: {name}")
            except Exception as e:
                print(f"❌ Falha ao carregar {name}: {str(e)}")

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    try:
        synced = await bot.tree.sync()
        print(f"🔁 {len(synced)} comandos slash sincronizados globalmente.")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    print(f"🤖 Bot online como {bot.user}")

async def main():
    await load_extensions()
    async with bot:
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
