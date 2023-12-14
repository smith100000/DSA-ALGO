

def double_character(s):
    l=[]
    for i in range(len(s)-1,-1,-1):
        if l and l[-1]==s[i]:
            l.pop()
        else:
            l.append(s[i])
    ans=""
    for i in range(len(l)-1,-1,-1):
        ans=ans+l[i]
    return ans

s=input()
print(double_character(s))