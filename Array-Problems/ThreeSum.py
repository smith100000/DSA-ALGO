

def three_sum(l):
    l.sort()
    l1=[]
    for i in range(len(l)-2):
        j=i+1
        k=len(l)-1
        while(j<k):
            sum=l[i]+l[j]+l[k]
            if(sum==0):
                l2=[]
                l2.append(l[i])
                l2.append(l[j])
                l2.append(l[k])
                l2.sort()
                if l2 not in l1:
                    l1.append(l2)
                j+=1
            elif sum<0:
                j+=1
            else:
                k-=1
    return l1

l=list(map(int,input().split()))
print(three_sum(l))