from random import shuffle
import time

print('Hey There!''\n''Welcome To The Code Carnival!!''\n''Lets Play THREE CUP MONTE')
time.sleep(1)
print('There Is A BALL Under One Of These Cups,Lets See If U Can Guess!!')
time.sleep(1)
print('\n', '\n')

picture = [
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 'A', 0, 1, 0, 0, 0, 1, 0, 'B', 0, 1, 0, 0, 0, 1, 0, 'C', 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
]


def ui(picture):

    for row in picture:
        for item in row:
            if item == 1:
                print('#', end='')
            elif item == 'A':
                print('0', end='')
            elif item == 'B':
                print('1', end='')
            elif item == 'C':
                print('2', end='')
            else:
                print(' ', end='')
        print('')


ui(picture)

main_list = ['', '', '0']

def shuffle_list(x):
    shuffle(main_list)
    return main_list


mixed_list = shuffle_list(main_list)



def player_guess():
    guess = []
    while guess not in ['0', '1', '2']:
        guess = input('\n'"choose a cup between 0 , 1 or 2"'\n')
    return int(guess)


guess = player_guess()


def guess_checker(mixed_list, guess):
    if mixed_list[guess] == '0':
        print('Congrats!You Got The Right One!!!')
    else:
        print('Pfff...Wrong Cup')
        if mixed_list[0] == '0':
            print('The Ball Was In Cup Number 0')
        elif mixed_list[1] == '0':
            print('The Ball Was In Cup Number 1')
        else:
            print('The Ball Was In Cup Number 2')


guess_checker(mixed_list, guess)
