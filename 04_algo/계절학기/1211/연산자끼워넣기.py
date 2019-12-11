import sys
sys.stdin = open('연산자끼워넣기.txt')

def dfs(cnt, ans):
    global max_n, min_n
    if cnt == N-1:
        if max_n < ans:
            max_n = ans
        if min_n > ans:
            min_n = ans
        return
    else:
        if oper[0] > 0:
            oper[0] -= 1
            dfs(cnt+1, ans + nums[cnt+1])
            oper[0] += 1

        if oper[1] > 0:
            oper[1] -= 1
            dfs(cnt + 1, ans - nums[cnt + 1])
            oper[1] += 1

        if oper[2] > 0:
            oper[2] -= 1
            dfs(cnt + 1, ans * nums[cnt + 1])
            oper[2] += 1

        # 음수를 나눴을때 // 로 나누면 반올림하기 때문에 int로 감싸주면 뒤에 나머지들 다 날림.
        if oper[3] > 0:
            oper[3] -= 1
            dfs(cnt + 1, int(ans / nums[cnt + 1]))
            oper[3] += 1




N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
cnt = 0
max_n = -987654321
min_n = 987654321
ans = nums[0]

dfs(cnt, ans)

print(max_n)
print(min_n)