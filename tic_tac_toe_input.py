#2023-Jan-26
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Tic tac toe input
#Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. 
#To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

#Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). 
#Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

#For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.

#My Solution
def get_row_col(n):
    if n == "A1":
        return (0, 0)
    elif n == "A2":
        return (1, 0)
    elif n =="A3":
        return (2, 0)
    elif n=="B1":
        return (0, 1)
    elif n == "B2":
        return (1, 1)
    elif n== "B3":
        return (2, 1)
    elif n == "C1":
        return (0, 2)
    elif n == "C1":
        return (1, 2)
    else:
        return (2, 2)
        
#Solution
def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)
