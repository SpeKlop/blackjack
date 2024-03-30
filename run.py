import pygame, sys
from settings import run_settings, gui_settings, bit_box, backward_card_rect, backward_card_rect, stay_text_rect
from gui import display, result_display
from game import new_game, hit, check, house
def main_run():
    pygame.init()
    screen = pygame.display.set_mode(run_settings['screen'], pygame.RESIZABLE)
    clock = pygame.time.Clock()
    while True:
        if run_settings['game_result'] == None:
            display(screen)
        if run_settings['game_result'] == 'won':
            result_display(screen)
        elif run_settings['game_result'] == 'tie':
            result_display(screen)
        elif run_settings['game_result'] == 'lose':
            result_display(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:          
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                


                if not run_settings['game_status']:

                    if bit_box.collidepoint(event.pos):
                        gui_settings['box_color'] = gui_settings['box_active_color']
                        
                    else:
                        gui_settings['box_color'] = gui_settings['box_inactive_color']
                else:
                    if backward_card_rect.collidepoint(event.pos):
                        hit()
                
                if stay_text_rect.collidepoint(event.pos):
                    print('stay')
                    house_status = house()
                    if house_status == True:
                        print('You won')
                        run_settings['game_status'] = False
                        gui_settings['player_hands'] = []
                        gui_settings['bot_hands'] = []
                        gui_settings['player_num'] = 0
                        gui_settings['player_coins'] += gui_settings['player_bit'] * 2
                        run_settings['game_result'] = 'won'
                    if type(house_status) is tuple:
                        print('Tie')
                        run_settings['game_status'] = False
                        gui_settings['player_hands'] = []
                        gui_settings['bot_hands'] = []
                        gui_settings['player_num'] = 0
                        run_settings['game_result'] = 'tie'
                        
                        gui_settings['player_coins'] += gui_settings['player_bit']
                    if house_status == False:
                        print('You lose')
                        run_settings['game_status'] = False
                        gui_settings['player_hands'] = []
                        gui_settings['bot_hands'] = []
                        gui_settings['player_num'] = 0
                        run_settings['game_result'] = 'lose'

                    
                        

            
            if event.type == pygame.KEYDOWN:
                if run_settings['game_result'] != None:

                    if event.key == pygame.K_RETURN:
                        run_settings['game_result'] = None

                if (run_settings['game_status'] == False) and (gui_settings['box_active_color'] == gui_settings['box_color']):
                    if event.key == pygame.K_RETURN:
                        try:
                            if int(gui_settings["player_coins"]) >= int(gui_settings['box_text']):
                                gui_settings["player_coins"] =  int(gui_settings["player_coins"]) - int(gui_settings['box_text'])
                                gui_settings['player_bit'] = int(gui_settings['box_text'])
                                new_game()
                                gui_settings['box_color'] = gui_settings['box_inactive_color']
                            else:
                                gui_settings['box_text'] = 'You dont have enought money'

                                continue
                        except:
                            if TypeError:
                                gui_settings['box_text'] = 'Only numbers is allowed to bit'
                                continue
                        gui_settings['box_text'] = ''
                    elif event.key == pygame.K_BACKSPACE:
                        gui_settings['box_text'] = gui_settings['box_text'][:-1]
                    else:
                        gui_settings['box_text'] += event.unicode
                

                
                    
            
        if run_settings['game_status']:
            if check():
                print('You lose')
                run_settings['game_status'] = False
                gui_settings['player_hands'] = []
                gui_settings['bot_hands'] = []
                gui_settings['player_num'] = 0
                run_settings['game_result'] = 'lose'



                


        clock.tick(run_settings['fps'])


        run_settings['screen'] = screen.get_size()



        
        
        