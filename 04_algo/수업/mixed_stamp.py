n = int(input())

data = [i for i in range(n)]
j = 0

cnt_n = 1
cnt_r = ord('A')

for i in range(n):
    for j in range(n-i):
        print(cnt_n, end=" ")
        cnt_n += 1

    for j in range(i+1):
        print(chr(cnt_r), end=" ")
        cnt_r += 1
    print()