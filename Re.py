import re

string = input()
substring = input()
found = False
for i in range((len(string)-len(substring))+1):
    m = re.match(substring, string[i:])
    if (m):
        match = (i, i+len(substring)-1)
        print(match)
        found = True

if not found:
    print((-1,-1))