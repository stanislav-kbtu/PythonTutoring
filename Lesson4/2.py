import re

words = ["HELLO", "SFDS1", "DFGDF", "them", "13123", "red", "lesson1", "Hi", "123", "3244", "aT", "tank"]

# ^ - Starts with, 
# $ - Ends with, 
# \d - number, 
# ? - zero or one occurence, 
# + - one or more occurences
# * - zero or more occurences
# . - any character
# [] - set of characters
pattern = "^\d+$"
pattern2 = "^.*\d$"
pattern3 = "[a-z]*"
pattern4 = "[tT]"
pattern5 = "^[A-Za-z]+$"
#res = re.findall(pattern, words) - returns list
# re.search - True or False

for word in words:
    if re.search(pattern5, word): 
        print(word)