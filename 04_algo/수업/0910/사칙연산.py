def inorder(T): #수정
    if T:
        inorder(tree[T][0])
        a += data[T-1][1]
        # tmp.append(data[T-1][1])
        inorder(tree[T][1])

import sys
sys.stdin = open('사칙연산.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    data = [list(input().split()) for _ in range(N)]
    tree = [[0 for _ in range(4)] for _ in range(N+1)]
    calc = ['+', '-', '/', '*']
    tmp = []
    a = ''
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] in calc:
                pass
            else:
                data[i][j] = int(data[i][j])

    for i in range(len(data)):
        if len(data[i]) > 2:
            tree[data[i][0]][0] = data[i][2]
            tree[data[i][0]][1] = data[i][3]
            tree[data[i][0]][2] = data[i][1]
        else:
            tree[data[i][0]][2] = data[i][1]

    # print(tree)

    inorder(1)
    for i in tmp:
        a += str(i)
        if type(i) == int:
            eval(a)

    print(a)
    # print('#{} {}'.format(tc, eval(a)))