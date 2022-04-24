import sys
input = sys.stdin.readline
from collections import deque

def sol(a: int, b: int) -> str:
    dp = [[-1]*10000 for _ in range(2)]
    dp[0][a] = -2
    q = deque([a])

    while q:
        for _ in range(len(q)):
            cur = q.popleft()

            if cur == b:
                ans = ''
                while cur != a:
                    ans = dp[1][cur] + ans
                    cur = dp[0][cur]
                return ans
            
            D = (cur*2) % 10000
            S = cur-1 if cur else 9999
            L = cur%1000*10 + cur//1000
            R = cur%10*1000 + cur//10
            # str_cur = str(cur).rjust(4,'0')
            # L = int(str_cur[1:]+str_cur[0])
            # R = int(str_cur[-1]+str_cur[:-1])
            for x,char in (D,'D'),(S,'S'),(L,'L'),(R,'R'):
                if dp[0][x] == -1:
                    dp[0][x] = cur
                    dp[1][x] = char
                    q.append(x)


print('\n'.join(sol(*map(int, input().split())) for _ in range(int(input()))))
