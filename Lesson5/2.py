list = []

for i in range(6):
    a = int(input())
    list.append(a)

# list.sort()
list.sort()

for number in list:

    if number % 2 == 1: 
        print(number)
        break