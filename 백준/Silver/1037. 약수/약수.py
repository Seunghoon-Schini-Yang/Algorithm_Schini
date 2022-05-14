def sol() -> int:
    miny, maxy = 1_000_000, 0
    for i in map(int, input().split()):
        miny = min(miny, i)
        maxy = max(maxy, i)
    return miny * maxy


input()
print(sol())
