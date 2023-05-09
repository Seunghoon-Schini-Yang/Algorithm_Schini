import sys
input = sys.stdin.readline


def _get(l, r):
    l += N-1; r += N-1
    _max = 0
    while l < r:
        if l&1:
            _max += tree[l]
            l += 1
        if r&1:
            r ^= 1
            _max += tree[r]
        l >>= 1; r >>= 1
    return _max


def _update(node, val):
    node += N-1
    while node:
        tree[node] += val
        node >>= 1
    return


if __name__ == '__main__':
    N, C = map(int, input().split())
    M = int(input())
    ts = [tuple(map(int, input().split())) for _ in range(M)]
    ts.sort(key=lambda x: (x[1], x[0]))
    
    tree = [0] * (N<<1)
    for s, r, v in ts:
        _max = _get(s, r)
        if C <= _max:  continue
        free = C - _max
        v = min(C, v)
        _update(r-1, min(v, free))
    print(_get(1, N))
