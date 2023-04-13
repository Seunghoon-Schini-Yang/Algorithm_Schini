import sys
input = sys.stdin.readline


def main():
    N = int(input())
    x, y = map(int, input().split())
    l, r, u, d = x, x, y, y
    for _ in range(N-1):
        x, y = map(int, input().split())
        if x < l:
            l = x
        elif r < x:
            r = x
        if y < d:
            d = y
        elif u < y:
            u = y   
    return (u-d) * (r-l)


if __name__ == '__main__':
    area = main()
    print(area)
        