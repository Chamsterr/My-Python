import re

string = 'helloworld'
regex_1 = 'hello(world)'
regex_2 = '(hello(world))'
res_1 = re.findall(regex_1, string)
res_2 = re.findall(regex_2, string)
print(res_1)
# ['world']
print(res_2)
# [('helloworld', 'world')]