from cgi import test


def insert_sort(A):
    """Сортировка вставками"""
    for x in range(len(A)):
        while x > 0 and A[x-1] > A[x]:
            A[x-1], A[x] = A[x], A[x-1] 
            x -= 1


def choose_sort(A):
    """Сортировка выбором"""
    N = len(A)
    for x in range(len(A)):
        for y in range(len(A)):
            if A[y] > A[x]:
                A[y], A[x] = A[x], A[y]

def buble_sort(A):
    """Сортировка пузырьком"""
    N = len(A)
    for bypass in range(1, N):
        for x in range(1, len(A)):
            if A[x-1] > A[x]:
                A[x-1], A[x] = A[x], A[x-1]

def test_sort(sort_func):
    A = [1, 2, 9, 8, 9, 1]
    A_sorted = [1, 1, 2, 8, 9, 9]

    A2 = [1, 1, 1, 1, 1, 1]
    A2_sorted = [1, 1, 1, 1, 1, 1]

    A3 = [11, 3, 4, 5, 1, 6, 9, 10, 11]
    A3_sorted = [1, 3, 4, 5, 6, 9, 10, 11, 11]

    sort_func(A)
    sort_func(A2)
    sort_func(A3)

    print(sort_func.__doc__)
    print("Test 1", end=" ")
    print('norm' if A == A_sorted else "ne norm")

    print("Test 2", end=" ")
    print('norm' if A2 == A2_sorted else "ne norm")

    print("Test 3", end=" ")
    print('norm' if A3 == A3_sorted else "ne norm")

if __name__ == "__main__":
    test_sort(buble_sort)
    test_sort(insert_sort)
    test_sort(choose_sort)