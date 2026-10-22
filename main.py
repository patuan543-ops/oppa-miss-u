import discord
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

TOKEN = os.getenv("TOKEN", "").strip()

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

def run_web():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), Handler)
    server.serve_forever()

def keep_alive():
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()

client = discord.Client()

@client.event
async def on_ready():
    print(f"Da login: {client.user}")
    try:
        activity = discord.Activity(
            type=discord.ActivityType.listening, 
            name="I Miss You Oppa"
        )
        # Thêm status=discord.Status.dnd để bật chế độ Không làm phiền
        await client.change_presence(status=discord.Status.dnd, activity=activity)
        print("Da set status DND thanh cong!")
    except Exception as e:
        print(f"Loi set status: {e}")

if __name__ == "__main__":
    keep_alive()
    client.run(TOKEN)
