import re

f = open('words.txt', 'r')

words = f.readlines()

f.close()

# + - 1 or more occurences
# ? - 0 or 1 occurences
# * - 0 or more occurences

pattern = '^[a].[e].[i].*'

for word in words:
    if re.search(pattern, word): print(word)
    