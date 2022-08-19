## Зависимости
import numpy as np
## Данные: годовые зарплаты в тысячах долларов (за 2025, 2026 и 2027 гг.)

dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]

empoyees = np.array([dataScientist, productManager, designer, softwareEngineer])

empoyees[0, ::2] = empoyees[0, ::2]*1.1
print(empoyees)