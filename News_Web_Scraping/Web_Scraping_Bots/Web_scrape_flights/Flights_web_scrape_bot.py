import hashlib
from urllib.request import urlopen, Request
from Web_Scraping_Bots.Web_scrape_flights.FLIGHTS_BOT import FLIGHTS_BOT
from Web_Scraping_Bots.Web_scrape_flights.Extract_flights_table import Extract_flights_table
import Web_Scraping_Bots.Constants as Const
from Web_Scraping_Bots.Web_scrape_flights.Flights_search import Flights_search
from Web_Scraping_Bots.Web_scrape_bot import Web_scrape_bot
"""
this class represent a bot that can extract information of current flights and search in the information
"""


class Flights_web_scrape_bot(FLIGHTS_BOT):
    def __init__(self,driver_path=Const.DRIVER_PATH):
        # base url
        self.__base_url = Request(Const.BEN_GURION_FLIGHTS_URL,
                                  headers={'User-Agent': 'Mozilla/5.0'})
        self.__driver = Web_scrape_bot(driver_path)
        # use the response for get most updated web page
        self.__response = urlopen(self.__base_url).read()
        # current state of web page
        self.__Hash = hashlib.sha224(self.__response).hexdigest()
        self.__driver.determine_page(Const.BEN_GURION_FLIGHTS_URL)
        Extract_flights_table(self.__driver)

    def update_flight_storage(self):
        """
        update all flight information ,
        only if we didn't have the most updated data of flights information
        @return:
        """
        self.__response = urlopen(self.__base_url).read()
        currentHash = hashlib.sha224(self.__response).hexdigest()
        # check if the current hush is the most updated
        if self.__Hash != currentHash:
            self.__Hash = currentHash
            self.__driver.determine_page(Const.BEN_GURION_FLIGHTS_URL)
            Extract_flights_table(self.__driver)

    def search_in_flights(self, search_text):
        """
        search the text in all of the flights
        and print the flights that contain any word of the text
        @param search_text: string that the user insert ,for search in the flights
        @return:
        """
        self.update_flight_storage()
        text_lower = search_text.lower()
        text_words = list(text_lower.split(" "))
        Flights_search(text_words)
