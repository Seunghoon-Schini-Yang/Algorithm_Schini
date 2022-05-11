import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    directions = [0] * 5
    edges = [list(map(int, input().split())) for _ in range(6)]
    for edge in edges:
        directions[edge[0]] += 1

    once, twice = list(), list()
    for i in range(1, 5):
        if directions[i] == 1:
            once.append(i)
        else:
            twice.append(i)

    if twice[0] > twice[1]:
        t_l, t_s = twice[0], twice[1]
    else:
        t_l, t_s = twice[1], twice[0]

    if t_l-t_s == 2:
        t_l,t_s = t_s,t_l
    
    tot, par = 1, 1
    for i in range(6):
        if edges[i][0] == t_l:
            if edges[(i+1)%6][0] == t_s:
                par *= edges[i][1]*edges[(i+1)%6][1]
        elif edges[i][0] in once:
            tot *= edges[i][1]

    return (tot - par) * n


print(sol(int(input())))
