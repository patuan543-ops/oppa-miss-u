import discord
import os

TOKEN = os.getenv("TOKEN", "").strip()
ASSET_ID = "1562365327784935454"
APP_ID = 1101687357900898304

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="I Miss You Oppa",
        details="I Miss You Oppa",
        state="I Miss You Oppa",
        application_id=APP_ID,
        assets={
            "large_image": ASSET_ID,
            "large_text": "I Miss You Oppa"
        },
        buttons=[
            {"label": "guns.lol", "url": "https://guns.lol/fym5"}
        ]
    )
    await client.change_presence(activity=activity)
    print(f"Treo thanh cong {client.user}")

client.run(TOKEN)
