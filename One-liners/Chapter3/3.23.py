## Зависимости
import numpy as np

## Данные: оценки за экзамен SAT для различных абитуриентов
sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])


top_three_students = students[np.argsort(sat_scores, axis=0)[:-4:-1]]
print(top_three_students)