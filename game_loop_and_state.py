import printing_utility
class Tic_Tac_Toe:
  """
    Defines an instance of the game Tic_Tac_Toe
      Complete with a method to handle looping game state,
      methods to update and change game states,
      and imports from other files to assist with displaying the game state
  """
  def __init__(self):
    self.board = [[None, None, None],
                  [None, None, None],
                  [None, None, None]]
    self.the_number_of_x_s = 0
    self.the_number_of_o_s = 0
    self.the_flattened_vector_of_positions = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),
                                              (3,1),(3,2),(3,3)]
  
  def remove_from_the_flattened_vector_of_positions(self,
                                                    the_position_to_be_removed):
    try:
      self.the_flattened_vector_of_positions.remove(the_position_to_be_removed)
    except:
      raise Exception("""The position tuple passed into 
remove_from_the_flattened_vector_of_positions featured a position that was no
longer in the_flattened_vector_of_positions.""")
  
  def determine_final_game_state(self):
    game_state = self.board
    top_row = (game_state[0][0],game_state[0][1],game_state[0][2])
    middle_row = (game_state[1][0],game_state[1][1],game_state[1][2])
    bottom_row = (game_state[2][0],game_state[2][1],game_state[2][2])
    left_column = (game_state[0][0],game_state[1][0],game_state[2][0])
    middle_column = (game_state[0][1],game_state[1][1],game_state[2][1])
    right_column = (game_state[0][2],game_state[1][2],game_state[2][2])
    top_left_bottom_right_diagonal = (game_state[0][0],game_state[1][1],game_state[2][2])
    bottom_left_top_right_diagonal = (game_state[2][0],game_state[1][1],game_state[0][2])
    x_win_condition = ("X","X","X")
    o_win_condition = ("O","O","O")
    all_possible_configurations_that_could_result_in_a_win = set()
    all_possible_configurations_that_could_result_in_a_win.add(top_row)
    all_possible_configurations_that_could_result_in_a_win.add(middle_row)
    all_possible_configurations_that_could_result_in_a_win.add(bottom_row)
    all_possible_configurations_that_could_result_in_a_win.add(left_column)
    all_possible_configurations_that_could_result_in_a_win.add(middle_column)
    all_possible_configurations_that_could_result_in_a_win.add(right_column)
    all_possible_configurations_that_could_result_in_a_win.add(top_left_bottom_right_diagonal)
    all_possible_configurations_that_could_result_in_a_win.add(bottom_left_top_right_diagonal)
    if x_win_condition in all_possible_configurations_that_could_result_in_a_win:
      return (True,"X")
    elif o_win_condition in all_possible_configurations_that_could_result_in_a_win:
      return (True, "O")
    else:
      return (False, None)

  def looping_game_logic(self):
    print("""When we ask you to input a character, please do so in the following
manner. Type two numbers into the terminal. The first one represents 
the row, and MUST range from 1 to 3, where 1 is the top row, and 3 is 
the bottom row. The second number MUST range from 1 to 3 as well, where 
1 represents the left most column and 3 represents the right most column. 
Alternatively, to quit the game, you may press a singular character, q.""")
    is_it_the_player_s_turn = True
    current_player = "X"
    print("Here is the starting board!")
    print()
    print("-----------")
    printing_utility.array_to_terminal_output(self.board)
    print("-----------")
    print()
    while True:
      # print("DEBUG - what is the current player?:", current_player)
      if (current_player == "X"):
        if (is_it_the_player_s_turn):
          print("It's the player's turn!")
          print()
          is_it_the_player_s_turn == False
        user_input_string = input("Please input your character as previously formatted:")
        print()
        if (user_input_string == "q"):
          break
        # print("Is this your string:",user_input_string)
        row_number = int(user_input_string[0]) - 1
        column_number = int(user_input_string[1]) - 1
        the_character_at_the_requested_user_location = self.board[row_number][column_number]
        # print("DEBUG - what is the_character_at_the_requested_user_location?", the_character_at_the_requested_user_location)
        if (the_character_at_the_requested_user_location is None):
          self.board[row_number][column_number] = "X"
          self.the_number_of_x_s += 1
          the_position_to_be_removed = (row_number+1, column_number+1)
          self.remove_from_the_flattened_vector_of_positions(the_position_to_be_removed)
          current_player = "O"
          print("Here is the board after the player's turn!")
          print()
          print("-----------")
          printing_utility.array_to_terminal_output(self.board)
          print("-----------")
          print()
        else:
          print("The location you wish to put a piece at is already taken!")
          print()

      elif (current_player == "O"):
        print("It's the cpu's turn!")
        print()
        is_it_the_player_s_turn = True
        the_position_to_be_removed = self.the_flattened_vector_of_positions[0]
        row_number = the_position_to_be_removed[0] - 1
        column_number = the_position_to_be_removed[1] - 1
        self.board[row_number][column_number] = "O"
        self.the_number_of_o_s += 1
        the_position_to_be_removed = (row_number+1, column_number+1)
        self.remove_from_the_flattened_vector_of_positions(the_position_to_be_removed)
        current_player = "X"
        print("Here is the board after the cpu's turn!")
        print()
        print("-----------")
        printing_utility.array_to_terminal_output(self.board)
        print("-----------")
        print()
      else:
        raise Exception("current_player variable is not either \'O\' or \'X\'")
      game_result_at_current_state = self.determine_final_game_state()
      if game_result_at_current_state[0]:
        if game_result_at_current_state[1] == "X":
          print("The player has won!")
        elif game_result_at_current_state[1] == "O":
          print("The cpu has won!")
        print()
        break
      else:
        if self.the_number_of_o_s + self.the_number_of_x_s == 9:
          print("No side won...")
          print()
          break

    print("Here's the final game state:")
    printing_utility.array_to_terminal_output(self.board)
      

tic_tac_toe_game_master = Tic_Tac_Toe()
tic_tac_toe_game_master.looping_game_logic()
                    