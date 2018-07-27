import re
 
str = '''"
100
LINK
DISPLAY
SYMBOL
"'''
 
regex = r'"([\s\S]*)"'
matches = re.findall(regex, str)
for match in matches:
    print(match)