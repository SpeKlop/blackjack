from functions import randomizer
from settings import cards, gui_settings, run_settings

def new_game():
    run_settings['game_status'] = True
    deck = randomizer(cards)
    for i in range(2):
        gui_settings['player_hands'].append(deck[0])
        deck = deck[1:]
        gui_settings['bot_hands'].append(deck[0])
        deck = deck[1:]
    gui_settings['card_deck'] = deck

def hit():
    gui_settings['player_hands'].append(gui_settings['card_deck'][0])
    gui_settings['card_deck'] = gui_settings['card_deck'][1:]

def check():
    counter = 0
    ace = 0
    
    for card, value in gui_settings['player_hands']:
        if type(value) is tuple:
            ace += 1
            continue
        counter += value
    for i in range(ace):
        ace -= 1
        if counter + 11 <= 21:
            counter += 11
        elif counter + 1 <= 21:
            counter += 1
        else:
            counter += 1

    if counter > 21:
        return True      
    
    gui_settings['player_num'] = counter
    return False

def house():
    counter = 0
    while counter < 17:
        gui_settings['bot_hands'].append(gui_settings['card_deck'][0])
        gui_settings['card_deck'] = gui_settings['card_deck'][1:]
        ace = 0
        counter = 0
        for card, value in gui_settings['bot_hands']:
            if type(value) is tuple:
                ace += 1
                continue
            counter += value
        for i in range(ace):
            ace -= 1
            if counter + 11 <= 21:
                counter += 11
            elif counter + 1 <= 21:
                counter += 1
            else:
                counter += 1
        if counter > 21:
            return True 
    
    if counter > gui_settings['player_num']:
        return False
    elif counter < gui_settings['player_num']:
        return True
    elif counter == gui_settings['player_num']:
        return ()