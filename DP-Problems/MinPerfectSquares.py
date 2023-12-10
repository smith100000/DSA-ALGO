
# Bottom-up approch

def min_perfect_bu(N,dp):
    dp[0],dp[1],dp[2]=0,1,1
    for i in range(N+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i-(j*j)] + 1)
            j+=1
    return dp[-1]
             

# Top-dowm Approach

def min_prefect_sq(N,dp):
    if N==0:
        return 0
    if dp[N]==-1:
        i,val=1,1000000
        while(i*i<=N):
            val=min(val,min_prefect_sq(N-(i**2),dp))
            i+=1
        dp[N]=val+1
    return dp[N]



N=int(input())
dp=[-1]*(N+1)
print(min_prefect_sq(N,dp))
print(min_perfect_bu(N,dp))