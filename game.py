def display(board):
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])


test_board = ['a', 'b', 'c',
              'a', 'b', 'c',
              'a', 'b', 'c', ]


def player_input():
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


player1_marker, player2_marker = player_input()

display(test_board)
player_input()
