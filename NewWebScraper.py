import requests
from bs4 import BeautifulSoup

# Step 1: Go to search URL and scrape the page
search_url = 'https://rl.insider.gg/en/pc/search'
response = requests.get(search_url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Step 2: Find all items with a class of "item common", "item uncommon", etc.
div_classes = ["item common", "item uncommon", "item limited", "item limited new", "item rare", "item veryrare", "item import", "item exotic", "item blackmarket"]
# div_classes = ["item limited new"]
items = []
for div_class in div_classes:
    item_divs = soup.find_all('div', class_=div_class)
    for item_div in item_divs:
        item_name = item_div.find('span', class_='itemName').text
        item_uri = item_div['data-uri']
        item_rarity = div_class.split()[-1].capitalize()
        item = {'name': item_name, 'uri': item_uri, 'rarity': item_rarity}
        items.append(item)

# Step 3: Access the API and create a new item for each scraped item
api_url = 'http://127.0.0.1:3000/items'
for item in items:
    new_item = {
        'valid_status': False,
        'image_uri': item['uri'],
        'item_shop_date_id': '',
        'name': item['name'],
        'rarity': item['rarity'],
        'item_type': '',
        'color': '',
        'image_location': f"https://rl.insider.gg/en/pc/{item['uri']}",
        'image': ''
    }
    response = requests.post(api_url, json=new_item)
    if response.status_code == 201:
        print(f"Item created: {item['name']}")
    else:
        print(f"Error creating item: {response.text}")