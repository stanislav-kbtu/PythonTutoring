import re

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

def Clearing(word):
    res = ""
    for letter in word:
        if letter not in vowels:
            pass
        else: res += letter
    return res

f = open('namelist.txt', 'r')
names = f.readlines()
f.close()
for name in names:
    skelet = Clearing(name)

    if not 'y' in skelet: 
      keep = vowels.index(skelet[0])
      order = True
      for letter in skelet:
          ind = vowels.index(letter)

          if ind == keep:
              pass
          if ind < keep:
              order = False
          if ind > keep:
              keep = ind
      if order == True:
          print(name)

    
