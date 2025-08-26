
def tic_tac_toe(board):
    print('starts the game ..')
    current = 'x'

    for i in range(9):

        pos=int(input('enter row position'))
        pos2=int(input('enter column position'))
        board[pos][pos2]=current
        if current =='x':
            current='o'
        else:
            current='x'
        print(board[0],'\n',board[1],'\n', board[2])
        # checking diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            print('{} wins..!'.format(board[0][0]))
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            print('{} wins..!'.format(board[0][2]))
            return board[0][2]
        # checking columns and rows
        elif board[0][0] == board[0][1] == board[0][2] and board[0][0] != ' ':
            print('{} wins..!'.format(board[0][0]))
            return board[0][0]
        elif board[0][0] == board[1][0] == board[2][0] and board[0][0] != ' ':
            print('{} wins..!'.format(board[0][0]))
            return board[0][0]
        elif board[0][1] == board[1][1] == board[2][1] and board[0][1] != ' ':
            print('{} wins..!'.format(board[0][1]))
            return board[0][1]
        elif board[1][0] == board[1][1] == board[1][2] and board[1][0] != ' ':
            print('{} wins..!'.format(board[1][0]))
            return board[1][0]
        elif board[0][2] == board[1][2] == board[2][2] and board[0][2] != ' ':
            print('{} wins..!'.format(board[0][2]))
            return board[0][2]
        elif board[2][0] == board[2][1] == board[2][2] and board[2][0] != ' ':
            print('{} wins..!.'.format(board[2][0]))
            return board[2][0]

    return None



board=[
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]

win=tic_tac_toe(board)
if win == None:
    print('its draw')
