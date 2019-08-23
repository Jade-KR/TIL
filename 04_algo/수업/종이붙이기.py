import sys
sys.stdin = open('종이붙이기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    data = [[0 for _ in range(N//10)] for _ in range(2)]
    print(data)

