import sys
sys.stdin = open('쉬운계단수.txt')

N = int(input())
data = [[0]*10 for _ in range(N+1)]
cnt = 0

for k in range(1, N+1):
    for p in range(10):
        if k == 1:
            data[k][p] = 1
            continue
        if p == 0:
            data[k][p] = data[k-1][p+1]
        elif p == 9:
            data[k][p] = data[k-1][p-1]
        elif 0 < p < 9:
            data[k][p] = data[k-1][p-1] + data[k-1][p+1]

for j in range(1, 10):
    cnt += data[N][j]

print(cnt % 1000000000)
# 1
# 2
# 3
# 9
#
# 10 12
# 21 23
# 32 34
# 98
#
# 101 121 123
# 210 212 232 234
# 321 323 343 345
#
#
# 1010 1012 1210 1212 1232 1234
