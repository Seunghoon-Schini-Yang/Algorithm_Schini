import sys
input = sys.stdin.readline


class Beads():
    def __init__(self, N):
        maxy = sumy = 0
        for _ in range(N):
            x = int(input())
            sumy += x
            maxy = x if maxy < x else maxy
        sumy -= maxy
        self.res = maxy-sumy if sumy <= maxy else (1 if (sumy-maxy)&1 else 0)


if __name__ == '__main__':
    beads = Beads(int(input()))
    print(beads.res)
