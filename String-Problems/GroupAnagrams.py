

def group_anagrams(l):
    dict={}
    for word in l:
        sorted_word="".join(sorted(word))
        if sorted_word not in dict:
            dict[sorted_word]=[word]
        else:
            dict[sorted_word].append(word)
    ans=[]
    for i in dict.values():
        ans.append(i)
    return ans
l=list(map(str,input().split()))
print(group_anagrams(l))
