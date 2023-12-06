  

def search(l1,k):
    l,r=0,len(l1)-1
    while(l<=r):
        if l1[l]==k:
            return l
        if l1[r]==k:
            return r
        l+=1
        r-=1
    return -1

l1=list(map(int,input().split()))
k=int(input())
print(search(l1,k))