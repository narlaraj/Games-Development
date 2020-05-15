import re
NameAge='''
We need to inform him with the latest information
'''
regex=re.compile("inform")
NameAge=regex.sub("Food",NameAge)

print(f"NameAge:{NameAge}")
