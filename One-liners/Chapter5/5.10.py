## Зависимости
import re

## Данные
text = '''
Alice Wonderland married John Doe.
The new name of former 'Alice Wonderland' is Alice Doe.
Alice Wonderland replaces her old name 'Wonderland' with her new name 'Doe'.
Alice's sister Jane Wonderland still keeps her old name.
'''
print(text)

result = re.sub("Alice Wonderland(?!')", 'Alice Doe',text)
print(result)