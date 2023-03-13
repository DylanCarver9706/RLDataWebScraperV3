import requests

url = "http://127.0.0.1:3000/items"

# Get all items from the API
response = requests.get(url)
items = response.json()

for item in items:
    if item['valid_status'] and item['image_location'].endswith('/black'):
        # Duplicate item without the "/black" in image_location
        new_item = item.copy()
        new_item['image_location'] = new_item['image_location'].replace('/black', '')
        
        # Set the valid_status to False and color to ""
        new_item['valid_status'] = False
        new_item['color'] = ""
        
        # Don't use the original image URI
        del new_item['image_uri']
        
        # Make a POST request with the new item
        response = requests.post(url, data=new_item)
        
        # Print a message if the item was added
        if response.status_code == 201:
            print(f"{new_item['item_type']} {new_item['name']} added")