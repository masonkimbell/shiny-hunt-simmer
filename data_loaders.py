import json
import random

from player import Player
from route import Route

def load_routes():
    with open('assets/routes.json', 'r+') as f:
        return json.load(f)

def load_players():
    try:
        with open('assets/player_data.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def select_player(players, name: str):
    try:
        players[name]
    except:
        print(f'hello new player {name} . initializing:')
        p = Player(name)
        p.save()
        return p

    p = Player(name, players[name]['encounters'], players[name]['dex'])
    print(f'hello returning player {name} .')
    return p

def select_route(routes):
    LOCKED_AREAS = ['birth_island', 'faraway_island']

    # select region
    print(f'\nselect a region:')
    for region in routes:
        print(f'{region}')
    print('')
    selected_region = input()
    print(f'\n{selected_region} selected .')

    odds = routes[selected_region]['odds']

    # select route in that region
    print(f'\nselect a route in {selected_region}:')
    for route in routes[selected_region]:
        if route != 'odds' and route not in LOCKED_AREAS:
            if 'mirage' in route:
                if random.randint(1, 5) == 1:
                    print(f'{route}')
            else:
                print(f'{route}')
    print('')
    selected_route = input()
    print(f'\n{selected_route} selected .')

    # exit if the only section of that route is a legendary encounter
    for key in routes[selected_region][selected_route].keys():
        if "static_legendary" not in key:
            break
        print('nothing here... yet')
        exit()

    # select section of that route
    print(f'\nselect a section of {selected_region}-{selected_route}:')
    for section in routes[selected_region][selected_route]:
        # legendaries are locked for now
        if section != 'static_legendary' and section != 'odds':
            print(f'{section}')
    print('')
    selected_section = input()
    print(f'\n{selected_section} selected .')

    # grab encounter table for the specified selection
    enc_table = routes[selected_region][selected_route][selected_section]
    r = Route(selected_region, selected_route, selected_section, enc_table, odds)
    r.print()
    return r
