from random import randint
#DECLARING ALL THE FUNCTIONS
#diplay the tic tac toe board
def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
#Ask for player input 'X' or'O' and assign the other player the opposite marker
def player_input():
    marker = ''
    #KEEP ASKING PLAYER 1 TO CHOOSE X OR O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    #ASSIGN PLAYER 2, THE OPPOSITE MARKER
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
#Assign the marker at a position on the board
def place_marker(board,marker,position):
    board[position] = marker
    display_board(board)
#Check whether any player has won or not
def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or 
    (board[1]==board[5]==board[9]==mark) or 
    (board[3]==board[5]==board[7]==mark))
#Randomly choose which player start first
def choose_first():
    if randint(0,1) == 0:
        return 'Player 1 will go first'
    else:
        return 'Player 2 will go first'
#Check whether the entered position is empty or not
def space_check(board,position):
    return board[position] == ' '
#Check whether the full board is empty or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
#Ask the user to input position and check whether it is available or not
def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Enter your next position (1-9): "))
    return position
#Ask the user whether they want to play again or not
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#THE MAIN PART:
print('Welcome to Tic Tac Toe Game !')

while True:
    #Board Reset
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn)
    play_game = input('Are you ready to play? Enter Yes or No: ')
    if play_game.lower()[0] == 'y':
        game_on = 'True'
    else:
        game_on = 'False'
    
    while game_on:
        #Player 1 turn
        if turn == 'Player 1 will go first':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1_marker,position)
            #Check after chance whether win?
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Congratulations! You have won the game Player 1!')
                game_on = False
            #If after chance not win, chance goes to Player 2 or it is a tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie')
                    break
                else:
                    turn = 'Player 2 will go first'
        #PLAYER 2 TURN
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker,position)
            #Check after chance whether win?
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congratulation! You have won the game Player 2!') 
                game_on = False
            #If after chance not win, chance goes to Player 1 or it is a tie
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a tie')
                    break
                else:
                    turn = 'Player 1 will go first'
#replay() condition False, then:
    if not replay():
        break