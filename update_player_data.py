import json
from data_loaders import load_players

players = load_players()

for player in players:
    for pkmn in players[player]['dex']:
        form_list = []
        found_in = []
        if players[player]['dex'][pkmn]['name']:
            found_in = ['hoenn']
            dexno = int(pkmn)
            if dexno >= 1 and dexno <= 151:
                form_list = ['kanto']
            elif dexno >= 152 and dexno <= 251:
                form_list = ['johto']
            elif dexno >= 252 and dexno <= 386:
                form_list = ['hoenn']
        players[player]['dex'][pkmn]['found_in'] = found_in      
        players[player]['dex'][pkmn]['forms'] = form_list

with open('assets/player_data.json', 'r+') as f:
    json.dump(players, f, indent=4)