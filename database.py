# import sqlite3
#
# database = sqlite3.connect('weather.db')
# cursor = database.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS weather(
#     weather_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     city CHAR(20),
#     temp CHAR(10),
#     wind CHAR(10),
#     description CHAR(30),
#     pressure CHAR(10),
#     humidity CHAR(10),
#     sunrise TEXT,
#     sunset TEXT
#     );
#     ''')
# database.commit()
# database.close()

import sqlite3

database = sqlite3.connect('photos.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS photos(
    albumId INTEGER,
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    url TEXT,
    thumbnailUrl TEXT
    )
    ''')
database.commit()
database.close()