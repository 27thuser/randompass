#will generate a random strong password that includes:
#   - 2 uppercase letters (A-Z).
#   - 2 lowercase letters (a-z).
#   - 2 digits (0-9).
#   - 2 punctuation marks (e.g., !, ?, #).
#can ask user how many characters they want

import random
import string
import array

# here i declare all pools of stuff that is included in the password
uplet = string.ascii_uppercase
lowlet = string.ascii_lowercase
digits = string.digits
punc = string.punctuation

# i put all of them in an array, right now, they are all null and represent every ascii character of their type
passarray = [uplet, lowlet, digits, punc]

def randompassgen(choice, size, unscrambledpass=""):  # i put 2 parameters, that can be chosen by the user, one is a check(xddddddd), one is the size of the password
    # this for look of range 4 will take 2 characters from each of these pools, and assign those as strings to each pool, giving them a value
    for i in range(4):
        passarray[i] = ''.join(random.choice(passarray[i]) for _ in range(2))
        unscrambledpass += passarray[i]  # this will shove all these pools of 2 characters into one string, that is unscrambled, goes from uplet to punc
    unscrambledarray = list(unscrambledpass)  # this godsend of a function turns the unscrambled password into an array of chars
    if choice == True:
        for i in range(size):  # almost same concept as last for loop, it will take a character randomly from the pool unscrambledarray until it satisfies the size condition of the user
            scrambledpass = ''.join(random.choice(unscrambledarray) for _ in range(size))
    else: #same thing, just with the default 8 characters
        scrambledpass = ''.join(random.choice(unscrambledarray) for _ in range(8))
    print(scrambledpass)

#simple stuff xdddd alrr
prompt = input("choose size?(y/n)")
if prompt == 'y':
    sizeprompt = int(input("how long should ur pass be(integer)"))
    randompassgen(True, sizeprompt)
elif prompt == 'n':
    randompassgen(False, 0)
else:
    print("Error")
