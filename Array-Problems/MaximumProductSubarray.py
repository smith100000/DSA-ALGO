

def max_product(l):
    cur_max,cur_min=1,1
    res=l[0]
    for i in l:
        vals=(i,i*cur_max,i*cur_min)
        cur_max=max(vals)
        cur_min=min(vals)
        res=max(res,cur_max)
    return res

l=list(map(int,input().split()))
print(max_product(l))