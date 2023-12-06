

def max_area(l1):
    l=0
    h=len(l1)-1
    ans=0
    while(l<h):
        ans=max(ans,(h-l)*min(l1[h],l1[l]))
        if l1[l]<l1[h]:
            l+=1
        else:
            h-=1
    return ans

l1=list(map(int,input().split()))
print(max_area(l1))