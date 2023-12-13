

def min_number_candides(A):
    l=[1]*len(A)
    for i in range(1,len(A)):
        if A[i]>A[i-1]:
            l[i]=l[i-1]+1
    for i in range(len(A)-2,-1,-1):
        if A[i]>A[i+1] and l[i]<=l[i+1]:
            l[i]=l[i+1]+1
    return sum(l)


A=list(map(int,input().split()))
print(min_number_candides(A))