f = open("file.txt", "r")

for line in f.readlines():
    print(line)

f.close()