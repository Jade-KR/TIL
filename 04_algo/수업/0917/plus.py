def plus(n):
    if n <= 1:
        return 1
    else:
        return n + plus(n-1)
print(plus(10))


