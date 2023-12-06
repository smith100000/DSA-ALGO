

def product_expert_self(l):
    l1=[1]*len(l)
    left=1
    for i in range(len(l)):
        l1[i]=l1[i]*left
        left=left*l[i]
    right=1
    for i in range(len(l)-1,-1,-1):
        l1[i]=l1[i]*right
        right=right*l[i]
    return l1

l=list(map(int,input().split()))
print(product_expert_self(l))