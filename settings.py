import pygame
from functions import text
pygame.init()
run_settings = {
    'screen' : (800, 500), #x, y
    'game_status' : False,
    'fps' : 60,
    'game_result' : None
}

display_settings = {
    'bgc' : (218, 208, 208), #rgb
}

gui_settings = {
    'coins_text' : 'yellow',
    'player_coins' : 100,
    'player_bit' : None,

    'box_active_color' : 'grey',
    'box_inactive_color' : 'black',
    'box_color' : 'black',
    'box_text_color' : 'black',
    'box_text' : '',
    'active' : False,
    'status' : False,

    'player_hands' : [],
    'bot_hands' : [],
    'card_deck' : [],
    'player_num' : 0,
    'stay' : False

    
}

cards = [
    ['black_jack/cards/2_of_clubs.png', 2], 
    ['black_jack/cards/2_of_diamonds.png', 2], 
    ['black_jack/cards/2_of_hearts.png', 2], 
    ['black_jack/cards/2_of_spades.png', 2],
    ['black_jack/cards/3_of_clubs.png', 3], 
    ['black_jack/cards/3_of_diamonds.png', 3], 
    ['black_jack/cards/3_of_hearts.png', 3], 
    ['black_jack/cards/3_of_spades.png', 3],
    ['black_jack/cards/4_of_clubs.png', 4], 
    ['black_jack/cards/4_of_diamonds.png', 4], 
    ['black_jack/cards/4_of_hearts.png', 4], 
    ['black_jack/cards/4_of_spades.png', 4],
    ['black_jack/cards/5_of_clubs.png', 5], 
    ['black_jack/cards/5_of_diamonds.png', 5], 
    ['black_jack/cards/5_of_hearts.png', 5], 
    ['black_jack/cards/5_of_spades.png', 5],
    ['black_jack/cards/6_of_clubs.png', 6], 
    ['black_jack/cards/6_of_diamonds.png', 6], 
    ['black_jack/cards/6_of_hearts.png', 6], 
    ['black_jack/cards/6_of_spades.png', 6],
    ['black_jack/cards/7_of_clubs.png', 7], 
    ['black_jack/cards/7_of_diamonds.png', 7], 
    ['black_jack/cards/7_of_hearts.png', 7], 
    ['black_jack/cards/7_of_spades.png', 7],
    ['black_jack/cards/8_of_clubs.png', 8], 
    ['black_jack/cards/8_of_diamonds.png', 8], 
    ['black_jack/cards/8_of_hearts.png', 8], 
    ['black_jack/cards/8_of_spades.png', 8],
    ['black_jack/cards/9_of_clubs.png', 9], 
    ['black_jack/cards/9_of_diamonds.png', 9], 
    ['black_jack/cards/9_of_hearts.png', 9], 
    ['black_jack/cards/9_of_spades.png', 9],
    ['black_jack/cards/10_of_clubs.png', 10], 
    ['black_jack/cards/10_of_diamonds.png', 10], 
    ['black_jack/cards/10_of_hearts.png', 10], 
    ['black_jack/cards/10_of_spades.png', 10],
    ['black_jack/cards/ace_of_clubs.png', (1, 11)],  # Ace can be worth either 1 or 11
    ['black_jack/cards/ace_of_diamonds.png', (1, 11)], 
    ['black_jack/cards/ace_of_hearts.png', (1, 11)], 
    ['black_jack/cards/ace_of_spades.png', (1, 11)],
    ['black_jack/cards/black_joker.png', 0],  # Joker value is usually not fixed, you can assign as needed
    ['black_jack/cards/jack_of_clubs.png', 10], 
    ['black_jack/cards/jack_of_diamonds.png', 10], 
    ['black_jack/cards/jack_of_hearts.png', 10],
    ['black_jack/cards/jack_of_spades.png', 10],
    ['black_jack/cards/king_of_clubs.png', 10], 
    ['black_jack/cards/king_of_diamonds.png', 10], 
    ['black_jack/cards/king_of_hearts.png', 10], 
    ['black_jack/cards/king_of_spades.png', 10],
    ['black_jack/cards/queen_of_clubs.png', 10], 
    ['black_jack/cards/queen_of_diamonds.png', 10], 
    ['black_jack/cards/queen_of_hearts.png', 10],
    ['black_jack/cards/queen_of_spades.png', 10], 
    ['black_jack/cards/red_joker.png', 0]  # Joker value is usually not fixed, you can assign as needed
]


bit_box = pygame.Rect(run_settings['screen'][0]/2, run_settings['screen'][1]/2, 150, 30)
backward_card_img = pygame.image.load('black_jack\cards\card_backward.png')
backward_card_img = pygame.transform.scale(backward_card_img, (100, 170))
backward_card_rect = pygame.Rect(run_settings['screen'][0]/2 - 400, run_settings['screen'][1]/2 - 85, 100, 170)

stay_text = text(None, 32, 'Stay', 'black')
stay_text_rect = stay_text.get_rect()
stay_text_rect.midright = (run_settings['screen'][0] - 60, run_settings['screen'][1] - 50)