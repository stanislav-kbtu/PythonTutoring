list = [10, 465, -10, 0, 100, 120, -45, 2]
smallest_number = list[0] # 10, -10


for i in range( len(list) ):

    if list[i] < smallest_number: 
        smallest_number = list[i]
print(smallest_number)

