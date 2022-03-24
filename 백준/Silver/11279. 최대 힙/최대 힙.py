import heapq
import sys
input = sys.stdin.readline

def solution(n: int):
    a = list()
    heapq.heapify(a)

    for _ in range(n):
        if (num := input())[0] == '0':
            try:
                print(-heapq.heappop(a))
            except IndexError:
                print(0)
        else:
            heapq.heappush(a, -int(num))


solution(int(input()))
