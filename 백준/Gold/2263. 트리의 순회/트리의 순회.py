import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))

def sol(n: int) -> None:
    def get_root(i_s: int, i_e: int, p_s: int, p_e: int) -> None:
        if i_s > i_e or p_s > p_e:
            return
        
        root = psodrs[p_e]
        root_idx = inodrs_cache[root]
        gap = root_idx - i_s

        pre.append(root)
        get_root(i_s, root_idx-1, p_s, p_s+gap-1)
        get_root(root_idx+1, i_e, p_s+gap, p_e-1)
        

    pre = []
    inodrs = list(map(int, input().split()))
    psodrs = list(map(int, input().split()))
    inodrs_cache = [0] * (n+1)
    for i in range(n):
        inodrs_cache[inodrs[i]] = i
    get_root(0, n-1, 0, n-1)
    return pre


print(*sol(int(input())))
