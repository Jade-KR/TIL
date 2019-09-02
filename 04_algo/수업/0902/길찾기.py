import sys
sys.stdin = open('길찾기.txt')

T = 10
for tc in range(1, T+1):
    N, L = map(int, input().split())
    data = list(map(int, input().split()))
    arr1 = [0 for _ in range(100)]
    arr2 = [0 for _ in range(100)]

    for i in range(0, L*2, 2):
        if not arr1[data[i]]:
            arr1[i] = data[i+1]