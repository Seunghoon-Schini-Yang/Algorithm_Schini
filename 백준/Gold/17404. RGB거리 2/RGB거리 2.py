import sys
input = sys.stdin.readline


def main(N):
    INF = (N+1) * 1000
    R, G, B  = map(int, input().split())
    R2, G2, B2  = map(int, input().split())
    rr = gg = bb = INF
    rb, rg, gr, gb, br, bg =\
        R+B2, R+G2, G+R2, G+B2, B+R2, B+G2
    for _ in range(N-2):
        R, G, B = map(int, input().split())
        rr, rg, rb, gr, gg, gb, br, bg, bb =\
        min(rg, rb) + R, min(rr, rb) + G, min(rr, rg) + B,\
        min(gg, gb) + R, min(gr, gb) + G, min(gr, gg) + B,\
        min(bg, bb) + R, min(br, bb) + G, min(br, bg) + B
    return min(rg, rb, gr, gb, br, bg)


if __name__ == '__main__':
    lowest_cost = main(int(input()))
    print(lowest_cost)
