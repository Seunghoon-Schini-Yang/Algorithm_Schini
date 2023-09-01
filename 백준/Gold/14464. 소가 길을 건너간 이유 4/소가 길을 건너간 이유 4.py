import sys
input = sys.stdin.readline
from heapq import heappush, heappop


class Farm():
    def __init__(self, C, N):
        stocks = [(int(input()),) for _ in range(C)] + [tuple(map(int, input().split())) for _ in range(N)]
        stocks.sort(key=lambda x: (x[0], -len(x)))
        pq = []
        pairs = 0
        for ls in stocks:
            if len(ls) == 2:
                heappush(pq, ls[1])
            else:
                while pq and pq[0] < ls[0]:
                    heappop(pq)
                if pq:
                    heappop(pq)
                    pairs += 1
        self.pairs = pairs


if __name__ == '__main__':
    farm = Farm(*map(int, input().split()))
    print(farm.pairs)
