

def ways_to_reach_block_cells(i,j,dp,l):
    if i<0 or j<0:
        return 0
    if l[i][j]==0:
        return 0
    if i==0 and j==0:
        return 1
    if dp[i][j]==-1:
        dp[i][j]=ways_to_reach_block_cells(i-1,j,dp,l)+ways_to_reach_block_cells(i,j-1,dp,l)
    return dp[i][j]

m=int(input())
n=int(input())
l=[]
for i in range(m):
    l1=list(map(int,input().split()))[:n]
    l.append(l1)
dp=[[-1 for i in range(n)]for j in range(m)]
print(ways_to_reach_block_cells(m-1,n-1,dp,l))