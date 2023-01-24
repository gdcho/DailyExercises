#2023-Jan-23
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Flatten a list
#Write a function that takes a list of lists and flattens it into a one-dimensional list.

#Name your function flatten. It should take a single parameter and return a list.

#My Solution
def flatten(lol):
    final = []
    for lst in lol:
        for x in lst:
            final.append(x)
    return final
        
# naive solution
def flatten(outer_list):
    result = []
    for inner_list in outer_list:
        for item in inner_list:
            result.append(item)
    return result

# solution with nested list comprehensions
# (can be put on a single line for conciseness)
def flatten(outer_list):
    return [
        item
        for inner_list in outer_list
        for item in inner_list
    ]
