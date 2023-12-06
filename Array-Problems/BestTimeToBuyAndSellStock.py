

def buy_stocks(l):
    prev=l[0]
    ans=0
    for i in l[1:]:
        if i<prev:
            prev=i
        ans=max(ans,i-prev)
    return ans

l=list(map(int,input().split()))
print(buy_stocks(l))
        