# gets the info from items that have multiple useses

import requests
from bs4 import BeautifulSoup

url = 'https://rl.insider.gg/en/pc/search'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.find_all('div', class_='decalGroup')

for item in items:
    data = item['data-decal-dropdown']
    data = eval(data)  # convert string to dict

    for sublist in data['Untradeable']:
        info = sublist[2].split('/')
        image_uri = '/'.join(info)
        name = f"{info[1].capitalize()} [{info[2].capitalize()}]"
        payload = {
            'name': name,
            'item_type': 'Decals',
            'valid_status': False,
            'image_uri': image_uri,
            'image_location': '',
            'image': ''
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post('http://127.0.0.1:3000/items', json=payload, headers=headers)

        if response.status_code == 200:
            print(f"{name} found")
        else:
            print(f"Error: {response.status_code}")



# import requests
# from bs4 import BeautifulSoup

# import json

# # URL to scrape
# url = "https://rl.insider.gg/en/pc/search"

# # Make a GET request to the website
# response = requests.get(url)

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all elements with class name "decalGroup"
# decal_groups = soup.find_all(class_="decalGroup")

# # Iterate over each decal group
# for decal_group in decal_groups:
#     # Get the data-decal-dropdown attribute
#     dropdown_data = decal_group.get("data-decal-dropdown")
#     if dropdown_data:
#         # Parse the dropdown data as a JSON object
#         dropdown_data = json.loads(dropdown_data)
#         for rarity, items in dropdown_data.items():
#             for item in items:
#                 # Get the image URI from the item data
#                 image_uri = item[2].split("/")[-1]
#                 # Get the item name from the item data
#                 name = item[1]
#                 # Create the data for the POST request
#                 data = {
#                     "id": None,
#                     "name": name,
#                     "rarity": rarity,
#                     "item_type": "Decals",
#                     "color": "",
#                     "valid_status": False,
#                     "image_uri": image_uri,
#                     "image_location": "",
#                     "image": ""
#                 }
#                 # Make the POST request to the API
#                 response = requests.post("http://127.0.0.1:3000/items", json=data)
#                 # Check if the item was created successfully
#                 if response.status_code == 200:
#                     print(f"{name} found")
#                 else:
#                     print(f"{name} not found")