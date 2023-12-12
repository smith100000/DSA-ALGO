

def can_place_flowers(l,n):
    l=[0]+l+[0]
    for i in range(1,len(l)-1):
        if l[i-1]==0 and l[i]==0 and l[i+1]==0:
            l[i]=1
            n-=1
    return n<=0

l=list(map(int,input().split()))
n=int(input())
print(can_place_flowers(l,n))