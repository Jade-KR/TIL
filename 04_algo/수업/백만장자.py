import sys
sys.stdin = open("백만장자.txt")
T = int(input())
for tc in range(1, T+1):
    d = int(input())
    data = list(map(int, input().split()))
    total = 0

    for i in range(d-2, -1, -1):
        if data[i] < max(data[i+1::]):
            total += max(data[i+1::]) - data[i]

    print('#{} {}'.format(tc, total))