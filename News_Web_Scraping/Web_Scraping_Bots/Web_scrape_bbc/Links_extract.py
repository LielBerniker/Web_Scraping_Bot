from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
"""
this class extract two type of web element that may contain an article,
then extract all the links in these elements and return them in list
"""


class Links_extract:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__all_articles_img = self.__driver.find_elements(By.CSS_SELECTOR,'div[class="media block-link"]')
        self.__all_articles_regular = self.__driver.find_elements(By.CSS_SELECTOR,'a[class="block-link__overlay-link"]')
        self.__all_links = []


    def get_links_to_list(self):
        """
         call functions that extract all type of articles from the web page
         @return: list of all the articles link
         """
        self.__pull_article_regular()
        self.__pull_article_img()
        return self.__all_links

    def __pull_article_regular(self):
        """
         update all the links of regular type article
         @return:
         """
        for cur_art_reg in self.__all_articles_regular:
            # pulling the article link
            article_reg_link = cur_art_reg.get_attribute('href').strip()
            self.__all_links.append(article_reg_link)

    def __pull_article_img(self):
        """
         update all the links of image type article
         @return:
         """
        for cur_art_img in self.__all_articles_img:
            # pulling the article link
            article_img_link = self.__pull_news_img_link(cur_art_img)
            self.__all_links.append(article_img_link)

    def __pull_news_img_link(self, cur_art: WebElement):
        """
        extract the link from the web element by selector
        @param cur_art: web element of article block
        @return: the link of the article
        """
        # get the link
        reel_link = cur_art.find_element(By.CSS_SELECTOR,'a[class="reel__link"]')
        link = reel_link.get_attribute('href').strip()
        return link
