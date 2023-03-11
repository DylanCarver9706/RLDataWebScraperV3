# updates item_type from image_uri
import requests

api_url = 'http://127.0.0.1:3000/items'

response = requests.get(api_url)
items = response.json()

for item in items:
    if 'image_uri' in item and item['image_uri']:
        item_type = item['image_uri'].split('/')[0].capitalize()
        if item_type != item['item_type']:
            item_data = {'item_type': item_type}
            patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
            print(f"{item['id']} Item type updated: {item['item_type']} -> {item_type}")