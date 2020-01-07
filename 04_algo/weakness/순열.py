def perm(n,k):
    if k == n:
        print(A)
        return
    else:
        for i in range(k,n):
            A[i], A[k] = A[k], A[i]
            perm(n,k+1)
            A[i], A[k] = A[k], A[i]

A= [1,2,3,4,5,6]
perm(6,0)