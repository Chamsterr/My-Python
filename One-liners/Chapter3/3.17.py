## Зависимости
from xml.etree.ElementInclude import include
import numpy as np

## Данные: популярные учетные записи Instagram (миллионы подписчиков)
inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

# my
superstar = inst[np.nonzero(np.array(list(map(int, inst[:, 0]))) > 100), 1]

superstar = inst[inst[:,0].astype(float) > 100, 1]

print(superstar)