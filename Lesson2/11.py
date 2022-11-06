numbers = [10, 21, 30, 41, 50, 61, 70, 80]

even_count = 0
odd_count = 0

for i in range(8):
    print("Iteration number- ", i)
    if numbers[i] % 2 == 0: 
        print("Even")
        even_count = even_count + 1
    else: 
        odd_count = odd_count + 1
        print("Odd")


print("Even -", even_count)
print("Odd -", odd_count)