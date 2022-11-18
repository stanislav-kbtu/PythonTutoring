numb = int(input())

for i in range(3):
    print("Guess:")
    a = int(input())
    if a < numb: print("The number is more")
    if a > numb: print("The number is fewer")
    if a == numb:
        print("BINGO!")
        break

