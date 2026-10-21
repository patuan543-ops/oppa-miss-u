import discord
import os
import time

USER_TOKEN = os.getenv("TOKEN")
APP_ID = 1562317792324362270

client = discord.Client()

@client.event
async def on_ready():
    print(f"Đã treo cho {client.user}")
    
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="Oppa Miss U",
        details="🥽 Playing on VR",
        state="guns.lol/fym5",
        application_id=APP_ID,
        assets={
            "large_image": "cat",
            "large_text": "Limertta VR"
        },
        timestamps={"start": int(time.time()) * 1000}
    )
    
    await client.change_presence(activity=activity)

client.run(USER_TOKEN)
