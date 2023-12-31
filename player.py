import json

class Player:
    def __init__(self, name, encounters=None, dex=None):
        self.name = name
        if not encounters:
            encounters = 0
        self.encounters = encounters
        if not dex:
            dex = self.setup_dex()
        self.dex = dex

    def setup_dex(self):
        out = {}

        start = 1

        while start <= 1017:
            if start < 10:
                key = f'000{str(start)}'
            elif start < 100:
                key = f'00{str(start)}'
            elif start < 1000:
                key = f'0{str(start)}'
            else:
                key = str(start)
            out[key] = {
                'name': None,
                'found_at': None,
                'found_count': 0,
                'found_in': [],
                'forms': []
            }
            start += 1

        return out

    def print(self):
        print(f'printing stats for {self.name}...\n')
        print(f'encounters done: {self.encounters}')
        for pkmn in self.dex:
            if self.dex[pkmn]['found_at']:
                if len(self.dex[pkmn]['forms']) > 1:
                    print(f'{self.dex[pkmn]["name"]} x{self.dex[pkmn]["found_count"]} {self.dex[pkmn]["forms"]}')
                else:
                    print(f'{self.dex[pkmn]["name"]} x{self.dex[pkmn]["found_count"]}')
        print('')

    def save(self):
        try:
            with open('assets/player_data.json', 'r') as f:
                player_data = json.load(f)
        except:
            with open('assets/player_data.json', 'x') as f:
                out = {
                    self.name: {
                        'encounters': self.encounters,
                        'dex': self.dex
                    }
                }
                json.dump(out, f, indent=4)
                return

        player_data[self.name]['encounters'] = self.encounters
        player_data[self.name]['dex'] = self.dex
        with open('assets/player_data.json', 'w') as f:
            json.dump(player_data, f, indent=4)
