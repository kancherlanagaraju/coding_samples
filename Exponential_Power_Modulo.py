def modexp(x,y,p):
    res = 1
    for i in range(y):
        res = res * x
    res = res % p
    return res


print(modexp(1999, 297, 3))


def modexp2(x,y,p):
    res = 1
    x = x % p

    for i in range(y):
        res = res * x
    res = res % p
    return res


print(modexp2(33, 33, 5))




