API_TOKEN = 'YOUR_BOT_TOKEN'  # replace with your bot token
DB_NAME = 'your_database_name.db'  # replace with your database name
# Change the following commands to suit your needs
WELCOME_MSG = "Welcome! To send your referral code, use the /add command followed by your code. Remember, " \
              "the code should contain only Latin letters and Arabic numerals."
INVALID_CODE_MSG = "Invalid referral code. The code should contain only Latin letters and Arabic numerals."
SUCCESSFUL_ADD_MSG = "Referral code added successfully!"
SUCCESSFUL_DEL_MSG = "Referral code deleted successfully!"
CODE_NOT_FOUND_MSG = "Referral code not found."
NO_CODE_AVAILABLE_MSG = "No referral codes available at the moment."
ADD_COMMAND = 'add'  # replace with your command name for adding a code
DEL_COMMAND = 'del'  # replace with your command name for deleting a code
GET_COMMAND = 'get'  # replace with your command name for getting a code
CODE_REGEX = r'^[a-zA-Z0-9]+$'  # regex for your code format
