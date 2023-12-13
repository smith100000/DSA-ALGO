

def max_vowels(s,k):
    vowels={'a','e','i','o','u'}
    count=0
    max_count=0
    for i in range(k):
        if s[i] in vowels:
            count+=1
    max_count=max(count,max_count)
    l,r=0,k
    while(r<len(s)):
        if s[r] in vowels:
            count+=1
        if s[l] in vowels:
            count-=1
        max_count=max(max_count,count)
        l+=1
        r+=1
    return count

s=input()
k=int(input())
print(max_vowels(s,k))