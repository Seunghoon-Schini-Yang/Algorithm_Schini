from collections import deque
n = int(input())
answer = [0] * n
answer[0] = 1
dq = deque([(i, cursor) for i, cursor in enumerate(map(int, input().split()), start=1)])
for i in range(1, n):
    idx, cursor = dq.popleft()
    if cursor > 0:
        for _ in range(cursor-1):
            dq.append(dq.popleft())
    else:
        for _ in range(-cursor):
            dq.appendleft(dq.pop())
    answer[i] = dq[0][0]
print(*answer)