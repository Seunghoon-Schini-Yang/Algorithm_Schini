def solution(board, skills):
    n, m = len(board), len(board[0])

    que = []
    for type, x1, y1, x2, y2, dgr in skills:
        dgr = dgr if type==2 else -dgr
        que.append([x1, y1, y2, dgr])
        que.append([x2+1, y1, y2, -dgr])
    que.sort(key=lambda x: x[0], reverse=True)
    del skills

    segtree = [0] * (m<<1)
    cur_state = [0] * m
    answer = 0

    for i in range(n):
        is_updated = False
        while que and que[-1][0] == i:
            _, y1, y2, dgr = que.pop()
            segtree = update_tree(segtree, y1+m, y2+m+1, dgr)
            is_updated = True
        
        if is_updated:
            cur_state = [get_tree(segtree, j+m) for j in range(m)]

        answer += sum( 1 if bval+tval > 0 else 0 for bval, tval in zip(board[i], cur_state) )
    return answer


def get_tree(tree, idx):
    cur = 0
    while idx:
        cur += tree[idx]
        idx >>= 1
    return cur


def update_tree(tree, s, e, val):
    while s < e:
        if s & 1:
            tree[s] += val
            s += 1
        if e & 1:
            e ^= 1
            tree[e] += val
        s >>= 1; e >>= 1
    return tree
