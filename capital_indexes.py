#2023-Jan-11
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Capital Indexes
#Write a function named capital_indexes. The function takes a single parameter, which is a string. 
#Your function should return a list of all the indexes in the string that have capital letters.

def capital_indexes(str):
    lst = []
    for x in range(len(str)):
        if str[x].isupper() == True:
            lst.append(x)
    return lst

