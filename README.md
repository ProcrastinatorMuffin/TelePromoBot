# Referral Code Bot
This is a template for a Telegram bot that handles referral codes. It allows users to add, get and delete referral codes. This bot is ideal for any situation where you want to distribute referral codes to users in a fair and randomized manner.

## Setup

1. Clone this repository to your local machine.

`git clone https://gitlab.com/ihavepixelxd/telegram_promocode_bot_template.git`

2. Install the required Python packages.

`pip install -r requirements.txt`

3. Create a new bot on Telegram. Follow the instructions given by BotFather to get your API token.

4. Replace `'YOUR_BOT_TOKEN'` in `config.py` with the API token you received from BotFather.

5. Modify the variables in `config.py` to fit your needs. This includes messages, commands and the regex used for validating the referral codes.

Uncomment the `initialize_database()` line in `database.py` to set up the database for the first time.

## Running the Bot

Once you've set up everything, you can start the bot by running the `bot.py` script:

`python bot.py`

The bot will then start listening for messages on Telegram. 
Users can add their referral codes with the `/add` command, get a random code with the `/get` command, and delete their code with the `/del` command. The exact command names may vary based on your configuration in `config.py`.
