import sys
sys.stdin = open('반복문자.txt')

T = int(input())
for tc in range(1, T+1):
    data = list(input())
    st = []
    cnt = 1
    for i in data:
        if len(st) != 0:
            if st[-1] == i:
                st.pop()
            else:
                st.append(i)

        else:
            st.append(i)

    print('#{} {}'.format(tc, len(st)))