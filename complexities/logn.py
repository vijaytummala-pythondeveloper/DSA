count = 0
def lognfun(n):

    if n <= 1 :
        return "done"
    else:
        globals()['count'] = globals()['count'] + 1
        return lognfun(n//2)

lognfun(128)
print(count)