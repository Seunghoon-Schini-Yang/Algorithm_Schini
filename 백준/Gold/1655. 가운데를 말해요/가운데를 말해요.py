import sys
input = sys.stdin.readline
from heapq import heappush, heappop


def get_m(x):
    global ll
    if not ll:
        if x <= r[0]:
            heappush(l, -x)
        else:
            heappush(l, -heappop(r))
            heappush(r, x)
    else:
        if -l[0] <= x:
            heappush(r, x)
        else:
            heappush(r, -heappop(l))
            heappush(l, -x)
    ll ^= 1
    return str(-l[0])


if __name__ == '__main__':
    N = int(input())
    l, r = [-int(input())], []
    ll = 1
    print(-l[0])
    print('\n'.join(get_m(int(input())) for _ in range(N-1)))
