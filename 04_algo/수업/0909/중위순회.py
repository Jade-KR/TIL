def inorder_traverse(T): #수정
    if T:
        inorder_traverse(arr[T][0])
        print(data[T-1][1], end= '')
        inorder_traverse(arr[T][1])

import sys
sys.stdin = open('중위순회.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]

    arr = [[0, 0, 0] for _ in range(N+1)]

    for i in range(N):
        if len(data[i]) == 4:
            arr[i+1][0] = int(data[i][2])
            arr[i+1][1] = int(data[i][3])
            arr[i+1][2] = int(i+1)
        elif len(data[i]) == 3:
            arr[i + 1][0] = int(data[i][2])
            arr[i + 1][2] = int(i + 1)
        else:
            arr[i + 1][2] = int(i + 1)

    visit = [0 for _ in range(N + 1)]
    print('#{}'.format(tc), end=" ")
    inorder_traverse(1)
    print()
