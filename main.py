import discord, os, base64

TOKEN = os.getenv("TOKEN","").strip()
IMG = "https://i.imgur.com/8Km9tFF.jpeg"
IMG_MP = f"mp:external/{base64.b64encode(IMG.encode()).decode().replace('=','').replace('/','_').replace('+','-')}"

client = discord.Client()

@client.event
async def on_ready():
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name="I Miss You Oppa",
        details="I Miss You Oppa",
        state="I Miss You Oppa",
        application_id=1101687357900898304,
        assets={
            "large_image": IMG_MP,
            "large_text": "I Miss You Oppa"
        },
        buttons=[
            {"label": "guns.lol", "url": "https://guns.lol/fym5"}
        ]
    )
    await client.change_presence(activity=activity)
    print(f"Treo thanh cong {client.user} - Da fix anh ?")

client.run(TOKEN)
