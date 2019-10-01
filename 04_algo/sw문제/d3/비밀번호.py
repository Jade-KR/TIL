import sys
sys.stdin = open('비밀번호.txt')

def check(D):
    for i in range(len(D) - 1):
        if D[i] == D[i + 1]:
            D.pop(i)
            D.pop(i)
            check(D)

T = 10
for tc in range(1, T+1):
    n, data = map(str, input().split())
    N = int(n)
    D = list(data)
    flag = 0

    for i in range(len(D)):
        D[i] = int(D[i])

    while flag != 1:
        for i in range(len(D)-1):
            if D[i] == D[i+1]:
                D.pop(i)
                D.pop(i)
                break

        for i in range(len(D)-1):
            if D[i] != D[i+1]:
                flag = 0
            elif D[i] == D[]


    print(D)

