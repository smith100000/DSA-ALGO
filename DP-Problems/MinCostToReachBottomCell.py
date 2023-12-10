

def min_cost_reach(i,j,dp,l):
    if i<0 or j<0:
        return 10000
    if i==0 and j==0:
        return l[i][j]
    if dp[i][j]==-1:
        dp[i][j]=min(min_cost_reach(i-1,j,dp,l),min_cost_reach(i,j-1,dp,l))+l[i][j]
    return dp[i][j]



m=int(input())
n=int(input())
l=[]
for i in range(m):
    l1=list(map(int,input().split()))[:n]
    l.append(l1)
dp=[[-1 for i in range(n)]for j in range(m)]
print(min_cost_reach(m-1,n-1,dp,l))