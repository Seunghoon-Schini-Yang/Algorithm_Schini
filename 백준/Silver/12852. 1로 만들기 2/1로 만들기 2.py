from collections import deque

def sol(n: int):
    dp = [1]*(n+1)
    dp[1] = 0
    q = deque([[1]])
    while q:
        for _ in range(len(q)):
            x = q.popleft()
            if x[-1] == n:
                print(len(x)-1)
                print(*reversed(x))
                return
            if dp[x[-1]+1]:
                dp[x[-1]+1] = 0
                q.append(x+[x[-1]+1])
            if x[-1]*2 <= n and dp[x[-1]*2]:
                dp[x[-1]*2] = 0
                q.append(x+[x[-1]*2])
            if x[-1]*3 <= n and dp[x[-1]*3]:
                dp[x[-1]*3] = 0
                q.append(x+[x[-1]*3])


sol(int(input()))
