text = "TTTTAACCA"
pattern = "TTA"
m = len(pattern)
n = len(text)
def bruteForce(text, pattern):
    i = 0
    j = 0
    while j < m and i < n:
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == m:
        return i - m
    else:
        return -1


def bruteForce2(text, pattern):
    for i in range(len(text)-len(pattern)+1):
        cnt = 0
        for j in range(len(pattern)):
            if text[i+j] != pattern[j]:
                break
            else:
                cnt += 1
        if cnt >= len(pattern):
            return i
    return -1


print("{}".format(bruteForce2(text, pattern)))
print(text.find(pattern))