import sys
sys.stdin = open('회전초밥.txt')

N, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(N)]
memo = [0]*(d+1)
cnt = 0

# 처음 부터 k번째까지 연속으로 먹은 종류들 체크
for i in range(k):
    memo[dishes[i]] += 1
memo[c] += 1

# 먹은 종류의 개수 answer에 저장
for i in range(1, d+1):
    if memo[i] > 0:
        cnt += 1
ans = cnt

# 체크한 것 다음 접시부터 확인
for i in range(k, N+k):
    memo[dishes[i % N]] += 1
    # 새로운 종류의 음식을 먹으면 +1
    if memo[dishes[i % N]] == 1:
        cnt += 1
    # 그 전에 먹었던 종류의 음식들 -1 해줌.
    memo[dishes[i-k]] -= 1
    if memo[dishes[i-k]] == 0:
        cnt -= 1
    # 현재 먹은 음식들 종류의 개수와 이전에 먹었던 음식 종류의 개수 중 높은 것.
    ans = max(ans, cnt)

print(ans)