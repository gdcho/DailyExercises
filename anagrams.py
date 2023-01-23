#2023-Jan-22
#rjs
#Python Programming Challenges (pythonprinciples.com/challenges/)

#anagrams
#Two strings are anagrams if you can make one from the other by rearranging the letters.

#Write a function named is_anagram that takes two strings as its parameters. 
#Your function should return True if the strings are anagrams, and False otherwise.

#My Solution
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
        
# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
