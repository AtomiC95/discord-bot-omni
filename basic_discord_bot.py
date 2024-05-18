"""This is a basic discord bot that can reply to messages and send messages to a channel"""

import discord
from dotenv import load_dotenv
import os
from prompt import get_prompt
import requests

load_dotenv()

token: str | None = os.getenv("DISCORD_API_TOKEN")

url = "http://127.0.0.1:5000/v1/chat/completions"

headers = {"Content-Type": "application/json"}

history = []


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user} (ID: {self.user.id})")
        print("------")

    async def on_message(self, message):
        # bot should not reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!omni"):
            print(f"Received message: {message.content.strip('!omni')}")
            user_message = message.content.strip("!omni")
            history.append({"role": "user", "content": user_message})
            data = {"mode": "chat", "messages": history}
            response = requests.post(url, headers=headers, json=data, verify=False)
            assistant_message = response.json()["choices"][0]["message"]["content"]
            print(f"Assistant message: {assistant_message}")
            history.append({"role": "assistant", "content": assistant_message})
            await message.reply(
                f"{assistant_message}",
                mention_author=True,
            )


intents = discord.Intents.default()
intents.message_content = True

clienbt = MyClient(intents=intents)
if token is not None:
    clienbt.run(token)
