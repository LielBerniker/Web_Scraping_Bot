import os
import json
import glob
import Web_Scraping_Bots.Constants as Const
from prettytable import PrettyTable

"""
this class collect all the articles that contain the words the user inserted,
then print the name and link for all the articles in a table
"""


class Article_search():
    def __init__(self,text_words):
        self.__text_words = text_words
        self.__articles_list = []
        self.__search_articles()

    def __search_articles(self):
        """
        the function find all the articles in the json file ,
        that contain some of the words in search in their content
        @return:
        """
        size = len(self.__text_words)
        path = Const.ARTICLES_DIR_PATH
        for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
            with open(filename, encoding='utf-8', mode='r') as currentFile:
                json_data = json.loads(currentFile.read())
                cur_content = json_data["content"]
                if self.__article_text_check(cur_content,size):
                    article_info = [json_data["name"],json_data["link"]]
                    self.__articles_list.append(article_info)
        self.__show_data_in_table()

    def __article_text_check(self, cur_content,size):
        """
        find if the content contain attlist half of the words in search
        @param cur_content: the current content
               size: number of words to search
        @return: True if this content contain attlist half of the words in search
        , False o.w.
        """
        counter = 0
        for word in self.__text_words:
            if word in cur_content:
                counter += 1
        if size == 1:
            if counter>0:
                return True
            else:
                return False
        else:
            if counter >= (len(self.__text_words) // 2):
                return True
            else:
                return False

    def __show_data_in_table(self):
        """
        print all the articles that contain the search words
        @return:
        """
        table = PrettyTable(field_names=["Article Name", "Article Link"])
        table.add_rows(self.__articles_list)
        print(table)
