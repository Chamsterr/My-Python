import requests

response = requests.get('https://www.example.com')

items = response.headers.items()

print(items)