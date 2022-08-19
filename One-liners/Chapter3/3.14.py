import numpy as np
## Данные: измерения индекса качества воздуха, AQI (строка = город)

X = np.array([[ 42, 40, 41, 43, 44, 43 ], # Гонконг
              [ 30, 31, 29, 29, 29, 30 ], # Нью-Йорк
              [ 8, 13, 31, 11, 11, 9 ], # Берлин
              [ 11, 11, 12, 13, 11, 12 ]]) # Монреаль

cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

polluted = set(cities[np.nonzero(X > np.average(X))[0]])
print(polluted)