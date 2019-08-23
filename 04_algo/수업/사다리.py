def check(data, x, y):
    if x < 0 or x <= size:
        return False
    if y < 0 or y >= size:
        return False
    if data[x][y] == 0:
        return False
    if data[x][y] == 9:
        return False
    return True

def solve(data):
    x, y, newx, newy = 0, 0, 0, 0
