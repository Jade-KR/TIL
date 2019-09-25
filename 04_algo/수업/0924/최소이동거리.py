def getMinIdx

def dijkstra(goal):
    D[0] = 0

    for i in range(N+1)

import sys
sys.stdin = open('최소이동거리.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visit = [0] * (N+1)
    D = [987654321] * (N+1)