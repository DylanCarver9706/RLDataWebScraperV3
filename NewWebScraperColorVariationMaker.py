import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:3000/items"
colors = ['/black', '/sienna', '/cobalt', '/crimson', '/fgreen', '/grey', '/lime', '/orange', '/pink', '/purple', '/saffron', '/sblue', '/white', '/gold']

# Get all items from the API
response = requests.get(url)
items = response.json()

for item in items:
    # Duplicate item for each color
    for color in colors:
        new_item = item.copy()
        
        # Clear the name
        # new_item['name'] = ''
        
        # Set the image location with the color
        new_item['image_location'] = new_item['image_location'] + color
        
        # Set the valid status and color
        new_item['valid_status'] = False
        new_item['color'] = color[1:].title()
        
        # Don't use the original image URI
        new_item['image_uri'] = new_item['image_uri']
        new_item['image'] = ''
        
        # Make a POST request with the new item
        response = requests.post(url, json=new_item)
        
        # Print a message if the item was added
        if response.status_code == 201:
            print(f"{new_item['item_type']} - {new_item['color']} {new_item['name']} added")

        # Set the valid status back to False for the next iteration
        new_item['valid_status'] = False
        