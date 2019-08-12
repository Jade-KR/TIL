def bubblesort(a):
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

data = [55, 7, 78, 12, 42] #참조형
bubblesort(data)
print(data)

'''
# def test():
    # a = 100
    # print(a)   읽기

#a = 100     값형
#test()
#print(a)
'''