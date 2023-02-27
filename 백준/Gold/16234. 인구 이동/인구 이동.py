import sys
input = sys.stdin.readline


def main():
    def adjs(r, c):
        if 0 < r:  yield r-1, c
        if 0 < c:  yield r, c-1
        if r < N-1:  yield r+1, c
        if c < N-1:  yield r, c+1

    
    N, L, R = map(int, input().split())
    popul = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    while True:
        is_visited = [[False]*N for _ in range(N)]
        is_repeat = 0

        for row in range(N):
            for col in range(N):
                if is_visited[row][col]:
                    is_repeat += 1
                    continue
                
                is_visited[row][col] = True
                stack = [(row, col)]
                cands = stack[:]
                _sum = popul[row][col]; _cnt = 1

                while stack:
                    r, c = stack.pop()
                    for rr, cc in adjs(r, c):
                        if not is_visited[rr][cc] and\
                            L <= abs(popul[r][c] - popul[rr][cc]) <= R:
                            is_visited[rr][cc] = True
                            stack.append((rr, cc))
                            cands.append((rr, cc))
                            _sum += popul[rr][cc]; _cnt += 1
                            
                _update = _sum // _cnt
                for r, c in cands:
                    popul[r][c] = _update
                
        if not is_repeat:
            break
        cnt += 1
    
    print(cnt)
    return


if __name__ == "__main__":
    main()
