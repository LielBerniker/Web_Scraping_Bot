class FLIGHTS_BOT:
    """This abstract class represents an bot that
    used to web scraping the ben gurion airport flights information web page."""

    def update_flight_storage(self):
        """
        update all flight information ,
        only if we didn't have the most updated data of flights information
        @return:
        """

    def search_in_flights(self, search_text: str):
        """
        search the text in all of the flights
        and print the flights that contain any word of the text
        @param search_text: string that the user insert ,for search in the flights
        @return:
        """
