def inorder(T): #수정
    global cnt
    if T:
        inorder(tree[T][0])
        cnt += 1
        tree[T][3] = cnt
        inorder(tree[T][1])

import sys
sys.stdin = open('이진탐색.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [[0, 0, 0, 0] for _ in range(N+1)]
    cnt = 0

    for i in range(1, N+1):
        if i*2 <= N:
            tree[i][0] = i*2
        else:
            tree[i][0] = 0
        if i*2+1 <= N:
            tree[i][1] = i*2 + 1
        else:
            tree[i][1] = 0
        tree[i][2] = i


    inorder(1)
    print('#{}'.format(tc), end =" ")
    for i in range(1, N+1):
        if tree[i][2] == 1:
            R = tree[i][3]
        if tree[i][2] == N//2:
            H = tree[i][3]

    print('{} {}'.format(R, H))