import sys
input = sys.stdin.readline
from collections import deque

def solution() -> int:
    n, k = map(int, input().split())
    goals = map(int, input().split())
    dq = deque(range(1, n + 1))
    ans = 0

    for goal in goals:
        temp = 0
        while (popy := dq.popleft()) != goal:
            dq.append(popy)
            temp += 1
        ans += min(temp, n - temp)
        n -= 1

    return ans


print(solution())
