list = [10, 465, -10, 0, 100, 120, -45, 2]
smallest = list[0]

for number in list:
    if number < smallest: 
        smallest = number
print(smallest)