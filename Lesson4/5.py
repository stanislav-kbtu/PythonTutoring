import re
text = """Theydfgd dfg dg df dfgdfdfgd app_le d43tfdbgd vcbdf43@#$ ora_nge"""

pattern1 = "[_]"
pattern2 = ""

print(re.sub(pattern1, pattern2, text))