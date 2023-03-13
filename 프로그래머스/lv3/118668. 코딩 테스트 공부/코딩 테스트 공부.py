from heapq import heappop, heappush


def solution(alp, cop, problems):
    n = max(map(lambda x: x[0], problems))
    m = max(map(lambda x: x[1], problems))
    memo = [[m+n for _ in range(m+1)] for _ in range(n+1)]

    alp = alp if alp <= n else n
    cop = cop if cop <= m else m
    stack = [(0, alp, cop)]
    while stack:
        cost, r, c = heappop(stack)
        if memo[r][c] < cost:
            continue
        memo[r][c] = cost

        if memo[r][c] + (n-r + m-c) < memo[n][m]:
            memo[n][m] = memo[r][c] + (n-r + m-c)

        for problem in problems:
            if problem[0] <= r and problem[1] <= c:
                rr = r + problem[2]
                cc = c + problem[3]
                cost = problem[4]
            else:
                cost = 0
                rr = r
                if r < problem[0]:
                    rr = problem[0]
                    cost += rr - r
                cc = c
                if c < problem[1]:
                    cc = problem[1]
                    cost += cc - c

            rr = rr if rr <= n else n
            cc = cc if cc <= m else m

            if memo[rr][cc] <= memo[r][c] + cost:
                continue
            memo[rr][cc] = memo[r][c] + cost

            if rr == n and cc == m:
                continue
            heappush(stack, (memo[r][c]+cost, rr, cc))

    return memo[n][m]
