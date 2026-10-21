import discord, os
from threading import Thread
from flask import Flask

TOKEN = os.getenv("TOKEN","").strip()

app = Flask(__name__)
@app.route('/')
def home(): return "OK"
Thread(target=lambda: app.run(host='0.0.0.0', port=8080), daemon=True).start()

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="I Miss You Oppa"))
    print(f"Treo thanh cong {client.user}")

client.run(TOKEN)
