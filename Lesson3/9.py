list = [10, 20, 30, 50, 60, 0, 70, 100]
maximum = list[0]
premax = list[0]

for number in list:
    if number > maximum: 
        maximum = number

for number in list:
    if number > premax and number != maximum: 
        premax = number

print(premax)