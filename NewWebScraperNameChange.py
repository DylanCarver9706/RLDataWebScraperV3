# updates "name" based on <title> from image_location
import requests
from bs4 import BeautifulSoup
import json

# Fetch all items from the API
url = "http://127.0.0.1:3000/items"
response = requests.get(url)
items = json.loads(response.text)

# Loop through each item and update the name
for item in items:
    image_location = item['image_location']
    if image_location:
        image_url = f"{image_location}"
        page = requests.get(image_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find("title").text
        item_name = title.split(" on PC")[0].strip()
        item['name'] = item_name
        # Update the item with the new name
        patch_url = f"http://127.0.0.1:3000/items/{item['id']}"
        response = requests.patch(patch_url, data=item)
        print(f"{item_name} updated successfully!")
    else:
        print("Item has no image location. Skipping...")