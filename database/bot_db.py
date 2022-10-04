import random
import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()
    if db:
        print('Successfully connected!')

    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(photo TEXT,"
               "name TEXT PRIMARY KEY, type TEXT, price INTEGER,"
               "description TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_dish = random.choice(result)
    await bot.send_photo(message.chat.id, random_dish[0],
                         caption=f"{random_dish[1]}, {random_dish[2]} стоит: {random_dish[3]}\n"
                                 f"{random_dish[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()


async def sql_command_delete(name):
    cursor.execute("DELETE FROM menu WHERE name = ?", (name, ))
    print(name)
    db.commit()


async def sql_command_get_all_id():
    return cursor.execute("SELECT name FROM menu").fetchall()