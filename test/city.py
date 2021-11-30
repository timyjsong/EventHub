from fixture import Fixture
from state import State
import json


class City:

    model = "app.City"

    def __init__(self, data):
        self.fixtures = []

        state_fixtures = State(data)

        # Populate countries set with country fields data
        cities = set()
        for element in data:
            fields = element.get("city")
            state_fields = element.get("state") # why does this include country key?

            fields["state_code"] = state_fields.get("state_code")
            fields["state_key"] = state_fixtures.find(state_fields)
            fields["country_code"] = state_fields.get("country_code")

            city_keys = tuple(fields)
            city_values = tuple(fields.values())
            city = (city_keys, city_values)
            cities.add(city)

        # to get unique items only - isn't this redundant bc its already a set?
        # also appends to a list-of-dict structure
        unique_cities = []
        for city in cities:
            unique_city = dict(zip(*city))
            unique_cities.append(unique_city)

        # assigning primary key
        for i, fields in enumerate(unique_cities):
            pk = i + 1
            fixture = Fixture(self.model, pk, fields)
            self.fixtures.append(fixture)

    def __iter__(self):
        for fixture in self.fixtures:
            yield fixture

    def find(self, fields):
        for fixture in self:
            if fixture.fields == fields:
                fk = fixture.pk
                break
        else:
            raise Exception(f"Could not find in Cities")
        
        return fk


def main():
    filename = __file__.replace("city.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    city_fixtures = City(data)
    for fixture in city_fixtures:
        print(fixture.get_fixture())


if __name__ == "__main__":
    main()
