import discord, os

TOKEN = os.getenv("TOKEN","").strip()
client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="I Miss You Oppa",
        details="I Miss You Oppa",
        state="I Miss You Oppa",
        assets={
            "large_image": "https://i.imgur.com/8Km9tFF.jpeg",
            "large_text": "I Miss You Oppa"
        }
    )
    await client.change_presence(activity=activity)
    print(f"Treo thanh cong {client.user}")

client.run(TOKEN)
