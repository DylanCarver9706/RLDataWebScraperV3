# Go through each item and update the image uri to remove the color suffix from the image_uri
import requests
import json

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of daily items from the API
response = requests.get(api_url)
items = response.json()

updated_count = 0

# Go through each item and update the image uri
for item in items:
    if item['image_uri']:
        # Remove the color suffix from the image_uri
        for color_suffix in ['/black', '/sienna', '/cobalt', '/crimson', '/fgreen', '/grey', '/lime', '/orange', '/pink', '/purple', '/saffron', '/sblue', '/white', '/gold']:
            if item['image_uri'].endswith(color_suffix):
                new_image_uri = item['image_uri'][:-(len(color_suffix))]
                item_data = {'image_uri': new_image_uri, 'image_location': f"https://rl.insider.gg/en/pc/{new_image_uri}"}
                patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
                print(f"{item['id']} Image URI updated")
                updated_count += 1
                break

print(f"Updated {updated_count} items")