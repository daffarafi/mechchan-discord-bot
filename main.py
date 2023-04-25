from dotenv import load_dotenv
import discord
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == client.user : return

        if message.content.startswith("halo") :
            await message.channel.send('Haro Warudo!')
            return

        if message.content.startswith("$ngebacot") :
            msg = message.content.strip("$ngebacot ")           

            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": msg}
                ]
            )

            await message.channel.send(completion.choices[0].message.content)
            return
        

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(os.getenv('DISCORD_API_TOKEN'))