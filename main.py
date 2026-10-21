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
    # status code
    print(f"Treo thanh cong {client.user}")

if __name__ == "__main__":
    keep_alive()
    client.run(TOKEN)
