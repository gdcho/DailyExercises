#Random password generator exercise
#https://www.101computing.net/random-password-generator/

import random

#A function that shuffles all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Lowercase letter (based on ASCII code)
digit1=chr(random.randint(48, 57)) #Generate a random digit (based on ASCII code)
digit2=chr(random.randint(48, 57)) #Generate a random digit (based on ASCII code)
punctuationSign1=chr(random.randint(33,47)) #Generate a random punctuation sign (based on ASCII code)
punctuationSign2=chr(random.randint(33,47)) #Generate a random punctuation sign (based on ASCII code)


#Generate password using all the characters, in random order
password = (uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2)*2
password = shuffle(password)

#Ouput
print(password)
