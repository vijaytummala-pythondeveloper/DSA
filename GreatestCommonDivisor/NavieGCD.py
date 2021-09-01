def NaiveGcd(a,b):
    best = 0
    for i in range(1,a+b+1):
        if a%i == 0 and b%i == 0:
            best = i

    return best

print(NaiveGcd(323582235,82758273))