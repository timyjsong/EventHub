import json


def main():
    filenames = [
        "country",
        "state",
        "city",
        "location",
        "venue",
        "event",
        "image",
        "date",
        "info"
    ]

    agg_list = []
    for filename in filenames:
        print(filename)
        with open(f"fixtures/{filename}.json", "r") as f:
            data = json.load(f)
        agg_list += data

    with open("fixtures/all.json", "w") as f:
        json.dump(agg_list, f)


if __name__ == "__main__":
    main()
