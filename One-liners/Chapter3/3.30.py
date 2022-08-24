## Зависимости
import numpy as np
## Данные: каждая строка соответствует корзине для покупок конкретного покупателя
## строка = [курс 1, курс 2, эл. книга 1, эл. книга 2]
## значение 1 означает, что товар был куплен

basket = np.array([ [0, 1, 1, 0],
                    [0, 0, 0, 1],
                    [1, 1, 0, 0],
                    [0, 1, 1, 1],
                    [1, 1, 1, 0],
                    [0, 1, 1, 0],
                    [1, 1, 0, 1],
                    [1, 1, 1, 1] ])

copurchases = [(i, j, np.sum(basket[:,i] + basket[:,j] == 2)) 
                for i in range(4) for j in range(i+1,4)]