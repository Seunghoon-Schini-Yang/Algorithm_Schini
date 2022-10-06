# bitmask dp
cnt = 0


def solution(k: int, dungeons: list) -> int:
    def dfs(k: int, mask: int, depth: int) -> None:
        global cnt
        cnt = max(cnt, depth)

        for i in range(n):
            if mask & (1<<i):
                continue
            if memo[mask|(1<<i)]:
                continue
            if k < dungeons[i][0]:
                continue
            
            memo[mask|(1<<i)] = True
            dfs(k-dungeons[i][1], mask|(1<<i), depth+1)

        return

    
    n = len(dungeons)
    memo = [False] * (1<<n)

    dfs(k, 0, 0)
    return cnt
