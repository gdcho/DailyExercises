#2023-Jan-12
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Middle Letter
#Write a function named mid that takes a string as its parameter.
#Your function should extract and return the middle letter. 
#If there is no middle letter, your function should return the empty string.



#My Solution
import math

def mid(str):
    str_len = len(str)
    if str_len %2 == 0:
        return ""
    return str[math.floor(len(str)/2)]

#Solution
def mid(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]