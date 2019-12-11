import sys
sys.stdin = open("감시.txt")

def perm(arr=[]):
    if len(arr) == cnt:
        print(arr)
        for k in range(cnt):


    else:
        for i in range(4):
            arr.append(data[i])
            perm(arr)
            arr.pop()

def check(x, y):
    pass

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cctv = []
direction = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cnt += 1
            cctv.append((i, j))



data = [1, 2, 3, 4]

# for a in range(N):
#     for b in range(M):
#         if 0 < office[a][b] < 6:
#             check(a, b)
perm()
print(cctv)