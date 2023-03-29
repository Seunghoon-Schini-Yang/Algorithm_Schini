import sys
input = sys.stdin.readline


def main():
    N = int(input())
    res = maxy = miny = 0
    for _ in range(N):
        trans, rres = map(int, input().split())
        if res + trans < 0:
            load = rres - trans - res
            maxy = gcd(maxy, load)
            miny = max(miny, rres)
            if maxy <= miny:
                print(-1)
                return
        elif rres - trans != res:
            print(-1)
            return
        res = rres
    print(maxy if maxy else 1)


def gcd(x, y):
    if not x:
        return y
    
    while x % y:
        x, y = y, x % y
    return y


if __name__ == '__main__':
    main()
