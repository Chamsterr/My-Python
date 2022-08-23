## Зависимости
import re

## Данные
text = 'peter piper picked a peck of pickled pepper'

result = re.findall('p.*?e.*?r ' , text)
print(result)