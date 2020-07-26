def display_board(board):
   # print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

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

def place_marker(board,marker,position):
    board[position] = marker
    display_board(board)

def win_check(board, mark):
    return ((board[1]==board[2]==board[3]==mark) or 
    (board[4]==board[5]==board[6]==mark) or 
    (board[7]==board[8]==board[9]==mark) or 
    (board[1]==board[4]==board[7]==mark) or 
    (board[2]==board[5]==board[8]==mark) or 
    (board[3]==board[6]==board[9]==mark) or 
    (board[1]==board[5]==board[9]==mark) or 
    (board[3]==board[5]==board[7]==mark))

from random import randint
def choose_first():
    if randint(0,1) == 0:
        return 'Player 1 choose first'
    else:
        return 'Player 2 choose first' 

def space_check(board,position):
    return board[position] == ' '



test_board = [' ']*10
display_board(test_board)