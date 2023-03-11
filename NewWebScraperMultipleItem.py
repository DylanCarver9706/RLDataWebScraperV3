# gets the info from items that have multiple useses

import requests
from bs4 import BeautifulSoup

# import json

url = "https://rl.insider.gg/en/pc/search"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.find_all("div", class_="decalGroup")

for item in items:
    data = item.get("data-decal-dropdown")
    data_dict = eval(data)
    for rarity in data_dict:
        for inner_array in data_dict[rarity]:
            name = f"{inner_array[1]} [{inner_array[2].split('/')[1]}]"
            image_uri = inner_array[2].replace("/", "_")
            payload = {
                "id": "",
                "name": name,
                "rarity": rarity.capitalize(),
                "item_type": "Decals",
                "color": "",
                "valid_status": False,
                "image_uri": image_uri,
                "image_location": "",
                "image": "",
            }
            response = requests.post("http://127.0.0.1:3000/items", json=payload)
            if response.status_code == 200:
                print(f"{name} found")



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