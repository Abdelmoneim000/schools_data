import pandas as pd
import json

# Load your Excel file
file_path = 'EDGE_GEOCODE_PUBLICSCH_2223.xlsx'
df = pd.read_excel(file_path)

# Extract only the relevant columns from the actual DataFrame
school_data_subset = df[['OPSTFIPS', 'LEAID', 'NAME', 'STREET', 'CITY', 'STATE', 'ZIP']]

# Grouping and restructuring data into a hierarchical dictionary
state_district_school_data = {}

# Iterate over each row to structure data by state and district
for _, row in school_data_subset.iterrows():
    state_id = str(row['OPSTFIPS']).zfill(2)  # Zero-pad state FIPS code for consistency
    district_id = str(row['LEAID'])
    school_info = {
        "school_name": row['NAME'],
        "street": row['STREET'],
        "city": row['CITY'],
        "zip": row['ZIP']
    }
    
    # Initialize state and district if not present
    if state_id not in state_district_school_data:
        state_district_school_data[state_id] = {"state_abbr": row['STATE'], "districts": {}}
    
    if district_id not in state_district_school_data[state_id]["districts"]:
        state_district_school_data[state_id]["districts"][district_id] = {"schools": []}
    
    # Append school information to the appropriate district
    state_district_school_data[state_id]["districts"][district_id]["schools"].append(school_info)

# Convert the structured data into a JSON file for easy access and HTML generation
json_output_path = 'schools_by_state_and_district.json'
with open(json_output_path, 'w') as json_file:
    json.dump(state_district_school_data, json_file, indent=2)

json_output_path
