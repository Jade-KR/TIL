def bfs(v):
    queue = [] #큐 생성
    queue.append(v) #시작점 v를 큐에 삽입(enQueue)
    visited[v] = 1
    print(v, end=" ")
    while len(queue) != 0:
        t = queue.pop(0)
        for w in range(1, V+1):
            if G[t][w] == 1 and visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                # visited[w] = visited[t] + 1 #떨어진 거리

                print(w, end=" ")

import sys
sys.stdin = open('BFS.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for i in range(V+1)] for j in range(V+1)]
visited = [0 for _ in range(V + 1)]
for i in range(0, len(temp), 2):
    G[temp[i]][temp[i+1]] = 1
    G[temp[i+1]][temp[i]] = 1
for i in range(V+1):
    print("{} {}".format(i, G[i]))
bfs(1)
print(visited)