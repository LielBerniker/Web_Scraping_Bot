import Web_Scraping_Bots.Constants as Const
import os
from selenium import webdriver

"""
this class represent a bot that 
"""


class Web_scrape_bot(webdriver.Chrome):
    def __init__(self, driver_path=Const.DRIVER_PATH,
                 exit_page=True):
        self.__driver_path = driver_path
        self.__exit_page = exit_page
        os.environ['PATH'] += self.__driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Web_scrape_bot, self).__init__(options=options)
        self.implicitly_wait(30)
        self.maximize_window()

    """
    exit the web page when finish the process ' only if exit page is true
    @return: 
    """

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.__exit_page:
            self.quit()

    def determine_page(self, url):
        self.get(url)
