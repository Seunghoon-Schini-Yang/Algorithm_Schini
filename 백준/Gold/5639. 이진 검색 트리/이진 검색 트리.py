import sys
input = sys.stdin.readlines
sys.setrecursionlimit(pow(10,9))

def sol(lines: str) -> list:
    def get_post(s: int, e: int) -> None:
        if s > e:
            return []
        
        root = pre[s]
        larger = e+1
        for i in range(s+1,e+1):
            if pre[i] > root:
                larger = i
                break
        

        return get_post(s+1, larger-1) + get_post(larger, e) + [root]


    pre = list(map(int, lines))
    n = len(pre)
    return get_post(0, n-1)


print(*sol(input()))
