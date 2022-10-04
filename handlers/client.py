from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from database.bot_db import sql_command_random
from handlers.parse import parser


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f'Жакшысынарбы {message.from_user.full_name}')


# @dp.message_handler(commands=['mem'])
async def mem(call: types.CallbackQuery):
    photo = open("media/memchik.png", 'rb')
    await bot.send_photo(call.from_user.id, photo)


# @dp.message_handler(commands=["quiz"])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("След.", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько весил самый толстый человек в истории?"
    answers = [
        "615",
        "523",
        "727",
        "827",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Learn more facts!",
        open_period=10,
        reply_markup=markup
    )


async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply('Комманда должна быть ответом на сообщение!')
    else:
        await bot.pin_chat_message(message.chat.id, message.message_id)


async def show_random_dish(message: types.Message):
    await sql_command_random(message)


async def parser_news(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,
            text=f"{item['link']}\n\n"
                 f"{item['title']}\n\n"
                 f"{item['time']}, "
                 f"#Y{item['day']}, "
                 f"#{item['year']}\n"
        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(mem, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(show_random_dish, commands=['get'])
    dp.register_message_handler(parser_news, commands=['news'])
