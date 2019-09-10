def preorder(T):
    global cnt
    if T:
        cnt += 1
        preorder(tree[T][0])
        preorder(tree[T][1])

import sys
sys.stdin = open('subtree.txt')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    info = list(map(int, input().split()))
    tree = [[0, 0, 0] for _ in range(E+2)]
    cnt = 0
    for i in range(0, len(info), 2):
        if tree[info[i]][0] == 0:
            tree[info[i]][0] = info[i+1]
        elif tree[info[i]][0] != 0:
            tree[info[i]][1] = info[i+1]
        tree[info[i]][2] = info[i]
        if tree[info[i+1]][2] == 0:
            tree[info[i+1]][2] = info[i]

    preorder(N)

    print('#{} {}'.format(tc, cnt))