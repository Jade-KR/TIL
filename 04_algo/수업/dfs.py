'''
7
0 1 1 0 1 0 0
0 1 1 0 1 0 1
1 1 1 0 1 0 1
0 0 0 0 1 1 1
0 1 0 0 0 0 0
0 1 1 1 1 1 0
0 1 1 1 0 0 0
'''
import sys
sys.stdin = open('prac.txt')

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
print(arr)
visited = [0 for i in range(n)]
cnt = 0
def dfs(v):
    visited[v] = 1
    print(v, end=" ")

    for w in range(n):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            dfs(1)
            cnt += 1

