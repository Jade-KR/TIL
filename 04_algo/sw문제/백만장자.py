import sys
sys.stdin = open("백만장자.txt")


def pop():
    if len(stack) == 0:
        return
    return stack.pop()


def push(target):
    stack.append(target)


T = int(input())
for tc in range(1, T+1):
    d = int(input())
    data = list(map(int, input().split()))
    total = 0
    stack = []
    d_pop = []

    # for i in range(d-2, -1, -1):
    #     if data[i] < max(data[i+1::]):
    #         total += max(data[i+1::]) - data[i]
    #
    # print('#{} {}'.format(tc, total))

    for i in range(len(data)-1):
        if data[i] <= data[i+1]:
            push(data[i])

