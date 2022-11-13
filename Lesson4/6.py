import re
text = """Theydfgd dfg dg df dfgdfdfgd app_le d43tfdbgd vcbdf43@#$ ora_nge"""

pattern1 = "[A-Z]"
pattern2 = "_"

print(re.sub(pattern1, pattern2, text))
