import sys
input = sys.stdin.readline


def sol(n: int) -> None:
    s = set()
    # s_rm = s.discard; s_add = s.add
    # s_clr = s.clear; s_update = s.update
    for _ in range(n):
        query = input().split()
        
        if query[0][0] == 'a':
            if query[0][1] == 'd':
                s.add(int(query[1]))
            else:
                s.clear(); s.update(range(1, 21))
        elif query[0][0] == 'r':
            s.discard(int(query[1]))
        elif query[0][0] == 'c':
            print(1 if int(query[1]) in s else 0)
        elif query[0][0] == 't':
            x = int(query[1])
            s.discard(x) if x in s else s.add(x)
        else:
            s.clear()


sol(int(input()))
