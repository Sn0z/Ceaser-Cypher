'''
The program is a Tic Tak Toe gaem where the player is 'X' and the computer is 'O'. 
The program handles and checks for wins and draw, and keeps track of the score. 

Name : Prarambha Shrestha
University id : 2408419
'''
import random
import os.path
import json

random.seed()

def draw_board(board):
    # Function to draw the Tic Tac Toe board
    """
    This function is to draw the board of the tic,tac,toe
    By using the ---- and for loop of |.
    """
    print('\t -----------')
    for row in board:
        print("\t| " + " | ".join(row) + " |")
        print('\t -----------')

def welcome(board):
    # Function to display a welcome message and the initial board layout
    '''
    This function is to pritn a welcoming message when the progarme starts
    '''
    print('Welcome to the "Unbeatable Noughts and Crosses" game.\nThe board  layout is shown below:')
    draw_board(board)
    print('When prompted, enter the number corresponding to the square you want.')

def initialise_board(board):
    # Function to initialize the board with empty spaces
    """
    This function is to make our tic,tac,toe board empty 
    by using the help of for loop where i is used to make the row and j is used to make colomn
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = ' '
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    """
    This gives the user with the option of to choose the place where they want to make the move
    for example if you press 5 then your move is in the middle of our tic,tac,toe board.
    but if you press any thing except of the numbers provided to you it will give you a error.
    """
    while True:
        move = input('''
                    1 2 3
                    4 5 6
Choose your square: 7 8 9 : ''')
        try:
            pos = int(move)-1
            row = pos // 3
            col = pos % 3
            if 0<=pos<=8:
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Invalid move. Place already taken")
            else:
                print("Enter Numebr within the range of (1-9)")
        except:
            print("Please type a number.")
    # and return row and col  
    return row, col 

def choose_computer_move(board):
    # develop code to let the computer chose a cell to put a nought in
    """
    This function is used by the bot by the help of random integer where after the player move
    it uses its move but in a random patteren which cannot be predicted for this to be accurate 
    it is used for both row and colomn where the bot will only make its move in the empty space
    with the help of if condition.
    """
    while True:
        #randiant returns int within the range of [0,2]
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            # and return row and col
            return row, col      
    
def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # Check rows
    """
    This is to check if we have won the game or not .It checks the row and colum and diagonals too. 
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == mark:
            return True

    # Check if columns match
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == mark:
            return True

    # Check if diagonal match    
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True

    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    """
    This is to check if the game is a draw or not with the help of loop and if condtion where for row in board
    which checks every row on the board and if every row is filled and no one has won then the program shows 
    its a draw.
    """
    # develop cope to check if all cells are occupied
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    '''
    This is the function which creates the table and asks for the user infomation. And checks 
    either it is a win or a loss or weatehr is its a draw
    '''
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        draw_board(board)
        # check if the player has won by calling check_for_win(board, mark),
        if check_for_win(board, 'X'):
            print("You won!")
            return 1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            print("The game is a draw.")
            return 0
        # if not, then call choose_computer_move(board) to choose a spot for the computer
        row, col = choose_computer_move(board)
        draw_board(board)
        # if computer won by calling check_for_win(board, mark), if so, return -1 for the score
        if check_for_win(board, 'O'):
            print("You lost!")  
            return -1
        # if drawn, return 0 for the score
        elif check_for_draw(board):
            print("Draw.")
            return 0
                                  
def menu():
    '''
    This fucntion displays the menu at when the player makes a choice
    '''
    print("Enter one of the following options:")
    print("\t1 - Play the game\n\t2 - Save score in file 'leaderboard.txt'\n\t3 - Load and display the scores from the 'leaderboard.txt'\n\tq - End the program") 
    choice = input("'1', '2', '3' or 'q'? ")
    return choice

def load_scores():
    """
    This function is used to check the file where to store the leaderboard and converts that into a JSON format 
    where it keeps our data into a dictionary format and then shows it to us as our leaderboard.
    """
    if os.path.exists('leaderboard.txt'):
        try:
            with open("leaderboard.txt", 'r') as file:
                leaders = json.load(file)
                return leaders
        except json.decoder.JSONDecodeError:
            print("Error: The file 'leaderboard.txt' does not contain valid JSON data.")
            return {}
    else: 
        # Handle the case when the file doesn't exist
        print("leaderboard.txt file not found.")
        return {}

def save_score(total_score):
    '''
    This function saves the score to the file leader.txt 
    '''
    # develop code to ask the player for their name
    name = input("Enter your name: ")
    current_score = load_scores()
    current_score[name] = total_score
    with open('leaderboard.txt', 'w') as f:
        json.dump(current_score, f)
    return 0

def display_leaderboard(leader_board):
    '''
    It displayes the file that the programe saved in leader.txt
    '''
    # develop code to display the leaderboard scores
    print("Leaderboard:")
    # passed in the Python dictionary parameter leader
    for name, score in leader_board.items():
        print(f"\t{name}: {score}")
    pass

