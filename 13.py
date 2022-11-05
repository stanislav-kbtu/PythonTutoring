degree = int(input())
measure = input()

if measure == 'f':
    print((5/9)*degree-((32*5)/9), "celcius")

if measure == 'c':
    print(degree * (9/5) + 32, "farehnheit")

if measure != 'c' and measure != 'f': 
    print("Error")
 