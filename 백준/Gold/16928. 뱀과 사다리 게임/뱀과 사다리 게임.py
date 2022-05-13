import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    visited = [0] * 100
    warp = dict()
    for _ in range(n):
        s,e = map(int, input().split())
        warp[s] = e

    cnt = 1
    que = [1]
    while que:
        temp = list()

        for p_loc in que:
            for c_loc in range(p_loc+1, p_loc+7):
                if c_loc == 100:
                    return cnt
                
                if not visited[c_loc]:
                    visited[c_loc] = 1

                    if warp.get(c_loc, 0):
                        visited[warp[c_loc]] = 1
                        temp.append(warp[c_loc])
                    else:
                        temp.append(c_loc)

        que = temp; cnt += 1


print(sol(sum(map(int, input().split()))))
