def factorial(n):
    result = 1
    for i in range(n, 0, -1):
        result = i*result
    return result

print(factorial(5))