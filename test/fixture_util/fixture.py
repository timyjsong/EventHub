
class Fixture:

    def __init__(self, model, pk, fields):
        self.model = model
        self.pk = pk
        self.fields = fields

    def get_fixture(self):
        return {
            "model": self.model,
            "pk": self.pk,
            "fields": self.fields
        }


# DIR_PATH = __file__.replace("fixture_util/fixture.py", "cache/consolidated.json")


def main():

    pass


if __name__ == "__main__":
    main()
