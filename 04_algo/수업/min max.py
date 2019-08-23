import sys
sys.stdin = open("min max.txt")
T= 10
for tc in range(1, T+1):
   N = int(input())
   val = list(map(int, input().split()))
   for i in range(N):
       max = 1
       min = 100
       max_index = 0
       min_index = 0
       for j in range(100):
           if max < val[j]:
               max = val[j]
               max_index = j
           if min > val[j]:
               min = val[j]
               min_index = j
       val[max_index] -= 1
       val[min_index] += 1
       max = 1
       min = 100
       for j in range(100):
           if max < val[j]:
               max = val[j]
               max_index = j
           if min > val[j]:
               min = val[j]
               min_index = j
   print('#{} {}'.format(tc, max-min))




    # max_b = box[0]
    # min_b = box[0]

    # while n != 0:
    #     max_b = box[0]
    #     min_b = box[0]
    #
    #     for i in range(len(box)):
    #         if box[i] > max_b:
    #             max_b = box[i]
    #
    #         if box[i] < min_b:
    #             min_b = box[i]
    #
    #     max_b -= 1
    #     min_b += 1
    #     n -= 1
    #
    #
    # print(max_b - min_b)
    #



