# makes a duplicate of each item whose "item_lacation" ends with a color
# that duplicate will then be a non color version of the original
import requests

url = "http://127.0.0.1:3000/items"
colors = ['/black', '/sienna', '/cobalt', '/crimson', '/fgreen', '/grey', '/lime', '/orange', '/pink', '/purple', '/saffron', '/sblue', '/white', '/gold']

# Get all items from the API
response = requests.get(url)
items = response.json()

for item in items:
    # if item['valid_status'] == True:
        for color in colors:
            if item['image_location'].endswith(color):
                new_item = item.copy()
                
                # Delete the color from the image_location
                new_item['image_location'] = new_item['image_location'].replace(color, "")
                
                # Set the valid status and color
                new_item['valid_status'] = False
                new_item['color'] = ""
                
                # Copy the image_uri from the original item
                new_item['image_uri'] = item['image_uri']
                
                # Make a POST request with the new item
                response = requests.post(url, data=new_item)
                
                # Print a message if the item was added
                if response.status_code == 201:
                    print(f"{new_item['item_type']} - {new_item['name']} added with color {color}")
