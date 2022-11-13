import re
# 
# re.sub() - replacing
list = ["Apple", "Black", "Nose", "Lie"]
pattern = "[aeyoiu]$"

for word in list:
    if re.search(pattern, word): print(word)