data = "2+3*4/5"
s = []

for i in range(len(data)):
    if data[i] == '+' or data[i] == '-' or data[i] == '*' or data[i] == '/':
        s.append(data[i])
    else:
        print(data[i], end="")

while len(s) != 0:
    print(s.pop(), end="")