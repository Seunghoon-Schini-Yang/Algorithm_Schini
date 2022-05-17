def sol(n: int, k: int) -> int:
    def factorcount(s: int, div: int) -> int:
        cur_div = div
        start = end = cnt = 0
        while not start or end:
            start = s % cur_div
            if not start:
                cnt += 1
            end = (start+gap)//cur_div
            cnt += end
            cur_div *= div
        return cnt
    
    
    k = min(n-k, k); gap = k-1
    return min(factorcount(n-k+1, 2)-factorcount(1, 2), factorcount(n-k+1, 5)-factorcount(1, 5))


print(sol(*map(int, input().split())))
