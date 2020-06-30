def main():
    game = reset_board()  # Generate initial empty board
    run = True
    player = 1
    print("""Welcome to Tic Tac Toe!
Enter your move as co-ordinates for the row and column.
E.g. top left would be '1, 1' and middle right '2, 3'""")

    while run:
        move = input(f"Player {player}, enter your move: ")  # Get player move
        if do_move(game, move, player):  # Check if move was valid
            if check_outcome(game, player):  # Check for win or tie
                if repeat_game():  # Check if user wants another game
                    game = reset_board()  # Reset game list
                    player = 1  # Reset player
                else:
                    run = False  # Exit game
            else:  # If no win print board and switch player
                print_board(game)
                player = player_switch(player)


def print_board(game):
    board_size = 3

    for x in range(board_size):
        print(" ---" * board_size)  # Print horizontal lines
        for n in range(len(game[x])):  # Print vertical lines with game values
            print(f"| {game[x][n]} ", end="")
        print("|")  # Print end of row and new line
    print(" ---" * board_size)  # Print bottom horizontal lines once board is finished


def do_move(game, move, player):  # Takes current board, desired move and player
    move_row = int(move.replace(" ", "")[0]) - 1  # Convert user input into correct format
    move_col = int(move.replace(" ", "")[2]) - 1

    if game[move_row][move_col] == 0:  # Check if desired move contains a 0, if so store the move
        if player == 1:  # Set value to X if player 1
            game[move_row][move_col] = "X"
            return True
        elif player == 2:  # Set value to O if player 2
            game[move_row][move_col] = "O"
            return True
    else:  # If move not a 0, it's already taken so get input again
        print("Invalid position, choose again!")
        return False


def check_outcome(game, player):
    for i in range(0, 3):
        if game[i][0] == game[i][1] == game[i][2]:  # Check rows
            if not game[i][0] == 0:  # Check it's not default value winning
                print(f"Player {player} has won!")  # Print winner
                return True
        elif game[0][i] == game[1][i] == game[2][i]:  # Check columns
            if not game[0][i] == 0:
                print(f"Player {player} has won!")
                return True
        elif game[0][0] == game[1][1] == game[2][2]:  # Check diagonal left to right
            if not game[0][0] == 0:
                print(f"Player {player} has won!")
                return True
        elif game[0][2] == game[1][1] == game[2][0]:  # Check diagonal right to left
            if not game[0][2] == 0:
                print(f"Player {player} has won!")
                return True

    # If no winners found, check whole board, if no zeros left it's a tie
    if "0" not in str(game):
        print("No more moves left!")
        return True
    else:
        return False


def repeat_game():
    repeat = input("Play another game? Enter yes/no: ")
    repeat = repeat.lower()
    if repeat in ["yes", "y"]:
        return True
    else:
        return False


def player_switch(player):  # Switches current player
    if player == 1:
        return 2
    else:
        return 1


def reset_board():  # Generate fresh board
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    return game


main()
