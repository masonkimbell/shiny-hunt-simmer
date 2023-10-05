import json

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
        print(f'{route}')
    print('')
    selected_route = input()
    print(f'\n{selected_route} selected .')

    # select section of that route
    print(f'\nselect a section of {selected_region}-{selected_route}:')
    for section in routes[selected_region][selected_route]:
        # legendaries are locked for now
        if section != 'static-L' and section != 'odds':
            print(f'{section}')
    print('')
    selected_section = input()
    print(f'\n{selected_section} selected .')

    # grab encounter table for the specified selection
    enc_table = routes[selected_region][selected_route][selected_section]
    r = Route(selected_region, selected_route, selected_section, enc_table, odds)
    r.print()
    return r
