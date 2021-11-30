from fixture import Fixture
from venue import Venue
from image import Image
from datetime import Datetime
from info import Info
import json


class Event:

    model = "app.Event"

    def __init__(self, data):
        self.fixtures = []

        # data gets transformed during this method call. why?
        venue_fixtures = Venue(data)
        image_fixtures = Image(data)
        datetime_fixtures = Datetime(data)
        info_fixtures = Info(data)

        # Populate events set with event fields data
        events = set()
        for element in data:
            fields = element.get("event")

            venue_fields = element.get("venue")
            image_fields = element.get("image")
            datetime_fields = element.get("datetime")
            info_fields = element.get("info")
            
            fields["venue_key"] = venue_fixtures.find(venue_fields)
            fields["image_key"] = image_fixtures.find(image_fields)
            fields["datetime_key"] = datetime_fixtures.find(datetime_fields)
            fields["info_key"] = info_fixtures.find(info_fields)

            event_keys = tuple(fields)
            event_values = tuple(fields.values())
            event = (event_keys, event_values)

            events.add(event)

        # creates a list-of-dict structure
        unique_events = []
        for event in events:
            unique_event = dict(zip(*event))
            unique_events.append(unique_event)

        # assigning primary key 
        for i, fields in enumerate(unique_events):
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
            raise Exception(f"Could not find in {self.model}")
        
        return fk


def main():
    filename = __file__.replace("event.py", "cache/consolidated.json")

    with open(filename, "r") as f:
        data = json.load(f)

    fixtures = Event(data)
    for fixture in fixtures:
        print(fixture.get_fixture())


if __name__ == "__main__":
    main()
