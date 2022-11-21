import re 

f = open('students.txt', 'r')

lines = f.readlines()

f.close()


f = open("students2.txt", 'x')

f.close()

f = open('students2.txt', 'w')
counter = 0
for line in lines:
    res = ""
    words = line.split()

    res += words[0].capitalize() + " "
    res += words[1].capitalize() + " "

    if words[2].count(".") == 1:
        res += words[2]

    else:
        pattern = '[a-z][.][a-z]+$'

        res += words[2][:words[2].index('@') + 1] + re.findall(pattern, words[2])[0]

    if len(words[3]) == 7:
        res += " +7(727)" + words[3]
    else:
        res += " +7" + words[3]
    f.write(res + '\n')
    if "@gmail" in res: counter += 1


f.close()

print(counterm, " gmail users.")