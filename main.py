import discord, os, threading, http.server, socketserver

TOKEN = os.getenv("TOKEN","").strip()
IMAGE_URL = "https://i.imgur.com/8Km9tFF.jpeg"

def keep_alive():
    PORT = int(os.environ.get("PORT", 10000))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=keep_alive, daemon=True).start()

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="I Miss You",
        details="I Miss You Oppa",
        state="I Miss You Oppa",
        application_id=1234567890123456789,
        assets={
            "large_image": IMAGE_URL,
            "large_text": "I Miss You Oppa",
            "small_image": IMAGE_URL,
            "small_text": "Oppa"
        },
        buttons=[
            {"label": "guns.lol", "url": "https://guns.lol/fym5"}
        ]
    )
    await client.change_presence(activity=activity)
    print(f"Da treo co anh {client.user}")

client.run(TOKEN)
