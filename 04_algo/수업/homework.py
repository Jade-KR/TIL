# import sys
# sys.stdin = open("0814.txt")


#
# T = 10
# N = input()
# for tc in range(1, T+1):
#     sum = 0
#     val = [list(map(int, input().split())) for _ in range(100)]
#     print(val)
'''C=[[1,2,3],[4,5,6],[7,8,19]]
print(C)
col = []
sum_c = 0
row = []
sum_r = 0
dia_r = []
sum_dr = 0
dia_l = []
sum_dl = 0

for i in range(len(C)):
    for j in range(len(C)):
        sum_c += C[i][j]
        sum_r += C[j][i]
    sum_dr += C[i][i]
    sum_dl += C[-i][-i]
    col.append(sum_c)
    row.append(sum_r)
    sum_c = 0
    sum_r = 0
dia_r.append(sum_dr)
dia_l.append(sum_dl)
print(col)
print(row)
print(dia_r)
print(dia_l)

max_col = col[0]
max_row = row[0]
for k in col:
    if max_col < k:
        max_col = k

for k in row:
    if max_row < k:
        max_row = k

print(max_col)
print(max_row)


'''
import sys

sys.stdin = open("0814.txt")

T = 10
for tc in range(1, T + 1):
    N = input()
    C = [list(map(int, input().split())) for _ in range(100)]
    sum_all = []
    for i in range(len(C)):
        sum_r = 0
        for j in range(len(C)):
            sum_r += C[i][j]
        sum_all.append(sum_r)

    for i in range(len(C)):
        sum_r = 0
        for j in range(len(C)):
            sum_r += C[j][i]
        sum_all.append(sum_r)

    sum_r = 0
    for i in range(len(C)):
        sum_r += C[i][i]
    sum_all.append(sum_r)

    sum_r = 0
    for i in range(len(C)):
        sum_r += C[i][-1 - i]
    sum_all.append(sum_r)

    max_sum = sum_all[0]

    for i in sum_all:
        if max_sum < i:
            max_sum = i
    print('#{} {}'.format(tc, max_sum))
