S1 = input()
S2 = input()
S3 = input()
longest_string = ""
shortest_string = ""

if len(S3) >= len(S2) and len(S3) >= len(S1):
    longest_string = S3

if len(S2) >= len(S3) and len(S2) >= len(S1):
    longest_string = S2

if len(S1) >= len(S2) and len(S1) >= len(S3):
    longest_string = S1

if len(S3) <= len(S2) and len(S3) <= len(S1):
    shortest_string = S3

if len(S2) <= len(S1) and len(S2) <= len(S3):
    shortest_string = S2

if len(S1) <= len(S2) and len(S1) <= len(S3):
    shortest_string = S1

print(shortest_string + longest_string)