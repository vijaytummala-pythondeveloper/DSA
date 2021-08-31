def fibonacci_recurrsion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recurrsion(n-1)+fibonacci_recurrsion(n-2)


print(fibonacci_recurrsion(20))