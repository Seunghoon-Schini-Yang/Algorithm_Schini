import sys
input = sys.stdin.readline


def adjs(r: int, c: int) -> tuple:
    yield r-1, c
    yield r-1, c+1
    yield r, c+1
    yield r+1, c+1
    yield r+1, c
    yield r+1, c-1
    yield r, c-1
    yield r-1, c-1


def spring_summer_winter():
    reprod = list()
    for r in range(n):
        for c in range(n):
            is_insufficient = False
            to_add = for_autumn = 0
            grown = dict()
            for age in sorted(trees[r][c]):
                if is_insufficient:
                    to_add += (age>>1)*(trees[r][c].pop(age))
                else:
                    cnt = trees[r][c][age]
                    limit = neuts[r][c]//age
                    if cnt <= limit:
                        neuts[r][c] -= age*(trees[r][c].pop(age))
                        grown[age+1] = cnt
                        if not (age+1)%5:
                            for_autumn += cnt
                    else:
                        if limit:
                            neuts[r][c] -= age*limit
                            trees[r][c][age] -= limit
                            grown[age+1] = limit
                            if not (age+1)%5:
                                for_autumn += limit
                        to_add += (age>>1)*(trees[r][c].pop(age))
                        is_insufficient = True
            
            trees[r][c] = grown
            neuts[r][c] += to_add+a[r][c]
            if for_autumn:
                reprod.append((r,c,for_autumn))
    return reprod


if __name__ == '__main__':
    n, m ,k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    neuts = [[5]*n for _ in range(n)]
    trees = [[dict() for _ in range(n)] for _ in range(n)]
    for i in range(m):
        r,c,age = map(int, input().split())
        trees[r-1][c-1][age] = 1

    for _ in range(k):
        for r,c,cnt in spring_summer_winter():
            for nr, nc in adjs(r, c):
                if 0<=nr<n and 0<=nc<n:
                    trees[nr][nc][1] = trees[nr][nc].get(1, 0) + cnt


    print(sum(sum(trees[r][c].values()) for r in range(n) for c in range(n)))
