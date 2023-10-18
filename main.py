from data_loaders import load_routes, load_players, select_route, select_player

if __name__ == '__main__':

    # add evolutions
    # add legendaries
    # add things like dexnav, hordes, etc

    players = load_players()

    if players:
        for player in players:
            name = player
    else:
        print('hello . enter your name .')
        name = input()

    p = select_player(players, name)
    
    routes = load_routes()

    r = select_route(routes)

    r.start_huntin(p)
