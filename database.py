import sqlite3
import csv


def register_db(id_client, name, first_item, second_item, third_item, username):
    with sqlite3.connect("bot_tint.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""INSERT or REPLACE INTO tMain VALUES (?, ?, ?, ?, ?, ?)""", (id_client, name, first_item,
                                                                                     second_item, third_item, username))
        cursor.close()
        connection.commit()


def add_items_db(id_client, first_item, second_item, third_item):
    with sqlite3.connect("bot_tint.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""UPDATE tMain SET first_item = "{first_item}", second_item = {second_item}, 
        third_item = {third_item} WHERE tg_id = {id_client}""")
        cursor.close()
        connection.commit()


def get_name(id_client):
    try:
        with sqlite3.connect("bot_tint.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"""SELECT name FROM tMain WHERE tg_id = {id_client}""")
            record = cursor.fetchone()
            cursor.close()
            connection.commit()
        return record[0]
    except Exception:
        return '?'


def get_all():
    with sqlite3.connect("bot_tint.db") as connection:
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM tMain""")
        record = cursor.fetchall()
        cursor.close()
        connection.commit()
    return record