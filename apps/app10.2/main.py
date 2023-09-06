import requests
import selectorlib
import sqlite3

from datetime import datetime


URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class Event:
    def scrape(self, url):
        """Scrape the page source from the URL"""
        response = requests.get(url, headers=HEADERS)
        source = response.text
        return source


    def extract(self, source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(source)["tours"]
        return value


class DataBase:

    def __init__(self):
        self.connection = sqlite3.connect("data.db")

    def store(self, extracted):
        now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO temperatures VALUES(?, ?)", (now, extracted))
        self.connection.commit()


if __name__ == "__main__":
    event = Event()
    database = DataBase()
    scraped = event.scrape(URL)
    extracted = event.extract(scraped)
    print(extracted)
    database.store(extracted)
