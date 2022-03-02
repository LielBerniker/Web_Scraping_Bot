from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
import os, shutil
import Web_Scraping_Bots.Constants as Const
from Web_Scraping_Bots.Web_scrape_flights.Flight_arriv_information import Flight_arriv_information
from Web_Scraping_Bots.Web_scrape_flights.Flight_depart_information import Flight_depart_information
from Web_Scraping_Bots.Web_scrape_flights.Update_flights_storage import Update_flights_storage
import time
from selenium.webdriver.common.by import By
"""
this class update the json files of flights depend on the flight type , arrival or departure.
extract all the data about the flight and store it as json files.
"""


class Extract_and_update_flights:
    def __init__(self, flight_type,driver:WebDriver):
        self.__driver = driver
        self.__all_flights=[]
        # extract the data about the flight depends on the flight type
        if flight_type == "arrivel":
            self.__empty_dir(Const.FLIGHTS_ARRIVE_DIR_PATH)
            time.sleep(0.4)
            self.__get_arrivel_data()
            Update_flights_storage(self.__all_flights,flight_type)
        else:
            self.__empty_dir(Const.FLIGHTS_DEPARTURES_DIR_PATH)
            time.sleep(0.4)
            self.__get_departures_data()
            Update_flights_storage(self.__all_flights, flight_type)

    def __get_arrivel_data(self):
        """
        go over all the flights and extract the information from each one
        @return:
        """
        arriv_table_rows = self.__driver.find_elements(By.CSS_SELECTOR,'tr[class^="flight_row"]')
        for row in arriv_table_rows:
            self.__get_arrivel_row_data(row)

    def __get_departures_data(self):
        """
        go over all the flights and extract the information from each one
        @return:
        """
        depart_table_rows = self.__driver.find_element(By.CSS_SELECTOR,'table[id="flight_board-departures_table"]')
        rows = depart_table_rows.find_elements(By.CSS_SELECTOR,'tr[role="row"][class^="flight_row"]')
        for row in rows:
            self.__get_departures_row_data(row)

    def __get_arrivel_row_data(self, cur_row: WebElement):
        """
        extract the information of the specific arrival flight
        @param cur_row: current row of information about flight
        @return: True if the save was successful, False o.w.
        """
        flight_info = Flight_arriv_information()
        flight_info.airline = self.__get_airline(cur_row)
        flight_info.flight_num = self.__get_flight_num(cur_row)
        flight_info.status = self.__get_status(cur_row)
        flight_info.land_from = self.__get_land(cur_row)
        flight_info.terminal = self.__get_terminal(cur_row)
        flight_info.schedule_time = self.__get_schedule(cur_row)
        flight_info.updated_time = self.__get_updated_time(cur_row)
        self.__all_flights.append(flight_info)

    def __get_departures_row_data(self, cur_row: WebElement):
        """
        extract the information of the specific departure flight
        @param cur_row: current row of information about flight
        @return: True if the save was successful, False o.w.
        """
        flight_info = Flight_depart_information()
        flight_info.airline = self.__get_airline(cur_row)
        flight_info.flight_num = self.__get_flight_num(cur_row)
        flight_info.status = self.__get_status(cur_row)
        flight_info.land_from = self.__get_land(cur_row)
        flight_info.terminal = self.__get_terminal(cur_row)
        flight_info.schedule_time = self.__get_schedule(cur_row)
        flight_info.updated_time = self.__get_updated_time(cur_row)
        flight_info.counter = self.__get_counter(cur_row)
        self.__all_flights.append(flight_info)

    def __get_counter(self, cur_row: WebElement):
        """
        get the counter by selector
        @param cur_row: current row of the flight information
        @return: return the counters of the flight
        """
        counter_block = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-counter"]')
        counter = counter_block.get_attribute("innerText")
        return counter

    def __get_airline(self, cur_row: WebElement):
        """
         get the airline name by selector
         @param cur_row: current row of the flight information
         @return: return the airline name of the flight
         """
        airline_block = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-airline"]')
        airline = airline_block.get_attribute("innerText")
        return airline

    def __get_flight_num(self, cur_row: WebElement):
        """
         get the flight number by selector
         @param cur_row: current row of the flight information
         @return: return the flight number of the flight
         """
        flight_num = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-flight"]').get_attribute("innerText")
        return flight_num

    def __get_status(self, cur_row: WebElement):
        """
         get the flight status by selector
         @param cur_row: current row of the flight information
         @return: return the status of the flight
         """
        status = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-status"]').get_attribute("innerText")
        return status

    def __get_land(self, cur_row: WebElement):
        """
         get the country by selector
         @param cur_row: current row of the flight information
         @return: return the country of the flight
         """
        land = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-city"]').get_attribute("innerText")
        return land

    def __get_terminal(self, cur_row: WebElement):
        """
         get the terminal by selector
         @param cur_row: current row of the flight information
         @return: return the terminal of the flight
         """
        terminal = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-terminal"]').get_attribute("innerText")
        return terminal

    def __get_schedule(self, cur_row: WebElement):
        """
         get the schedule time by selector
         @param cur_row: current row of the flight information
         @return: return the schedule time of the flight
         """
        schedule_block = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-scheduledTime"]')
        time_schedule = schedule_block.find_element(By.TAG_NAME,'time')
        hour_schedule = time_schedule.find_element(By.TAG_NAME,'strong').get_attribute("innerText")
        date_schedule = time_schedule.find_element(By.TAG_NAME,'div').get_attribute("innerText")
        total_schedule = hour_schedule + " " + date_schedule
        return total_schedule

    def __get_updated_time(self, cur_row: WebElement):
        """
         get the updated time by selector
         @param cur_row: current row of the flight information
         @return: return the updated of the flight
         """
        updated_time = cur_row.find_element(By.CSS_SELECTOR,'div[class="td-updatedTime"]').get_attribute("innerText")
        return updated_time

    def __empty_dir(self, path):
        """
         the function delete all files from the directory
         @param path: path to a directory
         @return:
         """
        folder_path = path
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
