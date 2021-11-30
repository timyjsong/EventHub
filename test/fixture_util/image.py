from fixture import Fixture
import json


class Image:

    model = "app.Image"

    def __init__(self, data):
        self.fixtures = []

        # Populate images set with image fields 
        images = set()
        for element in data:
            fields = element.get("image")
            image_keys = tuple(fields)
            image_values = tuple(fields.values())
            image = (image_keys, image_values)
            images.add(image)

        # also appends to a list-of-dict structure
        unique_images = []
        for image in images:
            unique_image = dict(zip(*image))
            unique_images.append(unique_image)

        # assigning primary key 
        for i, fields in enumerate(unique_images):
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
            raise Exception(f"Could not find in image")
        
        return fk


def main():
    filename = __file__.replace("fixture_util/image.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    image_fixtures = Image(data)
    for fixture in image_fixtures:
        print(fixture.get_fixture())
    

if __name__ == "__main__":
    main()
