cells = input("Enter cells: ").replace("_", " ")
cells = list(cells)

field = [
    [cells[0], cells[1], cells[2]],
    [cells[3], cells[4], cells[5]],
    [cells[6], cells[7], cells[8]]
]

count_x = sum(x.count("X") for x in field)
count_o = sum(o.count("O") for o in field)


def display_field():
    print("---------")
    print("|", field[0][0], field[0][1], field[0][2], "|")
    print("|", field[1][0], field[1][1], field[1][2], "|")
    print("|", field[2][0], field[2][1], field[2][2], "|")
    print("---------")


display_field()


def is_empty(x, y):
    col = int(x) - 1
    row = 3 - int(y)

    return field[row][col] == " "


def place(x, y):
    col = int(x) - 1
    row = 3 - int(y)

    field[row][col] = "X"


while True:
    move = input("Enter the coordinates: ")
    coords = move.split(" ")
    if coords[0].isalpha() or coords[1].isalpha():
        print("You should enter numbers!")
    elif 1 > (int(coords[0]) or int(coords[1])) or (int(coords[0]) or int(coords[1])) > 3:
        print("Coordinates must be from 1 to 3!")
    elif not is_empty(coords[0], coords[1]):
        print("This cell is occupied! Choose another one!")
    else:
        place(coords[0], coords[1])
        display_field()
        break


def check_rows(symbol):
    for i in range(0, 3):
        if field[i][0] == symbol \
                and field[i][1] == symbol \
                and field[i][2] == symbol:
            return True
    return False


def check_columns(symbol):
    for i in range(0, 3):
        if field[0][i] == symbol \
                and field[1][i] == symbol \
                and field[2][i] == symbol:
            return True
    return False


def check_diagonals(symbol):
    return field[1][1] == symbol and \
           ((field[0][0] == symbol and field[2][2] == symbol) or (field[0][2] == symbol and field[2][0] == symbol))


def check_win(symbol):
    return check_rows(symbol) or check_columns(symbol) or check_diagonals(symbol)


def check_draw():
    return not (check_win("X") and check_win("O"))


def in_game(array):
    return any(" " in x for x in array) and not (check_win("X") or check_win("O"))


def is_impossible():
    return abs(count_o - count_x) >= 2 or (check_win("X") and check_win("O"))


if is_impossible():
    print("Impossible")
elif check_win("X"):
    print("X wins")
elif check_win("O"):
    print("O wins")
elif in_game(field):
    print("Game not finished")
elif check_draw():
    print("Draw")
