import json


reversed_state_abbr_map = {
    "AL": "albama",
    "AK": "alaska",
    "AS": "american samoa",
    "AZ": "arzona",
    "AR": "arkansas",
    "CA": "california",
    "CO": "colorado",
    "CT": "connecticut",
    "DE": "delaware",
    "DC": "district of columbia",
    "FM": "federated states of micronesia",
    "FL": "florid",
    "GA": "georgia",
    "GU": "guam",
    "HI": "hawaii",
    "ID": "idaho",
    "IL": "illinois",
    "IN": "indiana",
    "IA": "iowa",
    "KS": "kansas",
    "KY": "kentucky",
    "LA": "louisiana",
    "ME": "maine",
    "MD": "maryland",
    "MA": "massachusetts",
    "MI": "michigan",
    "MN": "minnesota",
    "MS": "mississippi",
    "MO": "missouri",
    "MT": "montana",
    "NE": "nebraska",
    "NV": "nevada",
    "NH": "new hampshire",
    "NJ": "new jersey",
    "NM": "new mexico",
    "NY": "new york",
    "NC": "north carolina",
    "ND": "north dakota",
    "MP": "northern mariana islands",
    "OH": "ohio",
    "OK": "oklahoma",
    "OR": "oregon",
    "PA": "pennsylvania",
    "PR": "puerto rico",
    "PW": "republic of palau",
    "MH": "republic of the marshall islands",
    "RI": "rhode island",
    "SC": "south carolina",
    "SD": "south dakota",
    "TN": "tennessee",
    "TX": "texas",
    "UT": "utah",
    "VT": "vermont",
    "VI": "virgin islands",
    "VA": "virginia",
    "WA": "washington",
    "WV": "west virginia",
    "WI": "wisconsin",
    "WY": "wyoming"
}

def parse_links(file):
    """Parse links.txt and return a dictionary of state links."""
    state_links = {}
    with open(file, "r") as f:
        lines = f.readlines()

    current_state = None
    for line in lines:
        line = line.strip()
        if line.endswith(":"):
            current_state = line.split(":")[0].strip().lower()
            print(current_state)
            state_links[current_state] = {"website": "EMPTY", "yt-link": "EMPTY"}
        elif line and line != "EMPTY":
            if state_links[current_state]["website"] == "EMPTY":
                state_links[current_state]["website"] = line
            else:
                state_links[current_state]["yt-link"] = line

    return state_links

def add_links_to_json(json_file, links_file):
    """Add YouTube and website links to the JSON file for each state."""
    state_links = parse_links(links_file)
    print(state_links)

    # Load the existing JSON data
    with open(json_file, "r") as f:
        data = json.load(f)

    # Add the links to the JSON data
    for state_id, state_info in data.items():
        state_name = state_info["state_abbr"]

        if reversed_state_abbr_map[state_name] in state_links:
            state_info["website"] = state_links[reversed_state_abbr_map[state_name]]["website"]
            state_info["yt-link"] = state_links[reversed_state_abbr_map[state_name]]["yt-link"]

    # Write the updated data back to the file
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    json_file_path = "schools_by_state_and_district.json"
    links_file_path = "links.txt"
    add_links_to_json(json_file_path, links_file_path)