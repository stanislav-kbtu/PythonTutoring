import re

words = ["ab123df", "dfg124gdf", "ABD12HGF", "aabcd1dfgd", "768a", "u34", "ABC654UYH"]

pattern = "[a-zA-Z]+\d{3}[a-zA-z]+"
pattern2 = "[A-Z]+\d{3}[A-Z]+"
for word in words:
    if re.search(pattern2, word): print(word)

