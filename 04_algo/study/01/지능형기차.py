import sys
sys.stdin = open('지능형기차.txt')
info = []
for _ in range(4):
    info.append(list(map(int, input().split())))

people = 0
max_p = -1

for i in range(4):
    people = people - info[i][0] + info[i][1]
    if max_p < people:
        max_p = people

print(max_p)