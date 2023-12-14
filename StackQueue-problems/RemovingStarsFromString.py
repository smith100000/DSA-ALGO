

def remove_stars(s):
    l=[]
    for i in s:
        if i=="*":
            l.pop()
        else:
            l.append(i)
    return "".join(l)


s=input()
print(remove_stars(s))