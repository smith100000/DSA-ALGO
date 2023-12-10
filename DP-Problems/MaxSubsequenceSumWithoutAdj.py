

def max_subsequence(l,dp,i):
    if i>=len(l):
        return 0
    if dp[i]==-1:
        dp[i]=max(max_subsequence(l,dp,i+2)+l[i],max_subsequence(l,dp,i+1))
    return dp[i]

l=list(map(int,input().split()))
dp=[-1]*len(l)
print(max_subsequence(l,dp,0))