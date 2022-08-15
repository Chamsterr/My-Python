# from time import sleep
# from config import host, user, password, database
# from psycopg2 import Error

# import requests
# import pprint
# import psycopg2


# printer = pprint.PrettyPrinter()


def get_inventory_steam(steamID):
    if type(steamID) == int:
        url = f'https://steamcommunity.com/profiles/{steamID}/inventory/json/730/2'
    else:
        url = f'https://steamcommunity.com/id/{steamID}/inventory/json/730/2'

    data = requests.get(url).json()
    return data
#     #looks like i can make one request in 40 seconds

# def check_if_drop(inventory):
#     len_inventory = len(inventory["rgInventory"])
#     # Запрос к бд на сравнение было = сейчас

# print(get_inventory('kazikapa'))

from bs4 import BeautifulSoup
from cProfile import label
from time import sleep
from tkinter import Label
from turtle import width
from config import DB_URI
import requests
import pprint
import psycopg2
import xml.etree.ElementTree as ET


# printer = pprint.PrettyPrinter()

# db_connection = psycopg2.connect(DB_URI, sslmode="require")
# db_object = db_connection.cursor()


# db_object.execute("SELECT steam_id, name FROM accounts")
# result = db_object.fetchall()
# for db_row in result:
#     url = f"https://steamcommunity.com/profiles/{db_row[0]}/?xml=1"
#     data = requests.get(url)
#     tree = ET.fromstring(data.content)
#     print(db_row[1], tree[3].text)  



# def get_inventory_steam(steamID):
#     if type(steamID) == int:
#         url = f'https://steamcommunity.com/profiles/{steamID}/inventory/json/730/2'
#     else:
#         url = f'https://steamcommunity.com/id/{steamID}/inventory/json/730/2'

#     data = requests.get(url).json()
#     return data


# def get_extra_items(data):
#     db_object.execute("SELECT * FROM accounts")
#     result = db_object.fetchall()
#     for item in result:
#         inventory_num = len(get_inventory_steam(item[2])["rgInventory"])
#         get_changes = inventory_num  - item[3]
#         if get_changes > 0:
#             descriptions = {description['classid']: description["market_name"] for description in list(data['rgDescriptions'].values())[:get_changes]}
#             inventory_ = [item['classid'] for item in list(data['rgInventory'].values())[:get_changes]]
#             for item in inventory_:
#                 if item in descriptions.keys():
#                     if "Case" in  descriptions[item]:
#                         db_object.execute("UPDATE accounts SET inventory_num", inventory_num, "WHERE PK =", item[0])
#                         print("Детект и обработан")
#         elif get_changes < 0:
#             db_object.execute("UPDATE accounts SET inventory_num", inventory_num, "WHERE PK =", item[0])
#             print("Детект и ничего")


# db_connection = psycopg2.connect(DB_URI, sslmode="require")
# db_object = db_connection.cursor()
# db_object.execute("SELECT * FROM accounts")
# result = db_object.fetchall()
# output_message = ""
# online_accounts = []
# for db_row_2 in result:
#     html_text = requests.get(
#         f'https://steamcommunity.com/profiles/{db_row_2[2]}').text
#     soup = BeautifulSoup(html_text, 'lxml')
#     status = soup.find('div', class_='profile_in_game_name')
#     if status and status.text == "Counter-Strike: Global Offensive":
#         online_accounts.append(db_row_2[1])
# if online_accounts:
#     for num, online_account in enumerate(online_accounts):
#         output_message += f"{num + 1}) {online_account} \n"
# else:
#     output_message = "Никого не нашел"

# print(output_message)
# printer.pprint(list(inventory.values())[15])
# printer.pprint(list(descriptions.values())[14])
# printer.pprint(descriptions)
# print(len(arr[1]))

# import xml.etree.ElementTree as ET
# from bs4 import BeautifulSoup

