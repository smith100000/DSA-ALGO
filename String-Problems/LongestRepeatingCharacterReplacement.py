

def Longest_repating_character(s,k):
    l=0
    ans=0
    d={}
    for r in range(len(s)):
        if s[r] not in d:
            d[s[r]]=0
        d[s[r]]+=1
        count=r-l+1
        if count-max(d.values())<=k:
            ans=max(ans,count)
        else:
            d[s[l]]-=1
            l+=1
    return ans
s=input()
k=int(input())
print(Longest_repating_character(s,k))
