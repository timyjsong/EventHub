from fixture import Fixture
from country import Country
import json


class State:

    model = "app.State"

    def __init__(self, data):
        self.fixtures = []

        country_fixtures = Country(data)

        # Populate countries set with country fields data
        states = set()
        for element in data:
            fields = element.get("state")
            country_fields = element.get("country")

            fields["country_code"] = country_fields.get("country_code")
            fields["country_key"] = country_fixtures.find(country_fields)

            state_keys = tuple(fields)
            state_values = tuple(fields.values())
            state = (state_keys, state_values)
            states.add(state)

        # to get unique items only - isn't this redundant bc its already a set?
        # also appends to a list-of-dict structure
        unique_states = []
        for state in states:
            unique_state = dict(zip(*state))
            unique_states.append(unique_state)

        # assigning primary key
        for i, fields in enumerate(unique_states):
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
            raise Exception(f"Could not find in States")
        
        return fk


def main():
    filename = __file__.replace("fixture_util/state.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    state_fixtures = State(data)
    for fixture in state_fixtures:
        print(fixture.get_fixture())


if __name__ == "__main__":
    main()
