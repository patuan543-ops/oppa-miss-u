import discord, os

TOKEN = os.getenv("TOKEN","").strip()

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="I Miss You Oppa"))
    print(f"Treo thanh cong {client.user} - Khong bao gio exit!")

client.run(TOKEN)
