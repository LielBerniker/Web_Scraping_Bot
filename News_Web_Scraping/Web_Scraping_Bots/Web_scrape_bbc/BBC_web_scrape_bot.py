from Web_Scraping_Bots.Web_scrape_bot import Web_scrape_bot
from Web_Scraping_Bots.Web_scrape_bbc.Links_extract import Links_extract
from Web_Scraping_Bots.Web_scrape_bbc.Article_content_extract import Article_content_extract
from Web_Scraping_Bots.Web_scrape_bbc.Article_search import Article_search
import Web_Scraping_Bots.Constants as Const
from Web_Scraping_Bots.Web_scrape_bbc.BBC_BOT import BBC_BOT
"""
this class represent a bot that extracts all the news links in the bbc main page
"""


class BBC_web_scrape_bot(BBC_BOT):
    def __init__(self, driver_path=Const.DRIVER_PATH):
        self.__driver = Web_scrape_bot(driver_path)
        self.__articles_list = []
        self.update_articles_storage()

    def update_articles_storage(self):
        """
        this function first extract all the links of potential articles from the bbx web page
        then go over each link and extract the article content and name from it
        finally save it to a json , only if the article didn't already exist
        @return:
        """
        self.__driver.determine_page(Const.BBC_URL)
        link_extract = Links_extract(self.__driver)
        list_of_links = link_extract.get_links_to_list()
        for cur_link in list_of_links:
            self.__driver.determine_page(cur_link)
            content_extract = Article_content_extract(cur_link, self.__driver)
            content_extract.update_article_storage()
        self.__driver.close()

    def search_in_articles(self, search_text):
        """
        the function go over all the content of the articles
        then print the name and link of all articles that contain attlist half of the words in search
        @param self: string that contain words
        @return:
        """
        text_lower = search_text.lower()
        text_list = list(text_lower.split(" "))
        Article_search(text_list)
