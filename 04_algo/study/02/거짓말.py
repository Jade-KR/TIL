import sys
sys.stdin = open("거짓말.txt")

N, M = map(int, input().split())
trueList = list(map(int, input().split()))
guestList = [list(map(int, input().split())) for _ in range(M)]
ans = M
TL = set(trueList[1:len(trueList)])

# 진실을 알게 되는 사람이 없으면 지민이는 모든 파티에 참가하니까 답은 파티 개수
if trueList[0] == 0:
    print(ans)
else:
    # 파티 수 만큼 반복
    for _ in range(M):
        # 진실 아는 사람들과 같은 파티에 있던 사람들 또한 진실을 아는 사람들에 추가
        # 파티 수 만큼 돌면 소문이 완벽하게 돈다.
        for party in guestList:
            check = 0
            for t in TL:
                if t in party[1:len(party)]:
                    check = 1
                    break
            if check == 1:
                for k in party[1:len(party)]:
                    TL.add(k)

    # 거짓말 할 수 있는 파티 확인
    for party in guestList:
        check = 0
        for t in TL:
            if t in party[1:len(party)]:
                check = 1
                break
        if check == 1:
            ans -= 1


    print(ans)