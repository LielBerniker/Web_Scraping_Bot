from News_Web_Scraping.Web_Scraping_Bots.Web_scrape_flights.Flights_web_scrape_bot import Flights_web_scrape_bot
from News_Web_Scraping.Web_Scraping_Bots.Web_scrape_bbc.BBC_web_scrape_bot import BBC_web_scrape_bot
if __name__ == '__main__':
    bbc = Flights_web_scrape_bot()
    bbc.search_in_flights("am")
