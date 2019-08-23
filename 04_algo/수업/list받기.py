for tc in range(T):
    row, col = map(int, input().split())
    data = [[0 for _ in range(col) for _ in range(row)]]
    for i in range(row):
        data[i] = list(map(int, input().split()))

# data = [list(map(int, input().split())) for _ in range(row)]
