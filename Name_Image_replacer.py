# Replace

# import requests

# api_url = 'http://127.0.0.1:3000/daily_items'

# # Get the current list of daily items from the API
# response = requests.get(api_url)
# items = response.json()

# updated_count = 0

# # Go through each item and update the image
# for item in items:
#     if item['name'] == 'Buffy-Sugo':
#         item_data = {'image': 'https://static.wikia.nocookie.net/rocketleague/images/7/73/Buffy-Sugo_goal_explosion_icon.png/revision/latest?cb=20201024171342'}
#         patch_response = requests.patch(api_url+'/'+str(item['id']), json=item_data)
#         print(f"{item['id']} Image updated")
#         updated_count += 1

# print(f"Updated {updated_count} items")


# Delete

import requests

api_url = 'http://127.0.0.1:3000/daily_items'

# Get the current list of daily items from the API
response = requests.get(api_url)
items = response.json()

delete_count = 0

# Go through each item and delete if the name matches
for item in items:
    if item['name'] == 'Proffer':
        delete_response = requests.delete(api_url + '/' + str(item['id']))
        if delete_response.status_code == 204:
            print(f"{item['id']} Item deleted")
            delete_count += 1
        else:
            print(f"{item['id']} Error deleting item")

print(f"Deleted {delete_count} items")