# run = True
# while run:
#     db_object.execute("SELECT * FROM accounts")
#     result = db_object.fetchall()
#     for db_row in result:
#         html_text = requests.get(f'https://steamcommunity.com/profiles/{db_row[2]}').text
#         soup = BeautifulSoup(html_text, 'lxml')
#         status = soup.find('div', class_ = 'profile_in_game_name')
#         print(db_row[1])
#         if status and status.text == "Counter-Strike: Global Offensive":
#             print(db_row[1], 'Проверка') 
#             data = get_inventory_steam(db_row[2])
#             inventory_num = len(data["rgInventory"])
#             get_changes = inventory_num  - db_row[3]
#             if get_changes > 0:
#                 descriptions = {description['classid']: description["market_name"] for description in list(data['rgDescriptions'].values())[:get_changes]}
#                 inventory_ = [item['classid'] for item in list(data['rgInventory'].values())[:get_changes]]
#                 for item in inventory_:
#                     if item in descriptions.keys():
#                         if "Case" in  descriptions[item]:
#                             str = f"UPDATE accounts SET inventory_num = {inventory_num} WHERE PK = {db_row[0]}"
#                             INSERT = f"INSERT INTO drops(NAME, steam_id, date) VALUES('{descriptions[item]}', {db_row[2]}, NOW())"
#                             db_object.execute(str)
#                             db_object.execute(INSERT)
#                             print(INSERT)
#                             print("Детект и обработан")
#                             print(descriptions[item])
#             elif get_changes < 0:
#                 str = f"UPDATE accounts SET inventory_num = {inventory_num} WHERE PK = {db_row[0]}"
#                 db_object.execute(str)
#                 print(f"Детект что исчезло {abs(get_changes)} и обработано")
#             else:
#                 print("Все клиер")
#             db_connection.commit()
#             sleep(40)

# data = requests.get("https://steamcommunity.com/profiles/76561198858045998/?xml=1")
# root = data.getroot()
# print(root.tag)

# data = get_inventory_steam(76561199086937073)

# print(len(data["rgInventory"]))
# url = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v2/?key=EEFAD0B3EEDD3BCF1188009AE115829B&steamid=76561198211224904&appid=730"
# data = requests.get("https://steamcommunity.com/profiles/76561198858045998/?xml=1")

# print(data)
def get_offline_update(message):
    try:
        db_connection = psycopg2.connect(DB_URI, sslmode="require")
        db_object = db_connection.cursor()
        steam_ides = message.split()
        for steam_id in steam_ides:
            db_object.execute(f"SELECT * "
                            f"FROM accounts "
                            f"WHERE steam_id IN({steam_id})")
            result = db_object.fetchall()
            
            inventory = get_inventory_steam(int(steam_id))
            inventory_num = len(inventory["rgInventory"])
            get_changes = inventory_num - result[0][3]
            if get_changes > 0:
                descriptions = {
                            description['classid']: description["market_name"]
                            for
                            description in
                            list(inventory['rgDescriptions'].values())[
                            :get_changes]}
                inventory_ = [item['classid'] for item in
                                      list(inventory['rgInventory'].values())[
                                      :get_changes]]
                for item in inventory_:
                    if item in descriptions.keys():
                        if "Case" in descriptions[item]:
                            UPDATE = f"UPDATE accounts " \
                                     f"SET inventory_num = {inventory_num} " \
                                     f"WHERE PK = {result[0][0]}"
                            INSERT = f"INSERT INTO drops(NAME, steam_id, date) " \
                                     f"VALUES('{descriptions[item]}', " \
                                     f"{result[0][2]}, NOW())"
                            db_object.execute(UPDATE)
                            db_object.execute(INSERT)
                            bot.send_message(message.chat.id,
                                    f"{result[0][1]}: {descriptions[item]}")
            elif get_changes < 0:
                UPDATE = f"UPDATE accounts " \
                         f"SET inventory_num = {inventory_num} " \
                         f"WHERE PK = {result[0][0]}"
                db_object.execute(UPDATE)
            db_connection.commit()
            sleep(47)     
    except Exception as _ex:
        bot.send_message(message.chat.id, f"[INFO] Error while "
                                          f"working with PostgreSQL {_ex}")

# get_offline_update("76561198125996907 76561199030967955")

from PIL import Image
import matplotlib.pyplot as plt
import pandas
import numpy

def fig2img(fig):
    """Convert a Matplotlib figure to a PIL Image and return it"""
    import io
    buf = io.BytesIO()
    fig.savefig(buf, format="jpg", dpi=360)
    buf.seek(0)
    img = Image.open(buf)
    return img


try:
    db_connect = psycopg2.connect(DB_URI, sslmode="require")
    df = pandas.read_sql("SELECT name, SUM(val) FROM drops GROUP BY name",
                             db_connect)
    print(df)
    df.groupby(['name']).sum().plot(kind='pie', subplots=True,
                                        autopct='%1.0f%%', legend=False)
    # plt.savefig('fig1.png')
    # # fig.canvas.draw()
    # # data = numpy.frombuffer(fig.canvas.tostring_rgb(), dtype=numpy.uint8)
    # # data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    # # print(data)
    # plt.show()
    fig = plt.gcf()
    img = fig2img(fig)

    img.show()
    print(img)
except Exception as _ex:
    print( f"[INFO] {_ex}")