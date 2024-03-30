import pygame
from functions import text
from settings import display_settings, run_settings, gui_settings, bit_box, backward_card_img, backward_card_rect, stay_text, stay_text_rect
def display(screen):
    run_settings['game_result'] = None
    screen.fill(display_settings['bgc'])

    coins = text('black_jack\\text_fonts\open-sans\OpenSans-Regular.ttf', 32, f'{gui_settings["player_coins"]}', gui_settings['coins_text'])
    coins_rect = coins.get_rect()
    coins_rect.topright = (run_settings['screen'][0] - 40, 20)
    screen.blit(coins, coins_rect)

    if not run_settings['game_status']:
        your_bit_text = text('black_jack\\text_fonts\open-sans\OpenSans-Regular.ttf', 32, f'Your bit', 'black')
        your_bit_text_rect = your_bit_text.get_rect()
        your_bit_text_rect.center = (run_settings['screen'][0]/2, run_settings['screen'][1]/2 - 50)
        screen.blit(your_bit_text, your_bit_text_rect)

        box_input_text = text(None, 32, gui_settings['box_text'], gui_settings['box_text_color'])
        box_input_text_rect = box_input_text.get_rect()
        box_input_text_rect.center = (run_settings['screen'][0]/2, run_settings['screen'][1]/2)
        bit_box.center = (run_settings['screen'][0]/2, run_settings['screen'][1]/2)
        screen.blit(box_input_text, box_input_text_rect)
        width = max(200, box_input_text.get_width() + 10)
        bit_box.width = width
        pygame.draw.rect(screen, gui_settings['box_color'], bit_box, 2)
    
    
    if run_settings['game_status']:
        
        
        screen.blit(stay_text, stay_text_rect)
        screen.blit(backward_card_img, backward_card_rect)
        player_hands, bot_hands = (gui_settings['player_hands'], gui_settings['bot_hands'])
        
        x = 0
        for card, val in player_hands:
            card_img = pygame.image.load(card)
            card_img = pygame.transform.scale(card_img, (100, 170))
            screen.blit(card_img, (run_settings['screen'][0]/2 - 25 * len(player_hands) + x, run_settings['screen'][1] - 170 - 30))
            x += 50
        
        x = 0
        for card_index in range(len(bot_hands)):
            if card_index == 0: 
                card_img = pygame.image.load(bot_hands[card_index][0])
            else:
                if gui_settings['stay']:
                    card_img = pygame.image.load(bot_hands[card_index][0])
                else:
                    card_img = pygame.image.load('black_jack\cards\card_backward.png')
            card_img = pygame.transform.scale(card_img, (100, 170))
            screen.blit(card_img, (run_settings['screen'][0]/2 - 25 * len(bot_hands) + x, 0 + 30))
            x += 50


    pygame.display.update()

def result_display(screen):
    screen.fill(display_settings['bgc'])

    

    if run_settings['game_result'] == 'won':
        won_text = text(None, 50, f'You won {gui_settings["player_bit"]} coins', 'green')
        won_text_rect = won_text.get_rect()
        won_text_rect.center = (run_settings['screen'][0] / 2, run_settings['screen'][1] / 2)
        screen.blit(won_text, won_text_rect)
    elif run_settings['game_result'] == 'tie':
        tie_text = text(None, 50, f'It s Tie', 'black')
        tie_text_rect = tie_text.get_rect()
        tie_text_rect.center = (run_settings['screen'][0] / 2, run_settings['screen'][1] / 2)
        screen.blit(tie_text, tie_text_rect)
    elif run_settings['game_result'] == 'lose':
        lose_text = text(None, 50, f'You lose -{gui_settings["player_bit"]} coins', 'red')
        lose_text_rect = lose_text.get_rect()
        lose_text_rect.center = (run_settings['screen'][0] / 2, run_settings['screen'][1] / 2)
        screen.blit(lose_text, lose_text_rect)
    
    continue_text = text(None, 29, f'For continue press enter', 'black')
    continue_text_rect = continue_text.get_rect()
    continue_text_rect.center = (run_settings['screen'][0] / 2, run_settings['screen'][1] / 2 + 50)
    screen.blit(continue_text, continue_text_rect)


    
    pygame.display.update()
