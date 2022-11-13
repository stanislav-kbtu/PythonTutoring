import re

sentences = """Hello i`m from Africa. I`m 13 years old. My phone number is 87015463434. Goodbye. 
Red. Green hello bad here there 8-778-167-45-43"""

# re.search(), re.findall(), re.sub(), re.split()

pattern = "\d.?\d\d\d.?\d\d\d.?\d\d.?\d\d"

list = re.findall(pattern, sentences)

print(list)

