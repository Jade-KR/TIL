import sys
sys.stdin = open('나무재테크.txt')

N, M, K = map(int, input().split())
A = [[0]*N] + [list(map(int, input().split())) for _ in range(N)]
info = [list(map(int, input().split())) for _ in range(M)]

print(A)