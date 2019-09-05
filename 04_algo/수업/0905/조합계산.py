def comb(n, r):
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return comb(n-1, r-1) + comb(n-1, r)

print(comb(10, 5))

# 큰 수가 나오면 파스칼의 삼각형 만들어서 뽑아서 써야함.