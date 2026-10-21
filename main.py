import discord
import os
import time
from threading import Thread
from flask import Flask

USER_TOKEN = os.getenv("TOKEN", "").strip()
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
    print(f"Logged in as {client.user}")

client.run(USER_TOKEN)
