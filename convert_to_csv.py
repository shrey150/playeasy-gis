import requests
import json
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def extract_lat_long_via_address(address_or_zipcode):
    lat, lng = None, None
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    endpoint = f"{base_url}?address={address_or_zipcode}&key={API_KEY}"

    r = requests.get(endpoint)
    if r.status_code not in range(200, 299):
        return None, None
    try:
        results = r.json()['results'][0]
        print(results)
        lat = results['geometry']['location']['lat']
        lng = results['geometry']['location']['lng']
    except:
        pass
    print(f'Found {address_or_zipcode}: ({lat}, {lng})')
    return lat, lng

def enrich_with_geocoding_api(row):
    column_name = 'address'
    address_value = row[column_name]
    address_lat, address_lng = extract_lat_long_via_address(address_value)
    row['lat'] = address_lat
    row['lng'] = address_lng
    return row

with open("data.json", "r") as file:
    file_data = file.read()
    raw_data = json.loads(file_data)

    facilities = raw_data['data']

    df = pd.DataFrame.from_records(facilities)
    df = df[
        [
            "name",
            "type",
            "address",
            "maxSeated",
            "website",
        ]
    ]

df = df.apply(enrich_with_geocoding_api, axis=1)
df.to_csv("out.csv")