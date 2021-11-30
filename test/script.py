import json
from datetime import Datetime
from image import Image
from info import Info
from country import Country
from state import State
from city import City
from address import Address
from venue import Venue
from event import Event


def consolidate_json(path, filenames):
    pass
    agg_list = []
    for filename in filenames:
        with open(f"{path}{filename}.json", "r") as f:
            data = json.load(f)
        agg_list += data

    with open(f"{path}consolidated.json", "w") as f:
        json.dump(agg_list, f)

    return agg_list


def create_fixtures(fixture_models, filenames):
    for model in fixture_models:
        model.


def main():
    models = [
        "datetime",
        "image",
        "info",
        "country",
        "state",
        "city",
        "address",
        "venue",
        "event"
    ]

    parsed_names = [
        "parsed_json_0",
        "parsed_json_1",
        "parsed_json_2",
        "parsed_json_3",
        "parsed_json_4"
    ]

    cached_file = __file__.replace("script.py", "cache/consolidated.json")

    with open(cached_file, "r") as f:
        data = json.load(f)

    fixture_models = {
        "datetime": Datetime(data),
        "image": Image(data),
        "info": Info(data),
        "country": Country(data),
        "state": State(data),
        "city": City(data),
        "address": Address(data),
        "venue": Venue(data),
        "event": Event(data)
    }

    create_fixtures(fixture_models, fixture_models.keys())

    # parsed_events = consolidate_json(cache_path, parsed_names)
    # fixture_data = consolidate_json("fixtures/", models.keys())


if __name__ == "__main__":
    main()
