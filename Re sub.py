import re
import sys
n = input()
if(int(n) < 2):
    code = input()
else:
    code = sys.stdin.read()
    
code = re.sub('(?<= )&&(?= )', " and ", code)
code = re.sub('(?<= )\|\|(?= )', " or ", code)
print(code)