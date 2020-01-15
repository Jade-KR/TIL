import sys
sys.stdin = open('파괴된도시.txt')
import collections

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
destroyed = list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
check = [0]*(N+1)
visited = [0]*(N+1)
safe = set()
q = collections.deque()
cnt = 0
ans = []
out = 0

# 파괴된 도시들 체크하는 배열 만들기
for i in destroyed:
    check[i] = 1
# 폭탄 맞으면 안되는 도시 찾기 (safe)
for i in range(M):
    if city[i][0] not in destroyed or city[i][1] not in destroyed:
        safe.add(city[i][0])
        safe.add(city[i][1])

for i in range(M):
    adj[city[i][0]][city[i][1]] = 1
    adj[city[i][1]][city[i][0]] = 1

for k in range(1, N+1):
    if k not in safe:
        q.append(k)

while len(q):
    if out == 1:
        break
    v = q.popleft()
    cnt += 1
    ans.append(v)
    visited[v] = 1
    for w in range(1, N+1):
        if adj[v][w]:
            visited[w] = 1

    if check == visited:
        out = 1



if out == 0:
    print(-1)
else:
    print(cnt)
    for b in ans:
        print(b, end=' ')