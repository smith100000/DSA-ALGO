

def contains_duplicate(l):
    s=set()
    for i in l:
        if i in s:
            return True
        s.add(i)
    if len(s)==len(l):
        return False
    else:
        return True
    
l=list(map(int,input().split()))
print(contains_duplicate(l))