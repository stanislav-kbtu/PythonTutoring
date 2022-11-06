sum = 2
for i in range(0, 10, 2): 
    sum = sum + i
    print(sum, i)
    # 1-st iteration: i = 0, sum = 2
    # 2-nd iteration: i = 2, sum = 4
    # 3-rd iteration: i = 4, sum = 8
    # 4-th iteration: i = 6, sum = 14
    # 5-th iteration: i = 8, sum = 22

print(sum)