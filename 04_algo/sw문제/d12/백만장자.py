import sys
sys.stdin = open("백만장자.txt")

T = int(input())
for tc in range(1, T+1):
    d = int(input())
    data = list(map(int, input().split()))
    total = 0
    stack = []
    s_pop = []
    for i in (d-1, -1, -1):
        stack.append(data[i])
        if data[i] > data[i-1]:


