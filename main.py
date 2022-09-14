#-----Global Variables-----

#gameBoard
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#if Game is still going
game_still_going = True

#if winner or if tie
winner = None

#who's turn ,  started with x
current_player = "x"




def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():

  #display initial board
  display_board()

  while game_still_going :

    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  # after the game has ended.
  if winner == "x" or winner == "o":
    print(winner + " won. ")
  elif winner == None:
    print("Tie.")


def handle_turn(player):

  print(player + "'s turn.")
  position = input("choose a position from 1-9 :")

  valid = False
  while not valid:
    
    while position not in ["1" , "2" , "3", "4", "5", "6", "7", "8", "9" ] :
      position = input("choose a position from 1-9 :")
    
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You cant go there. Play again.")

  board[position] = player

  display_board()

#two ways for game to be over.
def check_if_game_over():
  check_if_win()  
  check_if_tie()

def check_if_win():

  global winner
  #check rows
  row_winner = check_rows()
  #check column
  column_winner = check_column()
  #check diagonal
  diagonal_winner = check_diagonal()

  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
    
  else:
    #no one won and tie.
    winner = None
      
  
  return

def check_rows():
  #set up global variable.
  global game_still_going

  #check if any rows have all X or O
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False

  #return the winner
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
    
  return

def check_column():
  #set up global variable.
  global game_still_going

  #check if any column have all X or O
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"

  if column_1 or column_2 or column_3:
    game_still_going = False

  #return the winner
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return


def check_diagonal():
  #set up global variable.
  global game_still_going

  #check if any diagonal have all X or O
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"

  if diagonal_1 or diagonal_2 :
    game_still_going = False

  #return the winner
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]

  return


def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return

# two players x & o.
def flip_player():
  global current_player

  #change player
  if current_player == "x":
    current_player = "o"
  elif current_player == "o":
    current_player = "x"
    
  return


play_game()
  
