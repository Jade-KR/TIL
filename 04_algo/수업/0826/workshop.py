import sys
sys.stdin = open('workshop.txt')

T = 10
for tc in range(1, T+1):
    L = int(input())
    data = input()
    s = []
    arr = []


    for i in data:
        if i not in '+*()':
            s.append(i)

        if not s:
            arr.append(i)
        else:
            if i == '(':
                arr.append(i)

            if i == '*':
                while s[-1] != '*':
                    s.pop()
            if i == '+':
                while s[-1] != '*' and s[-1] != '+':
                    s.pop()

            if i == ')':
                while s[-1] != '(':
                    arr.append(s.pop())


    print(data)