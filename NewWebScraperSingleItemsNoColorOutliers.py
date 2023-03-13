import requests

url = "http://127.0.0.1:3000/items"
response = requests.get(url)
items = response.json()

for item in items:
    if item['valid_status'] and item['image_location'].endswith('/black'):
        new_item = item.copy()
        new_item['image_location'] = new_item['image_location'].replace('/black', '')
        new_item['valid_status'] = True
        new_item['color'] = ''
        del new_item['image_uri']
        response = requests.post(url, data=new_item)
        if response.status_code == 201:
            print(f"{new_item['item_type']} - {new_item['name']} with black removed added")