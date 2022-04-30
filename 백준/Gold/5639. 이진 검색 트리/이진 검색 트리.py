import sys
input = sys.stdin.readlines
sys.setrecursionlimit(pow(10,9))

def sol(lines: str) -> list:
    def get_post(s: int, e: int) -> None:
        if s > e:
            return
        
        root = pre[s]
        larger = e+1
        for i in range(s+1,e+1):
            if pre[i] > root:
                larger = i
                break
        
        get_post(s+1, larger-1)
        get_post(larger, e)
        post.append(root)


    pre = list(map(int, lines))
    n = len(pre)
    post = []
    get_post(0, n-1)
    return post


print(*sol(input()))
