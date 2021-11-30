from fixture import Fixture
from address import Address
import json


class Venue:

    model = "app.Venue"

    def __init__(self, data):
        self.fixtures = []

        address_fixtures = Address(data)

        # Populate countries set with country fields data
        venues = set()
        for element in data:
            fields = element.get("venue")
            address_fields = element.get("address") # why does this include city key?

            fields["address_name"] = address_fields.get("city_name")
            fields["address_key"] = address_fixtures.find(address_fields)
            fields["city_name"] = address_fields.get("city_name")
            fields["state_code"] = address_fields.get("state_code")
            fields["country_code"] = address_fields.get("country_code")

            venue_keys = tuple(fields)
            venue_values = tuple(fields.values())
            venue = (venue_keys, venue_values)
            venues.add(venue)

        # to get unique items only - isn't this redundant bc its already a set?
        # also appends to a list-of-dict structure
        unique_venues = []
        for venue in venues:
            unique_venue = dict(zip(*venue))
            unique_venues.append(unique_venue)

        # assigning primary key 
        for i, fields in enumerate(unique_venues):
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
            raise Exception(f"Could not find in Venues")
        
        return fk


def main():
    filename = __file__.replace("fixture_util/venue.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    venue_fixtures = Venue(data)
    for fixture in venue_fixtures:
        print(fixture.get_fixture())
        break


if __name__ == "__main__":
    main()
