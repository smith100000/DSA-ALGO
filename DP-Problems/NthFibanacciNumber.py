
# Bottom-up Approach

def fib_bu(N,dp):
    dp[0]=0
    dp[1]=1
    for i in range(2,N+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[N]


# Top-dowm Approach

def fib_td(N,dp):
    if N<=1:
        return N
    if dp[N]==-1:
        dp[N]=fib_td(N-1,dp)+fib_td(N-2,dp)
    return dp[N]


N=int(input())
dp=[-1]*(N+1)
print(fib_td(N,dp))

        