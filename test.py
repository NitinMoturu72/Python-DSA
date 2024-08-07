import re

string = input()
substring = input()
substring_length = len(substring)

for i in range(len(string) - substring_length + 1):
    m = re.match(re.escape(substring), string[i:])
    if m:
        match = (i, i + substring_length - 1)
        print(match)