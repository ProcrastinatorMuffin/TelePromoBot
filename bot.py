import re
from aiogram import Bot, Dispatcher, types
from random import choice
from config import API_TOKEN, WELCOME_MSG, INVALID_CODE_MSG, SUCCESSFUL_ADD_MSG, SUCCESSFUL_DEL_MSG, \
    CODE_NOT_FOUND_MSG, NO_CODE_AVAILABLE_MSG, ADD_COMMAND, DEL_COMMAND, GET_COMMAND, CODE_REGEX
from database import add_code, get_codes, delete_code

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Handler for /start command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(WELCOME_MSG)


# Handler for add command
@dp.message_handler(commands=[ADD_COMMAND])
async def add_referral_code_command(message: types.Message):
    referral_code = message.get_args()
    if re.match(CODE_REGEX, referral_code):
        add_code(referral_code)
        await message.answer(SUCCESSFUL_ADD_MSG)
    else:
        await message.answer(INVALID_CODE_MSG)


# Handler for delete command
@dp.message_handler(commands=[DEL_COMMAND])
async def delete_referral_code_command(message: types.Message):
    referral_code = message.get_args()
    codes = [c[1] for c in get_codes()]
    if referral_code in codes:
        delete_code(referral_code)
        await message.answer(SUCCESSFUL_DEL_MSG)
    else:
        await message.answer(CODE_NOT_FOUND_MSG)


# Handler for get command
@dp.message_handler(commands=[GET_COMMAND])
async def send_referral_code(message: types.Message):
    # Get all codes from the database
    codes = get_codes()

    if codes:
        # Select a random code
        code = choice(codes)
        await message.answer(f"Here's your referral code: {code[1]}")
    else:
        await message.answer(NO_CODE_AVAILABLE_MSG)


# Start polling
if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
