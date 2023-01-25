#2023-Jan-24
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#Min-maxing
#Define a function named largest_difference that takes a list of numbers as its only parameter.

#Your function should compute and return the difference between the largest and smallest number in the list.

#My Solution
def largest_difference(lon):
    lon.sort()
    return lon[-1] - lon[0]
        
# short solution
def largest_difference(numbers):
    return max(numbers) - min(numbers)

# naive solution
def largest_difference(numbers):
    smallest = 100
    for n in numbers:
        if n < smallest:
            smallest = n

    largest = -100
    for n in numbers:
        if n > largest:
            largest = n

    difference = largest - smallest
    return difference
