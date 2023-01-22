#2023-Jan-15
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Type check
#Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.
#For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False


def only_ints(par1, par2):
    return type(par1) == int and type(par2) == int
