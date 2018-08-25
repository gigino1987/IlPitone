# coding: cp1252
# Number guess game

# importing randrange function from random module for generating
# number to guess

from random import randrange   

# main function game

def main():
    # declare a variable and putting a number casually extracted from range 1-100. The right interval is excluded
    num = randrange(1, 101)
    # initiation of p and t variables. p = prompt and t = chances (tentativi in italian)
    p, t = 0, 1    
    while p != num:
        try:
            p = int(input('What number? '))
        except ValueError:
            print('Bad value, isn\'t a number.')
            continue
        if p > num:
            print('No, More low')
            t+=1
        elif p < num:
            print('No, more high')
            t+=1
        else:
            pass
    print('Oh! Great! Number is %d!'%(p))
    print('You guessed in %d chances!!'%(t))
    r = ""
    while (r != 'y') and (r != 'n'):
        r = input('Would you guess another number (y/n)? ').lower()
    if r == 'n':
        print('Ok, goodbye.')
        input('Press Enter to close.')
        exit()
    else:
        print('Ok, arriving another number.')
        main()

# Game intro
print('\n'*300)   # Cleaning screen
print('Guess number game.')
print('Guess a number between 1 and 100.')
input('Press Enter to start. ')   # input e non print quando il testo deve essere inserito dall'utente o attendere la pressione di invio
main()