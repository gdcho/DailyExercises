#2023-Jan-18
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Adding and removing dots
#WWrite a function named add_dots that takes a string and adds "." in between each letter. 
#For example, calling add_dots("test") should return the string "t.e.s.t".

#Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
#For example, calling remove_dots("t.e.s.t") should return "test".

#My solution
def add_dots(string):
    final = ""
    for x in string:
        final += x
        final += "."
    return final[:-1]

def remove_dots(string):
    final = ""
    for x in string:
        if x != ".":
            final +=x
    return final

# long solution
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1]

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out
    
# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")
