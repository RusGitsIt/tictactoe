cell_list = "         "
players = ["X", "O"]
in_progress = True


# functions
def grid(cells):
    print("-" * 9)
    for i in range(3):
        print("|", " ".join(cells[3 * i:3 * i + 3]), "|")
    print("-" * 9)


def turn(cells, n):
    global cell_list
    x, y = 0, 0
    # user input
    while x not in range(1, 4) or y not in range(1, 4):
        x, y = input("Enter the coordinates: ").split()
        index = 8 - 3 * int(y) + int(x)
        if x not in "1234567890" or y not in "1234567890":
            print("You should enter numbers!")
        elif x not in "123" or y not in "123":
            print("Coordinates should be from 1 to 3!")
        elif cells[index] != " ":
            print("This cell is occupied!  Choose another one!")
        else:  # update game state
            f = list(cell_list)
            f[index] = n  # X or O
            cell_list = "".join(f)


def analysis(cells, n):
    global in_progress
    win_lines = [[cells[0], cells[1], cells[2]],
                 [cells[3], cells[4], cells[5]],
                 [cells[6], cells[7], cells[8]],
                 [cells[0], cells[3], cells[6]],
                 [cells[1], cells[4], cells[7]],
                 [cells[2], cells[5], cells[8]],
                 [cells[0], cells[4], cells[8]],
                 [cells[6], cells[4], cells[2]]]
    win_list = [n, n, n]

    for i in range(len(win_lines)):
        if set(win_list) == set(win_lines[i]):
            grid(cell_list)
            print(n, "wins")
            in_progress = False

    if in_progress and " " not in cell_list:
        grid(cell_list)
        print("Draw")
        in_progress = False


def lets_play(n):
    grid(cell_list)
    turn(cell_list, n)
    analysis(cell_list, n)


# game
while in_progress:
    lets_play(players[0])
    if in_progress:
        lets_play(players[1])
