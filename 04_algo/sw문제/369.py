n = int(input())
tmp = []
for i in range(1, n+1):
    if i % 3 == 0:
        i = '-'

    tmp.append(i)

for i in tmp:
    print(i, end=" ")


# for i in range(1, n+1):
#     if i