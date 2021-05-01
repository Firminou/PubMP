import discord
from config import config
client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send(config.msg_pub)
      print(f"J'ai envoyé la pub mp à {user.name}")

    except:
       print(f"Je n'ai pas réussi à envoyer la pub mp à {user.name}")

client.run(config.private_token, bot=False)