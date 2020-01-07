import sys
sys.stdin = open('prac.txt')

N = int(input())
data = [0]
data += list(map(int, input().split()))
tmp = [0]*(N+1)
ans = -987765543

for i in range(1, N+1):
    tmp[i] = max(tmp[i-1] + data[i], data[i])
    ans = max(ans, tmp[i])

print(ans)