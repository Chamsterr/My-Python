## Зависимости
import re

## Данные
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99', '11:59', '59:59', '24:24', '23:32']

input_ok = lambda x: re.fullmatch('[0-9]{2}.[0-9]{2}', x) !=None
# input_ok_2 = lambda x: re.fullmatch('[0-2][0-9]\:[0-5][0-9]', x) != None
input_ok_2 = lambda x: re.fullmatch('[0-1][0-9]|[2][0-3]\:[0-5][0-9]', x) != None

for x in inputs:
    print(input_ok(x))
    print(input_ok_2(x))
    print('---------------------')
