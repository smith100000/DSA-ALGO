

def longest_substring_without_repeating(s):
    s1=set()
    left=0
    ans=0
    i=0
    while(i<len(s)):
        if s[i] in s1:
            s1.remove(s[left])
            left+=1
        else:
            s1.add(s[i])
            l=len(s1)
            ans=max(ans,l)
            i+=1
    return ans
s=input()
print(longest_substring_without_repeating(s))
