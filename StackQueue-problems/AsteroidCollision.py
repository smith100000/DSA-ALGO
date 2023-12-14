

def collision(l):
    ans=[]
    i=0
    n=len(l)
    while(i<n):
        if len(ans)==0:
            ans.append(l[i])
        else:
            prev,curr=ans[-1],l[i]
            if prev<0 or curr>0:
                ans.append(l[i])
            else:
                if prev==abs(l[i]):
                    ans.pop()
                elif prev<abs(l[i]):
                    ans.pop()
                    i-=1
        i+=1
    return ans

l=list(map(int,input().split()))
print(collision(l))