Boots = {
    "size": 37,
    "color": "black",
    "heels": "yes",
    "material": "leather"
    }

Crocs = {
    "size": 38,
    "color": "white",
    "heels": "no",
    "material": "non-leather"
    }

Sneakers = {
    "size": 38,
    "color": "white",
    "heels": "yes",
    "material": "non-leather",
    "shoelaces": "no"
    }

Wedges = {
    "size": 40,
    "color": "orange",
    "heels": "yes",
    "material": "leather",
    "shoelaces": "yes"
    }

prices = {
    "Boots": 4000,
    "Crocs": 2000,
    "Sneakers": 1500,
    "Wedges": 3000}

col = input("input color: ")
s = int(input("input size: "))
found = False
if Boots["color"] == col and Boots["size"] == s:
    print("Boots: ", Boots)
    found = True

if Crocs["color"] == col and Crocs["size"] == s:
    print("Crocs: ",Crocs)
    found = True

if Sneakers["color"] == col and Sneakers["size"] == s:
    print("Sneakers: ",Sneakers)
    found = True

if Wedges["color"] == col and Wedges["size"] == s:
    print("Wedges: ",Wedges)
    found = True


if found == False: 
    print("No")
