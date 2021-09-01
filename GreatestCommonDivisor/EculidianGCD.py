def EculidianGcd(a,b):
    if b == 0:
        return a
    else :
        rem = a % b
        return EculidianGcd(b,rem)

print(EculidianGcd(100,50))