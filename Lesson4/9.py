import re

f = open("students.txt", "r")

data = f.readlines()

f.close()

pattern = "\d{3}[-]\d{4}"
pattern2 = "([a-z]*)\s([a-z]*)"
pattern3 = "[a-z]*[@][a-z]+[.][a-z]+[.][a-z]+"
list = []

for line in data:
    new_number = "301-" + re.findall(pattern, line)[0]

    res = re.search(pattern2, line)
    new_name = ""
    for name in res.groups():
        new_name += name[0].upper() + name[1:] + " "

    email = re.search(pattern3, line)[0]

    list.append(new_name + email + " " +  new_number)

f = open("students2.txt", "x") # 'x' - create file

for line in list:
    f.write(line + "\n")

f.close()

print("abc\ncd\n")

    