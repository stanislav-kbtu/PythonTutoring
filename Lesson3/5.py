list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list2_reversed = []

for i in range(4):
    list2_reversed.append( list2[3-i] )

for i in range(4):
    print(list1[i], list2_reversed[i])
