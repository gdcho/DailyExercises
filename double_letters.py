#2023-Jan-17
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Double letters
#WDefine a function named double_letters that takes a single parameter. The parameter is a string. 
#Your function must return True if there are two identical letters in a row in the string, and False otherwise.


#My Solution
def double_letters(string):
    for x in range(len(string)):
        if string[x] == string[x+1:x+2]:
            return True
    return False
    
# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])
