import sys
sys.stdin = open("view.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())   # 100
    arr = list(map(int, input().split()))
    total = 0

    for i in range(2, N-2):
        tmp1 = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        for j in tmp1:

        if arr[i] == 0:
            pass
        tmp = (max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]))
        if arr[i] - tmp > 0:
            total += arr[i] - tmp

    print("#{} {}".format(tc, total))