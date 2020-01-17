import sys
sys.stdin = open("거짓말.txt")

N, M = map(int, input().split())
trueList = [list(map(int, input().split()))]
guestList = [list(map(int, input().split())) for _ in range(M)]
