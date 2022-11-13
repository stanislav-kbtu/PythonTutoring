import re
substr = ["1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "0000"]
list = ["4123456789123456", "5123-4567-8912-3456", "61234-567-8912-3456", "4123356789123456", "5133-3367-8912-3456", "5123 - 3567 - 8912 - 3456"]
pattern = "^[456]\d\d\d[-]?\d\d\d\d[-]?\d\d\d\d[-]?\d\d\d\d$"

for number in list:
    valid = "Yes"
    number2 = ""
    if "-" in number:
        number2 = number.replace("-", "")

    for sub in substr:

        if sub in number2: 
            valid = "No"

    if not re.search(pattern, number): 
        valid = "No"

    if valid == "No": print("Invalid")
    else: print("Valid")


