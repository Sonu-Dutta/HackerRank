        
import re

def isBalanced(s):
    p= "\[\]|\(\)|\{\}"
    while re.search(p,s):
        s = re.sub(p,"",s)
    return "NO" if s else "YES"

for i in range(int(input())):
    print(isBalanced(input()))
