from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
from datetime import datetime

import pprint
import os
import requests


printer = pprint.PrettyPrinter()


def print_leaderboards():
    data = get_leaderboards().json
    categories = data['leaderboards']

    for category in categories:
        print('Category: ', category)
        for idx, entry in enumerate(categories[category]):
            print(f"Rank: {idx + 1}"
                  f"| Username: {entry['username']} | Rating {entry['score']}")


def category_stats(category, username):
    os.system("cls")
    tmp = get_player_stats(username).json['stats'][category]

    print(f'{category.replace("_", " ").capitalize()} ')
    print(f'   Current stats: \n' 
          f'      Rating: {tmp["last"]["rating"]} \n'
          f'      Last update: {datetime.fromtimestamp(tmp["last"]["date"])}')

    print(f'   Best game: \n' 
          f'      Rating: {tmp["best"]["rating"]} \n'
          f'      Date: {datetime.fromtimestamp(tmp["best"]["date"])}\n'
          f'      Game: {tmp["best"]["game"]}')

    print(f'   Record: \n'
          f'      Draw: {tmp["record"]["draw"]} \n'
          f'      Loss: {tmp["record"]["loss"]} \n'
          f'      Win: {tmp["record"]["win"]} \n ')


def get_player_stats_by_category(username):
    var = input('Choose category (number) \n'
                '   1.Chess blitz \n'
                '   2.Chess bullet \n' 
                '   3.Chess rapid \n'
                '   4.Lessons \n'
                '   5.Puzzle rush \n'
                '   6.Tactics\n')
    match var:
        case '1':
            category_stats('chess_blitz', username)
        case '2':
            category_stats('chess_bullet', username)
        case '3':
            category_stats('chess_rapid', username)
        case '4':
            category_stats('lessons', username)
        case '5':
            category_stats('puzzle_rush', username)
        case '6':
            category_stats('tactics', username)                


def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    printer.pprint(game)

    
get_most_recent_game('kazikapa')