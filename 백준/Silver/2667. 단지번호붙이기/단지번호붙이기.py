import sys
input = sys.stdin.readline

def sol(n: int) -> list:
    locs = [input().rstrip() for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    ans = list()

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and locs[i][j] == '1':
                cnt = 0
                stack = [(i,j)]
                while stack:
                    c_i, c_j = stack.pop()
                    if not visited[c_i][c_j] and locs[c_i][c_j] == '1':
                        cnt += 1
                        visited[c_i][c_j] = 1
                        if c_i > 0:
                            stack.append((c_i-1, c_j))
                        if c_i < n-1:
                            stack.append((c_i+1, c_j))
                        if c_j > 0:
                            stack.append((c_i, c_j-1))
                        if c_j < n-1:
                            stack.append((c_i, c_j+1))
                ans.append(cnt)

    ans.sort()
    print(len(ans))
    for num in ans:
        print(num)


sol(int(input()))
