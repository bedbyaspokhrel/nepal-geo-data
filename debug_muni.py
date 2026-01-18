
import json
import os

def check():
    path = "nepal_geo_data/data/municipalities.geojson"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Features count: {len(data.get('features', []))}")
    if data['features']:
        props = data['features'][0]['properties']
        print(f"Prop keys: {list(props.keys())}")
        name = props.get('gapa_napa', 'N/A')
        print(f"First Name: {name.encode('ascii', 'replace')}")
        
    # Search for Bhojpur
    found = False
    for f in data['features']:
        name = f['properties'].get('gapa_napa', '')
        if 'Bhojpur' in name:
            print(f"Found match: '{name}'")
            found = True
            break
            
    if not found:
        print("Bhojpur not found!")

if __name__ == "__main__":
    check()
