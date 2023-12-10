

def ways_to_reach(i,j,dp):
    if i<0 or j<0:
        return 0
    if i==0 and j==0:
        return 1
    if dp[i][j]==-1:
        dp[i][j]=ways_to_reach(i-1,j,dp)+ways_to_reach(i,j-1,dp)
    return dp[i][j]


m=int(input())
n=int(input())
dp=[[-1 for i in range(n)]for j in range(m)]
print(ways_to_reach(m-1,n-1,dp))