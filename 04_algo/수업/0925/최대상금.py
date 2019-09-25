def mx(n, c):
    if int(''.join(arr)) in check[c]:
        return
    else:
        check[c].add(int(''.join(arr)))

    if c == count:
        return


    for i in range(n-1):
        for j in range(i+1, n):
            arr[i], arr[j] = arr[j], arr[i]
            mx(n, c+1)
            arr[i], arr[j] = arr[j], arr[i]


import sys
sys.stdin = open('최대상금.txt')

T = int(input())
for tc in range(1, T+1):
    info, cnt = map(str, input().split())
    count = int(cnt)
    arr = list(info)
    check = [set() for _ in range(count+1)]
    mx(len(arr), 0)
    print('#{} {}'.format(tc, max(check[count])))
    # print(check)
'''
    큰 숫자 높은 자리수로 옮기기.
    큰 수가 여러개, 다른자리 수면 낮은 자리수의 숫자 옮기기
    
'''