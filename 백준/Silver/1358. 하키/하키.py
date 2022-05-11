import sys
input = sys.stdin.readline


def sol(w: int, h: int, x: int, y: int, p: int) -> int:
    cnt = 0
    for _ in range(p):
        r = h // 2
        px, py = map(int, input().split())
        if px < x-r or px > x+w+r or py < y or py > y+h:
            continue
        if x <= px <= x+w:
            cnt += 1
        elif px < x and (px-x)**2 + (py-y-r)**2 <= r**2 or px > x+w and (px-x-w)**2 + (py-y-r)**2 <= r**2:
            cnt += 1

    return cnt


print(sol(*map(int, input().split())))
