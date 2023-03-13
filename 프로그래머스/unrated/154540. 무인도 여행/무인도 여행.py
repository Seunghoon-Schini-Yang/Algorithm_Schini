def solution(maps):
    def adjs(r, c):
        if r > 0:  yield r-1, c
        if c > 0:  yield r, c-1
        if r < n-1:  yield r+1, c
        if c < m-1:  yield r, c+1

    
    n, m = len(maps), len(maps[0])
    maps = list(map(list, maps))
    answer = []

    for sr in range(n):
        for sc in range(m):
            if maps[sr][sc] == 'X':
                continue
            
            _sum = int(maps[sr][sc])
            maps[sr][sc] = 'X'
            stack = [(sr, sc)]
            while stack:
                r, c = stack.pop()
                for rr, cc in adjs(r, c):
                    if maps[rr][cc] == 'X':
                        continue
                    _sum += int(maps[rr][cc])
                    maps[rr][cc] = 'X'
                    stack.append((rr, cc))

            answer.append(_sum)


    answer.sort()
    return answer if answer else [-1]
