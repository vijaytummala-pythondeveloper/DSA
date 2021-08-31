def fibonacci_list(n):
    fib_list = [0,1]
    for i in range(2,n+1):
        fib_list.append(fib_list[i-1]+fib_list[i-2])
    return fib_list[n]

print(fibonacci_list(500))