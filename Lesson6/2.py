import re
f = open('students.txt', 'r')

d = f.readlines()

for line in d:
    l = line.split()

    print(re.findall('[a-z]+[.][a-z]+$', l[2])) #b.a

f.close()