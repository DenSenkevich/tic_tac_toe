
def start():
    global cells
    cells = input("Enter cells: ")
    cells = cells.replace("_", " ")
    cells = list(cells)

    print_matrix(cells)


def print_matrix(cells):
    print('-' * 9)
    for i in range(0, 7, 3):
        print(f"| {cells[i]} {cells[i + 1]} {cells[i + 2]} |")
    print('-' * 9)

    check_results(cells)


def check_results(cells):
    win_of_x = 0
    win_of_o = 0
    win_combines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]

    for a, b, c in win_combines:
        if (cells[a], cells[b], cells[c]) == ("X", "X", "X"):
            win_of_x += 1
        if (cells[a], cells[b], cells[c]) == ("O", "O", "O"):
            win_of_o += 1

    if win_of_x == 1:
        print("X wins")
        return

    elif win_of_o == 1:
        print("O wins")
        return

    elif cells.count("X") == 5 or cells.count("O") == 5:
        print("Draw")
        return

    ask_player(cells)


def ask_player(cells):
    global count
    coord = input("Enter the coordinates: ")
    if coord[0].isdigit() and coord[1] == " " and coord[2].isdigit():
        if not 0 < int(coord[0]) < 4 or not 0 < int(coord[2]) < 4:
            print("Coordinates should be from 1 to 3!")
            return ask_player(cells)
        if coord == "1 1":
            if cells[6] == " ":
                cells[6] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "1 2":
            if cells[3] == " ":
                cells[3] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "1 3":
            if cells[0] == " ":
                cells[0] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "2 1":
            if cells[7] == " ":
                cells[7] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "2 2":
            if cells[4] == " ":
                cells[4] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "2 3":
            if cells[1] == " ":
                cells[1] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "3 1":
            if cells[8] == " ":
                cells[8] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "3 2":
            if cells[5] == " ":
                cells[5] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)
        if coord == "3 3":
            if cells[2] == " ":
                cells[2] = x_or_o()
            else:
                print("This cell is occupied! Choose another one!")
                return ask_player(cells)

        print_matrix(cells)
    else:
        print("You should enter numbers!")
        ask_player(cells)


def x_or_o():
    global count
    count += 1
    return "X" if count % 2 == 1 else "O"


count = 0
if __name__ == "__main__":
    cells = "_________"
    cells = cells.replace("_", " ")
    cells = list(cells)
    print_matrix(cells)


