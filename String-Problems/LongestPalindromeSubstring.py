

def check_palindrome(s,i,j):
    while(i>=0 and j<len(s) and s[i]==s[j]):
        i-=1
        j+=1
    return s[i+1:j]

def longest_palindrome(s):
    if len(s)==0:
        return s
    ans=""
    for i in range(len(s)-1):
        odd_subarray=check_palindrome(s,i,i)
        if len(ans)<len(odd_subarray):
            ans=odd_subarray
        even_subarray=check_palindrome(s,i,i+1)
        if len(ans)<len(even_subarray):
            ans=even_subarray
    return ans

s=input()
print(longest_palindrome(s))
