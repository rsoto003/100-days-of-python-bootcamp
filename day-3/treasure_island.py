print('''
************************************************
                        _             
                       (_)            
 _ __ _   _ _ __  _ __  _ _ __   __ _ 
| '__| | | | '_ \| '_ \| | '_ \ / _` |
| |  | |_| | | | | | | | | | | | (_| |
|_|   \__,_|_| |_|_| |_|_|_| |_|\__, |
                                 __/ |
                                |___/ 
                                

************************************************
'''
)

print('welcome to treasure island')
print('your mission is to find the treasure.')

if input('You\'re at a crossroad, where do you want to go? Type "left" or "right" to continue. > ').lower() == 'left':
    if input('You\'re at a river. would you like to swim through? or would you like to wait? > ').lower() == 'wait':
        color = input('Pick a color: red, yellow or blue. > ')
        if color.lower() == 'yellow':
            print('\n\n\t\t$$$$$$$$$$ YOU WIN!!! $$$$$$$$$$')
        elif color.lower() == 'red':
            print('Whoops. Burned by fire. \n\n\t\t ******** GAME OVER. ********')
        elif color.lower() == 'blue':
            print('Darn. Eaten by beasts. \n\n\t\t ******** GAME OVER. ********')
        else:
            print('That was not an option. \n\n\t\t ******** GAME OVER. ********')
    else:
        print('NO!! You were attacked by a GIANT TROUT! \n\n\t\t ******** GAME OVER. ********')
else:
    print('oh no! you fell into a booby trap. \n\n\t\t ******** GAME OVER. ********')
