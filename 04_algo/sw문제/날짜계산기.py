import sys
sys.stdin = open('날짜계산기.txt')

d=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(int(input())):
    g=0
    w,x,y,z=list(map(int,input().split()))
    g+=z-x+1+sum(d[w-1:y-1])
    print('#{} {}'.format(i+1, g))