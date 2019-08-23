import sys
sys.stdin = open('ladder.txt')
T = 10
for tc in range(1, T+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    g = 0



    for i in range(100):
        if arr[99][i] == 2:
            g = i
            break

    for i in range(98, -1, -1):
        if not g - 1 < 0:
            if arr[i][g-1]:
                while 1:
                    if not g - 1 < 0:
                        if arr[i][g-1] == 0:
                            break
                        else:
                            g -= 1

                    else:
                        break
                continue

        if not g + 1 > 99:
            if arr[i][g + 1]:
                while 1:
                    if not g + 1 > 99:
                        if arr[i][g + 1] == 0:
                            break
                        else:
                            g += 1

                    else:
                        break
                continue

    print('#{} {}'.format(tc, g))



