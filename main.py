# import requests
# from datetime import datetime
# import sqlite3
#
# API = '6418b539e0697f54de8a3df65ebe9444'
#
# parameters = {
#     'appid': API,
#     'units': 'metric',
#     'lang': 'en'
# }
#
#
# while True:
#     city = input('Shaxar nomini kiriting: ')
#     if city.lower() == 'stop':
#         break
#     try:
#         parameters['q'] = city
#         response = requests.get('https://api.openweathermap.org/data/2.5/weather?',
#                                 params=parameters)
#         data = response.json()
#
#         name = data['name']
#         description = data['weather'][0]['description']
#         temp = data['main']['temp']
#         wind_speed = data['wind']['speed']
#         pressure = data['main']['pressure']
#         humidity = data['main']['humidity']
#         timezone = data['timezone']
#         sunrise = datetime.fromtimestamp(data['sys']['sunrise'] + timezone).strftime('%Y-%m-%d %H:%M:%S')
#         sunset = datetime.fromtimestamp(data['sys']['sunset'] + timezone).strftime('%Y-%m-%d %H:%M:%S')
#
#         print(f"""{name} shaxrida {description} ob-xavo
#     Ob-xavo darajasi: {temp}
#     Shamol tezligi: {wind_speed}
#     Quyosh chiqishi: {sunrise}
#     Quyosh botishi: {sunset}""")
#
#         database = sqlite3.connect('weather.db')
#         cursor = database.cursor()
#
#         cursor.execute('''
#             INSERT INTO weather(city, temp, wind, description, pressure, humidity, sunrise, sunset)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#             ''', (name, temp, wind_speed, description, pressure, humidity, sunrise, sunset))
#
#         database.commit()
#         database.close()
#
#     except:
#         print('invalid city')


import requests
import sqlite3

photos= requests.get('https://jsonplaceholder.typicode.com/photos').json()


for photo in photos:
    albumId =photo['albumId']
    id = photo['id']
    title = photo['title']
    url =photo['url']
    thumbnailUrl =photo['thumbnailUrl']

    database = sqlite3.connect('photos.db')
    cursor = database.cursor()

    cursor.execute('''
            INSERT INTO photos(albumId,id,title,url,thumbnailUrl)
            VALUES (?, ?, ?, ?, ?)
            ''', (albumId,id,title,url,thumbnailUrl))

    database.commit()
    database.close()

