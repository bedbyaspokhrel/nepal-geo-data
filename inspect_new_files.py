
import json

def check(path):
    print(f"Checking: {path}")
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"Type: {data.get('type')}")
        features = data.get('features', [])
        print(f"Feature Count: {len(features)}")
        
        if features:
            props = features[0]['properties']
            print(f"First Feature Properties: {json.dumps(props, indent=2)}")
            
            # Check for standard keys we rely on
            print(f"Keys: {list(props.keys())}")
            
    except Exception as e:
        print(f"Error: {e}")

check(r"E:\antigravity\New folder\nepalgeo\nepal-with-7provinces.geojson")
check(r"E:\antigravity\New folder\nepalgeo\nepal-with-77districts.geojson")
