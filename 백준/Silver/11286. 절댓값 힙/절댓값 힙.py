from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def solution(n: int) -> str:
    answer = []
    prior_q = []
    dd = {}
    for _ in range(n):
        if (num := int(input())):
            if num < 0:
                dd[num] = dd.get((num := -num), 0) + 1
            heappush(prior_q, num)
        else:
            if prior_q:
                if dd.get((num := heappop(prior_q)), 0):
                    answer.append(-num)
                    dd[num] -= 1
                else:
                    answer.append(num)
            else:
                answer.append(0)
    
    return '\n'.join(map(str, answer))


print(solution(int(input())))