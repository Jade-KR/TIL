import sys
sys.stdin = open('이진힙.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = list(map(int , input().split()))
    tree = [0 for _ in range(N+2)]
    check = 0

    for i in range(0, len(info)-2, 3):
        tree[i+1] = info[i]
        tree[i+2] = info[i+1]
        tree[i+3] = info[i+2]


    print(tree)
    while check < N//2 + 1:
        if tree[check+1] > tree[check+2]:
            tree[check+1], tree[check+2] = tree[check+2], tree[check+1]
        check += 1
    print(tree)
