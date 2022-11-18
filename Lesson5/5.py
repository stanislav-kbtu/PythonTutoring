groceries = ['Banana', 'Orange', 'Apple', "Pear"] 

stock = {
    "Banana": 6,
    "Apple": 1,
    "Orange": 32,
    "Pear": 15}

prices = {
    "Banana": 4,
    "Apple": 2,
    "Orange": 1.5,
    "Pear": 3}


def compute_bill(food):

    total = 0

    for fruit in food:

        if stock[fruit] > 0:
            total = total + prices[fruit]
            stock[fruit] = stock[fruit] - 1
            
        else: 
            print("No such product:", fruit)



    return total


food = ["Banana", "Pear", "Orange", "Apple", "Apple"]
res = compute_bill(food)
print(res)



