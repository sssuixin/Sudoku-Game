"""
This is a Sudoku game that ask a user for a number between 1 - 9 replace with '?'. 
Duplicate number are not allow in each row, colume, and nonet, which end up the sum of each row, colume, and nonet's should be 45, (1+2+3+4+5+6+7+8+9=45).
"""
###########
#FUNCTIONS#
###########

#Prints all rows for user
def print_board(x): 
  for i in range(9): 
      print(x[i])
      print(blank_line)
      if (i + 1) % 3 == 0: 
          print(blank_line)
      else: 
          continue

# The replace_question program replaces the "?" in the grid with a number of the user's choice, then updates the board so that the "?" spot chosen is updated with the user's choice of number.
def replace_question(level, level_answer, mistakes_amount):
    print("This function allows the user to replace a '?' space." )
    print("List the row, group within row, and specific '?' spot within group that you want to edit in the sudoku board.")
    print(blank_line)
    #This while loop continues asking user to put numbers into the board, while checking if the numbers are correct. It will stop when user complete the sudoku board.
    global mistakes
    mistakes = 0
    while (level != level_answer) and (mistakes < mistakes_amount):
        #This while loop asks user for four number inputs. While asking, it also checks if the inputs are valid numbers within proper range. It will stop when python gets a proper set of numbers.
        while True: 
            try:
                rownum = int(input("Enter row number (1, 2, 3, etc): "))
                column = int(input("Enter column number (1, 2, 3, etc): "))
                number = input("Enter the number you want to replace the '?' spot with: ")
                if (rownum > 9) or (rownum <= 0) or (column > 9) or (column <= 0):
                    print("Number out of range!")
                    print("\n")
                    continue
                else:
                    break
            except ValueError:
                print("Please enter numbers!")
                print("\n")
                continue
        # This if statement will convert the column number user selected to group number and spot number.   
        if column <= 3:
            group = 1
        elif column > 6:
            group = 3
        else:
            group = 2
        spot = column - (group - 1)*3
        # This if satement will fill the number into sudoku board when user entered the correct one, or it will tell user to enter again.
        if number == level_answer[rownum-1][group-1][spot-1]:
            level[rownum-1][group-1][spot-1] = number
            print("Mistakes: " + str(mistakes) + "/" + str(mistakes_amount))
            print("\n")
            print("UPDATED BOARD:")
            print("\n")
            print_board(level)
            
        else:
            mistakes = mistakes + 1
            print("Incorrect number. Try again!")
            print("Mistakes: " + str(mistakes) + "/" + str(mistakes_amount))
            print("\n")

# This function help user to select the game level(Easy/Medium/Hard). After level being selected, certain amount of chances of making mistakes are assigned. This function also calls the replace_question function.
def level_selection():
    while True:
        global mode
        user_level = input("Select the game difficulty (Easy/Medium/Hard): ")
        if (user_level == "Easy") or (user_level == "easy"):
            mode = "easy"
            print_board(rows_easy)
            print("\n")
            print("You've got 3 chances of making mistakes.")
            replace_question(rows_easy, rows_easy_answer, 3)
            break
        elif (user_level == "Medium") or (user_level == "medium"):
            mode = "medium"
            mistakes_amount = 4
            print_board(rows_medium)
            print("\n")
            print("You've got 4 chances of making mistakes.")
            replace_question(rows_medium, rows_medium_answer, 4)
            break
        elif (user_level == "Hard") or (user_level == "hard"):
            mode = "hard"
            mistakes_amount = 5
            print_board(rows_hard)
            print("\n")
            print("You've got 5 chances of making mistakes.")
            replace_question(rows_hard, rows_hard_answer, 5)
            break
        else:
            print("Please input correctly!")
            print("\n")
            continue

##############
#MAIN PROGRAM#
##############

#RULES
#Below, the rules of the game are printed for the user.

