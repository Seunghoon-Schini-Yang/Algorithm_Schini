import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class Farm():
    def __init__(self, N, P, K):
        graph = [[] for _ in range(N+1)]
        prices = []
        for _ in range(P):
            n1, n2 , price = map(int, input().split())
            prices.append(price)
            graph[n1].append((price, n2))
            graph[n2].append((price, n1))
        prices = [0] + sorted(set(prices))
        
        self.N = N
        self.graph = graph

        if self._dijkstra(1) == N:
            self.minimum = -1
        else:
            s, e = 0, len(prices)-1
            while s < e:
                m = (s+e)>>1
                pay = self._dijkstra(prices[m])
                if pay <= K:
                    e = m
                else:
                    s = m+1
            self.minimum = prices[e]


    def _dijkstra(self, thres):
        dist = [self.N] * (self.N+1)
        dist[1] = 0
        pq = [(0, 1)]
        while pq:
            p, n = heappop(pq)
            if dist[n] < p:
                continue
            for pp, nn in self.graph[n]:
                pp = p if pp <= thres else p+1
                if dist[nn] <= pp:
                    continue
                dist[nn] = pp
                heappush(pq, (pp, nn))
        return dist[self.N]


if __name__ == '__main__':
    farm = Farm(*map(int, input().split()))
    print(farm.minimum)
