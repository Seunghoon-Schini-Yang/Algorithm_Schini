def sol(n: int) -> int:
    rooms = map(int, input().split())
    p, vp = map(int, input().split())
    return n + sum((max(room-p, 0)+vp-1) // vp for room in rooms)


print(sol(int(input())))