print("SUDOKU GAME")
print("----------")
print("INSTRUCTIONS:")
print("----------")
print("1. 2 players total, including the computer.")
print("2. The player wins the game when they finish solving the sudoku puzzle.")
print("3. Each row must contain the numbers from 1 - 9 without repetition.")
print("4. Each column must contain the numbers from 1 - 9 without repetition.")
print("5. Each nonet (3 x 3 box) must contain the numbers from 1 - 9 without repetition.")
print("6. The digits can only occur once per block.")
print("7. The sum of every single row, column, and nonet must equal to 45,(1+2+3+4+5+6+7+8+9 = 45).")
print("8. There is no tie score. ")
print("9. Have fun with your brain.")
print("----------")
print("\n")
print("GAME START: ")
print("\n")

#Unfilled rows for sudoku board - easy mode
row1_easy = [["?", "4", "?"], ["1", "8", "2"], ["?", "?", "6"]]
row2_easy = [["6", "2", "3"], ["?", "?", "?"], ["1", "9", "?"]]
row3_easy = [["8", "?", "1"], ["?", "?", "?"], ["?", "?", "4"]]
row4_easy = [["?", "?", "?"], ["7", "?", "?"], ["2", "5", "?"]]
row5_easy = [["7", "5", "2"], ["?", "6", "3"], ["8", "4", "1"]]
row6_easy = [["4", "9", "8"], ["?", "1", "5"], ["?", "?", "3"]]
row7_easy = [["?", "?", "?"], ["?", "9", "?"], ["?", "3", "?"]]
row8_easy = [["2", "1", "?"], ["3", "?", "?"], ["?", "8", "?"]]
row9_easy = [["?", "8", "9"], ["?", "2", "4"], ["6", "?", "7"]]
blank_line = ""
rows_easy = row1_easy, row2_easy, row3_easy, row4_easy, row5_easy, row6_easy, row7_easy, row8_easy, row9_easy

#Answer for sudoku board - easy mode
row1_easy_answer = [["9", "4", "5"], ["1", "8", "2"], ["3", "7", "6"]]
row2_easy_answer = [["6", "2", "3"], ["4", "5", "7"], ["1", "9", "8"]]
row3_easy_answer = [["8", "7", "1"], ["6", "3", "9"], ["5", "2", "4"]]
row4_easy_answer = [["1", "3", "6"], ["7", "4", "8"], ["2", "5", "9"]]
row5_easy_answer = [["7", "5", "2"], ["9", "6", "3"], ["8", "4", "1"]]
row6_easy_answer = [["4", "9", "8"], ["2", "1", "5"], ["7", "6", "3"]]
row7_easy_answer = [["5", "6", "7"], ["8", "9", "1"], ["4", "3", "2"]]
row8_easy_answer = [["2", "1", "4"], ["3", "7", "6"], ["9", "8", "5"]]
row9_easy_answer = [["3", "8", "9"], ["5", "2", "4"], ["6", "1", "7"]]
rows_easy_answer = row1_easy_answer, row2_easy_answer, row3_easy_answer, row4_easy_answer, row5_easy_answer, row6_easy_answer, row7_easy_answer, row8_easy_answer, row9_easy_answer

#Unfilled rows for sudoku board - medium mode
row1_medium = [["6", "8", "4"], ["?", "?", "3"], ["2", "?", "?"]]
row2_medium = [["7", "?", "9"], ["2", "8", "4"], ["1", "?", "3"]]
row3_medium = [["?", "?", "?"], ["?", "?", "?"], ["4", "?", "?"]]
row4_medium = [["?", "?", "?"], ["?", "2", "?"], ["8", "3", "1"]]
row5_medium = [["?", "?", "8"], ["5", "?", "9"], ["7", "?", "?"]]
row6_medium = [["2", "4", "7"], ["?", "3", "?"], ["?", "?", "?"]]
row7_medium = [["?", "?", "2"], ["?", "?", "?"], ["?", "?", "?"]]
row8_medium = [["4", "?", "3"], ["9", "5", "1"], ["6", "?", "8"]]
row9_medium = [["?", "?", "6"], ["3", "?", "?"], ["5", "7", "9"]]
rows_medium = row1_medium, row2_medium, row3_medium, row4_medium, row5_medium, row6_medium, row7_medium, row8_medium, row9_medium


