import heapq
import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    prior_q = []
    heapq.heapify(prior_q)
    for _ in range(n):
        if (num := input())[0] == '0':
            print(heapq.heappop(prior_q) if prior_q else 0)
        else:
            heapq.heappush(prior_q, int(num))


solution(int(input()))
