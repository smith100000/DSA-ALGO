

def min_side_jumps(l):
    curr={2}
    i=0
    j=len(l)
    res=0
    while(i<j):
        obs={l[i]}
        curr=curr.difference(obs)
        if curr==set():
            blockade={l[i-1],l[i]}
            curr={1,2,3}.difference(blockade)
            res+=1
        i+=1
    return res

l=list(map(int,input().split()))
print(min_side_jumps(l))
