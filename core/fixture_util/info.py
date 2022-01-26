from fixture import Fixture
import json


class Info:

    model = "app.Info"

    def __init__(self, data):
        self.fixtures = []

        # Populate infos set with info fields 
        infos = set()
        for element in data:
            fields = element.get("info")
            info_keys = tuple(fields)
            info_values = tuple(fields.values())
            info = (info_keys, info_values)
            infos.add(info)

        # also appends to a list-of-dict structure
        unique_infos = []
        for info in infos:
            unique_info = dict(zip(*info))
            unique_infos.append(unique_info)

        # assigning primary key 
        for i, fields in enumerate(unique_infos):
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
            raise Exception(f"Could not find in info")
        
        return fk


def main():
    filename = __file__.replace("fixture_util/info.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    info_fixtures = Info(data)
    for fixture in info_fixtures:
        print(fixture.get_fixture())
    

if __name__ == "__main__":
    main()
