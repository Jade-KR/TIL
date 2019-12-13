import sys
sys.stdin = open('치킨.txt')

def comb(dep=0):
    global ans
    if len(arr) == M:
        tmp = 0
        for w in range(hc):
            min_d = 98765433
            for e in range(M):
                distance = abs(house[w][0] - arr[e][0]) + abs(house[w][1] - arr[e][1])
                if min_d > distance:
                    min_d = distance
            tmp += min_d
        if ans > tmp:
            ans = tmp
        return
    if dep == cnt:
        return
    for k in range(dep, cnt):
        arr.append(chicken[k])
        comb(k+1)
        arr.pop()

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
cnt = 0
ans = 9876554124
hc = 0
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chicken.append([i, j])
            cnt += 1
        elif data[i][j] == 1:
            house.append([i, j])
            hc += 1


arr = []
comb()
print(ans)