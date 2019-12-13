import sys
sys.stdin = open('퇴사.txt')

def dfs(idx, info, m):
    global max_m
    if info == 0 or data[idx-1 + info[0]] == 0:
        if max_m < m:
            max_m = m
        return
    m += info[1]
    for k in range(1, N-idx+5):
        next_task = idx + k
        if next_task >= idx+info[0]:
            dfs(next_task, data[next_task], m)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
max_m = 0
for _ in range(5):
    data.append(0)
for i in range(N):
    dfs(i, data[i], 0)

print(max_m)