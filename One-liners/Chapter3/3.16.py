import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

indices = np.array([[False, False, True],
                    [False, False, False],
                    [True, True, False]])

print(a[indices])
# [3 7 8]