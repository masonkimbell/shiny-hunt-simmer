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
            enc_rate = self.encounter_rates[idx] if self.encounter_rates[idx] <= 99 else 99
            try:
                enc_list += f' - {self.map[self.encounters[idx]].split("_")[0]} ({self.map[self.encounters[idx]].split("_")[1]}) @ {enc_rate}%\n'
            except IndexError:
                enc_list += f' - {self.map[self.encounters[idx]]} @ {enc_rate}%\n'
        print(enc_list)

    def start_huntin(self, player: Player):

        def signal_handler(sig, frame):
            print(f'\nexit detected . saving {player.name}...')
            player.save()
            print(f'progress for {player.name} saved .\n')
            player.print()
            print('goodbye .')
            exit()

        print('enter ctrl-c to stop hunting .\n')

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
                print(f'{count} - yes {self.map[p].split("_")[0]} ({self.map[p].split("_")[1]})!')

                # if regional form, deal with that !!!
                dexno_and_form = p.split('_')
                dexno = dexno_and_form[0]
                name = self.map[p].split('_')[0]


                # set found time, count, add name to pokedex
                if not player.dex[dexno]['found_at']:
                    player.dex[dexno]['found_at'] = time.time()
                player.dex[dexno]['found_count'] += 1
                player.dex[dexno]['name'] = name

                # set what regions this pokemon has been found in
                if self.region_name not in player.dex[dexno]['found_in']:
                    player.dex[dexno]['found_in'].append(self.region_name)
                
                # set what form has been found if this pokemon has multiple forms
                if len(dexno_and_form) > 1:
                    form = dexno_and_form[1]
                    if form not in player.dex[dexno]['forms']:
                        player.dex[dexno]['forms'].append(form)

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