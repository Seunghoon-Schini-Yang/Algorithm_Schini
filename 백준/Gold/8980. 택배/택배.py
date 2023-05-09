import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, C = map(int, input().split())
    M = int(input())
    ts = [tuple(map(int, input().split())) for _ in range(M)]
    ts.sort(key=lambda x: x[1])
    
    tree = [0] * N
    ans = 0
    for s, r, v in ts:
        _max = max(tree[s-1:r])
        if _max == C:  continue
        free = C - _max
        load = min(free, v)
        ans += load
        for i in range(s-1, r):
            tree[i] += load
    print(ans)
