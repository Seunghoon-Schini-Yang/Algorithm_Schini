from collections import deque


def solution(rc, operations):
    R, C = len(rc), len(rc[0])
    ul, ur, dl, dr = rc[0][0], rc[0][-1], rc[-1][0], rc[-1][-1]
    u, d = deque(rc[0][1:-1]), deque(rc[-1][1:-1])
    l, r = deque([rc[i][0] for i in range(1, R-1)]), deque([rc[i][-1] for i in range(1, R-1)])
    box = deque([deque(r[1:-1]) for r in rc[1:-1]])
    for oper in operations:
        if oper == 'Rotate':
            u.appendleft(ul)
            l.append(dl)
            d.append(dr)
            r.appendleft(ur)
            ul = l.popleft()
            dl = d.popleft()
            dr = r.pop()
            ur = u.pop()
        else:
            l.appendleft(ul)
            ul = dl
            dl = l.pop()

            box.appendleft(u)
            u = d
            d = box.pop()

            r.appendleft(ur)
            ur = dr
            dr = r.pop()
    
    rc = [[ul] + list(u) + [ur]]
    for _ in range(R-2):
        rc.append([l.popleft()] + list(box.popleft()) + [r.popleft()])
    rc.append([dl] + list(d) + [dr])
    return rc
