import sys
sys.stdin = open('prac.txt')

a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in b:
    if i in a:
        print(b.index(i))

print(a)