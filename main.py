import discord
import os
import time

USER_TOKEN = os.getenv("TOKEN")
APP_ID = 1562365327784935454

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="Oppa Miss U",
        details="Playing on VR",
        state="guns.lol/fym5",
        application_id=APP_ID,
        assets={
            "large_image": "cat",
            "large_text": "Oppa Miss U",
            "small_image": "vr",
            "small_text": "VR"
        },
        timestamps={"start": int(time.time())}
    )
    await cli
