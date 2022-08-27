import re

text = 'if you use words too often words become used'

result_test = re.search('[^\s]*', text)

result = re.search('(?P<x>[^\s]*)(?P=x)', text)
print(result)