def solution(m, n, sx, sy, balls):
    def dist(x, y):
        if not (sx == x and sy > y):
            yield (sy+y)**2 + (sx-x)**2
        if not (sx == x and sy < y):
            yield (n*2-sy-y)**2 + (sx-x)**2
        if not (sy == y and sx > x):
            yield (sx+x)**2 + (sy-y)**2
        if not (sy == y and sx < x):
            yield (m*2-sx-x)**2 + (sy-y)**2


    answer = [min(d for d in dist(x, y)) for x, y in balls]
    return answer
