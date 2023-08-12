import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class Arr():
    def __init__(self):
        self.N, self.L = map(int, input().split())
        self.arr = map(int, input().split())
        self.pq = []
        self.mins = [self._get_min(i, x) for i, x in enumerate(self.arr)]
    
    
    def _get_min(self, i, x):
        heappush(self.pq, (x, i))
        while self.pq[0][1] <= i-self.L:
            heappop(self.pq)
        return self.pq[0][0]
        

if __name__ == '__main__':
    arr = Arr()
    print(*arr.mins)