#Answer for sudoku board - medium mode
row1_medium_answer = [["6", "8", "4"], ["7", "1", "3"], ["2", "9", "5"]]
row2_medium_answer = [["7", "5", "9"], ["2", "8", "4"], ["1", "6", "3"]]
row3_medium_answer = [["3", "2", "1"], ["6", "9", "5"], ["4", "8", "7"]]
row4_medium_answer = [["9", "6", "5"], ["4", "2", "7"], ["8", "3", "1"]]
row5_medium_answer = [["1", "3", "8"], ["5", "6", "9"], ["7", "4", "2"]]
row6_medium_answer = [["2", "4", "7"], ["1", "3", "8"], ["9", "5", "6"]]
row7_medium_answer = [["5", "9", "2"], ["8", "7", "6"], ["3", "1", "4"]]
row8_medium_answer = [["4", "7", "3"], ["9", "5", "1"], ["6", "2", "8"]]
row9_medium_answer = [["8", "1", "6"], ["3", "4", "2"], ["5", "7", "9"]]
rows_medium_answer = row1_medium_answer, row2_medium_answer, row3_medium_answer, row4_medium_answer, row5_medium_answer, row6_medium_answer, row7_medium_answer, row8_medium_answer, row9_medium_answer

#Unfilled rows for sudoku board - hard mode
row1_hard = [["?", "?", "?"], ["?", "6", "?"], ["?", "?", "?"]]
row2_hard = [["?", "?", "?"], ["?", "?", "?"], ["9", "2", "5"]]
row3_hard = [["?", "?", "8"], ["5", "?", "9"], ["1", "?", "4"]]
row4_hard = [["?", "2", "?"], ["9", "?", "6"], ["5", "?", "7"]]
row5_hard = [["?", "8", "4"], ["?", "?", "7"], ["6", "?", "?"]]
row6_hard = [["7", "5", "?"], ["?", "?", "?"], ["3", "4", "?"]]
row7_hard = [["?", "?", "7"], ["6", "9", "?"], ["?", "5", "?"]]
row8_hard = [["5", "?", "?"], ["8", "2", "?"], ["?", "7", "6"]]
row9_hard = [["4", "6", "?"], ["?", "1", "5"], ["8", "?", "?"]]
rows_hard = row1_hard, row2_hard, row3_hard, row4_hard, row5_hard, row6_hard, row7_hard, row8_hard, row9_hard

#Answer for sudoku board - hard mode
row1_hard_answer = [["1", "9", "5"], ["4", "6", "2"], ["7", "3", "8"]]
row2_hard_answer = [["6", "4", "3"], ["1", "7", "8"], ["9", "2", "5"]]
row3_hard_answer = [["2", "7", "8"], ["5", "3", "9"], ["1", "6", "4"]]
row4_hard_answer = [["3", "2", "1"], ["9", "4", "6"], ["5", "8", "7"]]
row5_hard_answer = [["9", "8", "4"], ["3", "5", "7"], ["6", "1", "2"]]
row6_hard_answer = [["7", "5", "6"], ["2", "8", "1"], ["3", "4", "9"]]
row7_hard_answer = [["8", "3", "7"], ["6", "9", "4"], ["2", "5", "1"]]
row8_hard_answer = [["5", "1", "9"], ["8", "2", "3"], ["4", "7", "6"]]
row9_hard_answer = [["4", "6", "2"], ["7", "1", "5"], ["8", "9", "3"]]
rows_hard_answer = row1_hard_answer, row2_hard_answer, row3_hard_answer, row4_hard_answer, row5_hard_answer, row6_hard_answer, row7_hard_answer, row8_hard_answer, row9_hard_answer

# Calls the functions
level_selection()
print(blank_line)

#Prints message to indicate that the puzzle is completed.
if (mode == "easy") and (mistakes == 3):
    print("GAME OVER")
    print("You lost the game because you made 3 mistakes.")
elif (mode == "medium") and (mistakes == 4) :
    print("GAME OVER")
    print("You lost the game because you made 4 mistakes.")
elif (mode == "hard") and (mistakes == 5):
    print("GAME OVER")
    print("You lost the game becuase you made 5 mistakes.")
else:
    print("You have completed the sudoku puzzle. Congratulations! ")