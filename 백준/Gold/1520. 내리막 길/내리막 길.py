import sys
input = sys.stdin.readline

def solution(m: int, n: int) -> int:
    if m == n == 1:
        return 1
    
    alts = [[*map(int, input().split())] for _ in range(m)]
    dstn = alts[m-1][n-1]
    stack, path = [(0, 0)], list()
    dp = [[-1] * n for _ in range(m)]
    dp[m-1][n-1] = 1

    while stack:
        i, j = stack.pop()
        if (dp[i][j] != -1 or check_four(i, j, m, n, dstn, alts, stack, path, dp)) and path:
            c_i, c_j = path.pop()
            dp[c_i][c_j] += dp[i][j]
            while path and (c_i, c_j) != path[-1]:
                i, j = c_i, c_j
                c_i, c_j = path.pop()
                dp[c_i][c_j] += dp[i][j]
        else:
            dp[i][j] = 0

    return dp[0][0]


def check_four(i: int, j: int, m: int, n: int, dstn: int, alts: list, stack: list, path: list, dp:list) -> bool:
    p_alt = alts[i][j]

    a = check(i, j+1, m, n, dstn, p_alt, alts)
    b = check(i+1, j, m, n, dstn, p_alt, alts)
    c = check(i, j-1, m, n, dstn, p_alt, alts)
    d = check(i-1, j, m, n, dstn, p_alt, alts)

    if a:
        stack.append((i, j+1))
        path.append((i, j))
    if b:
        stack.append((i+1, j))
        path.append((i, j))
    if c:
        stack.append((i, j-1))
        path.append((i, j))
    if d:
        stack.append((i-1, j))
        path.append((i, j))

    if a or b or c or d:
        return False
    dp[i][j] = 0
    return True


def check(i: int, j: int, m: int, n: int, dstn: int, p_alt: int, alts: list) -> bool:
    if (i >= 0 and i < m and j >= 0 and j < n and alts[i][j] > dstn or i == m-1 and j == n-1) and p_alt > alts[i][j]:
        return True
    return False


print(solution(*map(int, input().split())))
