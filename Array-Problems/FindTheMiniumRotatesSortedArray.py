

def find_min(l):
    res=l[0]
    left,right=0,len(l)-1
    while(left<=right):
        if l[left]<l[right]:
            res=min(res,l[left])
            break
        m=(left+right)//2
        res=min(res,l[m])
        if l[m]>=l[left]:
            left=m+1
        else:
            right=m-1
    return res

l=list(map(int,input().split()))
print(find_min(l))