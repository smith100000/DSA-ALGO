

import heapq
def max_money_earn(l):
    heap=[]
    l.sort()
    current_profit=0
    max_profit=0
    for start,finish,profit in l:
        while heap and heap[0][0]<=start:
            _,temp=heapq.heappop(heap)
            current_profit=max(current_profit,temp)
        heapq.heappush(heap,(finish,current_profit+profit))
        max_profit=max(max_profit,current_profit+profit)
    return max_profit


N=int(input())
l=[]
for i in range(N):
    l1=list(map(int,input().split()))[:3]
    l.append(l1)
print(max_money_earn(l))