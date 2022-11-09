# built-in functions: len(), range()

# built-in functions in list: .append() .count()

list = [1, 1, 1, 2, 3, 1, 5, 6, 6]
counter = 0

for number in list:
    if number == 1: 
        counter = counter + 1

print(counter)