#2023-Jan-19
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Counting syllables
#Define a function named count that takes a single parameter. 
#The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:

# My solution
def count(string):
    li = []
    li[:0] = string
    count = li.count("-")
    return count+1

# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))
