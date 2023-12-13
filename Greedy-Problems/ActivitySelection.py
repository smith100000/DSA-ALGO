

def max_activity_selection(A,B):
    l=[]
    for i in range(len(A)):
        l.append([A[i],B[i]])
    l.sort(key=lambda x: x[1])
    count=1
    e=l[0][1]
    for start,end in l[1:]:
        if e<=start:
            e=end
            count+=1
    return count


A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(max_activity_selection(A,B))