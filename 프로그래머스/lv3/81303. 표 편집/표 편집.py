def solution(n, k, cmds):
    ll = [[i-1, i+1] for i in range(n)]
    stack = []
    
    for cmd in cmds:
        if cmd[0] == 'U':
            for _ in range(int(cmd[2:])):
                k = ll[k][0]
        elif cmd[0] == 'D':
            for _ in range(int(cmd[2:])):
                k = ll[k][1]
        elif cmd == 'C':
            stack.append(k)
            if ll[k][0] != -1:
                ll[ll[k][0]][1] = ll[k][1]
            if ll[k][1] != n:
                ll[ll[k][1]][0] = ll[k][0]
            k = ll[k][0] if ll[k][1] == n else ll[k][1]
        else:
            c = stack.pop()
            if ll[c][0] != -1:
                ll[ll[c][0]][1] = c
            if ll[c][1] != n:
                ll[ll[c][1]][0] = c
    
    while ll[k][0] != -1:
        k = ll[k][0]
    linked = [False] * n
    while k != n:
        linked[k] = True
        k = ll[k][1]
    return ''.join('O' if linked[i] else 'X' for i in range(n))
