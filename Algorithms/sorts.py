from cgi import test


def insert_sort(A):
    """Сортировка вставками"""
    for x in range(len(A)):
        k = x
        while k > 0 and A[k - 1] > A[k]:
            A[k - 1], A[k] = A[k], A[k - 1]
            k -= 1


def choose_sort(A):
    """Сортировка выбором"""
    for x in range(0, len(A) - 1):
        for y in range(x + 1, len(A)):
            if A[y] < A[x]:
                A[y], A[x] = A[x], A[y]


def buble_sort(A):
    """Сортировка пузырьком"""
    for bypass in range(1, len(A)):
        for x in range(1, len(A)):
            if A[x - 1] > A[x]:
                A[x - 1], A[x] = A[x], A[x - 1]


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
    print("norm" if A == A_sorted else "ne norm")

    print("Test 2", end=" ")
    print("norm" if A2 == A2_sorted else "ne norm")

    print("Test 3", end=" ")
    print("norm" if A3 == A3_sorted else "ne norm")


if __name__ == "__main__":
    test_sort(buble_sort)
    test_sort(insert_sort)
    test_sort(choose_sort)


ls = (
    lambda a, b: len(a)
    if not b
    else len(b)
    if not a
    else min(ls(a[1:], b[1:]) + (a[0] != b[0]), ls(a, b[1:]) + 1, ls(a[1:], b) + 1)
)

a = "daa"
b = "daa"

print(ls(a, b))


def func(a, b):
    if not a:
        return len(b)
    elif not b:
        return len(a)
    else:
        return min(
            func(a[1:], b[1:]) + (a[0] != b[0]), func(a[1:], b) + 1, func(a, b[1:]) + 1
        )


print(func(a, b))
