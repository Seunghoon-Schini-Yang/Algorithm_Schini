import sys
from heapq import heapify, heappop, heappush


class SteppingStones():
    def __init__(self, stones, k):
        answer = sys.maxsize
        stones = [(-stone, i) for i, stone in enumerate(stones)]
        pq = stones[:(k-1)]
        heapify(pq)
        for i in range(k-1, len(stones)):
            heappush(pq, stones[i])
            while pq and pq[0][1] + k <= i:
                heappop(pq)
            answer = min(answer, -pq[0][0])
        self.answer = answer


def solution(stones, k):
    step_stones = SteppingStones(stones, k)
    return step_stones.answer