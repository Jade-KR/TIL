import sys
sys.stdin = open('연습문제1.txt')

data = input()

for i in range(0, len(data), 7):
    print(int(data[i: i+7], 2)) #int(데이터, x진수) = x진수를 10진수로 바꿔줌










for i in range(10):
    n = 0
    for j in range(i*7, i*7+7, 1):
        n = n*2 + arr[j]
    print(n, end=" ")
print()