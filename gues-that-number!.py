'''This is a game.'''
def run():
    import time
    print('importing nessasary modules...')
    import random
    print('Complete!')
    print('')
    print('guess that N U M B E R')
    ranNum = random.randint(0, 10)
    guess = int(input(int))
    while guess != ranNum:
        if guess > ranNum:
            print(' to High!')
            guess = int(input(int))

        elif guess < ranNum:
            print("to low")
            guess = int(input(int))
            
    print("CORRECT!!!!")
 
    
