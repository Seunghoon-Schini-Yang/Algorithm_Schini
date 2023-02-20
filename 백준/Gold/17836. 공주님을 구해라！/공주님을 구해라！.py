import sys
input = sys.stdin.readline


def main():
    N, M, T = map(int, input().split())
    castle = [list(map(int, input().split())) for _ in range(N)]
    is_visited = [[False]*M for _ in range(N)]
    is_visited[0][0] = True

    cnt = 0; warp = N * M
    cands = [(0,0)]
    while cands:
        cnt += 1
        tmp = []
        for loc in cands:
            for cx, cy in adjs(*loc):
                if cx < 0 or cx >= N or cy < 0 or cy >= M or is_visited[cx][cy] or castle[cx][cy] == 1:
                    continue
                if cx == N-1 and cy == M-1:
                    return min(cnt, warp)
                
                is_visited[cx][cy] = True
                if not castle[cx][cy]:
                    tmp.append((cx, cy))
                else:
                    warp = cnt + N + M - cx - cy - 2
        
        if cnt == T:
            break
        cands = tmp

    return warp if warp <= T and warp < N * M else "Fail"
                

def adjs(x, y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1


if __name__ == "__main__":
    print(main())
