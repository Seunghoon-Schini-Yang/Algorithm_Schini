# my
import sys
input = sys.stdin.readline

def sol(v: int) -> int:
    maxy = -sys.maxsize
    tree = [{} for _ in range(v+1)]
    dp = [[] for _ in range(v+1)]
    q = []
    for _ in range(v):
        line = map(int, input().split())
        p_n = next(line)
        cnt = 0
        while (c_n := next(line)) != -1:
            tree[p_n][c_n] = next(line)
            cnt += 1
        if cnt == 1:
            q.append(p_n)

    for _ in range(v-1):
        p_n = q.pop()
        c_n,_ = tree[p_n].popitem()
        w = tree[c_n].pop(p_n)

        if not tree[c_n]:
            return max(maxy,w)
        
        dp[c_n].append(w)
        if len(tree[c_n]) == 1:
            if len(dp[c_n]) > 1:
                temp = sum(sorted(dp[c_n])[-2:])
                if maxy < temp:
                    maxy = temp
            for key in tree[c_n]:
                cc_n = key
            temp = max(dp[c_n])
            tree[cc_n][c_n] += temp
            tree[c_n][cc_n] += temp
            q.append(c_n)


print(sol(int(input())))
