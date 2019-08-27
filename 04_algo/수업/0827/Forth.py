import sys
sys.stdin = open('Forth.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(input().split())
    arr = []
    s = []
    try:
        for i in range(len(data)-1):
            if data[i].isdigit():
                s.append(data[i])
            else:
                # if not s:
                #     result = 'error'
                #     s.append(result)
                #     break
                num2 = int(s.pop())
                # if not s:
                #     result = 'error'
                #     s.append(result)
                #     break
                num1 = int(s.pop())
                if data[i] == "+":
                    result = num2 + num1
                elif data[i] == '-':
                    result = num2 - num1
                elif data[i] == '*':
                    result = num2 * num1
                elif data[i] == '/':
                    result = num2 // num1
                s.append(str(result))
    except:
        s.append('error')
    if len(s) > 1:
        result = 'error'
        s.append(result)
    print('#{} {}'.format(tc, s[-1]))