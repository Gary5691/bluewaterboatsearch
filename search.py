#!/usr/bin/env python3

from time import sleep
import json
import requests
from bs4 import BeautifulSoup as bs4

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def search_boats(boats):

    with open("templates/search_boats.html", "w") as outfile:
        for boat in boats:
            r = requests.get(boats[boat])
            soup = bs4(r.content, features="html.parser")
            result = soup.find_all("h1")
            results_list = []
            for i in result:
                results_list.append(i.get_text(strip=True))
            if "0 Results" in results_list[0]:
                pass
            else:
                outfile.write(
                    f'Searched for <b>{boat}</b> and found <a href="{boats[boat]}" target="_blank" style="target-new: tab;">{boats[boat]}</a><p>'
                )


def read_boats():

    with open("got_boats.json", "r") as infile:
        boats = json.load(infile)
        return boats


def main():

    while True:

        # introduce a delay to avoid trying to read got_boats.json while its locked for writing
        # sleep(300)

        boats = read_boats()
        search_boats(boats)

        # get new search results every hour.
        sleep(3600)


if __name__ == "__main__":
    main()
