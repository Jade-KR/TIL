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
    s_pop = []


