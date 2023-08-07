import sys
input = sys.stdin.readline
from heapq import heappop, heappush


class TestSet():
    def __init__(self, N):
        qs = [tuple(map(int, input().split())) for _ in range(N)]
        qs.sort(key=lambda x: -x[0])
        pq = []
        i = ramen = 0
        for thres in range(N, 0, -1):
            while i < N and qs[i][0] == thres:
                heappush(pq, -qs[i][1])
                i += 1
            if pq:
                ramen += heappop(pq)
        self.answer = -ramen
        
        
if __name__ == '__main__':
    testset = TestSet(int(input()))
    print(testset.answer)
