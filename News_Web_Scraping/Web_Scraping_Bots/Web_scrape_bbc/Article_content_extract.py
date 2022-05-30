import json
from selenium.webdriver.remote.webdriver import WebDriver
import News_Web_Scraping.Web_Scraping_Bots.Constants as Const
import os
import re
from selenium.webdriver.common.by import By
from News_Web_Scraping.Web_Scraping_Bots.Web_scrape_bbc.Article_information import Article_information

"""
this class extracts an articles content 
and update the articles storage of articles json files, if needed
"""


class Article_content_extract:
    def __init__(self, article_link, driver: WebDriver):
        self.__cur_driver = driver
        # article object
        self.__article_info = Article_information(driver.title.strip(), article_link)
        self.__remove_unnecessary_letters_from_name()

    def update_article_storage(self):
        """
        determine witch type of article the current article is,
        then extract the content of the article
        @return:
        """
        # first check if the article not already exist
        if not self.__article_exist():
            if self.__article_info.name.endswith('BBC Reel'):
                return
            elif self.__article_info.name.endswith('BBC Sport'):
                self.__extract_article_content_sport()
            elif self.__article_info.name.endswith('BBC Food'):
                self.__extract_article_content_food()
            elif self.__article_info.name.endswith('BBC News'):
                self.__extract_article_content_news()
            elif self.__article_info.name.endswith('BBC Culture') or self.__article_info.name.endswith(
                    'BBC Travel') or self.__article_info.name.endswith('BBC Future') or self.__article_info.name.endswith(
                'Worklife'):
                self.__extract_article_content_general()
            else:
                self.__extract_article_content_none()

    def __article_exist(self):
        """
        checks if the article not already exist
        @return: True if the the article have a json file by name, False o.w.
        """
        path = Const.ARTICLES_PATH + self.__article_info.name + ".json"
        if os.path.isfile(path) and os.access(path, os.R_OK):
            # checks if file exists and if it is a proper file
            return True
        else:
            return False

    def __extract_article_content_news(self):
        """
        extract the content of article of type news
        @return:
        """
        all_content = ""
        all_content_blocks = self.__cur_driver.find_elements(By.CSS_SELECTOR,
                                                             'p[class^="ssrcss-1q0x1qg-Paragraph"]')
        for cur_block in all_content_blocks:
            cur_text = cur_block.get_attribute("innerText")
            all_content += cur_text + " "
        self.__article_info.content = all_content
        self.__write_to_json()

    def __extract_article_content_food(self):
        """
        extract the content of article of type food
        @return:
        """
        all_content = ""
        all_content_blocks = self.__cur_driver.find_elements(By.CSS_SELECTOR,
                                                             'p[class="blocks-text-block__paragraph"]')
        for cur_block in all_content_blocks:
            cur_text = cur_block.get_attribute("innerText")
            all_content += cur_text + " "
        self.__article_info.content = all_content
        self.__write_to_json()

    def __extract_article_content_sport(self):
        """
        extract the content of article of type sport
        @return:
        """
        # get only articles not live updates - live -
        n = re.findall(" - ", self.__article_info.name)
        if len(n) > 1:
            return
        all_content = ""
        all_content_blocks_p = self.__cur_driver.find_elements(By.CSS_SELECTOR, 'p[data-reactid*="paragraph"]')
        for cur_block_p in all_content_blocks_p:
            all_content += cur_block_p.get_attribute('innerText') + " "
        self.__article_info.content = all_content
        self.__write_to_json()

    def __extract_article_content_general(self):
        """
        extract the content of article of general type
        @return:
        """
        all_content = ""
        all_content_blocks = self.__cur_driver.find_elements(By.CSS_SELECTOR,
                                                             'div[class="body-text-card b-reith-sans-font"]')
        for cur_block in all_content_blocks:
            all_p = cur_block.find_elements(By.TAG_NAME, 'p')
            for cur_p in all_p:
                all_content += cur_p.get_attribute('innerText') + " "
        self.__article_info.content = all_content
        self.__write_to_json()

    def __extract_article_content_none(self):
        """
        extract the content of article that the type of the article is not specified
        @return:
        """
        all_content = ""
        all_content_blocks = self.__cur_driver.find_elements(By.TAG_NAME,
                                                             'p')
        for cur_block in all_content_blocks:
            all_content += cur_block.get_attribute('innerText')
        self.__article_info.content = all_content
        self.__write_to_json()

    def __write_to_json(self):
        """
        create a json object to the article and save it in the proper directory
        @return:
        """
        self.__article_info.content = self.__article_info.content.lower()
        json_obj_style = {
            "name": self.__article_info.name,
            "link": self.__article_info.link,
            "content": self.__article_info.content
        }
        # Serializing json
        json_object = json.dumps(json_obj_style)
        # Writing to sample.json

        file_name = self.__article_info.name + ".json"
        file_full_path = Const.ARTICLES_PATH + file_name
        try:
            with open(file_full_path, "w") as outfile:
                outfile.write(json_object)
        except:
            pass

    def __remove_unnecessary_letters_from_name(self):
        """
        fix the article name , by remove all letters that my cause problem in the file create process
        @return:
        """
        article_name = self.__article_info.name
        article_name = article_name.replace(':', '')
        article_name = article_name.replace('?', '')
        article_name = article_name.replace('*', '')
        article_name = article_name.replace('<', '')
        article_name = article_name.replace('>', '')
        article_name = article_name.replace('\\', '')
        article_name = article_name.replace('/', '')
        article_name = article_name.replace('|', '')
        article_name = article_name.replace('"', '')
        article_name = article_name.replace("'", "")
        article_name = article_name.replace('\n', "")
        self.__article_info.name = article_name
