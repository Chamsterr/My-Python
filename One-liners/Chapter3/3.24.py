## Зависимости
import numpy as np

## Данные (строка = [название, рейтинг])
books = np.array([['Coffee Break NumPy', 4.6],
                  ['Lord of the Rings', 5.0],
                  ['Harry Potter', 4.3],
                  ['Winnie-the-Pooh', 3.9],
                  ['The Clown of God', 2.2],
                  ['Coffee Break Python', 4.7]])

bookss = books[:, 1:2]

find_bestseller = lambda x, y: x[x[:, 1].astype(float) > y]

print(find_bestseller(books, 3))