import sys
sys.stdin = open('표준입출력.txt')

T = int(input())
N, M = map(int, input().split())
a = [list(map(int, input())) for _ in range(5)]

print(T)
print('{} {}'.format(N, M))
for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end='')
    print()