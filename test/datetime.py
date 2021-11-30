from fixture import Fixture
import json


class Datetime:

    model = "app.Datetime"

    def __init__(self, data):
        self.fixtures = []

        # Populate datetimes set with datetime fields 
        datetimes = set()
        for element in data:
            fields = element.get("datetime")
            datetime_keys = tuple(fields)
            datetime_values = tuple(fields.values())
            datetime = (datetime_keys, datetime_values)
            datetimes.add(datetime)

        # also appends to a list-of-dict structure
        unique_datetimes = []
        for datetime in datetimes:
            unique_datetime = dict(zip(*datetime))
            unique_datetimes.append(unique_datetime)

        # assigning primary key 
        for i, fields in enumerate(unique_datetimes):
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
            raise Exception(f"Could not find in datetime")
        
        return fk


def main():
    filename = __file__.replace("datetime.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    datetime_fixtures = Datetime(data)
    for fixture in datetime_fixtures:
        print(fixture.get_fixture())
    

if __name__ == "__main__":
    main()
