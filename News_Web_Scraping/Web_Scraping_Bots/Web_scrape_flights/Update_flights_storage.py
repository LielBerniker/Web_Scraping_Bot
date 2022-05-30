import json
import News_Web_Scraping.Web_Scraping_Bots.Constants as Const

"""
this class creates json files and save them in the proper directory by flight type 
"""


class Update_flights_storage:
    def __init__(self, flights_info, flight_type):
        self.__flights_info = flights_info
        self.__flight_type = flight_type
        # creates json by the type of flight
        if flight_type == "arrivel":
            for flight_info in self.__flights_info:
                self.__create_arriv_json(flight_info)
        else:
            for flight_info in self.__flights_info:
                self.__create_depart_json(flight_info)

    def __create_arriv_json(self, flight_info):
        """
        create a json to flight type arrival
        then save the json
        @param flight_info: contain information of flight
        @return:
        """
        json_obj_style = {
            "airline": flight_info.airline.lower(),
            "status": flight_info.status,
            "land_from": flight_info.land_from,
            "flight_num": flight_info.flight_num,
            "terminal": flight_info.terminal,
            "schedule_time": flight_info.schedule_time,
            "updated_time": flight_info.updated_time
        }
        # Serializing json
        # path to dir
        json_object = json.dumps(json_obj_style)
        dir_path = Const.FLIGHTS_ARRIVE_PATH
        self.__file_create(dir_path, flight_info.flight_num, json_object)

    def __create_depart_json(self, flight_info):
        """
        create a json to flight type departure
        then save the json
        @param flight_info: contain information of flight
        @return:
        """
        json_obj_style = {
            "airline": flight_info.airline.lower(),
            "status": flight_info.status,
            "land_from": flight_info.land_from,
            "flight_num": flight_info.flight_num,
            "terminal": flight_info.terminal,
            "schedule_time": flight_info.schedule_time,
            "updated_time": flight_info.updated_time,
            "counter": flight_info.counter
        }
        # Serializing json
        # path to dir
        json_object = json.dumps(json_obj_style)
        dir_path = Const.FLIGHTS_DEPARTURES_PATH
        self.__file_create(dir_path, flight_info.flight_num, json_object)

    def __file_create(self, dir_path, flight_num, json_object):
        """
        save json
        @param dir_path: the path to the wright directory
        @param flight_num: flight number
        @param json_object: the json object of the current flight
        @return:
        """
        # Writing to sample.json
        file_name = flight_num + ".json"
        file_full_path = dir_path + file_name
        with open(file_full_path, "w") as outfile:
            outfile.write(json_object)
