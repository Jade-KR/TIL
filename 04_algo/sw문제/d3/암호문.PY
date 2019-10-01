import sys
sys.stdin = open('암호문.txt')
T = 10
for tc in range(1, T+1):
    L = int(input())
    code = list(map(int, input().split()))
    N = int(input())
    command = list(map(str, input().split()))
    print(command)
