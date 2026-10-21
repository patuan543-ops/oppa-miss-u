import discord, os, threading, http.server, socketserver

TOKEN = os.getenv("TOKEN","").strip()
IMG_ID = "1562365327784935454"

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
        name="I Miss You Oppa",
        details="I Miss You Oppa",
        state="I Miss You Oppa",
        assets={
            "large_image": IMG_ID,
            "large_text": "I Miss You Oppa",
            "small_image": IMG_ID,
            "small_text": "VR"
        },
        buttons=[
            {"label": "Gun.lol", "url": "https://gun.lol/fym5"}
        ]
    )
    await client.change_presence(activity=activity)
    print(f"Da treo co anh {client.user}")

client.run(TOKEN)
