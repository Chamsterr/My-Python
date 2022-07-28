import requests
import pprint

printer = pprint.PrettyPrinter()

def get_inventory(steamID):
    url = f'https://steamcommunity.com/profiles/{steamID}/inventory/json/730/2'
    descriptions = requests.get(url).json()['rgDescriptions']
    inventory = requests.get(url).json()["rgInventory"]

    print(f'Counter-Strike: Global Offensive:', len(inventory))

    for description in descriptions.values():
        print(description['market_name'], description['classid'])