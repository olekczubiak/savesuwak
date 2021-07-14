import requests
import json
from time import sleep

data1 = [{'artist': 'Little Simz', 'title': 'Woman ft. Cleo Sol', 'artworkUrl': 'https://images.radio.co/station_logos/s93b51ccc1.20190415084832.png'}, {'artist': 'Flohio', 'title': 'Flash', 'artworkUrl': 'https://is1-ssl.mzstatic.com/image/thumb/Music124/v4/5c/08/65/5c08657e-395e-1bb9-da6f-ee35cee8b4fd/source/100x100bb.jpg'}, {'artist': 'Rasmentalism', 'title': 'Umarł Król, Niech Żyje', 'artworkUrl': 'https://is5-ssl.mzstatic.com/image/thumb/Music118/v4/23/98/c1/2398c1a5-4b1c-8025-e171-34093108a085/source/100x100bb.jpg'}, {'artist': 'Denzel Curry', 'title': "BLACK BALLOONS l 13LACK 13ALLOONZ (feat. Twelve'len & GoldLink)", 'artworkUrl': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/e7/ed/6a/e7ed6a39-eda3-3c5e-2f4d-398f5bb05166/source/100x100bb.jpg'}, {'artist': 'Szczyl; Tymek', 'title': 'Anastazja', 'artworkUrl': 'https://is1-ssl.mzstatic.com/image/thumb/Music125/v4/df/ed/ce/dfedcefa-f0a0-5a5d-c872-1c65b9981595/source/100x100bb.jpg'}, {'artist': 'Jack Harlow', 'title': 'Way Out (feat. Big Sean)', 'artworkUrl': 'https://is1-ssl.mzstatic.com/image/thumb/Music115/v4/9b/9f/ff/9b9fff35-576a-c92f-42c4-889601cd3212/source/100x100bb.jpg'}, {'artist': 'Lorde', 'title': 'Solar Power', 'artworkUrl': 'https://is5-ssl.mzstatic.com/image/thumb/Music125/v4/81/3e/66/813e6684-c36c-9f6e-457d-0cf63f6d2fb0/source/100x100bb.jpg'}, {'artist': 'Childish Gambino', 'title': '3005', 'artworkUrl': 'https://is4-ssl.mzstatic.com/image/thumb/Music124/v4/ff/76/03/ff760377-ff58-7789-2dac-758356f11d55/source/100x100bb.jpg'}, {'artist': 'DaBaby', 'title': 'ROCKSTAR ft. Roddy Ricch', 'artworkUrl': 'https://images.radio.co/station_logos/s93b51ccc1.20190415084832.png'}, {'artist': 'Otsochodzi', 'title': 'Wszystko co mam ft. Rosalie., OKI', 'artworkUrl': 'https://images.radio.co/station_logos/s93b51ccc1.20190415084832.png'}, {'artist': 'Nyck Caution', 'title': 'Bad Day (feat. Denzel Curry)', 'artworkUrl': 'https://is3-ssl.mzstatic.com/image/thumb/Music124/v4/51/a5/3c/51a53c0d-4a6a-d263-97ad-9310a2e55786/source/100x100bb.jpg'}, {'artist': 'Tyler, The Creator', 'title': 'JUGGERNAUT', 'artworkUrl': 'https://is5-ssl.mzstatic.com/image/thumb/Music115/v4/21/97/ea/2197ea89-2bd4-b688-c2e6-6b81bdb8b422/source/100x100bb.jpg'}, {'artist': 'Kaz Bałagane', 'title': 'Blueface ft. Młody Dron', 'artworkUrl': 'https://images.radio.co/station_logos/s93b51ccc1.20190415084832.png'}, {'artist': 'Saweetie', 'title': 'Emotional (feat. Quavo)', 'artworkUrl': 'https://is4-ssl.mzstatic.com/image/thumb/Music125/v4/5d/f3/b8/5df3b823-c435-f28f-da30-16b3ef76cfef/source/100x100bb.jpg'}, {'artist': 'Berson', 'title': 'Trochę Pokory ft. Floral Bugs prod. @atutowy', 'artworkUrl': 'https://images.radio.co/station_logos/s93b51ccc1.20190415084832.png'}]

fake_db = []


def download_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return 'Error - API status code'

def save_to_file(data):
    pass

def number_of_elements(json_data):
    return int(len((json_data)))

def parse_data(json_data: str,number_of_song: int ,key_word: str):
    return json.dumps(json_data[number_of_song][key_word])

def return_all_data(json_data):
    for n in range(number_of_elements(json_data)):
        title = str(parse_data(json_data, n, 'title')).replace('"', '')
        artist = str(parse_data(json_data, n, 'artist')).replace('"', '')
        element = f'{artist} – {title}'
        if element in fake_db:
            pass
        else:
            fake_db.append(element)
            save_to_file(element)
        # print(f' {artist} – {title}')




if __name__ == "__main__":
    n: int = 0 
    while True:
        n += 1
        return_all_data(download_data('https://newonce.net/api/radio_history'))
        print(f'Próba numer = {n}')
        print(fake_db)

        # Spi 15 piosenek średnio po 3 min czyli 15*180 = 2700 sec
        # sleep(2700)
        # Testowo na 2 piosenki czyli 2 * 180 = 360 sec
        sleep(33)
        # Testowa blokada bezpieczeństwa udtawiona na 2.35h 
        if n == 3:
            break



# print(number_of_elements(data1))

# return_all_data(download_data('https://newonce.net/api/radio_history'))
# print(download_data('https://newonce.net/api/radio_history'))
# print(parse_data(data1, 0, 'title'))
# print(parse_data(data1, 0, 'artist'))
