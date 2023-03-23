# Outputs the items to a .txt file by item type

import requests

url = "http://127.0.0.1:3000/items"

# Get all items from the API
response = requests.get(url)
items = response.json()

with open('ItemTypeSeparator.txt', 'w') as f:
    for item in items:
        # Format the output string
        output_string = f'{item["item_type"]}.create(valid_status: {item["valid_status"]}, image_uri: "{item["image_uri"]}", name: "{item["name"]}", rarity: "{item["rarity"]}", item_type: "{item["item_type"]}", color: "{item["color"]}", image_location: {item["image_location"]}, image: "{item["image"]}")\n'

        # Append the output to the file
        f.write(output_string)



# Outputs items where "image" is not empty

# import requests

# url = "http://127.0.0.1:3000/items"

# # Get all items from the API
# response = requests.get(url)
# items = response.json()

# # Create or overwrite the output file
# with open("NewWebScraperAllMultipleItems.txt", "w") as f:
#     # Loop through each item in the API
#     for item in items:
#         # Check if the image location is empty
#         if item['image'] != '':
#             # Write the formatted string to the file
#             f.write(f"Item.create(valid_status: {item['valid_status']}, image_uri: \"{item['image_uri']}\", name: \"{item['name']}\", rarity: \"{item['rarity']}\", item_type: \"{item['item_type']}\", color: \"{item['color']}\", image_location: \"{item['image_location']}\", image: \"{item['image']}\")\n")




# Outputs new web scraper items to a .txt file

# import requests
# import time

# api_url = 'http://127.0.0.1:3000/items'

# # Get the current list of items from the API
# response = requests.get(api_url)
# items = response.json()

# # Create a new file with a unique filename based on the current timestamp
# filename = f"NewWebScraperSeeds_{int(time.time())}.txt"
# with open(filename, 'w') as f:
#     # Go through each item and write the data to the text file
#     for item in items:
#         f.write(f"Item.create(valid_status: {item['valid_status']}, image_uri: \"{item['image_uri']}\", name: \"{item['name']}\", rarity: \"{item['rarity']}\", item_type: \"{item['item_type']}\", color: \"{item['color']}\", image_location: \"{item['image_location']}\", image: \"{item['image']}\")\n")


# Outputs as is DB items to a .txt file

# import requests

# api_url = 'http://127.0.0.1:3000/items'
# response = requests.get(api_url)
# items = response.json()

# with open('items.txt', 'w') as f:
#     for item in items:
#         valid_status = item['valid_status']
#         image_uri = item['image_uri']
#         item_shop_date_id = item['item_shop_date_id']
#         name = item['name']
#         rarity = item['rarity']
#         item_type = item['item_type']
#         color = item['color']
#         image_location = item['image_location']
#         image = item['image']
#         text = f"DailyItem.create(valid_status: {valid_status}, image_uri: \"{image_uri}\", item_shop_date_id: {item_shop_date_id}, name: \"{name}\", rarity: \"{rarity}\", item_type: \"{item_type}\", color: \"{color}\", image_location: \"{image_location}\", image: \"{image}\")\n"
#         f.write(text)


# Outputs validated items to a .txt file

# import requests

# api_url = "http://127.0.0.1:3000/items"
# output_file = "items.txt"

# response = requests.get(api_url)
# items = response.json()

# with open(output_file, "w") as f:
#     for item in items:
#         if item["valid_status"] is True:
#             f.write('Item.create(valid_status: {0}, image_uri: "{1}", name: "{2}", rarity: "{3}", item_type: "{4}", color: "{5}", image_location: "{6}", image: "{7}")\n'.format(
#                 item["valid_status"], item["image_uri"], item["name"], item["rarity"], item["item_type"], item["color"], item["image_location"], item["image"]
#             ))


# Outputs the potential DNE items to a .txt file

# import requests

# api_url = 'http://127.0.0.1:3000/items'

# # Get the current list of daily items from the API
# response = requests.get(api_url)
# items = response.json()

# # Open a new text file to write the filtered items
# with open('filtered_items.txt', 'w') as f:
#     # Go through each item and check if it meets the filtering criteria
#     for item in items:
#         if not item['valid_status'] and not item['color'] and not item['image_uri']:
#             # Write the item to the text file in the desired format
#             f.write(f"DailyItem.create(image_uri: \"{item['image_uri']}\", item_shop_date_id: date1.id, name: \"{item['name']}\", rarity: \"{item['rarity']}\", item_type: \"{item['item_type']}\", color: \"{item['color']}\", image_location: \"{item['image_location']}\")\n")
#             print(f"{item['id']} {item['name']} meets the criteria")




# Counts how many potential DNE items

# import requests

# api_url = 'http://127.0.0.1:3000/items'

# # Get the current list of daily items from the API
# response = requests.get(api_url)
# items = response.json()

# invalid_count = 0

# # Go through each item and check if it has a valid status of false and empty "image_uri" and "color" attributes
# for item in items:
#     if item['valid_status'] is False and not item['image_uri'] and not item['color']:
#         invalid_count += 1

# print(f"There are {invalid_count} items with a valid status of false, an empty image_uri, and an empty color")


# Counts how many valid items there are

# import requests

# api_url = 'http://127.0.0.1:3000/items'

# # Get the current list of daily items from the API
# response = requests.get(api_url)
# items = response.json()

# valid_count = 0

# # Go through each item and check if it has a valid status of true
# for item in items:
#     if item['valid_status'] is True:
#         valid_count += 1

# print(f"There are {valid_count} items with a valid status of true")