## Зависимости
import re

## Данные
text = 'if you use words too often words become used'

## Однострочник
style_problems = re.search('\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s', ' ' + text + ' ')

## Результат
print(style_problems)