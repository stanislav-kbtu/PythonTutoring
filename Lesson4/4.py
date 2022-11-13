import re
# \s - returns match where string contains white space
numbers = ["+77013457656", "87015467683", "87781249845", "+7 701 876 90 82", "+7 705 873 34 34"]

pattern = "([+][7]|[8])\s?([7][0][1]|[7][0][5])\s?\d\d\d\s?\d\d\s?\d\d"

for number in numbers:
    if re.search(pattern, number): print(number)