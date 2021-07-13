
# Main game cycle
def play_game():
    # FILLER
    f = "-"

    # GAME FIELD
    matrix = [[f] * 3 for i in range(3)]

    # TURN MARKER
    piece = 'X'

    # DRAWING A FIELD
    def show_field():
        print('-------')
        print('  0 1 2')
        for i in range(3):
            print(i, " ".join(map(str, matrix[i])))
        print('-------')

    # CHECKING USER INPUT
    def get_move():
        s = piece + ': '
        while True:
            x = input('row for ' + s)
            y = input('col for ' + s)

            if not (x.isdigit()) or not (y.isdigit()):
                print('_____________________________')
                print(" Only digits 0..2 acceptable! ")
                print('-----------------------------')
                show_field()
                continue

            x, y = int(x), int(y)

            if 0 > x or x > 2 or 0 > y or y > 2:
                print('_____________________________')
                print(" Only digits 0..2 acceptable! ")
                print('-----------------------------')
                show_field()
                continue

            if matrix[x][y] != f:
                print('____________________')
                print(" Choose another move! ")
                print('---------------------')
                show_field()
                continue

            return x, y

    # CHECKING FOR WINNER
    def check_winner():

        # CHECK HORIZONTAL
        for r in range(3):
            if matrix[r][0] == piece and matrix[r][1] == piece and matrix[r][2] == piece:
                return True
        # CHECK VERTICAL
        for c in range(3):
            if matrix[0][c] == piece and matrix[1][c] == piece and matrix[2][c] == piece:
                return True

        # CHECK DIAGONAL 1
        if matrix[0][0] == piece and matrix[1][1] == piece and matrix[2][2] == piece:
            return True

        # CHECK DIAGONAL 2
        if matrix[0][2] == piece and matrix[1][1] == piece and matrix[2][0] == piece:
            return True

    def check_draw():
        draw = True
        for i in range(3):
            if f in matrix[i]:
                draw = False
        return draw

    while True:
        show_field()
        x, y = get_move()
        matrix[x][y] = piece

        if check_winner():
            print('****************')
            print('  '+piece + ' is winner!')
            print('****************')
            return True

        if check_draw():
            print('****************')
            print('   nobody wins')
            print('****************')
            return False

        if piece == 'X':
            piece = '0'
        else:
            piece = 'X'


"""Starting game"""
while True:
    print('***************************************')
    c = input('Do you want to play in Tic Toc game? (y/n)')
    print('***************************************')

    if c == 'y' or c == 'Y':
        if play_game():
            print ('\n\nWow! it was cool!\n')
        else:
            print('\n\nHeh.. There was two equal competitors\n')
    else:
        print('**********************************')
        print('******** Good bye! ***************')
        print('**********************************')
        break
