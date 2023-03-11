# updates the rarity in the db based on image_location

import requests
from bs4 import BeautifulSoup

api_url = 'http://127.0.0.1:3000/items'

response = requests.get(api_url)
items = response.json()

for item in items:
    img_location = item['image_location']
    img_response = requests.get(img_location)
    img_html = img_response.text

    item_info_start = img_html.find('<div id="itemInfoContainer"')
    if item_info_start != -1:
        item_info_end = img_html.find('</div>', item_info_start)
        item_info = img_html[item_info_start:item_info_end+6]
        if 'Common' in item_info:
            rarity = 'Common'
        elif 'Rare' in item_info:
            rarity = 'Rare'
        elif 'Premium' in item_info:
            rarity = 'Premium'
        elif 'Limited' in item_info:
            rarity = 'Limited'
        elif 'Very Rare' in item_info:
            rarity = 'Very Rare'
        elif 'Import' in item_info:
            rarity = 'Import'
        elif 'Exotic' in item_info:
            rarity = 'Exotic'
        elif 'Black Market' in item_info:
            rarity = 'Black Market'
        else:
            print(f"Could not find rarity for item {item['id']}")
            continue

        item['rarity'] = rarity
        patch_response = requests.patch(api_url+'/'+str(item['id']), json=item)
        print(f"{item['id']} rarity updated to {rarity}")
    else:
        print(f"Could not find item info for item {item['id']}")