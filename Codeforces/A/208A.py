import re
s=input()
s=s.replace("WUB"," ")
s=s.strip()
print(re.sub(' +',' ',s))