import re
txt = '<div>hello world</div>'
test = '<div> 2595958 <small><small> </div>'

print(re.findall('<.*>', txt))
# ['<div>hello world</div>']

print(re.findall('<.*?>', txt))
# ['<div>', '</div>']

print(re.findall('>.*?<', test))

то_что_нужно = re.findall('>.*?<', test)[0][2:-2]
print(то_что_нужно)