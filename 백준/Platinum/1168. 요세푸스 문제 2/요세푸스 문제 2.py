def get_kth(s: int, rem: int) -> int:
    if rem == seg_tree[s]:
        return down_del_tree(s, rem)
    rem -= seg_tree[s]
    
    while s:
        if not s&1:
            if rem > seg_tree[s^1]:
                rem -= seg_tree[s^1]
            else:
                return down_del_tree(s^1, rem)
        s >>= 1

    s = start
    rem -= seg_tree[s]
    if not rem:
        seg_tree[s] = 0
        return s-N+1
    
    while s:
        
        if not s&1:
            if rem > seg_tree[s^1]:
                rem -= seg_tree[s^1]
            else:
                return down_del_tree(s^1, rem)
        s >>= 1


def down_del_tree(x: int, rem: int) -> int:
    while x<<1 < N*2:
        x <<= 1
        if rem > seg_tree[x]:
            rem -= seg_tree[x]
            x ^= 1

    kth = x
    while x:
        seg_tree[x] -= 1
        x >>= 1
    return kth-N+1


if __name__ == '__main__':
    N,K = map(int, input().split())
    seg_tree = [0]*N + [1]*N
    for i in range(N-1, 0, -1):
        seg_tree[i] = seg_tree[i<<1] + seg_tree[(i<<1)^1]
    
    start = 1
    while start < N:
        start <<= 1
    
    josephus = [0]*(N+1)
    for i in range(N):
        rem = K%(N-i) if K%(N-i) else N-i
        josephus[i+1] = get_kth(N if josephus[i]==N else josephus[i]+N, rem)
    print('<'+', '.join(map(str, josephus[1:]))+'>')