from fixture import Fixture
from city import City
import json


class Address:

    model = "app.Address"

    def __init__(self, data):
        self.fixtures = []

        city_fixtures = City(data)

        # Populate countries set with country fields data
        addresses = set()
        for element in data:
            fields = element.get("address")
            city_fields = element.get("city") # why does this include city key?

            fields["city_name"] = city_fields.get("city_name")
            fields["city_key"] = city_fixtures.find(city_fields)
            fields["state_code"] = city_fields.get("state_code")
            fields["country_code"] = city_fields.get("country_code")

            address_keys = tuple(fields)
            address_values = tuple(fields.values())
            address = (address_keys, address_values)
            addresses.add(address)

        # to get unique items only - isn't this redundant bc its already a set?
        # also appends to a list-of-dict structure
        unique_addresses = []
        for address in addresses:
            unique_address = dict(zip(*address))
            unique_addresses.append(unique_address)

        # assigning primary key
        for i, fields in enumerate(unique_addresses):
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
            raise Exception(f"Could not find in Addresses")
        
        return fk


def main():
    filename = __file__.replace("address.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    address_fixtures = Address(data)
    for fixture in address_fixtures:
        print(fixture.get_fixture())


if __name__ == "__main__":
    main()
