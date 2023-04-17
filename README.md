# Discord Server

Want to hang out with us? Join us at the [Lingua Discord Server!](https://discord.gg/JRdhFQvA)

Help us experiment with this bot, and see what we can improve.

# Lingua AI Chatbot

Welcome to the Lingua Project repo! This is an open-source project that consists of two parts: a console-based chatbot and a Discord bot.

## LinguaConsoleBot

The LinguaConsoleBot is a chatbot that runs in the console/terminal. It uses the OpenAI GPT-3 API to generate responses to user input in a conversation.

### Prerequisites

To run the LinguaConsoleBot, you will need to have Python 3 installed. You will also need an OpenAI API key to access the GPT-3 API.

### Installation

- Clone the repository to your local machine
- Install the required Python libraries by running pip install -r requirements.txt
- Create a .env file and add your OpenAI API key as OPENAI_API_KEY=YOUR_API_KEY
- Run the chatbot by running python LinguaConsoleBot/Lingua.py

## LinguaDiscordBot

The LinguaDiscordBot is a chatbot that runs on Discord. It uses the OpenAI GPT-3 API to generate responses to user input in a conversation.

### Prerequisites

To run the LinguaDiscordBot, you will need to have Python 3 installed. You will also need an OpenAI API key and a Discord bot token.

### Installation

- Clone the repository to your local machine
- Install the required Python libraries by running pip install -r requirements.txt
- Create a .env file and add your OpenAI API key and Discord bot token as follows:

`OPENAI_API_KEY=YOUR_API_KEY` and `DISCORD_TOKEN=YOUR_BOT_TOKEN`

### Usage

Once the bot is up and running, users can start a conversation by typing !start in a Discord channel where the bot has been added. The bot will create a new text channel for the conversation and provide instructions on how to interact with it. Users can use !speak to send messages to the bot and !feedback to receive feedback on the conversation so far.

### Disclaimer

Please note that the Lingua AI Chatbot is a tool designed to facilitate language learning and should not be relied upon for accurate translations or professional language advice. The creator of this bot is not responsible for any harm that may arise from its use.

### License

This project is licensed under the terms of the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this software, as long as you adhere to the terms of the license.
