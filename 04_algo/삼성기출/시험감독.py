import sys
sys.stdin = open('시험감독.txt')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = N
chk = 0

if B > C:
    big = B
    small = C
    chk = 1
elif B == C:
    big = C
    small = B
else:
    big = C
    small = B

for i in range(N):
    A[i] = A[i] - B
    if A[i] <= 0:
        continue
    # 총감독관이 big 일때.
    if chk == 1:
        cnt += A[i] // small
        A[i] = A[i] % small
        if A[i]:
            cnt += 1
    else:
        # 부감독관이 big 일때.
        cnt += A[i] // big
        A[i] = A[i] % big
        if A[i]:
            cnt += 1
print(cnt)