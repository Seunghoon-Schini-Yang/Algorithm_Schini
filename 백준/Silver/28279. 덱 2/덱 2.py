import sys
input = sys.stdin.readline
from collections import deque


def query(q):
    if q[0] == '1':
        _, d = map(int, q.split())
        dq.appendleft(d)
        return -2
    elif q[0] == '2':
        _, d = map(int, q.split())
        dq.append(d)
        return -2
    else:
        q = int(q)
        if q == 3:
            return dq.popleft() if dq else -1
        elif q == 4:
            return dq.pop() if dq else -1
        elif q == 5:
            return len(dq)
        elif q == 6:
            return 0 if dq else 1
        elif q == 7:
            return dq[0] if dq else -1
        else:
            return dq[-1] if dq else -1

        
dq = deque()
for _ in range(int(input())):
    a = query(input())
    if a != -2:
        print(a)
