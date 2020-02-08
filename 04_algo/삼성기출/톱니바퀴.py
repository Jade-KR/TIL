import sys
sys.stdin = open('톱니바퀴.txt')

cogs = [[0]] + [list(map(str, input())) for _ in range(4)]
K = int(input())
info = [list(map(int, input().split())) for _ in range(K)]
ans = 0


def checkRight(v, d):
    if 1 < v < 5:
        if checkContact[v-1][0] != checkContact[v][1]:
            if d == 1:
                t = cogs[v].pop()
                cogs[v].insert(0, t)
            else:
                t = cogs[v].pop(0)
                cogs[v].append(t)

            checkRight(v+1, -d)
def checkLeft(v, d):
    if 1 <= v < 4:
        if checkContact[v + 1][1] != checkContact[v][0]:
            if d == 1:
                t = cogs[v].pop()
                cogs[v].insert(0, t)
            else:
                t = cogs[v].pop(0)
                cogs[v].append(t)

            checkLeft(v - 1, -d)

for k in range(K):
    checkContact = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(1, 5):
        checkContact[i][0], checkContact[i][1] = cogs[i][2], cogs[i][6]

    if info[k][1] == 1:
        t = cogs[info[k][0]].pop()
        cogs[info[k][0]].insert(0, t)
    else:
        t = cogs[info[k][0]].pop(0)
        cogs[info[k][0]].append(t)

    checkRight(info[k][0]+1, -info[k][1])
    checkLeft(info[k][0]-1, -info[k][1])

for i in range(1, 5):
    if cogs[i][0] == '1':
        if i == 1:
            ans += 1
        else:
            ans += 2**(i-1)
print(ans)