import random, pygame

def randomizer(array, nested = False):
    if type(array) is not list:
        raise TypeError
    temp_arr = array.copy()
    random_arr = []
    while temp_arr != []:
        selected = random.choice(temp_arr)
        if type(selected) is list and nested:
            temp_arr.remove(selected)
            selected = randomizer(selected, nested = True)
            random_arr.append(selected)
            continue
                 
        random_arr.append(selected)
        temp_arr.remove(selected)

    return random_arr


#pygame

def text(font, size, text, color , bgc = None):
    font = pygame.font.Font(font, size)
    text = font.render(text, True, color, bgc)
    return text


timer_dict = {
    'clock' : 0
}

def timer(time, cd):
    timer_dict['clock'] +=  1/60
    if time + timer_dict['clock'] >= time + cd:
        timer_dict['clock'] =  0
        return True
    return False


