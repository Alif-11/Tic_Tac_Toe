# Keep it simple, silly!
def array_to_terminal_output(array):
  print("###########") # there are 11 hashtags here. Ignore the first and last,
                       # since they will be used for formatting the array in the
                       # terminal.
  for row_array in array:
    the_string_to_print_for_this_row_array = "#"
    for column_element in row_array:
      if column_element is None:
        the_string_to_print_for_this_row_array += "| |"
      elif column_element == "X":
        the_string_to_print_for_this_row_array += "|X|"
      elif column_element == "O":
        the_string_to_print_for_this_row_array += "|O|"
      else:
        raise Exception("An invalid character has appeared in your array.") 
    the_string_to_print_for_this_row_array += "#"
    print(the_string_to_print_for_this_row_array)
  print("###########")