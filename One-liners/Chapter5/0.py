import re
text = '''A blockchain, originally block chain, is a growing list of records, called blocks, which are linked using cryptography.
'''
print(re.findall('b...k', text))
# ['block', 'block', 'block']

print(re.findall('y.*y', text))
# ['yptography']

test = "ab abc abcc abccdc"
print(re.findall('abc*', test))

print(re.findall('blocks?', text))
# ['block', 'block', 'blocks']