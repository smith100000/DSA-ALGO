

def can_jump(l):
    max_jump=0
    for i in range(len(l)):
        if max_jump<i:
            return False
        max_jump=max(max_jump,i+l[i])
    return True

l=list(map(int,input().split()))
print(can_jump(l))