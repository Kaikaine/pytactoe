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


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[0] == board[1] == board[2] == mark) or
            (board[3] == board[4] == board[5] == mark) or
            (board[6] == board[7] == board[8] == mark) or

            (board[0] == board[3] == board[6] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or

            (board[6] == board[4] == board[2] == mark) or
            (board[8] == board[4] == board[0] == mark))


player_input()
place_marker(test_board, '$', 8)
display(test_board)
win_check(test_board, 'X')
