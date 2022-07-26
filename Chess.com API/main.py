from chessdotcom import get_leaderboards
import pprint

printer = pprint.PrettyPrinter()


def print_leaderboards():

    data = get_leaderboards().json
    # printer.pprint(data)

    categories = data['leaderboards']
    # printer.pprint(categories)

    for category in categories:
        print('Category: ', category)
        for idx, entry in enumerate(categories[category]):
            print(entry)



print_leaderboards()