import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} としてログインしました！")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

bot.run("YOUR_BOT_TOKEN")  # ←後でここは環境変数に置き換えると安全！
