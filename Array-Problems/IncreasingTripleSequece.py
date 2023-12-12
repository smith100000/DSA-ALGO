

def increasing_triple(l):
    first,second=float('inf')
    for n in l:
        if n<=first:
            first=n
        elif n<=second:
            second=n
        else:
            return True
    return False


l=list(map(int,input().split()))
print(increasing_triple(l))