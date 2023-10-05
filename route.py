import json
import random
import signal
import sys
import time

from player import Player

class Route:
    def __init__(self, region_name: str, route_name: str, sec_name: str, section: dict, odds: int):
            self.encounters = []
            self.encounter_rates = []
            self.region_name = region_name
            self.route_name = route_name
            self.sec_name = sec_name
            self.odds = odds

            with open('assets/map.json', 'r') as f:
                self.map = json.load(f)

            for enc in section['encounters']:
                self.encounters.append(enc)
                self.encounter_rates.append(section['encounters'][enc])

    def print(self):
        enc_list = f'\nencounters on {self.name}:\n'
        for idx, _ in enumerate(self.encounters):
            enc_list += f' - {self.map[self.encounters[idx]]} @ {self.encounter_rates[idx]}%\n'
        print(enc_list)

    def start_huntin(self, player: Player):

        def signal_handler(sig, frame):
            print(f'exit detected . saving {player.name}...')
            player.save()
            print(f'progress for {player.name} saved . goodbye .')
            exit()

        # give user time to read the menus
        time.sleep(10)

        choices = self.encounters
        weights = self.encounter_rates
        odds = self.odds

        count = 1

        while True:
            p = random.choices(choices, weights=weights)[0]
            s = random.randint(1, odds)
            if s == 1:
                print(f'{count} - yes {self.map[p]} !')
                if not player.dex[p]['found_at']:
                    player.dex[p]['found_at'] = time.time()
                player.dex[p]['found_count'] += 1
                player.dex[p]['name'] = self.map[p]
                player.save()
            else:
                print(f'{count} - no .')
            count += 1
            player.encounters += 1
            signal.signal(signal.SIGINT, signal_handler)
            time.sleep(0.2)


    @property
    def name(self):
        return f'{self.region_name}-{self.route_name}-{self.sec_name}'