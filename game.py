import random


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


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):

    for i in range(0, 8):
        if space_check(board, i):
            return False
    # board full
    return True


def player_choice(board):
    position = 9

    while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8] or not space_check(board, position):
        position = int(input('Choose a position: (0-8) '))

    return position


def replay():

    choice = input("Play again? Y/N: ")

    return choice == "Y"

# player_input()
# place_marker(test_board, '$', 8)
# display(test_board)
# win_check(test_board, 'X')


print('Welcome to Py Tac Toc')

while True:

    # Play game

    game_board = [' ']*10

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Y/N ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':
            display(game_board)

            position = player_choice(game_board)

            place_marker(game_board, player1_marker, position)

            if win_check(game_board, player1_marker):
                display(game_board)
                print("Player 1 wins")
                game_on = False
            else:
                if full_board_check(game_board):
                    display(game_board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player 2"

        else:
            display(game_board)

            position = player_choice(game_board)

            place_marker(game_board, player2_marker, position)

            if win_check(game_board, player2_marker):
                display(game_board)
                print("Player 2 wins")
                game_on = False
            else:
                if full_board_check(game_board):
                    display(game_board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player 1"
    if not replay():
        break
