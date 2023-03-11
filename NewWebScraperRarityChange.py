# fix naming error with rarity blackmarket -> Black Market
import requests

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of daily items from the API
response = requests.get(api_url)
items = response.json()

updated_count = 0

# Go through each item and update the rarity
for item in items:
    rarity = item['rarity']
    if rarity == 'Veryrare':
        rarity = 'Very Rare'
    elif rarity == 'Blackmarket':
        rarity = 'Black Market'
    else:
        continue

    item_data = {'rarity': rarity}
    patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
    if patch_response.status_code == 200:
        print(f"{item['id']} Rarity updated to {rarity}")
        updated_count += 1
    else:
        print(f"{item['id']} Error updating rarity")

print(f"Updated {updated_count} items")