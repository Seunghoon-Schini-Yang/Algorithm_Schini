import sys
input = sys.stdin.readline


def query(q):
    if q[0] == '1':
        _, d = map(int, q.split())
        stack.append(d)
        return -2
    else:
        q = int(q)
        if q == 2:
            return stack.pop() if stack else -1
        elif q == 3:
            return len(stack)
        elif q == 4:
            return 0 if stack else 1
        else:
            return stack[-1] if stack else -1

        
stack = []
for _ in range(int(input())):
    a = query(input())
    if a != -2:
        print(a)
