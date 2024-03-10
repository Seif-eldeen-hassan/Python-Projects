# File: Task 6 (Connect- 4 game)
# Purpose: The first player to connect 4 symbols horizontally, vertically or diagonally wins.
# Author: Seif eldeen hassan mohamed
# ID: 20230182

Board = [["#","#","#","#","#","#","#"],
         ["#","#","#","#","#","#","#"],
         ["#","#","#","#","#","#","#"],  
         ["#","#","#","#","#","#","#"],
         ["#","#","#","#","#","#","#"],
         ["#","#","#","#","#","#","#"]]

# Function to take input from a player
def Taking_input(player):
    while True:
        Move = input(f"Player {player} : Please Choose X / O \n").upper()
        if Move == "X" or Move == "O":
            break
        else:
            print("Invalid Choice, Please Choose X / O")
    return Move

def Check_column(player):
    while True:
        global column
        column = (input(f"Player {player} : Please input the column "))
        if column.isdigit() == False :
            print("Please Enter Valid integer\n")
            continue

        else:
            column = int(column)
            if 0 < column <= 7:
                return(column)
            else: 
                print("Column out of range\n")
                
        
# Function to update the board based on the player's move
def Input(player_turn):
    if player_turn == 1:
        player = Player_1
    elif player_turn == 2:
        player = Player_2
    i = 5
    while True:
        if Board[i][column-1] == "#":
            Board[i][column-1] = player
            break
        else:
            if i < 0:
                print("You reached the max, Try again\n")
                return("Stop")
            else: 
                i -= 1

# Function to print the current state of the board
def Print_Board():
    for row in Board:
        print(" ".join(row))

# Function to check for a horizontal win
def Checking_Horizontal():
    for r in range(6):
        for c in range(4):
            if (Board[r][c] == Board[r][c+1] == Board[r][c+2] == Board[r][c+3] == "O" or
                Board[r][c] == Board[r][c+1] == Board[r][c+2] == Board[r][c+3] == "X"):
                return True
    return False

# Function to check for a vertical win
def Checking_Vertical():
    for c in range(7):
        for r in range(3):
            if (Board[r][c] == Board[r+1][c] == Board[r+2][c] == Board[r+3][c] == "O" or
                Board[r][c] == Board[r+1][c] == Board[r+2][c] == Board[r+3][c] == "X"):
                return True
    return False

# Function to check for a diagonal win (lower diagonals)
# Function to check for a diagonal win (lower diagonals)
def Checking_lower_Diagonals():
    for r in range(6):
        for c in range(4):
            if (r >= 3 and Board[r][c] == Board[r-1][c+1] == Board[r-2][c+2] == Board[r-3][c+3] == "O" or
                r >= 3 and Board[r][c] == Board[r-1][c+1] == Board[r-2][c+2] == Board[r-3][c+3] == "X"):
                return True
            elif ((r >= 3 and c >= 3) and Board[r][c] == Board[r-1][c-1] == Board[r-2][c-2] == Board[r-3][c-3] == "O" or
                 (r >= 3 and c >= 3) and Board[r][c] == Board[r-1][c-1] == Board[r-2][c-2] == Board[r-3][c-3] == "X"):
                return True
    return False

# Function to check for a diagonal win (upper diagonals)
def Checking_upper_Diagonals():
    for r in range(3):
        for c in range(4):
            if (Board[r][c] == Board[r+1][c+1] == Board[r+2][c+2] == Board[r+3][c+3] == "O" or
                Board[r][c] == Board[r+1][c+1] == Board[r+2][c+2] == Board[r+3][c+3] == "X"): 
                return True  
            elif (c >= 3 and Board[r][c] == Board[r+1][c-1] == Board[r+2][c-2] == Board[r+3][c-3] == "O" or 
                  c >= 3 and Board[r][c] == Board[r+1][c-1] == Board[r+2][c-2] == Board[r+3][c-3] == "X"): 
                return True 
    return False


# Function to check for a winner
def Checking_winner(player):
    if Checking_Horizontal() or Checking_Vertical() or Checking_lower_Diagonals() or Checking_upper_Diagonals():
        print(f"Player {player} : wins\n")   
        return(True)


# Function to check for a draw
def Checking_draw():
    for r in range(6):
        for c in range(7):
            if Board[r][c] == "#":
                return False  # If there is an empty cell, the game is not a draw

    print("The Game ends in a Draw\n")
    return True  # If there are no empty cells, the game is a draw


def checking_tryagain():
        while True:
            # Ask the user if they want to try again or exit
            print("Do you want to try again ? ")
            print("1) Try Again ")
            print("2) Exit ")
            Choice = (input())
            if Choice == "1":
                Main_game()
            elif Choice == "2":
                exit()
            else:
                print("Invalid Choice, Please Choose 1 or 2 \n")


# Main game Function
def Main_game(): 
    while True:
         # Reset the board to its initial state
        global Board
        Board = [["#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#"],  
                 ["#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#"],
                 ["#","#","#","#","#","#","#"]]
        Print_Board()
        global Player_1 , Player_2
        Player_1 = Taking_input(1)
        if Player_1 == "X":
           Player_2 = "O" 
        else:
           Player_2 = "X"  # Assign the other player's symbol
        print(f"Player 1 : will Play with  '{Player_1}'")
        print(f"Player 2 : will Play with  '{Player_2}'")
        while True:
            column = Check_column(1)
            if Input(1) == "Stop":
                continue
            else:
                Print_Board()
                if Checking_winner(1) or Checking_draw():
                    break
                column = Check_column(2)
                if Input(2) == "Stop":
                    continue
                else:
                 Print_Board()
                if Checking_winner(2) or Checking_draw():
                    break
        checking_tryagain()

Main_game()

             


