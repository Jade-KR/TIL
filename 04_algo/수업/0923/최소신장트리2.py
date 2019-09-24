import sys
sys.stdin = open('최소신장트리.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(E)]

