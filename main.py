import discord
import os
import time
from threading import Thread
from flask import Flask

USER_TOKEN = os.getenv("TOKEN")
APP_ID = 1562365327784935454

app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run_web, daemon=True).start()

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
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
    await client.change_presence(activity=activity)

client.run(USER_TOKEN)
