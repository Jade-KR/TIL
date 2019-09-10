def preorder_traverse(T):
    global check
    if T:
        preorder_traverse(arr[T][0])
        preorder_traverse(arr[T][1])
    if T == b:
        check = 0
        return

def findA(p1, p2):
    for i in range(len(p1)):
        for j in range()

def parent(B):
    s = tree[n][2]
    p = []

    while s != 0:
        p.append(s)
        s = tree[s][2]
    return p

import sys
sys.stdin = open('공통조상.txt')

T = int(input())
for tc in range(1, T+1):
    V, E, a, b = map(int, input().split())
    info = list(map(int, input().split()))
    arr = [[0, 0, 0] for _ in range(V + 1)]
    check = 1
    p1 = []
    p2 = []

    for i in range(0, (V - 1) * 2, 2):
        if arr[info[i]][0] == 0:
            arr[info[i]][0] = info[i + 1]
        elif arr[info[i]][0] != 0:
            arr[info[i]][1] = info[i + 1]
        arr[info[i]][2] = info[i]
        if arr[info[i+1]][2] == 0:
            arr[info[i+1]][2] = info[i]


