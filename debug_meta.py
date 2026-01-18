import json
import os

def check():
    # Relative to nepal-geo-data/
    path = "nepal_geo_data/data/meta_en.json"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        meta = json.load(f)
    
    print(f"Total Provinces in Metadata: {len(meta)}")

    found = False
    for i, province in enumerate(meta):
        print(f"Province {i+1} keys: {list(province.keys())}")
        districts = province.get('districts', [])
        if isinstance(districts, dict):
            print(f"  Districts is DICT")
            districts = list(districts.values())
        else:
             print(f"  Districts is LIST")
        
        print(f"  Districts count: {len(districts)}")
        
        if len(districts) > 0:
             # print sample
             pass

        for district in districts:
            if isinstance(district, str): continue
            
            d_id = district.get('id')
            if d_id == 27:
                print(f"District 27 Municipalities:")
                for muni in munis:
                    print(f" - '{muni.get('name')}'")
    
    if not found:
        print("Kathmandu not found in metadata!")

if __name__ == "__main__":
    check()
