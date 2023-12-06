

def palindromic_count_substrings(s):
    r1=0
    for i in range(len(s)):
        l=r=i
        while(l>=0 and r<len(s) and s[l]==s[r]):
            r1+=1
            l-=1
            r+=1
        l=i
        r=i+1
        while(l>=0 and r<len(s) and s[l]==s[r]):
            r1+=1
            l-=1
            r+=1
    return r1
s=input()
print(palindromic_count_substrings(s))

