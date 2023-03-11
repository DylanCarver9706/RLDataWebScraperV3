# Outputs new web scraper single items to a .txt file

import requests

api_url = 'http://127.0.0.1:3000/items'

# Get the current list of items from the API
response = requests.get(api_url)
items = response.json()

# Create a new file to write the formatted items to
with open('NewWebScraperSingleItems.txt', 'w') as f:
    for item in items:
        # Format the item attributes and write to the file
        formatted_item = f"Item.create(valid_status: {item['valid_status']}, image_uri: \"{item['image_uri']}\", name: \"{item['name']}\", rarity: \"{item['rarity']}\", item_type: \"{item['item_type']}\", color: \"{item['color']}\", image_location: \"{item['image_location']}\", image: \"{item['image']}\"\n)"
        f.write(formatted_item)

print("Done writing items to file")


# Outputs as is DB items to a .txt file

# import requests

# api_url = 'http://127.0.0.1:3000/daily_items'
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

# api_url = "http://127.0.0.1:3000/daily_items"
# output_file = "daily_items.txt"

# response = requests.get(api_url)
# items = response.json()

# with open(output_file, "w") as f:
#     for item in items:
#         if item["valid_status"] is True:
#             f.write('DailyItem.create(valid_status: {0}, image_uri: "{1}", item_shop_date_id: date1.id, name: "{2}", rarity: "{3}", item_type: "{4}", color: "{5}", image_location: "{6}", image: "{7}")\n'.format(
#                 item["valid_status"], item["image_uri"], item["name"], item["rarity"], item["item_type"], item["color"], item["image_location"], item["image"]
#             ))


# Outputs the potential DNE items to a .txt file

# import requests

# api_url = 'http://127.0.0.1:3000/daily_items'

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

# api_url = 'http://127.0.0.1:3000/daily_items'

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

# api_url = 'http://127.0.0.1:3000/daily_items'

# # Get the current list of daily items from the API
# response = requests.get(api_url)
# items = response.json()

# valid_count = 0

# # Go through each item and check if it has a valid status of true
# for item in items:
#     if item['valid_status'] is True:
#         valid_count += 1

# print(f"There are {valid_count} items with a valid status of true")