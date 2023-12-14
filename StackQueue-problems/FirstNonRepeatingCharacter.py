

def first_non_repeating(s):
    ans=""
    l=[]
    dict={}
    for i in s:
        l.append(i)
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
        while l and dict[l[0]]>1:
            l.pop(0)
        if l:
            ans=ans+l[0]
        else:
            ans=ans+"-"
    return ans

s=input()
print(first_non_repeating(s))