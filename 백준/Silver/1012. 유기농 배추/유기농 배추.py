import sys
input = sys.stdin.readline

def sol(w: int, h: int, k: int) -> int:
    ans = 0
    locs = {tuple(map(int, input().split())) for _ in range(k)}
    while locs:
        stack = [locs.pop()]
        while stack:
            i, j = stack.pop()
            for x in ((i+1 ,j), (i-1, j), (i, j-1), (i, j+1)):
                check(x, locs, stack)
        ans += 1

    return ans


def check(x: tuple, locs: set, stack: list) -> None:
    if x in locs:
        locs.remove(x)
        stack.append(x)


for _ in range(int(input())):
    print(sol(*map(int, input().split())))
