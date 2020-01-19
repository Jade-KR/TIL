import sys
sys.stdin = open('에라토스테네스.txt')

N, K = map(int, input().split())
cnt = 0
visited = [0]*(N+1)
check = 0

for i in range(2, N+1):
    if check == 1:
        break
    if visited[i] != 0:
        continue
    for j in range(i, N+1, i):
        if check == 1:
            break
        if visited[j] != 0:
            continue
        cnt += 1
        visited[j] = 1
        if cnt == K:
            ans = j
            check = 1
print(ans)

# numbers = [i for i in range(2, N+1)]
# check = 0
# ans = 0
# print(numbers)
# while len(numbers):
#     if check == 1:
#         break
#     t = numbers.pop(numbers.index(min(numbers)))
#     nt = t
#     cnt += 1
#     if cnt == K:
#         ans = t
#         check = 1
#     while nt <= N:
#         if check == 1:
#             break
#         nt = nt + t
#         if nt in numbers:
#             numbers.pop(numbers.index(nt))
#             cnt += 1
#             if cnt == K:
#                 ans = nt
#                 check = 1
#
# print(ans)