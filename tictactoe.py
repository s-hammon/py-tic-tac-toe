WIN_ROWS = ({0, 1, 2}, {3, 4, 5}, {6, 7, 8},
            {0, 3, 6}, {1, 4, 7}, {2, 5, 8},
            {0, 4, 8}, {2, 4, 6})

SYMBOL_X = "X"
SYMBOL_O = "O"
SYMBOL_EMPTY = " "


def convert_coordinates(x, y):
    return (x - 1) + (3 * (3 - y))


def is_empty(x, y):
    """Checks if a selected cell is empty."""
    return field[convert_coordinates(x, y)] == SYMBOL_EMPTY


def validate_input(coordinates):
    global input_x
    global input_y

    try:
        input_x, input_y = [int(i) for i in coordinates.split()]
    except ValueError:
        print("You should enter numbers!")
        return False

    if 1 > (input_x or input_y) or (input_x or input_y) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif not is_empty(input_x, input_y):
        print("This cell is occupied! Choose another one!")
        return False

    return True


def is_winner(symbol):
    this_pos = {i for i in range(len(field)) if field[i] == symbol}

    for x in WIN_ROWS:
        if this_pos.issuperset(x):
            return True

    return False


def check_win():
    global winner
    if is_winner(SYMBOL_X):
        winner = SYMBOL_X
    elif is_winner(SYMBOL_O):
        winner = SYMBOL_O


def no_more_turns():
    return field.count(SYMBOL_EMPTY) == 0


def finished():
    return no_more_turns() or winner is not None


def end_game():
    if winner is not None:
        print(f"{winner} wins")
    elif no_more_turns():
        print("Draw")


def place(x, y, char):
    field[convert_coordinates(x, y)] = char


def display_field():
    """Displays field in console."""

    print(9 * "-")
    for row in range(3):
        print("|", " ".join(field[row * 3: 3 + row * 3]), "|")
    print(9 * "-")


winner = None
current_turn = SYMBOL_X
input_x = 0
input_y = 0

field = list(9 * SYMBOL_EMPTY)
display_field()

while not finished():
    user_input = input("Enter the coordinates: ")

    if validate_input(user_input):
        place(input_x, input_y, current_turn)
        current_turn = SYMBOL_X if current_turn == SYMBOL_O else SYMBOL_O
        display_field()
        check_win()
        end_game()
