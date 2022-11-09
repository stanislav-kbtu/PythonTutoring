def Transform(s, n, letter):
    return ((s * n) + letter)*2

s = input()
n = int(input())
let = input()

transformed_string = Transform(s, n, let)

print(transformed_string)