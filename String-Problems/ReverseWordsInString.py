

def reverse_words(s):
    s=s.split()
    l=[]
    for i in range(len(s)-1,-1,-1):
        l.append(s[i])
    return " ".join(l)

s=input()
print(reverse_words(s))
