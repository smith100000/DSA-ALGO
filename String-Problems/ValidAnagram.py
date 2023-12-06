

def valid_anagram(s,t):
    if len(s)!=len(t):
        return False
    freq=[0]*26
    for i in range(len(s)):
        freq[ord(s[i])-ord('a')]+=1
        freq[ord(t[i])-ord('a')]-=1
    for i in freq:
        if i!=0:
            return False
    return True
s=input()
t=input()
print(valid_anagram(s,t))