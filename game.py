def display(board):
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])


test_board = ['a', 'b', 'c',
              'a', 'b', 'c',
              'a', 'b', 'c', ]

display(test_board)
