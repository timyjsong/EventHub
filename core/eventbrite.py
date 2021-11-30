""" Module for EventHub """

import json

from bs4 import BeautifulSoup
import requests

from logger import LOGGER

LOGGER = LOGGER.get_logger("eventbrite")


def main():
#     for i in range(100000):
#         print(i)
#         url = f"https://www.eventbriteapi.com/v3/events/{i}/teams/"
#         headers = {"Authorization": "Bearer CQCEREOAHXNRKCQGUDQO"}
#         r = requests.get(url, headers=headers)
#         if "NOT_FOUND" not in r.text:
#             print(f"event id: {i}")
#             break

#     url = "https://www.eventbrite.com/d/ma--boston/music--events/boston/?page=1"
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, "lxml")
#     script = soup.findAll("script")[-1]
#     json_data = json.loads(script.text.strip())
#     print(json.dumps(json_data))
#

#     url = "https://www.eventbrite.com/e/halloween-night-at-hava-10-31-21-tickets-177691137977"

#     url = "https://www.eventbrite.com/e/audien-at-royale-102921-1000-pm-21-tickets-170761882387?aff=ebdssbdestsearch"
#     r = requests.get(url)

#     soup = BeautifulSoup(r.text, "lxml")
#     data = None
#     for script in soup.findAll("script"):
#         if script.attrs.get("type") == "application/ld+json":
#             data = json.loads(script.text.strip())
#             break
#     print(json.dumps(data))

    pass


if __name__ == "__main__":
    main()
