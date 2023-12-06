

def valid_parenthesis(s):
    stack=[]
    pairs={
        '(':')',
        '{':'}',
        '[':']'
    }
    for i in s:
        if i not in pairs:
            stack.append(i)
        elif len(stack)==0 or i!=pairs[stack.pop()]:
            return False
    return len(stack)==0
s=input()
print(valid_parenthesis(s))