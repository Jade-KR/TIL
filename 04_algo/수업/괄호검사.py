import sys
sys.stdin = open('괄호검사.txt')

T = int(input())
for tc in range(1, T+1):
    data = input()
    st = []
    result = 1

    for i in data:
        if i == '(' or i == '{':
            st.append(i)
        elif i == '}':
            if len(st) != 0:
                if st[-1] == '{':
                    st.pop()
                else:
                    result = 0
                    break
            else:
                result = 0
                break
        elif i == ')':
            if len(st) != 0:#아닐때 break로 깨줘야함
                if st[-1] == '(':
                    st.pop()
                else:
                    result = 0
                    break
            else:
                result = 0
                break

    if len(st):
        result = 0

    print('#{} {}'.format(tc, result))