import discord, os

TOKEN = os.getenv("TOKEN","").strip()
APP_ID = 1101687357900898304
ASSET_ID = "1562365327784935454"

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.listening,
        name="I Miss You Oppa",
        application_id=APP_ID,
        assets={
            "large_image": ASSET_ID,
            "large_text": "Meow"
        }
    )
    await client.change_presence(activity=activity)
    print(f"Treo thanh cong {client.user}")

client.run(TOKEN)
