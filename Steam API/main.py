from time import sleep
import requests
import pprint

printer = pprint.PrettyPrinter()


def get_inventory(steamID):
    url = f'https://steamcommunity.com/profiles/{steamID}/inventory/json/730/2'
    data = requests.get(url)
    print(data.status_code)

    data = data.json()
    
    descriptions = data['rgDescriptions']
    inventory = data["rgInventory"]

    print(f'Counter-Strike: Global Offensive:', len(inventory))

    for description in descriptions.values():
        print(description['market_name'], description['classid'])