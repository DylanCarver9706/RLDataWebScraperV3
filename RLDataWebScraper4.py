# takes the image_location + color and replaces image_location with that
import requests
import time

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of daily items from the API
response = requests.get(api_url)
items = response.json()

updated_count = 0
skipped_count = 0

# Go through each item and update the image location
for item in items:
    if item['valid_status'] is True:
        skipped_count += 1
        continue
    if not item['color']:
        skipped_count += 1
        continue
    if item['image_location'].endswith(item['color']):
        skipped_count += 1
        continue
    while True:
        try:
            new_location = item['image_location'] + '/' + item['color']
            item_data = {'image_location': new_location}
            patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
            print(f"{item['id']} Image location updated")
            updated_count += 1
            break
        except Exception as e:
            print(f"Error updating item {item['id']}: {e}")
            print(f"Retrying in 5 minutes...")
            time.sleep(5 * 60)

print(f"Updated {updated_count} items")
print(f"Skipped {skipped_count} items")