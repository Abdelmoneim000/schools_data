import json


if __name__ == "__main__":
    with open("schools_by_state_and_district.json") as f:
        schools_dict = json.load(f)
        for key in schools_dict:
            print(f"{schools_dict[key]["state_abbr"]} state code: {key}")