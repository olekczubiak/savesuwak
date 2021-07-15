import requests
import json
import time
import smtplib, ssl
from env import RECIVER_MAIL, SENDER_MAIL, PASSWORD, PORT, SMTP_SERVER

MY_TIME = str(time.ctime()).replace(' ', '-')[:10]
fake_db = []


def download_data(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    else:
        return 'Error - API status code'


class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = SMTP_SERVER
        self.port = PORT
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, subject, reciver, body):
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + reciver,
            "MIME-Version: 1.0",
            "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            RECIVER_MAIL,
            headers + "\r\n\r\n" + body)



def save_to_file(data: str, filename: str = MY_TIME):
    f = open(f'data/{filename}', 'a')
    f.write(f'{data} \n ')

def number_of_elements(json_data):
    return int(len((json_data)))

def parse_data(json_data: str,number_of_song: int ,key_word: str):
    return json.dumps(json_data[number_of_song][key_word], ensure_ascii=False).encode('utf8')

def return_all_data(json_data):
    for n in range(number_of_elements(json_data)):
        title = '<b>' + str(parse_data(json_data, n, 'title').decode()).replace('"', '') + '</b>'
        title_to_save =  str(parse_data(json_data, n, 'title').decode()).replace('"', '')
        artist = str(parse_data(json_data, n, 'artist').decode()).replace('"', '')
        element = f'{artist} – {title}'
        element_to_save = f'{artist} – {title_to_save}'
        if element in fake_db:
            pass
        else:
            fake_db.append(element)
            save_to_file(element_to_save)



if __name__ == "__main__":
    n: int = 0 
    while True:
        n += 1
        return_all_data(download_data('https://newonce.net/api/radio_history'))

        if n == 3:
            output: str = ''
            for element in fake_db:
                output +=  '<li>'+ element + '</li>'
            html = f"<html><head></head><body><p>Audycja z dzisiaj<br> <ol> {output.encode('ascii', 'ignore')} </ol></body></html>"
            gm = Gmail(SENDER_MAIL, PASSWORD)
            gm.send_message(f'Funkowa środa Suwaka {MY_TIME}' , RECIVER_MAIL, html)
            break

        # Spi 15 piosenek średnio po 3 min czyli 15*180 = 2700 sec
        time.sleep(2700)

        # Testowo na 2 piosenki czyli 2 * 180 = 360 sec
        # time.sleep(360)