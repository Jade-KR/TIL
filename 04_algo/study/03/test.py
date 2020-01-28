import sys, collections
sys.stdin = open('후보추천.txt')
N = int(input())
V = int(input())
S = list(map(int, input().split()))
voted = [0 for _ in range(102)]
ans = collections.deque()

for s in S:
    mini = 1001
    if voted[s]:
        voted[s] += 1
    else:
        ans.append(s)
        voted[s] = 1

    for an in ans:
        if voted[an] < mini:
            mini = voted[an]
            a = an
    if len(ans) > N:
        if ans[0] == a:
            ans.popleft()
        else:
            ans.remove(a)
        voted[a] = 0

for answer in sorted(ans):
    print(answer, end=" ")