import numpy as np

#Cоздание одномерного массива из списка
a = np.array([1, 2, 3])
print(a)
# [1 2 3]

#Cоздание двумерного массива из списка списков

b = np.array([[1, 2],
              [3, 4]])
print(b)

# [[1 2]
#  [3 4]]
#Создание трехмерного массива из списка списков списков
c = np.array([[[1, 2],
               [3, 4]],
              [[5, 6],
               [7, 8]]])
print(c)

'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''