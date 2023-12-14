

def daily_temperatue(l):
    ans=[0]*len(l)
    stack=[]
    for i in range(len(l)-1,-1,-1):
        while stack and l[i]>=l[stack[-1]]:
            stack.pop()
        if stack:
            ans[i]=l[-1]-i
        else:
            ans[i]=0
        stack.append(i)
    return ans

l=list(map(int,input().split()))
print(daily_temperatue(l))