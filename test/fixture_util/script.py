import os
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


def consolidate_json(path):
    agg_list = []

    for i in range(5):
        with open(f"{path}parsed_json_{i}.json", "r") as f:
            data = json.load(f)
        agg_list += data

    with open(f"{path}consolidated_new.json", "w") as f:
        json.dump(agg_list, f)

    return agg_list


def create_fixtures(fixtures_path, fixture_models):
    if not os.path.exists(fixtures_path):
        os.makedirs(fixtures_path, exist_ok=True)

    consolidated_fixtures = []
    for model in fixture_models:
        print(model)
        fixtures = fixture_models.get(model).fixtures

        fixture_list = [fixture.get_fixture() for fixture in fixtures]
        with open(f"{fixtures_path}{model}.json", "w") as f:
            json.dump(fixture_list, f)
        consolidated_fixtures += fixture_list

    with open(f"{fixtures_path}consolidated.json", "w") as f:
        json.dump(consolidated_fixtures, f)


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

    file_path = __file__.replace(
        "fixture_util/script.py", "cache/")
    # creates a consolidated json file and returns the contents
    consolidate_json(file_path)

    filename = __file__.replace("fixture_util/script.py", "cache/consolidated.json")

    with open(filename, "r") as f:
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

    fixtures_path = __file__.replace('fixture_util/script.py', 'fixtures/')
    create_fixtures(fixtures_path, fixture_models)
    

    # fixture_data = consolidate_json("fixtures/", models.keys())


if __name__ == "__main__":
    main()
