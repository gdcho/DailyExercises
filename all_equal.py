#2023-Feb-23
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#All equal
#Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

#My Solution
def all_equal(lst):
    if len(lst) == 0:
        return True
    if len(lst) == lst.count(lst[0]):
        return True
    return False
        
# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True

# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)
