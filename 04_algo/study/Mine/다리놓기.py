import sys
sys.stdin = open('다리놓기.txt')

T = int(input())
for tc in range(1, T+1):
    W, E = map(int, input().split())

    pascal = [[1] + [0]*(E) for _ in range(E+1)]

    for i in range(1, E+1):
        for j in range(i+1):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    print(pascal[E][W])