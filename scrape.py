#!/usr/bin/env python3

from time import sleep
import requests
from bs4 import BeautifulSoup as bs4
import json


from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_boats():

    r = requests.get("http://bluewaterboats.org/")
    soup = bs4(r.content, features="html.parser")

    # this finds the href instances that have the boat name in name-feet format eg vega-88
    list_of_boats = []
    for link in soup.find_all("a"):
        list_of_boats.append(link.get("href")[1:])

    # we swap the "-"s for "+"s ready for feeding into a search url
    formatted_list_of_boats = []
    for boat in list_of_boats:
        formatted_boat = boat.replace("-", "+")
        formatted_list_of_boats.append(formatted_boat)

    # there were multiple results matching the same boat, so we find the unique ones here
    unique_formatted_list_of_boats = []
    for boat in formatted_list_of_boats:
        if boat not in unique_formatted_list_of_boats:
            unique_formatted_list_of_boats.append(boat)

    # and strip of the leading entry, its always null for some reason.
    del unique_formatted_list_of_boats[0]

    boats_json = {}
    for item in unique_formatted_list_of_boats:
        boats_json.update(
            {
                item.replace(
                    "+", " "
                ): "https://www.gumtree.com.au/s-sail-boats/{}/k0c20028r10".format(item)
            }
        )

    # return a list in the format ["vega+88","vega+99"]
    return boats_json


def write_boats(boats):

    with open("got_boats.json", "w") as outfile:
        outfile.write(json.dumps(boats))


def main():

    while True:
        boats = get_boats()
        write_boats(boats)

        # run this once a day
        sleep(86400)


if __name__ == "__main__":
    main()
