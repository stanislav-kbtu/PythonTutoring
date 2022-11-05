secret = "mystery"

for i in range(3):
    print("Guess my word !")
    guess = input()
    if guess == secret: print("Good job")
    else: print("No!")

print("You couldn`t guess it!")
