def nth_fibonacci_number(n):
    return int(
        1/(5)**0.5 *(
        (((1 + (5)**0.5)/2)**n) - (((1 - (5)**0.5)/2)**n)
    )
    )

res = nth_fibonacci_number(500)
print(res)