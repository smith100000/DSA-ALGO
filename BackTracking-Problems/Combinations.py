

def combinations(n,k,start,comb):
    if len(comb)==k:
        print(comb)
    for i in range(start,n+1):
        comb.append(i)
        combinations(n,k,i+1,comb)
        comb.pop()
    
n=int(input())
k=int(input())
combinations(n,k,1,[])