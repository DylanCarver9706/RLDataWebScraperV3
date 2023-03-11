# updates image_location to https://rl.insider.gg/en/pc/ + image_uri
import requests

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of items from the API
response = requests.get(api_url)
items = response.json()

updated_count = 0

# Go through each item and update the image location
for item in items:
    image_uri = item['image_uri']
    image_location = f"https://rl.insider.gg/en/pc/{image_uri}"
    patch_response = requests.patch(api_url+'/'+str(item['id']), json={'image_location': image_location})
    print(f"{item['id']} Image location updated")
    updated_count += 1

print(f"Updated {updated_count} items")
