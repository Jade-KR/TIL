n = int(input())
cmp = [3, 6, 9]
tmp = []
for i in range(1, n+1):
    if i > 0 and i <= 10:
        if i % 3 == 0:
            i = '-'
        tmp.append(i)

    elif i >= 10 and i <= 100:
        if i // 10 in cmp and i % 10 in cmp:
            i = '--'
        elif i // 10 in cmp:
            i = '-'
        elif i % 10 in cmp:
            i = '-'
        tmp.append(i)

    elif i >= 100 and i <= 1000:
        if i // 100 in cmp:
            if i // 10 in cmp and i % 10 in cmp:
                i = '--'
            elif i // 10 in cmp:
                i = '-'
            elif i % 10 in cmp:
                i = '-'
            tmp.append(i)

        elif

for i in tmp:
    print(i, end=" ")

