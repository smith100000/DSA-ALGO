

def two_sum(l,k):
    dict={}
    for i in range(len(l)):
        if l[i] in dict:
            return dict[l[i]],i
        else:
            dict[k-l[i]]=i
            
l=list(map(int,input().split()))
k=int(input())
print(two_sum(l,k))