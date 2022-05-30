from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from News_Web_Scraping.Web_Scraping_Bots.Web_scrape_flights.Extract_and_updtae_flights import Extract_and_update_flights
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
this class extract all the arrival and departure flights data ,
and save all the data in to json files
"""


class Extract_flights_table:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__get_tables_data()

    def __get_tables_data(self):
        """
        extract all rows that contain information about arrival flights ,
        then go to departure flights and do the same
        @return:
        """
        flight_type1 = "arrivel"
        self.__get_arrivel_table()
        Extract_and_update_flights(flight_type1, self.__driver)
        flight_type2 = "depart"
        self.__get_departures_table()
        Extract_and_update_flights(flight_type2, self.__driver)

    def __get_arrivel_table(self):
        """
        the function click the next button until the full table of arrival flights is shown
        then click the cancel automatic update,
        its imported that we can extract the information without that the web elements will change.
        then save all the flight information in to json files
        @return:
        """
        button_next = self.__driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
        style_state = button_next.get_attribute("style")
        while style_state is "":
            button_next.click()
            button_next = self.__driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
            style_state = button_next.get_attribute("style")
        # cancel automatic update
        button_update = self.__driver.find_element(By.CSS_SELECTOR, 'a[id="toggleAutoUpdate"][role="button"]')
        button_update.click()

    def __get_departures_table(self):
        """
         first the function click a button to go to the departure flights table,
         then it clicks the next button until the full table of departure flights is shown
         then save all the flight information in to json files
         @return:
         """
        # button to go to departure table
        button_deap = self.__driver.find_element(By.CSS_SELECTOR, 'a[id="tab--departures_flights-label"]')
        button_deap.click()
        # wait until the next button is available
        element1 = WebDriverWait(self.__driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="next"][type="button"]')))
        button_next = self.__driver.find_element(By.CSS_SELECTOR, 'button[id="next"][type="button"]')
        style_state = button_next.get_attribute("style")
        while style_state is "":
            button_next.click()
            button_next = self.__driver.find_element(By.CSS_SELECTOR, 'button[id="next"]')
            style_state = button_next.get_attribute("style")
