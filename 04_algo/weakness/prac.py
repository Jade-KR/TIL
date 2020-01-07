import sys
sys.stdin = open('prac.txt')

def comb(dep=0):
    pass

T = int(input())
for tc in range(1, T+1):
    W, E = map(int, input().split())
    A = [i+1 for i in range(W)]
    arr = [0]*E

    print(A)