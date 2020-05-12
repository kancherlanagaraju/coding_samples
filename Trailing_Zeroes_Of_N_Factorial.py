def findTrailingZeroes(N) :

    zeros = 0
    i = 5

    while (N/i >= 1):
        print("i value is :", i)
        zeros += N // i
        print("total zeroes:",zeros)
        i *= 5
    return zeros

print(findTrailingZeroes(25))