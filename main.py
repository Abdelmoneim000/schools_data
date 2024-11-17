import pandas as pd
import json

# Load the Excel file
file_path = 'EDGE_GEOCODE_PUBLICSCH_2223.xlsx'
df = pd.read_excel(file_path)

# Organize data by district
district_data = {}

# Iterate through the DataFrame rows
for index, row in df.iterrows():
    lea_id = row['LEAID']
    school_info = {
        'ncessch': row['NCESSCH'],
        'name': row['NAME'],
        'opstfips': row['OPSTFIPS'],
        'street': row['STREET'],
        'city': row['CITY'],
        'state': row['STATE'],
        'zip': row['ZIP'],
        'county': row['CNTY'],
        'locale': row['LOCALE'],
        'latitude': row['LAT'],
        'longitude': row['LON'],
        'school_year': row['SCHOOLYEAR']
    }
    
    # If the district (LEAID) doesn't exist, create a new entry
    if lea_id not in district_data:
        district_data[lea_id] = {
            'district_id': lea_id,
            'schools': []
        }
    
    # Append the school info to the district's school list
    district_data[lea_id]['schools'].append(school_info)

# Convert the district data to JSON format
json_output = json.dumps(district_data, indent=4)

# Write the JSON output to a file
with open('school_data_by_district.json', 'w') as json_file:
    json_file.write(json_output)

print("Data has been extracted and saved to 'school_data_by_district.json'.")