def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = []
    right = []
    middle = len(arr) / 2
    for i in range(middle-1):
        left.append(i)

    for j in range(middle, len(arr)):
        right.append(i)




import sys
sys.stdin = open('병합정렬.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    m = len(arr)//2

    while
