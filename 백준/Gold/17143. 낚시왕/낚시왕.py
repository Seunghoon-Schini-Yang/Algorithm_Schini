import sys
input = sys.stdin.readline


if __name__ == '__main__':
    tot_z = 0
    R,C,M = map(int, input().split())
    sharks = {c:dict() for c in range(C)}

    for _ in range(M):
        r,c,s,d,z = map(int, input().split())
        if d == 1 or d == 2:
            s %= (R-1)*2
        else:
            s %= (C-1)*2
        sharks[c-1][r-1] = (s,d,z)
    
    for cc in range(C):
        if sharks[cc]:
            tot_z += sharks[cc].pop(min(sharks[cc]))[2]
        
        tmp = {c:dict() for c in range(C)}
        for c, c_dict in sharks.items():
            for r, (s,d,z) in c_dict.items():
                nc = c; nr = r

                if d == 1:
                    nr -= s
                    if nr < 0:
                        d = 2
                        nr *= -1
                        if nr >= R:
                            d = 1
                            nr = (R-1)*2 - nr
                elif d == 2:
                    nr += s
                    if nr >= R:
                        d = 1
                        nr = (R-1)*2 - nr
                        if nr < 0:
                            d = 2
                            nr *= -1
                elif d == 3:
                    nc += s
                    if nc >= C:
                        d = 4
                        nc = (C-1)*2 - nc
                        if nc < 0:
                            d = 3
                            nc *= -1
                else:
                    nc -= s
                    if nc < 0:
                        d = 3
                        nc *= -1
                        if nc >= C:
                            d = 4
                            nc = (C-1)*2 - nc

                is_exist = tmp[nc].get(nr, False)
                if is_exist and z < is_exist[2]:
                    continue
                tmp[nc][nr] = (s,d,z)
        sharks = tmp

    print(tot_z)
