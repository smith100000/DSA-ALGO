

def count_subsets(l,k,n,i,sum):
    if i==n:
        if sum==k:
            return 1
        else:
            return 0
    sum=sum+l[i]
    ca=count_subsets(l,k,n,i+1,sum)
    sum=sum-l[i]
    cb=count_subsets(l,k,n,i+1,sum)
    return ca+cb

l=list(map(int,input().split()))
k=int(input())
n=len(l)
print(count_subsets(l,k,n,0,0))