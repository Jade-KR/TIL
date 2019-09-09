def preorder_traverse(T):
    if T:
        print(T, end=" ")
        preorder_traverse(arr[T][0])
        preorder_traverse(arr[T][1])

def inorder_traverse(T): #수정
    if T:
        inorder_traverse(arr[T][0])
        print(T, end= ' ')
        inorder_traverse(arr[T][1])

def postorder_traverse(T): #수정
    if T:
        postorder_traverse(arr[T][0])
        postorder_traverse(arr[T][1])
        print(T, end=' ')

import sys
sys.stdin = open('트리연습.txt')

V = int(input())
info = list(map(int, input().split()))
arr = [[0, 0, 0] for _ in range(V+1)]

for i in range(0, (V-1)*2, 2):
    if arr[info[i]][0] == 0:
        arr[info[i]][0] = info[i+1]
    elif arr[info[i]][0] != 0:
        arr[info[i]][1] = info[i+1]
    arr[info[i+1]][2] = info[i]

visit = [0 for _ in range(V+1)]

print(arr)
print(visit)

preorder_traverse(1)