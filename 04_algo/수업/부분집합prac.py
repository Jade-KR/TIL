arr = [1, 2, 3]

for i in range(1, 1 << len(arr)):
    sum = 0
    for j in range(len(arr)):
        if i & (1 << j):
            sum += arr[j]
            print(arr[j], end=" ")
    print()
    # if sum == 10:
    #     for j in range(len(arr)):
    #         if i & (1 << j):
    #             print(arr[j], end=" ")
    #     print()