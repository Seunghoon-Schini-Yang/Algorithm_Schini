# dfs (recursive)
import sys
input = sys.stdin.readline


def get_coords() -> None:
    for r in range(n):
        for c in range(n):
            if village[r][c] == 1:
                home.append((r, c))
            elif village[r][c] == 2:
                chicken.append((r, c))
    return


def get_dist() -> None:
    for h in range(h_len):
        hr, hc = home[h]
        for c in range(c_len):
            cr, cc = chicken[c]
            distance[h][c] = abs(hr-cr)+abs(hc-cc)
    return


def get_min_dist(min_arr: int, depth: int, idx: int):
    if depth == m:
        global miny
        cur_sum = sum(min_arr)
        if cur_sum < miny:
            miny = cur_sum
        return
    
    for c_i in range(idx, c_len):
        replica = min_arr.copy()
        for h_i in range(h_len):
            if distance[h_i][c_i] < replica[h_i]:
                replica[h_i] = distance[h_i][c_i]
        get_min_dist(replica, depth+1, c_i+1)
    return


if __name__ == '__main__':
    n,m = map(int, input().split())
    village = [list(map(int, input().split())) for _ in range(n)]
    home = list(); chicken = list()
    get_coords()

    h_len = len(home); c_len = len(chicken)
    distance = [[0]*c_len for _ in range(h_len)]
    get_dist()

    miny = pow(10, 9)
    get_min_dist([miny]*h_len, 0, 0)
    print(miny)
