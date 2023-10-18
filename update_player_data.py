import json
from data_loaders import load_players

players = load_players()

with open('assets/map.json', 'r') as f:
    map = json.load(f)

for player in players:
    for pkmn in players[player]['dex']:
        form_list = []
        found_in = []
        if players[player]['dex'][pkmn]['name']:
            found_in = ['hoenn']
            dexno = int(pkmn)
            if dexno >= 1 and dexno <= 151:
                try:
                    map[pkmn]
                except KeyError:
                    form_list = ['kanto']
            elif dexno >= 152 and dexno <= 251:
                try:
                    map[pkmn]
                except KeyError:
                    form_list = ['johto']
            elif dexno >= 252 and dexno <= 386:
                try:
                    map[pkmn]
                except KeyError:
                    form_list = ['hoenn']
        players[player]['dex'][pkmn]['found_in'] = found_in      
        players[player]['dex'][pkmn]['forms'] = form_list

with open('assets/player_data.json', 'r+') as f:
    json.dump(players, f, indent=4)