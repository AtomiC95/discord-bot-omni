# discord-bot-omni

# General

This is a dicords bot that is connceted to an Local LLM of your choice, via the oobabooga API.
As for now the bot is able to respond to messages that are send via `!omni`.

# Further Development

The bot is still in development and will be able to do more things in the future.

# TODO

- [ ] Add RAG-functionality via llamaindex

# Setup

To get started you need to create a bot within the discord developer portal and get the token.
This can be done by following the steps in the [Discord Developer Portal](https://discord.com/developers/applications).

After you have the token you need to create a `.env` file in the root directory of the project and add the following line:

`DISCORD_API_TOKEN = "YOUR_TOKEN"`

## oobabooga API

Now you need to get oobabooga text-generation-webui running on your local machine. You can find the repository [here](https://github.com/oobabooga/text-generation-webui).
follow the instructions in the README on how to set it up. To get the API running you need to run the following command:

`bash start_linux.sh --api --listen --trust-mode-remote-code --verbose`

By default the API will run on `http://localhost:5000`. The `--trust-mode-remote-code` is needed for specific models for example [microsoft/Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) model needs it.

### Load Model

Load a model within the webui for more on that read the README of the [text-generation-webui](https://github.com/oobabooga/text-generation-webui).

# Run

know you can run the bot by running the following command:

`python basic_dico_bot.py`

# Usage

Within the discord server you can now send `!omni` and the bot will respond with a generated text from the oobabooga API.
