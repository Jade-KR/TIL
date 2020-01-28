import sys
sys.stdin = open('후보추천.txt')

cnt = 0
N = int(input())
cntVote = int(input())
candidate = list(map(int, input().split()))
frame = [[0, 0, 0]]*N
ans = []
while cnt < cntVote:
    # 후보 번호, 투표 순서, 투표 수
    tmp = [candidate[cnt], cnt, 1]
    checkEmpty = 0
    # 사진 틀이 비었을 때
    for i in range(N):
        if frame[i] != [0, 0, 0]:
            # 사진 틀에 후보가 있으면
            if frame[i][0] == candidate[cnt]:
                frame[i][2] += 1
                checkEmpty = 1
                break
            # 없으면
        else:
            frame[i] = tmp
            checkEmpty = 1
            break
    # 사진 틀이 꽉 찼을 때
    if checkEmpty == 0:
        takeOutList = []
        min_c = 987654334
        # 투표 수 제일 적은 값 찾기
        for k in range(N):
            if min_c > frame[k][2]:
                min_c = frame[k][2]

        # 투표 수 제일 적은애들 모아놓기
        for p in range(N):
            if frame[p][2] == min_c:
                takeOutList.append(p)

        min_t = 987653541
        point = 0
        # 투표 수 적은애들 중에서 사진 틀에 들어온지 오래된 사진 찾기
        for u in takeOutList:
            if min_t > frame[u][1]:
                min_t = frame[u][1]
                point = u
        # 오래된 사진 새로운 사진으로 대체
        frame[point] = tmp
    cnt += 1

for a in range(N):
    ans.append(frame[a][0])

for a in sorted(ans):
    print(a, end=" ")