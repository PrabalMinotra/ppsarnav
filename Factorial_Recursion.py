def facto(n):
    if n == 1:
        return 1
    elif n == 0 :
        return 0
    else:
        return n*facto(n-1)


print(facto(500))