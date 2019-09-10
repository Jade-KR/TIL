import heapq

# heap = [7, 2, 5, 3, 4, 6]
# heapq.heapify(heap)
# print(heap)
# heapq.heappush(heap, 1)
# print(heap)
# while heap:
#     print(heapq.heappop(heap), end = " ")


tmp = [7, 2, 5, 3, 4, 6]
heap2 = []
for i in range(len(tmp)):
    heapq.heappush(heap2, (-tmp[i], tmp[i]))
heapq.heappush(heap2, (-1, 1))
print(heap2)
while heap2:
    print(heapq.heappop(heap2)[1], end = " ")