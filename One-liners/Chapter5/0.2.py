import re

text = '''
    "One can never have enough socks", said Dumbledore.
    "Another Christmas has come and gone and I didn't
    get a single pair. People will insist on giving me books."
    Christmas Quote
'''

regex = 'Christ.*'

print(re.match(regex, text))
# None

print(re.search(regex, text))
# <re.Match object; span=(70, 110), match="Christmas has come and gone and I didn't">

print(re.findall(regex, text))
# ["Christmas has come and gone and I didn't", 'Christmas Quote'