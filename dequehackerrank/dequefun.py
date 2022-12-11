from collections import deque
d=deque()
n=int(input())
for _ in range(n):
    lst=input().strip()
    if lst[0]=='append':
        d.append(int(lst[1]))
    elif lst[0]=='appendleft':
        d.appendleft(int(lst[1]))    
    elif lst[0]=='pop':
        d.pop()
    elif lst[0]=='popleft':
        d.popleft()
        
