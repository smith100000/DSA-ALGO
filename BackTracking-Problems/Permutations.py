

def void_permutations(A,temp):
    if len(A)==0:
        print(temp)
        return
    for i in range(0,len(A)):
        temp.append(A[i])
        void_permutations(A[0:i]+A[i+1:len(A)],temp)
        #   if nums[i] in combination:
        #   continue
        temp.pop()

A=list(map(int,input().split()))
void_permutations(A,[])
