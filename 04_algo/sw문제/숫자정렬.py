import sys
sys.stdin = open('숫자정렬.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    tmp = sorted(data)
    print('#{} '.format(tc), end="")
    for i in tmp:
        print(i, end=" ")
    print()