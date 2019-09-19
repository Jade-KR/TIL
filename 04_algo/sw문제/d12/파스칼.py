import sys
sys.stdin = open('파스칼.txt')
T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    s = sorted(data)

    s.pop(0)
    s.pop()

    print('#{} {}'.format(tc, int(round(sum(s)/len(s), 0))))
