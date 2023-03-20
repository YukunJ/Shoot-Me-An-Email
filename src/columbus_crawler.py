"""
    Functionality for crawl IronState Columbus collection apartments in Jersey City only
"""
import requests
import time
from bs4 import BeautifulSoup
from emailer import Emailer


class ColumbusCrawler:

    def __init__(self, apartment_name: str, entry_url: str, emailer: Emailer = None, frequency: int = 300):
        self.apartment_name = apartment_name
        self.entry_url = entry_url
        self.frequency = frequency
        self.emailer = emailer
        self.last_seen = None

    def crawl(self) -> None:
        soup = BeautifulSoup(requests.get(self.entry_url).text, "html.parser")
        # extract out all available 1b1b units listing
        listings = soup.find_all("article", class_="floorplans-box active",
                                 attrs={"data-beds": "1", "data-baths": "1.00"})
        # concatenate date, price and space as the unique identification key for each unit
        this_seen = set()
        for listing in listings:
            details = listing.find_all("li")
            date = details[0].text
            price = details[1].text
            space = details[2].text
            key = date + " " + price + " " + space
            this_seen.add(key)
        # compare with last_seen, if any new unit appears, sends out notifications
        if (self.last_seen is not None):
            diff = self.last_seen.difference(this_seen)
            if (len(diff) > 0 and self.emailer is not None):
                email = "We find the following new units for " + self.apartment_name + "\n"
                email += " ".join(list(diff))
                self.emailer.broadcast_email(email)
        else:
            # first time crawl
            print("First time crawl. We see the following units available:")
            for key in this_seen:
                print(key)
        self.last_seen = this_seen

    def run(self) -> None:
        while True:
            self.crawl()
            time.sleep(self.frequency)

if __name__ == "__main__":
    emailer = Emailer()
    emailer.add_subscriber("yukunj.cs@gmail.com")
    cc = ColumbusCrawler("50-columbus", "https://ironstate.com/property/50-columbus/", emailer)
    cc.run()