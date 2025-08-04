import discord
from discord.ext import commands
import os
from keep_alive import keep_alive  # ここ追加！

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ ログインしました: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

keep_alive()  # ここでFlaskサーバーを起動
bot.run(os.environ.get("TOKEN"))