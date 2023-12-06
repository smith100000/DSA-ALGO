

def max_subarray(l):
    cur_sum=l[0]
    max_sum=l[0]
    for i in l[1:]:
        cur_sum=max(i+cur_sum,i)
        max_sum=max(max_sum,cur_sum)
    return max_sum

l=list(map(int,input().split()))
print(max_subarray(l))