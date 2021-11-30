from fixture import Fixture
import json


class Country:

    model = "app.Country"

    def __init__(self, data):
        self.fixtures = []

        # Populate countries set with country fields data
        countries = set()
        for element in data:
            fields = element.get("country")
            country_keys = tuple(fields)
            country_values = tuple(fields.values())
            country = (country_keys, country_values)
            countries.add(country)

        # to get unique items only - isn't this redundant bc its already a set?
        unique_countries = []
        for country in countries:
            unique_country = dict(zip(*country))
            unique_countries.append(unique_country)

        for i, fields in enumerate(unique_countries):
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
            raise Exception(f"Could not find {fields} in Country")
        
        return fk


def main():
    filename = __file__.replace("fixture_util/country.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    country_fixtures = Country(data)
    for fixture in country_fixtures:
        print(fixture.get_fixture())


if __name__ == "__main__":
    main()
