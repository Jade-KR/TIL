import sys
sys.stdin = open('토너먼트.txt')


def dvd(a, b):
    if a == b:
        return a
    n_d1 = dvd(a, (a+b)//2)
    n_d2 = dvd((a+b)//2+1, b)

    return play(n_d1, n_d2)


def play(a, b):
    lis = [1, 2, 3]

    if lis[data[a]-2] == data[b]:
        return a
    elif data[a] == data[b]:
        return a
    else:
        return b



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    print('#{} '.format(tc), end="")
    print(dvd(0, len(data)-1)+1)
