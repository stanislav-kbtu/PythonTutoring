n = int(input())

list =[]
for i in range(n):
    a = int(input())
    list.append(a)

increasing = None
for i in range(n): #i : 0, n-1
    if list[i] < list[i + 1]: 
        increasing = True
        break
    if list[i] > list[i + 1]: 
        increasing = False
        break

for i in range(n-1): # i: 0; n - 2
    if increasing == True and list[i] > list[i + 1]:
        print(i)
        break
    if increasing == False and list[i] < list[i + 1]:
        print(i)
        break