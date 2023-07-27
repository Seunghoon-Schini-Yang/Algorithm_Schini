import sys
input = sys.stdin.readline
from heapq import heappush, heappop


class Railway():
    def __init__(self, n):
        hos = [(0, 0) for _ in range(n)]
        for i in range(n):
            home, office = map(int, input().split())
            hos[i] = (home, office) if home < office else (office, home)
        L = lim = int(input())
        hos = [(home, office) for home, office in hos if office-home <= L]
        hos.sort(key=lambda x: x[1])
        pq = []
        maxy = 0
        for home, office in hos:
            if L < office-home:
                continue
            lim = office
            while pq and pq[0] < lim-L:
                heappop(pq)
            heappush(pq, home)
            maxy = max(maxy, len(pq))
        self.answer = maxy

        
if __name__ == '__main__':
    rail = Railway(int(input()))
    print(rail.answer)
