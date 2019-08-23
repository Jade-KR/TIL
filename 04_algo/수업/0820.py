import sys
sys.stdin = open('0820.txt')
# 작은 수 부터 차례대로 정렬
nnnn=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for tc in range(1, T+1):
    tn, N = input().split()
    text = input().split()
    result = []
    data = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9
    }
    number_list = [0]*10

    for i in text:
        number_list[int(data[i])] += 1
    i = 0
    print('#{}'.format(tc))
    for k in nnnn:
        for l in range(number_list[i]):
            print(k, end=" ")
        i += 1
    print()