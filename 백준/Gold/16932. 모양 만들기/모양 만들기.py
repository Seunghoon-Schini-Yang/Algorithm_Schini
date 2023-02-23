import sys
input = sys.stdin.readline


def main():
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    memo = [[0]*M for _ in range(N)]
    sizes = [0]


    def adjs(r, c):
        if r < N-1:  yield r+1, c
        if c < M-1:  yield r, c+1
        if r:  yield r-1, c
        if c:  yield r, c-1


    def dfs(row, col, grp):
        cnt = 1
        stack = [(row, col)]
        while stack:
            r, c = stack.pop()
            for cr, cc in adjs(r, c):
                if memo[cr][cc] or not arr[cr][cc]:
                    continue
                memo[cr][cc] = grp
                cnt += 1
                stack.append((cr, cc))
        sizes.append(cnt)
        return


    grp = 0
    for row in range(N):
        for col in range(M):
            if memo[row][col] or not arr[row][col]:
                continue
            grp += 1
            memo[row][col] = grp
            dfs(row, col, grp)

    answer = 0
    for row in range(N):
        for col in range(M):
            if memo[row][col]:
                continue
            
            cands = set()
            for r, c in adjs(row, col):
                if not memo[r][c]:
                    continue
                cands.add(memo[r][c])
            answer = max(answer, 1 + sum(sizes[cand] for cand in cands))
    
    print(answer)
    return


if __name__ == "__main__":
    main()
