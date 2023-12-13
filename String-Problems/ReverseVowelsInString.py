
#Two-Pointer Approach

def reverse_vowel_string(s):
    vowels={'a','A','e','E','i','I','o','O','u','U'}
    l=list(s)
    start,end=0,len(s)-1
    while(start<end):
        if l[start] in vowels and l[end] in vowels:
            l[start],l[end]=l[end],l[start]
            start+=1
            end-=1
        elif l[start] not in vowels:
            start+=1
        else:
            end-=1
    return "".join(l)


#Using Stack

def reverse_vowel_string1(s):
    vowels={'a','A','e','E','i','I','o','O','u','U'}
    l=[]
    for i in s:
        if i in vowels:
            l.append(i)
    s1=""
    for i in s:
        if i in vowels:
            s1=s1+l.pop()
        else:
            s1=s1+i
    return s1

s=input()
print(reverse_vowel_string(s))
print(reverse_vowel_string(s))