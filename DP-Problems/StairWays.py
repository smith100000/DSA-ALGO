
# Bottom-up Approach

def stair_bu(N,dp):
    dp[0]=1
    dp[1]=1
    for i in range(2,N+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[N]


# Top-dowm Approach

def stair_td(N,dp):
    if N<=1:
        return 1
    if dp[N]==-1:
        dp[N]=stair_td(N-1,dp)+stair_td(N-2,dp)
    return dp[N]


N=int(input())
dp=[-1]*(N+1)
print(stair_td(N,dp))
