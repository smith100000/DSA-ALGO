

def print_numbers(n,l,i):
    if i==n:
        for i in l:
            print(i,end="")
        print()
        return
    l[i]=1
    print_numbers(n,l,i+1)
    l[i]=2
    print_numbers(n,l,i+1)


n=int(input())
l=[0]*n
print_numbers(n,l,0)