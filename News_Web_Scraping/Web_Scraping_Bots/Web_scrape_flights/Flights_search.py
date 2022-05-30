import os
import json
import glob
from prettytable import PrettyTable
import News_Web_Scraping.Web_Scraping_Bots.Constants as Const

"""
this class collect all the flights that contain the words the user inserted,
then print the information of the flights bt the table match to the flight type , arrival or departure
"""


class Flights_search():
    def __init__(self,search_list):
        self.__text_words = search_list
        self.__arriv_flights = []
        self.__depart_flights = []
        self.__search_flights()

    def __search_flights(self):
        """
        call functions that search in the json files for the flights that contain the text'
        then print the flights in tables
        @return:
        """
        self.__get_all_arriv_flights()
        self.__get_all_depart_flights()
        self.__show_arriv_in_table()
        self.__show_depart_in_table()

    def __get_all_arriv_flights(self):
        """
         go over all the json files in the flight arrival directory
         then get information only from the ones that contains some of the search text in one of their attributes
         @return:
         """
        path = Const.FLIGHTS_ARRIVE_DIR_PATH
        for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
            with open(filename, encoding='utf-8', mode='r') as currentFile:
                json_data = json.loads(currentFile.read())
                # get all the flight information
                flight_arriv_info = [json_data["airline"], json_data["status"], json_data["land_from"],
                                     json_data["flight_num"], json_data["terminal"], json_data["schedule_time"],
                                     json_data["updated_time"]]
                if self.__flight_text_check(flight_arriv_info):
                    self.__arriv_flights.append(flight_arriv_info)

    def __get_all_depart_flights(self):
        """
         go over all the json files in the flight departure directory
         then get information only from the ones that contains some of the search text in one of their attributes
         @return:
         """
        path = Const.FLIGHTS_DEPARTURES_DIR_PATH
        for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
            with open(filename, encoding='utf-8', mode='r') as currentFile:
                json_data = json.loads(currentFile.read())
                # get all the flight information
                flight_depart_info = [json_data["airline"], json_data["status"], json_data["land_from"],
                                      json_data["flight_num"], json_data["terminal"], json_data["schedule_time"],
                                      json_data["updated_time"], json_data["counter"]]
                if self.__flight_text_check(flight_depart_info):
                    self.__depart_flights.append(flight_depart_info)

    def __flight_text_check(self, cur_flight):
        """
        checks if the currnt contain any word from the search text in one of his attributes
        @param cur_flight: current flight information
        @return: True one of the flight fields contain one of the text word, False o.w.
        """
        for data in cur_flight:
            for word in self.__text_words:
                if word in data:
                    return True
            return False

    def __show_arriv_in_table(self):
        """
        print all the arrival flight that match the conditions in a table
        @return:
        """
        table = PrettyTable(
            field_names=["airline name", "     land_from     ", " status ", "flight_num", "terminal",
                         "schedule_time", "updated_time"
                         ])
        table.title = "ARRIVAL FLIGHTS"
        table.add_rows(self.__arriv_flights)
        print(table)

    def __show_depart_in_table(self):
        """
        print all the departure flight that match the conditions in a table
        @return:
        """
        table = PrettyTable(
            field_names=["airline name", "     land_in     ", " status ", "flight_num", "terminal",
                         "schedule_time", "updated_time","counter"
                         ])
        table.title = "DEPARTURE FLIGHTS"
        table.add_rows(self.__depart_flights)
        print(table)
