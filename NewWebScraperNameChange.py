# updates name to web scraper data using image_location
import requests
from bs4 import BeautifulSoup

# Step 1: Get all items from API
response = requests.get('http://127.0.0.1:3000/items')
items = response.json()

# Step 2: Loop through each item and update name
for item in items:
    image_location = item['image_location']
    if image_location:
        image_url = f"{image_location}"
        response = requests.get(image_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        name_span = soup.find('span', {'id': 'itemNameSpan'})
        if name_span:
            item['name'] = name_span.text.strip()

            # Step 3: Update name on item
            payload = {
                'name': item['name']
            }
            patch_url = f"http://127.0.0.1:3000/items/{item['id']}"
            requests.patch(patch_url, json=payload)
