import sys
sys.stdin = open('치킨.txt')

def comb(dep=0):
    global ans, result
    if len(arr) == M:
        cmp = 0
        for v in arr:
            x, y = chicken[v]
            min_s = 987654321
            all = 0
            for hx, hy in house:
                tmp = 0
                tmp += abs(x-hx) + abs(y-hy)
                all += tmp
                if min_s > tmp:
                    min_s = tmp
            cmp += min_s
        if result > all:
            result = all
        if ans >= cmp and result > all:
            ans = cmp
        return
    if dep == cnt:
        return
    for k in range(dep, cnt):
        arr.append(a[k])
        comb(k+1)
        arr.pop()

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
cnt = 0
result = 987654321
ans = 987654321
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chicken.append((i, j))
            cnt += 1
        elif data[i][j] == 1:
            house.append((i, j))


a = [i for i in range(cnt)]
arr = []

comb()
print(result)