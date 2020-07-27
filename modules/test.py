import re

string = 'My Name is Santosh rai'

a = re.search('My', string)

print(a.span())