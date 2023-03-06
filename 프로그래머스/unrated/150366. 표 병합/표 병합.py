def solution(commands):
    def union(r1, c1, r2, c2):
        if ps[r1][c1] > ps[r2][c2]:
            ps[r1][c1] = (r2, c2)
            update(r1, c1, default)
            cs[(r2, c2)].extend(cs[(r1, c1)])
            cs[((r1, c1))] = [(r1, c1)]
            return r2, c2
        else:
            if ps[r1][c1] == ps[r2][c2]:
                ps[r1][c1] -= 1
            ps[r2][c2] = (r1, c1)
            update(r2, c2, default)
            cs[(r1, c1)].extend(cs[(r2, c2)])
            cs[((r2, c2))] = [(r2, c2)]
            return r1, c1
    

    def find(r, c):
        if isinstance(ps[r][c], int):
            return r, c
        ps[r][c] = find(*ps[r][c])
        return ps[r][c]
    

    def update(r, c, value):
        # r, c = find(r, c)
        mapping[board[r][c]].remove((r, c))
        tmp = mapping.get(value, set())
        tmp.add((r, c))
        mapping[value] = tmp
        board[r][c] = value


    def replace(bef, af):
        rcs = mapping.pop(bef, set())
        if not rcs:
            return
        mapping[af] = mapping.get(af, set()).union(rcs)
        for r, c in rcs:
            board[r][c] = af

    
    def merge(r1, c1, r2, c2):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)
        if (r1, c1) == (r2, c2):
            return
        value = board[r2][c2] if not board[r1][c1] else board[r1][c1]
        update(*union(r1, c1, r2, c2), value)


    def unmerge(r, c):
        _r, _c = r, c
        r, c = find(r, c)
        value = board[r][c]
        update(r, c, default)
        for rr, cc in cs[(r, c)]:
            ps[rr][cc] = -1
        cs[(r, c)] = [(r, c)]
        update(_r, _c, value)


    answer = []
    default = ''
    board = [[default] * 51 for _ in range(51)]
    mapping = {default: {(r, c) for r in range(51) for c in range(51)}}
    ps = [[-1] * 51 for _ in range(51)]
    cs = {(r, c): [(r, c)] for r in range(51) for c in range(51)}
    
    for command in commands:
        _type, *_command = command.split()
        if _type == 'UPDATE':
            if len(_command) == 3:
                r, c = find(*map(int, _command[:2]))
                update(r, c, _command[-1])
            else:
                replace(*_command)
        elif _type == 'MERGE':
            merge(*map(int, _command))
        elif _type == 'UNMERGE':
            unmerge(*map(int, _command))
        else:
            r, c = find(*map(int, _command))
            answer.append(board[r][c] if board[r][c] else 'EMPTY')
    
    return answer
