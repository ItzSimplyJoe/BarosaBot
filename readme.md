# Discord Bot
This is a Discord bot created using the discord.py library. The bot is designed to perform various commands and provide functionality for a Discord server. Below is an overview of the bot's features and how to set it up.

## Features
- Help command: help - Displays a list of available commands and their descriptions.
- Staff help command: shelp - Displays a list of staff-specific commands and their descriptions.
- IP command: ip - Retrieves the server IP address.
- Store command: store - Provides information about the server's online store.
- Website command: website - Displays the server's website URL.
- Rules command: rules - Shows the server's rules.
- Clear command: clear [amount] - Clears a specified number of messages from the current channel (default: 5).
- Kick command: kick [member] [reason] - Kicks the specified member from the server with an optional reason.
- Ban command: ban [member] [reason] - Bans the specified member from the server with an optional reason.
- Unban command: unban [member] - Unbans the specified member from the server.
- Ticket command: ticket - Creates a support ticket.
- Close command: close - Closes the current ticket.
- Add command: add [member] - Adds a member to the current ticket.
- Remove command: remove [member] - Removes a member from the current ticket.
  Staff application command: apply - Initiates the staff application process.
## Setup
Install the necessary dependencies:

1. discord.py: ```pip install discord.py```
- Create a new Discord bot and obtain the bot token.

2. Go to the Discord Developer Portal.
- Create a new application and navigate to the "Bot" tab.
- Click on "Add Bot" to create a bot for your application.
- Under the "Token" section, click on "Copy" to copy the bot token.
3. Configure the bot:

- Create a config.json file in the same directory as the main bot file.
- Open the config.json file and enter the following content:
```json{
  "token": "YOUR_BOT_TOKEN",
  "prefix": "!"
}```
Replace YOUR_BOT_TOKEN with the bot token you obtained in the previous step.
4. Customize the bot's behavior:

- Modify the event handlers and commands in the main bot file (bot.py) to fit your requirements.
- You can add or remove commands by defining new functions and using the @bot.command() decorator.
5. Run the bot:

- Execute the main bot file using Python: python bot.py
- If everything is set up correctly, you should see the message ">> Bot is online <<" indicating that the bot has successfully connected to Discord.
Note: Make sure the bot has the necessary permissions in your Discord server, such as managing messages and kicking/banning members if required.

Feel free to modify and expand the bot's functionality to suit your needs. For more information and advanced usage of the discord.py library, refer to the discord.py documentation.

If you have any questions or need further assistance, feel free to reach out.