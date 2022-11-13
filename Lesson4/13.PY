import re
list = ["DEXTER <dexter@hotmail.com>", "VIRUS <virus!@variable.:p>", "GALINA <galka@kbtu.kz>"]

pattern = "[A-Z]+\s[<][a-z!$%&]+[@][a-z]+[.][a-z]+[>]"

for line in list:
    if re.search(pattern, line): print(line)