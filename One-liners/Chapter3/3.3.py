import numpy as np


alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]

employees = np.array(['Alice', 'Bob', 'Tim'])
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

max_income = salaries*(1-taxation)

# most_clear_income = employees[np.nonzero(max_income == np.max(max_income))[0]]
print(employees[np.nonzero(max_income == np.max(max_income))[0]])