# deletes items in DB that have the same "image_location"
import requests

url = "http://127.0.0.1:3000/items"

# Get all items from the API
response = requests.get(url)
items = response.json()

# Keep track of image locations that have been seen
seen_locations = set()

# Keep track of items that have been deleted
deleted_items = []

# Loop through all items and check their image location
for item in items:
    location = item['image_location']

    # Check if the location has been seen before
    if location in seen_locations:
        # If so, delete the item and add it to the deleted_items list
        response = requests.delete(f"{url}/{item['id']}")
        if response.status_code == 204:
            deleted_items.append(f"{item['name']} - {item['color']}")
            print(f"{item['name']} - {item['color']} deleted")
    else:
        # If not, add it to the seen_locations set
        seen_locations.add(location)

# Print out the number of items that were deleted
print(f"{len(deleted_items)} items were deleted.")
