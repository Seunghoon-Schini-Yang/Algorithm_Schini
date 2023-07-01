dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def bfs(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == "P":
                v = [[False]*5 for _ in range(5)]
                v[r][c] = True
                q = [(r, c)]
                for _ in range(2):
                    tmp = []
                    for r, c in q:
                        for i in range(4):
                            rr, cc = r+dr[i], c+dc[i]
                            if 0 <= rr < 5 and 0 <= cc < 5:
                                if place[rr][cc] == 'X' or v[rr][cc]:
                                    continue
                                if place[rr][cc] == 'P':
                                    return 0
                                tmp.append((rr, cc))
                                v[rr][cc] = True
                    q = tmp    
    return 1


def solution(places):
    return [bfs(place) for place in places]
