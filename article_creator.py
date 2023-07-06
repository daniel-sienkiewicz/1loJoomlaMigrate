import requests
import json

url = 'https://<URL>/api/index.php/v1/content/articles'
headers = {
    'Content-Type': 'text/html; charset=utf-8',
    'X-Joomla-Token': '<TOKEN>'
}

with open('j17_content.json', encoding="utf-8") as file:
    json_data = json.load(file)

for item in json_data[2]['data']:
    dataa = {
        "alias": item.get('alias'),
        "state": 1,
        "created": item.get('created'),
        "articletext": item.get('introtext').replace('\\"', '"'),
        "catid": 2,
        "language": "*",
        "metadesc": "",
        "metakey": "",
        "featured": item.get('featured'),
        "title": item.get('title').replace('\\"', '"').replace("\r\n", "")
    }

    response = requests.post(url, headers=headers, json=dataa)
    print(response.text)
