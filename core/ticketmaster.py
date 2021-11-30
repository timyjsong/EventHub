""" Module for EventHub """

import os
import shutil
import json
from argparse import ArgumentParser

import requests

from logger import LOGGER
from config import TICKETMASTER_API_KEY

LOGGER = LOGGER.get_logger("ticketmaster")
DIRPATH = "cache"


def cache_loader(url, filename, params=None):
    """ cache loader"""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        LOGGER.debug(f"Cache miss: {url}, creating {filename}")
        os.makedirs(DIRPATH, exist_ok=True)
        data = requests.get(url, params=params).json()
        with open(filename, "w") as f:
            json.dump(data, f)
        return data
    else:
        LOGGER.debug(f"Cache hit: {filename}")

    return data


def get_largest_image(images):
    largest_area = 0
    largest_index = 0

    for index, image in enumerate(images):
        width = int(image["width"])
        height = int(image["height"])
        area = width * height
        if area >= largest_area:
            largest_area = area
            largest_index = index

    return largest_index


def main(args):
    if args.reload is True:
        LOGGER.debug(f"Wiping Cache")
        shutil.rmtree(DIRPATH)

    for i in range(5):
        LOGGER.info(i)
        url = "https://app.ticketmaster.com/discovery/v2/events.json"
        params = {
            "classificationName": "music",
            "stateCode": "MA",
            "size": "200",
            "page": i,
            "apikey": "j1VmyKjOQxiSg8utJFq8A0nQ4uEJ4T8J"
        }

        filename = f"{DIRPATH}/ticketmaster_data_{i}.json"
        data = cache_loader(url, filename, params=params)

        embedded = data.get("_embedded")

        events = []
        for ii, event in enumerate(embedded.get("events")):

            LOGGER.debug(f"Page: {i}, Event: {ii}")

            event_name = event["name"]
            event_url = event["url"]

            images = event["images"]
            image_index = get_largest_image(images)
            image = images[image_index]
            image_url = image["url"]
            image_width = image["width"]
            image_height = image["height"]

            # Data relating to dates
            dates_data = event["dates"]
            local_start_date = dates_data["start"].get("localDate", "N/A")
            local_start_time = dates_data["start"].get("localTime", "N/A")
            timezone = dates_data.get("timezone", "N/A")

            # Information about event
            info = event.get("info", "N/A")
            please_note = event.get("pleaseNote", "N/A")

            legal_age_enforced = False
            if event.get("ageRestrictions"):
                legal_age_enforced = event["ageRestrictions"]["legalAgeEnforced"]

            # Data relating to the venue
            venue_data = event["_embedded"]["venues"][0]
            venue_name = venue_data["name"] 
            venue_url = venue_data.get("url", "N/A")
            venue_city = venue_data["city"]["name"]
            venue_state = venue_data["state"]["name"]
            venue_state_code = venue_data["state"]["stateCode"]
            venue_country_name = venue_data["country"]["name"]
            venue_country_code = venue_data["country"]["countryCode"]
            venue_address = venue_data["address"]["line1"] # potential multiple lines
            venue_location_longitude = venue_data["location"]["longitude"]
            venue_location_latitude = venue_data["location"]["latitude"]
            venue_parking_detail = venue_data.get("parkingDetail", "N/A")
            venue_accessible_seating = venue_data.get("accessibleSeatingDetail", "N/A") # not in all iterations

            venue_general_rule = "N/A"
            if venue_data.get("generalInfo"):
                venue_general_rule = venue_data["generalInfo"].get("generalRule", "N/A")

            _event = {
                "event": { 
                    "event_name": event_name,
                    "event_url": event_url
                },
                "image": {
                    "image_url": image_url,
                    "image_width": image_width,
                    "image_height": image_height 
                },
                "datetime": {
                    "local_start_date": local_start_date,
                    "local_start_time": local_start_time,
                    "timezone": timezone
                },
                "info": {
                    "please_note": please_note,
                    "legal_age_enforced": legal_age_enforced
                },
                "venue": {
                    "venue_name": venue_name,
                    "venue_url": venue_url,
                    "venue_parking_detail": venue_parking_detail,
                    "venue_accessible_seating": venue_accessible_seating,
                    "venue_general_rule": venue_general_rule
                },
                "address": {
                    "address_name": venue_address,
                    "longitude": venue_location_longitude,
                    "latitude": venue_location_latitude
                },
                "city": {
                    "city_name": venue_city
                },
                "state": {
                    "state_name": venue_state,
                    "state_code": venue_state_code
                },
                "country": {
                    "country_name": venue_country_name,
                    "country_code": venue_country_code
                }
            }

            events.append(_event)

        outfile = f"cache/parsed_json_{i}.json"
        with open(outfile, "w") as f:
            json.dump(events, f)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-r", "--reload", action="store_true", help="force reloading cache")
    args = parser.parse_args()
    main(args)
