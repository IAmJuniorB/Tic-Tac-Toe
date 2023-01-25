board = [[" ", " ", " "], [" ", " ", " "],[" ", " ", " "]]

def printBoard():
    for row in board:
        print(row)

def makeMove(player, row, col):
    if board[row][col] == " ":
        board[row][col] = player

def win():
    #horizontals first
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[0] != " ":
            return row[0]

    #verticals
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ":
        return board[0][0]

    for row in board:
        for slot in row:
            if slot == " ":
                return " " #game is still ongoing
    return "draw"


players = ["X", "O"]
player = 0
while win() == " ":
    printBoard()
    row = int(input("What row?"))
    col = int(input("What col?"))
    makeMove(players[player], row-1, col-1)
    player = (player + 1) % len(players)
printBoard()
