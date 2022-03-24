import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    prior_q = list()
    dd = defaultdict(int)
    for _ in range(n):
        if (num := int(input())):
            if num < 0:
                dd[(num := abs(num))] += 1
            heapq.heappush(prior_q, num)
        else:
            if prior_q:
                if dd[(num := heapq.heappop(prior_q))]:
                    print(-num)
                    dd[num] -= 1
                else:
                    print(num)
            else:
                print(0)


solution(int(input()))
