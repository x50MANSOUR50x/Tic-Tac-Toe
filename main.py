from os import system
from time import sleep

blocks = ''' 
  1 | 2 | 3
-------------
  4 | 5 | 6
-------------
  7 | 8 | 9
    '''

blocks_avaliable = [1, 2, 3, 4, 5, 6, 7, 8, 9]

system('cls')
print("Welcome to Tic Tac Toe Game :)")
sleep(3)
system('cls')

game_on = True

player1_won = False
player2_won = False

while(game_on):
    counter = 0

    #system('cls')

    print(blocks)

    player1 = input("Player 1 where Would you like to play:\n")
    while(int(player1) not in blocks_avaliable):
        print("Enter a number for an avaliable place")
        print(blocks)
        player1 = input("Player 1 where Would you like to play:\n")
    blocks = blocks.replace(player1, 'X')
    blocks_avaliable.remove(int(player1))
    blocks_avaliable.insert(int(player1) - 1, 'X')

    print(blocks)

    for number in range(1, 10):
        if(number not in blocks_avaliable):
            counter += 1
    
    if(counter >= 9):
        print("Player 1 draws with Player 2 !!!")
        break

    for index in range(0, 8, 3):
        if(blocks_avaliable[index] == 'X' and blocks_avaliable[index + 1] == 'X' and blocks_avaliable[index + 2] == 'X'):
            print("Player 1 won ;)")
            player1_won = True
            break
        if(blocks_avaliable[index] == 'O' and blocks_avaliable[index + 1] == 'O' and blocks_avaliable[index + 2] == 'O'):
            print("Player 2 won ;)")
            player2_won = True
            break

    for index in range(0, 3):
        if(blocks_avaliable[index] == 'X' and blocks_avaliable[index + 3] == 'X' and blocks_avaliable[index + 6] == 'X'):
            print("Player 1 won ;)")
            player1_won = True
            break
        if(blocks_avaliable[index] == 'O' and blocks_avaliable[index + 3] == 'O' and blocks_avaliable[index + 6] == 'O'):
            print("Player 2 won ;)")
            player2_won = True
            break

    if(blocks_avaliable[0] == 'X' and blocks_avaliable[4] == 'X' and blocks_avaliable[8] == 'X'):
        print("Player 1 won ;)")
        player1_won = True
        break

    if(blocks_avaliable[0] == 'O' and blocks_avaliable[4] == 'O' and blocks_avaliable[8] == 'O'):
        print("Player 2 won ;)")
        player2_won = True
        break

    if(blocks_avaliable[3] == 'X' and blocks_avaliable[5] == 'X' and blocks_avaliable[7] == 'X'):
        print("Player 1 won ;)")
        player1_won = True
        break

    if(blocks_avaliable[3] == 'O' and blocks_avaliable[5] == 'O' and blocks_avaliable[7] == 'O'):
        print("Player 2 won ;)")
        player2_won = True
        break

    if(player1_won or player2_won):
        break

    player2 = input("Player 2 where Would you like to play:\n")
    while(int(player2) not in blocks_avaliable):
        print("Enter a number for an avaliable place")
        print(blocks)
        player2 = input("Player 2 where Would you like to play:\n")
    blocks = blocks.replace(player2, 'O')
    blocks_avaliable.remove(int(player2))
    blocks_avaliable.insert(int(player2) - 1, 'O')

    print(blocks)

    for index in range(0, 8, 3):
        if(blocks_avaliable[index] == 'X' and blocks_avaliable[index + 1] == 'X' and blocks_avaliable[index + 2] == 'X'):
            print("Player 1 won ;)")
            player1_won = True
            break
        if(blocks_avaliable[index] == 'O' and blocks_avaliable[index + 1] == 'O' and blocks_avaliable[index + 2] == 'O'):
            print("Player 2 won ;)")
            player2_won = True
            break

    for index in range(0, 3):
        if(blocks_avaliable[index] == 'X' and blocks_avaliable[index + 3] == 'X' and blocks_avaliable[index + 6] == 'X'):
            print("Player 1 won ;)")
            player1_won = True
            break
        if(blocks_avaliable[index] == 'O' and blocks_avaliable[index + 3] == 'O' and blocks_avaliable[index + 6] == 'O'):
            print("Player 2 won ;)")
            player2_won = True
            break
    
    if(blocks_avaliable[0] == 'X' and blocks_avaliable[4] == 'X' and blocks_avaliable[8] == 'X'):
        print("Player 1 won ;)")
        player1_won = True
        break

    if(blocks_avaliable[0] == 'O' and blocks_avaliable[4] == 'O' and blocks_avaliable[8] == 'O'):
        print("Player 2 won ;)")
        player2_won = True
        break

    if(blocks_avaliable[2] == 'X' and blocks_avaliable[4] == 'X' and blocks_avaliable[6] == 'X'):
        print("Player 1 won ;)")
        player1_won = True
        break

    if(blocks_avaliable[2] == 'O' and blocks_avaliable[4] == 'O' and blocks_avaliable[6] == 'O'):
        print("Player 2 won ;)")
        player2_won = True
        break

    if(player1_won or player2_won):
        break


sleep(5)
system('cls')
print("Thank you for tring Tic Tac Toe game !!!")
sleep(3)
system('cls')

